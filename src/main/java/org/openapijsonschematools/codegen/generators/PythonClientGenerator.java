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
import com.github.curiousoddman.rgxgen.config.RgxGenOption;
import com.github.curiousoddman.rgxgen.config.RgxGenProperties;
import com.google.common.base.CaseFormat;
import io.swagger.v3.oas.models.Components;
import io.swagger.v3.oas.models.OpenAPI;

import org.apache.commons.io.FileUtils;
import org.apache.commons.io.FilenameUtils;
import org.openapijsonschematools.codegen.generators.generatormetadata.GeneratorLanguage;
import org.openapijsonschematools.codegen.generators.models.CliOption;
import org.openapijsonschematools.codegen.common.CodegenConstants;
import org.openapijsonschematools.codegen.generators.generatormetadata.GeneratorType;
import org.openapijsonschematools.codegen.generators.generatormetadata.features.ComponentsFeature;
import org.openapijsonschematools.codegen.generators.generatormetadata.features.OperationFeature;
import org.openapijsonschematools.codegen.generators.generatormetadata.features.SchemaFeature;
import org.openapijsonschematools.codegen.generators.openapimodels.CodegenDiscriminator;
import org.openapijsonschematools.codegen.generators.openapimodels.CodegenPatternInfo;
import org.openapijsonschematools.codegen.generators.openapimodels.CodegenSchema;
import org.openapijsonschematools.codegen.templating.SupportingFile;
import org.openapijsonschematools.codegen.generators.generatormetadata.features.DataTypeFeature;
import org.openapijsonschematools.codegen.generators.generatormetadata.features.DocumentationFeature;
import org.openapijsonschematools.codegen.generators.generatormetadata.features.GlobalFeature;
import org.openapijsonschematools.codegen.generators.generatormetadata.features.ParameterFeature;
import org.openapijsonschematools.codegen.generators.generatormetadata.features.SecurityFeature;
import org.openapijsonschematools.codegen.generators.generatormetadata.features.WireFormatFeature;
import org.openapijsonschematools.codegen.generators.openapimodels.PairCacheKey;
import org.openapijsonschematools.codegen.templating.HandlebarsEngineAdapter;
import io.swagger.v3.oas.models.media.*;
import io.swagger.v3.oas.models.parameters.Parameter;
import io.swagger.v3.oas.models.security.SecurityScheme;
import org.apache.commons.lang3.StringUtils;
import org.openapijsonschematools.codegen.generators.openapimodels.CodegenDiscriminator.MappedModel;
import org.openapijsonschematools.codegen.templating.TemplatingEngineAdapter;
import org.openapijsonschematools.codegen.generators.generatormetadata.GeneratorMetadata;
import org.openapijsonschematools.codegen.generators.generatormetadata.Stability;
import org.openapijsonschematools.codegen.common.ModelUtils;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import javax.validation.constraints.NotNull;
import java.io.File;
import java.io.IOException;
import java.time.OffsetDateTime;
import java.time.ZoneOffset;
import java.time.format.DateTimeFormatter;
import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import static org.openapijsonschematools.codegen.common.StringUtils.camelize;
import static org.openapijsonschematools.codegen.common.StringUtils.underscore;

@SuppressWarnings("rawtypes")
public class PythonClientGenerator extends DefaultGenerator implements Generator {
    private final Logger LOGGER = LoggerFactory.getLogger(PythonClientGenerator.class);

    public static final String PACKAGE_URL = "packageUrl";
    // nose is a python testing framework, we use pytest if USE_NOSE is unset
    public static final String USE_NOSE = "useNose";
    public static final String RECURSION_LIMIT = "recursionLimit";

    protected String packageUrl;
    protected String apiDocPath = "docs/apis/tags/";
    // keep this in case the user has provided a custom model path
    // todo connect that custom path in here
    protected String modelDocPath = "docs/components/schema/";
    protected boolean useNose = false;

    protected Map<Character, String> regexModifiers;

    private final String testFolder;

    // A cache to efficiently look up a Schema instance based on the return value of `toModelName()`.
    private Map<String, Schema> modelNameToSchemaCache;
    private final DateTimeFormatter iso8601Date = DateTimeFormatter.ISO_DATE;
    private final DateTimeFormatter iso8601DateTime = DateTimeFormatter.ISO_DATE_TIME;
    private boolean nonCompliantUseDiscrIfCompositionFails = false;
    private final HashMap<PairCacheKey, String> modelNameCache = new HashMap<>();
    protected String packageVersion = "1.0.0";
    protected String projectName; // for setup.py, e.g. petstore-api

    public PythonClientGenerator() {
        super();
        loadDeepObjectIntoItems = false;
        importBaseType = false;
        addSchemaImportsFromV3SpecLocations = true;
        removeEnumValuePrefix = false;

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

        modifyFeatureSet(features -> features
                .includeDataTypeFeatures(
                        DataTypeFeature.Int32,
                        DataTypeFeature.Int64,
                        DataTypeFeature.Integer,
                        DataTypeFeature.Float,
                        DataTypeFeature.Double,
                        DataTypeFeature.Number,
                        DataTypeFeature.String,
                        DataTypeFeature.Binary,
                        DataTypeFeature.Boolean,
                        DataTypeFeature.Date,
                        DataTypeFeature.DateTime,
                        DataTypeFeature.Uuid,
                        DataTypeFeature.File,
                        DataTypeFeature.Array,
                        DataTypeFeature.Object,
                        DataTypeFeature.Null,
                        DataTypeFeature.AnyType,
                        DataTypeFeature.Enum
                )
                .excludeDataTypeFeatures(
                        DataTypeFeature.Byte,
                        DataTypeFeature.Password
                )
                .includeSchemaFeatures(
                        SchemaFeature.AdditionalProperties,
                        SchemaFeature.AllOf,
                        SchemaFeature.AnyOf,
                        SchemaFeature.Const,
                        SchemaFeature.Contains,
                        SchemaFeature.Default,
                        SchemaFeature.DependentRequired,
                        SchemaFeature.DependentSchemas,
                        SchemaFeature.Discriminator,
                        SchemaFeature.Else,
                        SchemaFeature.Enum,
                        SchemaFeature.ExclusiveMaximum,
                        SchemaFeature.ExclusiveMinimum,
                        SchemaFeature.Format,
                        SchemaFeature.If,
                        SchemaFeature.Items,
                        SchemaFeature.MaxContains,
                        SchemaFeature.MaxItems,
                        SchemaFeature.MaxLength,
                        SchemaFeature.MaxProperties,
                        SchemaFeature.Maximum,
                        SchemaFeature.MinContains,
                        SchemaFeature.MinItems,
                        SchemaFeature.MinLength,
                        SchemaFeature.MinProperties,
                        SchemaFeature.Minimum,
                        SchemaFeature.MultipleOf,
                        SchemaFeature.Not,
                        SchemaFeature.Nullable,
                        SchemaFeature.OneOf,
                        SchemaFeature.Pattern,
                        SchemaFeature.PatternProperties,
                        SchemaFeature.PrefixItems,
                        SchemaFeature.Properties,
                        SchemaFeature.PropertyNames,
                        SchemaFeature.Ref,
                        SchemaFeature.Required,
                        SchemaFeature.Then,
                        SchemaFeature.Type,
                        SchemaFeature.UnevaluatedItems,
                        SchemaFeature.UnevaluatedProperties,
                        SchemaFeature.UniqueItems
                )
                .includeDocumentationFeatures(
                        DocumentationFeature.Readme,
                        DocumentationFeature.Servers,
                        DocumentationFeature.Security,
                        DocumentationFeature.ComponentSchemas,
                        DocumentationFeature.ComponentResponses,
                        DocumentationFeature.ComponentParameters,
                        DocumentationFeature.ComponentRequestBodies,
                        DocumentationFeature.ComponentHeaders,
                        DocumentationFeature.ComponentSecuritySchemes,
                        DocumentationFeature.Api
                )
                .includeWireFormatFeatures(WireFormatFeature.JSON, WireFormatFeature.Custom)
                .includeSecurityFeatures(
                        SecurityFeature.ApiKey,
                        SecurityFeature.HTTP_Basic,
                        SecurityFeature.HTTP_Bearer
                )
                .includeGlobalFeatures(
                        GlobalFeature.Info,
                        GlobalFeature.Servers,
                        GlobalFeature.Paths,
                        GlobalFeature.Components,
                        GlobalFeature.Security,
                        GlobalFeature.Tags
                )
                .includeComponentsFeatures(
                        ComponentsFeature.schemas,
                        ComponentsFeature.responses,
                        ComponentsFeature.parameters,
                        ComponentsFeature.requestBodies,
                        ComponentsFeature.headers,
                        ComponentsFeature.securitySchemes
                )
                .includeParameterFeatures(
                        ParameterFeature.Name,
                        ParameterFeature.Required,
                        ParameterFeature.In_Path,
                        ParameterFeature.In_Query,
                        ParameterFeature.In_Header,
                        ParameterFeature.Style_Matrix,
                        ParameterFeature.Style_Label,
                        ParameterFeature.Style_Form,
                        ParameterFeature.Style_Simple,
                        ParameterFeature.Style_PipeDelimited,
                        ParameterFeature.Style_SpaceDelimited,
                        ParameterFeature.Explode,
                        ParameterFeature.Schema,
                        ParameterFeature.Content
                )
                .includeOperationFeatures(
                        OperationFeature.Responses_Default,
                        OperationFeature.Responses_HttpStatusCode,
                        OperationFeature.Responses_RangedResponseCodes,
                        OperationFeature.Responses_RedirectionResponse,
                        OperationFeature.Security,
                        OperationFeature.Servers
                )
        );

        modelPackage = "components.schema";
        apiPackage = "apis";
        outputFolder = "generated-code" + File.separatorChar + "python";

        embeddedTemplateDir = templateDir = "python";

        testFolder = "test";

        // default HIDE_GENERATION_TIMESTAMP to true
        hideGenerationTimestamp = Boolean.TRUE;

        // from https://docs.python.org/3/reference/lexical_analysis.html#keywords
        setReservedWordsLowerCase(
                Arrays.asList(
                        // @property
                        "property",
                        // python reserved words
                        "and", "del", "from", "not", "while", "as", "elif", "global", "or", "with",
                        "assert", "else", "if", "pass", "yield", "break", "except", "import",
                        "print", "class", "exec", "in", "raise", "continue", "finally", "is",
                        "return", "def", "for", "lambda", "try", "self", "nonlocal", "None", "True",
                        "False", "async", "await",
                        // types
                        "float", "int", "str", "bool", "dict", "immutabledict", "list", "tuple"));

        regexModifiers = new HashMap<>();
        regexModifiers.put('i', "IGNORECASE");
        regexModifiers.put('l', "LOCALE");
        regexModifiers.put('m', "MULTILINE");
        regexModifiers.put('s', "DOTALL");
        regexModifiers.put('u', "UNICODE");

        cliOptions.clear();
        cliOptions.add(new CliOption(CodegenConstants.PACKAGE_NAME, "python package name (convention: snake_case).")
                .defaultValue("openapi_client"));
        cliOptions.add(new CliOption(CodegenConstants.PROJECT_NAME, "python project name in setup.py (e.g. petstore-api)."));
        cliOptions.add(new CliOption(CodegenConstants.PACKAGE_VERSION, "python package version.")
                .defaultValue("1.0.0"));
        cliOptions.add(new CliOption(PACKAGE_URL, "python package URL."));
        // this generator does not use SORT_PARAMS_BY_REQUIRED_FLAG
        // this generator uses the following order for endpoint parameters and model properties
        // required params
        // optional params which are set to unset as their default for method signatures only
        // optional params as **kwargs
        cliOptions.add(new CliOption(CodegenConstants.HIDE_GENERATION_TIMESTAMP, CodegenConstants.HIDE_GENERATION_TIMESTAMP_DESC)
                .defaultValue(Boolean.TRUE.toString()));
        cliOptions.add(new CliOption(CodegenConstants.SOURCECODEONLY_GENERATION, CodegenConstants.SOURCECODEONLY_GENERATION_DESC)
                .defaultValue(Boolean.FALSE.toString()));
        cliOptions.add(CliOption.newBoolean(USE_NOSE, "use the nose test framework").
                defaultValue(Boolean.FALSE.toString()));
        cliOptions.add(new CliOption(RECURSION_LIMIT, "Set the recursion limit. If not set, use the system default value."));
        CliOption templateEngineOption = new CliOption(CodegenConstants.TEMPLATING_ENGINE, "template engine");
        templateEngineOption.setDefault("handlebars");
        Map<String, String> templateEngineEnumValueToDesc = new HashMap<>();
        templateEngineEnumValueToDesc.put("handlebars", "handlebars templating engine");
        templateEngineOption.setEnum(templateEngineEnumValueToDesc);
        cliOptions.add(templateEngineOption);
        CliOption nonCompliantUseDiscrIfCompositionFails = CliOption.newBoolean(CodegenConstants.NON_COMPLIANT_USE_DISCR_IF_COMPOSITION_FAILS, CodegenConstants.NON_COMPLIANT_USE_DISCR_IF_COMPOSITION_FAILS_DESC);
        Map<String, String> nonCompliantUseDiscrIfCompositionFailsOpts = new HashMap<>();
        nonCompliantUseDiscrIfCompositionFailsOpts.put("true", "If composition fails and a discriminator exists, the composition errors will be ignored and validation will be attempted with the discriminator");
        nonCompliantUseDiscrIfCompositionFailsOpts.put("false", "Composition validation must succeed. Discriminator validation must succeed.");
        nonCompliantUseDiscrIfCompositionFails.setEnum(nonCompliantUseDiscrIfCompositionFailsOpts);

        cliOptions.add(nonCompliantUseDiscrIfCompositionFails);

        // Composed schemas can have the 'additionalProperties' keyword, as specified in JSON schema.
        // In principle, this should be enabled by default for all code generators. However, due to limitations
        // in other code generators, support needs to be enabled on a case-by-case basis.
        supportsAdditionalPropertiesWithComposedSchema = true;

        // this tells users what openapi types turn in to
        instantiationTypes.put("object", "immutabledict.immutabledict");
        instantiationTypes.put("array", "tuple");
        instantiationTypes.put("string", "str");
        instantiationTypes.put("number", "typing.Union[float, int]");
        instantiationTypes.put("integer", "int");
        instantiationTypes.put("boolean", "bool");
        instantiationTypes.put("null", "None");

        languageSpecificPrimitives.add("file_type");
        languageSpecificPrimitives.add("none_type");

        generatorMetadata = GeneratorMetadata.newBuilder(generatorMetadata)
                .stability(Stability.STABLE)
                .build();
    }

