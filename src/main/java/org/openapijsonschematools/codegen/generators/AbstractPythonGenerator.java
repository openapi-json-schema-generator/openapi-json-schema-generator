/*
 * Copyright 2018 OpenAPI-Generator Contributors (https://openapi-generator.tech)
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     https://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package org.openapijsonschematools.codegen.generators;

import com.github.curiousoddman.rgxgen.RgxGen;
import io.swagger.v3.oas.models.media.ArraySchema;
import io.swagger.v3.oas.models.media.Schema;
import org.apache.commons.io.FilenameUtils;
import org.apache.commons.lang3.StringUtils;
import org.openapijsonschematools.codegen.common.CodegenConstants;
import org.openapijsonschematools.codegen.common.ModelUtils;
import org.openapijsonschematools.codegen.generators.generatormetadata.GeneratorLanguage;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.io.File;
import java.io.IOException;
import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.stream.Collectors;

import static org.openapijsonschematools.codegen.common.StringUtils.camelize;
import static org.openapijsonschematools.codegen.common.StringUtils.underscore;

public abstract class AbstractPythonGenerator extends DefaultGenerator implements Generator {
    private final Logger LOGGER = LoggerFactory.getLogger(AbstractPythonGenerator.class);

    protected String packageVersion = "1.0.0";
    protected String projectName; // for setup.py, e.g. petstore-api

    public AbstractPythonGenerator() {
        super();

        packageName = "openapi_client";

        // from https://docs.python.org/3/reference/lexical_analysis.html#keywords
        setReservedWordsLowerCase(
                Arrays.asList(
                        // local variable name used in API methods (endpoints)
                        "all_params", "resource_path", "path_params", "query_params",
                        "header_params", "form_params", "local_var_files", "body_params", "auth_settings",
                        // @property
                        "property",
                        // python reserved words
                        "and", "del", "from", "not", "while", "as", "elif", "global", "or", "with",
                        "assert", "else", "if", "pass", "yield", "break", "except", "import",
                        "print", "class", "exec", "in", "raise", "continue", "finally", "is",
                        "return", "def", "for", "lambda", "try", "self", "nonlocal", "None", "True",
                        "False", "async", "await",
                        // imports, imports_schema_types.handlebars, include these to prevent name collision
                        "datetime", "decimal", "functools", "io", "re",
                        "typing", "typing_extensions", "uuid", "immutabledict", "schemas"
                ));

        languageSpecificPrimitives.clear();
        languageSpecificPrimitives.add("int");
        languageSpecificPrimitives.add("float");
        languageSpecificPrimitives.add("list");
        languageSpecificPrimitives.add("dict");
        languageSpecificPrimitives.add("bool");
        languageSpecificPrimitives.add("str");
        languageSpecificPrimitives.add("datetime");
        languageSpecificPrimitives.add("date");
        languageSpecificPrimitives.add("object");
        // TODO file and binary is mapped as `file`
        languageSpecificPrimitives.add("file");
        languageSpecificPrimitives.add("bytes");

        typeMapping.clear();
        typeMapping.put("integer", "int");
        typeMapping.put("float", "float");
        typeMapping.put("number", "float");
        typeMapping.put("long", "int");
        typeMapping.put("double", "float");
        typeMapping.put("array", "list");
        typeMapping.put("set", "list");
        typeMapping.put("map", "dict");
        typeMapping.put("boolean", "bool");
        typeMapping.put("string", "str");
        typeMapping.put("date", "date");
        typeMapping.put("DateTime", "datetime");
        typeMapping.put("object", "object");
        typeMapping.put("AnyType", "object");
        typeMapping.put("file", "file");
        // TODO binary should be mapped to byte array
        // mapped to String as a workaround
        typeMapping.put("binary", "str");
        typeMapping.put("ByteArray", "str");
        // map uuid to string for the time being
        typeMapping.put("UUID", "str");
        typeMapping.put("URI", "str");
        typeMapping.put("null", "none_type");
    }

    @Override
    public void processOpts() {
        super.processOpts();

        if (StringUtils.isEmpty(System.getenv("PYTHON_POST_PROCESS_FILE"))) {
            LOGGER.info("Environment variable PYTHON_POST_PROCESS_FILE not defined so the Python code may not be properly formatted. To define it, try 'export PYTHON_POST_PROCESS_FILE=\"/usr/local/bin/yapf -i\"' (Linux/Mac)");
            LOGGER.info("NOTE: To enable file post-processing, 'enablePostProcessFile' must be set to `true` (--enable-post-process-file for CLI).");
        }
    }

    @Override
    public String escapeReservedWord(String name) {
        if (this.reservedWordsMappings().containsKey(name)) {
            return this.reservedWordsMappings().get(name);
        }
        return "_" + name;
    }

    @Override
    public String toVarName(String name) {
        // sanitize name
        name = sanitizeName(name); // FIXME: a parameter should not be assigned. Also declare the methods parameters as 'final'.

        // remove dollar sign
        name = name.replaceAll("$", "");

        // if it's all upper case, convert to lower case
        if (name.matches("^[A-Z_]*$")) {
            name = name.toLowerCase(Locale.ROOT);
        }

        // underscore the variable name
        // petId => pet_id
        name = underscore(name);

        // remove leading underscore
        name = name.replaceAll("^_*", "");

        // for reserved word or word starting with number, append _
        if (isReservedWord(name) || name.matches("^\\d.*")) {
            name = escapeReservedWord(name);
        }

        return name;
    }

    @Override
    public String toParamName(String name) {
        // to avoid conflicts with 'callback' parameter for async call
        if ("callback".equals(name)) {
            return "param_callback";
        }

        // should be the same as variable name
        return toVarName(name);
    }

    @Override
    public String escapeQuotationMark(String input) {
        // remove ' to avoid code injection
        return input.replace("'", "");
    }

    @Override
    public String escapeUnsafeCharacters(String input) {
        // remove multiline comment
        return input.replace("'''", "'_'_'");
    }

    @Override
    public void postProcessFile(File file, String fileType) {
        if (file == null) {
            return;
        }
        String pythonPostProcessFile = System.getenv("PYTHON_POST_PROCESS_FILE");
        if (StringUtils.isEmpty(pythonPostProcessFile)) {
            return; // skip if PYTHON_POST_PROCESS_FILE env variable is not defined
        }

        // only process files with py extension
        if ("py".equals(FilenameUtils.getExtension(file.toString()))) {
            String command = pythonPostProcessFile + " " + file;
            try {
                Process p = Runtime.getRuntime().exec(command);
                int exitValue = p.waitFor();
                if (exitValue != 0) {
                    LOGGER.error("Error running the command ({}). Exit value: {}", command, exitValue);
                } else {
                    LOGGER.info("Successfully executed: {}", command);
                }
            } catch (InterruptedException | IOException e) {
                LOGGER.error("Error running the command ({}). Exception: {}", command, e.getMessage());
                // Restore interrupted state
                Thread.currentThread().interrupt();
            }
        }
    }

    @Override
    public String toExampleValue(Schema schema) {
        return toExampleValueRecursive(schema, new ArrayList<>(), 5);
    }

    private String toExampleValueRecursive(Schema schema, List<Schema> includedSchemas, int indentation) {
        boolean cycleFound = includedSchemas.stream().filter(s->schema.equals(s)).count() > 1;
        if (cycleFound) {
            return "";
        }
        String indentationString = "";
        for (int i = 0; i < indentation; i++) indentationString += "    ";
        String example = null;
        if (schema.getExample() != null) {
            example = schema.getExample().toString();
        }

        if (ModelUtils.isNullType(schema) && null != example) {
            // The 'null' type is allowed in OAS 3.1 and above. It is not supported by OAS 3.0.x,
            // though this tooling supports it.
            return "None";
        }
        // correct "true"s into "True"s, since super.toExampleValue uses "toString()" on Java booleans
        if (ModelUtils.isBooleanSchema(schema) && null != example) {
            if ("false".equalsIgnoreCase(example)) example = "False";
            else example = "True";
        }

        // correct "&#39;"s into "'"s after toString()
        if (ModelUtils.isStringSchema(schema) && schema.getDefault() != null && !ModelUtils.isDateSchema(schema) && !ModelUtils.isDateTimeSchema(schema)) {
            example = (String) schema.getDefault();
        }

        if (StringUtils.isNotBlank(example) && !"null".equals(example)) {
            if (ModelUtils.isStringSchema(schema)) {
                example = "'" + example + "'";
            }
            return example;
        }

        if (schema.getEnum() != null && !schema.getEnum().isEmpty()) {
            // Enum case:
            example = schema.getEnum().get(0).toString();
            if (ModelUtils.isStringSchema(schema)) {
                example = "'" + escapeText(example) + "'";
            }
            if (null == example)
                LOGGER.warn("Empty enum. Cannot built an example!");

            return example;
        } else if (null != schema.get$ref()) {
            // $ref case:
            Map<String, Schema> allDefinitions = ModelUtils.getSchemas(this.openAPI);
            String ref = ModelUtils.getSimpleRef(schema.get$ref());
            if (allDefinitions != null) {
                Schema refSchema = allDefinitions.get(ref);
                if (null == refSchema) {
                    return "None";
                } else {
                    String refTitle = refSchema.getTitle();
                    if (StringUtils.isBlank(refTitle) || "null".equals(refTitle)) {
                        refSchema.setTitle(ref);
                    }
                    if (StringUtils.isNotBlank(schema.getTitle()) && !"null".equals(schema.getTitle())) {
                        includedSchemas.add(schema);
                    }
                    return toExampleValueRecursive(refSchema, includedSchemas, indentation);
                }
            } else {
                LOGGER.warn("allDefinitions not defined in toExampleValue!\n");
            }
        }
        if (ModelUtils.isDateSchema(schema)) {
            example = "datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date()";
            return example;
        } else if (ModelUtils.isDateTimeSchema(schema)) {
            example = "datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')";
            return example;
        } else if (ModelUtils.isBinarySchema(schema)) {
            example = "bytes(b'blah')";
            return example;
        } else if (ModelUtils.isByteArraySchema(schema)) {
            example = "YQ==";
        } else if (ModelUtils.isStringSchema(schema)) {
            // a BigDecimal:
            if ("Number".equalsIgnoreCase(schema.getFormat())) {
                return "1";
            }
            if (StringUtils.isNotBlank(schema.getPattern())) {
                String pattern = schema.getPattern();
                RgxGen rgxGen = new RgxGen(patternCorrection(pattern));
                // this seed makes it so if we have [a-z] we pick a
                Random random = new Random(18);
                String sample = rgxGen.generate(random);
                // omit leading / and trailing /, omit trailing /i
                Pattern valueExtractor = Pattern.compile("^/\\^?(.+?)\\$?/.?$");
                Matcher m = valueExtractor.matcher(sample);
                if (m.find()) {
                    example = m.group(m.groupCount());
                } else {
                    example = sample;
                }
            }
            if (example == null) {
                example = "";
            }
            int len = 0;
            if (null != schema.getMinLength()) {
                len = schema.getMinLength().intValue();
                if (len < 1) {
                    example = "";
                } else {
                    for (int i = 0; i < len; i++) example += i;
                }
            }
        } else if (ModelUtils.isIntegerSchema(schema)) {
            if (schema.getMinimum() != null)
                example = schema.getMinimum().toString();
            else
                example = "56";
        } else if (ModelUtils.isNumberSchema(schema)) {
            if (schema.getMinimum() != null)
                example = schema.getMinimum().toString();
            else
                example = "1.337";
        } else if (ModelUtils.isBooleanSchema(schema)) {
            example = "True";
        } else if (ModelUtils.isArraySchema(schema)) {
            if (StringUtils.isNotBlank(schema.getTitle()) && !"null".equals(schema.getTitle())) {
                includedSchemas.add(schema);
            }
            ArraySchema arrayschema = (ArraySchema) schema;
            example = "[\n" + indentationString + toExampleValueRecursive(arrayschema.getItems(), includedSchemas, indentation + 1) + "\n" + indentationString + "]";
        } else if (ModelUtils.isMapSchema(schema)) {
            if (StringUtils.isNotBlank(schema.getTitle()) && !"null".equals(schema.getTitle())) {
                includedSchemas.add(schema);
            }
            Object additionalObject = schema.getAdditionalProperties();
            if (additionalObject instanceof Schema) {
                Schema additional = (Schema) additionalObject;
                String theKey = "'key'";
                if (additional.getEnum() != null && !additional.getEnum().isEmpty()) {
                    theKey = additional.getEnum().get(0).toString();
                    if (ModelUtils.isStringSchema(additional)) {
                        theKey = "'" + escapeText(theKey) + "'";
                    }
                }
                example = "{\n" + indentationString + theKey + " : " + toExampleValueRecursive(additional, includedSchemas, indentation + 1) + "\n" + indentationString + "}";
            } else {
                example = "{ }";
            }
        } else if (ModelUtils.isObjectSchema(schema)) {
            if (StringUtils.isBlank(schema.getTitle())) {
                example = "None";
                return example;
            }

            // I remove any property that is a discriminator, since it is not well supported by the python generator
            String toExclude = null;
            if (schema.getDiscriminator() != null) {
                toExclude = schema.getDiscriminator().getPropertyName();
            }

            example = packageName + ".models." + underscore(schema.getTitle()) + "." + schema.getTitle() + "(";

            // if required only:
            // List<String> reqs = schema.getRequired();

            // if required and optionals
            List<String> reqs = new ArrayList<>();
            if (schema.getProperties() != null && !schema.getProperties().isEmpty()) {
                for (Object toAdd : schema.getProperties().keySet()) {
                    reqs.add((String) toAdd);
                }

                Map<String, Schema> properties = schema.getProperties();
                Set<String> propkeys = null;
                if (properties != null) propkeys = properties.keySet();
                if (toExclude != null && reqs.contains(toExclude)) {
                    reqs.remove(toExclude);
                }
                for (String toRemove : includedSchemas.stream().map(Schema::getTitle).collect(Collectors.toList())) {
                    if (reqs.contains(toRemove)) {
                        reqs.remove(toRemove);
                    }
                }
                if (StringUtils.isNotBlank(schema.getTitle()) && !"null".equals(schema.getTitle())) {
                    includedSchemas.add(schema);
                }
                if (null != schema.getRequired()) for (Object toAdd : schema.getRequired()) {
                    reqs.add((String) toAdd);
                }
                if (null != propkeys) for (String propname : propkeys) {
                    Schema schema2 = properties.get(propname);
                    if (reqs.contains(propname)) {
                        String refTitle = schema2.getTitle();
                        if (StringUtils.isBlank(refTitle) || "null".equals(refTitle)) {
                            schema2.setTitle(propname);
                        }
                        example += "\n" + indentationString + underscore(propname) + " = " +
                                toExampleValueRecursive(schema2, includedSchemas, indentation + 1) + ", ";
                    }
                }
            }
            example += ")";
        } else {
            LOGGER.warn("Type {} not handled properly in toExampleValue", schema.getType());
        }

        if (ModelUtils.isStringSchema(schema)) {
            example = "'" + escapeText(example) + "'";
        }

        return example;
    }

    @Override
    public String sanitizeTag(String tag) {
        return sanitizeName(tag);
    }

    public String patternCorrection(String pattern) {
        // Java does not recognize starting and ending forward slashes and mode modifiers
        // It considers them as characters with no special meaning and tries to find them in the match string
        boolean checkEnding = pattern.endsWith("/i") || pattern.endsWith("/g") || pattern.endsWith("/m");
        if (checkEnding) pattern = pattern.substring(0, pattern.length() - 2);
        if (pattern.endsWith("/")) pattern = pattern.substring(0, pattern.length() - 1);
        if (pattern.startsWith("/")) pattern = pattern.substring(1);
        return pattern;
    }

    public void setPackageName(String packageName) {
        this.packageName = packageName;
        additionalProperties.put(CodegenConstants.PACKAGE_NAME, this.packageName);
    }

    public void setProjectName(String projectName) {
        this.projectName = projectName;
    }

    public void setPackageVersion(String packageVersion) {
        this.packageVersion = packageVersion;
    }

    @Override
    public String toModelFilename(String name, String jsonPath) {
        // underscore the model file name
        // PhoneNumber => phone_number
        return toModuleFilename(name, jsonPath);
    }

    @Override
    public String toApiFilename(String name) {
        // e.g. PhoneNumberApi.py => phone_number_api.py
        return underscore(toApiName(name));
    }

    @Override
    public String toApiName(String name) {
        return super.toApiName(name);
    }

    @Override
    public String toApiVarName(String name) {
        return underscore(toApiName(name));
    }

    protected static String dropDots(String str) {
        return str.replaceAll("\\.", "_");
    }

    @Override
    public GeneratorLanguage generatorLanguage() { return GeneratorLanguage.PYTHON; }
}
