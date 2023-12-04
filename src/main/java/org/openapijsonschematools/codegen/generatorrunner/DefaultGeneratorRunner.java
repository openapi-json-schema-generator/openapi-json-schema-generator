/*
 * Copyright 2018 OpenAPI-Generator Contributors (https://openapi-generator.tech)
 * Copyright 2018 SmartBear Software
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

package org.openapijsonschematools.codegen.generatorrunner;

import io.swagger.v3.core.util.Json;
import io.swagger.v3.oas.models.Components;
import io.swagger.v3.oas.models.OpenAPI;
import io.swagger.v3.oas.models.headers.Header;
import io.swagger.v3.oas.models.info.Contact;
import io.swagger.v3.oas.models.info.Info;
import io.swagger.v3.oas.models.info.License;
import io.swagger.v3.oas.models.media.Schema;
import io.swagger.v3.oas.models.parameters.Parameter;
import io.swagger.v3.oas.models.parameters.RequestBody;
import io.swagger.v3.oas.models.responses.ApiResponse;
import io.swagger.v3.oas.models.security.*;
import io.swagger.v3.oas.models.tags.Tag;
import org.apache.commons.io.FilenameUtils;
import org.apache.commons.io.comparator.PathFileComparator;
import org.apache.commons.lang3.StringUtils;
import org.openapijsonschematools.codegen.config.ClientOptInput;
import org.openapijsonschematools.codegen.common.CodegenConstants;
import org.openapijsonschematools.codegen.common.DryRunStatus;
import org.openapijsonschematools.codegen.generatorrunner.ignore.CodegenIgnoreProcessor;
import org.openapijsonschematools.codegen.generators.Generator;
import org.openapijsonschematools.codegen.config.GlobalSettings;
import org.openapijsonschematools.codegen.generators.openapimodels.CodegenHeader;
import org.openapijsonschematools.codegen.generators.openapimodels.CodegenKey;
import org.openapijsonschematools.codegen.generators.openapimodels.CodegenMediaType;
import org.openapijsonschematools.codegen.generators.openapimodels.CodegenOperation;
import org.openapijsonschematools.codegen.generators.openapimodels.CodegenParameter;
import org.openapijsonschematools.codegen.generators.openapimodels.CodegenPathItem;
import org.openapijsonschematools.codegen.generators.openapimodels.CodegenRequestBody;
import org.openapijsonschematools.codegen.generators.openapimodels.CodegenResponse;
import org.openapijsonschematools.codegen.generators.openapimodels.CodegenSchema;
import org.openapijsonschematools.codegen.generators.openapimodels.CodegenSecurityRequirementValue;
import org.openapijsonschematools.codegen.generators.openapimodels.CodegenSecurityScheme;
import org.openapijsonschematools.codegen.generators.openapimodels.CodegenServer;
import org.openapijsonschematools.codegen.generators.openapimodels.CodegenTag;
import org.openapijsonschematools.codegen.generators.openapimodels.CodegenText;
import org.openapijsonschematools.codegen.templating.DryRunTemplateManager;
import org.openapijsonschematools.codegen.templating.SupportingFile;
import org.openapijsonschematools.codegen.common.SerializerUtils;
import org.openapijsonschematools.codegen.templating.CommonTemplateContentLocator;
import org.openapijsonschematools.codegen.templating.GeneratorTemplateContentLocator;
import org.openapijsonschematools.codegen.templating.MustacheEngineAdapter;
import org.openapijsonschematools.codegen.templating.TemplateManager;
import org.openapijsonschematools.codegen.templating.TemplateManagerOptions;
import org.openapijsonschematools.codegen.common.ImplementationVersion;
import org.openapijsonschematools.codegen.common.ModelUtils;
import org.openapijsonschematools.codegen.common.OnceLogger;
import org.openapijsonschematools.codegen.common.URLPathUtils;
import org.openapijsonschematools.codegen.templating.TemplateDefinition;
import org.openapijsonschematools.codegen.templating.TemplatePathLocator;
import org.openapijsonschematools.codegen.templating.TemplateProcessor;
import org.openapijsonschematools.codegen.templating.TemplatingEngineAdapter;
import org.openapijsonschematools.codegen.templating.TemplateFileType;
import org.openapijsonschematools.codegen.generators.generatormetadata.GeneratorMetadata;
import org.openapijsonschematools.codegen.generators.generatormetadata.Stability;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.io.*;
import java.net.URL;
import java.nio.charset.StandardCharsets;
import java.nio.file.Path;
import java.time.ZonedDateTime;
import java.util.*;
import java.util.function.Function;
import java.util.stream.Collectors;

import static org.apache.commons.lang3.StringUtils.removeStart;

@SuppressWarnings("rawtypes")
public class DefaultGeneratorRunner implements GeneratorRunner {
    private static final String METADATA_DIR = ".openapi-generator";
    protected final Logger LOGGER = LoggerFactory.getLogger(DefaultGeneratorRunner.class);
    private final boolean dryRun;
    public Generator generator;
    protected ClientOptInput opts;
    public OpenAPI openAPI;
    protected CodegenIgnoreProcessor ignoreProcessor;
    private Boolean generateApis = null;
    private Boolean generateModels = null;
    private Boolean generateSupportingFiles = null;
    private Boolean generateApiTests = null;
    private Boolean generateApiDocumentation = null;
    private Boolean generateModelTests = null;
    private Boolean generateModelDocumentation = null;
    private Boolean generateMetadata = true;
    private String contextPath;
    private Map<String, String> generatorPropertyDefaults = new HashMap<>();
    protected TemplateProcessor templateProcessor = null;

    private List<TemplateDefinition> userDefinedTemplates = new ArrayList<>();


    public DefaultGeneratorRunner() {
        this(false);
    }

    public DefaultGeneratorRunner(Boolean dryRun) {
        this.dryRun = Boolean.TRUE.equals(dryRun);
        LOGGER.info("Generating with dryRun={}", this.dryRun);
    }

    private void setTemplateProcessor() {
        // must be called after processOptions
        TemplateManagerOptions templateManagerOptions = new TemplateManagerOptions(this.generator.isEnableMinimalUpdate(), this.generator.isSkipOverwrite());

        if (this.dryRun) {
            this.templateProcessor = new DryRunTemplateManager(templateManagerOptions);
        } else {
            TemplatingEngineAdapter templatingEngine = this.generator.getTemplatingEngine();

            if (templatingEngine instanceof MustacheEngineAdapter) {
                MustacheEngineAdapter mustacheEngineAdapter = (MustacheEngineAdapter) templatingEngine;
                mustacheEngineAdapter.setCompiler(this.generator.processCompiler(mustacheEngineAdapter.getCompiler()));
            }

            TemplatePathLocator commonTemplateLocator = new CommonTemplateContentLocator();
            TemplatePathLocator generatorTemplateLocator = new GeneratorTemplateContentLocator(this.generator);
            this.templateProcessor = new TemplateManager(
                    templateManagerOptions,
                    templatingEngine,
                    new TemplatePathLocator[]{generatorTemplateLocator, commonTemplateLocator}
            );
        }
    }

    @SuppressWarnings("deprecation")
    @Override
    public GeneratorRunner opts(ClientOptInput opts) {
        this.opts = opts;
        this.openAPI = opts.getOpenAPI();
        this.generator = opts.getConfig();
        List<TemplateDefinition> userFiles = opts.getUserDefinedTemplates();
        if (userFiles != null) {
            this.userDefinedTemplates = Collections.unmodifiableList(userFiles);
        }

        String ignoreFileLocation = generator.getIgnoreFilePathOverride();
        if (ignoreFileLocation != null) {
            final File ignoreFile = new File(ignoreFileLocation);
            if (ignoreFile.exists() && ignoreFile.canRead()) {
                this.ignoreProcessor = new CodegenIgnoreProcessor(ignoreFile);
            } else {
                LOGGER.warn("Ignore file specified at {} is not valid. This will fall back to an existing ignore file if present in the output directory.", ignoreFileLocation);
            }
        }

        if (this.ignoreProcessor == null) {
            this.ignoreProcessor = new CodegenIgnoreProcessor(generator.getOutputDir());
        }
        return this;
    }

    /**
     * Retrieves an instance to the configured template processor, available after user-defined options are
     * applied via {@link DefaultGeneratorRunner#opts(ClientOptInput)}.
     *
     * @return A configured {@link TemplateProcessor}, or null.
     */
    public TemplateProcessor getTemplateProcessor() {
        return templateProcessor;
    }

    /**
     * Programmatically disable the output of .openapi-generator/VERSION, .openapi-generator-ignore,
     * or other metadata files used by OpenAPI JSON Schema Generator.
     *
     * @param generateMetadata true: enable outputs, false: disable outputs
     */
    @SuppressWarnings("WeakerAccess")
    public void setGenerateMetadata(Boolean generateMetadata) {
        this.generateMetadata = generateMetadata;
    }

    /**
     * Set generator properties otherwise pulled from system properties.
     * Useful for running tests in parallel without relying on System.properties.
     *
     * @param key   The system property key
     * @param value The system property value
     */
    @SuppressWarnings("WeakerAccess")
    public void setGeneratorPropertyDefault(final String key, final String value) {
        this.generatorPropertyDefaults.put(key, value);
    }

    private Boolean getGeneratorPropertyDefaultSwitch(final String key, final Boolean defaultValue) {
        String result = null;
        if (this.generatorPropertyDefaults.containsKey(key)) {
            result = this.generatorPropertyDefaults.get(key);
        }
        if (result != null) {
            return Boolean.valueOf(result);
        }
        return defaultValue;
    }

    public void configureGeneratorProperties() {
        // allows generating only models by specifying a CSV of models to generate, or empty for all
        // NOTE: Boolean.TRUE is required below rather than `true` because of JVM boxing constraints and type inference.
        generateApis = GlobalSettings.getProperty(CodegenConstants.APIS) != null ? Boolean.TRUE : getGeneratorPropertyDefaultSwitch(CodegenConstants.APIS, null);
        generateModels = GlobalSettings.getProperty(CodegenConstants.MODELS) != null ? Boolean.TRUE : getGeneratorPropertyDefaultSwitch(CodegenConstants.MODELS, null);
        generateSupportingFiles = GlobalSettings.getProperty(CodegenConstants.SUPPORTING_FILES) != null ? Boolean.TRUE : getGeneratorPropertyDefaultSwitch(CodegenConstants.SUPPORTING_FILES, null);

        if (generateApis == null && generateModels == null && generateSupportingFiles == null) {
            // no specifics are set, generate everything
            generateApis = generateModels = generateSupportingFiles = true;
        } else {
            if (generateApis == null) {
                generateApis = false;
            }
            if (generateModels == null) {
                generateModels = false;
            }
            if (generateSupportingFiles == null) {
                generateSupportingFiles = false;
            }
        }
        // model/api tests and documentation options rely on parent generate options (api or model) and no other options.
        // They default to true in all scenarios and can only be marked false explicitly
        generateModelTests = GlobalSettings.getProperty(CodegenConstants.MODEL_TESTS) != null ? Boolean.valueOf(GlobalSettings.getProperty(CodegenConstants.MODEL_TESTS)) : getGeneratorPropertyDefaultSwitch(CodegenConstants.MODEL_TESTS, true);
        generateModelDocumentation = GlobalSettings.getProperty(CodegenConstants.MODEL_DOCS) != null ? Boolean.valueOf(GlobalSettings.getProperty(CodegenConstants.MODEL_DOCS)) : getGeneratorPropertyDefaultSwitch(CodegenConstants.MODEL_DOCS, true);
        generateApiTests = GlobalSettings.getProperty(CodegenConstants.API_TESTS) != null ? Boolean.valueOf(GlobalSettings.getProperty(CodegenConstants.API_TESTS)) : getGeneratorPropertyDefaultSwitch(CodegenConstants.API_TESTS, true);
        generateApiDocumentation = GlobalSettings.getProperty(CodegenConstants.API_DOCS) != null ? Boolean.valueOf(GlobalSettings.getProperty(CodegenConstants.API_DOCS)) : getGeneratorPropertyDefaultSwitch(CodegenConstants.API_DOCS, true);

        // Additional properties added for tests to exclude references in project related files
        generator.additionalProperties().put(CodegenConstants.GENERATE_API_TESTS, generateApiTests);
        generator.additionalProperties().put(CodegenConstants.GENERATE_MODEL_TESTS, generateModelTests);

        generator.additionalProperties().put(CodegenConstants.GENERATE_API_DOCS, generateApiDocumentation);
        generator.additionalProperties().put(CodegenConstants.GENERATE_MODEL_DOCS, generateModelDocumentation);

        generator.additionalProperties().put(CodegenConstants.GENERATE_APIS, generateApis);
        generator.additionalProperties().put(CodegenConstants.GENERATE_MODELS, generateModels);

        if (!generateApiTests && !generateModelTests) {
            generator.additionalProperties().put(CodegenConstants.EXCLUDE_TESTS, true);
        }

        if (GlobalSettings.getProperty("debugOpenAPI") != null) {
            System.out.println(SerializerUtils.toJsonString(openAPI));
        } else if (GlobalSettings.getProperty("debugSwagger") != null) {
            // This exists for backward compatibility
            // We fall to this block only if debugOpenAPI is null. No need to dump this twice.
            LOGGER.info("Please use system property 'debugOpenAPI' instead of 'debugSwagger'.");
            System.out.println(SerializerUtils.toJsonString(openAPI));
        }

        generator.processOpts();
        setTemplateProcessor();
        generator.preprocessOpenAPI(openAPI);

        // set OpenAPI to make these available to all methods
        generator.setOpenAPI(openAPI);

        generator.additionalProperties().put("generatorVersion", ImplementationVersion.read());
        generator.additionalProperties().put("generatedDate", ZonedDateTime.now().toString());
        generator.additionalProperties().put("generatedYear", String.valueOf(ZonedDateTime.now().getYear()));
        generator.additionalProperties().put("generatorClass", generator.getClass().getSimpleName());
        generator.additionalProperties().put("inputSpec", generator.getInputSpec());

        if (openAPI.getExtensions() != null) {
            generator.vendorExtensions().putAll(openAPI.getExtensions());
        }

        // TODO: Allow user to define _which_ servers object in the array to target.
        // Configures contextPath/basePath according to api document's servers
        URL url = URLPathUtils.getServerURL(openAPI, generator.serverVariableOverrides());
        contextPath = removeTrailingSlash(generator.escapeText(url.getPath())); // for backward compatibility
    }

    private void configureOpenAPIInfo() {
        Info info = this.openAPI.getInfo();
        if (info == null) {
            return;
        }
        if (info.getTitle() != null) {
            generator.additionalProperties().put("appName", generator.escapeText(info.getTitle()));
        }
        if (info.getVersion() != null) {
            generator.additionalProperties().put("appVersion", generator.escapeText(info.getVersion()));
        } else {
            LOGGER.error("Missing required field info version. Default appVersion set to 1.0.0");
            generator.additionalProperties().put("appVersion", "1.0.0");
        }

        if (StringUtils.isEmpty(info.getDescription())) {
            // set a default description if none if provided
            String msg = "No description provided (generated by Openapi JSON Schema Generator https://github.com/openapi-json-schema-tools/openapi-json-schema-generator)";
            CodegenText txt = new CodegenText(msg, generator.escapeText(msg));
            generator.additionalProperties().put("appDescription", txt);
        } else {
            String msg = info.getDescription();
            CodegenText txt = new CodegenText(msg, generator.escapeText(msg));
            generator.additionalProperties().put("appDescription", txt);
        }

        if (info.getContact() != null) {
            Contact contact = info.getContact();
            if (contact.getEmail() != null) {
                generator.additionalProperties().put("infoEmail", generator.escapeText(contact.getEmail()));
            }
            if (contact.getName() != null) {
                generator.additionalProperties().put("infoName", generator.escapeText(contact.getName()));
            }
            if (contact.getUrl() != null) {
                generator.additionalProperties().put("infoUrl", generator.escapeText(contact.getUrl()));
            }
        }

        if (info.getLicense() != null) {
            License license = info.getLicense();
            if (license.getName() != null) {
                generator.additionalProperties().put("licenseInfo", generator.escapeText(license.getName()));
            }
            if (license.getUrl() != null) {
                generator.additionalProperties().put("licenseUrl", generator.escapeText(license.getUrl()));
            }
        }

        if (info.getVersion() != null) {
            generator.additionalProperties().put("version", generator.escapeText(info.getVersion()));
        } else {
            LOGGER.error("Missing required field info version. Default version set to 1.0.0");
            generator.additionalProperties().put("version", "1.0.0");
        }

        if (info.getTermsOfService() != null) {
            generator.additionalProperties().put("termsOfService", generator.escapeText(info.getTermsOfService()));
        }
    }

    private void generateSchemaDocumentation(List<File> files, CodegenSchema schema, String jsonPath, String docRoot) {
        Map<String, Object> schemaData = new HashMap<>();
        schemaData.put("packageName", generator.packageName());
        schemaData.put("schema", schema);
        schemaData.putAll(generator.additionalProperties());
        schemaData.put("docRoot", docRoot);
        schemaData.put("identifierPieces", Collections.unmodifiableList(new ArrayList<>()));
        schemaData.put("headerSize", "#");
        generateXDocs(files, jsonPath, CodegenConstants.JSON_PATH_LOCATION_TYPE.SCHEMA, CodegenConstants.MODEL_DOCS, schemaData, generateModelDocumentation);
    }

    private void generateSchema(List<File> files, CodegenSchema schema, String jsonPath) {
        Map<String, Object> schemaData = new HashMap<>();
        schemaData.put("packageName", generator.packageName());
        schemaData.put("schema", schema);
        schemaData.put("identifierPieces", Collections.unmodifiableList(new ArrayList<>()));
        schemaData.putAll(generator.additionalProperties());
        generateXs(files, jsonPath, CodegenConstants.JSON_PATH_LOCATION_TYPE.SCHEMA, CodegenConstants.MODELS, schemaData, generateModels);
    }

    @Override
    public String requestBodyFileFolder() {
        return "";
    }

    private String packageFilename(List<String> pathSegments) {
        String prefix = generator.getOutputDir() + File.separatorChar + generator.packagePath() + File.separatorChar;
        String suffix = pathSegments.stream().collect(Collectors.joining(File.separator));
        return prefix + suffix;
    }

    private String filenameFromRoot(List<String> pathSegments) {
        String prefix = generator.getOutputDir() + File.separatorChar;
        String suffix = pathSegments.stream().collect(Collectors.joining(File.separator));
        return prefix + suffix;
    }

    private void generateFile(Map<String, Object> templateData, String templateName, String outputFilename, List<File> files, boolean shouldGenerate, String skippedByOption) {
        try {
            File written = processTemplateToFile(templateData, templateName, outputFilename, shouldGenerate, skippedByOption);
            if (written != null) {
                files.add(written);
                if (generator.isEnablePostProcessFile() && !dryRun) {
                    generator.postProcessFile(written, skippedByOption);
                }
            }
        } catch (IOException e) {
            LOGGER.error("Error when writing template file {}", e.toString());
        }
    }

    private void generateFiles(List<List<Object>> processTemplateToFileInfos, boolean shouldGenerate, String skippedByOption, List<File> files) {
        for (List<Object> processTemplateToFileInfo: processTemplateToFileInfos) {
            Map<String, Object> templateData = (Map<String, Object>) processTemplateToFileInfo.get(0);
            String templateName = (String) processTemplateToFileInfo.get(1);
            String outputFilename = (String) processTemplateToFileInfo.get(2);
            try {
                File written = processTemplateToFile(templateData, templateName, outputFilename, shouldGenerate, skippedByOption);
                if (written != null) {
                    files.add(written);
                    if (generator.isEnablePostProcessFile() && !dryRun) {
                        generator.postProcessFile(written, skippedByOption);
                    }
                }
            } catch (IOException e) {
                LOGGER.error("Error when writing template file {}", e.toString());
            }
        }
    }

    private void generatePathItem(List<File> files, CodegenKey pathKey, CodegenPathItem pathItem, String jsonPath, List<CodegenServer> servers, List<HashMap<String, CodegenSecurityRequirementValue>> security) {
        Map<String, Object> pathTemplateInfo = new HashMap<>();
        pathTemplateInfo.put("pathModule", pathKey.snakeCase);
        pathTemplateInfo.put("apiClassName", pathKey.camelCase);
        pathTemplateInfo.put("path", pathKey.original);
        generateXs(files, jsonPath, CodegenConstants.JSON_PATH_LOCATION_TYPE.PATH, CodegenConstants.APIS, pathTemplateInfo, true);

        if (pathItem.servers != null) {
            generateServers(files, pathItem.servers, jsonPath + "/servers");
        }

        if (pathItem.parameters != null) {
            generateXs(files, jsonPath + "/parameters", CodegenConstants.JSON_PATH_LOCATION_TYPE.PARAMETERS, CodegenConstants.PARAMETERS, null, true);
            int i = 0;
            for (CodegenParameter param: pathItem.parameters) {
                generateParameter(files, param, jsonPath + "/parameters/" + i);
                i += 1;
            }
        }

        if (pathItem.operations != null) {
            // tests/test_paths/test_some_path/__init__.py
            generateXTests(files, jsonPath, CodegenConstants.JSON_PATH_LOCATION_TYPE.PATH, CodegenConstants.API_TESTS, new HashMap<>(), true);

            for (Map.Entry<CodegenKey, CodegenOperation> entry: pathItem.operations.entrySet()) {
                CodegenKey httpMethod = entry.getKey();
                CodegenOperation operation = entry.getValue();
                String operationJsonPath = jsonPath + "/" + httpMethod.original;

                Map<String, Object> endpointMap = new HashMap<>();
                endpointMap.put("operation", operation);
                endpointMap.put("pathItem", pathItem);
                endpointMap.put("httpMethod", httpMethod);
                endpointMap.put("security", security);
                endpointMap.put("path", pathKey);
                generateXs(files, operationJsonPath, CodegenConstants.JSON_PATH_LOCATION_TYPE.OPERATION, CodegenConstants.APIS, endpointMap, true);
                if (operation.pathParametersSchema != null) {
                    String objectJsonPath = operationJsonPath + "/" + "PathParameters";
                    generateSchema(files, operation.pathParametersSchema, objectJsonPath);
                }
                if (operation.queryParametersSchema != null) {
                    String objectJsonPath = operationJsonPath + "/" + "QueryParameters";
                    generateSchema(files, operation.queryParametersSchema, objectJsonPath);
                }
                if (operation.headerParametersSchema != null) {
                    String objectJsonPath = operationJsonPath + "/" + "HeaderParameters";
                    generateSchema(files, operation.headerParametersSchema, objectJsonPath);
                }
                if (operation.cookieParametersSchema != null) {
                    String objectJsonPath = operationJsonPath + "/" + "CookieParameters";
                    generateSchema(files, operation.cookieParametersSchema, objectJsonPath);
                }

                // operation docs
                Map<String, Object> endpointInfo = new HashMap<>();
                endpointInfo.put("operation", operation);
                endpointInfo.put("httpMethod", httpMethod);
                endpointInfo.put("path", pathKey);
                endpointInfo.put("pathItem", pathItem);
                endpointInfo.put("servers", servers);
                endpointInfo.put("security", security);
                endpointInfo.put("packageName", generator.packageName());
                endpointInfo.put("apiPackage", generator.apiPackage());
                endpointInfo.put("headerSize", "#");
                endpointInfo.put("identifierPieces", Collections.unmodifiableList(new ArrayList<>()));
                endpointInfo.put("docRoot", "../../");
                generateXDocs(files, operationJsonPath, CodegenConstants.JSON_PATH_LOCATION_TYPE.OPERATION, CodegenConstants.APIS, endpointInfo, true);

                // paths.some_path.security.security_requirement_0.py
                if (operation.security != null) {
                    String securityJsonPath = operationJsonPath + "/security";
                    generateSecurity(files, operation.security, securityJsonPath);
                }

                // paths.some_path.post.request_body.py, only written if there is no refModule
                if (operation.requestBody != null) {
                    String requestBodyJsonPath = operationJsonPath + "/requestBody";
                    generateRequestBody(files, operation.requestBody, requestBodyJsonPath, "../../../../");
                }

                if (operation.servers != null) {
                    generateServers(files, operation.servers, operationJsonPath + "/servers");
                }

                // paths.some_path.post.parameters.parameter_0.py
                if (operation.parameters != null && !operation.parameters.allParameters.isEmpty()) {
                    String parametersJsonPath = operationJsonPath + "/parameters";
                    generateXs(files, parametersJsonPath, CodegenConstants.JSON_PATH_LOCATION_TYPE.PARAMETERS, CodegenConstants.PARAMETERS, null, true);
                    Integer i = 0;
                    for (CodegenParameter cp: operation.parameters.allParameters) {
                        String parameterJsonPath = parametersJsonPath + "/" + i.toString();
                        generateParameter(files, cp, parameterJsonPath);
                        i++;
                    }
                }

                if (operation.responses != null && !operation.responses.isEmpty()) {
                    String responsesJsonPath = operationJsonPath + "/responses";
                    generateXs(files, responsesJsonPath, CodegenConstants.JSON_PATH_LOCATION_TYPE.RESPONSES, CodegenConstants.RESPONSES, null, true);
                    for (Map.Entry<String, CodegenResponse> responseEntry: operation.responses.entrySet()) {
                        // paths.some_path.post.responses.response_200.__init__.py (file per response)
                        // response is a package because responses have Headers which can be refed
                        // so each inline header should be a module in the response package
                        String code = responseEntry.getKey();
                        CodegenResponse response = responseEntry.getValue();
                        String responseJsonPath = responsesJsonPath + "/" + code;
                        generateResponse(files, response, responseJsonPath, "../../../../../");
                    }
                }

                Map<String, Object> endpointTestMap = new HashMap<>();
                endpointTestMap.put("operation", operation);
                endpointTestMap.put("httpMethod", httpMethod);
                endpointTestMap.put("path", pathKey);
                // tests/test_paths/test_some_path/test_post.py
                generateXTests(files, operationJsonPath, CodegenConstants.JSON_PATH_LOCATION_TYPE.OPERATION, CodegenConstants.API_TESTS, endpointTestMap, true);
            }
        }
    }

    private void generatePaths(List<File> files, TreeMap<CodegenKey, CodegenPathItem> paths, List<CodegenServer> servers, List<HashMap<String, CodegenSecurityRequirementValue>> security) {
        if (paths == null || paths.isEmpty()) {
            LOGGER.info("Skipping generation of paths because the specification document lacks them.");
            return;
        }
        if (!generateApis) {
            LOGGER.info("Skipping generation of paths because generateApis is set to false.");
            return;
        }

        String pathsJsonPath = "#/paths";
        generateXs(files, pathsJsonPath, CodegenConstants.JSON_PATH_LOCATION_TYPE.PATHS, CodegenConstants.APIS, null, true);

        // tests/test_paths/__init__.py
        generateXTests(files, pathsJsonPath, CodegenConstants.JSON_PATH_LOCATION_TYPE.PATHS, CodegenConstants.API_TESTS, new HashMap<>(), true);

        // tests/__init__.py
        generateXTests(files, "#", CodegenConstants.JSON_PATH_LOCATION_TYPE.TEST_ROOT, CodegenConstants.APIS, null, true);

        for (Map.Entry<CodegenKey, CodegenPathItem> entry: paths.entrySet()) {
            CodegenKey pathKey = entry.getKey();
            CodegenPathItem pathItem = entry.getValue();
            String jsonPath = "#/paths/" + ModelUtils.encodeSlashes(pathKey.original);

            generatePathItem(files, pathKey, pathItem, jsonPath, servers, security);
        }
    }

    private void generateContent(List<File> files, LinkedHashMap<CodegenKey, CodegenMediaType> content, String jsonPath, String docRoot) {
        String contentJsonPath = jsonPath + "/content";
        boolean schemaExists = false;

        // content-type + schema generation
        for (Map.Entry<CodegenKey, CodegenMediaType> contentInfo: content.entrySet()) {
            String contentType = contentInfo.getKey().original;
            CodegenMediaType codegenMediaType = contentInfo.getValue();
            CodegenSchema schema = codegenMediaType.schema;
            if (schema != null) {
                schemaExists = true;
                String contentTypeJsonPath = contentJsonPath + "/" + ModelUtils.encodeSlashes(contentType);

                // schema
                String schemaJsonPath = contentTypeJsonPath + "/schema";
                generateSchema(files, schema, schemaJsonPath);
                generateSchemaDocumentation(files, schema, schemaJsonPath, docRoot + "../../");

                Map<String, String> contentTypeTemplateInfo = generator.jsonPathTemplateFiles().get(CodegenConstants.JSON_PATH_LOCATION_TYPE.CONTENT_TYPE);
                if (contentTypeTemplateInfo == null || contentTypeTemplateInfo.isEmpty()) {
                    continue;
                }
                // content-type
                for (Map.Entry<String, String> contentTypeEntry: contentTypeTemplateInfo.entrySet()) {
                    String templateFile = contentTypeEntry.getKey();
                    String outputFile = contentTypeEntry.getValue();
                    String outputFilepath = generator.getFilepath(contentTypeJsonPath) + File.separatorChar + outputFile;
                    HashMap<String, Object> contentTypeTemplateData = new HashMap<>();
                    contentTypeTemplateData.put("schema", schema);
                    try {
                        File written = processTemplateToFile(contentTypeTemplateData, templateFile, outputFilepath, true, CodegenConstants.CONTENT);
                        if (written != null) {
                            files.add(written);
                            if (generator.isEnablePostProcessFile() && !dryRun) {
                                generator.postProcessFile(written, "content");
                            }
                        }
                    } catch (IOException e) {
                        throw new RuntimeException("Could not generate schema for jsonPath '" + jsonPath + "'", e);
                    }
                }
            }
        }

        Map<String, String> contentTemplateInfo = generator.jsonPathTemplateFiles().get(CodegenConstants.JSON_PATH_LOCATION_TYPE.CONTENT);
        if (schemaExists && contentTemplateInfo != null && !contentTemplateInfo.isEmpty()) {
            for (Map.Entry<String, String> contentEntry: contentTemplateInfo.entrySet()) {
                String contentTemplateFile = contentEntry.getKey();
                String outputFile = contentEntry.getValue();
                String outputFilepath = generator.getFilepath(contentJsonPath) + File.separatorChar + outputFile;
                HashMap<String, Object> contentTemplateData = new HashMap<>();
                contentTemplateData.put("content", content);
                try {
                    File written = processTemplateToFile(contentTemplateData, contentTemplateFile, outputFilepath, true, CodegenConstants.CONTENT);
                    if (written != null) {
                        files.add(written);
                        if (generator.isEnablePostProcessFile() && !dryRun) {
                            generator.postProcessFile(written, "content");
                        }
                    }
                } catch (IOException e) {
                    throw new RuntimeException("Could not generate schema for jsonPath '" + jsonPath + "'", e);
                }
            }
        }
    }

    private void generateResponse(List<File> files, CodegenResponse response, String jsonPath, String docRoot) {
        Map<String, Object> templateData = new HashMap<>();
        templateData.put("packageName", generator.packageName());
        templateData.put("response", response);
        generateXs(files, jsonPath, CodegenConstants.JSON_PATH_LOCATION_TYPE.RESPONSE, CodegenConstants.RESPONSES, templateData, true);

        // headers
        if (response.headers != null && !response.headers.isEmpty()) {
            String headersJsonPath = jsonPath + "/headers";
            generateXs(files, headersJsonPath, CodegenConstants.JSON_PATH_LOCATION_TYPE.HEADERS, CodegenConstants.HEADERS, null, true);
            for (Map.Entry<String, CodegenHeader> headerInfo: response.headers.entrySet()) {
                String headerName = headerInfo.getKey();
                CodegenHeader header = headerInfo.getValue();
                String headerJsonPath = headersJsonPath + "/" + headerName;
                generateHeader(files, header, headerJsonPath, docRoot + "../../");
            }
            // synthetic json path
            String headersObjectJsonPath = jsonPath + "/Headers";
            generateSchema(files, response.headersObjectSchema, headersObjectJsonPath);
        }
        LinkedHashMap<CodegenKey, CodegenMediaType> content = response.content;
        if (content != null && !content.isEmpty()) {
            generateContent(files, content, jsonPath, docRoot + "../");
        }
    }

    private TreeMap<String, CodegenResponse> generateResponses(List<File> files) {
        String skipMsg = "Skipping generation of component responses because the specification document lacks them.";
        Components components = this.openAPI.getComponents();
        if (components == null) {
            LOGGER.info(skipMsg);
            return null;
        }
        final Map<String, ApiResponse> specResponses = components.getResponses();
        if (specResponses == null) {
            LOGGER.info(skipMsg);
            return null;
        }
        TreeMap<String, CodegenResponse> responses = new TreeMap<>();
        String responsesJsonPath = "#/components/responses";
        generateXs(files, responsesJsonPath, CodegenConstants.JSON_PATH_LOCATION_TYPE.RESPONSES, CodegenConstants.RESPONSES, null, true);
        for (Map.Entry<String, ApiResponse> responseEntry: specResponses.entrySet()) {
            String componentName = responseEntry.getKey();
            ApiResponse apiResponse = responseEntry.getValue();
            String sourceJsonPath = responsesJsonPath + "/" + componentName;
            CodegenResponse response = generator.fromResponse(apiResponse, sourceJsonPath);
            responses.put(componentName, response);
            generateResponse(files, response, sourceJsonPath, "../../");

            Map<String, Object> templateData = new HashMap<>();
            templateData.put("packageName", generator.packageName());
            templateData.put("docRoot", "../../");
            templateData.put("headerSize", "#");
            templateData.put("identifierPieces", Collections.unmodifiableList(new ArrayList<>()));
            templateData.put("response", response);
            // TODO make this a property that can be turned off and on
            generateXDocs(files, sourceJsonPath, CodegenConstants.JSON_PATH_LOCATION_TYPE.RESPONSE, CodegenConstants.RESPONSE_DOCS, templateData, true);
        }
        return responses;
    }

    private void generateRequestBody(List<File> files, CodegenRequestBody requestBody, String jsonPath, String docRoot) {
        Map<String, Object> templateData = new HashMap<>();
        templateData.put("packageName", generator.packageName());
        templateData.put("requestBody", requestBody);
        generateXs(files, jsonPath, CodegenConstants.JSON_PATH_LOCATION_TYPE.REQUEST_BODY, CodegenConstants.REQUEST_BODIES, templateData, true);

        // schemas
        LinkedHashMap<CodegenKey, CodegenMediaType> content = requestBody.content;
        if (content != null && !content.isEmpty()) {
            generateContent(files, content, jsonPath, docRoot);
        }
    }

    private void generateSecurityScheme(List<File> files, CodegenSecurityScheme securityScheme, String jsonPath) {
        Map<String, Object> templateData = new HashMap<>();
        templateData.put("packageName", generator.packageName());
        templateData.put("securityScheme", securityScheme);
        generateXs(files, jsonPath, CodegenConstants.JSON_PATH_LOCATION_TYPE.SECURITY_SCHEME, CodegenConstants.SECURITY_SCHEMES, templateData, true);
    }

    private TreeMap<String, CodegenSecurityScheme> generateSecuritySchemes(List<File> files) {
        String skipMsg = "Skipping generation of component securitySchemes because the specification document lacks them.";
        Components components = this.openAPI.getComponents();
        if (components == null) {
            LOGGER.info(skipMsg);
            return null;
        }
        final Map<String, SecurityScheme> specSecuritySchemes = components.getSecuritySchemes();
        if (specSecuritySchemes == null) {
            LOGGER.info(skipMsg);
            return null;
        }
        TreeMap<String, CodegenSecurityScheme> securitySchemes = new TreeMap<>();
        String jsonPath = "#/components/securitySchemes";
        generateXs(files, jsonPath, CodegenConstants.JSON_PATH_LOCATION_TYPE.SECURITY_SCHEMES, CodegenConstants.SECURITY_SCHEMES, null, true);
        for (Map.Entry<String, SecurityScheme> entry: specSecuritySchemes.entrySet()) {
            String componentName = entry.getKey();
            SecurityScheme specSecurityScheme = entry.getValue();
            String sourceJsonPath = jsonPath + "/" + componentName;
            CodegenSecurityScheme securityScheme = generator.fromSecurityScheme(specSecurityScheme, sourceJsonPath);
            securitySchemes.put(componentName, securityScheme);

            generateSecurityScheme(files, securityScheme, sourceJsonPath);

            // doc generation
            Map<String, Object> templateData = new HashMap<>();
            templateData.put("packageName", generator.packageName());
            templateData.put("securityScheme", securityScheme);
            templateData.put("headerSize", "#");
            templateData.put("identifierPieces", Collections.unmodifiableList(new ArrayList<>()));
            // TODO add a flag to turn this off
            generateXDocs(files, sourceJsonPath, CodegenConstants.JSON_PATH_LOCATION_TYPE.SECURITY_SCHEME, CodegenConstants.SECURITY_SCHEME_DOCS, templateData, true);
        }
        // sort them
        securitySchemes = new TreeMap<>(securitySchemes);
        return securitySchemes;
    }

    private TreeMap<String, CodegenRequestBody> generateRequestBodies(List<File> files) {
        String skipMsg = "Skipping generation of component requestBodies because the specification document lacks them.";
        Components components = this.openAPI.getComponents();
        if (components == null) {
            LOGGER.info(skipMsg);
            return null;
        }
        final Map<String, RequestBody> specRequestBodies = components.getRequestBodies();
        if (specRequestBodies == null) {
            LOGGER.info(skipMsg);
            return null;
        }
        TreeMap<String, CodegenRequestBody> requestBodies = new TreeMap<>();
        String requestBodiesJsonPath = "#/components/requestBodies";
        generateXs(files, requestBodiesJsonPath, CodegenConstants.JSON_PATH_LOCATION_TYPE.REQUEST_BODIES, CodegenConstants.REQUEST_BODIES, null, true);
        for (Map.Entry<String, RequestBody> entry: specRequestBodies.entrySet()) {
            String componentName = entry.getKey();
            RequestBody specRequestBody = entry.getValue();
            String sourceJsonPath = requestBodiesJsonPath + "/" + componentName;
            CodegenRequestBody requestBody = generator.fromRequestBody(specRequestBody, sourceJsonPath);
            requestBodies.put(componentName, requestBody);

            generateRequestBody(files, requestBody, sourceJsonPath, "../../");

            // doc generation
            Map<String, Object> templateData = new HashMap<>();
            templateData.put("packageName", generator.packageName());
            templateData.put("requestBody", requestBody);
            templateData.put("headerSize", "#");
            templateData.put("identifierPieces", Collections.unmodifiableList(new ArrayList<>()));
            templateData.put("docRoot", "../../");
            // todo add flag to turn this off
            generateXDocs(files, sourceJsonPath, CodegenConstants.JSON_PATH_LOCATION_TYPE.REQUEST_BODY, CodegenConstants.REQUEST_BODY_DOCS, templateData, true);
        }
        // sort them
        requestBodies = new TreeMap<>(requestBodies);
        return requestBodies;
    }

    private void generateParameter(List<File> files, CodegenParameter parameter, String jsonPath) {
        Map<String, Object> templateData = new HashMap<>();
        templateData.put("packageName", generator.packageName());
        templateData.put("parameter", parameter);
        generateXs(files, jsonPath, CodegenConstants.JSON_PATH_LOCATION_TYPE.PARAMETER, CodegenConstants.PARAMETERS, templateData, true);

        // schema
        CodegenSchema schema = parameter.schema;
        if (schema != null) {
            String schemaJsonPath = parameter.getSetSchemaJsonPath(jsonPath);
            generateSchema(files, schema, schemaJsonPath);
            generateSchemaDocumentation(files, schema, schemaJsonPath, "../../../");
        }
        LinkedHashMap<CodegenKey, CodegenMediaType> content = parameter.content;
        if (schema == null && content != null && !content.isEmpty()) {
            generateContent(files, content, jsonPath, "../../../");
        }
    }

    private TreeMap<String, CodegenParameter> generateParameters(List<File> files) {
        String skipMsg = "Skipping generation of component parameters because the specification document lacks them.";
        Components components = this.openAPI.getComponents();
        if (components == null) {
            LOGGER.info(skipMsg);
            return null;
        }
        final Map<String, Parameter> specParameters = components.getParameters();
        if (specParameters == null || specParameters.isEmpty()) {
            LOGGER.info(skipMsg);
            return null;
        }
        TreeMap<String, CodegenParameter> parameters = new TreeMap<>();
        String parametersJsonPath = "#/components/parameters";
        generateXs(files, parametersJsonPath, CodegenConstants.JSON_PATH_LOCATION_TYPE.PARAMETERS, CodegenConstants.PARAMETERS, null, true);
        for (Map.Entry<String, Parameter> entry: specParameters.entrySet()) {
            String componentName = entry.getKey();
            Parameter specParameter = entry.getValue();
            String parameterJsonPath = parametersJsonPath + "/" + componentName;
            CodegenParameter parameter = generator.fromParameter(specParameter, parameterJsonPath);
            parameters.put(componentName, parameter);
            generateParameter(files, parameter, parameterJsonPath);

            Map<String, Object> templateData = new HashMap<>();
            templateData.put("packageName", generator.packageName());
            templateData.put("parameter", parameter);
            templateData.put("headerSize", "#");
            templateData.put("identifierPieces", Collections.unmodifiableList(new ArrayList<>()));
            templateData.put("docRoot", "../../");
            // todo add flag to turn this off
            generateXDocs(files, parameterJsonPath, CodegenConstants.JSON_PATH_LOCATION_TYPE.PARAMETER, CodegenConstants.PARAMETER_DOCS, templateData, true);
        }
        return parameters;
    }

    private void generateHeader(List<File> files, CodegenHeader header, String jsonPath, String docRoot) {
        Map<String, Object> headertTemplateData = new HashMap<>();
        headertTemplateData.put("packageName", generator.packageName());
        headertTemplateData.put("header", header);

        // header
        generateXs(files, jsonPath, CodegenConstants.JSON_PATH_LOCATION_TYPE.HEADER, CodegenConstants.HEADERS, headertTemplateData, true);

        // schema
        CodegenSchema schema = header.schema;
        if (schema != null) {
            String schemaJsonPath = header.getSetSchemaJsonPath(jsonPath);
            generateSchema(files, schema, schemaJsonPath);
            generateSchemaDocumentation(files, schema, schemaJsonPath, docRoot + "../");
        }
        LinkedHashMap<CodegenKey, CodegenMediaType> content = header.content;
        if (schema == null && content != null && !content.isEmpty()) {
            generateContent(files, content, jsonPath, docRoot + "../");
        }
    }

    private void generateXDocs(List<File> files, String jsonPath, CodegenConstants.JSON_PATH_LOCATION_TYPE type, String skippedByOption, Map<String, Object> templateInfo, boolean shouldGenerate) {
        Map<String, String> templateFileToOutputFile = generator.jsonPathDocTemplateFiles().get(type);
        if (templateFileToOutputFile == null || templateFileToOutputFile.isEmpty()) {
            return;
        }
        for (Map.Entry<String, String> entry : templateFileToOutputFile.entrySet()) {
            String templateFile = entry.getKey();
            String suffix = entry.getValue();
            String filename = generator.getDocsFilepath(jsonPath) + suffix;

            HashMap<String, Object> templateData = new HashMap<>();
            templateData.put("packageName", generator.packageName());
            templateData.put("modelPackage", generator.modelPackage());
            if (templateInfo != null && !templateInfo.isEmpty()) {
                templateData.putAll(templateInfo);
            }
            try {
                File written = processTemplateToFile(templateData, templateFile, filename, shouldGenerate, skippedByOption);
                if (written != null) {
                    files.add(written);
                    if (generator.isEnablePostProcessFile() && !dryRun) {
                        generator.postProcessFile(written, skippedByOption);
                    }
                }
            } catch (Exception e) {
                throw new RuntimeException("Could not generate file '" + filename + "'", e);
            }
        }
    }

    private void generateXTests(List<File> files, String jsonPath, CodegenConstants.JSON_PATH_LOCATION_TYPE type, String skippedByOption, Map<String, Object> templateInfo, boolean shouldGenerate) {
        Map<String, String> templateFileToOutputFile = generator.jsonPathTestTemplateFiles().get(type);
        if (templateFileToOutputFile == null || templateFileToOutputFile.isEmpty()) {
            return;
        }
        for (Map.Entry<String, String> entry : templateFileToOutputFile.entrySet()) {
            String templateFile = entry.getKey();
            String suffix = entry.getValue();
            String filename = generator.getTestFilepath(jsonPath) + suffix;

            HashMap<String, Object> templateData = new HashMap<>();
            templateData.put("packageName", generator.packageName());
            templateData.put("modelPackage", generator.modelPackage());
            if (templateInfo != null && !templateInfo.isEmpty()) {
                templateData.putAll(templateInfo);
            }
            try {
                File testFile = new File(filename);
                if (testFile.exists()) {
                    this.templateProcessor.skip(testFile.toPath(), "Test files never overwrite an existing file of the same name.");
                } else {
                    File written = processTemplateToFile(templateData, templateFile, filename, shouldGenerate, skippedByOption);
                    if (written != null) {
                        files.add(written);
                        if (generator.isEnablePostProcessFile() && !dryRun) {
                            generator.postProcessFile(written, skippedByOption);
                        }
                    }
                }
            } catch (Exception e) {
                throw new RuntimeException("Could not generate file '" + filename + "'", e);
            }
        }
    }

    private void generateXs(List<File> files, String jsonPath, CodegenConstants.JSON_PATH_LOCATION_TYPE type, String skippedByOption, Map<String, Object> templateInfo, boolean shouldGenerate) {
        Map<String, String> templateFileToOutputFile = generator.jsonPathTemplateFiles().get(type);
        if (templateFileToOutputFile == null || templateFileToOutputFile.isEmpty()) {
            return;
        }
        for (Map.Entry<String, String> entry : templateFileToOutputFile.entrySet()) {
            String templateFile = entry.getKey();
            String suffix = entry.getValue();
            String filename = generator.getFilepath(jsonPath) + suffix;

            HashMap<String, Object> templateData = new HashMap<>();
            templateData.put("packageName", generator.packageName());
            templateData.put("modelPackage", generator.modelPackage());
            if (templateInfo != null && !templateInfo.isEmpty()) {
                templateData.putAll(templateInfo);
            }
            try {
                File written = processTemplateToFile(templateData, templateFile, filename, shouldGenerate, skippedByOption);
                if (written != null) {
                    files.add(written);
                    if (generator.isEnablePostProcessFile() && !dryRun) {
                        generator.postProcessFile(written, skippedByOption);
                    }
                }
            } catch (Exception e) {
                throw new RuntimeException("Could not generate file '" + filename + "'", e);
            }
        }
    }

    private TreeMap<String, CodegenHeader> generateHeaders(List<File> files) {
        String skipMsg = "Skipping generation of component headers because the specification document lacks them.";
        Components components = this.openAPI.getComponents();
        if (components == null) {
            LOGGER.info(skipMsg);
            return null;
        }
        final Map<String, Header> specHeaders = components.getHeaders();
        if (specHeaders == null || specHeaders.isEmpty()) {
            LOGGER.info(skipMsg);
            return null;
        }
        TreeMap<String, CodegenHeader> headers = new TreeMap<>();
        String headersJsonPath = "#/components/headers";
        generateXs(files, headersJsonPath, CodegenConstants.JSON_PATH_LOCATION_TYPE.HEADERS, CodegenConstants.HEADERS, null, true);
        for (Map.Entry<String, Header> entry: specHeaders.entrySet()) {
            String componentName = entry.getKey();
            Header specHeader = entry.getValue();
            String sourceJsonPath = headersJsonPath + "/" + componentName;
            CodegenHeader header = generator.fromHeader(specHeader, sourceJsonPath);
            headers.put(componentName, header);

            generateHeader(files, header, sourceJsonPath, "../../");

            // documentation
            Map<String, Object> templateData = new HashMap<>();
            templateData.put("packageName", generator.packageName());
            templateData.put("header", header);
            templateData.put("headerSize", "#");
            templateData.put("docRoot", "../../");
            templateData.put("identifierPieces", Collections.unmodifiableList(new ArrayList<>()));
            // TODO add flag to turn this off
            generateXDocs(files, sourceJsonPath, CodegenConstants.JSON_PATH_LOCATION_TYPE.HEADER, CodegenConstants.HEADER_DOCS, templateData, true);
        }
        // sort them
        headers = new TreeMap<>(headers);
        return headers;
    }

    protected TreeMap<String, CodegenSchema> generateSchemas(List<File> files) {
        if (!generateModels) {
            LOGGER.info("Skipping generation of component schemas.");
            return null;
        }

        final Map<String, Schema> specSchemas = ModelUtils.getSchemas(this.openAPI);
        if (specSchemas == null || specSchemas.isEmpty()) {
            LOGGER.warn("Skipping generation of component schemas because the specification document lacks them.");
            return null;
        }

        TreeMap<String, CodegenSchema> schemas = new TreeMap<>();
        String modelNames = GlobalSettings.getProperty("models");
        Set<String> modelsToGenerate = null;
        if (modelNames != null && !modelNames.isEmpty()) {
            modelsToGenerate = new HashSet<>(Arrays.asList(modelNames.split(",")));
        }

        // limit to only the specified models
        Set<String> componentNames = specSchemas.keySet();
        if (modelsToGenerate != null && !modelsToGenerate.isEmpty()) {
            Set<String> updatedKeys = new HashSet<>();
            for (String componentName: componentNames) {
                if (modelsToGenerate.contains(componentName)) {
                    updatedKeys.add(componentName);
                }
            }
            componentNames = updatedKeys;
        }

        // create model instances
        for (String componentName : componentNames) {
            try {
                Schema specSchema = specSchemas.get(componentName);

                String sourceJsonPath = "#/components/schemas/" + componentName;
                CodegenSchema codegenSchema = generator.fromSchema(specSchema, sourceJsonPath, sourceJsonPath);
                schemas.put(componentName, codegenSchema);

            } catch (Exception e) {
                throw new RuntimeException("Could not process model '" + componentName + "'" + ".Please make sure that your schema is correct!", e);
            }
        }

        generateXTests(files, "#/components", CodegenConstants.JSON_PATH_LOCATION_TYPE.COMPONENTS, CodegenConstants.MODELS, null, true);
        String schemasJsonPath = "#/components/schemas";
        generateXs(files, schemasJsonPath, CodegenConstants.JSON_PATH_LOCATION_TYPE.SCHEMAS, CodegenConstants.MODELS, null, true);
        generateXTests(files, schemasJsonPath, CodegenConstants.JSON_PATH_LOCATION_TYPE.SCHEMAS, CodegenConstants.MODELS, null, true);
        // generate files based on processed models
        for (Map.Entry<String, CodegenSchema> entry: schemas.entrySet()) {
            String componentName = entry.getKey();
            CodegenSchema schema = entry.getValue();
            try {
                // to generate model files
                String jsonPath = schemasJsonPath + "/" + componentName;
                generateSchema(files, schema, jsonPath);

                // to generate model test files
                Map<String, Object> schemaData = new HashMap<>();
                schemaData.put("packageName", generator.packageName());
                schemaData.put("schema", schema);
                schemaData.putAll(generator.additionalProperties());
                if (generateModelTests) {
                    generateXTests(files, jsonPath, CodegenConstants.JSON_PATH_LOCATION_TYPE.SCHEMA, CodegenConstants.MODELS, schemaData, true);
                }

                // to generate model documentation files
                if (generateModelDocumentation) {
                    generateSchemaDocumentation(files, schema, jsonPath, "../../");
                }

            } catch (Exception e) {
                throw new RuntimeException("Could not generate model '" + componentName + "'", e);
            }
        }
        if (GlobalSettings.getProperty("debugModels") != null) {
            LOGGER.info("############ Model info ############");
            Json.prettyPrint(schemas);
        }
        // sort them
        schemas = new TreeMap<>(schemas);
        return schemas;
    }

    @SuppressWarnings("unchecked")
    void generateApis(List<File> files, TreeMap<CodegenKey, CodegenPathItem> paths) {
        if (!generateApis) {
            LOGGER.info("Skipping generation of APIs.");
            return;
        }
        // accumulate tag to operations
        Set<String> allowListedTags = null;
        String apiNames = GlobalSettings.getProperty("apis");
        if (apiNames != null && !apiNames.isEmpty()) {
            allowListedTags = new HashSet<>(Arrays.asList(apiNames.split(",")));
        }
        String jsonPath = "#/apis";
        Map<String, String> apiPathsTemplates = generator.jsonPathTemplateFiles().get(CodegenConstants.JSON_PATH_LOCATION_TYPE.API_PATHS);
        if (apiPathsTemplates != null) {
            for (Map.Entry<String, String> apiPathEntry: apiPathsTemplates.entrySet()) {
                String templateFile = apiPathEntry.getKey();
                String apiFileName = apiPathEntry.getValue();
                String thisJsonPath = jsonPath + "/paths";
                Map<String, Object> apiData = new HashMap<>();
                String packageName = generator.packageName();
                apiData.put("packageName", packageName);
                String outputFile = generator.getFilepath(thisJsonPath) + apiFileName;
                generateFile(apiData, templateFile, outputFile, files, true, CodegenConstants.APIS);
            }
        }

        HashMap<CodegenTag, HashMap<CodegenKey, ArrayList<CodegenOperation>>> tagToPathToOperations = new HashMap<>();
        HashMap<CodegenTag, TreeMap<CodegenKey, HashMap<CodegenKey, CodegenOperation>>> tagToOperationIdToPathToOperation = new HashMap<>();
        Map<String, String> apiPathTemplates = generator.jsonPathTemplateFiles().get(CodegenConstants.JSON_PATH_LOCATION_TYPE.API_PATH);
        for(Map.Entry<CodegenKey, CodegenPathItem> entry: paths.entrySet()) {
            CodegenKey path = entry.getKey();
            CodegenPathItem pathItem = entry.getValue();

            if (apiPathTemplates != null) {
                for (Map.Entry<String, String> apiPathEntry: apiPathTemplates.entrySet()) {
                    String templateFile = apiPathEntry.getKey();
                    String suffix = apiPathEntry.getValue();
                    Map<String, Object> apiData = new HashMap<>();
                    String packageName = generator.packageName();
                    apiData.put("packageName", packageName);
                    apiData.put("path", path);
                    apiData.put("pathItem", pathItem);
                    String thisJsonPath = jsonPath + "/paths/" + ModelUtils.encodeSlashes(path.original);
                    String outputFile = generator.getFilepath(thisJsonPath) + suffix;
                    generateFile(apiData, templateFile, outputFile, files, true, CodegenConstants.APIS);
                }
            }

            // store operations by tag + path
            for(CodegenOperation op: pathItem.operations.values()) {
                for(CodegenTag tag: op.tags.values()) {
                    if (allowListedTags != null && !allowListedTags.contains(tag.name)) {
                        continue;
                    }
                    if (!tagToPathToOperations.containsKey(tag)) {
                        tagToPathToOperations.put(tag, new HashMap<>());
                        tagToOperationIdToPathToOperation.put(tag, new TreeMap<>());
                    }
                    HashMap<CodegenKey, ArrayList<CodegenOperation>> pathToOperations = tagToPathToOperations.get(tag);
                    if (!pathToOperations.containsKey(path)) {
                        pathToOperations.put(path, new ArrayList<>());
                    }
                    pathToOperations.get(path).add(op);
                    TreeMap<CodegenKey, HashMap<CodegenKey, CodegenOperation>> operationIdToPathToOperation = tagToOperationIdToPathToOperation.get(tag);
                    if (!operationIdToPathToOperation.containsKey(op.operationId)) {
                        HashMap<CodegenKey, CodegenOperation> pathToOperation = new HashMap<>();
                        pathToOperation.put(path, op);
                        operationIdToPathToOperation.put(op.operationId, pathToOperation);
                    }
                }
            }
        }

        // files in the apiPackage root folder
        Map<String, String> apiRootTemplates = generator.jsonPathTemplateFiles().get(CodegenConstants.JSON_PATH_LOCATION_TYPE.API_ROOT_FOLDER);
        if (apiRootTemplates != null) {
            for (Map.Entry<String, String> entry: apiRootTemplates.entrySet()) {
                String templateFile = entry.getKey();
                String fileName = entry.getValue();
                Map<String, Object> apiData = new HashMap<>();
                String packageName = generator.packageName();
                apiData.put("packageName", packageName);
                apiData.put("apiClassname", "Api");
                apiData.put("tagToPathToOperations", tagToPathToOperations);
                apiData.put("paths", paths);
                String outputFile = generator.getFilepath(jsonPath) + fileName;

                generateFile(apiData, templateFile, outputFile, files, true, CodegenConstants.APIS);
            }
        }

        Map<String, String> apiTagsTemplates = generator.jsonPathTemplateFiles().get(CodegenConstants.JSON_PATH_LOCATION_TYPE.API_TAGS);
        if (apiTagsTemplates != null) {
            for (Map.Entry<String, String> apiPathEntry: apiTagsTemplates.entrySet()) {
                String templateFile = apiPathEntry.getKey();
                String fileName = apiPathEntry.getValue();
                Map<String, Object> apiData = new HashMap<>();
                String packageName = generator.packageName();
                apiData.put("packageName", packageName);
                String thisJsonPath = jsonPath + "/tags";
                String outputFile = generator.getFilepath(thisJsonPath) + fileName;
                generateFile(apiData, templateFile, outputFile, files, true, CodegenConstants.APIS);
            }
        }

        Map<String, String> apiTagTemplates = generator.jsonPathTemplateFiles().get(CodegenConstants.JSON_PATH_LOCATION_TYPE.API_TAG);
        Map<String, String> apiDocTagTemplates = generator.jsonPathDocTemplateFiles().get(CodegenConstants.JSON_PATH_LOCATION_TYPE.API_TAG);
        for(Map.Entry<CodegenTag, HashMap<CodegenKey, ArrayList<CodegenOperation>>> entry: tagToPathToOperations.entrySet()) {
            CodegenTag tag = entry.getKey();
            HashMap<CodegenKey, ArrayList<CodegenOperation>> pathToOperations = entry.getValue();

            Map<String, Object> apiData = new HashMap<>();
            String packageName = generator.packageName();
            apiData.put("packageName", packageName);
            apiData.put("tag", tag);
            apiData.put("pathToOperations", pathToOperations);
            apiData.put("apiPackage", generator.apiPackage());

            class OperationIdComparator implements Comparator<CodegenKey>{
                @Override
                public int compare(CodegenKey e1, CodegenKey e2) {
                    return e1.snakeCase.compareTo(e2.snakeCase);
                }
            }

            TreeMap<CodegenKey, HashMap<CodegenKey, CodegenOperation>> operationIdToPathToOperation = new TreeMap<>(new OperationIdComparator());
            operationIdToPathToOperation.putAll(tagToOperationIdToPathToOperation.get(tag));
            apiData.put("operationIdToPathToOperation", operationIdToPathToOperation);

            if (apiTagTemplates != null) {
                for (Map.Entry<String, String> apiPathEntry: apiTagTemplates.entrySet()) {
                    String templateFile = apiPathEntry.getKey();
                    String fileName = apiPathEntry.getValue();
                    String thisJsonPath = jsonPath + "/tags/" + tag.name;
                    String outputFile = generator.getFilepath(thisJsonPath) + fileName;
                    generateFile(apiData, templateFile, outputFile, files, true, CodegenConstants.APIS);
                }
            }
            // api docs
            if (generateApiDocumentation && apiDocTagTemplates != null) {
                for (Map.Entry<String, String> apiPathEntry: apiDocTagTemplates.entrySet()) {
                    String templateFile = apiPathEntry.getKey();
                    String fileName = apiPathEntry.getValue();
                    String thisJsonPath = jsonPath + "/tags/" + tag.name;
                    String outputFile = generator.getDocsFilepath(thisJsonPath) + fileName;
                    generateFile(apiData, templateFile, outputFile, files, true, CodegenConstants.APIS);
                }
            }
        }
    }

    private void generateSupportingFiles(List<File> files, Map<String, Object> bundle) {
        if (!generateSupportingFiles) {
            // TODO: process these anyway and report via dryRun?
            LOGGER.info("Skipping generation of supporting files.");
            return;
        }
        Set<String> supportingFilesToGenerate = null;
        String supportingFiles = GlobalSettings.getProperty(CodegenConstants.SUPPORTING_FILES);
        if (supportingFiles != null && !supportingFiles.isEmpty()) {
            supportingFilesToGenerate = new HashSet<>(Arrays.asList(supportingFiles.split(",")));
        }

        for (SupportingFile support : generator.supportingFiles()) {
            try {
                String outputFolder = generator.outputFolder();
                if (StringUtils.isNotEmpty(support.getFolder())) {
                    outputFolder += File.separator + support.getFolder();
                }
                File of = new File(outputFolder);
                if (!of.isDirectory()) {
                    if (!dryRun && !of.mkdirs()) {
                        OnceLogger.once(LOGGER).debug("Output directory {} not created. It {}.", outputFolder, of.exists() ? "already exists." : "may not have appropriate permissions.");
                    }
                }
                String outputFilename = new File(support.getDestinationFilename()).isAbsolute() // split
                        ? support.getDestinationFilename()
                        : outputFolder + File.separator + support.getDestinationFilename().replace('/', File.separatorChar);

                boolean shouldGenerate = true;
                if (supportingFilesToGenerate != null && !supportingFilesToGenerate.isEmpty()) {
                    shouldGenerate = supportingFilesToGenerate.contains(support.getDestinationFilename());
                }

                File written = processTemplateToFile(bundle, support.getTemplateFile(), outputFilename, shouldGenerate, CodegenConstants.SUPPORTING_FILES);
                if (written != null) {
                    files.add(written);
                    if (generator.isEnablePostProcessFile() && !dryRun) {
                        generator.postProcessFile(written, "supporting-file");
                    }
                }
            } catch (Exception e) {
                throw new RuntimeException("Could not generate supporting file '" + support + "'", e);
            }
        }

        // Consider .openapi-generator-ignore a supporting file
        // Output .openapi-generator-ignore if it doesn't exist and wasn't explicitly created by a generator
        final String openapiGeneratorIgnore = ".openapi-generator-ignore";
        String ignoreFileNameTarget = generator.outputFolder() + File.separator + openapiGeneratorIgnore;
        File ignoreFile = new File(ignoreFileNameTarget);
        if (generateMetadata) {
            try {
                boolean shouldGenerate = !ignoreFile.exists();
                if (shouldGenerate && supportingFilesToGenerate != null && !supportingFilesToGenerate.isEmpty()) {
                    shouldGenerate = supportingFilesToGenerate.contains(openapiGeneratorIgnore);
                }
                File written = processTemplateToFile(bundle, openapiGeneratorIgnore, ignoreFileNameTarget, shouldGenerate, CodegenConstants.SUPPORTING_FILES);
                if (written != null) {
                    files.add(written);
                    if (generator.isEnablePostProcessFile() && !dryRun) {
                        generator.postProcessFile(written, "openapi-generator-ignore");
                    }
                }
            } catch (Exception e) {
                throw new RuntimeException("Could not generate supporting file '" + ignoreFileNameTarget + "'", e);
            }
        } else {
            this.templateProcessor.skip(ignoreFile.toPath(), "Skipped by generateMetadata option supplied by user.");
        }

        generateVersionMetadata(files);
    }

    Map<String, Object> buildSupportFileBundle(
            TreeMap<String, CodegenSchema> schemas,
            TreeMap<String, CodegenRequestBody> requestBodies,
            TreeMap<String, CodegenResponse> responses,
            TreeMap<String, CodegenHeader> headers,
            TreeMap<String, CodegenParameter> parameters,
            TreeMap<String, CodegenSecurityScheme> securitySchemes,
            List<CodegenServer> servers,
            TreeMap<CodegenKey, CodegenPathItem> paths,
            List<HashMap<String, CodegenSecurityRequirementValue>> security) {

        Map<String, Object> bundle = new HashMap<>(generator.additionalProperties());
        bundle.put("apiPackage", generator.apiPackage());

        URL url = URLPathUtils.getServerURL(openAPI, generator.serverVariableOverrides());
        boolean hasServers = false;
        if (servers != null) {
            hasServers = true;
        } else if (paths != null) {
            for (CodegenPathItem pathItem: paths.values()) {
                if (pathItem.servers != null) {
                    hasServers = true;
                    break;
                }
                if (pathItem.operations != null) {
                    for (CodegenOperation operation: pathItem.operations.values()) {
                        if (operation.servers != null) {
                            hasServers = true;
                            break;
                        }
                    }
                    if (hasServers) {
                        break;
                    }
                }
            }
        }

        bundle.put("openAPI", openAPI);
        bundle.put("scheme", URLPathUtils.getScheme(url, generator));
        bundle.put("contextPath", contextPath);
        bundle.put("requestBodies", requestBodies);
        bundle.put("responses", responses);
        bundle.put("headers", headers);
        bundle.put("parameters", parameters);
        bundle.put("schemas", schemas);
        bundle.put("securitySchemes", securitySchemes);
        bundle.put("servers", servers);
        bundle.put("hasServers", hasServers);  // also true if there are no root servers but there are pathItem/operation servers
        bundle.put("paths", paths);
        bundle.put("security", security);
        bundle.put("apiFolder", generator.apiPackage().replace('.', File.separatorChar));
        bundle.put("modelPackage", generator.modelPackage());
        bundle.put("library", generator.getLibrary());
        if (securitySchemes == null) {
            bundle.put("hasHttpSignatureSecurityScheme", false);
        } else {
            for (CodegenSecurityScheme ss: securitySchemes.values()) {
                if (ss.type.equals("http") && ss.scheme.equals("signature")) {
                    bundle.put("hasHttpSignatureSecurityScheme", true);
                }
            }
        }
        bundle.put("generatorLanguageVersion", generator.generatorLanguageVersion());
        // todo verify support and operation bundles have access to the common variables

        if (openAPI.getExternalDocs() != null) {
            bundle.put("externalDocs", openAPI.getExternalDocs());
        }

        generator.postProcessSupportingFileData(bundle);

        if (GlobalSettings.getProperty("debugSupportingFiles") != null) {
            LOGGER.info("############ Supporting file info ############");
            Json.prettyPrint(bundle);
        }
        return bundle;
    }

    private void generateServers(List<File> files, List<CodegenServer> servers, String jsonPath) {
        if (servers == null && servers.isEmpty()) {
            return;
        }
        generateXs(files, jsonPath, CodegenConstants.JSON_PATH_LOCATION_TYPE.SERVERS, CodegenConstants.SERVERS, null, true);

        int i = 0;
        for (CodegenServer server: servers) {
            Map<String, Object> templateData = new HashMap<>();
            templateData.put("packageName", generator.packageName());
            templateData.put("server", server);
            String serverJsonPath = jsonPath + "/" + i;
            generateXs(files, serverJsonPath, CodegenConstants.JSON_PATH_LOCATION_TYPE.SERVER, CodegenConstants.SERVERS, templateData, true);

            // doc generation
            if (server.rootServer) {
                templateData.put("headerSize", "#");
                templateData.put("identifierPieces", Collections.unmodifiableList(new ArrayList<>()));
                generateXDocs(files, serverJsonPath, CodegenConstants.JSON_PATH_LOCATION_TYPE.SERVER, CodegenConstants.SERVERS, templateData, true);
            }
            i++;
        }
    }

    private TreeMap<String, CodegenTag> getTags() {
        List<Tag> specTags = openAPI.getTags();
        if (specTags == null) {
            return null;
        }

        TreeMap<String, CodegenTag> tags = new TreeMap<>();
        for(Tag specTag: specTags) {
            String name = specTag.getName();
            CodegenTag tag = generator.fromTag(name, specTag.getDescription());
            tags.put(name, tag);
        }
        return tags;
    }

    private void generateSecurity(List<File> files, List<HashMap<String, CodegenSecurityRequirementValue>> security, String jsonPath) {
        if (security == null || security.isEmpty()) {
            return;
        }
        if (!generateApis) {
            LOGGER.info("Skipping generation of security because generateApis is set to false.");
            return;
        }
        generateXs(files, jsonPath, CodegenConstants.JSON_PATH_LOCATION_TYPE.SECURITIES, CodegenConstants.SECURITY, null, true);

        int i = 0;
        for (HashMap<String, CodegenSecurityRequirementValue> securityRequirementObject: security) {
            Map<String, Object> templateData = new HashMap<>();
            templateData.put("packageName", generator.packageName());
            templateData.put("securityRequirementObject", securityRequirementObject);
            String serverJsonPath = jsonPath + "/" + i;
            generateXs(files, serverJsonPath, CodegenConstants.JSON_PATH_LOCATION_TYPE.SECURITY, CodegenConstants.SECURITY, templateData, true);
            i++;
        }
    }

    @Override
    public List<File> generate() {
        if (openAPI == null) {
            throw new RuntimeException("Issues with the OpenAPI input. Possible causes: invalid/missing spec, malformed JSON/YAML files, etc.");
        }

        if (generator == null) {
            throw new RuntimeException("missing config!");
        }

        if (generator.getGeneratorMetadata() == null) {
            LOGGER.warn("Generator '{}' is missing generator metadata!", generator.getName());
        } else {
            GeneratorMetadata generatorMetadata = generator.getGeneratorMetadata();
            if (StringUtils.isNotEmpty(generatorMetadata.getGenerationMessage())) {
                LOGGER.info(generatorMetadata.getGenerationMessage());
            }

            Stability stability = generatorMetadata.getStability();
            String stabilityMessage = String.format(Locale.ROOT, "Generator '%s' is considered %s.", generator.getName(), stability.value());
            if (stability == Stability.DEPRECATED) {
                LOGGER.warn(stabilityMessage);
            } else {
                LOGGER.info(stabilityMessage);
            }
        }

        configureGeneratorProperties();
        configureOpenAPIInfo();

        generator.processOpenAPI(openAPI);

        processUserDefinedTemplates();

        List<File> files = new ArrayList<>();
        // tags
        TreeMap<String, CodegenTag> tags = getTags();
        // components.schemas / models
        TreeMap<String, CodegenSchema> schemas = generateSchemas(files);
        // components.requestBodies
        TreeMap<String, CodegenRequestBody> requestBodies = generateRequestBodies(files);
        // components.headers, must be before generateResponses, because those can $ref these
        TreeMap<String, CodegenHeader> headers = generateHeaders(files);
        // components.responses
        TreeMap<String, CodegenResponse> responses = generateResponses(files);
        // components.parameters, must be before processPaths, because those can $ref these
        TreeMap<String, CodegenParameter> parameters = generateParameters(files);
        // components.securitySchemes
        TreeMap<String, CodegenSecurityScheme> securitySchemes = generateSecuritySchemes(files);
        // security
        List<HashMap<String, CodegenSecurityRequirementValue>> security = generator.fromSecurity(openAPI.getSecurity(), "#/security");
        generateSecurity(files, security, "#/security");

        boolean schemasExist = (schemas != null && !schemas.isEmpty());
        boolean requestBodiesExist = (requestBodies != null && !requestBodies.isEmpty());
        boolean headersExist = (headers != null && !headers.isEmpty());
        boolean responsesExist = (responses != null && !responses.isEmpty());
        boolean parametersExist = (parameters != null && !parameters.isEmpty());
        if (schemasExist || requestBodiesExist || headersExist || responsesExist || parametersExist) {
            generateXs(files, "#/components", CodegenConstants.JSON_PATH_LOCATION_TYPE.COMPONENTS, CodegenConstants.COMPONENTS, null, true);
        }

        // servers
        String serversJsonPath = "#/servers";
        List<CodegenServer> servers = generator.fromServers(openAPI.getServers(), serversJsonPath);
        // paths
        TreeMap<CodegenKey, CodegenPathItem> paths = generator.fromPaths(openAPI.getPaths());
        generatePaths(files, paths, servers, security);
        generateServers(files, servers, serversJsonPath);
        // apis
        generateApis(files, paths);

        // supporting files
        Map<String, Object> bundle = buildSupportFileBundle(schemas, requestBodies, responses, headers, parameters, securitySchemes, servers, paths, security);
        generateSupportingFiles(files, bundle);

        if (dryRun) {
            boolean verbose = Boolean.parseBoolean(GlobalSettings.getProperty("verbose"));
            StringBuilder sb = new StringBuilder();

            sb.append(System.lineSeparator()).append(System.lineSeparator());
            sb.append("Dry Run Results:");
            sb.append(System.lineSeparator()).append(System.lineSeparator());

            Map<String, DryRunStatus> dryRunStatusMap = ((DryRunTemplateManager) this.templateProcessor).getDryRunStatusMap();

            dryRunStatusMap.entrySet().stream().sorted(Map.Entry.comparingByKey()).forEach(entry -> {
                DryRunStatus status = entry.getValue();
                try {
                    status.appendTo(sb);
                    sb.append(System.lineSeparator());
                    if (verbose) {
                        sb.append("  ")
                                .append(StringUtils.rightPad(status.getState().getDescription(), 20, "."))
                                .append(" ").append(status.getReason())
                                .append(System.lineSeparator());
                    }
                } catch (IOException e) {
                    LOGGER.debug("Unable to document dry run status for {}.", entry.getKey());
                }
            });

            sb.append(System.lineSeparator()).append(System.lineSeparator());
            sb.append("States:");
            sb.append(System.lineSeparator()).append(System.lineSeparator());

            for (DryRunStatus.State state : DryRunStatus.State.values()) {
                sb.append("  - ").append(state.getShortDisplay()).append(" ").append(state.getDescription()).append(System.lineSeparator());
            }

            sb.append(System.lineSeparator());

            LOGGER.error(sb.toString());
        } else {
            // This exists here rather than in the method which generates supporting files to avoid accidentally adding files after this metadata.
            if (generateSupportingFiles) {
                generateFilesMetadata(files);
            }
        }

        // post-process
        generator.postProcess();

        // reset GlobalSettings, so that the running thread can be reused for another generator-run
        GlobalSettings.reset();

        return files;
    }

    private void processUserDefinedTemplates() {
        // TODO: initial behavior is "merge" user defined with built-in templates. consider offering user a "replace" option.
        if (userDefinedTemplates != null && !userDefinedTemplates.isEmpty()) {
            Map<String, SupportingFile> supportingFilesMap = generator.supportingFiles().stream()
                    .collect(Collectors.toMap(TemplateDefinition::getTemplateFile, Function.identity(), (oldValue, newValue) -> oldValue));

            // TemplateFileType.SupportingFiles
            userDefinedTemplates.stream()
                    .filter(i -> i.getTemplateType().equals(TemplateFileType.SupportingFiles))
                    .forEach(userDefinedTemplate -> {
                        SupportingFile newFile = new SupportingFile(
                                userDefinedTemplate.getTemplateFile(),
                                userDefinedTemplate.getFolder(),
                                userDefinedTemplate.getDestinationFilename()
                        );
                        if (supportingFilesMap.containsKey(userDefinedTemplate.getTemplateFile())) {
                            SupportingFile f = supportingFilesMap.get(userDefinedTemplate.getTemplateFile());
                            generator.supportingFiles().remove(f);

                            if (!f.isCanOverwrite()) {
                                newFile.doNotOverwrite();
                            }
                        }
                        generator.supportingFiles().add(newFile);
                    });

            // Others, excluding TemplateFileType.SupportingFiles
            userDefinedTemplates.stream()
                    .filter(i -> !i.getTemplateType().equals(TemplateFileType.SupportingFiles))
                    .forEach(userDefinedTemplate -> {
                        // determine file extension…
                        // if template is in format api.ts.mustache, we'll extract .ts
                        // if user has provided an example destination filename, we'll use that extension
                        String templateFile = userDefinedTemplate.getTemplateFile();
                        int lastSeparator = templateFile.lastIndexOf('.');
                        String templateExt = FilenameUtils.getExtension(templateFile.substring(0, lastSeparator));
                        if (StringUtils.isBlank(templateExt)) {
                            // hack: destination filename in this scenario might be a suffix like Impl.java
                            templateExt = userDefinedTemplate.getDestinationFilename();
                        } else {
                            templateExt = StringUtils.prependIfMissing(templateExt, ".");
                        }

                        switch (userDefinedTemplate.getTemplateType()) {
                            case API:
                                Map<String, String> apiTemplateFiles = generator.jsonPathTemplateFiles().getOrDefault(CodegenConstants.JSON_PATH_LOCATION_TYPE.API_ROOT_FOLDER, new HashMap<>());
                                apiTemplateFiles.put(templateFile, templateExt);
                                break;
                            case Model:
                                Map<String, String> schemaTemplateToSuffix = generator.jsonPathTemplateFiles().getOrDefault(CodegenConstants.JSON_PATH_LOCATION_TYPE.SCHEMA, new HashMap<>());
                                schemaTemplateToSuffix.put(templateFile, templateExt);
                                break;
                            case APIDocs:
                                Map<String, String> apiDocTemplateToSuffix = generator.jsonPathDocTemplateFiles().getOrDefault(CodegenConstants.JSON_PATH_LOCATION_TYPE.API_ROOT_FOLDER, new HashMap<>());
                                apiDocTemplateToSuffix.put(templateFile, templateExt);
                                break;
                            case ModelDocs:
                                Map<String, String> schemaDocTemplateToSuffix = generator.jsonPathDocTemplateFiles().getOrDefault(CodegenConstants.JSON_PATH_LOCATION_TYPE.SCHEMA, new HashMap<>());
                                schemaDocTemplateToSuffix.put(templateFile, templateExt);
                                break;
                            case APITests:
                                Map<String, String> apiTestTemplateToSuffix = generator.jsonPathTestTemplateFiles().getOrDefault(CodegenConstants.JSON_PATH_LOCATION_TYPE.OPERATION, new HashMap<>());
                                apiTestTemplateToSuffix.put(templateFile, templateExt);
                                break;
                            case ModelTests:
                                Map<String, String> modelTestTemplateToSuffix = generator.jsonPathTestTemplateFiles().getOrDefault(CodegenConstants.JSON_PATH_LOCATION_TYPE.SCHEMA, new HashMap<>());
                                modelTestTemplateToSuffix.put(templateFile, templateExt);
                                break;
                            case SupportingFiles:
                                // excluded by filter
                                break;
                        }
                    });
        }
    }

    protected File processTemplateToFile(Map<String, Object> templateData, String templateName, String outputFilename, boolean shouldGenerate, String skippedByOption) throws IOException {
        return processTemplateToFile(templateData, templateName, outputFilename, shouldGenerate, skippedByOption, this.generator.getOutputDir());
    }

    private File processTemplateToFile(Map<String, Object> templateData, String templateName, String outputFilename, boolean shouldGenerate, String skippedByOption, String intendedOutputDir) throws IOException {
        String adjustedOutputFilename = outputFilename.replaceAll("//", "/").replace('/', File.separatorChar);
        File target = new File(adjustedOutputFilename);
        if (ignoreProcessor.allowsFile(target)) {
            if (shouldGenerate) {
                Path outDir = java.nio.file.Paths.get(intendedOutputDir).toAbsolutePath();
                Path absoluteTarget = target.toPath().toAbsolutePath();
                if (!absoluteTarget.startsWith(outDir)) {
                    throw new RuntimeException(String.format(Locale.ROOT, "Target files must be generated within the output directory; absoluteTarget=%s outDir=%s", absoluteTarget, outDir));
                }
                return this.templateProcessor.write(templateData, templateName, target);
            } else {
                this.templateProcessor.skip(target.toPath(), String.format(Locale.ROOT, "Skipped by %s options supplied by user.", skippedByOption));
                return null;
            }
        } else {
            this.templateProcessor.ignore(target.toPath(), "Ignored by rule in ignore file.");
            return null;
        }
    }

    private static String generateParameterId(Parameter parameter) {
        return parameter.getName() + ":" + parameter.getIn();
    }

    /**
     * Generates a file at .openapi-generator/VERSION to track the version of user's latest run.
     *
     * @param files The list tracking generated files
     */
    private void generateVersionMetadata(List<File> files) {
        String versionMetadata = generator.outputFolder() + File.separator + METADATA_DIR + File.separator + generator.getVersionMetadataFilename();
        if (generateMetadata) {
            File versionMetadataFile = new File(versionMetadata);
            try {
                File written = this.templateProcessor.writeToFile(versionMetadata, ImplementationVersion.read().getBytes(StandardCharsets.UTF_8));
                if (written != null) {
                    files.add(versionMetadataFile);
                    if (generator.isEnablePostProcessFile() && !dryRun) {
                        generator.postProcessFile(written, "openapi-generator-version");
                    }
                }
            } catch (IOException e) {
                throw new RuntimeException("Could not generate supporting file '" + versionMetadata + "'", e);
            }
        } else {
            Path metadata = java.nio.file.Paths.get(versionMetadata);
            this.templateProcessor.skip(metadata, "Skipped by generateMetadata option supplied by user.");
        }
    }

    private Path absPath(File input) {
        // intentionally creates a new absolute path instance, disconnected from underlying FileSystem provider of File
        return java.nio.file.Paths.get(input.getAbsolutePath());
    }

    /**
     * Generates a file at .openapi-generator/FILES to track the files created by the user's latest run.
     * This is ideal for CI and regeneration of code without stale/unused files from older generations.
     *
     * @param files The list tracking generated files
     */
    private void generateFilesMetadata(List<File> files) {
        if (generateMetadata) {
            try {
                StringBuilder sb = new StringBuilder();
                Path outDir = absPath(new File(this.generator.getOutputDir()));

                List<File> filesToSort = new ArrayList<>();

                // Avoid side-effecting sort in this path when generateMetadata=true
                files.forEach(f -> {
                    // We have seen NPE on CI for getPath() returning null, so guard against this (to be fixed in 5.0 template management refactor)
                    //noinspection ConstantConditions
                    if (f != null && f.getPath() != null) {
                        filesToSort.add(outDir.relativize(absPath(f)).normalize().toFile());
                    }
                });

                // NOTE: Don't use File.separator here as we write linux-style paths to FILES, and File.separator will
                // result in incorrect match on Windows machines.
                String relativeMeta = METADATA_DIR + "/VERSION";
                filesToSort.sort(PathFileComparator.PATH_COMPARATOR);
                filesToSort.forEach(f -> {
                    // some Java implementations don't honor .relativize documentation fully.
                    // When outDir is /a/b and the input is /a/b/c/d, the result should be c/d.
                    // Some implementations make the output ./c/d which seems to mix the logic
                    // as documented for symlinks. So we need to trim any / or ./ from the start,
                    // as nobody should be generating into system root and our expectation is no ./
                    String relativePath = removeStart(removeStart(f.toString(), "." + File.separator), File.separator);
                    if (File.separator.equals("\\")) {
                        // ensure that windows outputs same FILES format
                        relativePath = relativePath.replace(File.separator, "/");
                    }
                    if (!relativePath.equals(relativeMeta)) {
                        sb.append(relativePath).append(System.lineSeparator());
                    }
                });

                String targetFile = generator.outputFolder() + File.separator + METADATA_DIR + File.separator + generator.getFilesMetadataFilename();

                File filesFile = this.templateProcessor.writeToFile(targetFile, sb.toString().getBytes(StandardCharsets.UTF_8));
                if (filesFile != null) {
                    files.add(filesFile);
                }
            } catch (Exception e) {
                LOGGER.warn("Failed to write FILES metadata to track generated files.");
            }
        }
    }

    private String removeTrailingSlash(String value) {
        return StringUtils.removeEnd(value, "/");
    }

}