    @Override
    public TemplatingEngineAdapter getTemplatingEngine() {
        TemplatingEngineAdapter te = super.getTemplatingEngine();
        HandlebarsEngineAdapter hea = (HandlebarsEngineAdapter) te;
        hea.infiniteLoops(true);
        hea.setPrettyPrint(true);
        return hea;
    }

    @Override
    public void processOpts() {

        super.processOpts();

        if (!"handlebars".equals(this.templateEngineName)) {
            throw new RuntimeException("Only the HandlebarsEngineAdapter is supported for this generator");
        }

        jsonPathDocTemplateFiles.put(
                CodegenConstants.JSON_PATH_LOCATION_TYPE.API_TAG,
                new HashMap<>() {{
                    put("apis/tags/api_doc.hbs", ".md");
                }}
        );

        HashMap<String, String> apiRootTemplates = new HashMap<>();
        apiRootTemplates.put("apis/apis_tag_to_api.hbs", File.separatorChar + "tag_to_api.py");
        apiRootTemplates.put("apis/apis_path_to_api.hbs", File.separatorChar + "path_to_api.py");
        apiRootTemplates.put("apis/__init__.hbs", File.separatorChar + "__init__.py");

        jsonPathTemplateFiles.put(
                CodegenConstants.JSON_PATH_LOCATION_TYPE.API_ROOT_FOLDER,
                apiRootTemplates
        );
        jsonPathTemplateFiles.put(
                CodegenConstants.JSON_PATH_LOCATION_TYPE.API_PATH,
                new HashMap<>() {{
                    put("apis/paths/api.hbs", ".py");
                }}
        );
        jsonPathTemplateFiles.put(
                CodegenConstants.JSON_PATH_LOCATION_TYPE.API_PATHS,
                new HashMap<>() {{
                    put("apis/paths/__init__.hbs", File.separatorChar + "__init__.py");
                }}
        );
        jsonPathTemplateFiles.put(
                CodegenConstants.JSON_PATH_LOCATION_TYPE.API_TAG,
                new HashMap<>() {{
                    put("apis/tags/api.hbs", ".py");
                }}
        );
        jsonPathTemplateFiles.put(
                CodegenConstants.JSON_PATH_LOCATION_TYPE.API_TAGS,
                new HashMap<>() {{
                    put("apis/tags/__init__.hbs", File.separatorChar + "__init__.py");
                }}
        );

        jsonPathDocTemplateFiles.put(
                CodegenConstants.JSON_PATH_LOCATION_TYPE.OPERATION,
                new HashMap<>() {{
                    put("paths/path/verb/operation_doc.hbs", ".md");
                }}
        );
        jsonPathDocTemplateFiles.put(
                CodegenConstants.JSON_PATH_LOCATION_TYPE.SCHEMA,
                new HashMap<>() {{
                    put("components/schemas/schema_doc.hbs", ".md");
                }}
        );
        jsonPathDocTemplateFiles.put(
                CodegenConstants.JSON_PATH_LOCATION_TYPE.REQUEST_BODY,
                new HashMap<>() {{
                    put("components/request_bodies/request_body_doc.hbs", ".md");
                }}
        );
        jsonPathDocTemplateFiles.put(
                CodegenConstants.JSON_PATH_LOCATION_TYPE.PARAMETER,
                new HashMap<>() {{
                    put("components/parameters/parameter_doc.hbs", ".md");
                }}
        );
        jsonPathDocTemplateFiles.put(
                CodegenConstants.JSON_PATH_LOCATION_TYPE.RESPONSE,
                new HashMap<>() {{
                    put("components/responses/response_doc.hbs", ".md");
                }}
        );
        jsonPathDocTemplateFiles.put(
                CodegenConstants.JSON_PATH_LOCATION_TYPE.HEADER,
                new HashMap<>() {{
                    put("components/headers/header_doc.hbs", ".md");
                }}
        );
        jsonPathDocTemplateFiles.put(
                CodegenConstants.JSON_PATH_LOCATION_TYPE.SECURITY_SCHEME,
                new HashMap<>() {{
                    put("components/security_schemes/security_scheme_doc.hbs", ".md");
                }}
        );
        jsonPathDocTemplateFiles.put(
                CodegenConstants.JSON_PATH_LOCATION_TYPE.SERVER,
                new HashMap<>() {{
                    put("servers/server_doc.hbs", ".md");
                }}
        );

        HashMap<String, String> schemaTemplates = new HashMap<>();
        schemaTemplates.put("components/schemas/schema.hbs", ".py");
        jsonPathTemplateFiles.put(
                CodegenConstants.JSON_PATH_LOCATION_TYPE.SCHEMA,
                schemaTemplates
        );
        // there is no deeper info so the filenames can be individually generated
        jsonPathTemplateFiles.put(
                CodegenConstants.JSON_PATH_LOCATION_TYPE.SECURITY_SCHEME,
                new HashMap<>() {{
                    put("components/security_schemes/security_scheme.hbs", ".py");
                }}
        );
        jsonPathTemplateFiles.put(
                CodegenConstants.JSON_PATH_LOCATION_TYPE.SECURITY_SCHEMES,
                new HashMap<>() {{
                    put("__init__.hbs", File.separatorChar + "__init__.py");
                }}
        );
        jsonPathTemplateFiles.put(
                CodegenConstants.JSON_PATH_LOCATION_TYPE.HEADERS,
                new HashMap<>() {{
                    put("__init__.hbs", File.separatorChar + "__init__.py");
                }}
        );
        jsonPathTemplateFiles.put(
                CodegenConstants.JSON_PATH_LOCATION_TYPE.HEADER,
                new HashMap<>() {{
                    put("components/headers/header.hbs", File.separatorChar + "__init__.py");
                }}
        );
        jsonPathTemplateFiles.put(
                CodegenConstants.JSON_PATH_LOCATION_TYPE.PARAMETERS,
                new HashMap<>() {{
                    put("__init__.hbs", File.separatorChar + "__init__.py");
                }}
        );
        jsonPathTemplateFiles.put(
                CodegenConstants.JSON_PATH_LOCATION_TYPE.PARAMETER,
                new HashMap<>() {{
                    put("components/parameters/parameter.hbs", File.separatorChar + "__init__.py");
                }}
        );
        jsonPathTemplateFiles.put(
                CodegenConstants.JSON_PATH_LOCATION_TYPE.REQUEST_BODIES,
                new HashMap<>() {{
                    put("__init__.hbs", File.separatorChar + "__init__.py");
                }}
        );
        jsonPathTemplateFiles.put(
                CodegenConstants.JSON_PATH_LOCATION_TYPE.REQUEST_BODY,
                new HashMap<>() {{
                    put("components/request_bodies/request_body.hbs", File.separatorChar + "__init__.py");
                }}
        );
        jsonPathTemplateFiles.put(
                CodegenConstants.JSON_PATH_LOCATION_TYPE.RESPONSES,
                new HashMap<>() {{
                    put("__init__.hbs", File.separatorChar + "__init__.py");
                }}
        );
        jsonPathTemplateFiles.put(
                CodegenConstants.JSON_PATH_LOCATION_TYPE.RESPONSE,
                new HashMap<>() {{
                    put("components/responses/response.hbs", File.separatorChar + "__init__.py");
                }}
        );
        jsonPathTemplateFiles.put(
                CodegenConstants.JSON_PATH_LOCATION_TYPE.SERVERS,
                new HashMap<>() {{
                    put("__init__.hbs", File.separatorChar + "__init__.py");
                }}
        );
        jsonPathTemplateFiles.put(
                CodegenConstants.JSON_PATH_LOCATION_TYPE.SERVER,
                new HashMap<>() {{
                    put("servers/server.hbs", ".py");
                }}
        );
        jsonPathTemplateFiles.put(
                CodegenConstants.JSON_PATH_LOCATION_TYPE.SCHEMAS,
                new HashMap<>() {{
                    put("components/schemas/__init__schema.hbs", File.separatorChar + "__init__.py");
                }}
        );
        jsonPathTemplateFiles.put(
                CodegenConstants.JSON_PATH_LOCATION_TYPE.SECURITIES,
                new HashMap<>() {{
                    put("__init__.hbs", File.separatorChar + "__init__.py");
                }}
        );
        jsonPathTemplateFiles.put(
                CodegenConstants.JSON_PATH_LOCATION_TYPE.SECURITY,
                new HashMap<>() {{
                    put("security/security.hbs", ".py");
                }}
        );

        jsonPathTemplateFiles.put(
                CodegenConstants.JSON_PATH_LOCATION_TYPE.PATHS,
                new HashMap<>() {{
                    put("paths/__init__paths.hbs", File.separatorChar + "__init__.py");
                }}
        );
        jsonPathTemplateFiles.put(
                CodegenConstants.JSON_PATH_LOCATION_TYPE.PATH,
                new HashMap<>() {{
                    put("paths/path/__init__path.hbs", File.separatorChar + "__init__.py");
                }}
        );
        jsonPathTestTemplateFiles.put(
                CodegenConstants.JSON_PATH_LOCATION_TYPE.PATHS,
                new HashMap<>() {{
                    put("paths/__init__test.hbs", File.separatorChar + "__init__.py");
                }}
        );
        jsonPathTestTemplateFiles.put(
                CodegenConstants.JSON_PATH_LOCATION_TYPE.PATH,
                new HashMap<>() {{
                    put("__init__.hbs", File.separatorChar + "__init__.py");
                }}

        );
        jsonPathTestTemplateFiles.put(
                CodegenConstants.JSON_PATH_LOCATION_TYPE.TEST_ROOT,
                new HashMap<>() {{
                    put("__init__.hbs", File.separatorChar + "__init__.py");
                }}

        );
        jsonPathTestTemplateFiles.put(
                CodegenConstants.JSON_PATH_LOCATION_TYPE.OPERATION,
                new HashMap<>() {{
                    put("paths/path/verb/operation_test.hbs", ".py");
                }}

        );
        jsonPathTestTemplateFiles.put(
                CodegenConstants.JSON_PATH_LOCATION_TYPE.COMPONENTS,
                new HashMap<>() {{
                    put("__init__.hbs", File.separatorChar + "__init__.py");
                }}

        );
        jsonPathTestTemplateFiles.put(
                CodegenConstants.JSON_PATH_LOCATION_TYPE.SCHEMAS,
                new HashMap<>() {{
                    put("__init__.hbs", File.separatorChar + "__init__.py");
                }}

        );
        jsonPathTestTemplateFiles.put(
                CodegenConstants.JSON_PATH_LOCATION_TYPE.SCHEMA,
                new HashMap<>() {{
                    put("components/schemas/schema_test.hbs", ".py");
                }}

        );
        HashMap<String, String> operationTemplates = new HashMap<>();
        operationTemplates.put("__init__.hbs", File.separatorChar + "__init__.py");
        operationTemplates.put("paths/path/verb/operation.hbs", File.separatorChar + "operation.py");
        jsonPathTemplateFiles.put(
                CodegenConstants.JSON_PATH_LOCATION_TYPE.OPERATION,
                operationTemplates
        );
        jsonPathTemplateFiles.put(
                CodegenConstants.JSON_PATH_LOCATION_TYPE.COMPONENTS,
                new HashMap<>() {{
                    put("__init__.hbs", File.separatorChar + "__init__.py");
                }}
        );
        jsonPathTemplateFiles.put(
                CodegenConstants.JSON_PATH_LOCATION_TYPE.CONTENT,
                new HashMap<>() {{
                    put("__init__.hbs", File.separatorChar + "__init__.py");
                }}
        );
        jsonPathTemplateFiles.put(
                CodegenConstants.JSON_PATH_LOCATION_TYPE.CONTENT_TYPE,
                new HashMap<>() {{
                    put("__init__.hbs", File.separatorChar + "__init__.py");
                }}
        );

        if (StringUtils.isEmpty(System.getenv("PYTHON_POST_PROCESS_FILE"))) {
            LOGGER.info("Environment variable PYTHON_POST_PROCESS_FILE not defined so the Python code may not be properly formatted. To define it, try 'export PYTHON_POST_PROCESS_FILE=\"/usr/local/bin/yapf -i\"' (Linux/Mac)");
            LOGGER.info("NOTE: To enable file post-processing, 'enablePostProcessFile' must be set to `true` (--enable-post-process-file for CLI).");
        }

        boolean excludeTests = false;

        if (additionalProperties.containsKey(CodegenConstants.PACKAGE_NAME)) {
            setPackageName((String) additionalProperties.get(CodegenConstants.PACKAGE_NAME));
        }

        if (additionalProperties.containsKey(CodegenConstants.PROJECT_NAME)) {
            setProjectName((String) additionalProperties.get(CodegenConstants.PROJECT_NAME));
        } else {
            // default: set project based on package name
            // e.g. petstore_api (package name) => petstore-api (project name)
            setProjectName(packageName.replaceAll("_", "-"));
        }

        if (additionalProperties.containsKey(CodegenConstants.PACKAGE_VERSION)) {
            setPackageVersion((String) additionalProperties.get(CodegenConstants.PACKAGE_VERSION));
        }

        additionalProperties.put(CodegenConstants.PROJECT_NAME, projectName);
        additionalProperties.put(CodegenConstants.PACKAGE_NAME, packageName);
        additionalProperties.put(CodegenConstants.PACKAGE_VERSION, packageVersion);

        if (additionalProperties.containsKey(CodegenConstants.EXCLUDE_TESTS)) {
            excludeTests = Boolean.parseBoolean(additionalProperties.get(CodegenConstants.EXCLUDE_TESTS).toString());
        }

        boolean generateSourceCodeOnly = false;
        if (additionalProperties.containsKey(CodegenConstants.SOURCECODEONLY_GENERATION)) {
            generateSourceCodeOnly = Boolean.parseBoolean(additionalProperties.get(CodegenConstants.SOURCECODEONLY_GENERATION).toString());
        }

        // make api and model doc path available in templates
        additionalProperties.put("apiDocPath", apiDocPath);
        additionalProperties.put("modelDocPath", modelDocPath);

        if (additionalProperties.containsKey(PACKAGE_URL)) {
            setPackageUrl((String) additionalProperties.get(PACKAGE_URL));
        }

        if (additionalProperties.containsKey(USE_NOSE)) {
            setUseNose((String) additionalProperties.get(USE_NOSE));
        }

        // check to see if setRecursionLimit is set and whether it's an integer
        if (additionalProperties.containsKey(RECURSION_LIMIT)) {
            try {
                Integer.parseInt((String) additionalProperties.get(RECURSION_LIMIT));
            } catch (NumberFormatException | NullPointerException e) {
                throw new IllegalArgumentException("recursionLimit must be an integer, e.g. 2000.");
            }
        }

        if (additionalProperties.containsKey(CodegenConstants.NON_COMPLIANT_USE_DISCR_IF_COMPOSITION_FAILS)) {
            nonCompliantUseDiscrIfCompositionFails = Boolean.parseBoolean(
                    additionalProperties.get(CodegenConstants.NON_COMPLIANT_USE_DISCR_IF_COMPOSITION_FAILS).toString()
            );
        }

        String readmePath = "README.md";
        String readmeTemplate = "README.hbs";
        if (generateSourceCodeOnly) {
            readmePath = packagePath() + "_" + readmePath;
            readmeTemplate = "README_onlypackage.hbs";
        }
        supportingFiles.add(new SupportingFile(readmeTemplate, "", readmePath));
        supportingFiles.add(new SupportingFile("migration_2_0_0.hbs", "", "migration_2_0_0.md"));
        supportingFiles.add(new SupportingFile("migration_3_0_0.hbs", "", "migration_3_0_0.md"));
        supportingFiles.add(new SupportingFile("migration_other_python_generators.hbs", "", "migration_other_python_generators.md"));
        supportingFiles.add(new SupportingFile("__init__package.hbs", packagePath(), "__init__.py"));
        supportingFiles.add(new SupportingFile("__init__.hbs", packagePath(), "py.typed"));

        if (!generateSourceCodeOnly) {
            supportingFiles.add(new SupportingFile("tox.hbs", "", "tox.ini"));
            supportingFiles.add(new SupportingFile("test-requirements.hbs", "", "test-requirements.txt"));

            supportingFiles.add(new SupportingFile("git_push.hbs", "", "git_push.sh"));
            supportingFiles.add(new SupportingFile("gitignore.hbs", "", ".gitignore"));
            supportingFiles.add(new SupportingFile("travis.hbs", "", ".travis.yml"));
            supportingFiles.add(new SupportingFile("gitlab-ci.hbs", "", ".gitlab-ci.yml"));
            supportingFiles.add(new SupportingFile("pyproject.hbs", "", "pyproject.toml"));
        }
        // configurations package
        supportingFiles.add(new SupportingFile("__init__.hbs", packagePath() + File.separatorChar + "configurations", "__init__.py"));
        supportingFiles.add(new SupportingFile("configurations" + File.separatorChar + "schema_configuration.hbs", packagePath() + File.separatorChar + "configurations", "schema_configuration.py"));
        supportingFiles.add(new SupportingFile("configurations" + File.separatorChar + "api_configuration.hbs", packagePath() + File.separatorChar + "configurations", "api_configuration.py"));

        // If the package name consists of dots(openapi.client), then we need to create the directory structure like openapi/client with __init__ files.
        String[] packageNameSplits = packageName.split("\\.");
        String currentPackagePath = "";
        for (int i = 0; i < packageNameSplits.length - 1; i++) {
            if (i > 0) {
                currentPackagePath = currentPackagePath + File.separatorChar;
            }
            currentPackagePath = currentPackagePath + packageNameSplits[i];
            supportingFiles.add(new SupportingFile("__init__.hbs", currentPackagePath, "__init__.py"));
        }

        supportingFiles.add(new SupportingFile("exceptions.hbs", packagePath(), "exceptions.py"));

        // shared_imports
        supportingFiles.add(new SupportingFile("__init__.hbs", packagePath() + File.separator + "shared_imports", "__init__.py"));
        supportingFiles.add(new SupportingFile("shared_imports/header_imports.hbs", packagePath() + File.separator + "shared_imports", "header_imports.py"));
        supportingFiles.add(new SupportingFile("shared_imports/response_imports.hbs", packagePath() + File.separator + "shared_imports", "response_imports.py"));
        supportingFiles.add(new SupportingFile("shared_imports/schema_imports.hbs", packagePath() + File.separator + "shared_imports", "schema_imports.py"));
        supportingFiles.add(new SupportingFile("shared_imports/security_scheme_imports.hbs", packagePath() + File.separator + "shared_imports", "security_scheme_imports.py"));
        supportingFiles.add(new SupportingFile("shared_imports/server_imports.hbs", packagePath() + File.separator + "shared_imports", "server_imports.py"));
        supportingFiles.add(new SupportingFile("shared_imports/operation_imports.hbs", packagePath() + File.separator + "shared_imports", "operation_imports.py"));

        if (Boolean.FALSE.equals(excludeTests)) {
            supportingFiles.add(new SupportingFile("__init__.hbs", testFolder, "__init__.py"));
            supportingFiles.add(new SupportingFile("__init__.hbs", testFolder + File.separator + modelPackage.replace('.', File.separatorChar), "__init__.py"));
            supportingFiles.add(new SupportingFile("__init__.hbs", testFolder + File.separator + "components", "__init__.py"));
        }

        supportingFiles.add(new SupportingFile("api_client.hbs", packagePath(), "api_client.py"));
        supportingFiles.add(new SupportingFile("api_response.hbs", packagePath(), "api_response.py"));
        supportingFiles.add(new SupportingFile("rest.hbs", packagePath(), "rest.py"));
        supportingFiles.add(new SupportingFile("schemas/__init__.hbs", packagePath() + File.separator + "schemas", "__init__.py"));
        supportingFiles.add(new SupportingFile("schemas/validation.hbs", packagePath() + File.separator + "schemas", "validation.py"));
        supportingFiles.add(new SupportingFile("schemas/schema.hbs", packagePath() + File.separator + "schemas", "schema.py"));
        supportingFiles.add(new SupportingFile("schemas/schemas.hbs", packagePath() + File.separator + "schemas", "schemas.py"));
        supportingFiles.add(new SupportingFile("schemas/format.hbs", packagePath() + File.separator + "schemas", "format.py"));
        supportingFiles.add(new SupportingFile("schemas/original_immutabledict.hbs", packagePath() + File.separator + "schemas", "original_immutabledict.py"));
        supportingFiles.add(new SupportingFile("security_schemes.hbs", packagePath(), "security_schemes.py"));
        supportingFiles.add(new SupportingFile("server.hbs", packagePath(), "server.py"));

        // add the models and apis folders
        Boolean generateModels = (Boolean) additionalProperties().get(CodegenConstants.GENERATE_MODELS);
        if (Boolean.TRUE.equals(generateModels)) {
            supportingFiles.add(new SupportingFile("components/schemas/__init__schemas.hbs", packagePath() + File.separator + "components" + File.separator + "schemas", "__init__.py"));
        }
    }

    @Override
    public String toApiName(String name) {
        if (name.isEmpty()) {
            return "DefaultApi";
        }
        return toModelName(name, null) + apiNameSuffix;
    }

    @Override
    public String toModuleFilename(String name, String jsonPath) {
        // underscore the model file name
        // PhoneNumber => phone_number
        return underscore(dropDots(toModelName(name, jsonPath)));
    }

    protected String toSecurityPascalCase(String basename, String jsonPath) {
        return "Security";
    }

    @Override
    public String toContentTypeFilename(String name) {
        return toModuleFilename(name, null);
    }

    /*
    This method requires jsonPath to be passed in
    It handles responses and schemas
     */
    @Override
    public String toModelName(String name, String jsonPath) {
        boolean rootEntity = (jsonPath != null && jsonPath.endsWith(name));
        PairCacheKey key = new PairCacheKey(name, jsonPath);
        if (modelNameCache.containsKey(key)) {
            return modelNameCache.get(key);
        }
        String sanitizedName = sanitizeName(name);
        // remove dollar sign
        sanitizedName = sanitizedName.replaceAll("$", "");
        // remove whitespace
        sanitizedName = sanitizedName.replaceAll("\\s+", "");

        String nameWithPrefixSuffix = sanitizedName;
        if (!StringUtils.isEmpty(modelNamePrefix)) {
            // add '_' so that model name can be camelized correctly
            nameWithPrefixSuffix = modelNamePrefix + "_" + nameWithPrefixSuffix;
        }

        if (!StringUtils.isEmpty(modelNameSuffix)) {
            // add '_' so that model name can be camelized correctly
            nameWithPrefixSuffix = nameWithPrefixSuffix + "_" + modelNameSuffix;
        }

        // camelize the model name
        // phone_number => PhoneNumber
        String camelizedName = camelize(nameWithPrefixSuffix);
        if (camelizedName.isEmpty()) {
            // happens with a name like "/"
            camelizedName = camelize(toEnumVarName(name, null).toLowerCase(Locale.ROOT));
        }

        String[] pathPieces;
        boolean isComponent = false;
        if (jsonPath != null) {
            pathPieces = jsonPath.split("/");
            // #/components/schemas/blah -> size 4
            if (pathPieces.length == 4 && jsonPath.startsWith("#/components/")) {
                isComponent = true;
            }
        }

        // model name cannot use reserved keyword, e.g. return
        if (isReservedWord(camelizedName)) {
            String modelName = "_" + camelizedName; // e.g. return => ModelReturn (after camelize)
            if (isComponent && rootEntity) {
                LOGGER.warn("{} (reserved word) cannot be used as name. Renamed to {}", camelizedName, modelName);
            }
            modelNameCache.put(key, modelName);
            return modelName;
        }


        // model name starts with number
        if (camelizedName.matches("^\\d.*")) {
            String modelName = "_" + camelizedName; // e.g. return => ModelReturn (after camelize)
            if (isComponent && rootEntity) {
                LOGGER.warn("{} (component name starts with number) cannot be used as name. Renamed to {}", camelizedName, modelName);
            }
            modelNameCache.put(key, modelName);
            return modelName;
        }

        modelNameCache.put(key, camelizedName);
        return camelizedName;
    }

    /**
     * Configures a friendly name for the generator.  This will be used by the
     * generator to select the library with the -g flag.
     *
     * @return the friendly name for the generator
     */
    @Override
    public String getName() {
        return "python";
    }

    @Override
    public String getHelp() {
        return String.join("<br />",
                "Generates a Python client library",
                "",
                "Features in this generator:",
                "- type hints on endpoints and model creation",
                "- model parameter names use the spec defined keys and cases",
                "- robust composition (oneOf/anyOf/allOf/not) where payload data is stored in one instance only",
                "- endpoint parameter names use the spec defined keys and cases",
                "- inline schemas are supported at any location including composition",
                "- multiple content types supported in request body and response bodies",
                "- run time type checking + json schema validation",
                "- json schema keyword validation may be selectively disabled with SchemaConfiguration",
                "- enums of type string/integer/boolean typed using typing.Literal",
                "- mypy static type checking run on generated sample",
                "- Sending/receiving decimals as strings supported with type:string format: number -> DecimalSchema",
                "- Sending/receiving uuids as strings supported with type:string format: uuid -> UUIDSchema",
                "- quicker load time for python modules (a single endpoint can be imported and used without loading others)",
                "- composed schemas with type constraints supported (type:object + oneOf/anyOf/allOf)",
                "- schemas are not coerced/cast. For example string + date are both stored as string, and there is a date accessor");
    }

    public String pythonDate(Object dateValue) {
        String strValue;
        if (dateValue instanceof OffsetDateTime) {
            OffsetDateTime date;
            try {
                date = (OffsetDateTime) dateValue;
            } catch (ClassCastException e) {
                LOGGER.warn("Invalid `date` format for value {}", dateValue.toString());
                date = ((Date) dateValue).toInstant().atOffset(ZoneOffset.UTC);
            }
            strValue = date.format(iso8601Date);
        } else {
            strValue = dateValue.toString();
        }
        return strValue;
    }

    public String pythonDateTime(Object dateTimeValue) {
        String strValue;
        if (dateTimeValue instanceof OffsetDateTime) {
            OffsetDateTime dateTime;
            try {
                dateTime = (OffsetDateTime) dateTimeValue;
            } catch (ClassCastException e) {
                LOGGER.warn("Invalid `date-time` format for value {}", dateTimeValue.toString());
                dateTime = ((Date) dateTimeValue).toInstant().atOffset(ZoneOffset.UTC);
            }
            strValue = dateTime.format(iso8601DateTime);
        } else {
            strValue = dateTimeValue.toString();
        }
        return strValue;
    }

    @Override
    public String toModelImport(String refClass) {
        // name looks like cat.Cat
        String[] refClassPieces = refClass.split("\\.");
        if (refClassPieces.length != 2) {
            return null;
        }
        String modelModule = refClassPieces[0];
        return "from " + packageName + "." +  modelPackage() + " import " + modelModule;
    }

    /***
     * Override with special post-processing for all models.
     * we have a custom version of this method to:
     * - remove any primitive models that do not contain validations
     *      these models are unaliased as inline definitions wherever the spec has them as refs
     *      this means that the generated client does not use these models
     *      because they are not used we do not write them
     * - fix the model imports, go from model name to the full import string with toModelImport + globalImportFixer
     * Also cleans the test folder if test cases exist and the testFolder is set because the tests are autogenerated
     *
     * @param models a map going from the model name to an object holding the model info
     * @return the updated models
     */
    @Override
    public TreeMap<String, CodegenSchema> postProcessAllModels(TreeMap<String, CodegenSchema> models) {
        super.postProcessAllModels(models);

        boolean anyModelContainsTestCases = false;
        for (CodegenSchema cm : models.values()) {
            if (cm.testCases != null && !cm.testCases.isEmpty()) {
                anyModelContainsTestCases = true;
                break;
            }
        }
        boolean testFolderSet = testFolder != null;
        if (testFolderSet && anyModelContainsTestCases) {
            // delete the test folder because tests there will be autogenerated
            String testPath = outputFolder + File.separatorChar + testFolder;
            File testDirectory = new File(testPath);
            try {
                FileUtils.cleanDirectory(testDirectory);
            } catch (IOException e) {
                LOGGER.info("Unable to delete the test folder because of exception=" + e);
            }

        }

        return models;
    }

    protected boolean isValid(String name) {
        boolean isValid = super.isValid(name);
        if (!isValid) {
            return false;
        }
        return name.matches("^[_a-zA-Z]\\w*$");
    }

    /**
     * Convert OAS Property object to Codegen Property object
     * We have a custom version of this method to always set allowableValues.enumVars on all enum variables
     * Together with unaliasSchema this sets primitive types with validations as models
     * This method is used by fromResponse
     *
     * @param p OAS property schema
     * @return Codegen Property object
     */
    @Override
    public CodegenSchema fromSchema(Schema p, String sourceJsonPath, String currentJsonPath) {
        // fix needed for values with /n /t etc. in them
        CodegenSchema cp = super.fromSchema(p, sourceJsonPath, currentJsonPath);
        if (cp.types != null && cp.types.contains("integer") && cp.format == null) {
            // this generator treats integers as type number
            // so integer validation info must be set using formatting
            cp.format = "int";
        }
        return cp;
    }

    /**
     * Return the sanitized variable name for enum
     *
     * @param value    enum variable name
     * @param prop property
     * @return the sanitized variable name for enum
     */
    @Override
    public String toEnumVarName(String value, Schema prop) {
        // our enum var names are keys in a python dict, so change spaces to underscores
        if (value.isEmpty()) {
            return "EMPTY";
        }
        if (value.equals("null")) {
            return "NONE";
        }

        // value is int or float
        String intPattern = "^[-+]?\\d+$";
        String floatPattern = "^[-+]?\\d+\\.\\d+$";
        Boolean intMatch = Pattern.matches(intPattern, value);
        Boolean floatMatch = Pattern.matches(floatPattern, value);
        if (intMatch || floatMatch) {
            String plusSign = "^\\+.+";
            String negSign = "^-.+";
            String enumVarName;
            if (Pattern.matches(plusSign, value)) {
                enumVarName = value.replace("+", "POSITIVE_");
            } else if (Pattern.matches(negSign, value)) {
                enumVarName = value.replace("-", "NEGATIVE_");
            } else {
                enumVarName = "POSITIVE_" + value;
            }
            if (floatMatch) {
                enumVarName = enumVarName.replace(".", "_PT_");
            }
            return enumVarName;
        }

        // every character in value is not allowed
        String valueWithAllowedCharsOnly = value.replaceAll("^\\W+", "");
        if (valueWithAllowedCharsOnly.isEmpty()) {
            StringBuilder usedValueBuilder = new StringBuilder();
            for (int i = 0; i < value.length(); i++){
                char c = value.charAt(i);
                String charName = Character.getName(Character.hashCode(c));
                if (usedValueBuilder.length() > 0) {
                    usedValueBuilder.append("_");
                }
                usedValueBuilder.append(charNameToVarName(charName));
            }
            return usedValueBuilder.toString();
        }

        String usedValue = value;
        // Replace " " with _
        usedValue = usedValue.replaceAll("[ ]+", "_");

        // replace all invalid characters with their character name descriptions
        Pattern nonWordCharPattern = Pattern.compile("\\W+");
        Matcher matcher = nonWordCharPattern.matcher(usedValue);
        Stack<AbstractMap.SimpleEntry<Integer, String>> matchStartToGroup = new Stack<>();
        while (matcher.find()) {
            matchStartToGroup.add(new AbstractMap.SimpleEntry<>(matcher.start(), matcher.group()));
        }
        char underscore = '_';
        while (!matchStartToGroup.isEmpty()) {
            AbstractMap.SimpleEntry<Integer, String> entry = matchStartToGroup.pop();
            Integer startIndex = entry.getKey();
            String match = entry.getValue();
            String prefix = "";
            String suffix = "";
            if (startIndex > 0 && usedValue.charAt(startIndex-1) != underscore) {
                prefix = "_";
            }
            int indexAfter = startIndex + match.length();
            if (startIndex + match.length() < usedValue.length() && usedValue.charAt(indexAfter) != underscore) {
                suffix = "_";
            }
            StringBuilder convertedMatch = new StringBuilder();
            for (int i = 0; i < match.length(); i++) {
                String charName = charNameToVarName(Character.getName(Character.hashCode(match.charAt(i))));
                convertedMatch.append(charName);
                if (i != match.length() - 1) {
                    convertedMatch.append("_");
                }
            }
            String replacement = prefix + convertedMatch + suffix;
            usedValue = usedValue.substring(0, startIndex) + replacement + usedValue.substring(indexAfter);
        }

        // add camel case underscore
        String regex = "([a-z])([A-Z]+)";
        String regexReplacement = "$1_$2";
        usedValue = usedValue.replaceAll(regex, regexReplacement);

        // uppercase
        usedValue = usedValue.toUpperCase(Locale.ROOT);

        if (usedValue.length() > 1) {
            // remove trailing _
            usedValue = usedValue.replaceAll("_$", "");
        }
        return usedValue;
    }

    protected String toTestCaseName(String specTestCaseName) {
        return CaseFormat.UPPER_CAMEL.to(CaseFormat.LOWER_UNDERSCORE, specTestCaseName);
    }

    @Override
    public String escapeUnsafeCharacters(String value) {
        // handles escape characters and the like
        String stringValue = value;
        String backslash = "\\";
        if (stringValue.contains(backslash)) {
            stringValue = stringValue.replace(backslash, "\\\\");
        }
        String nullChar = "\0";
        if (stringValue.contains(nullChar)) {
            stringValue = stringValue.replace(nullChar, "\\x00");
        }
        String doubleQuoteChar = "\"";
        if (stringValue.contains(doubleQuoteChar)) {
            stringValue = stringValue.replace(doubleQuoteChar, "\\\"");
        }
        String lineSep = System.lineSeparator();
        if (stringValue.contains(lineSep)) {
            stringValue = stringValue.replace(lineSep, "\\n");
        }
        String carriageReturn = "\r";
        if (stringValue.contains(carriageReturn)) {
            stringValue = stringValue.replace(carriageReturn, "\\r");
        }
        String tab = "\t";
        if (stringValue.contains(tab)) {
            stringValue = stringValue.replace(tab, "\\t");
        }
        String formFeed = "\f";
        if (stringValue.contains(formFeed)) {
            stringValue = stringValue.replace(formFeed, "\\f");
        }
        return stringValue;
    }

    public String getRefClassWithRefModule(Schema sc) {
        String ref = sc.get$ref();
        if (ref != null) {
            return toRefModule(ref, null, "schemas") + "." + toRefClass(ref, null, "schemas");
        }
        return null;
    }

    /**
     * Gets an example if it exists
     *
     * @param sc input schema
     * @return the example value
     */
    protected Object getObjectExample(Schema sc) {
        Schema schema = sc;
        String ref = sc.get$ref();
        if (ref != null) {
            schema = ModelUtils.getSchema(this.openAPI, ModelUtils.getSimpleRef(ref));
        }
        if (schema == null) {
            return null;
        }
        // TODO handle examples in object models in the future
        boolean objectModel = (ModelUtils.isObjectSchema(schema) || ModelUtils.isMapSchema(schema) || ModelUtils.isComposedSchema(schema));
        if (objectModel) {
            return null;
        }
        if (schema.getExample() != null) {
            return schema.getExample();
        }
        if (schema.getDefault() != null) {
            return schema.getDefault();
        } else if (schema.getEnum() != null && !schema.getEnum().isEmpty()) {
            return schema.getEnum().get(0);
        }
        return null;
    }

    /***
     * Ensures that the string has a leading and trailing quote
     *
     * @param in input string
     * @return quoted string
     */
    private String ensureQuotes(String in) {
        String strPattern = "^['\"].*?['\"]$";
        if (in.matches(strPattern)) {
            return in;
        }
        return "\"" + in + "\"";
    }

    @Override
    public String toExampleValue(Schema schema) {
        String modelName = getRefClassWithRefModule(schema);
        Object objExample = getObjectExample(schema);
        return toExampleValueRecursive(modelName, schema, objExample, 1, "", 0, new ArrayList<>());
    }

    @Override
    public String toExampleValue(Schema schema, Object objExample) {
        String modelName = getRefClassWithRefModule(schema);
        return toExampleValueRecursive(modelName, schema, objExample, 1, "", 0, new ArrayList<>());
    }

    private Boolean simpleStringSchema(Schema schema) {
        Schema sc = schema;
        String ref = schema.get$ref();
        if (ref != null) {
            sc = ModelUtils.getSchema(this.openAPI, ModelUtils.getSimpleRef(ref));
        }
        if (sc == null) {
            return Boolean.FALSE;
        }
        return ModelUtils.isStringSchema(sc) && !ModelUtils.isDateSchema(sc) && !ModelUtils.isDateTimeSchema(sc) && !"Number".equalsIgnoreCase(sc.getFormat()) && !ModelUtils.isByteArraySchema(sc) && !ModelUtils.isBinarySchema(sc) && schema.getPattern() == null;
    }

    private String getSchemaName(String complexType) {
        String[] packageNameSplits = complexType.split("\\.");
        if (packageNameSplits.length == 1) {
            return packageNameSplits[0];
        }
        return packageNameSplits[1];
    }

    private MappedModel getDiscriminatorMappedModel(CodegenDiscriminator disc) {
        for (MappedModel mm : disc.mappedModels) {
            String complexType = mm.modelName;
            String schemaName = getSchemaName(complexType);
            Schema modelSchema = getModelNameToSchemaCache().get(schemaName);
            if (ModelUtils.isObjectSchema(modelSchema)) {
                return mm;
            }
        }
        return null;
    }

    /***
     * Recursively generates string examples for schemas
     *
     * @param modelName the string name of the refed model that will be generated for the schema or null
     * @param schema the schema that we need an example for
     * @param objExample the example that applies to this schema, for now only string example are used
     * @param indentationLevel integer indentation level that we are currently at
     *                         we assume the indentation amount is 4 spaces times this integer
     * @param prefix the string prefix that we will use when assigning an example for this line
     *               this is used when setting key: value, pairs "key: " is the prefix
     *               and this is used when setting properties like some_property='some_property_example'
     * @param exampleLine this is the current line that we are generating an example for, starts at 0
     *                    we don't indent in the 0th line because using the example value looks like:
     *                    prop = ModelName( line 0
     *                        some_property='some_property_example' line 1
     *                    ) line 2
     *                    and our example value is:
     *                    ModelName( line 0
     *                        some_property='some_property_example' line 1
     *                    ) line 2
     * @param includedSchemas are a list of schemas that we have moved through to get here. If the new schemas that we
     *                        are looking at is in includedSchemas then we have hit a cycle.
     * @return the string example
     */
    private String toExampleValueRecursive(String modelName, Schema schema, Object objExample, int indentationLevel, String prefix, Integer exampleLine, List<Schema> includedSchemas) {
        boolean couldHaveCycle = !includedSchemas.isEmpty() && potentiallySelfReferencingSchema(schema);
        // If we have seen the ContextAwareSchemaNode more than once before, we must be in a cycle.
        boolean cycleFound = false;
        if (couldHaveCycle) {
            cycleFound = includedSchemas.subList(0, includedSchemas.size()-1).stream().anyMatch(schema::equals);
        }
        final String indentionConst = "    ";
        StringBuilder currentIndentation = new StringBuilder();
        String closingIndentation;
        currentIndentation.append(indentionConst.repeat(Math.max(0, indentationLevel)));
        if (exampleLine.equals(0)) {
            closingIndentation = currentIndentation.toString();
            currentIndentation = new StringBuilder();
        } else {
            closingIndentation = currentIndentation.toString();
        }
        String openChars = "";
        String closeChars = "";
        if (modelName != null) {
            openChars = modelName + ".validate(";
            closeChars = ")";
            if (ModelUtils.isTypeObjectSchema(schema)) {
                openChars = openChars + "{";
                closeChars = "}" + closeChars;
            }
        }

        String fullPrefix = currentIndentation + prefix + openChars;

        String example = null;
        if (objExample != null) {
            example = objExample.toString();
        }
        if (null != schema.get$ref()) {
            Map<String, Schema> allDefinitions = new HashMap<>();
            Components components = this.openAPI.getComponents();
            if (components != null && components.getSchemas() != null) {
                allDefinitions = components.getSchemas();
            }
            String refValue = schema.get$ref();
            String ref = ModelUtils.getSimpleRef(refValue);
            Schema refSchema = allDefinitions.get(ref);
            if (null == refSchema) {
                if (refValue.startsWith("#/components/schemas/")) {
                    LOGGER.warn("Unable to find referenced schema " + refValue + "\n");
                }
                // TODO get examples working for refs like
                // #/paths/~1fake~1parameterCollisions~1{1}~1{aB}~1{Ab}~1{self}~1{A-B}~1/post/parameters/5/schema
                // #/components/responses/SuccessInlineContentAndHeader/headers/someHeader/schema
                return fullPrefix + "None" + closeChars;
            }
            String refModelName = getRefClassWithRefModule(schema);
            return toExampleValueRecursive(refModelName, refSchema, objExample, indentationLevel, prefix, exampleLine, includedSchemas);
        } else if (ModelUtils.isNullType(schema)) {
            // The 'null' type is allowed in OAS 3.1 and above. It is not supported by OAS 3.0.x,
            // though this tooling supports it.
            return fullPrefix + "None" + closeChars;
        } else if (ModelUtils.isAnyType(schema)) {
            /*
             This schema may be a composed schema
             TODO generate examples for some of these use cases in the future like
             only oneOf without a discriminator
             */
            if (cycleFound) {
                return "";
            }
            boolean hasProperties = (schema.getProperties() != null && !schema.getProperties().isEmpty());
            CodegenDiscriminator disc = createDiscriminator(modelName, schema, openAPI, "");
            if (ModelUtils.isComposedSchema(schema)) {
                if(includedSchemas.contains(schema)) {
                    return "";
                }
                includedSchemas.add(schema);
                // complex composed object type schemas not yet handled and the code returns early
                if (hasProperties) {
                    // what if this composed schema defined properties + allOf?
                    // or items + properties, both a list and a dict could be accepted as payloads
                    return fullPrefix + "{}" + closeChars;
                }
                ComposedSchema cs = (ComposedSchema) schema;
                int allOfExists = 0;
                if (cs.getAllOf() != null && !cs.getAllOf().isEmpty()) {
                    allOfExists = 1;
                }
                int anyOfExists = 0;
                if (cs.getAnyOf() != null && !cs.getAnyOf().isEmpty()) {
                    anyOfExists = 1;
                }
                int oneOfExists = 0;
                if (cs.getOneOf() != null && !cs.getOneOf().isEmpty()) {
                    oneOfExists = 1;
                }
                if (allOfExists + anyOfExists + oneOfExists > 1) {
                    // what if it needs one oneOf schema, one anyOf schema, and two allOf schemas?
                    return fullPrefix + "None" + closeChars;
                }
                // for now only oneOf with discriminator is supported
                if (!(oneOfExists == 1 && disc != null)) {
                    return fullPrefix + "None" + closeChars;
                }
            }
            if (disc != null) {
                // a discriminator means that this is object type
                MappedModel mm = getDiscriminatorMappedModel(disc);
                if (mm == null) {
                    return fullPrefix + "None" + closeChars;
                }
                String discPropNameValue = mm.mappingName;
                String schemaName = getSchemaName(mm.modelName);
                Schema modelSchema = getModelNameToSchemaCache().get(schemaName);
                CodegenSchema cp = new CodegenSchema();
                cp.jsonPathPiece = getKey(disc.propertyName.original, "misc", null);
                cp.example = discPropNameValue;
                return exampleForObjectModel(modelSchema, fullPrefix, closeChars, cp, indentationLevel, exampleLine, closingIndentation, includedSchemas);
            }
            return fullPrefix + "None" + closeChars;
        } else if (ModelUtils.isBooleanSchema(schema)) {
            if (example == null) {
                example = "True";
            } else {
                if ("false".equalsIgnoreCase(objExample.toString())) {
                    example = "False";
                } else {
                    example = "True";
                }
            }
            return fullPrefix + example + closeChars;
        } else if (ModelUtils.isStringSchema(schema)) {
            if (example != null) {
                return fullPrefix + ensureQuotes(escapeUnsafeCharacters(example)) + closeChars;
            }
            if (ModelUtils.isDateSchema(schema)) {
                example = pythonDate(Objects.requireNonNullElse(objExample, "1970-01-01"));
            } else if (ModelUtils.isDateTimeSchema(schema)) {
                example = pythonDateTime(Objects.requireNonNullElse(objExample, "1970-01-01T00:00:00.00Z"));
            } else if (ModelUtils.isBinarySchema(schema)) {
                if (objExample == null) {
                    example = "/path/to/file";
                }
                example = "open('" + example + "', 'rb')";
                return fullPrefix + example + closeChars;
            } else if (ModelUtils.isByteArraySchema(schema)) {
                if (objExample == null) {
                    example = "'YQ=='";
                }
            } else if ("Number".equalsIgnoreCase(schema.getFormat())) {
                // a BigDecimal:
                example = "2";
            } else if (StringUtils.isNotBlank(schema.getPattern())) {
                String pattern = schema.getPattern();
                CodegenPatternInfo results = getPatternInfo(pattern);
                String extractedPattern = results.pattern.original;
                LinkedHashSet<String> regexFlags = results.flags;
                /*
                RxGen does not support our ECMA dialect https://github.com/curious-odd-man/RgxGen/issues/56
                So strip off the leading / and trailing / and turn on ignore case if we have it
                 */
                RgxGen rgxGen;
                if (regexFlags != null && regexFlags.contains("i")) {
                    rgxGen = new RgxGen(extractedPattern);
                    RgxGenProperties properties = new RgxGenProperties();
                    RgxGenOption.CASE_INSENSITIVE.setInProperties(properties, true);
                    rgxGen.setProperties(properties);
                } else {
                    rgxGen = new RgxGen(extractedPattern);
                }

                // this seed makes it so if we have [a-z] we pick a
                Random random = new Random(18);
                example = rgxGen.generate(random);
            } else if (schema.getMinLength() != null) {
                example = "";
                int len = schema.getMinLength();
                example = example + "a".repeat(Math.max(0, len));
            } else if (ModelUtils.isUUIDSchema(schema)) {
                example = "046b6c7f-0b8a-43b9-b35d-6489e6daee91";
            } else {
                example = "string_example";
            }
            assert example != null;
            return fullPrefix + ensureQuotes(example) + closeChars;
        } else if (ModelUtils.isIntegerSchema(schema)) {
            if (objExample == null) {
                if (schema.getMinimum() != null) {
                    example = schema.getMinimum().toString();
                } else {
                    example = "1";
                }
            }
            return fullPrefix + example + closeChars;
        } else if (ModelUtils.isNumberSchema(schema)) {
            if (objExample == null) {
                if (schema.getMinimum() != null) {
                    example = schema.getMinimum().toString();
                } else {
                    example = "3.14";
                }
            }
            return fullPrefix + example + closeChars;
        } else if (ModelUtils.isArraySchema(schema)) {
            if (objExample instanceof Iterable) {
                // If the example is already a list, return it directly instead of wrongly wrap it in another list
                return fullPrefix + objExample + closeChars;
            }
            if (ModelUtils.isComposedSchema(schema)) {
                // complex composed array type schemas not yet handled and the code returns early
                return fullPrefix + "[]" + closeChars;
            }
            ArraySchema arrayschema = (ArraySchema) schema;
            Schema itemSchema = arrayschema.getItems();
            String itemModelName = getRefClassWithRefModule(itemSchema);
            if(includedSchemas.contains(schema)) {
                return "";
            }
            includedSchemas.add(schema);
            String itemExample = toExampleValueRecursive(itemModelName, itemSchema, objExample, indentationLevel + 1, "", exampleLine + 1, includedSchemas);
            if (StringUtils.isEmpty(itemExample) || cycleFound) {
                return fullPrefix + "[]" + closeChars;
            } else {
                return fullPrefix + "[" + "\n" + itemExample + "\n" + closingIndentation + "]" + closeChars;
            }
        } else if (ModelUtils.isTypeObjectSchema(schema)) {
            if (modelName == null) {
                fullPrefix += "{";
                closeChars = "}";
            }
            if (cycleFound) {
                return fullPrefix + closeChars;
            }
            boolean hasProperties = (schema.getProperties() != null && !schema.getProperties().isEmpty());
            CodegenDiscriminator disc = createDiscriminator(modelName, schema, openAPI, "");
            if (ModelUtils.isComposedSchema(schema)) {
                // complex composed object type schemas not yet handled and the code returns early
                if (hasProperties) {
                    // what if this composed schema defined properties + allOf?
                    return fullPrefix + closeChars;
                }
                ComposedSchema cs = (ComposedSchema) schema;
                int allOfExists = 0;
                if (cs.getAllOf() != null && !cs.getAllOf().isEmpty()) {
                    allOfExists = 1;
                }
                int anyOfExists = 0;
                if (cs.getAnyOf() != null && !cs.getAnyOf().isEmpty()) {
                    anyOfExists = 1;
                }
                int oneOfExists = 0;
                if (cs.getOneOf() != null && !cs.getOneOf().isEmpty()) {
                    oneOfExists = 1;
                }
                if (allOfExists + anyOfExists + oneOfExists > 1) {
                    // what if it needs one oneOf schema, one anyOf schema, and two allOf schemas?
                    return fullPrefix + closeChars;
                }
                // for now only oneOf with discriminator is supported
                if (!(oneOfExists == 1 && disc != null)) {
                    return fullPrefix + closeChars;
                }
            }
            if (disc != null) {
                MappedModel mm = getDiscriminatorMappedModel(disc);
                if (mm == null) {
                    return fullPrefix + closeChars;
                }
                String discPropNameValue = mm.mappingName;
                String schemaName = getSchemaName(mm.modelName);
                Schema modelSchema = getModelNameToSchemaCache().get(schemaName);
                CodegenSchema cp = new CodegenSchema();
                cp.jsonPathPiece = getKey(disc.propertyName.original, "misc", null);
                cp.example = discPropNameValue;
                return exampleForObjectModel(modelSchema, fullPrefix, closeChars, cp, indentationLevel, exampleLine, closingIndentation, includedSchemas);
            }
            Object addPropsObj = schema.getAdditionalProperties();
            if (hasProperties) {
                return exampleForObjectModel(schema, fullPrefix, closeChars, null, indentationLevel, exampleLine, closingIndentation, includedSchemas);
            } else if (addPropsObj instanceof Schema) {
                // TODO handle true case for additionalProperties
                Schema addPropsSchema = (Schema) addPropsObj;
                String key = "key";
                Object addPropsExample = getObjectExample(addPropsSchema);
                if (addPropsSchema.getEnum() != null && !addPropsSchema.getEnum().isEmpty()) {
                    key = addPropsSchema.getEnum().get(0).toString();
                }
                addPropsExample = exampleFromStringOrArraySchema(addPropsSchema, addPropsExample, key);
                String addPropPrefix = ensureQuotes(key) + ": ";
                String addPropsModelName = getRefClassWithRefModule(addPropsSchema);
                if(includedSchemas.contains(schema)) {
                    return "";
                }
                includedSchemas.add(schema);

                example = fullPrefix + "\n" + toExampleValueRecursive(addPropsModelName, addPropsSchema, addPropsExample, indentationLevel + 1, addPropPrefix, exampleLine + 1, includedSchemas) + ",\n" + closingIndentation + closeChars;
            } else {
                example = fullPrefix + closeChars;
            }
        } else {
            LOGGER.warn("Type " + schema.getType() + " not handled properly in toExampleValue");
        }

        return example;
    }

    private boolean potentiallySelfReferencingSchema(Schema schema) {
        return null != schema.get$ref() || ModelUtils.isArraySchema(schema) || ModelUtils.isMapSchema(schema) || ModelUtils.isObjectSchema(schema) || ModelUtils.isComposedSchema(schema);
    }

    private String exampleForObjectModel(Schema schema, String fullPrefix, String closeChars, CodegenSchema discProp, int indentationLevel, int exampleLine, String closingIndentation, List<Schema> includedSchemas) {

        Map<String, Schema> requiredAndOptionalProps = ((Schema<?>) schema).getProperties();
        if (requiredAndOptionalProps == null || requiredAndOptionalProps.isEmpty()) {
            return fullPrefix + closeChars;
        }

        if(includedSchemas.contains(schema)) {
            return "";
        }
        includedSchemas.add(schema);

        StringBuilder exampleBuilder = new StringBuilder(fullPrefix + "\n");
        for (Map.Entry<String, Schema> entry : requiredAndOptionalProps.entrySet()) {
            String propName = entry.getKey();
            Schema propSchema = entry.getValue();
            propName = toVarName(propName);
            String propModelName = null;
            Object propExample;
            if (discProp != null && propName.equals(discProp.jsonPathPiece.original)) {
                propExample = discProp.example;
            } else {
                propModelName = getRefClassWithRefModule(propSchema);
                propExample = exampleFromStringOrArraySchema(
                        propSchema,
                        null,
                        propName);
            }

            exampleBuilder.append(toExampleValueRecursive(propModelName,
                    propSchema,
                    propExample,
                    indentationLevel + 1,
                    "\"" + propName + "\": ",
                    exampleLine + 1,
                    includedSchemas)).append(",\n");
        }
        String example = exampleBuilder.toString();

        // TODO handle additionalProperties also
        example += closingIndentation + closeChars;
        return example;

    }

    private Object exampleFromStringOrArraySchema(Schema sc, Object currentExample, String propName) {
        if (currentExample != null) {
            return currentExample;
        }
        Schema schema = sc;
        if (sc == null) {
            return null;
        }
        String ref = sc.get$ref();
        if (ref != null) {
            schema = ModelUtils.getSchema(this.openAPI, ModelUtils.getSimpleRef(ref));
        }
        if (schema == null) {
            return null;
        }
        Object example = getObjectExample(schema);
        if (example != null) {
            return example;
        } else if (simpleStringSchema(schema)) {
            return propName + "_example";
        } else if (ModelUtils.isArraySchema(schema)) {
            ArraySchema arraySchema = (ArraySchema) schema;
            Schema itemSchema = arraySchema.getItems();
            example = getObjectExample(itemSchema);
            if (example != null) {
                return example;
            } else if (simpleStringSchema(itemSchema)) {
                return propName + "_example";
            }
        }
        return null;
    }


    /***
     * Set the codegenParameter example value
     * We have a custom version of this function, so we can invoke toExampleValue
     *
     * @param parameter the base parameter that came from the spec
     */
    @Override
    public String getParameterExampleValue(Parameter parameter) {
        Schema schema = parameter.getSchema();
        if (schema == null) {
            LOGGER.warn("CodegenParameter.example defaulting to null because parameter lacks a schema");
            return null;
        }

        Object example;
        if (parameter.getExtensions() != null && parameter.getExtensions().containsKey("x-example")) {
            example = parameter.getExtensions().get("x-example");
        } else if (parameter.getExample() != null) {
            example = parameter.getExample();
        } else if (parameter.getExamples() != null && !parameter.getExamples().isEmpty() && parameter.getExamples().values().iterator().next().getValue() != null) {
            example = parameter.getExamples().values().iterator().next().getValue();
        } else {
            example = getObjectExample(schema);
        }
        example = exampleFromStringOrArraySchema(schema, example, parameter.getName());
        return toExampleValue(schema, example);
    }

    /**
     * Return a map from model name to Schema for efficient lookup.
     *
     * @return map from model name to Schema.
     */
    protected Map<String, Schema> getModelNameToSchemaCache() {
        if (modelNameToSchemaCache == null) {
            // Create a cache to efficiently lookup schema based on model name.
            Map<String, Schema> m = new HashMap<>();
            ModelUtils.getSchemas(openAPI).forEach((key, schema) -> m.put(toModelName(key, null), schema));
            modelNameToSchemaCache = Collections.unmodifiableMap(m);
        }
        return modelNameToSchemaCache;
    }

    @Override
    public GeneratorType getTag() {
        return GeneratorType.CLIENT;
    }

    @Override
    public String toResponseModuleName(String componentName, String jsonPath) {
        String[] pathPieces = jsonPath.split("/");
        if (jsonPath.startsWith("#/components/responses")) {
            if (pathPieces.length == 3) {
                return "responses";
            }// #/components/responses/SomeResponse
            // #/components/responses/SomeResponse/content/schema
            String suffix = toModuleFilename(componentName, jsonPath);
            String spacer = "";
            if (!suffix.startsWith("_")) {
                spacer = "_";
            }
            return "response" + spacer + suffix;
        }
        if (pathPieces.length == 5) {// #/paths/somePath/verb/responses
            return "responses";
        }// #/paths/somePath/verb/responses/200
        // #/paths/somePath/verb/responses/200/content/schema
        return "response_" + componentName.toLowerCase(Locale.ROOT);
    }

    @Override
    public String toRequestBodyFilename(String componentName, String jsonPath) {
        if (jsonPath.startsWith("#/components")) {
            return toModuleFilename("request_body_" + componentName, null);
        }
        return toModuleFilename("request_body", null);
    }

    public String toHeaderFilename(String componentName, String jsonPath) {
        String[] pathPieces = jsonPath.split("/");
        if ((pathPieces.length == 5 || pathPieces.length == 7) && componentName.equals("headers")) {
            // #/components/responses/SomeResponse/headers
            // #/paths/somePath/verb/responses/200/headers
            return "headers";
        }
        return toModuleFilename("header_" + componentName, null);
    }

    public void setUseNose(String val) {
        this.useNose = Boolean.parseBoolean(val);
    }

    public void setPackageUrl(String packageUrl) {
        this.packageUrl = packageUrl;
    }

    public String packagePath() {
        // src is needed for modern packaging per
        // https://packaging.python.org/en/latest/tutorials/packaging-projects/
        return "src" + File.separatorChar + packageName.replace('.', File.separatorChar);
    }


    protected boolean needToImport(String refClass) {
        return refClass.contains(".");
    }

    @Override
    public String defaultTemplatingEngine() {
        return "handlebars";
    }

    @Override
    public String generatorLanguageVersion() { return ">=3.8"; }

    @Override
    public void preprocessOpenAPI(OpenAPI openAPI) {
        String originalSpecVersion;
        String xOriginalSwaggerVersion = "x-original-swagger-version";
        if (openAPI.getExtensions() != null && !openAPI.getExtensions().isEmpty() && openAPI.getExtensions().containsKey(xOriginalSwaggerVersion)) {
            originalSpecVersion = (String) openAPI.getExtensions().get(xOriginalSwaggerVersion);
        } else {
            originalSpecVersion = openAPI.getOpenapi();
        }
        int specMajorVersion = Integer.parseInt(originalSpecVersion.substring(0, 1));
        if (specMajorVersion < 3) {
            throw new RuntimeException("Your spec version of "+originalSpecVersion+" is too low. " + getName() + " only works with specs with version >= 3.X.X. Please use a tool like Swagger Editor or Swagger Converter to convert your spec to v3");
        }
    }

    public Map<String, Object> postProcessSupportingFileData(Map<String, Object> data) {
        data.put(CodegenConstants.NON_COMPLIANT_USE_DISCR_IF_COMPOSITION_FAILS, nonCompliantUseDiscrIfCompositionFails);
        return data;
    }

    @Override
    protected String getRefClassWithModule(String ref, String sourceJsonPath) {
        String refModule = toRefModule(ref, sourceJsonPath, "schemas");
        String refClass = toRefClass(ref, sourceJsonPath, "schemas");
        if (refModule == null) {
            return refClass;
        }
        return refModule + "." + refClass;
    }

    @Override
    public String toParameterFilename(String name, String jsonPath) {
        // adds prefix parameter_ onto the result so modules do not start with _
        try {
            Integer.parseInt(name);
            // for parameters in path, or an endpoint
            return "parameter_" + name;
        } catch (NumberFormatException nfe) {
            // for header parameters in responses
            return "parameter_" + toModuleFilename(name, null);
        }
    }

    @Override
    public String toSecuritySchemeFilename(String basename, String jsonPath) {
        return "security_scheme_" + toModuleFilename(basename, null);
    }

    @Override
    public String toServerFilename(String basename, String jsonPath) {
        if (jsonPath.endsWith("/servers")) {
            return "servers";
        }
        return "server_" + basename;
    }

    @Override
    public String toSecurityFilename(String basename, String jsonPath) {
        if (jsonPath.endsWith("/security")) {
            return "security";
        }
        return "security_requirement_object_" + basename;
    }

    @Override
    public String getPascalCaseParameter(String name, String jsonPath) {
        try {
            Integer.parseInt(name);
            // for parameters in path, or an endpoint
            return "Parameter" + name;
        } catch (NumberFormatException nfe) {
            // for header parameters in responses
            return toModelName(name, null);
        }
    }

    public String getPascalCaseResponse(String name, String jsonPath) {
        if (name.matches("^\\d[X\\d]{2}$")) {
            // 200 or 2XX
            return "ResponseFor" + name;
        }
        return toModelName(name, null);
    }

    @Override
    public String toParamName(String basename) {
        return toParameterFilename(basename, null);
    }

    private String toSchemaRefClass(String ref, String sourceJsonPath) {
        String[] refPieces = ref.split("/");
        if (ref.equals(sourceJsonPath)) {
            // self reference, no import needed
            if (ref.startsWith("#/components/schemas/") && refPieces.length == 4) {
                return toModelName(refPieces[3], ref);
            }
            Set<String> httpMethods = new HashSet<>(Arrays.asList("post", "put", "patch", "get", "delete", "trace", "options"));
            boolean requestBodyCase = (
                    refPieces.length == 8 &&
                            refPieces[1].equals("paths") &&
                            httpMethods.contains(refPieces[3]) &&
                            refPieces[4].equals("requestBody") &&
                            refPieces[5].equals("content") &&
                            refPieces[7].equals("schema")
            );
            if (requestBodyCase) {
                String contentType = ModelUtils.decodeSlashes(refPieces[6]);
                // the code knows that content-type are never valid python names
                return toVarName(contentType);
            }
            return null;
        }
        if (sourceJsonPath != null && ref.startsWith(sourceJsonPath + "/")) {
            // internal in-schema reference, no import needed
            // TODO handle this in the future
            if (getFilepath(sourceJsonPath).equals(getFilepath(ref))) {
                // TODO ensure that getFilepath returns the same file for somePath/get/QueryParameters
                // TODO ensure that getFilepath returns the same file for schemas/SomeSchema...
                return null;
            }
        }
        // reference is external, import needed
        // module info is stored in refModule
        if (ref.startsWith("#/components/schemas/") && refPieces.length == 4) {
            String schemaName = refPieces[3];
            return toModelName(schemaName, ref);
        }
        if (ref.startsWith("#/components/parameters/")) {
            if (refPieces.length == 5) {
                // #/components/parameters/PathUserName/schema
                String schemaName = refPieces[4];
                return toModelName(schemaName, ref);
            }
            if (refPieces.length == 7) {
                // #/components/parameters/PathUserName/content/mediaType/schema
                String schemaName = refPieces[6];
                return toModelName(schemaName, ref);
            }
        }
        if (ref.startsWith("#/components/headers/")) {
            if (refPieces.length == 5) {
                // #/components/headers/Int32JsonContentTypeHeader/schema
                String schemaName = refPieces[4];
                return toModelName(schemaName, ref);
            }
            if (refPieces.length == 7) {
                // #/components/headers/Int32JsonContentTypeHeader/content/application~1json/schema
                String schemaName = refPieces[6];
                return toModelName(schemaName, ref);
            }
        }
        if (ref.startsWith("#/components/responses/")) {
            if (refPieces.length == 7) {
                // #/components/responses/SuccessInlineContentAndHeader/headers/someHeader/schema
                String schemaName = refPieces[6];
                return toModelName(schemaName, ref);
            }
            if (refPieces.length == 9) {
                // #/components/responses/SuccessInlineContentAndHeader/headers/someHeader/content/application~1json/schema
                String schemaName = refPieces[8];
                return toModelName(schemaName, ref);
            }
        }
        if (ref.startsWith("#/paths/")) {
            if (refPieces.length == 6) {
                // #/paths/~1commonParam~1{subDir}~1/parameters/0/schema
                String schemaName = refPieces[5];
                return toModelName(schemaName, ref);
            } else if (refPieces.length == 7) {
                // #/paths/~1pet~1{petId}/get/parameters/0/schema
                String schemaName = refPieces[6];
                return toModelName(schemaName, ref);
            } else if (refPieces.length == 8) {
                // #/paths/~1user~1login/get/responses/200/headers/X-Rate-Limit/schema
                String schemaName = refPieces[7];
                return toModelName(schemaName, ref);
            } else if (refPieces.length == 9) {
                // #/paths/~1pet~1{petId}/get/parameters/0/content/mediaType/schema
                // #/paths/~1user~1login/get/responses/200/headers/X-Rate-Limit/schema
                String schemaName = refPieces[8];
                return toModelName(schemaName, ref);
            } else if (refPieces.length == 10) {
                // #/paths/~1user~1login/get/responses/200/headers/X-Rate-Limit/content/application~1json/schema
                String schemaName = refPieces[9];
                return toModelName(schemaName, ref);
            } else if (refPieces.length == 11) {
                // #/paths/~1user~1login/get/responses/200/headers/X-Rate-Limit/content/application~1json/schema
                String schemaName = refPieces[10];
                return toModelName(schemaName, ref);
            }

        }
        return null;
    }

    private String toRequestBodyRefClass(String ref) {
        String[] refPieces = ref.split("/");
        if (ref.startsWith("#/components/requestBodies/") && refPieces.length == 4) {
            return toModelName(refPieces[3], ref);
        }
        return null;
    }

    private String toResponseRefClass(String ref) {
        String[] refPieces = ref.split("/");
        if (ref.startsWith("#/components/responses/") && refPieces.length == 4) {
            return toModelName(refPieces[3], ref);
        }
        return null;
    }

    private String toHeaderRefClass(String ref) {
        String[] refPieces = ref.split("/");
        if (ref.startsWith("#/components/headers/") && refPieces.length == 4) {
            return toModelName(refPieces[3], ref);
        }
        return null;
    }

    private String toParameterRefClass(String ref) {
        String[] refPieces = ref.split("/");
        if (ref.startsWith("#/components/parameters/") && refPieces.length == 4) {
            return toModelName(refPieces[3], ref);
        }
        return null;
    }

    private String toSecuritySchemesRefClass(String ref) {
        String[] refPieces = ref.split("/");
        if (ref.startsWith("#/components/securitySchemes/") && refPieces.length == 4) {
            return toModelName(refPieces[3], ref);
        }
        return null;
    }

    @Override
    public String toRefClass(String ref, String sourceJsonPath, String expectedComponentType) {
        if (ref == null) {
            return null;
        }
        switch (expectedComponentType) {
            case "schemas":
                return toSchemaRefClass(ref, sourceJsonPath);
            case "requestBodies":
                return toRequestBodyRefClass(ref);
            case "responses":
                return toResponseRefClass(ref);
            case "headers":
                return toHeaderRefClass(ref);
            case "parameters":
                return toParameterRefClass(ref);
            case "securitySchemes":
                return toSecuritySchemesRefClass(ref);
        }
        return null;
    }

    @Override
    public String getOperationIdSnakeCase(String operationId) {
        // throw exception if method name is empty (should not occur as an auto-generated method name will be used)
        if (StringUtils.isEmpty(operationId)) {
            throw new RuntimeException("Empty method name (operationId) not allowed");
        }

        // method name cannot use reserved keyword, e.g. return
        if (isReservedWord(operationId)) {
            LOGGER.warn("{} (reserved word) cannot be used as method name. Renamed to {}", operationId, underscore(sanitizeName("call_" + operationId)));
            operationId = "call_" + operationId;
        }

        // operationId starts with a number
        if (operationId.matches("^\\d.*")) {
            LOGGER.warn("{} (starting with a number) cannot be used as method name. Renamed to {}", operationId, underscore(sanitizeName("call_" + operationId)));
            operationId = "call_" + operationId;
        }

        return underscore(sanitizeName(operationId));
    }

    @Override
    public void postProcess() {
        LOGGER.info("################################################################################");
        LOGGER.info("# Thanks for using OpenAPI JSON Schema Generator.                              #");
        LOGGER.info("# Please consider donation to help us maintain this project \uD83D\uDE4F                 #");
        LOGGER.info("# https://github.com/sponsors/spacether                                        #");
        LOGGER.info("#                                                                              #");
        LOGGER.info("# This generator was written by Justin Black (https://github.com/spacether)    #");
        LOGGER.info("# Please support his work directly via https://github.com/sponsors/spacether \uD83D\uDE4F#");
        LOGGER.info("################################################################################");
    }

    @Override
    public String getSchemaPascalCaseName(String name, @NotNull String sourceJsonPath) {
        String usedKey = escapeUnsafeCharacters(name);
        HashMap<String, Integer> keyToQty = sourceJsonPathToKeyToQty.getOrDefault(sourceJsonPath, new HashMap<>());
        if (!sourceJsonPathToKeyToQty.containsKey(sourceJsonPath)) {
            sourceJsonPathToKeyToQty.put(sourceJsonPath, keyToQty);
        }
        Integer qty = keyToQty.getOrDefault(usedKey.toLowerCase(Locale.ROOT), 0);
        qty += 1;
        keyToQty.put(usedKey.toLowerCase(Locale.ROOT), qty);
        String suffix = "";
        if (qty > 1) {
            suffix = qty.toString();
        }
        return toModelName(usedKey + suffix, sourceJsonPath);
    }

    @Override
    public String getSchemaFilename(String jsonPath) {
        String[] pieces = jsonPath.split("/");
        String name = pieces[pieces.length - 1];
        if (name.equals("Headers") && jsonPath.contains("/responses/")) {
            // synthetic response headers jsonPath
            return "header_parameters";
        }
        return toModelFilename(name, jsonPath);
    }

    @Override
    public String escapeReservedWord(String name) {
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
    public String escapeQuotationMark(String input) {
        // remove ' to avoid code injection
        return input.replace("'", "");
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
    public String toApiVarName(String name) {
        return underscore(toApiName(name));
    }

    protected static String dropDots(String str) {
        return str.replaceAll("\\.", "_");
    }

    @Override
    public GeneratorLanguage generatorLanguage() { return GeneratorLanguage.PYTHON; }

    @Override
    public void setOpenAPI(OpenAPI openAPI) {
        super.setOpenAPI(openAPI);
        Components components = openAPI.getComponents();
        // Generate the 'signing.py' module, but only if the 'HTTP signature' security scheme is specified in the OAS.
        Map<String, SecurityScheme> securitySchemeMap = components != null ? components.getSecuritySchemes() : null;
        if (securitySchemeMap != null) {
            for (SecurityScheme securityScheme: securitySchemeMap.values()) {
                if (securityScheme.getType() == SecurityScheme.Type.HTTP && securityScheme.getScheme().equals("signature")) {
                    supportingFiles.add(new SupportingFile("signing.hbs", packagePath(), "signing.py"));
                    break;
                }
            }
        }
    }
}
