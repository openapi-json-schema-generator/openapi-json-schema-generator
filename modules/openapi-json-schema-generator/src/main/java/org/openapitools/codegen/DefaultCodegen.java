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

package org.openapitools.codegen;

import com.github.benmanes.caffeine.cache.Cache;
import com.github.benmanes.caffeine.cache.Caffeine;
import com.github.benmanes.caffeine.cache.Ticker;
import com.google.common.collect.ImmutableMap;
import com.samskivert.mustache.Mustache;
import com.samskivert.mustache.Mustache.Compiler;
import com.samskivert.mustache.Mustache.Lambda;

import org.apache.commons.lang3.ObjectUtils;
import org.apache.commons.text.StringEscapeUtils;
import org.apache.commons.lang3.StringUtils;
import org.apache.commons.lang3.tuple.Pair;
import org.openapitools.codegen.CodegenDiscriminator.MappedModel;
import org.openapitools.codegen.api.TemplatingEngineAdapter;
import org.openapitools.codegen.config.GlobalSettings;
import org.openapitools.codegen.examples.ExampleGenerator;
import org.openapitools.codegen.meta.FeatureSet;
import org.openapitools.codegen.meta.GeneratorMetadata;
import org.openapitools.codegen.meta.Stability;
import org.openapitools.codegen.meta.features.*;
import org.openapitools.codegen.model.OperationsMap;
import org.openapitools.codegen.serializer.SerializerUtils;
import org.openapitools.codegen.templating.MustacheEngineAdapter;
import org.openapitools.codegen.templating.mustache.*;
import org.openapitools.codegen.utils.ModelUtils;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.io.File;
import java.util.*;
import java.util.Map.Entry;
import java.util.concurrent.ConcurrentSkipListSet;
import java.util.concurrent.TimeUnit;
import java.util.function.Consumer;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.stream.Collectors;
import java.util.stream.Stream;

import io.swagger.v3.core.util.Json;
import io.swagger.v3.oas.models.OpenAPI;
import io.swagger.v3.oas.models.Operation;
import io.swagger.v3.oas.models.PathItem;
import io.swagger.v3.oas.models.callbacks.Callback;
import io.swagger.v3.oas.models.examples.Example;
import io.swagger.v3.oas.models.headers.Header;
import io.swagger.v3.oas.models.media.*;
import io.swagger.v3.oas.models.parameters.*;
import io.swagger.v3.oas.models.responses.ApiResponse;
import io.swagger.v3.oas.models.security.OAuthFlow;
import io.swagger.v3.oas.models.security.OAuthFlows;
import io.swagger.v3.oas.models.security.SecurityScheme;
import io.swagger.v3.oas.models.servers.Server;
import io.swagger.v3.oas.models.servers.ServerVariable;
import io.swagger.v3.parser.util.SchemaTypeUtil;

import static org.openapitools.codegen.CodegenConstants.UNSUPPORTED_V310_SPEC_MSG;
import static org.openapitools.codegen.utils.OnceLogger.once;
import static org.openapitools.codegen.utils.StringUtils.*;

public class DefaultCodegen implements CodegenConfig {
    private final Logger LOGGER = LoggerFactory.getLogger(DefaultCodegen.class);

    public static FeatureSet DefaultFeatureSet;

    // A cache of sanitized words. The sanitizeName() method is invoked many times with the same
    // arguments, this cache is used to optimized performance.
    private static Cache<SanitizeNameOptions, String> sanitizedNameCache;
    private static final String xSchemaTestExamplesKey = "x-schema-test-examples";
    private static final String xSchemaTestExamplesRefPrefix = "#/components/x-schema-test-examples/";
    protected static Schema falseSchema;
    protected static Schema trueSchema = new Schema();

    static {
        DefaultFeatureSet = FeatureSet.newBuilder()
                .includeDataTypeFeatures(
                        DataTypeFeature.Int32, DataTypeFeature.Int64, DataTypeFeature.Float, DataTypeFeature.Double,
                        DataTypeFeature.Decimal, DataTypeFeature.String, DataTypeFeature.Byte, DataTypeFeature.Binary,
                        DataTypeFeature.Boolean, DataTypeFeature.Date, DataTypeFeature.DateTime, DataTypeFeature.Password,
                        DataTypeFeature.File, DataTypeFeature.Array, DataTypeFeature.Object, DataTypeFeature.Maps, DataTypeFeature.CollectionFormat,
                        DataTypeFeature.CollectionFormatMulti, DataTypeFeature.Enum, DataTypeFeature.ArrayOfEnum, DataTypeFeature.ArrayOfModel,
                        DataTypeFeature.ArrayOfCollectionOfPrimitives, DataTypeFeature.ArrayOfCollectionOfModel, DataTypeFeature.ArrayOfCollectionOfEnum,
                        DataTypeFeature.MapOfEnum, DataTypeFeature.MapOfModel, DataTypeFeature.MapOfCollectionOfPrimitives,
                        DataTypeFeature.MapOfCollectionOfModel, DataTypeFeature.MapOfCollectionOfEnum
                        // Custom types are template specific
                )
                .includeDocumentationFeatures(
                        DocumentationFeature.Api, DocumentationFeature.Model
                        // README is template specific
                )
                .includeGlobalFeatures(
                        GlobalFeature.Host, GlobalFeature.BasePath, GlobalFeature.Info, GlobalFeature.PartialSchemes,
                        GlobalFeature.Consumes, GlobalFeature.Produces, GlobalFeature.ExternalDocumentation, GlobalFeature.Examples,
                        GlobalFeature.Callbacks
                        // TODO: xml structures, styles, link objects, parameterized servers, full schemes for OAS 2.0
                )
                .includeSchemaSupportFeatures(
                        SchemaSupportFeature.Simple, SchemaSupportFeature.Composite,
                        SchemaSupportFeature.Polymorphism
                        // Union (OneOf) not 100% yet.
                )
                .includeParameterFeatures(
                        ParameterFeature.Path, ParameterFeature.Query, ParameterFeature.Header, ParameterFeature.Body,
                        ParameterFeature.FormUnencoded, ParameterFeature.FormMultipart, ParameterFeature.Cookie
                )
                .includeSecurityFeatures(
                        SecurityFeature.BasicAuth, SecurityFeature.ApiKey, SecurityFeature.BearerToken,
                        SecurityFeature.OAuth2_Implicit, SecurityFeature.OAuth2_Password,
                        SecurityFeature.OAuth2_ClientCredentials, SecurityFeature.OAuth2_AuthorizationCode
                        // OpenIDConnect not yet supported
                )
                .includeWireFormatFeatures(
                        WireFormatFeature.JSON, WireFormatFeature.XML
                        // PROTOBUF and Custom are generator specific
                )
                .build();

        int cacheSize = Integer.parseInt(GlobalSettings.getProperty(NAME_CACHE_SIZE_PROPERTY, "500"));
        int cacheExpiry = Integer.parseInt(GlobalSettings.getProperty(NAME_CACHE_EXPIRY_PROPERTY, "10"));
        sanitizedNameCache = Caffeine.newBuilder()
                .maximumSize(cacheSize)
                .expireAfterAccess(cacheExpiry, TimeUnit.SECONDS)
                .ticker(Ticker.systemTicker())
                .build();
        falseSchema = new Schema();
        falseSchema.setNot(new Schema());
    }

    protected GeneratorMetadata generatorMetadata;
    protected String inputSpec;
    protected String outputFolder = "";
    protected Set<String> defaultIncludes;
    protected Map<String, String> typeMapping;
    // instantiationTypes map from container types only: set, map, and array to the in language-type
    protected Map<String, String> instantiationTypes;
    protected Set<String> reservedWords;
    protected Set<String> languageSpecificPrimitives = new HashSet<>();
    protected Map<String, String> importMapping = new HashMap<>();
    // a map to store the mappping between a schema and the new one
    protected Map<String, String> schemaMapping = new HashMap<>();
    // a map to store the mappping between inline schema and the name provided by the user
    protected Map<String, String> inlineSchemaNameMapping = new HashMap<>();
    // a map to store the inline schema naming conventions
    protected Map<String, String> inlineSchemaNameDefault = new HashMap<>();
    protected String modelPackage = "", apiPackage = "", fileSuffix;
    protected String modelNamePrefix = "", modelNameSuffix = "";
    protected String apiNamePrefix = "", apiNameSuffix = "Api";
    protected String testPackage = "";
    protected String filesMetadataFilename = "FILES";
    protected String versionMetadataFilename = "VERSION";

    protected String packageName = "openapi_client";
    /*
    apiTemplateFiles are for API outputs only (controllers/handlers).
    API templates may be written multiple times; APIs are grouped by tag and the file is written once per tag group.
    */
    protected Map<String, String> apiTemplateFiles = new HashMap<>();
    protected Map<String, String> apiXToApiTemplateFiles = new HashMap<>();
    protected Map<String, String> modelTemplateFiles = new HashMap<>();
    protected Map<String, String> requestBodyTemplateFiles = new HashMap<>();
    protected Map<String, String> requestBodyDocTemplateFiles = new HashMap();
    protected Map<String, String> headerTemplateFiles = new HashMap<>();
    protected Map<String, String> headerDocTemplateFiles = new HashMap<>();
    protected Map<String, String> responseTemplateFiles = new HashMap<>();
    protected Map<String, String> responseDocTemplateFiles = new HashMap<>();
    protected Map<String, String> pathEndpointTemplateFiles = new HashMap();
    protected Set<String> pathEndpointDocTemplateFiles = new HashSet<>();
    protected Set<String> pathEndpointTestTemplateFiles = new HashSet<>();
    protected Map<String, String> pathEndpointRequestBodyTemplateFiles = new HashMap<>();
    protected Set<String> pathEndpointParameterTemplateFiles = new HashSet<>();
    protected Map<String, String> pathEndpointResponseTemplateFiles = new HashMap<>();
    protected Set<String> pathEndpointResponseHeaderTemplateFiles = new HashSet<>();
    protected Map<String, String> apiTestTemplateFiles = new HashMap<>();
    protected Map<String, String> modelTestTemplateFiles = new HashMap<>();
    protected Map<String, String> apiDocTemplateFiles = new HashMap<>();
    protected Map<String, String> modelDocTemplateFiles = new HashMap<>();
    protected Map<String, String> parameterTemplateFiles = new HashMap<>();
    protected Map<String, String> parameterDocTemplateFiles = new HashMap<>();
    protected Map<String, String> reservedWordsMappings = new HashMap<>();
    protected String templateDir;
    protected String embeddedTemplateDir;
    protected Map<String, Object> additionalProperties = new HashMap<>();
    protected Map<String, String> serverVariables = new HashMap<>();
    protected Map<String, Object> vendorExtensions = new HashMap<>();
    /*
    Supporting files are those which aren't models, APIs, or docs.
    These get a different map of data bound to the templates. Supporting files are written once.
    See also 'apiTemplateFiles'.
    */
    protected List<SupportingFile> supportingFiles = new ArrayList<>();
    protected List<CliOption> cliOptions = new ArrayList<>();
    protected boolean skipOverwrite;
    protected boolean removeOperationIdPrefix;
    protected String removeOperationIdPrefixDelimiter = "_";
    protected int removeOperationIdPrefixCount = 1;
    protected boolean skipOperationExample;

    protected final static Pattern JSON_MIME_PATTERN = Pattern.compile("(?i)application\\/json(;.*)?");
    protected final static Pattern JSON_VENDOR_MIME_PATTERN = Pattern.compile("(?i)application\\/vnd.(.*)+json(;.*)?");
    private static final Pattern COMMON_PREFIX_ENUM_NAME = Pattern.compile("[a-zA-Z0-9]+\\z");

    /**
     * True if the code generator supports multiple class inheritance.
     * This is used to model the parent hierarchy based on the 'allOf' composed schemas.
     */
    protected boolean supportsMultipleInheritance;
    /**
     * True if the code generator supports single class inheritance.
     * This is used to model the parent hierarchy based on the 'allOf' composed schemas.
     * Note: the single-class inheritance technique has inherent limitations because
     * a 'allOf' composed schema may have multiple $ref child schemas, each one
     * potentially representing a "parent" in the class inheritance hierarchy.
     * Some language generators also use class inheritance to implement the `additionalProperties`
     * keyword. For example, the Java code generator may generate 'extends HashMap'.
     */
    protected boolean supportsInheritance;
    /**
     * True if the language generator supports the 'additionalProperties' keyword
     * as sibling of a composed (allOf/anyOf/oneOf) schema.
     * Note: all language generators should support this to comply with the OAS specification.
     */
    protected boolean supportsAdditionalPropertiesWithComposedSchema;
    protected boolean supportsMixins;
    protected Map<String, String> supportedLibraries = new LinkedHashMap<>();
    protected String library;
    protected Boolean sortParamsByRequiredFlag = true;
    protected Boolean sortModelPropertiesByRequiredFlag = false;
    protected Boolean ensureUniqueParams = true;
    protected Boolean allowUnicodeIdentifiers = false;
    protected String gitHost, gitUserId, gitRepoId, releaseNote;
    protected String httpUserAgent;
    protected Boolean hideGenerationTimestamp = true;
    // How to encode special characters like $
    // They are translated to words like "Dollar" and prefixed with '
    // Then translated back during JSON encoding and decoding
    protected Map<String, String> specialCharReplacements = new LinkedHashMap<>();
    // When a model is an alias for a simple type
    protected Map<String, String> typeAliases = null;
    // The extension of the generated documentation files (defaults to markdown .md)
    protected String docExtension;
    protected String ignoreFilePathOverride;
    // flag to indicate whether to use environment variable to post process file
    protected boolean enablePostProcessFile = false;
    private TemplatingEngineAdapter templatingEngine = new MustacheEngineAdapter();
    // flag to indicate whether to use the utils.OneOfImplementorAdditionalData related logic
    protected boolean useOneOfInterfaces = false;
    // whether or not the oneOf imports machinery should add oneOf interfaces as imports in implementing classes
    protected boolean addOneOfInterfaceImports = false;
    protected List<CodegenSchema> addOneOfInterfaces = new ArrayList<>();

    // flag to indicate whether to only update files whose contents have changed
    protected boolean enableMinimalUpdate = false;

    // acts strictly upon a spec, potentially modifying it to have consistent behavior across generators.
    protected boolean strictSpecBehavior = true;
    // flag to indicate whether enum value prefixes are removed
    protected boolean removeEnumValuePrefix = true;

    // Support legacy logic for evaluating discriminators
    protected boolean legacyDiscriminatorBehavior = true;

    // Specify what to do if the 'additionalProperties' keyword is not present in a schema.
    // See CodegenConstants.java for more details.
    protected boolean disallowAdditionalPropertiesIfNotPresent = true;

    // If the server adds new enum cases, that are unknown by an old spec/client, the client will fail to parse the network response.
    // With this option enabled, each enum will have a new case, 'unknown_default_open_api', so that when the server sends an enum case that is not known by the client/spec, they can safely fallback to this case.
    protected boolean enumUnknownDefaultCase = false;
    protected String enumUnknownDefaultCaseName = "unknown_default_open_api";

    // make openapi available to all methods
    protected OpenAPI openAPI;

    // A cache to efficiently lookup a Schema instance based on the return value of `toModelName()`.
    private Map<String, Schema> modelNameToSchemaCache;

    // A cache to efficiently lookup schema `toModelName()` based on the schema Key
    private final Map<String, String> schemaKeyToModelNameCache = new HashMap<>();

    protected boolean loadDeepObjectIntoItems = true;

    // if true then baseTypes will be imported
    protected boolean importBaseType = true;

    // if True codegenParameter and codegenResponse imports will come
    // from deeper schema defined locations
    protected boolean addSchemaImportsFromV3SpecLocations = false;

    protected boolean addSuffixToDuplicateOperationNicknames = true;

    public boolean getAddSuffixToDuplicateOperationNicknames() {
        return addSuffixToDuplicateOperationNicknames;
    }

    @Override
    public List<CliOption> cliOptions() {
        return cliOptions;
    }

    @Override
    public void processOpts() {

        if (additionalProperties.containsKey(CodegenConstants.TEMPLATE_DIR)) {
            this.setTemplateDir((String) additionalProperties.get(CodegenConstants.TEMPLATE_DIR));
        }

        if (additionalProperties.containsKey(CodegenConstants.MODEL_PACKAGE)) {
            this.setModelPackage((String) additionalProperties.get(CodegenConstants.MODEL_PACKAGE));
        }

        if (additionalProperties.containsKey(CodegenConstants.API_PACKAGE)) {
            this.setApiPackage((String) additionalProperties.get(CodegenConstants.API_PACKAGE));
        }

        if (additionalProperties.containsKey(CodegenConstants.HIDE_GENERATION_TIMESTAMP)) {
            setHideGenerationTimestamp(convertPropertyToBooleanAndWriteBack(CodegenConstants.HIDE_GENERATION_TIMESTAMP));
        } else {
            additionalProperties.put(CodegenConstants.HIDE_GENERATION_TIMESTAMP, hideGenerationTimestamp);
        }

        if (additionalProperties.containsKey(CodegenConstants.SORT_PARAMS_BY_REQUIRED_FLAG)) {
            this.setSortParamsByRequiredFlag(Boolean.valueOf(additionalProperties
                    .get(CodegenConstants.SORT_PARAMS_BY_REQUIRED_FLAG).toString()));
        }

        if (additionalProperties.containsKey(CodegenConstants.SORT_MODEL_PROPERTIES_BY_REQUIRED_FLAG)) {
            this.setSortModelPropertiesByRequiredFlag(Boolean.valueOf(additionalProperties
                    .get(CodegenConstants.SORT_MODEL_PROPERTIES_BY_REQUIRED_FLAG).toString()));
        }

        if (additionalProperties.containsKey(CodegenConstants.ENSURE_UNIQUE_PARAMS)) {
            this.setEnsureUniqueParams(Boolean.valueOf(additionalProperties
                    .get(CodegenConstants.ENSURE_UNIQUE_PARAMS).toString()));
        }

        if (additionalProperties.containsKey(CodegenConstants.ALLOW_UNICODE_IDENTIFIERS)) {
            this.setAllowUnicodeIdentifiers(Boolean.valueOf(additionalProperties
                    .get(CodegenConstants.ALLOW_UNICODE_IDENTIFIERS).toString()));
        }

        if (additionalProperties.containsKey(CodegenConstants.API_NAME_PREFIX)) {
            this.setApiNamePrefix((String) additionalProperties.get(CodegenConstants.API_NAME_PREFIX));
        }

        if (additionalProperties.containsKey(CodegenConstants.API_NAME_SUFFIX)) {
            this.setApiNameSuffix((String) additionalProperties.get(CodegenConstants.API_NAME_SUFFIX));
        }

        if (additionalProperties.containsKey(CodegenConstants.MODEL_NAME_PREFIX)) {
            this.setModelNamePrefix((String) additionalProperties.get(CodegenConstants.MODEL_NAME_PREFIX));
        }

        if (additionalProperties.containsKey(CodegenConstants.MODEL_NAME_SUFFIX)) {
            this.setModelNameSuffix((String) additionalProperties.get(CodegenConstants.MODEL_NAME_SUFFIX));
        }

        if (additionalProperties.containsKey(CodegenConstants.REMOVE_OPERATION_ID_PREFIX)) {
            this.setRemoveOperationIdPrefix(Boolean.parseBoolean(additionalProperties
                    .get(CodegenConstants.REMOVE_OPERATION_ID_PREFIX).toString()));
        }

        if (additionalProperties.containsKey(CodegenConstants.REMOVE_OPERATION_ID_PREFIX_DELIMITER)) {
            this.setRemoveOperationIdPrefixDelimiter(additionalProperties
                    .get(CodegenConstants.REMOVE_OPERATION_ID_PREFIX_DELIMITER).toString());
        }

        if (additionalProperties.containsKey(CodegenConstants.REMOVE_OPERATION_ID_PREFIX_COUNT)) {
            this.setRemoveOperationIdPrefixCount(Integer.parseInt(additionalProperties
                    .get(CodegenConstants.REMOVE_OPERATION_ID_PREFIX_COUNT).toString()));
        }

        if (additionalProperties.containsKey(CodegenConstants.SKIP_OPERATION_EXAMPLE)) {
            this.setSkipOperationExample(Boolean.parseBoolean(additionalProperties
                    .get(CodegenConstants.SKIP_OPERATION_EXAMPLE).toString()));
        }

        if (additionalProperties.containsKey(CodegenConstants.DOCEXTENSION)) {
            this.setDocExtension(String.valueOf(additionalProperties
                    .get(CodegenConstants.DOCEXTENSION).toString()));
        }

        if (additionalProperties.containsKey(CodegenConstants.ENABLE_POST_PROCESS_FILE)) {
            this.setEnablePostProcessFile(Boolean.parseBoolean(additionalProperties
                    .get(CodegenConstants.ENABLE_POST_PROCESS_FILE).toString()));
        }

        if (additionalProperties.containsKey(CodegenConstants.REMOVE_ENUM_VALUE_PREFIX)) {
            this.setRemoveEnumValuePrefix(Boolean.parseBoolean(additionalProperties
                    .get(CodegenConstants.REMOVE_ENUM_VALUE_PREFIX).toString()));
        }

        if (additionalProperties.containsKey(CodegenConstants.LEGACY_DISCRIMINATOR_BEHAVIOR)) {
            this.setLegacyDiscriminatorBehavior(Boolean.parseBoolean(additionalProperties
                    .get(CodegenConstants.LEGACY_DISCRIMINATOR_BEHAVIOR).toString()));
        }
        if (additionalProperties.containsKey(CodegenConstants.DISALLOW_ADDITIONAL_PROPERTIES_IF_NOT_PRESENT)) {
            this.setDisallowAdditionalPropertiesIfNotPresent(Boolean.parseBoolean(additionalProperties
                    .get(CodegenConstants.DISALLOW_ADDITIONAL_PROPERTIES_IF_NOT_PRESENT).toString()));
        }
        if (additionalProperties.containsKey(CodegenConstants.ENUM_UNKNOWN_DEFAULT_CASE)) {
            this.setEnumUnknownDefaultCase(Boolean.parseBoolean(additionalProperties
                    .get(CodegenConstants.ENUM_UNKNOWN_DEFAULT_CASE).toString()));
        }
    }

    /***
     * Preset map builder with commonly used Mustache lambdas.
     *
     * To extend the map, override addMustacheLambdas(), call parent method
     * first and then add additional lambdas to the returned builder.
     *
     * If common lambdas are not desired, override addMustacheLambdas() method
     * and return empty builder.
     *
     * @return preinitialized map with common lambdas
     */
    protected ImmutableMap.Builder<String, Lambda> addMustacheLambdas() {

        return new ImmutableMap.Builder<String, Mustache.Lambda>()
                .put("lowercase", new LowercaseLambda().generator(this))
                .put("uppercase", new UppercaseLambda())
                .put("snakecase", new SnakecaseLambda())
                .put("titlecase", new TitlecaseLambda())
                .put("camelcase", new CamelCaseLambda(true).generator(this))
                .put("pascalcase", new CamelCaseLambda(false).generator(this))
                .put("indented", new IndentedLambda())
                .put("indented_8", new IndentedLambda(8, " "))
                .put("indented_12", new IndentedLambda(12, " "))
                .put("indented_16", new IndentedLambda(16, " "));
    }

    private void registerMustacheLambdas() {
        ImmutableMap<String, Lambda> lambdas = addMustacheLambdas().build();

        if (lambdas.size() == 0) {
            return;
        }

        if (additionalProperties.containsKey("lambda")) {
            LOGGER.error("A property called 'lambda' already exists in additionalProperties");
            throw new RuntimeException("A property called 'lambda' already exists in additionalProperties");
        }
        additionalProperties.put("lambda", lambdas);
    }

    // override with any special post-processing for all models
    @Override
    @SuppressWarnings("static-method")
    public TreeMap<String, CodegenSchema> postProcessAllModels(TreeMap<String, CodegenSchema> schemas) {
        return schemas;
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
            ModelUtils.getSchemas(openAPI).forEach((key, schema) -> m.put(toModelName(key), schema));
            modelNameToSchemaCache = Collections.unmodifiableMap(m);
        }
        return modelNameToSchemaCache;
    }

    @Override
    public String packageName() {
        return packageName;
    }

    public String packagePath() {
        return packageName.replace('.', File.separatorChar);
    }

    /**
     * Index all CodegenModels by model name.
     *
     * @param objs Map of models
     * @return map of all models indexed by names
     */
    public TreeMap<String, CodegenSchema> getAllModels(TreeMap<String, CodegenSchema> objs) {
        return objs;
    }

    /**
     * Loop through all models to update different flags (e.g. isSelfReference), children models, etc
     *
     * @param objs Map of models
     * @return maps of models with various updates
     */
    @Override
    public TreeMap<String, CodegenSchema> updateAllModels(TreeMap<String, CodegenSchema> objs) {
        return objs;
    }

    // override with any special post-processing
    @Override
    @SuppressWarnings("static-method")
    public TreeMap<String, CodegenSchema> postProcessModels(TreeMap<String, CodegenSchema> objs) {
        return objs;
    }

    /**
     * post process enum defined in model's properties
     *
     * @param objs Map of models
     * @return maps of models with better enum support
     */
    public TreeMap<String, CodegenSchema> postProcessModelsEnum(TreeMap<String, CodegenSchema> objs) {
        for (CodegenSchema cm : objs.values()) {

            // for enum model
            if (Boolean.TRUE.equals(cm.isEnum) && cm.allowableValues != null) {
                Map<String, Object> allowableValues = cm.allowableValues;
                List<Object> values = (List<Object>) allowableValues.get("values");
                List<Map<String, Object>> enumVars = buildEnumVars(values, cm);
                // if "x-enum-varnames" or "x-enum-descriptions" defined, update varnames
                updateEnumVarsWithExtensions(enumVars, cm.getVendorExtensions(), cm);
                cm.allowableValues.put("enumVars", enumVars);
            }

            // update codegen property enum with proper naming convention
            // and handling of numbers, special characters
            if (cm.getRequiredProperties() != null) {
                for (CodegenSchema var : cm.getRequiredProperties().values()) {
                    if (var == null) {
                        continue;
                    }
                    updateCodegenPropertyEnum(var);
                }
            }

            if (cm.getOptionalProperties() != null) {
                for (CodegenSchema var : cm.getOptionalProperties().values()) {
                    updateCodegenPropertyEnum(var);
                }
            }
        }
        return objs;
    }

    /**
     * Returns the common prefix of variables for enum naming if
     * two or more variables are present
     *
     * @param vars List of variable names
     * @return the common prefix for naming
     */
    public String findCommonPrefixOfVars(List<Object> vars) {
        if (vars.size() > 1) {
            try {
                String[] listStr = vars.toArray(new String[vars.size()]);
                String prefix = StringUtils.getCommonPrefix(listStr);
                // exclude trailing characters that should be part of a valid variable
                // e.g. ["status-on", "status-off"] => "status-" (not "status-o")
                final Matcher matcher = COMMON_PREFIX_ENUM_NAME.matcher(prefix);
                return matcher.replaceAll("");
            } catch (ArrayStoreException e) {
                // do nothing, just return default value
            }
        }
        return "";
    }

    /**
     * Return the enum default value in the language specified format
     *
     * @param value    enum variable name
     * @param prop property
     * @return the default value for the enum
     */
    public String toEnumDefaultValue(String value, CodegenSchema prop) {
        return value;
    }

    /**
     * Return the enum value in the language specified format
     * e.g. status becomes "status"
     *
     * @param value    enum variable name
     * @param prop property
     * @return the sanitized value for enum
     */
    public String toEnumValue(String value, CodegenSchema prop) {
        if (prop.isNumber || prop.isBoolean) {
            return value;
        } else {
            return "\"" + escapeText(value) + "\"";
        }
    }

    /**
     * Return the sanitized variable name for enum
     *
     * @param value    enum variable name
     * @param prop the property that holds the data type booleans
     * @return the sanitized variable name for enum
     */
    public String toEnumVarName(String value, CodegenSchema prop) {
        if (value.length() == 0) {
            return "EMPTY";
        }

        String var = value.replaceAll("\\W+", "_").toUpperCase(Locale.ROOT);
        if (var.matches("\\d.*")) {
            return "_" + var;
        } else {
            return var;
        }
    }

    /**
     * Set the OpenAPI document.
     * This method is invoked when the input OpenAPI document has been parsed and validated.
     */
    @Override
    public void setOpenAPI(OpenAPI openAPI) {
        String originalSpecVersion;
        String xOriginalSwaggerVersion = "x-original-swagger-version";
        if (openAPI.getExtensions() != null && !openAPI.getExtensions().isEmpty() && openAPI.getExtensions().containsValue(xOriginalSwaggerVersion)) {
            originalSpecVersion = (String) openAPI.getExtensions().get(xOriginalSwaggerVersion);
        } else {
            originalSpecVersion = openAPI.getOpenapi();
        }
        Integer specMajorVersion = Integer.parseInt(originalSpecVersion.substring(0, 1));
        Integer specMinorVersion = Integer.parseInt(originalSpecVersion.substring(2, 3));
        boolean specVersionGreaterThanOrEqualTo310 = (specMajorVersion == 3 && specMinorVersion >= 1);
        if (specVersionGreaterThanOrEqualTo310) {
            LOGGER.warn(UNSUPPORTED_V310_SPEC_MSG);
        }
        this.openAPI = openAPI;
        // Set global settings such that helper functions in ModelUtils can lookup the value
        // of the CLI option.
        ModelUtils.setDisallowAdditionalPropertiesIfNotPresent(getDisallowAdditionalPropertiesIfNotPresent());
    }

    // override with any message to be shown right before the process finishes
    @Override
    @SuppressWarnings("static-method")
    public void postProcess() {
        System.out.println("################################################################################");
        System.out.println("# Thanks for using OpenAPI Generator.                                          #");
        System.out.println("# Please consider donation to help us maintain this project \uD83D\uDE4F                 #");
        System.out.println("# https://opencollective.com/openapi_generator/donate                          #");
        System.out.println("################################################################################");
    }

    // override with any special post-processing
    @Override
    @SuppressWarnings("static-method")
    public OperationsMap postProcessOperationsWithModels(OperationsMap objs, TreeMap<String, CodegenSchema> schemas) {
        return objs;
    }

    // override with any special post-processing
    @Override
    @SuppressWarnings("static-method")
    public Map<String, Object> postProcessSupportingFileData(Map<String, Object> objs) {
        return objs;
    }

    // override to post-process any model properties
    @Override
    @SuppressWarnings("unused")
    public void postProcessModelProperty(CodegenSchema model, CodegenSchema property) {
    }

    // override to post-process any parameters
    @Override
    @SuppressWarnings("unused")
    public void postProcessParameter(CodegenParameter parameter) {
    }

    //override with any special handling of the entire OpenAPI spec document
    @Override
    @SuppressWarnings("unused")
    public void preprocessOpenAPI(OpenAPI openAPI) {
        if (useOneOfInterfaces && openAPI.getComponents() != null) {
            // we process the openapi schema here to find oneOf schemas and create interface models for them
            Map<String, Schema> schemas = new HashMap<>(openAPI.getComponents().getSchemas());
            if (schemas == null) {
                schemas = new HashMap<>();
            }
            Map<String, PathItem> pathItems = openAPI.getPaths();

            // we need to add all request and response bodies to processed schemas
            if (pathItems != null) {
                for (Map.Entry<String, PathItem> e : pathItems.entrySet()) {
                    for (Map.Entry<PathItem.HttpMethod, Operation> op : e.getValue().readOperationsMap().entrySet()) {
                        String opId = getOrGenerateOperationId(op.getValue(), e.getKey(), op.getKey().toString());
                        // process request body
                        RequestBody b = ModelUtils.getReferencedRequestBody(openAPI, op.getValue().getRequestBody());
                        Schema requestSchema = null;
                        if (b != null) {
                            requestSchema = ModelUtils.getSchemaFromRequestBody(b);
                        }
                        if (requestSchema != null) {
                            schemas.put(opId, requestSchema);
                        }
                        // process all response bodies
                        if (op.getValue().getResponses() != null) {
                            for (Map.Entry<String, ApiResponse> ar : op.getValue().getResponses().entrySet()) {
                                ApiResponse a = ModelUtils.getReferencedApiResponse(openAPI, ar.getValue());
                                Schema responseSchema = ModelUtils.getSchemaFromResponse(a);
                                if (responseSchema != null) {
                                    schemas.put(opId + ar.getKey(), responseSchema);
                                }
                            }
                        }
                    }
                }
            }

            // also add all properties of all schemas to be checked for oneOf
            Map<String, Schema> propertySchemas = new HashMap<>();
            for (Map.Entry<String, Schema> e : schemas.entrySet()) {
                Schema s = e.getValue();
                Map<String, Schema> props = s.getProperties();
                if (props == null) {
                    props = new HashMap<>();
                }
                for (Map.Entry<String, Schema> p : props.entrySet()) {
                    propertySchemas.put(e.getKey() + "/" + p.getKey(), p.getValue());
                }
            }
            schemas.putAll(propertySchemas);

            // go through all gathered schemas and add them as interfaces to be created
            for (Map.Entry<String, Schema> e : schemas.entrySet()) {
                String schemaName = e.getKey();
                String sourceJsonPath = "#/components/schemas/" + schemaName;
                String n = toModelName(e.getKey());
                Schema s = e.getValue();
                String nOneOf = toModelName(n + "OneOf");
                if (ModelUtils.isComposedSchema(s)) {
                    if (e.getKey().contains("/")) {
                        // if this is property schema, we also need to generate the oneOf interface model
                        addOneOfNameExtension((ComposedSchema) s, nOneOf);
                    } else {
                        // else this is a component schema, so we will just use that as the oneOf interface model
                        addOneOfNameExtension((ComposedSchema) s, n);
                    }
                } else if (ModelUtils.isArraySchema(s)) {
                    Schema items = ((ArraySchema) s).getItems();
                    if (ModelUtils.isComposedSchema(items)) {
                        addOneOfNameExtension((ComposedSchema) items, nOneOf);
                    }
                } else if (ModelUtils.isMapSchema(s)) {
                    Schema addProps = getAdditionalProperties(s);
                    if (addProps != null && ModelUtils.isComposedSchema(addProps)) {
                        addOneOfNameExtension((ComposedSchema) addProps, nOneOf);
                    }
                }
            }
        }
    }

    // override with any special handling of the entire OpenAPI spec document
    @Override
    @SuppressWarnings("unused")
    public void processOpenAPI(OpenAPI openAPI) {
    }

    // override with any special handling of the JMustache compiler
    @Override
    @SuppressWarnings("unused")
    public Compiler processCompiler(Compiler compiler) {
        return compiler;
    }

    // override with any special handling for the templating engine
    @Override
    @SuppressWarnings("unused")
    public TemplatingEngineAdapter processTemplatingEngine(TemplatingEngineAdapter templatingEngine) {
        return templatingEngine;
    }

    // override with any special text escaping logic
    @Override
    @SuppressWarnings("static-method")
    public String escapeText(String input) {
        if (input == null) {
            return input;
        }

        // remove \t, \n, \r
        // replace \ with \\
        // replace " with \"
        // outer unescape to retain the original multi-byte characters
        // finally escalate characters avoiding code injection
        return escapeUnsafeCharacters(
                StringEscapeUtils.unescapeJava(
                                StringEscapeUtils.escapeJava(input)
                                        .replace("\\/", "/"))
                        .replaceAll("[\\t\\n\\r]", " ")
                        .replace("\\", "\\\\")
                        .replace("\"", "\\\""));
    }

    /**
     * Escape characters while allowing new lines
     *
     * @param input String to be escaped
     * @return escaped string
     */
    @Override
    public String escapeTextWhileAllowingNewLines(String input) {
        if (input == null) {
            return input;
        }

        // remove \t
        // replace \ with \\
        // replace " with \"
        // outer unescape to retain the original multi-byte characters
        // finally escalate characters avoiding code injection
        return escapeUnsafeCharacters(
                StringEscapeUtils.unescapeJava(
                                StringEscapeUtils.escapeJava(input)
                                        .replace("\\/", "/"))
                        .replaceAll("[\\t]", " ")
                        .replace("\\", "\\\\")
                        .replace("\"", "\\\""));
    }

    // override with any special encoding and escaping logic
    @Override
    @SuppressWarnings("static-method")
    public String encodePath(String input) {
        return escapeText(input);
    }

    /**
     * override with any special text escaping logic to handle unsafe
     * characters so as to avoid code injection
     *
     * @param input String to be cleaned up
     * @return string with unsafe characters removed or escaped
     */
    @Override
    public String escapeUnsafeCharacters(String input) {
        LOGGER.warn("escapeUnsafeCharacters should be overridden in the code generator with proper logic to escape " +
                "unsafe characters");
        // doing nothing by default and code generator should implement
        // the logic to prevent code injection
        // later we'll make this method abstract to make sure
        // code generator implements this method
        return input;
    }

    /**
     * Escape single and/or double quote to avoid code injection
     *
     * @param input String to be cleaned up
     * @return string with quotation mark removed or escaped
     */
    @Override
    public String escapeQuotationMark(String input) {
        LOGGER.warn("escapeQuotationMark should be overridden in the code generator with proper logic to escape " +
                "single/double quote");
        return input.replace("\"", "\\\"");
    }

    @Override
    public Set<String> defaultIncludes() {
        return defaultIncludes;
    }

    @Override
    public Map<String, String> typeMapping() {
        return typeMapping;
    }

    @Override
    public Map<String, String> instantiationTypes() {
        return instantiationTypes;
    }

    @Override
    public Set<String> reservedWords() {
        return reservedWords;
    }

    @Override
    public Set<String> languageSpecificPrimitives() {
        return languageSpecificPrimitives;
    }

    @Override
    public Map<String, String> importMapping() {
        return importMapping;
    }

    @Override
    public Map<String, String> schemaMapping() {
        return schemaMapping;
    }

    @Override
    public Map<String, String> inlineSchemaNameMapping() {
        return inlineSchemaNameMapping;
    }

    @Override
    public Map<String, String> inlineSchemaNameDefault() {
        return inlineSchemaNameDefault;
    }

    @Override
    public String testPackage() {
        return testPackage;
    }

    @Override
    public String modelPackage() {
        return modelPackage;
    }

    @Override
    public String apiPackage() {
        return apiPackage;
    }

    @Override
    public String fileSuffix() {
        return fileSuffix;
    }

    @Override
    public String templateDir() {
        return templateDir;
    }

    @Override
    public String embeddedTemplateDir() {
        if (embeddedTemplateDir != null) {
            return embeddedTemplateDir;
        } else {
            return templateDir;
        }
    }

    @Override
    public Map<String, String> apiDocTemplateFiles() {
        return apiDocTemplateFiles;
    }

    @Override
    public Map<String, String> modelDocTemplateFiles() {
        return modelDocTemplateFiles;
    }

    @Override
    public Map<String, String> reservedWordsMappings() {
        return reservedWordsMappings;
    }

    @Override
    public Map<String, String> apiTestTemplateFiles() {
        return apiTestTemplateFiles;
    }

    @Override
    public Map<String, String> modelTestTemplateFiles() {
        return modelTestTemplateFiles;
    }

    @Override
    public Map<String, String> apiTemplateFiles() {
        return apiTemplateFiles;
    }

    @Override
    public Map<String, String> apiXToApiTemplateFiles() { return apiXToApiTemplateFiles; }

    @Override
    public Map<String, String> modelTemplateFiles() {
        return modelTemplateFiles;
    }

    @Override
    public Map<String, String> requestBodyTemplateFiles() { return requestBodyTemplateFiles; }

    @Override
    public Map<String, String> requestBodyDocTemplateFiles() { return requestBodyDocTemplateFiles; }

    @Override
    public Map<String, String> headerTemplateFiles() { return headerTemplateFiles; }

    @Override
    public Map<String, String> headerDocTemplateFiles() { return headerDocTemplateFiles; }

    @Override
    public Map<String, String> responseTemplateFiles() { return responseTemplateFiles; }

    @Override
    public Map<String, String> responseDocTemplateFiles() { return responseDocTemplateFiles; }

    @Override
    public Map<String, String> parameterTemplateFiles() { return parameterTemplateFiles; }

    @Override
    public Map<String, String> parameterDocTemplateFiles() { return parameterDocTemplateFiles; }

    @Override
    public Map<String, String> pathEndpointTemplateFiles() { return pathEndpointTemplateFiles; }

    @Override
    public Set<String> pathEndpointDocTemplateFiles() { return pathEndpointDocTemplateFiles; }

    @Override
    public Set<String> pathEndpointTestTemplateFiles() { return pathEndpointTestTemplateFiles; }

    @Override
    public Map<String, String> pathEndpointRequestBodyTemplateFiles() { return pathEndpointRequestBodyTemplateFiles; }

    @Override
    public Set<String> pathEndpointParameterTemplateFiles() { return pathEndpointParameterTemplateFiles; }

    @Override
    public Map<String, String> pathEndpointResponseTemplateFiles() { return pathEndpointResponseTemplateFiles; }

    @Override
    public Set<String> pathEndpointResponseHeaderTemplateFiles() { return pathEndpointResponseHeaderTemplateFiles; }

    public String toRequestBodyFilename(String componentName) {
        return toModuleFilename(componentName);
    }

    public String toResponseModuleName(String componentName) { return toModuleFilename(componentName); }

    public String toHeaderFilename(String componentName) { return toModuleFilename(componentName); }

    public String toRequestBodyDocFilename(String componentName) { return toModuleFilename(componentName); }

    public String toResponseDocFilename(String componentName) { return toModuleFilename(componentName); }

    public String toHeaderDocFilename(String componentName) { return toModuleFilename(componentName); }

    @Override
    public String apiFileFolder() {
        return outputFolder + File.separator + apiPackage().replace('.', File.separatorChar);
    }

    @Override
    public String modelFileFolder() {
        return outputFolder + File.separator + modelPackage().replace('.', File.separatorChar);
    }

    @Override
    public String apiTestFileFolder() {
        return outputFolder + File.separator + testPackage().replace('.', File.separatorChar);
    }

    @Override
    public String modelTestFileFolder() {
        return outputFolder + File.separator + testPackage().replace('.', File.separatorChar);
    }

    @Override
    public String apiDocFileFolder() {
        return outputFolder;
    }

    @Override
    public String modelDocFileFolder() {
        return outputFolder;
    }

    @Override
    public String requestBodyDocFileFolder() { return outputFolder; }

    @Override
    public String responseDocFileFolder() { return outputFolder; }

    @Override
    public String headerFileFolder() { return outputFolder; }

    @Override
    public String headerDocFileFolder() { return outputFolder; }

    @Override
    public String parameterFileFolder() { return outputFolder; }

    @Override
    public String parameterDocFileFolder() { return outputFolder; }

    @Override
    public Map<String, Object> additionalProperties() {
        return additionalProperties;
    }

    @Override
    public Map<String, String> serverVariableOverrides() {
        return serverVariables;
    }

    @Override
    public Map<String, Object> vendorExtensions() {
        return vendorExtensions;
    }

    @Override
    public List<SupportingFile> supportingFiles() {
        return supportingFiles;
    }

    @Override
    public String outputFolder() {
        return outputFolder;
    }

    @Override
    public void setOutputDir(String dir) {
        this.outputFolder = dir;
    }

    @Override
    public String getOutputDir() {
        return outputFolder();
    }

    @Override
    public String getInputSpec() {
        return inputSpec;
    }

    @Override
    public void setInputSpec(String inputSpec) {
        this.inputSpec = inputSpec;
    }

    @Override
    public String getFilesMetadataFilename() {
        return filesMetadataFilename;
    }

    public void setFilesMetadataFilename(String filesMetadataFilename) {
        this.filesMetadataFilename = filesMetadataFilename;
    }

    @Override
    public String getVersionMetadataFilename() {
        return versionMetadataFilename;
    }

    public void setVersionMetadataFilename(String versionMetadataFilename) {
        this.versionMetadataFilename = versionMetadataFilename;
    }

    public void setTemplateDir(String templateDir) {
        this.templateDir = templateDir;
    }

    public void setModelPackage(String modelPackage) {
        this.modelPackage = modelPackage;
    }

    public String getModelNamePrefix() {
        return modelNamePrefix;
    }

    public void setModelNamePrefix(String modelNamePrefix) {
        this.modelNamePrefix = modelNamePrefix;
    }

    public String getModelNameSuffix() {
        return modelNameSuffix;
    }

    public void setModelNameSuffix(String modelNameSuffix) {
        this.modelNameSuffix = modelNameSuffix;
    }

    public String getApiNameSuffix() {
        return apiNameSuffix;
    }

    public void setApiNameSuffix(String apiNameSuffix) {
        this.apiNameSuffix = apiNameSuffix;
    }

    public String getApiNamePrefix() {
        return apiNamePrefix;
    }

    public void setApiNamePrefix(String apiNamePrefix) {
        this.apiNamePrefix = apiNamePrefix;
    }

    public void setApiPackage(String apiPackage) {
        this.apiPackage = apiPackage;
    }

    public Boolean getSortParamsByRequiredFlag() {
        return sortParamsByRequiredFlag;
    }

    public void setSortParamsByRequiredFlag(Boolean sortParamsByRequiredFlag) {
        this.sortParamsByRequiredFlag = sortParamsByRequiredFlag;
    }

    public Boolean getSortModelPropertiesByRequiredFlag() {
        return sortModelPropertiesByRequiredFlag;
    }

    public void setSortModelPropertiesByRequiredFlag(Boolean sortModelPropertiesByRequiredFlag) {
        this.sortModelPropertiesByRequiredFlag = sortModelPropertiesByRequiredFlag;
    }
    public Boolean getEnsureUniqueParams() {
        return ensureUniqueParams;
    }

    public void setEnsureUniqueParams(Boolean ensureUniqueParams) {
        this.ensureUniqueParams = ensureUniqueParams;
    }

    public Boolean getLegacyDiscriminatorBehavior() {
        return legacyDiscriminatorBehavior;
    }

    public void setLegacyDiscriminatorBehavior(boolean val) {
        this.legacyDiscriminatorBehavior = val;
    }

    public Boolean getDisallowAdditionalPropertiesIfNotPresent() {
        return disallowAdditionalPropertiesIfNotPresent;
    }

    public void setDisallowAdditionalPropertiesIfNotPresent(boolean val) {
        this.disallowAdditionalPropertiesIfNotPresent = val;
    }

    public Boolean getEnumUnknownDefaultCase() {
        return enumUnknownDefaultCase;
    }

    public void setEnumUnknownDefaultCase(boolean val) {
        this.enumUnknownDefaultCase = val;
    }

    public Boolean getAllowUnicodeIdentifiers() {
        return allowUnicodeIdentifiers;
    }

    public void setAllowUnicodeIdentifiers(Boolean allowUnicodeIdentifiers) {
        this.allowUnicodeIdentifiers = allowUnicodeIdentifiers;
    }

    public Boolean getUseOneOfInterfaces() {
        return useOneOfInterfaces;
    }

    public void setUseOneOfInterfaces(Boolean useOneOfInterfaces) {
        this.useOneOfInterfaces = useOneOfInterfaces;
    }

    /**
     * Return the regular expression/JSON schema pattern (http://json-schema.org/latest/json-schema-validation.html#anchor33)
     *
     * @param pattern the pattern (regular expression)
     * @return properly-escaped pattern
     */
    public String toRegularExpression(String pattern) {
        return addRegularExpressionDelimiter(escapeText(pattern));
    }

    /**
     * Return the file name of the Api Test
     *
     * @param name the file name of the Api
     * @return the file name of the Api
     */
    @Override
    public String toApiFilename(String name) {
        return toApiName(name);
    }

    /**
     * Return the file name of the Api Documentation
     *
     * @param name the file name of the Api
     * @return the file name of the Api
     */
    @Override
    public String toApiDocFilename(String name) {
        return toApiName(name);
    }

    /**
     * Return the file name of the Api Test
     *
     * @param name the file name of the Api
     * @return the file name of the Api
     */
    @Override
    public String toApiTestFilename(String name) {
        return toApiName(name) + "Test";
    }

    /**
     * Return the variable name in the Api
     *
     * @param name the variable name of the Api
     * @return the snake-cased variable name
     */
    @Override
    public String toApiVarName(String name) {
        return lowerCamelCase(name);
    }

    /**
     * Return the capitalized file name of the model
     *
     * @param name the model name
     * @return the file name of the model
     */
    @Override
    public String toModelFilename(String name) {
        return toModuleFilename(name);
    }

    @Override
    public String toModuleFilename(String name) {
        return camelize(name);
    }

    public String toPathFilename(String name) {
        return toModuleFilename(name);
    }

    @Override
    public String toParameterFilename(String basename) {
        return toModuleFilename(basename);
    }

    @Override
    public String toParameterDocFilename(String componentName) { return toModuleFilename(componentName); }

    /**
     * Return the capitalized file name of the model test
     *
     * @param name the model name
     * @return the file name of the model
     */
    @Override
    public String toModelTestFilename(String name) {
        return camelize(name) + "Test";
    }

    /**
     * Return the capitalized file name of the model documentation
     *
     * @param name the model name
     * @return the file name of the model
     */
    @Override
    public String toModelDocFilename(String name) {
        return camelize(name);
    }

    /**
     * Returns metadata about the generator.
     *
     * @return A provided {@link GeneratorMetadata} instance
     */
    @Override
    public GeneratorMetadata getGeneratorMetadata() {
        return generatorMetadata;
    }

    /**
     * Return the operation ID (method name)
     *
     * @param operationId operation ID
     * @return the sanitized method name
     */
    @SuppressWarnings("static-method")
    public String toOperationId(String operationId) {
        // throw exception if method name is empty
        if (StringUtils.isEmpty(operationId)) {
            throw new RuntimeException("Empty method name (operationId) not allowed");
        }

        return operationId;
    }

    /**
     * Return the variable name by removing invalid characters and proper escaping if
     * it's a reserved word.
     *
     * @param name the variable name
     * @return the sanitized variable name
     */
    public String toVarName(final String name) {
        if (reservedWords.contains(name)) {
            return escapeReservedWord(name);
        } else if (name.chars().anyMatch(character -> specialCharReplacements.containsKey(String.valueOf((char) character)))) {
            return escape(name, specialCharReplacements, null, null);
        }
        return name;
    }

    /**
     * Return the parameter name by removing invalid characters and proper escaping if
     * it's a reserved word.
     *
     * @param name Codegen property object
     * @return the sanitized parameter name
     */
    @Override
    public String toParamName(String name) {
        name = removeNonNameElementToCamelCase(name); // FIXME: a parameter should not be assigned. Also declare the methods parameters as 'final'.
        if (reservedWords.contains(name)) {
            return escapeReservedWord(name);
        } else if (name.chars().anyMatch(character -> specialCharReplacements.containsKey(String.valueOf((char) character)))) {
            return escape(name, specialCharReplacements, null, null);
        }
        return name;

    }

    /**
     * Return the parameter name of array of model
     *
     * @param name name of the array model
     * @return the sanitized parameter name
     */
    public String toArrayModelParamName(String name) {
        return toParamName(name);
    }

    /**
     * Return the Enum name (e.g. StatusEnum given 'status')
     *
     * @param property Codegen property
     * @return the Enum name
     */
    @SuppressWarnings("static-method")
    public String toEnumName(CodegenSchema property) {
        return StringUtils.capitalize(property.name.getName()) + "Enum";
    }

    /**
     * Return the escaped name of the reserved word
     *
     * @param name the name to be escaped
     * @return the escaped reserved word
     * <p>
     * throws Runtime exception as reserved word is not allowed (default behavior)
     */
    @Override
    @SuppressWarnings("static-method")
    public String escapeReservedWord(String name) {
        throw new RuntimeException("reserved word " + name + " not allowed");
    }

    /**
     * Return the fully-qualified "Model" name for import
     *
     * @param refClass the name of the "Model"
     * @return the fully-qualified "Model" name for import
     */
    @Override
    public String toModelImport(String refClass) {
        if ("".equals(modelPackage())) {
            return refClass;
        } else {
            return modelPackage() + "." + refClass;
        }
    }

    /**
     * Returns the same content as [[toModelImport]] with key the fully-qualified Model name and value the initial input.
     * In case of union types this method has a key for each separate model and import.
     *
     * @param name the name of the "Model"
     * @return Map of fully-qualified models.
     */
    @Override
    public Map<String, String> toModelImportMap(String name) {
        return Collections.singletonMap(this.toModelImport(name), name);
    }

    /**
     * Return the fully-qualified "Api" name for import
     *
     * @param name the name of the "Api"
     * @return the fully-qualified "Api" name for import
     */
    @Override
    public String toApiImport(String name) {
        return apiPackage() + "." + name;
    }

    /**
     * Default constructor.
     * This method will map between OAS type and language-specified type, as well as mapping
     * between OAS type and the corresponding import statement for the language. This will
     * also add some language specified CLI options, if any.
     * returns string presentation of the example path (it's a constructor)
     */
    public DefaultCodegen() {
        CodegenType codegenType = getTag();
        if (codegenType == null) {
            codegenType = CodegenType.OTHER;
        }

        generatorMetadata = GeneratorMetadata.newBuilder()
                .stability(Stability.STABLE)
                .featureSet(DefaultFeatureSet)
                .generationMessage(String.format(Locale.ROOT, "OpenAPI Generator: %s (%s)", getName(), codegenType.toValue()))
                .build();

        defaultIncludes = new HashSet<>(
                Arrays.asList("double",
                        "int",
                        "long",
                        "short",
                        "char",
                        "float",
                        "String",
                        "boolean",
                        "Boolean",
                        "Double",
                        "Void",
                        "Integer",
                        "Long",
                        "Float")
        );

        typeMapping = new HashMap<>();
        typeMapping.put("array", "List");
        typeMapping.put("set", "Set");
        typeMapping.put("map", "Map");
        typeMapping.put("boolean", "Boolean");
        typeMapping.put("string", "String");
        typeMapping.put("int", "Integer");
        typeMapping.put("float", "Float");
        typeMapping.put("double", "Double");
        typeMapping.put("number", "BigDecimal");
        typeMapping.put("decimal", "BigDecimal");
        typeMapping.put("DateTime", "Date");
        typeMapping.put("long", "Long");
        typeMapping.put("short", "Short");
        typeMapping.put("char", "String");
        typeMapping.put("object", "Object");
        typeMapping.put("integer", "Integer");
        // FIXME: java specific type should be in Java Based Abstract Impl's
        typeMapping.put("ByteArray", "byte[]");
        typeMapping.put("binary", "File");
        typeMapping.put("file", "File");
        typeMapping.put("UUID", "UUID");
        typeMapping.put("URI", "URI");
        typeMapping.put("AnyType", "oas_any_type_not_mapped");

        instantiationTypes = new HashMap<>();

        reservedWords = new HashSet<>();

        cliOptions.add(CliOption.newBoolean(CodegenConstants.SORT_PARAMS_BY_REQUIRED_FLAG,
                CodegenConstants.SORT_PARAMS_BY_REQUIRED_FLAG_DESC).defaultValue(Boolean.TRUE.toString()));
        cliOptions.add(CliOption.newBoolean(CodegenConstants.SORT_MODEL_PROPERTIES_BY_REQUIRED_FLAG,
                CodegenConstants.SORT_MODEL_PROPERTIES_BY_REQUIRED_FLAG_DESC).defaultValue(Boolean.TRUE.toString()));
        cliOptions.add(CliOption.newBoolean(CodegenConstants.ENSURE_UNIQUE_PARAMS, CodegenConstants
                .ENSURE_UNIQUE_PARAMS_DESC).defaultValue(Boolean.TRUE.toString()));
        // name formatting options
        cliOptions.add(CliOption.newBoolean(CodegenConstants.ALLOW_UNICODE_IDENTIFIERS, CodegenConstants
                .ALLOW_UNICODE_IDENTIFIERS_DESC).defaultValue(Boolean.FALSE.toString()));
        // option to change the order of form/body parameter
        cliOptions.add(CliOption.newBoolean(CodegenConstants.PREPEND_FORM_OR_BODY_PARAMETERS,
                CodegenConstants.PREPEND_FORM_OR_BODY_PARAMETERS_DESC).defaultValue(Boolean.FALSE.toString()));

        // option to change how we process + set the data in the discriminator mapping
        CliOption legacyDiscriminatorBehaviorOpt = CliOption.newBoolean(CodegenConstants.LEGACY_DISCRIMINATOR_BEHAVIOR, CodegenConstants.LEGACY_DISCRIMINATOR_BEHAVIOR_DESC).defaultValue(Boolean.TRUE.toString());
        Map<String, String> legacyDiscriminatorBehaviorOpts = new HashMap<>();
        legacyDiscriminatorBehaviorOpts.put("true", "The mapping in the discriminator includes descendent schemas that allOf inherit from self and the discriminator mapping schemas in the OAS document.");
        legacyDiscriminatorBehaviorOpts.put("false", "The mapping in the discriminator includes any descendent schemas that allOf inherit from self, any oneOf schemas, any anyOf schemas, any x-discriminator-values, and the discriminator mapping schemas in the OAS document AND Codegen validates that oneOf and anyOf schemas contain the required discriminator and throws an error if the discriminator is missing.");
        legacyDiscriminatorBehaviorOpt.setEnum(legacyDiscriminatorBehaviorOpts);
        cliOptions.add(legacyDiscriminatorBehaviorOpt);

        // option to change how we process + set the data in the 'additionalProperties' keyword.
        CliOption disallowAdditionalPropertiesIfNotPresentOpt = CliOption.newBoolean(
                CodegenConstants.DISALLOW_ADDITIONAL_PROPERTIES_IF_NOT_PRESENT,
                CodegenConstants.DISALLOW_ADDITIONAL_PROPERTIES_IF_NOT_PRESENT_DESC).defaultValue(Boolean.TRUE.toString());
        Map<String, String> disallowAdditionalPropertiesIfNotPresentOpts = new HashMap<>();
        disallowAdditionalPropertiesIfNotPresentOpts.put("false",
                "The 'additionalProperties' implementation is compliant with the OAS and JSON schema specifications.");
        disallowAdditionalPropertiesIfNotPresentOpts.put("true",
                "Keep the old (incorrect) behaviour that 'additionalProperties' is set to false by default.");
        disallowAdditionalPropertiesIfNotPresentOpt.setEnum(disallowAdditionalPropertiesIfNotPresentOpts);
        cliOptions.add(disallowAdditionalPropertiesIfNotPresentOpt);
        this.setDisallowAdditionalPropertiesIfNotPresent(true);

        CliOption enumUnknownDefaultCaseOpt = CliOption.newBoolean(
                CodegenConstants.ENUM_UNKNOWN_DEFAULT_CASE,
                CodegenConstants.ENUM_UNKNOWN_DEFAULT_CASE_DESC).defaultValue(Boolean.FALSE.toString());
        Map<String, String> enumUnknownDefaultCaseOpts = new HashMap<>();
        enumUnknownDefaultCaseOpts.put("false",
                "No changes to the enum's are made, this is the default option.");
        enumUnknownDefaultCaseOpts.put("true",
                "With this option enabled, each enum will have a new case, 'unknown_default_open_api', so that when the enum case sent by the server is not known by the client/spec, can safely be decoded to this case.");
        enumUnknownDefaultCaseOpt.setEnum(enumUnknownDefaultCaseOpts);
        cliOptions.add(enumUnknownDefaultCaseOpt);
        this.setEnumUnknownDefaultCase(false);

        // initialize special character mapping
        initializeSpecialCharacterMapping();

        // Register common Mustache lambdas.
        registerMustacheLambdas();
    }

    /**
     * Initialize special character mapping
     */
    protected void initializeSpecialCharacterMapping() {
        // Initialize special characters
        specialCharReplacements.put("$", "Dollar");
        specialCharReplacements.put("^", "Caret");
        specialCharReplacements.put("|", "Pipe");
        specialCharReplacements.put("=", "Equal");
        specialCharReplacements.put("*", "Star");
        specialCharReplacements.put("-", "Minus");
        specialCharReplacements.put("&", "Ampersand");
        specialCharReplacements.put("%", "Percent");
        specialCharReplacements.put("#", "Hash");
        specialCharReplacements.put("@", "At");
        specialCharReplacements.put("!", "Exclamation");
        specialCharReplacements.put("+", "Plus");
        specialCharReplacements.put(":", "Colon");
        specialCharReplacements.put(";", "Semicolon");
        specialCharReplacements.put(">", "Greater_Than");
        specialCharReplacements.put("<", "Less_Than");
        specialCharReplacements.put(".", "Period");
        specialCharReplacements.put("_", "Underscore");
        specialCharReplacements.put("?", "Question_Mark");
        specialCharReplacements.put(",", "Comma");
        specialCharReplacements.put("'", "Quote");
        specialCharReplacements.put("\"", "Double_Quote");
        specialCharReplacements.put("/", "Slash");
        specialCharReplacements.put("\\", "Back_Slash");
        specialCharReplacements.put("(", "Left_Parenthesis");
        specialCharReplacements.put(")", "Right_Parenthesis");
        specialCharReplacements.put("{", "Left_Curly_Bracket");
        specialCharReplacements.put("}", "Right_Curly_Bracket");
        specialCharReplacements.put("[", "Left_Square_Bracket");
        specialCharReplacements.put("]", "Right_Square_Bracket");
        specialCharReplacements.put("~", "Tilde");
        specialCharReplacements.put("`", "Backtick");

        specialCharReplacements.put("<=", "Less_Than_Or_Equal_To");
        specialCharReplacements.put(">=", "Greater_Than_Or_Equal_To");
        specialCharReplacements.put("!=", "Not_Equal");
        specialCharReplacements.put("<>", "Not_Equal");
        specialCharReplacements.put("~=", "Tilde_Equal");
    }

    /**
     * Return the symbol name of a symbol
     *
     * @param input Symbol (e.g. $)
     * @return Symbol name (e.g. Dollar)
     */
    protected String getSymbolName(String input) {
        return specialCharReplacements.get(input);
    }

    /**
     * Return the example path
     *
     * @param path      the path of the operation
     * @param operation OAS operation object
     * @return string presentation of the example path
     */
    @Override
    @SuppressWarnings("static-method")
    public String generateExamplePath(String path, Operation operation) {
        StringBuilder sb = new StringBuilder();
        sb.append(path);

        if (operation.getParameters() != null) {
            int count = 0;

            for (Parameter param : operation.getParameters()) {
                if (param instanceof QueryParameter) {
                    StringBuilder paramPart = new StringBuilder();
                    QueryParameter qp = (QueryParameter) param;

                    if (count == 0) {
                        paramPart.append("?");
                    } else {
                        paramPart.append(",");
                    }
                    count += 1;
                    if (!param.getRequired()) {
                        paramPart.append("[");
                    }
                    paramPart.append(param.getName()).append("=");
                    paramPart.append("{");

                    // TODO support for multi, tsv?
                    if (qp.getStyle() != null) {
                        paramPart.append(param.getName()).append("1");
                        if (Parameter.StyleEnum.FORM.equals(qp.getStyle())) {
                            if (qp.getExplode() != null && qp.getExplode()) {
                                paramPart.append(",");
                            } else {
                                paramPart.append("&").append(param.getName()).append("=");
                                paramPart.append(param.getName()).append("2");
                            }
                        } else if (Parameter.StyleEnum.PIPEDELIMITED.equals(qp.getStyle())) {
                            paramPart.append("|");
                        } else if (Parameter.StyleEnum.SPACEDELIMITED.equals(qp.getStyle())) {
                            paramPart.append("%20");
                        } else {
                            LOGGER.warn("query parameter '{}' style not support: {}", param.getName(), qp.getStyle());
                        }
                    } else {
                        paramPart.append(param.getName());
                    }

                    paramPart.append("}");
                    if (!param.getRequired()) {
                        paramPart.append("]");
                    }
                    sb.append(paramPart);
                }
            }
        }

        return sb.toString();
    }

    /**
     * Return the instantiation type of the property, especially for map and array
     *
     * @param schema property schema
     * @return string presentation of the instantiation type of the property
     */
    public String toInstantiationType(Schema schema) {
        if (ModelUtils.isMapSchema(schema)) {
            Schema additionalProperties = getAdditionalProperties(schema);
            String inner = getSchemaType(additionalProperties);
            return instantiationTypes.get("map") + "<String, " + inner + ">";
        } else if (ModelUtils.isArraySchema(schema)) {
            ArraySchema arraySchema = (ArraySchema) schema;
            String inner = getSchemaType(getSchemaItems(arraySchema));
            String parentType;
            if (ModelUtils.isSet(schema)) {
                parentType = "set";
            } else {
                parentType = "array";
            }
            return instantiationTypes.get(parentType) + "<" + inner + ">";
        } else {
            return null;
        }
    }

    /**
     * Return the example value of the parameter.
     *
     * @param codegenParameter Codegen parameter
     */
    public void setParameterExampleValue(CodegenParameter codegenParameter) {

        // set the example value
        // if not specified in x-example, generate a default value
        // TODO need to revise how to obtain the example value
        if (codegenParameter.vendorExtensions != null && codegenParameter.vendorExtensions.containsKey("x-example")) {
            codegenParameter.example = Json.pretty(codegenParameter.vendorExtensions.get("x-example"));
        }
    }

    /**
     * Return the example value of the parameter.
     *
     * @param codegenParameter Codegen parameter
     * @param parameter        Parameter
     */
    public void setParameterExampleValue(CodegenParameter codegenParameter, Parameter parameter) {
        if (parameter.getExample() != null) {
            codegenParameter.example = parameter.getExample().toString();
            return;
        }

        if (parameter.getExamples() != null && !parameter.getExamples().isEmpty()) {
            Example example = parameter.getExamples().values().iterator().next();
            if (example.getValue() != null) {
                codegenParameter.example = example.getValue().toString();
                return;
            }
        }

        Schema schema = parameter.getSchema();
        if (schema != null && schema.getExample() != null) {
            codegenParameter.example = schema.getExample().toString();
            return;
        }

        setParameterExampleValue(codegenParameter);
    }

    /**
     * Return the example value of the parameter.
     *
     * @param codegenParameter Codegen parameter
     * @param requestBody      Request body
     */
    public void setParameterExampleValue(CodegenParameter codegenParameter, RequestBody requestBody) {
        Content content = requestBody.getContent();

        if (content.size() > 1) {
            // @see ModelUtils.getSchemaFromContent()
            once(LOGGER).warn("Multiple MediaTypes found, using only the first one");
        }

        MediaType mediaType = content.values().iterator().next();
        if (mediaType.getExample() != null) {
            codegenParameter.example = mediaType.getExample().toString();
            return;
        }

        if (mediaType.getExamples() != null && !mediaType.getExamples().isEmpty()) {
            Example example = mediaType.getExamples().values().iterator().next();
            if (example.getValue() != null) {
                codegenParameter.example = example.getValue().toString();
                return;
            }
        }

        setParameterExampleValue(codegenParameter);
    }

    protected CodegenSchema getParameterSchema(CodegenParameter param) {
        CodegenSchema p = param.getSchema();
        if (p == null) {
            String firstContentType = (String) param.getContent().keySet().toArray()[0];
            p = param.getContent().get(firstContentType).getSchema();
        }
        return p;
    }

    /**
     * Return the example value of the property
     *
     * @param schema Property schema
     * @return string presentation of the example value of the property
     */
    public String toExampleValue(Schema schema) {
        if (schema.getExample() != null) {
            return schema.getExample().toString();
        }

        return getPropertyDefaultValue(schema);
    }

    /**
     * Return the default value of the property
     * <p>
     * Return null if you do NOT want a default value.
     * Any non-null value will cause {{#defaultValue} check to pass.
     *
     * @param schema Property schema
     * @return string presentation of the default value of the property
     */
    @SuppressWarnings("static-method")
    public String toDefaultValue(Schema schema) {
        if (schema.getDefault() != null) {
            return schema.getDefault().toString();
        }

        return getPropertyDefaultValue(schema);
    }

    /**
     * Return property value depending on property type.
     *
     * @param schema property type
     * @return property value
     */
    @SuppressWarnings("squid:S3923")
    private String getPropertyDefaultValue(Schema schema) {
        /*
         * Although all branches return null, this is left intentionally as examples for new contributors
         */
        if (ModelUtils.isBooleanSchema(schema)) {
            return "null";
        } else if (ModelUtils.isDateSchema(schema)) {
            return "null";
        } else if (ModelUtils.isDateTimeSchema(schema)) {
            return "null";
        } else if (ModelUtils.isNumberSchema(schema)) {
            return "null";
        } else if (ModelUtils.isIntegerSchema(schema)) {
            return "null";
        } else if (ModelUtils.isStringSchema(schema)) {
            return "null";
        } else if (ModelUtils.isObjectSchema(schema)) {
            return "null";
        } else {
            return "null";
        }
    }

    /**
     * returns the OpenAPI type for the property. Use getAlias to handle $ref of primitive type
     *
     * @param schema property schema
     * @return string presentation of the type
     **/
    @SuppressWarnings("static-method")
    public String getSchemaType(Schema schema) {
        if (schema instanceof ComposedSchema) { // composed schema
            ComposedSchema cs = (ComposedSchema) schema;
            // Get the interfaces, i.e. the set of elements under 'allOf', 'anyOf' or 'oneOf'.
            List<Schema> schemas = ModelUtils.getInterfaces(cs);

            List<String> names = new ArrayList<>();
            // Build a list of the schema types under each interface.
            // For example, if a 'allOf' composed schema has $ref children,
            // add the type of each child to the list of names.
            for (Schema s : schemas) {
                names.add(getSingleSchemaType(s));
            }

            if (cs.getAllOf() != null) {
                return toAllOfName(names, cs);
            } else if (cs.getAnyOf() != null) { // anyOf
                return toAnyOfName(names, cs);
            } else if (cs.getOneOf() != null) { // oneOf
                return toOneOfName(names, cs);
            }
        }

        return getSingleSchemaType(schema);

    }

    protected Schema<?> getSchemaItems(ArraySchema schema) {
        Schema<?> items = schema.getItems();
        if (items == null) {
            LOGGER.error("Undefined array inner type for `{}`. Default to String.", schema.getName());
            items = new StringSchema().description("TODO default missing array inner type to string");
            schema.setItems(items);
        }
        return items;
    }

    /**
     * Return the name of the 'allOf' composed schema.
     *
     * @param names          List of names
     * @param composedSchema composed schema
     * @return name of the allOf schema
     */
    @SuppressWarnings("static-method")
    public String toAllOfName(List<String> names, ComposedSchema composedSchema) {
        Map<String, Object> exts = composedSchema.getExtensions();
        if (exts != null && exts.containsKey("x-all-of-name")) {
            return (String) exts.get("x-all-of-name");
        }
        if (names.size() == 0) {
            LOGGER.error("allOf has no member defined: {}. Default to ERROR_ALLOF_SCHEMA", composedSchema);
            return "ERROR_ALLOF_SCHEMA";
        } else if (names.size() == 1) {
            return names.get(0);
        } else {
            LOGGER.warn("allOf with multiple schemas defined. Using only the first one: {}", names.get(0));
            return names.get(0);
        }
    }

    /**
     * Return the name of the anyOf schema
     *
     * @param names          List of names
     * @param composedSchema composed schema
     * @return name of the anyOf schema
     */
    @SuppressWarnings("static-method")
    public String toAnyOfName(List<String> names, ComposedSchema composedSchema) {
        return "anyOf<" + String.join(",", names) + ">";
    }

    /**
     * Return the name of the oneOf schema.
     * <p>
     * This name is used to set the value of CodegenSchema.openApiType.
     * <p>
     * If the 'x-one-of-name' extension is specified in the OAS document, return that value.
     * Otherwise, a name is constructed by creating a comma-separated list of all the names
     * of the oneOf schemas.
     *
     * @param names          List of names
     * @param composedSchema composed schema
     * @return name of the oneOf schema
     */
    @SuppressWarnings("static-method")
    public String toOneOfName(List<String> names, ComposedSchema composedSchema) {
        Map<String, Object> exts = composedSchema.getExtensions();
        if (exts != null && exts.containsKey("x-one-of-name")) {
            return (String) exts.get("x-one-of-name");
        }
        return "oneOf<" + String.join(",", names) + ">";
    }

    @Override
    public Schema unaliasSchema(Schema schema) {
        return ModelUtils.unaliasSchema(this.openAPI, schema, schemaMapping);
    }

    /**
     * Return a string representation of the schema type, resolving aliasing and references if necessary.
     *
     * @param schema input
     * @return the string representation of the schema type.
     */
    protected String getSingleSchemaType(Schema schema) {
        Schema unaliasSchema = unaliasSchema(schema);

        if (StringUtils.isNotBlank(unaliasSchema.get$ref())) { // reference to another definition/schema
            // get the schema/model name from $ref
            String schemaName = ModelUtils.getSimpleRef(unaliasSchema.get$ref());
            if (StringUtils.isNotEmpty(schemaName)) {
                if (schemaMapping.containsKey(schemaName)) {
                    return schemaName;
                }
                return getAlias(schemaName);
            } else {
                LOGGER.warn("Error obtaining the datatype from ref: {}. Default to 'object'", unaliasSchema.get$ref());
                return "object";
            }
        } else { // primitive type or model
            return getAlias(getPrimitiveType(unaliasSchema));
        }
    }

    /**
     * Return the OAI type (e.g. integer, long, etc) corresponding to a schema.
     * <pre>$ref</pre> is not taken into account by this method.
     * <p>
     * If the schema is free-form (i.e. 'type: object' with no properties) or inline
     * schema, the returned OAI type is 'object'.
     *
     * @param schema
     */
    private String getPrimitiveType(Schema schema) {
        if (schema == null) {
            throw new RuntimeException("schema cannot be null in getPrimitiveType");
        } else if (typeMapping.containsKey(schema.getType() + "+" + schema.getFormat())) {
            // allows custom type_format mapping.
            // use {type}+{format}
            return typeMapping.get(schema.getType() + "+" + schema.getFormat());
        } else if (ModelUtils.isNullType(schema)) {
            // The 'null' type is allowed in OAS 3.1 and above. It is not supported by OAS 3.0.x,
            // though this tooling supports it.
            return "null";
        } else if (ModelUtils.isDecimalSchema(schema)) {
            // special handle of type: string, format: number
            return "decimal";
        } else if (ModelUtils.isByteArraySchema(schema)) {
            return "ByteArray";
        } else if (ModelUtils.isFileSchema(schema)) {
            return "file";
        } else if (ModelUtils.isBinarySchema(schema)) {
            return SchemaTypeUtil.BINARY_FORMAT;
        } else if (ModelUtils.isBooleanSchema(schema)) {
            return SchemaTypeUtil.BOOLEAN_TYPE;
        } else if (ModelUtils.isDateSchema(schema)) {
            return SchemaTypeUtil.DATE_FORMAT;
        } else if (ModelUtils.isDateTimeSchema(schema)) {
            return "DateTime";
        } else if (ModelUtils.isNumberSchema(schema)) {
            if (schema.getFormat() == null) { // no format defined
                return "number";
            } else if (ModelUtils.isFloatSchema(schema)) {
                return SchemaTypeUtil.FLOAT_FORMAT;
            } else if (ModelUtils.isDoubleSchema(schema)) {
                return SchemaTypeUtil.DOUBLE_FORMAT;
            } else {
                LOGGER.warn("Unknown `format` {} detected for type `number`. Defaulting to `number`", schema.getFormat());
                return "number";
            }
        } else if (ModelUtils.isIntegerSchema(schema)) {
            if (ModelUtils.isLongSchema(schema)) {
                return "long";
            } else {
                return schema.getType(); // integer
            }
        } else if (ModelUtils.isMapSchema(schema)) {
            return "map";
        } else if (ModelUtils.isArraySchema(schema)) {
            if (ModelUtils.isSet(schema)) {
                return "set";
            } else {
                return "array";
            }
        } else if (ModelUtils.isUUIDSchema(schema)) {
            return "UUID";
        } else if (ModelUtils.isURISchema(schema)) {
            return "URI";
        } else if (ModelUtils.isStringSchema(schema)) {
            if (typeMapping.containsKey(schema.getFormat())) {
                // If the format matches a typeMapping (supplied with the --typeMappings flag)
                // then treat the format as a primitive type.
                // This allows the typeMapping flag to add a new custom type which can then
                // be used in the format field.
                return schema.getFormat();
            }
            return "string";
        } else if (schema.getProperties() != null && !schema.getProperties().isEmpty()) { // having property implies it's a model
            return "object";
        } else if (ModelUtils.isAnyType(schema)) {
            return "AnyType";
        } else if (StringUtils.isNotEmpty(schema.getType())) {
            if (!schemaMapping.containsKey(schema.getType())) {
                LOGGER.warn("Unknown type found in the schema: {}. To map it, please use the schema mapping option (e.g. --schema-mappings in CLI)", schema.getType());
            }
            return schema.getType();
        }
        // The 'type' attribute has not been set in the OAS schema, which means the value
        // can be an arbitrary type, e.g. integer, string, object, array, number...
        // TODO: we should return a different value to distinguish between free-form object
        // and arbitrary type.
        return "object";
    }

    /**
     * Return the lowerCamelCase of the string
     *
     * @param name string to be lowerCamelCased
     * @return lowerCamelCase string
     */
    @SuppressWarnings("static-method")
    public String lowerCamelCase(String name) {
        return (name.length() > 0) ? (Character.toLowerCase(name.charAt(0)) + name.substring(1)) : "";
    }

    /**
     * Determine the type alias for the given type if it exists. This feature
     * was originally developed for Java because the language does not have an aliasing
     * mechanism of its own but later extends to handle other languages
     *
     * @param name The type name.
     * @return The alias of the given type, if it exists. If there is no alias
     * for this type, then returns the input type name.
     */
    public String getAlias(String name) {
        if (typeAliases != null && typeAliases.containsKey(name)) {
            return typeAliases.get(name);
        }
        return name;
    }

    /**
     * Output the API (class) name (capitalized) ending with the specified or default suffix
     * Return DefaultApi if name is empty
     *
     * @param name the name of the Api
     * @return capitalized Api name
     */
    @Override
    public String toApiName(String name) {
        if (name.length() == 0) {
            return "DefaultApi";
        }
        return camelize(apiNamePrefix + "_" + name + "_" + apiNameSuffix);
    }

    /**
     * Converts the OpenAPI schema name to a model name suitable for the current code generator.
     * May be overridden for each programming language.
     * In case the name belongs to the TypeSystem it won't be renamed.
     *
     * @param name the name of the model
     * @return capitalized model name
     */
    @Override
    public String toModelName(final String name) {
        if (schemaKeyToModelNameCache.containsKey(name)) {
            return schemaKeyToModelNameCache.get(name);
        }

        String camelizedName = camelize(modelNamePrefix + "_" + name + "_" + modelNameSuffix);
        schemaKeyToModelNameCache.put(name, camelizedName);
        return camelizedName;
    }

    private static class NamedSchema {
        private NamedSchema(Schema s, String sourceJsonPath, String currentJsonPath) {
            this.schema = s;
            this.sourceJsonPath = sourceJsonPath;
            this.currentJsonPath = currentJsonPath;
        }

        private Schema schema;
        private String sourceJsonPath;
        private String currentJsonPath;

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;
            NamedSchema that = (NamedSchema) o;
            return Objects.equals(schema, that.schema) &&
                    Objects.equals(sourceJsonPath, that.sourceJsonPath) &&
                    Objects.equals(currentJsonPath, that.currentJsonPath);
        }

        @Override
        public int hashCode() {
            return Objects.hash(schema, sourceJsonPath);
        }
    }

    Map<NamedSchema, CodegenSchema> schemaCodegenPropertyCache = new HashMap<>();

    protected void updateModelForComposedSchema(CodegenSchema m, Schema schema, String sourceJsonPath) {
        final ComposedSchema composed = (ComposedSchema) schema;

        // TODO revise the logic below to set discriminator
        if (composed.getAllOf() != null) {
            int modelImplCnt = 0; // only one inline object allowed in a ComposedModel
            int modelDiscriminators = 0; // only one discriminator allowed in a ComposedModel
            for (Schema innerSchema : composed.getAllOf()) { // TODO need to work with anyOf, oneOf as well
                if (m.discriminator == null && innerSchema.getDiscriminator() != null) {
                    LOGGER.debug("discriminator is set to null (not correctly set earlier): {}", m.name);
                    m.setDiscriminator(createDiscriminator(m.name.getName(), innerSchema, this.openAPI, sourceJsonPath));
                    modelDiscriminators++;
                }

                if (modelDiscriminators > 1) {
                    LOGGER.error("Allof composed schema is inheriting >1 discriminator. Only use one discriminator: {}", composed);
                }

                if (modelImplCnt++ > 1) {
                    LOGGER.warn("More than one inline schema specified in allOf:. Only the first one is recognized. All others are ignored.");
                    break; // only one schema with discriminator allowed in allOf
                }
            }
        }
    }

    protected String toTestCaseName(String specTestCaseName) {
        return specTestCaseName;
    }

    /**
     * A method that allows generators to pre-process test example payloads
     * This can be useful if one needs to change how values like null in string are represnted
     * @param data the test data payload
     * @return the updated test data payload
     */
    protected Object processTestExampleData(Object data) {
        return data;
    }

    /**
     * Processes any test cases if they exist in the components.x-test-examples vendor extensions
     * If they exist then cast them to java class instances and return them back in a map
     * @param refToTestCases the component schema name that the test cases are for
     */
    private HashMap<String, SchemaTestCase> extractSchemaTestCases(String refToTestCases) {
        // schemaName to a map of test case name to test case
        HashMap<String, Object> vendorExtensions = (HashMap<String, Object>) openAPI.getComponents().getExtensions();
        if (vendorExtensions ==  null || !vendorExtensions.containsKey(xSchemaTestExamplesKey)) {
            return null;
        }
        if (!refToTestCases.startsWith(xSchemaTestExamplesRefPrefix)) {
            return null;
        }
        String schemaName = refToTestCases.substring(xSchemaTestExamplesRefPrefix.length());
        HashMap<String, SchemaTestCase> schemaTestCases = new HashMap<>();
        LinkedHashMap<String, Object> schemaNameToTestCases = (LinkedHashMap<String, Object>) vendorExtensions.get(xSchemaTestExamplesKey);

        if (!schemaNameToTestCases.containsKey(schemaName)) {
            return null;
        }
        LinkedHashMap<String, LinkedHashMap<String, Object>> testNameToTesCase = (LinkedHashMap<String, LinkedHashMap<String, Object>>) schemaNameToTestCases.get(schemaName);
        for (Entry<String, LinkedHashMap<String, Object>> entry: testNameToTesCase.entrySet()) {
            LinkedHashMap<String, Object> testExample = (LinkedHashMap<String, Object>) entry.getValue();
            String nameInSnakeCase = toTestCaseName(entry.getKey());
            Object data = processTestExampleData(testExample.get("data"));
            SchemaTestCase testCase = new SchemaTestCase(
                    (String) testExample.getOrDefault("description", ""),
                    new ObjectWithTypeBooleans(data),
                    (boolean) testExample.get("valid")
            );
            schemaTestCases.put(nameInSnakeCase, testCase);
        }
        return schemaTestCases;
    }

    protected String toComponentModule(String componentName, String priorJsonPathSegment) {
        return packageName + "." + priorJsonPathSegment + "." + componentName;
    }

    protected void setAddProps(Schema schema, JsonSchema property, String sourceJsonPath, String currentJsonPath) {
        if (schema.getAdditionalProperties() == null) {
            return;
        }
        CodegenSchema addPropProp = null;
        String additonalPropertiesJsonPath = currentJsonPath + "/additionalProperties";
        if (schema.getAdditionalProperties() instanceof Boolean) {
            Schema usedSchema = getSchemaFromBooleanOrSchema(schema.getAdditionalProperties());
            addPropProp = fromSchema(usedSchema, sourceJsonPath, additonalPropertiesJsonPath);
        } else {
            addPropProp = fromSchema((Schema) schema.getAdditionalProperties(), sourceJsonPath, additonalPropertiesJsonPath);
        }
        if (ModelUtils.isComposedSchema(schema) && !supportsAdditionalPropertiesWithComposedSchema) {
            return;
        }
        if (addPropProp != null) {
            property.setAdditionalProperties(addPropProp);
        }
    }

    /**
     * Recursively look in Schema sc for the discriminator discPropName
     * and return a CodegenSchema with the dataType and required params set
     * the returned CodegenSchema may not be required and it may not be of type string
     *
     * @param composedSchemaName The name of the sc Schema
     * @param sc                 The Schema that may contain the discriminator
     * @param discPropName       The String that is the discriminator propertyName in the schema
     */
    private CodegenSchema discriminatorFound(String composedSchemaName, Schema sc, String discPropName, OpenAPI openAPI) {
        Schema refSchema = ModelUtils.getReferencedSchema(openAPI, sc);
        if (refSchema.getProperties() != null && refSchema.getProperties().get(discPropName) != null) {
            Schema discSchema = (Schema) refSchema.getProperties().get(discPropName);
            CodegenSchema cp = new CodegenSchema();
            if (ModelUtils.isStringSchema(discSchema)) {
                cp.isString = true;
            }
            return cp;
        }
        if (ModelUtils.isComposedSchema(refSchema)) {
            ComposedSchema composedSchema = (ComposedSchema) refSchema;
            if (composedSchema.getAllOf() != null) {
                // If our discriminator is in one of the allOf schemas break when we find it
                for (Schema allOf : composedSchema.getAllOf()) {
                    CodegenSchema cp = discriminatorFound(composedSchemaName, allOf, discPropName, openAPI);
                    if (cp != null) {
                        return cp;
                    }
                }
            }
            if (composedSchema.getOneOf() != null && composedSchema.getOneOf().size() != 0) {
                // All oneOf definitions must contain the discriminator
                CodegenSchema cp = new CodegenSchema();
                for (Schema oneOf : composedSchema.getOneOf()) {
                    String modelName = ModelUtils.getSimpleRef(oneOf.get$ref());
                    CodegenSchema thisCp = discriminatorFound(composedSchemaName, oneOf, discPropName, openAPI);
                    if (thisCp == null) {
                        LOGGER.warn(
                                "'{}' defines discriminator '{}', but the referenced OneOf schema '{}' is missing {}",
                                composedSchemaName, discPropName, modelName, discPropName);
                    }
                    if (cp != null && cp.refClass == null) {
                        cp = thisCp;
                        continue;
                    }
                    if (cp != thisCp) {
                        LOGGER.warn(
                                "'{}' defines discriminator '{}', but the OneOf schema '{}' has a different {} definition than the prior OneOf schema's. Make sure the {} type and required values are the same",
                                composedSchemaName, discPropName, modelName, discPropName, discPropName);
                    }
                }
                return cp;
            }
            if (composedSchema.getAnyOf() != null && composedSchema.getAnyOf().size() != 0) {
                // All anyOf definitions must contain the discriminator because a min of one must be selected
                CodegenSchema cp = new CodegenSchema();
                for (Schema anyOf : composedSchema.getAnyOf()) {
                    String modelName = ModelUtils.getSimpleRef(anyOf.get$ref());
                    CodegenSchema thisCp = discriminatorFound(composedSchemaName, anyOf, discPropName, openAPI);
                    if (thisCp == null) {
                        LOGGER.warn(
                                "'{}' defines discriminator '{}', but the referenced AnyOf schema '{}' is missing {}",
                                composedSchemaName, discPropName, modelName, discPropName);
                    }
                    if (cp != null && cp.refClass == null) {
                        cp = thisCp;
                        continue;
                    }
                    if (cp != thisCp) {
                        LOGGER.warn(
                                "'{}' defines discriminator '{}', but the AnyOf schema '{}' has a different {} definition than the prior AnyOf schema's. Make sure the {} type and required values are the same",
                                composedSchemaName, discPropName, modelName, discPropName, discPropName);
                    }
                }
                return cp;

            }
        }
        return null;
    }

    /**
     * Recursively look in Schema sc for the discriminator and return it
     * Schema sc location
     * OpenAPI openAPI the spec where we are searching for the discriminator
     *
     * @param sc The Schema that may contain the discriminator
     */
    private Discriminator recursiveGetDiscriminator(Schema sc, OpenAPI openAPI) {
        Schema refSchema = ModelUtils.getReferencedSchema(openAPI, sc);
        Discriminator foundDisc = refSchema.getDiscriminator();
        if (foundDisc != null) {
            return foundDisc;
        }

        if (this.getLegacyDiscriminatorBehavior()) {
            return null;
        }
        Discriminator disc = new Discriminator();
        if (ModelUtils.isComposedSchema(refSchema)) {
            ComposedSchema composedSchema = (ComposedSchema) refSchema;
            if (composedSchema.getAllOf() != null) {
                // If our discriminator is in one of the allOf schemas break when we find it
                for (Schema allOf : composedSchema.getAllOf()) {
                    foundDisc = recursiveGetDiscriminator(allOf, openAPI);
                    if (foundDisc != null) {
                        disc.setPropertyName(foundDisc.getPropertyName());
                        disc.setMapping(foundDisc.getMapping());
                        return disc;
                    }
                }
            }
            if (composedSchema.getOneOf() != null && composedSchema.getOneOf().size() != 0) {
                // All oneOf definitions must contain the discriminator
                Integer hasDiscriminatorCnt = 0;
                Integer hasNullTypeCnt = 0;
                Set<String> discriminatorsPropNames = new HashSet<>();
                for (Schema oneOf : composedSchema.getOneOf()) {
                    if (ModelUtils.isNullType(oneOf)) {
                        // The null type does not have a discriminator. Skip.
                        hasNullTypeCnt++;
                        continue;
                    }
                    foundDisc = recursiveGetDiscriminator(oneOf, openAPI);
                    if (foundDisc != null) {
                        discriminatorsPropNames.add(foundDisc.getPropertyName());
                        hasDiscriminatorCnt++;
                    }
                }
                if (discriminatorsPropNames.size() > 1) {
                    LOGGER.warn("The oneOf schemas have conflicting discriminator property names. " +
                            "oneOf schemas must have the same property name, but found " + String.join(", ", discriminatorsPropNames));
                }
                if (foundDisc != null && (hasDiscriminatorCnt + hasNullTypeCnt) == composedSchema.getOneOf().size() && discriminatorsPropNames.size() == 1) {
                    disc.setPropertyName(foundDisc.getPropertyName());
                    disc.setMapping(foundDisc.getMapping());
                    return disc;
                }
                // If the scenario when oneOf has two children and one of them is the 'null' type,
                // there is no need for a discriminator.
            }
            if (composedSchema.getAnyOf() != null && composedSchema.getAnyOf().size() != 0) {
                // All anyOf definitions must contain the discriminator because a min of one must be selected
                Integer hasDiscriminatorCnt = 0;
                Integer hasNullTypeCnt = 0;
                Set<String> discriminatorsPropNames = new HashSet<>();
                for (Schema anyOf : composedSchema.getAnyOf()) {
                    if (ModelUtils.isNullType(anyOf)) {
                        // The null type does not have a discriminator. Skip.
                        hasNullTypeCnt++;
                        continue;
                    }
                    foundDisc = recursiveGetDiscriminator(anyOf, openAPI);
                    if (foundDisc != null) {
                        discriminatorsPropNames.add(foundDisc.getPropertyName());
                        hasDiscriminatorCnt++;
                    }
                }
                if (discriminatorsPropNames.size() > 1) {
                    LOGGER.warn("The anyOf schemas have conflicting discriminator property names. " +
                            "anyOf schemas must have the same property name, but found " + String.join(", ", discriminatorsPropNames));
                }
                if (foundDisc != null && (hasDiscriminatorCnt + hasNullTypeCnt) == composedSchema.getAnyOf().size() && discriminatorsPropNames.size() == 1) {
                    disc.setPropertyName(foundDisc.getPropertyName());
                    disc.setMapping(foundDisc.getMapping());
                    return disc;
                }
                // If the scenario when anyOf has two children and one of them is the 'null' type,
                // there is no need for a discriminator.
            }
        }
        return null;
    }

    /**
     * This function is only used for composed schemas which have a discriminator
     * Process oneOf and anyOf models in a composed schema and adds them into
     * a list if the oneOf and anyOf models contain
     * the required discriminator. If they don't contain the required
     * discriminator or the discriminator is the wrong type then an error is
     * thrown
     *
     * @param composedSchemaName The String model name of the composed schema where we are setting the discriminator map
     * @param discPropName       The String that is the discriminator propertyName in the schema
     * @param c                  The ComposedSchema that contains the discriminator and oneOf/anyOf schemas
     * @param openAPI            The OpenAPI spec that we are using
     * @return the list of oneOf and anyOf MappedModel that need to be added to the discriminator map
     */
    protected List<MappedModel> getOneOfAnyOfDescendants(String composedSchemaName, String discPropName, ComposedSchema c, OpenAPI openAPI, String sourceJsonPath) {
        ArrayList<List<Schema>> listOLists = new ArrayList<>();
        listOLists.add(c.getOneOf());
        listOLists.add(c.getAnyOf());
        List<MappedModel> descendentSchemas = new ArrayList<>();
        for (List<Schema> schemaList : listOLists) {
            if (schemaList == null) {
                continue;
            }
            for (Schema sc : schemaList) {
                if (ModelUtils.isNullType(sc)) {
                    continue;
                }
                String ref = sc.get$ref();
                if (ref == null) {
                    // for schemas with no ref, it is not possible to build the discriminator map
                    // because ref is how we get the model name
                    // we only hit this use case for a schema with inline composed schemas, and one of those
                    // schemas also has inline composed schemas
                    // Note: if it is only inline one level, then the inline model resolver will move it into its own
                    // schema and make it a $ref schema in the oneOf/anyOf location
                    LOGGER.warn(
                            "Invalid inline schema defined in oneOf/anyOf in '{}'. Per the OpenApi spec, for this case when a composed schema defines a discriminator, the oneOf/anyOf schemas must use $ref. Change this inline definition to a $ref definition",
                            composedSchemaName);
                }
                CodegenSchema df = discriminatorFound(composedSchemaName, sc, discPropName, openAPI);
                String modelName = ModelUtils.getSimpleRef(ref);
                if (df == null || !df.isString) {
                    String msgSuffix = "";
                    if (df == null) {
                        msgSuffix += discPropName + " is missing from the schema, define it as required and type string";
                    } else {
                        if (!df.isString) {
                            msgSuffix += "invalid type for " + discPropName + ", set it to string";
                        }
                    }
                    LOGGER.warn("'{}' defines discriminator '{}', but the referenced schema '{}' is incorrect. {}",
                            composedSchemaName, discPropName, modelName, msgSuffix);
                }
                MappedModel mm = new MappedModel(modelName, getRefClassWithModule("#/components/schemas/" + modelName, sourceJsonPath));
                descendentSchemas.add(mm);
                Schema cs = ModelUtils.getSchema(openAPI, modelName);
                if (cs == null) { // cannot lookup the model based on the name
                    LOGGER.error("Failed to lookup the schema '{}' when processing oneOf/anyOf. Please check to ensure it's defined properly.", modelName);
                } else {
                    Map<String, Object> vendorExtensions = cs.getExtensions();
                    if (vendorExtensions != null && !vendorExtensions.isEmpty() && vendorExtensions.containsKey("x-discriminator-value")) {
                        String xDiscriminatorValue = (String) vendorExtensions.get("x-discriminator-value");
                        mm = new MappedModel(xDiscriminatorValue, getRefClassWithModule("#/components/schemas/" + modelName, sourceJsonPath));
                        descendentSchemas.add(mm);
                    }
                }
            }
        }
        return descendentSchemas;
    }

    protected List<MappedModel> getAllOfDescendants(String thisSchemaName, OpenAPI openAPI, String sourceJsonPath) {
        ArrayList<String> queue = new ArrayList();
        List<MappedModel> descendentSchemas = new ArrayList();
        Map<String, Schema> schemas = ModelUtils.getSchemas(openAPI);
        String currentSchemaName = thisSchemaName;
        Set<String> keys = schemas.keySet();

        int count = 0;
        // hack: avoid infinite loop on potential self-references in event our checks fail.
        while (100000 > count++) {
            for (String childName : keys) {
                if (childName.equals(thisSchemaName)) {
                    // skip the source schema
                    continue;
                }
                Schema child = schemas.get(childName);
                if (ModelUtils.isComposedSchema(child)) {
                    ComposedSchema composedChild = (ComposedSchema) child;
                    List<Schema> parents = composedChild.getAllOf();
                    if (parents != null) {
                        for (Schema parent : parents) {
                            String ref = parent.get$ref();
                            if (ref == null) {
                                // for schemas with no ref, it is not possible to build the discriminator map
                                // because ref is how we get the model name
                                // we hit this use case when an allOf composed schema contains an inline schema
                                continue;
                            }
                            String parentName = ModelUtils.getSimpleRef(ref);
                            if (parentName != null && parentName.equals(currentSchemaName)) {
                                if (queue.contains(childName) || descendentSchemas.stream().anyMatch(i -> childName.equals(i.getMappingName()))) {
                                    throw new RuntimeException("Stack overflow hit when looking for " + thisSchemaName + " an infinite loop starting and ending at " + childName + " was seen");
                                }
                                queue.add(childName);
                                break;
                            }
                        }
                    }
                }
            }
            if (queue.size() == 0) {
                break;
            }
            currentSchemaName = queue.remove(0);
            MappedModel mm = new MappedModel(currentSchemaName, getRefClassWithModule("#/components/schemas/" + currentSchemaName, sourceJsonPath));
            descendentSchemas.add(mm);
            Schema cs = schemas.get(currentSchemaName);
            Map<String, Object> vendorExtensions = cs.getExtensions();
            if (vendorExtensions != null && !vendorExtensions.isEmpty() && vendorExtensions.containsKey("x-discriminator-value")) {
                String xDiscriminatorValue = (String) vendorExtensions.get("x-discriminator-value");
                mm = new MappedModel(xDiscriminatorValue, getRefClassWithModule("#/components/schemas/" + currentSchemaName, sourceJsonPath));
                descendentSchemas.add(mm);
            }
        }
        return descendentSchemas;
    }

    protected String getRefClassWithModule(String ref, String sourceJsonPath) {
        String refClass = toRefClass(ref, sourceJsonPath);
        return refClass;
    }

    protected CodegenDiscriminator createDiscriminator(String schemaName, Schema schema, OpenAPI openAPI, String sourceJsonPath) {
        Discriminator sourceDiscriminator = recursiveGetDiscriminator(schema, openAPI);
        if (sourceDiscriminator == null) {
            return null;
        }
        CodegenDiscriminator discriminator = new CodegenDiscriminator();
        String discPropName = sourceDiscriminator.getPropertyName();
        discriminator.setPropertyName(toVarName(discPropName));
        discriminator.setPropertyBaseName(sourceDiscriminator.getPropertyName());

        // FIXME: for now, we assume that the discriminator property is String
        discriminator.setPropertyType(typeMapping.get("string"));

        // check to see if the discriminator property is an enum string
        if (schema.getProperties() != null &&
                schema.getProperties().get(discPropName) instanceof StringSchema) {
            StringSchema s = (StringSchema) schema.getProperties().get(discPropName);
            if (s.getEnum() != null && !s.getEnum().isEmpty()) { // it's an enum string
                discriminator.setIsEnum(true);
            }
        }

        discriminator.setMapping(sourceDiscriminator.getMapping());
        List<MappedModel> uniqueDescendants = new ArrayList<>();
        if (sourceDiscriminator.getMapping() != null && !sourceDiscriminator.getMapping().isEmpty()) {
            for (Entry<String, String> e : sourceDiscriminator.getMapping().entrySet()) {
                String name;
                String value = e.getValue();
                String modelName = null;
                if (value.indexOf('/') >= 0) {
                    name = ModelUtils.getSimpleRef(value);
                    if (ModelUtils.getSchema(openAPI, name) == null) {
                        LOGGER.error("Failed to lookup the schema '{}' when processing the discriminator mapping of oneOf/anyOf. Please check to ensure it's defined properly.", name);
                    } else {
                        modelName = getRefClassWithModule(e.getValue(), sourceJsonPath);
                    }
                } else {
                    String ref = "#/components/schemas/" + value;
                    modelName = getRefClassWithModule(ref, sourceJsonPath);
                }
                if (modelName != null) {
                    uniqueDescendants.add(new MappedModel(e.getKey(), modelName));
                }
            }
        }

        boolean legacyUseCase = (this.getLegacyDiscriminatorBehavior() && uniqueDescendants.isEmpty());
        if (!this.getLegacyDiscriminatorBehavior() || legacyUseCase) {
            // for schemas that allOf inherit from this schema, add those descendants to this discriminator map
            List<MappedModel> otherDescendants = getAllOfDescendants(schemaName, openAPI, sourceJsonPath);
            for (MappedModel otherDescendant : otherDescendants) {
                // add only if the mapping names are not the same
                boolean matched = false;
                for (MappedModel uniqueDescendant : uniqueDescendants) {
                    if (uniqueDescendant.getMappingName().equals(otherDescendant.getMappingName())) {
                        matched = true;
                        break;
                    }
                }

                if (matched == false) {
                    uniqueDescendants.add(otherDescendant);
                }
            }
        }
        // if there are composed oneOf/anyOf schemas, add them to this discriminator
        if (ModelUtils.isComposedSchema(schema) && !this.getLegacyDiscriminatorBehavior()) {
            List<MappedModel> otherDescendants = getOneOfAnyOfDescendants(schemaName, discPropName, (ComposedSchema) schema, openAPI, sourceJsonPath);
            for (MappedModel otherDescendant : otherDescendants) {
                if (!uniqueDescendants.contains(otherDescendant)) {
                    uniqueDescendants.add(otherDescendant);
                }
            }
        }
        if (!this.getLegacyDiscriminatorBehavior()) {
            Collections.sort(uniqueDescendants);
        }
        discriminator.getMappedModels().addAll(uniqueDescendants);

        return discriminator;
    }

    /**
     * Handle the model for the 'additionalProperties' keyword in the OAS schema.
     *
     * @param codegenModel The codegen representation of the schema.
     * @param schema       The input OAS schema.
     */
    protected void addAdditionPropertiesToCodeGenModel(CodegenSchema codegenModel, Schema schema) {}

    /**
     * Add schema's properties to "properties" and "required" list
     *
     * @param properties     all properties
     * @param required       required property only
     * @param schema         schema in which the properties will be added to the lists
     * @param visitedSchemas circuit-breaker - the schemas with which the method was called before for recursive structures
     */
    protected void addProperties(Map<String, Schema> properties, List<String> required, Schema schema, Set<Schema> visitedSchemas) {
        if (!visitedSchemas.add(schema)) {
            return;
        }
        if (schema instanceof ComposedSchema) {
            ComposedSchema composedSchema = (ComposedSchema) schema;

            if (composedSchema.getAllOf() != null) {
                for (Schema component : composedSchema.getAllOf()) {
                    addProperties(properties, required, component, visitedSchemas);
                }
            }

            if (schema.getRequired() != null) {
                required.addAll(schema.getRequired());
            }

            if (composedSchema.getOneOf() != null) {
                for (Schema component : composedSchema.getOneOf()) {
                    addProperties(properties, required, component, visitedSchemas);
                }
            }

            if (composedSchema.getAnyOf() != null) {
                for (Schema component : composedSchema.getAnyOf()) {
                    addProperties(properties, required, component, visitedSchemas);
                }
            }

            return;
        }

        if (StringUtils.isNotBlank(schema.get$ref())) {
            Schema interfaceSchema = ModelUtils.getReferencedSchema(this.openAPI, schema);
            addProperties(properties, required, interfaceSchema, visitedSchemas);
            return;
        }
        if (schema.getProperties() != null) {
            properties.putAll(schema.getProperties());
        }
        if (schema.getRequired() != null) {
            required.addAll(schema.getRequired());
        }
    }

    protected void updatePropertyForObject(CodegenSchema property, Schema p, String sourceJsonPath, String currentJsonPath) {
        addVarsRequiredVarsAdditionalProps(p, property, sourceJsonPath, currentJsonPath);
    }

    protected void updatePropertyForAnyType(CodegenSchema property, Schema p, String sourceJsonPath, String currentJsonPath) {
        // The 'null' value is allowed when the OAS schema is 'any type'.
        // See https://github.com/OAI/OpenAPI-Specification/issues/1389
        if (Boolean.FALSE.equals(p.getNullable())) {
            LOGGER.warn("Schema '{}' is any type, which includes the 'null' value. 'nullable' cannot be set to 'false'", p.getName());
        }
        addVarsRequiredVarsAdditionalProps(p, property, sourceJsonPath, currentJsonPath);
    }

    protected void updatePropertyForString(CodegenSchema property, Schema p) {
        if (ModelUtils.isByteArraySchema(p)) {
            property.setIsString(false);
            property.isByteArray = true;
        } else if (ModelUtils.isBinarySchema(p)) {
            property.isBinary = true;
            property.isFile = true; // file = binary in OAS3
        } else if (ModelUtils.isUUIDSchema(p)) {
            property.isUuid = true;
        } else if (ModelUtils.isURISchema(p)) {
            property.isUri = true;
        } else if (ModelUtils.isEmailSchema(p)) {
            property.isEmail = true;
        } else if (ModelUtils.isDateSchema(p)) { // date format
            property.setIsString(false); // for backward compatibility with 2.x
            property.isDate = true;
        } else if (ModelUtils.isDateTimeSchema(p)) { // date-time format
            property.setIsString(false); // for backward compatibility with 2.x
            property.isDateTime = true;
        } else if (ModelUtils.isDecimalSchema(p)) { // type: string, format: number
            property.isDecimal = true;
            property.setIsString(false);
        }
        property.pattern = toRegularExpression(p.getPattern());
    }

    protected void updatePropertyForNumber(CodegenSchema property, Schema p) {
        property.isNumeric = Boolean.TRUE;
        if (ModelUtils.isFloatSchema(p)) { // float
            property.isFloat = Boolean.TRUE;
        } else if (ModelUtils.isDoubleSchema(p)) { // double
            property.isDouble = Boolean.TRUE;
        }
    }

    protected void updatePropertyForInteger(CodegenSchema property, Schema p) {
        property.isNumeric = Boolean.TRUE;
        if (ModelUtils.isLongSchema(p)) { // int64/long format
            property.isLong = Boolean.TRUE;
        } else {
            property.isInteger = Boolean.TRUE; // older use case, int32 and unbounded int
            if (ModelUtils.isShortSchema(p)) { // int32
                property.setIsShort(Boolean.TRUE);
            }
        }
    }

    protected boolean isValid(String name) {
        return !isReservedWord(name);
    }

    protected String getImport(String className, CodegenSchema schema) {
        if (className == null) {
            return schema.getRefClass();
        }
        return className;
    }

    /**
     * Recursively collect all necessary imports to include so that the type may be resolved.
     *
     * @param featureSet the generator feature set, used to determine if composed schemas should be added
     * @return all of the imports
     */
    private Set<String> getImports(CodegenSchema schema, FeatureSet featureSet) {
        Set<String> imports = new HashSet<>();
        if (schema.getDiscriminator() != null && schema.getDiscriminator().getMappedModels() != null) {
            CodegenDiscriminator disc = schema.getDiscriminator();
            for (CodegenDiscriminator.MappedModel mm : disc.getMappedModels()) {
                if (!"".equals(mm.getModelName())) {
                    String complexType = mm.getModelName();
                    if (shouldAddImport(complexType)) {
                        imports.add(getImport(complexType, null));
                    }
                }
            }
        }
        if (schema.getAllOf() != null || schema.getAnyOf() != null || schema.getOneOf() != null || schema.getNot() != null) {
            List<CodegenSchema> allOfs = Collections.emptyList();
            List<CodegenSchema> oneOfs = Collections.emptyList();
            List<CodegenSchema> anyOfs = Collections.emptyList();
            List<CodegenSchema> nots = Collections.emptyList();
            if (schema.getAllOf() != null && featureSet.getSchemaSupportFeatures().contains(SchemaSupportFeature.allOf)) {
                allOfs = schema.getAllOf();
            }
            if (schema.getOneOf() != null && featureSet.getSchemaSupportFeatures().contains(SchemaSupportFeature.oneOf)) {
                oneOfs = schema.getOneOf();
            }
            if (schema.getAnyOf() != null && featureSet.getSchemaSupportFeatures().contains(SchemaSupportFeature.anyOf)) {
                anyOfs = schema.getAnyOf();
            }
            if (schema.getNot() != null && featureSet.getSchemaSupportFeatures().contains(SchemaSupportFeature.not)) {
                nots = Arrays.asList(schema.getNot());
            }
            Stream<CodegenSchema> allSchemas = Stream.of(
                    allOfs.stream(), anyOfs.stream(), oneOfs.stream(), nots.stream()).flatMap(i -> i);
            for (CodegenSchema cs: allSchemas.collect(Collectors.toList())) {
                imports.addAll(getImports(cs, featureSet));
            }
        }
        // items can exist for AnyType and type array
        if (schema.getItems() != null && schema.getIsArray()) {
            imports.addAll(getImports(schema.getItems(), featureSet));
        }
        // additionalProperties can exist for AnyType and type object
        if (schema.getAdditionalProperties() != null) {
            imports.addAll(getImports(schema.getAdditionalProperties(), featureSet));
        }
        // vars can exist for AnyType and type object
        if (schema.getProperties() != null && !schema.getProperties().isEmpty()) {
            for (CodegenSchema cs: schema.getProperties().values()) {
                imports.addAll(getImports(cs, featureSet));
            }
        }
        // referenced or inline schemas
        String refClass = schema.getRefClass();
        String refModule = schema.getRefModule();
        if (refClass != null && refModule != null) {
            // self reference classes do not contain refModule
            imports.add(getImport(null, schema));
        }
        return imports;
    }

    /**
     * Convert OAS Property object to Codegen Property object.
     * <p>
     * The return value is cached. An internal cache is looked up to determine
     * if the CodegenSchema return value has already been instantiated for
     * the (String name, Schema p) arguments.
     * Any subsequent processing of the CodegenSchema return value must be idempotent
     * for a given (String name, Schema schema).
     *
     * @param p        OAS property schema
     * @param sourceJsonPath the path when the schema started being created
     * @param currentJsonPath the current json path
     * @return Codegen Property object
     */
    public CodegenSchema fromSchema(Schema p, String sourceJsonPath, String currentJsonPath) {
        if (p == null) {
            LOGGER.error("Undefined property/schema at `{}`", currentJsonPath);
            return null;
        }
        LOGGER.debug("debugging fromSchema for {} {} : {}", sourceJsonPath, currentJsonPath, p);
        CodegenSchema property = new CodegenSchema();
        NamedSchema ns = new NamedSchema(p, sourceJsonPath, currentJsonPath);
        CodegenSchema cpc = schemaCodegenPropertyCache.get(ns);
        if (cpc != null) {
            LOGGER.debug("Cached fromSchema for {} {}: {}", sourceJsonPath, currentJsonPath, p);
            return cpc;
        }

        if (p.equals(trueSchema)) {
            property.setIsBooleanSchemaTrue(true);
        } else if (p.equals(falseSchema)) {
            property.setIsBooleanSchemaFalse(true);
        }

        // unalias schema
        p = unaliasSchema(p);

        ModelUtils.syncValidationProperties(p, property);
        property.setFormat(p.getFormat());
        property.setExternalDocumentation(p.getExternalDocs());

        boolean isComponentSchema = false;
        if (currentJsonPath != null) {
            String[] refPieces = currentJsonPath.split("/");
            if (refPieces.length >= 4) {
                // component schemas + proprties/items/additionalProperties use case
                String lastPathFragment = refPieces[refPieces.length-1];
                String usedName = lastPathFragment;
                if (refPieces.length >= 5) {
                    // proprties/items/additionalProperties use case
                    // # components schemas someSchema additionalProperties/items
                    if (lastPathFragment.equals("additionalProperties")) {
                        String priorFragment = refPieces[refPieces.length-2];
                        if (!"properties".equals(priorFragment)) {
                            property.setSchemaIsFromAdditionalProperties(true);
                        }
                        // usedName = getAdditionalPropertiesName();
                    } else if (lastPathFragment.equals("schema")) {
                        String priorFragment = refPieces[refPieces.length-2];
                        if (!"parameters".equals(priorFragment)) {
                            String evenDeeperFragment = refPieces[refPieces.length-3];
                            if ("content".equals(evenDeeperFragment)) {
                                // body or parameter content type schemas, in which case 1 deeper is content
                                usedName = ModelUtils.decodeSlashes(priorFragment);
                            }
                        }
                    } else {
                        try {
                            Integer.parseInt(usedName);
                            // for oneOf/anyOf/allOf
                            String priorFragment = refPieces[refPieces.length-2];
                            if ("allOf".equals(priorFragment) || "anyOf".equals(priorFragment) || "oneOf".equals(priorFragment)) {
                                usedName = refPieces[refPieces.length-2] + "_" + usedName;
                            }
                        } catch (NumberFormatException nfe) {
                            // any other case
                            ;
                        }
                    }
                } else {
                    // component schema use case
                    // TODO set discriminator on any schema instances in the future not just these
                    if (!currentJsonPath.startsWith("#/components/schemas/") || refPieces.length != 4) {
                        throw new RuntimeException("Invalid sourceJsonPath "+ sourceJsonPath);
                    }

                    isComponentSchema = true;
                    property.setDiscriminator(createDiscriminator(usedName, p, this.openAPI, currentJsonPath));
                    if (p instanceof ComposedSchema) {
                        updateModelForComposedSchema(property, p, currentJsonPath);
                    }

                    property.setComponentModule(toComponentModule(usedName, "schemas"));
                    if (openAPI != null) {
                        HashMap<String, SchemaTestCase> schemaTestCases = extractSchemaTestCases(xSchemaTestExamplesRefPrefix + usedName);
                        property.testCases = schemaTestCases;
                    }

                }
                CodegenKey ck = getKey(usedName);
                property.name = ck;
            }
        }
        property.description = escapeText(p.getDescription());
        property.unescapedDescription = p.getDescription();
        property.title = p.getTitle();
        // put toExampleValue in a try-catch block to log the error as example values are not critical
        try {
            property.example = toExampleValue(p);
        } catch (Exception e) {
            LOGGER.error("Error in generating `example` for the property {}. Default to ERROR_TO_EXAMPLE_VALUE. Enable debugging for more info.", sourceJsonPath);
            LOGGER.debug("Exception from toExampleValue: {}", e.getMessage());
            property.example = "ERROR_TO_EXAMPLE_VALUE";
        }
        property.defaultValue = toDefaultValue(p);

        if (p.getDeprecated() != null) {
            property.deprecated = p.getDeprecated();
        } else if (p.get$ref() != null) {
            // Since $ref should be replaced with the model it refers
            // to, $ref'ing a model with 'deprecated' set should cause
            // the property to reflect the model's 'deprecated' value.
            String ref = ModelUtils.getSimpleRef(p.get$ref());
            if (ref != null) {
                Schema referencedSchema = ModelUtils.getSchemas(this.openAPI).get(ref);
                if (referencedSchema != null && referencedSchema.getDeprecated() != null) {
                    property.deprecated = referencedSchema.getDeprecated();
                }
            }
        }
        if (p.getReadOnly() != null) {
            property.isReadOnly = p.getReadOnly();
        }
        if (p.getWriteOnly() != null) {
            property.isWriteOnly = p.getWriteOnly();
        }
        if (p.getNullable() != null) {
            property.isNullable = p.getNullable();
        }

        if (p.getXml() != null) {
            if (p.getXml().getAttribute() != null) {
                property.isXmlAttribute = p.getXml().getAttribute();
            }
            property.xmlPrefix = p.getXml().getPrefix();
            property.xmlName = p.getXml().getName();
            property.xmlNamespace = p.getXml().getNamespace();
        }
        if (p.getExtensions() != null && !p.getExtensions().isEmpty()) {
            property.getVendorExtensions().putAll(p.getExtensions());
        } else if (p.get$ref() != null) {
            Schema referencedSchema = ModelUtils.getReferencedSchema(this.openAPI, p);
            if (referencedSchema.getExtensions() != null && !referencedSchema.getExtensions().isEmpty()) {
                property.getVendorExtensions().putAll(referencedSchema.getExtensions());
            }
        }

        //Inline enum case:
        if (p.getEnum() != null && !p.getEnum().isEmpty()) {
            List<Object> _enum = p.getEnum();
            property._enum = new ArrayList<>();
            for (Object i : _enum) {
                property._enum.add(String.valueOf(i));
            }
            property.isEnum = true;

            Map<String, Object> allowableValues = new HashMap<>();
            allowableValues.put("values", _enum);
            if (allowableValues.size() > 0) {
                property.allowableValues = allowableValues;
            }
        }

        Schema referencedSchema = ModelUtils.getReferencedSchema(this.openAPI, p);

        //Referenced enum case:
        if (referencedSchema.getEnum() != null && !referencedSchema.getEnum().isEmpty()) {
            List<Object> _enum = referencedSchema.getEnum();

            Map<String, Object> allowableValues = new HashMap<>();
            allowableValues.put("values", _enum);
            if (allowableValues.size() > 0) {
                property.allowableValues = allowableValues;
            }
        }

        if (referencedSchema.getNullable() != null) {
            property.isNullable = referencedSchema.getNullable();
        }

        property.setTypeProperties(p);
        Schema notSchema = p.getNot();
        if (notSchema != null) {
            CodegenSchema notProperty = fromSchema(notSchema, sourceJsonPath, currentJsonPath + "/not");
            property.setNot(notProperty);
        }
        List<Schema> allOfs = p.getAllOf();
        if (allOfs != null && !allOfs.isEmpty()) {
            List<CodegenSchema> allOfProps = getComposedProperties(allOfs, "allOf", sourceJsonPath, currentJsonPath);
            property.setAllOf(allOfProps);
        }
        List<Schema> anyOfs = p.getAnyOf();
        if (anyOfs != null && !anyOfs.isEmpty()) {
            List<CodegenSchema> anyOfProps = getComposedProperties(anyOfs, "anyOf", sourceJsonPath, currentJsonPath);
            property.setAnyOf(anyOfProps);
        }
        List<Schema> oneOfs = p.getOneOf();
        if (oneOfs != null && !oneOfs.isEmpty()) {
            List<CodegenSchema> oneOfProps = getComposedProperties(oneOfs, "oneOf", sourceJsonPath, currentJsonPath);
            property.setOneOf(oneOfProps);
        }
        if (ModelUtils.isIntegerSchema(p)) { // integer type
            updatePropertyForInteger(property, p);
        } else if (ModelUtils.isBooleanSchema(p)) { // boolean type
            // no action
        } else if (ModelUtils.isFileSchema(p) && !ModelUtils.isStringSchema(p)) {
            // swagger v2 only, type file
            property.isFile = true;
        } else if (ModelUtils.isStringSchema(p)) {
            updatePropertyForString(property, p);
        } else if (ModelUtils.isNumberSchema(p)) {
            updatePropertyForNumber(property, p);
        } else if (ModelUtils.isArraySchema(p)) {
            // default to string if inner item is undefined
            if (p.getXml() != null) {
                property.isXmlWrapped = p.getXml().getWrapped() == null ? false : p.getXml().getWrapped();
                property.xmlPrefix = p.getXml().getPrefix();
                property.xmlNamespace = p.getXml().getNamespace();
                property.xmlName = p.getXml().getName();
            }

            // handle inner property
            ArraySchema arraySchema = (ArraySchema) p;
            Schema innerSchema = unaliasSchema(arraySchema.getItems());
            CodegenSchema innerProperty = fromSchema(
                    innerSchema, sourceJsonPath, currentJsonPath + "/items");
            property.setItems(innerProperty);
        } else if (ModelUtils.isTypeObjectSchema(p)) {
            updatePropertyForObject(property, p, sourceJsonPath, currentJsonPath);
        } else if (ModelUtils.isAnyType(p)) {
            updatePropertyForAnyType(property, p, sourceJsonPath, currentJsonPath);
        } else if (!ModelUtils.isNullType(p)) {
            // referenced model
            ;
        }
        String ref = p.get$ref();
        if (ref != null) {
            property.setRef(ref);
            property.setRefClass(toRefClass(
                    ref,
                    sourceJsonPath
            ));
            property.setRefModule(toRefModule(ref, "schemas", sourceJsonPath));
        }
        if (addSchemaImportsFromV3SpecLocations && isComponentSchema) {
            property.imports = new TreeSet<>();
            addImports(property.imports, getImports(property, generatorMetadata.getFeatureSet()));
        }
        schemaCodegenPropertyCache.put(ns, property);

        LOGGER.debug("debugging fromSchema return: {}", property);
        return property;
    }

    public String toRefClass(String ref, String sourceJsonPath) {
        String[] refPieces = ref.split("/");
        return toModelName(refPieces[refPieces.length-1]);
    }

    protected CodegenSchema getMostInnerItems(CodegenSchema property) {
        CodegenSchema currentProperty = property;
        while (currentProperty != null && (Boolean.TRUE.equals(currentProperty.isMap)
                || Boolean.TRUE.equals(currentProperty.isArray)) && currentProperty.items != null) {
            currentProperty = currentProperty.items;
        }
        return currentProperty;
    }

    public String getBodyParameterName(CodegenOperation co) {
        String bodyParameterName = "body";
        if (co != null && co.vendorExtensions != null && co.vendorExtensions.containsKey("x-codegen-request-body-name")) {
            bodyParameterName = (String) co.vendorExtensions.get("x-codegen-request-body-name");
        }
        return bodyParameterName;
    }

    /**
     * Convert OAS Operation object to Codegen Operation object
     *
     * @param httpMethod HTTP method
     * @param operation  OAS operation object
     * @param path       the path of the operation
     * @param servers    list of servers
     * @return Codegen Operation object
     */
    @Override
    public CodegenOperation fromOperation(String path,
                                          String httpMethod,
                                          Operation operation,
                                          List<Server> servers) {
        LOGGER.debug("fromOperation => operation: {}", operation);
        if (operation == null)
            throw new RuntimeException("operation cannot be null in fromOperation");

        Map<String, Schema> schemas = ModelUtils.getSchemas(this.openAPI);
        CodegenOperation op = new CodegenOperation();
        Set<String> imports = new HashSet<>();
        if (operation.getExtensions() != null && !operation.getExtensions().isEmpty()) {
            op.vendorExtensions.putAll(operation.getExtensions());

            Object isCallbackRequest = op.vendorExtensions.remove("x-callback-request");
            op.isCallbackRequest = Boolean.TRUE.equals(isCallbackRequest);
        }

        // servers setting
        if (operation.getServers() != null && !operation.getServers().isEmpty()) {
            // use operation-level servers first if defined
            op.servers = fromServers(operation.getServers());
        } else if (servers != null && !servers.isEmpty()) {
            // use path-level servers
            op.servers = fromServers(servers);
        }

        // tags
        List<String> operationtTagNames = operation.getTags();
        Map<String, CodegenTag> codegenTags = new HashMap<>();
        if (operationtTagNames != null) {
            for (String tagName: operation.getTags()) {
                CodegenTag codegenTag = new CodegenTag();
                codegenTag.setName(tagName);
                codegenTag.setModuleName(toApiFilename(tagName));
                codegenTag.setClassName(toApiName(tagName));
                codegenTags.put(tagName, codegenTag);
            }
        } else {
            String tagName = "default";
            CodegenTag codegenTag = new CodegenTag();
            codegenTag.setName(tagName);
            codegenTag.setModuleName(toApiFilename(tagName));
            codegenTag.setClassName(toApiName(tagName));
            codegenTags.put(tagName, codegenTag);
        }
        op.tags = codegenTags;

        // store the original operationId for plug-in
        op.operationIdOriginal = operation.getOperationId();

        String operationId = getOrGenerateOperationId(operation, path, httpMethod);
        // remove prefix in operationId
        if (removeOperationIdPrefix) {
            // The prefix is everything before the removeOperationIdPrefixCount occurrence of removeOperationIdPrefixDelimiter
            String[] components = operationId.split("[" + removeOperationIdPrefixDelimiter + "]");
            if (components.length > 1) {
                // If removeOperationIdPrefixCount is -1 or bigger that the number of occurrences, uses the last one
                int component_number = removeOperationIdPrefixCount == -1 ? components.length - 1 : removeOperationIdPrefixCount;
                component_number = Math.min(component_number, components.length - 1);
                // Reconstruct the operationId from its split elements and the delimiter
                operationId = String.join(removeOperationIdPrefixDelimiter, Arrays.copyOfRange(components, component_number, components.length));
            }
        }
        operationId = removeNonNameElementToCamelCase(operationId);

        if (isStrictSpecBehavior() && !path.startsWith("/")) {
            // modifies an operation.path to strictly conform to OpenAPI Spec
            op.path = "/" + path;
        } else {
            op.path = path;
        }
        String sourceJsonPath = "#/paths/" + ModelUtils.encodeSlashes(op.path) + "/" + httpMethod;

        op.operationId = toOperationId(operationId);
        op.summary = escapeText(operation.getSummary());
        op.unescapedNotes = operation.getDescription();
        op.notes = escapeText(operation.getDescription());
        op.hasConsumes = false;
        op.hasProduces = false;
        if (operation.getDeprecated() != null) {
            op.isDeprecated = operation.getDeprecated();
        }

        addConsumesInfo(operation, op);

        if (operation.getResponses() != null && !operation.getResponses().isEmpty()) {
            op.responses = new TreeMap<>();
            for (Map.Entry<String, ApiResponse> operationGetResponsesEntry : operation.getResponses().entrySet()) {
                String key = operationGetResponsesEntry.getKey();
                ApiResponse response = operationGetResponsesEntry.getValue();
                addProducesInfo(response, op);
                String usedSourceJsonPath = sourceJsonPath + "/responses/" + key;
                CodegenResponse r = fromResponse(response, usedSourceJsonPath);

                op.responses.put(key, r);
                if ("default".equals(key)) {
                    op.defaultResponse = r;
                } else {
                    if (op.nonDefaultResponses == null) {
                        op.nonDefaultResponses = new TreeMap<>();
                    }
                    op.nonDefaultResponses.put(key, r);
                    if (key.endsWith("XX") && key.length() == 3) {
                        if (op.wildcardCodeResponses == null) {
                            op.wildcardCodeResponses = new TreeMap<>();
                        }
                        Integer firstNumber = Integer.parseInt(key.substring(0, 1));
                        op.wildcardCodeResponses.put(firstNumber, r);
                        if (firstNumber > 3 && r.getContent() != null) {
                            for (CodegenMediaType cm: r.getContent().values()) {
                                if (cm.getSchema() != null) {
                                    op.hasErrorResponseObject = true;
                                    break;
                                }
                            }
                        }
                    } else {
                        if (op.statusCodeResponses == null) {
                            op.statusCodeResponses = new TreeMap<>();
                        }
                        Integer statusCode = Integer.parseInt(key);
                        op.statusCodeResponses.put(statusCode, r);
                        if (statusCode > 299 && r.getContent() != null) {
                            for (CodegenMediaType cm: r.getContent().values()) {
                                if (cm.getSchema() != null) {
                                    op.hasErrorResponseObject = true;
                                    break;
                                }
                            }
                        }
                    }
                }
            }

            // sort them
            if (op.responses != null) {
                op.responses = new TreeMap<>(op.responses);
            }
            if (op.nonDefaultResponses != null) {
                op.nonDefaultResponses = new TreeMap<>(op.nonDefaultResponses);
            }
            if (op.statusCodeResponses != null) {
                op.statusCodeResponses = new TreeMap<>(op.statusCodeResponses);
            }
            if (op.wildcardCodeResponses != null) {
                op.wildcardCodeResponses = new TreeMap<>(op.wildcardCodeResponses);
            }
        }

        if (operation.getCallbacks() != null && !operation.getCallbacks().isEmpty()) {
            operation.getCallbacks().forEach((name, callback) -> {
                CodegenCallback c = fromCallback(name, callback, servers);
                op.callbacks.add(c);
            });
        }

        List<Parameter> parameters = operation.getParameters();
        List<CodegenParameter> allParams = new ArrayList<>();
        List<CodegenParameter> bodyParams = new ArrayList<>();
        List<CodegenParameter> pathParams = new ArrayList<>();
        List<CodegenParameter> queryParams = new ArrayList<>();
        List<CodegenParameter> headerParams = new ArrayList<>();
        List<CodegenParameter> cookieParams = new ArrayList<>();
        List<CodegenParameter> formParams = new ArrayList<>();
        List<CodegenParameter> requiredParams = new ArrayList<>();
        List<CodegenParameter> optionalParams = new ArrayList<>();

        CodegenParameter requestBody = null;
        RequestBody opRequestBody = operation.getRequestBody();
        if (opRequestBody != null) {

            String bodyParameterName = getBodyParameterName(op);
            requestBody = fromRequestBody(opRequestBody, bodyParameterName, sourceJsonPath + "/requestBody");
            requestBody.description = escapeText(opRequestBody.getDescription());
            postProcessParameter(requestBody);

            bodyParams.add(requestBody);

            // add example
            if (schemas != null && !isSkipOperationExample() && opRequestBody.getContent() != null) {
                String firstContentType = (String) opRequestBody.getContent().keySet().toArray()[0];
                op.requestBodyExamples = new ExampleGenerator(schemas, this.openAPI).generate(
                    null, new ArrayList<>(getConsumesInfo(this.openAPI, operation)), opRequestBody.getContent().get(firstContentType).getSchema());
            }
        }

        if (parameters != null) {
            Integer i = 0;
            for (Parameter param : parameters) {
                String usedSourceJsonPath = sourceJsonPath + "/parameters/" + i.toString();
                CodegenParameter p = fromParameter(param, usedSourceJsonPath);
                allParams.add(p);
                i++;

                if (p.isQueryParam) {
                    queryParams.add(p.copy());
                } else if (p.isPathParam) {
                    pathParams.add(p.copy());
                } else if (p.isHeaderParam) {
                    headerParams.add(p.copy());
                } else if (p.isCookieParam) {
                    cookieParams.add(p.copy());
                } else {
                    LOGGER.warn("Unknown parameter type for {}", p.baseName);
                }

            }
        }

        // create optional, required parameters
        for (CodegenParameter cp : allParams) {
            if (cp.required) { //required parameters
                requiredParams.add(cp.copy());
            } else { // optional parameters
                optionalParams.add(cp.copy());
                op.hasOptionalParams = true;
            }
        }
        if (requestBody != null) {
            if (requestBody.required) {
                requiredParams.add(requestBody.copy());
            } else {
                optionalParams.add(requestBody.copy());
                op.hasOptionalParams = true;
            }
        }

        // add imports to operation import tag
        for (String i : imports) {
            if (needToImport(i)) {
                op.imports.add(i);
            }
        }

        op.requestBody = requestBody;
        op.httpMethod = httpMethod.toUpperCase(Locale.ROOT);

        // move "required" parameters in front of "optional" parameters
        if (sortParamsByRequiredFlag) {
            Collections.sort(allParams, new Comparator<CodegenParameter>() {
                @Override
                public int compare(CodegenParameter one, CodegenParameter another) {
                    if (one.required == another.required)
                        return 0;
                    else if (one.required)
                        return -1;
                    else
                        return 1;
                }
            });
        }

        op.allParams = allParams;
        op.bodyParams = bodyParams;
        op.pathParams = pathParams;
        op.queryParams = queryParams;
        op.headerParams = headerParams;
        op.cookieParams = cookieParams;
        op.requiredParams = requiredParams;
        op.optionalParams = optionalParams;
        op.externalDocs = operation.getExternalDocs();
        // legacy support
        op.nickname = op.operationId;

        if (op.allParams.size() > 0) {
            op.hasParams = true;
        }
        op.hasRequiredParams = op.requiredParams.size() > 0;

        // set Restful Flag
        op.isRestfulShow = op.isRestfulShow();
        op.isRestfulIndex = op.isRestfulIndex();
        op.isRestfulCreate = op.isRestfulCreate();
        op.isRestfulUpdate = op.isRestfulUpdate();
        op.isRestfulDestroy = op.isRestfulDestroy();
        op.isRestful = op.isRestful();

        return op;
    }

    public boolean isParameterNameUnique(CodegenParameter p, List<CodegenParameter> parameters) {
        for (CodegenParameter parameter : parameters) {
            if (System.identityHashCode(p) == System.identityHashCode(parameter)) {
                continue; // skip itself
            }

            if (p.paramName.equals(parameter.paramName)) {
                return false;
            }
        }

        return true;
    }

    /**
     * Convert OAS Response object to Codegen Response object
     *
     * @param response     OAS Response object
     * @return Codegen Response object
     */
    public CodegenResponse fromResponse(ApiResponse response, String sourceJsonPath) {
        String responseRef = response.get$ref();
        ApiResponse usedResponse = response;
        String usedSourceJsonPath = sourceJsonPath;
        if (responseRef != null) {
            usedResponse = ModelUtils.getReferencedApiResponse(this.openAPI, response);
            usedSourceJsonPath = responseRef;
        }

        if (usedResponse == null) {
            LOGGER.error("response in fromResponse cannot be null!");
            throw new RuntimeException("response in fromResponse cannot be null!");
        }

        CodegenResponse r = new CodegenResponse();
        if (responseRef != null) {
            r.setRef(responseRef);
            r.setRefModule(toRefModule(responseRef, "responses", sourceJsonPath));
        }
        if (sourceJsonPath != null) {
            String[] refPieces = sourceJsonPath.split("/");
            if (sourceJsonPath.startsWith("#/components/responses/") && refPieces.length == 4) {
                String componentName = refPieces[3];
                r.setComponentModule(toComponentModule(componentName, "responses"));
            }
        }
        r.message = escapeText(usedResponse.getDescription());
        // TODO need to revise and test examples in responses
        // ApiResponse does not support examples at the moment
        r.jsonSchema = Json.pretty(usedResponse);
        if (usedResponse.getExtensions() != null && !usedResponse.getExtensions().isEmpty()) {
            r.vendorExtensions.putAll(usedResponse.getExtensions());
        }

        Map<String, Header> headers = usedResponse.getHeaders();
        if (headers != null && !headers.isEmpty()) {
            if (!usedResponse.getHeaders().isEmpty()) {
                r.hasHeaders = true;
            }
            Map<String, CodegenHeader> responseHeaders = new HashMap<>();
            for (Entry<String, Header> entry : headers.entrySet()) {
                String headerName = entry.getKey();
                Header header = entry.getValue();
                String headerSourceJsonPath = usedSourceJsonPath + "/headers/" + headerName;
                CodegenHeader responseHeader = fromHeader(header, headerSourceJsonPath);
                responseHeaders.put(headerName, responseHeader);
            }
            r.setHeaders(responseHeaders);
        }
        r.setContent(getContent(usedResponse.getContent(), r.imports, "", usedSourceJsonPath + "/content"));

        return r;
    }

    /**
     * Convert OAS Callback object to Codegen Callback object
     *
     * @param name     callback name
     * @param callback OAS Callback object
     * @param servers  list of servers
     * @return Codegen Response object
     */
    public CodegenCallback fromCallback(String name, Callback callback, List<Server> servers) {
        CodegenCallback c = new CodegenCallback();
        c.name = name;

        if (callback.getExtensions() != null && !callback.getExtensions().isEmpty()) {
            c.vendorExtensions.putAll(callback.getExtensions());
        }

        callback.forEach((expression, pi) -> {
            CodegenCallback.Url u = new CodegenCallback.Url();
            u.expression = expression;

            if (pi.getExtensions() != null && !pi.getExtensions().isEmpty()) {
                u.vendorExtensions.putAll(pi.getExtensions());
            }

            Stream.of(
                            Pair.of("get", pi.getGet()),
                            Pair.of("head", pi.getHead()),
                            Pair.of("put", pi.getPut()),
                            Pair.of("post", pi.getPost()),
                            Pair.of("delete", pi.getDelete()),
                            Pair.of("patch", pi.getPatch()),
                            Pair.of("options", pi.getOptions()))
                    .filter(p -> p.getValue() != null)
                    .forEach(p -> {
                        String method = p.getKey();
                        Operation op = p.getValue();

                        boolean genId = op.getOperationId() == null;
                        if (genId) {
                            op.setOperationId(getOrGenerateOperationId(op, c.name + "_" + expression.replaceAll("\\{\\$.*}", ""), method));
                        }

                        if (op.getExtensions() == null) {
                            op.setExtensions(new HashMap<>());
                        }
                        // This extension will be removed later by `fromOperation()` as it is only needed here to
                        // distinguish between normal operations and callback requests
                        op.getExtensions().put("x-callback-request", true);

                        CodegenOperation co = fromOperation(expression, method, op, servers);
                        if (genId) {
                            co.operationIdOriginal = null;
                            // legacy (see `fromOperation()`)
                            co.nickname = co.operationId;
                        }
                        u.requests.add(co);
                    });

            c.urls.add(u);
        });

        return c;
    }

    public CodegenHeader fromHeader(Header header, String sourceJsonPath) {
        String headerRef = header.get$ref();
        Header usedHeader = header;
        String usedSourceJsonPath = sourceJsonPath;
        if (headerRef != null) {
            usedHeader = ModelUtils.getReferencedHeader(this.openAPI, header);
            usedSourceJsonPath = headerRef;
        }

        CodegenHeader codegenHeader = new CodegenHeader();
        setHeaderInfo(usedHeader, codegenHeader, usedSourceJsonPath, "Header");
        if (usedHeader.getStyle() != null) {
            codegenHeader.style = usedHeader.getStyle().toString();
        }
        if (headerRef != null) {
            String refModule = toRefModule(headerRef, "headers", sourceJsonPath);
            codegenHeader.setRefModule(refModule);
        }
        if (sourceJsonPath != null) {
            String[] refPieces = sourceJsonPath.split("/");
            if (sourceJsonPath.startsWith("#/components/headers/") && refPieces.length == 4) {
                String componentName = refPieces[3];
                codegenHeader.setComponentModule(toComponentModule(componentName, "headers"));
            }
        }
        return codegenHeader;
    }

    private void setHeaderInfo(Header header, CodegenHeader codegenHeader, String sourceJsonPath, String type) {
        codegenHeader.description = escapeText(header.getDescription());
        codegenHeader.unescapedDescription = header.getDescription();
        if (header.getRequired() != null) {
            codegenHeader.required = header.getRequired();
        }
        if (header.getDeprecated() != null) {
            codegenHeader.isDeprecated = header.getDeprecated();
        }
        codegenHeader.jsonSchema = Json.pretty(header);

        if (header.getExtensions() != null && !header.getExtensions().isEmpty()) {
            codegenHeader.vendorExtensions.putAll(header.getExtensions());
        }

        // the parameter model name is obtained from the schema $ref
        // e.g. #/components/schemas/list_pageQuery_parameter => toModelName(list_pageQuery_parameter)
        if (header.getSchema() != null) {
            String usedSourceJsonPath = sourceJsonPath + "/schema";
            CodegenSchema prop = fromSchema(
                    header.getSchema(),
                    usedSourceJsonPath,
                    usedSourceJsonPath
            );
            codegenHeader.setSchema(prop);
            if (addSchemaImportsFromV3SpecLocations) {
                addImports(codegenHeader.imports, getImports(prop, generatorMetadata.getFeatureSet()));
            }
        } else if (header.getContent() != null) {
            Content content = header.getContent();
            codegenHeader.setContent(getContent(content, codegenHeader.imports, "schema", sourceJsonPath + "/content"));
        }

        // the default value is false
        // https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.2.md#user-content-parameterexplode
        codegenHeader.isExplode = header.getExplode() == null ? false : header.getExplode();

        if (header.getRequired() != null) {
            codegenHeader.required = header.getRequired().booleanValue();
        }


        String priorJsonPathFragment = sourceJsonPath.substring(sourceJsonPath.lastIndexOf("/") + 1);
        codegenHeader.paramName = toParamName(priorJsonPathFragment);

        // default to UNKNOWN_PARAMETER_NAME if paramName is null
        if (codegenHeader.paramName == null) {
            codegenHeader.paramName = "UNKNOWN_" + type.toUpperCase(Locale.ROOT) + "_NAME";
            LOGGER.warn(type + " name not defined properly. Default to " + codegenHeader.paramName);
        }
    }

    /**
     * Convert OAS Parameter object to Codegen Parameter object
     *
     * @param parameter OAS parameter object
     * @param sourceJsonPath the json path to the parameter
     * @return Codegen Parameter object
     */
    public CodegenParameter fromParameter(Parameter parameter, String sourceJsonPath) {
        String parameterRef = parameter.get$ref();
        Parameter usedParameter = parameter;
        String usedSourceJsonPath = sourceJsonPath;
        if (parameterRef != null) {
            usedParameter = ModelUtils.getReferencedParameter(this.openAPI, parameter);
            usedSourceJsonPath = parameterRef;
        }

        CodegenParameter codegenParameter = new CodegenParameter();

        Header prameterHeader = new Header();
        prameterHeader.setContent(usedParameter.getContent());
        prameterHeader.setDescription(usedParameter.getDescription());
        prameterHeader.setDeprecated(usedParameter.getDeprecated());
        prameterHeader.setSchema(usedParameter.getSchema());
        prameterHeader.set$ref(usedParameter.get$ref());
        prameterHeader.setExamples(usedParameter.getExamples());
        prameterHeader.setExample(usedParameter.getExample());
        prameterHeader.setExplode(usedParameter.getExplode());
        prameterHeader.setExtensions(usedParameter.getExtensions());
        prameterHeader.setRequired(usedParameter.getRequired());
        setHeaderInfo(prameterHeader, codegenParameter, usedSourceJsonPath, "Parameter");

        if (usedParameter.getStyle() != null) {
            codegenParameter.style = usedParameter.getStyle().toString();
        }
        codegenParameter.baseName = usedParameter.getName();

        if (parameterRef != null) {
            String refModule = toRefModule(parameterRef, "parameters", sourceJsonPath);
            codegenParameter.setRefModule(refModule);
        }
        if (sourceJsonPath != null) {
            String[] refPieces = sourceJsonPath.split("/");
            if (sourceJsonPath.startsWith("#/components/parameters/") && refPieces.length == 4) {
                String componentName = refPieces[3];
                codegenParameter.setComponentModule(toComponentModule(componentName, "parameters"));
            }
        }

        if (GlobalSettings.getProperty("debugParser") != null) {
            LOGGER.info("working on Parameter {}", parameter.getName());
            LOGGER.info("JSON schema: {}", codegenParameter.jsonSchema);
        }

        if (parameter instanceof QueryParameter || "query".equalsIgnoreCase(usedParameter.getIn())) {
            codegenParameter.isQueryParam = true;
            codegenParameter.isAllowEmptyValue = parameter.getAllowEmptyValue() != null && usedParameter.getAllowEmptyValue();
        } else if (parameter instanceof PathParameter || "path".equalsIgnoreCase(usedParameter.getIn())) {
            codegenParameter.required = true;
            codegenParameter.isPathParam = true;
        } else if (parameter instanceof HeaderParameter || "header".equalsIgnoreCase(usedParameter.getIn())) {
            codegenParameter.isHeaderParam = true;
        } else if (parameter instanceof CookieParameter || "cookie".equalsIgnoreCase(usedParameter.getIn())) {
            codegenParameter.isCookieParam = true;
        } else {
            LOGGER.warn("Unknown parameter type: {}", usedParameter.getName());
        }
        if (parameter.getStyle() != null) {
            codegenParameter.isDeepObject = Parameter.StyleEnum.DEEPOBJECT == usedParameter.getStyle();
        }

        // set the parameter example value
        // should be overridden by lang codegen
        setParameterExampleValue(codegenParameter, usedParameter);

        postProcessParameter(codegenParameter);
        LOGGER.debug("debugging codegenParameter return: {}", codegenParameter);
        return codegenParameter;
    }

    /**
     * Convert map of OAS SecurityScheme objects to a list of Codegen Security objects
     *
     * @param securitySchemeMap a map of OAS SecuritySchemeDefinition object
     * @return a list of Codegen Security objects
     */
    @Override
    @SuppressWarnings("static-method")
    public List<CodegenSecurity> fromSecurity(Map<String, SecurityScheme> securitySchemeMap) {
        if (securitySchemeMap == null) {
            return Collections.emptyList();
        }

        List<CodegenSecurity> codegenSecurities = new ArrayList<>(securitySchemeMap.size());
        for (String key : securitySchemeMap.keySet()) {
            final SecurityScheme securityScheme = securitySchemeMap.get(key);
            if (SecurityScheme.Type.APIKEY.equals(securityScheme.getType())) {
                final CodegenSecurity cs = defaultCodegenSecurity(key, securityScheme);
                cs.isBasic = cs.isOAuth = false;
                cs.isApiKey = true;
                cs.keyParamName = securityScheme.getName();
                cs.isKeyInHeader = securityScheme.getIn() == SecurityScheme.In.HEADER;
                cs.isKeyInQuery = securityScheme.getIn() == SecurityScheme.In.QUERY;
                cs.isKeyInCookie = securityScheme.getIn() == SecurityScheme.In.COOKIE;  //it assumes a validation step prior to generation. (cookie-auth supported from OpenAPI 3.0.0)
                codegenSecurities.add(cs);
            } else if (SecurityScheme.Type.HTTP.equals(securityScheme.getType())) {
                final CodegenSecurity cs = defaultCodegenSecurity(key, securityScheme);
                cs.isKeyInHeader = cs.isKeyInQuery = cs.isKeyInCookie = cs.isApiKey = cs.isOAuth = false;
                cs.isBasic = true;
                if ("basic".equalsIgnoreCase(securityScheme.getScheme())) {
                    cs.isBasicBasic = true;
                } else if ("bearer".equalsIgnoreCase(securityScheme.getScheme())) {
                    cs.isBasicBearer = true;
                    cs.bearerFormat = securityScheme.getBearerFormat();
                } else if ("signature".equalsIgnoreCase(securityScheme.getScheme())) {
                    // HTTP signature as defined in https://datatracker.ietf.org/doc/draft-cavage-http-signatures/
                    // The registry of security schemes is maintained by IANA.
                    // https://www.iana.org/assignments/http-authschemes/http-authschemes.xhtml
                    // As of January 2020, the "signature" scheme has not been registered with IANA yet.
                    // This scheme may have to be changed when it is officially registered with IANA.
                    cs.isHttpSignature = true;
                    once(LOGGER).warn("Security scheme 'HTTP signature' is a draft IETF RFC and subject to change.");
                } else {
                    once(LOGGER).warn("Unknown scheme `{}` found in the HTTP security definition.", securityScheme.getScheme());
                }
                codegenSecurities.add(cs);
            } else if (SecurityScheme.Type.OAUTH2.equals(securityScheme.getType())) {
                final OAuthFlows flows = securityScheme.getFlows();
                boolean isFlowEmpty = true;
                if (securityScheme.getFlows() == null) {
                    throw new RuntimeException("missing oauth flow in " + key);
                }
                if (flows.getPassword() != null) {
                    final CodegenSecurity cs = defaultOauthCodegenSecurity(key, securityScheme);
                    setOauth2Info(cs, flows.getPassword());
                    cs.isPassword = true;
                    cs.flow = "password";
                    codegenSecurities.add(cs);
                    isFlowEmpty = false;
                }
                if (flows.getImplicit() != null) {
                    final CodegenSecurity cs = defaultOauthCodegenSecurity(key, securityScheme);
                    setOauth2Info(cs, flows.getImplicit());
                    cs.isImplicit = true;
                    cs.flow = "implicit";
                    codegenSecurities.add(cs);
                    isFlowEmpty = false;
                }
                if (flows.getClientCredentials() != null) {
                    final CodegenSecurity cs = defaultOauthCodegenSecurity(key, securityScheme);
                    setOauth2Info(cs, flows.getClientCredentials());
                    cs.isApplication = true;
                    cs.flow = "application";
                    codegenSecurities.add(cs);
                    isFlowEmpty = false;
                }
                if (flows.getAuthorizationCode() != null) {
                    final CodegenSecurity cs = defaultOauthCodegenSecurity(key, securityScheme);
                    setOauth2Info(cs, flows.getAuthorizationCode());
                    cs.isCode = true;
                    cs.flow = "accessCode";
                    codegenSecurities.add(cs);
                    isFlowEmpty = false;
                }

                if (isFlowEmpty) {
                    once(LOGGER).error("Invalid flow definition defined in the security scheme: {}", flows);
                }
            } else {
                once(LOGGER).error("Unknown type `{}` found in the security definition `{}`.", securityScheme.getType(), securityScheme.getName());
            }
        }

        // sort auth methods to maintain the same order
        Collections.sort(codegenSecurities, new Comparator<CodegenSecurity>() {
            @Override
            public int compare(CodegenSecurity one, CodegenSecurity another) {
                return ObjectUtils.compare(one.name, another.name);
            }
        });

        return codegenSecurities;
    }

    private CodegenSecurity defaultCodegenSecurity(String key, SecurityScheme securityScheme) {
        final CodegenSecurity cs = new CodegenSecurity();
        cs.name = key;
        cs.type = securityScheme.getType().toString();
        cs.isCode = cs.isPassword = cs.isApplication = cs.isImplicit = false;
        cs.isHttpSignature = false;
        cs.isBasicBasic = cs.isBasicBearer = false;
        cs.scheme = securityScheme.getScheme();
        if (securityScheme.getExtensions() != null) {
            cs.vendorExtensions.putAll(securityScheme.getExtensions());
        }
        return cs;
    }

    private CodegenSecurity defaultOauthCodegenSecurity(String key, SecurityScheme securityScheme) {
        final CodegenSecurity cs = defaultCodegenSecurity(key, securityScheme);
        cs.isKeyInHeader = cs.isKeyInQuery = cs.isKeyInCookie = cs.isApiKey = cs.isBasic = false;
        cs.isOAuth = true;
        return cs;
    }

    protected void setReservedWordsLowerCase(List<String> words) {
        reservedWords = new HashSet<>();
        for (String word : words) {
            reservedWords.add(word.toLowerCase(Locale.ROOT));
        }
    }

    protected boolean isReservedWord(String word) {
        return word != null && reservedWords.contains(word.toLowerCase(Locale.ROOT));
    }

    /**
     * Get operationId from the operation object, and if it's blank, generate a new one from the given parameters.
     *
     * @param operation  the operation object
     * @param path       the path of the operation
     * @param httpMethod the HTTP method of the operation
     * @return the (generated) operationId
     */
    protected String getOrGenerateOperationId(Operation operation, String path, String httpMethod) {
        String operationId = operation.getOperationId();
        if (StringUtils.isBlank(operationId)) {
            String tmpPath = path;
            tmpPath = tmpPath.replaceAll("\\{", "");
            tmpPath = tmpPath.replaceAll("\\}", "");
            String[] parts = (tmpPath + "/" + httpMethod).split("/");
            StringBuilder builder = new StringBuilder();
            if ("/".equals(tmpPath)) {
                // must be root tmpPath
                builder.append("root");
            }
            for (String part : parts) {
                if (part.length() > 0) {
                    if (builder.toString().length() == 0) {
                        part = Character.toLowerCase(part.charAt(0)) + part.substring(1);
                    } else {
                        part = camelize(part);
                    }
                    builder.append(part);
                }
            }
            operationId = sanitizeName(builder.toString());
            LOGGER.warn("Empty operationId found for path: {} {}. Renamed to auto-generated operationId: {}", httpMethod, path, operationId);
        }
        return operationId;
    }

    /**
     * Check the type to see if it needs import the library/module/package
     *
     * @param type name of the type
     * @return true if the library/module/package of the corresponding type needs to be imported
     */
    protected boolean needToImport(String type) {
        return StringUtils.isNotBlank(type) && !defaultIncludes.contains(type)
                && !languageSpecificPrimitives.contains(type);
    }

    /**
     * Add operation to group
     *
     * @param tag          name of the tag
     * @param resourcePath path of the resource
     * @param operation    OAS Operation object
     * @param co           Codegen Operation object
     * @param operations   map of Codegen operations
     */
    @Override
    @SuppressWarnings("static-method")
    public void addOperationToGroup(String tag, String resourcePath, Operation operation, CodegenOperation
            co, Map<String, List<CodegenOperation>> operations) {
        List<CodegenOperation> opList = operations.get(tag);
        if (opList == null) {
            opList = new ArrayList<>();
            operations.put(tag, opList);
        }
        // check for operationId uniqueness
        String uniqueName = co.operationId;
        int counter = 0;
        for (CodegenOperation op : opList) {
            if (uniqueName.equals(op.operationId)) {
                uniqueName = co.operationId + "_" + counter;
                counter++;
            }
        }
        if (!co.operationId.equals(uniqueName)) {
            LOGGER.warn("generated unique operationId `{}`", uniqueName);
        }
        co.operationId = uniqueName;
        co.operationIdLowerCase = uniqueName.toLowerCase(Locale.ROOT);
        co.operationIdCamelCase = camelize(uniqueName);
        co.operationIdSnakeCase = underscore(uniqueName);
        opList.add(co);
        co.baseName = tag;
    }

    protected void addImports(CodegenSchema m, CodegenSchema type) {
        addImports(m.imports, type);
    }

    protected void addImports(Set<String> importsToBeAddedTo, CodegenSchema type) {
        addImports(importsToBeAddedTo, getImports(type, generatorMetadata.getFeatureSet()));
    }

    protected void addImports(Set<String> importsToBeAddedTo, Set<String> importsToAdd) {
        importsToAdd.stream().forEach(i -> addImport(importsToBeAddedTo, i));
    }

    protected void addImport(Set<String> importsToBeAddedTo, String type) {
        if (shouldAddImport(type)) {
            importsToBeAddedTo.add(type);
        }
    }

    protected boolean shouldAddImport(String type) {
        return type != null && needToImport(type);
    }

    /**
     * Add variables (properties) to codegen model (list of properties, various flags, etc)
     *
     * @param m          Must be an instance of JsonSchema, may be model or property...
     * @param properties a map of properties (schema)
     * @param mandatory  a set of required properties' name
     */
    protected void addProperties(JsonSchema m, Map<String, Schema> properties, Set<String> mandatory, String sourceJsonPath, String currentJsonPath) {
        if (properties == null) {
            return;
        }

        CodegenSchema cm = null;
        if (m instanceof CodegenSchema) {
            cm = (CodegenSchema) m;
        }
        LinkedHashMap<CodegenKey, CodegenSchema> propertiesMap = new LinkedHashMap<>();
        LinkedHashMap<CodegenKey, CodegenSchema> optionalProperties = new LinkedHashMap<>();

        for (Map.Entry<String, Schema> entry : properties.entrySet()) {
            final String key = entry.getKey();
            final Schema prop = entry.getValue();
            if (prop == null) {
                LOGGER.warn("Please report the issue. There shouldn't be null property for {}", key);
            } else {
                final CodegenSchema cp;

                String propertySourceJsonPath = currentJsonPath + "/properties/" + key;
                cp = fromSchema(prop, sourceJsonPath, propertySourceJsonPath);

                CodegenKey ck = getKey(key);
                propertiesMap.put(ck, cp);
                if (!mandatory.contains(key)) {
                    optionalProperties.put(ck, cp);
                }

                if (cm == null) {
                    continue;
                }

                if (!addSchemaImportsFromV3SpecLocations) {
                    addImportsForPropertyType(cm, cp);
                }
            }
        }
        if (!propertiesMap.isEmpty()) {
            m.setProperties(propertiesMap);
        }
        if (!optionalProperties.isEmpty()) {
            m.setOptionalProperties(optionalProperties);
        }
        return;
    }

    /**
     * For a given property, adds all needed imports to the model
     * This includes a flat property type (e.g. property type: ReferencedModel)
     * as well as container type (property type: array of ReferencedModel's)
     *
     * @param model    The codegen representation of the OAS schema.
     * @param property The codegen representation of the OAS schema's property.
     */
    protected void addImportsForPropertyType(CodegenSchema model, CodegenSchema property) {
        if (model.imports == null) {
            model.imports = new TreeSet<>();
        }
        if (property.isArray) {
            if (Boolean.TRUE.equals(property.getUniqueItems())) { // set
                addImport(model.imports, typeMapping.get("set"));
            } else { // array
                addImport(model.imports, typeMapping.get("array"));
            }
        }

        if (property.isMap) { // map
            addImport(model.imports, typeMapping.get("map"));
        }

        addImports(model, property);
    }

    /**
     * Determine all of the types in the model definitions (schemas) that are aliases of
     * simple types.
     *
     * @param schemas The complete set of model definitions (schemas).
     * @return A mapping from model name to type alias
     */
    Map<String, String> getAllAliases(Map<String, Schema> schemas) {
        if (schemas == null || schemas.isEmpty()) {
            return new HashMap<>();
        }

        Map<String, String> aliases = new HashMap<>();
        for (Map.Entry<String, Schema> entry : schemas.entrySet()) {
            Schema schema = entry.getValue();
            if (isAliasOfSimpleTypes(schema)) {
                String oasName = entry.getKey();
                String schemaType = getPrimitiveType(schema);
                aliases.put(oasName, schemaType);
            }

        }

        return aliases;
    }

    private static Boolean isAliasOfSimpleTypes(Schema schema) {
        return (!ModelUtils.isObjectSchema(schema)
                && !ModelUtils.isArraySchema(schema)
                && !ModelUtils.isMapSchema(schema)
                && !ModelUtils.isComposedSchema(schema)
                && schema.getEnum() == null);
    }

    /**
     * Remove characters not suitable for variable or method name from the input and camelize it
     *
     * @param name string to be camelize
     * @return camelized string
     */
    @SuppressWarnings("static-method")
    public String removeNonNameElementToCamelCase(String name) {
        return removeNonNameElementToCamelCase(name, "[-_:;#" + removeOperationIdPrefixDelimiter + "]");
    }

    /**
     * Remove characters that is not good to be included in method name from the input and camelize it
     *
     * @param name                  string to be camelize
     * @param nonNameElementPattern a regex pattern of the characters that is not good to be included in name
     * @return camelized string
     */
    protected String removeNonNameElementToCamelCase(final String name, final String nonNameElementPattern) {
        String result = Arrays.stream(name.split(nonNameElementPattern))
                .map(StringUtils::capitalize)
                .collect(Collectors.joining(""));
        if (result.length() > 0) {
            result = result.substring(0, 1).toLowerCase(Locale.ROOT) + result.substring(1);
        }
        return result;
    }

    @Override
    public String apiFilename(String templateName, String tag) {
        String suffix = apiTemplateFiles().get(templateName);
        return apiFileFolder() + File.separator + toApiFilename(tag) + suffix;
    }

    @Override
    public String schemaFilename(String templateName, String jsonPath) {
        String[] pathPieces = jsonPath.split("/");
        String suffix = modelTemplateFiles().get(templateName);
        if (jsonPath.startsWith("#/components/schemas/") && pathPieces.length == 4) {
            return modelFileFolder() + File.separator + toModelFilename(pathPieces[3]) + suffix;
        }
        return null;
    }

    /**
     * Return the full path and API documentation file
     *
     * @param templateName template name
     * @param tag          tag
     * @return the API documentation file name with full path
     */
    @Override
    public String apiDocFilename(String templateName, String tag) {
        String docExtension = getDocExtension();
        String suffix = docExtension != null ? docExtension : apiDocTemplateFiles().get(templateName);
        return apiDocFileFolder() + File.separator + toApiDocFilename(tag) + suffix;
    }

    /**
     * Return the full path and API test file
     *
     * @param templateName template name
     * @param tag          tag
     * @return the API test file name with full path
     */
    @Override
    public String apiTestFilename(String templateName, String tag) {
        String suffix = apiTestTemplateFiles().get(templateName);
        return apiTestFileFolder() + File.separator + toApiTestFilename(tag) + suffix;
    }

    @Override
    public boolean shouldOverwrite(String filename) {
        return !(skipOverwrite && new File(filename).exists());
    }

    @Override
    public boolean isSkipOverwrite() {
        return skipOverwrite;
    }

    @Override
    public void setSkipOverwrite(boolean skipOverwrite) {
        this.skipOverwrite = skipOverwrite;
    }

    @Override
    public boolean isRemoveOperationIdPrefix() {
        return removeOperationIdPrefix;
    }

    @Override
    public boolean isSkipOperationExample() {
        return skipOperationExample;
    }

    @Override
    public void setRemoveOperationIdPrefix(boolean removeOperationIdPrefix) {
        this.removeOperationIdPrefix = removeOperationIdPrefix;
    }

    public String getRemoveOperationIdPrefixDelimiter() {
        return removeOperationIdPrefixDelimiter;
    }

    public void setRemoveOperationIdPrefixDelimiter(String removeOperationIdPrefixDelimiter) {
        this.removeOperationIdPrefixDelimiter = removeOperationIdPrefixDelimiter;
    }

    public int getRemoveOperationIdPrefixCount() {
        return removeOperationIdPrefixCount;
    }

    public void setRemoveOperationIdPrefixCount(int removeOperationIdPrefixCount) {
        this.removeOperationIdPrefixCount = removeOperationIdPrefixCount;
    }

    @Override
    public void setSkipOperationExample(boolean skipOperationExample) {
        this.skipOperationExample = skipOperationExample;
    }

    @Override
    public boolean isHideGenerationTimestamp() {
        return hideGenerationTimestamp;
    }

    @Override
    public void setHideGenerationTimestamp(boolean hideGenerationTimestamp) {
        this.hideGenerationTimestamp = hideGenerationTimestamp;
    }

    /**
     * All library templates supported.
     * (key: library name, value: library description)
     *
     * @return the supported libraries
     */
    @Override
    public Map<String, String> supportedLibraries() {
        return supportedLibraries;
    }

    /**
     * Set library template (sub-template).
     *
     * @param library Library template
     */
    @Override
    public void setLibrary(String library) {
        if (library != null && !supportedLibraries.containsKey(library)) {
            StringBuilder sb = new StringBuilder("Unknown library: " + library + "\nAvailable libraries:");
            if (supportedLibraries.size() == 0) {
                sb.append("\n  ").append("NONE");
            } else {
                for (String lib : supportedLibraries.keySet()) {
                    sb.append("\n  ").append(lib);
                }
            }
            throw new RuntimeException(sb.toString());
        }
        this.library = library;
    }

    /**
     * Library template (sub-template).
     *
     * @return Library template
     */
    @Override
    public String getLibrary() {
        return library;
    }

    /**
     * check if current active library equals to passed
     *
     * @param library - library to be compared with
     * @return {@code true} if passed library is active, {@code false} otherwise
     */
    public final boolean isLibrary(String library) {
        return library.equals(this.library);
    }

    /**
     * Set Git host.
     *
     * @param gitHost Git host
     */
    @Override
    public void setGitHost(String gitHost) {
        this.gitHost = gitHost;
    }

    /**
     * Git host.
     *
     * @return Git host
     */
    @Override
    public String getGitHost() {
        return gitHost;
    }

    /**
     * Set Git user ID.
     *
     * @param gitUserId Git user ID
     */
    @Override
    public void setGitUserId(String gitUserId) {
        this.gitUserId = gitUserId;
    }

    /**
     * Git user ID
     *
     * @return Git user ID
     */
    @Override
    public String getGitUserId() {
        return gitUserId;
    }

    /**
     * Set Git repo ID.
     *
     * @param gitRepoId Git repo ID
     */
    @Override
    public void setGitRepoId(String gitRepoId) {
        this.gitRepoId = gitRepoId;
    }

    /**
     * Git repo ID
     *
     * @return Git repo ID
     */
    @Override
    public String getGitRepoId() {
        return gitRepoId;
    }

    /**
     * Set release note.
     *
     * @param releaseNote Release note
     */
    @Override
    public void setReleaseNote(String releaseNote) {
        this.releaseNote = releaseNote;
    }

    /**
     * Release note
     *
     * @return Release note
     */
    @Override
    public String getReleaseNote() {
        return releaseNote;
    }

    /**
     * Documentation files extension
     *
     * @return Documentation files extension
     */
    @Override
    public String getDocExtension() {
        return docExtension;
    }

    /**
     * Set Documentation files extension
     *
     * @param userDocExtension documentation files extension
     */
    @Override
    public void setDocExtension(String userDocExtension) {
        this.docExtension = userDocExtension;
    }

    /**
     * Set HTTP user agent.
     *
     * @param httpUserAgent HTTP user agent
     */
    @Override
    public void setHttpUserAgent(String httpUserAgent) {
        this.httpUserAgent = httpUserAgent;
    }

    /**
     * HTTP user agent
     *
     * @return HTTP user agent
     */
    @Override
    public String getHttpUserAgent() {
        return httpUserAgent;
    }

    @SuppressWarnings("static-method")
    protected CliOption buildLibraryCliOption(Map<String, String> supportedLibraries) {
        StringBuilder sb = new StringBuilder("library template (sub-template) to use:");
        for (String lib : supportedLibraries.keySet()) {
            sb.append("\n").append(lib).append(" - ").append(supportedLibraries.get(lib));
        }
        return new CliOption(CodegenConstants.LIBRARY, sb.toString());
    }

    /**
     * Sanitize name (parameter, property, method, etc)
     *
     * @param name string to be sanitize
     * @return sanitized string
     */
    @Override
    @SuppressWarnings("static-method")
    public String sanitizeName(String name) {
        return sanitizeName(name, "\\W");
    }

    @Override
    public void setTemplatingEngine(TemplatingEngineAdapter templatingEngine) {
        this.templatingEngine = templatingEngine;
    }

    @Override
    public TemplatingEngineAdapter getTemplatingEngine() {
        return this.templatingEngine;
    }

    /**
     * Sanitize name (parameter, property, method, etc)
     *
     * @param name            string to be sanitize
     * @param removeCharRegEx a regex containing all char that will be removed
     * @return sanitized string
     */
    public String sanitizeName(String name, String removeCharRegEx) {
        return sanitizeName(name, removeCharRegEx, new ArrayList<>());
    }

    /**
     * Sanitize name (parameter, property, method, etc)
     *
     * @param name            string to be sanitize
     * @param removeCharRegEx a regex containing all char that will be removed
     * @param exceptionList   a list of matches which should not be sanitized (i.e exception)
     * @return sanitized string
     */
    @SuppressWarnings("static-method")
    public String sanitizeName(final String name, String removeCharRegEx, ArrayList<String> exceptionList) {
        // NOTE: performance wise, we should have written with 2 replaceAll to replace desired
        // character with _ or empty character. Below aims to spell out different cases we've
        // encountered so far and hopefully make it easier for others to add more special
        // cases in the future.

        // better error handling when map/array type is invalid
        if (name == null) {
            LOGGER.error("String to be sanitized is null. Default to ERROR_UNKNOWN");
            return "ERROR_UNKNOWN";
        }

        // if the name is just '$', map it to 'value' for the time being.
        if ("$".equals(name)) {
            return "value";
        }

        SanitizeNameOptions opts = new SanitizeNameOptions(name, removeCharRegEx, exceptionList);

        return sanitizedNameCache.get(opts, sanitizeNameOptions -> {
            String modifiable = sanitizeNameOptions.getName();
            List<String> exceptions = sanitizeNameOptions.getExceptions();
            // input[] => input
            modifiable = this.sanitizeValue(modifiable, "\\[\\]", "", exceptions);

            // input[a][b] => input_a_b
            modifiable = this.sanitizeValue(modifiable, "\\[", "_", exceptions);
            modifiable = this.sanitizeValue(modifiable, "\\]", "", exceptions);

            // input(a)(b) => input_a_b
            modifiable = this.sanitizeValue(modifiable, "\\(", "_", exceptions);
            modifiable = this.sanitizeValue(modifiable, "\\)", "", exceptions);

            // input.name => input_name
            modifiable = this.sanitizeValue(modifiable, "\\.", "_", exceptions);

            // input-name => input_name
            modifiable = this.sanitizeValue(modifiable, "-", "_", exceptions);

            // a|b => a_b
            modifiable = this.sanitizeValue(modifiable, "\\|", "_", exceptions);

            // input name and age => input_name_and_age
            modifiable = this.sanitizeValue(modifiable, " ", "_", exceptions);

            // /api/films/get => _api_films_get
            // \api\films\get => _api_films_get
            modifiable = modifiable.replaceAll("/", "_");
            modifiable = modifiable.replaceAll("\\\\", "_");

            // remove everything else other than word, number and _
            // $php_variable => php_variable
            if (allowUnicodeIdentifiers) { //could be converted to a single line with ?: operator
                modifiable = Pattern.compile(sanitizeNameOptions.getRemoveCharRegEx(), Pattern.UNICODE_CHARACTER_CLASS).matcher(modifiable).replaceAll("");
            } else {
                modifiable = modifiable.replaceAll(sanitizeNameOptions.getRemoveCharRegEx(), "");
            }
            return modifiable;
        });
    }

    private String sanitizeValue(String value, String replaceMatch, String replaceValue, List<String> exceptionList) {
        if (exceptionList.size() == 0 || !exceptionList.contains(replaceMatch)) {
            return value.replaceAll(replaceMatch, replaceValue);
        }
        return value;
    }

    /**
     * Sanitize tag
     *
     * @param tag Tag
     * @return Sanitized tag
     */
    @Override
    public String sanitizeTag(String tag) {
        tag = camelize(sanitizeName(tag));

        // tag starts with numbers
        if (tag.matches("^\\d.*")) {
            tag = "Class" + tag;
        }

        return tag;
    }

    /**
     * Update codegen property's enum by adding "enumVars" (with name and value)
     *
     * @param var list of CodegenSchema
     */
    public void updateCodegenPropertyEnum(CodegenSchema var) {
        Map<String, Object> allowableValues = var.allowableValues;

        if (allowableValues == null) {
            return;
        }

        List<Object> values = (List<Object>) allowableValues.get("values");
        if (values == null) {
            return;
        }

        Optional<Schema> referencedSchema = ModelUtils.getSchemas(openAPI).entrySet().stream()
                .filter(entry -> Objects.equals(var.refClass, toModelName(entry.getKey())))
                .map(Map.Entry::getValue)
                .findFirst();
        List<Map<String, Object>> enumVars = buildEnumVars(values, var);

        // if "x-enum-varnames" or "x-enum-descriptions" defined, update varnames
        Map<String, Object> extensions = var.getVendorExtensions();
        if (referencedSchema.isPresent()) {
            extensions = referencedSchema.get().getExtensions();
        }
        updateEnumVarsWithExtensions(enumVars, extensions, var);
        allowableValues.put("enumVars", enumVars);

        // handle default value for enum, e.g. available => StatusEnum.AVAILABLE
        if (var.defaultValue != null) {
            final String enumDefaultValue = getEnumDefaultValue(var.defaultValue, var);

            String enumName = null;
            for (Map<String, Object> enumVar : enumVars) {
                if (enumDefaultValue.equals(enumVar.get("value"))) {
                    enumName = (String) enumVar.get("name");
                    break;
                }
            }
            if (enumName != null) {
                var.defaultValue = toEnumDefaultValue(enumName, var);
            }
        }
    }

    protected String getEnumDefaultValue(String defaultValue, CodegenSchema prop) {
        final String enumDefaultValue;
        if (prop.isString) {
            enumDefaultValue = toEnumValue(defaultValue, prop);
        } else {
            enumDefaultValue = defaultValue;
        }
        return enumDefaultValue;
    }

    protected List<Map<String, Object>> buildEnumVars(List<Object> values, CodegenSchema prop) {
        List<Map<String, Object>> enumVars = new ArrayList<>();
        int truncateIdx = 0;

        if (isRemoveEnumValuePrefix()) {
            String commonPrefix = findCommonPrefixOfVars(values);
            truncateIdx = commonPrefix.length();
        }

        for (Object value : values) {
            Map<String, Object> enumVar = new HashMap<>();
            String enumName;
            if (truncateIdx == 0) {
                enumName = String.valueOf(value);
            } else {
                enumName = value.toString().substring(truncateIdx);
                if (enumName.isEmpty()) {
                    enumName = value.toString();
                }
            }

            enumVar.put("name", toEnumVarName(enumName, prop));
            enumVar.put("value", toEnumValue(String.valueOf(value), prop));
            enumVar.put("isString", prop.isString);
            enumVars.add(enumVar);
        }

        if (enumUnknownDefaultCase) {
            // If the server adds new enum cases, that are unknown by an old spec/client, the client will fail to parse the network response.
            // With this option enabled, each enum will have a new case, 'unknown_default_open_api', so that when the server sends an enum case that is not known by the client/spec, they can safely fallback to this case.
            Map<String, Object> enumVar = new HashMap<>();
            String enumName = enumUnknownDefaultCaseName;

            String enumValue;
            if (prop.isString) {
                enumValue = enumUnknownDefaultCaseName;
            } else {
                // This is a dummy value that attempts to avoid collisions with previously specified cases.
                // Int.max / 192
                // The number 192 that is used to calculate this random value, is the Swift Evolution proposal for frozen/non-frozen enums.
                // [SE-0192](https://github.com/apple/swift-evolution/blob/master/proposals/0192-non-exhaustive-enums.md)
                // Since this functionality was born in the Swift 5 generator and latter on broth to all generators
                // https://github.com/OpenAPITools/openapi-generator/pull/11013
                enumValue = String.valueOf(11184809);
            }

            enumVar.put("name", toEnumVarName(enumName, prop));
            enumVar.put("value", toEnumValue(enumValue, prop));
            enumVar.put("isString", prop.isString);
            enumVars.add(enumVar);
        }

        return enumVars;
    }

    protected void updateEnumVarsWithExtensions(List<Map<String, Object>> enumVars, Map<String, Object> vendorExtensions, CodegenSchema prop) {
        if (vendorExtensions != null) {
            updateEnumVarsWithExtensions(enumVars, vendorExtensions, "x-enum-varnames", "name");
            updateEnumVarsWithExtensions(enumVars, vendorExtensions, "x-enum-descriptions", "enumDescription");
        }
    }

    private void updateEnumVarsWithExtensions(List<Map<String, Object>> enumVars, Map<String, Object> vendorExtensions, String extensionKey, String key) {
        if (vendorExtensions.containsKey(extensionKey)) {
            List<String> values = (List<String>) vendorExtensions.get(extensionKey);
            int size = Math.min(enumVars.size(), values.size());
            for (int i = 0; i < size; i++) {
                enumVars.get(i).put(key, values.get(i));
            }
        }
    }

    /**
     * If the pattern misses the delimiter, add "/" to the beginning and end
     * Otherwise, return the original pattern
     *
     * @param pattern the pattern (regular expression)
     * @return the pattern with delimiter
     */
    public String addRegularExpressionDelimiter(String pattern) {
        if (StringUtils.isEmpty(pattern)) {
            return pattern;
        }

        if (!pattern.matches("^/.*")) {
            return "/" + pattern.replaceAll("/", "\\\\/") + "/";
        }

        return pattern;
    }

    /**
     * reads propertyKey from additionalProperties, converts it to a boolean and
     * writes it back to additionalProperties to be usable as a boolean in
     * mustache files.
     *
     * @param propertyKey property key
     * @return property value as boolean
     */
    public boolean convertPropertyToBooleanAndWriteBack(String propertyKey) {
        boolean result = convertPropertyToBoolean(propertyKey);
        writePropertyBack(propertyKey, result);
        return result;
    }

    /**
     * Provides an override location, if any is specified, for the .openapi-generator-ignore.
     * <p>
     * This is originally intended for the first generation only.
     *
     * @return a string of the full path to an override ignore file.
     */
    @Override
    public String getIgnoreFilePathOverride() {
        return ignoreFilePathOverride;
    }

    /**
     * Sets an override location for the '.openapi-generator-ignore' location for the first code generation.
     *
     * @param ignoreFileOverride The full path to an ignore file
     */
    @Override
    public void setIgnoreFilePathOverride(final String ignoreFileOverride) {
        this.ignoreFilePathOverride = ignoreFileOverride;
    }

    public boolean convertPropertyToBoolean(String propertyKey) {
        final Object booleanValue = additionalProperties.get(propertyKey);
        boolean result = Boolean.FALSE;
        if (booleanValue instanceof Boolean) {
            result = (Boolean) booleanValue;
        } else if (booleanValue instanceof String) {
            result = Boolean.parseBoolean((String) booleanValue);
        } else {
            LOGGER.warn("The value (generator's option) must be either boolean or string. Default to `false`.");
        }
        return result;
    }

    public void writePropertyBack(String propertyKey, boolean value) {
        additionalProperties.put(propertyKey, value);
    }

    private void setOauth2Info(CodegenSecurity codegenSecurity, OAuthFlow flow) {
        codegenSecurity.authorizationUrl = flow.getAuthorizationUrl();
        codegenSecurity.tokenUrl = flow.getTokenUrl();
        codegenSecurity.refreshUrl = flow.getRefreshUrl();

        if (flow.getScopes() != null && !flow.getScopes().isEmpty()) {
            List<Map<String, Object>> scopes = new ArrayList<>();
            for (Map.Entry<String, String> scopeEntry : flow.getScopes().entrySet()) {
                Map<String, Object> scope = new HashMap<>();
                scope.put("scope", scopeEntry.getKey());
                scope.put("description", escapeText(scopeEntry.getValue()));
                scopes.add(scope);
            }
            codegenSecurity.scopes = scopes;
        }
    }

    private void addConsumesInfo(Operation operation, CodegenOperation codegenOperation) {
        RequestBody requestBody = ModelUtils.getReferencedRequestBody(this.openAPI, operation.getRequestBody());
        if (requestBody == null || requestBody.getContent() == null || requestBody.getContent().isEmpty()) {
            return;
        }

        Set<String> consumes = requestBody.getContent().keySet();
        List<Map<String, String>> mediaTypeList = new ArrayList<>();
        for (String key : consumes) {
            Map<String, String> mediaType = new HashMap<>();
            if ("*/*".equals(key)) {
                // skip as it implies `consumes` in OAS2 is not defined
                continue;
            } else {
                mediaType.put("mediaType", escapeQuotationMark(key));
            }
            mediaTypeList.add(mediaType);
        }

        if (!mediaTypeList.isEmpty()) {
            codegenOperation.consumes = mediaTypeList;
            codegenOperation.hasConsumes = true;
        }
    }

    public static Set<String> getConsumesInfo(OpenAPI openAPI, Operation operation) {
        RequestBody requestBody = ModelUtils.getReferencedRequestBody(openAPI, operation.getRequestBody());

        if (requestBody == null || requestBody.getContent() == null || requestBody.getContent().isEmpty()) {
            return Collections.emptySet(); // return empty set
        }
        return requestBody.getContent().keySet();
    }

    public boolean hasFormParameter(OpenAPI openAPI, Operation operation) {
        Set<String> consumesInfo = getConsumesInfo(openAPI, operation);

        if (consumesInfo == null || consumesInfo.isEmpty()) {
            return false;
        }

        for (String consume : consumesInfo) {
            if (consume != null &&
                    (consume.toLowerCase(Locale.ROOT).startsWith("application/x-www-form-urlencoded") ||
                            consume.toLowerCase(Locale.ROOT).startsWith("multipart"))) {
                return true;
            }
        }

        return false;
    }

    public boolean hasBodyParameter(OpenAPI openAPI, Operation operation) {
        RequestBody requestBody = ModelUtils.getReferencedRequestBody(openAPI, operation.getRequestBody());
        if (requestBody == null) {
            return false;
        }

        Schema schema = ModelUtils.getSchemaFromRequestBody(requestBody);
        return ModelUtils.getReferencedSchema(openAPI, schema) != null;
    }

    private void addProducesInfo(ApiResponse inputResponse, CodegenOperation codegenOperation) {
        ApiResponse response = ModelUtils.getReferencedApiResponse(this.openAPI, inputResponse);
        if (response == null || response.getContent() == null || response.getContent().isEmpty()) {
            return;
        }

        Set<String> produces = response.getContent().keySet();
        if (codegenOperation.produces == null) {
            codegenOperation.produces = new ArrayList<>();
        }

        Set<String> existingMediaTypes = new HashSet<>();
        for (Map<String, String> mediaType : codegenOperation.produces) {
            existingMediaTypes.add(mediaType.get("mediaType"));
        }

        for (String key : produces) {
            // escape quotation to avoid code injection, "*/*" is a special case, do nothing
            String encodedKey = "*/*".equals(key) ? key : escapeQuotationMark(key);
            //Only unique media types should be added to "produces"
            if (!existingMediaTypes.contains(encodedKey)) {
                Map<String, String> mediaType = new HashMap<>();
                mediaType.put("mediaType", encodedKey);
                codegenOperation.produces.add(mediaType);
                codegenOperation.hasProduces = Boolean.TRUE;
            }
        }
    }

    /**
     * returns the list of MIME types the APIs can produce
     *
     * @param openAPI   current specification instance
     * @param operation Operation
     * @return a set of MIME types
     */
    public static Set<String> getProducesInfo(final OpenAPI openAPI, final Operation operation) {
        if (operation.getResponses() == null || operation.getResponses().isEmpty()) {
            return null;
        }

        Set<String> produces = new ConcurrentSkipListSet<>();

        for (ApiResponse r : operation.getResponses().values()) {
            ApiResponse response = ModelUtils.getReferencedApiResponse(openAPI, r);
            if (response.getContent() != null) {
                produces.addAll(response.getContent().keySet());
            }
        }

        return produces;
    }

    @Override
    public CodegenType getTag() {
        return null;
    }

    @Override
    public String getName() {
        return null;
    }

    @Override
    public String getHelp() {
        return null;
    }

    protected void addBodyModelSchema(CodegenParameter codegenParameter, String name, Schema schema, Set<String> imports, String bodyParameterName, boolean forceSimpleRef, String sourceJsonPath) {
        CodegenSchema codegenModel = null;
        if (StringUtils.isNotBlank(name)) {
            schema.setName(name);
            String path = "#/components/schemas/" + name;
            codegenModel = fromSchema(schema, path, path);
        }

        if (codegenModel != null && (codegenModel.getProperties() != null || forceSimpleRef)) {
            if (StringUtils.isEmpty(bodyParameterName)) {
                codegenParameter.baseName = codegenModel.name.getCamelCaseName();
            } else {
                codegenParameter.baseName = bodyParameterName;
            }
            codegenParameter.paramName = toParamName(codegenParameter.baseName);
            codegenParameter.description = codegenModel.description;
        } else {
            CodegenSchema codegenSchema = fromSchema(schema, sourceJsonPath, sourceJsonPath);

            if (codegenSchema != null && codegenSchema.getRefClass() != null && codegenSchema.getRefClass().contains(" | ")) {
                if (!addSchemaImportsFromV3SpecLocations) {
                    // TODO move this splitting logic to the generator that needs it only
                    List<String> parts = Arrays.asList(codegenSchema.getRefClass().split(" \\| "));
                    imports.addAll(parts);
                }
                String codegenModelName = codegenSchema.getRefClass();
                codegenParameter.baseName = codegenModelName;
                codegenParameter.paramName = toParamName(codegenParameter.baseName);
                codegenParameter.description = codegenSchema.getDescription();
            } else {
                if (ModelUtils.isMapSchema(schema)) {// http body is map
                    LOGGER.error("Map should be supported. Please report to openapi-generator github repo about the issue.");
                } else if (codegenSchema != null) {
                    String codegenModelName, codegenModelDescription;

                    if (codegenModel != null) {
                        codegenModelName = codegenModel.name.getCamelCaseName();
                        codegenModelDescription = codegenModel.description;
                    } else {
                        LOGGER.warn("The following schema has undefined (null) baseType. " +
                                "It could be due to form parameter defined in OpenAPI v2 spec with incorrect consumes. " +
                                "A correct 'consumes' for form parameters should be " +
                                "'application/x-www-form-urlencoded' or 'multipart/?'");
                        LOGGER.warn("schema: {}", schema);
                        LOGGER.warn("codegenModel is null. Default to UNKNOWN_BASE_TYPE");
                        codegenModelName = "UNKNOWN_BASE_TYPE";
                        codegenModelDescription = "UNKNOWN_DESCRIPTION";
                    }

                    if (StringUtils.isEmpty(bodyParameterName)) {
                        codegenParameter.baseName = codegenModelName;
                    } else {
                        codegenParameter.baseName = bodyParameterName;
                    }

                    codegenParameter.paramName = toParamName(codegenParameter.baseName);
                    codegenParameter.description = codegenModelDescription;
                    if (!addSchemaImportsFromV3SpecLocations) {
                        if (codegenSchema.refClass != null) {
                            imports.add(codegenSchema.refClass);
                        }
                    }
                }
            }

        }
    }

    protected void updateRequestBodyForMap(CodegenParameter codegenParameter, Schema schema, String name, Set<String> imports, String bodyParameterName, String sourceJsonPath) {
        if (StringUtils.isNotBlank(name)) {
            this.addBodyModelSchema(codegenParameter, name, schema, imports, bodyParameterName, true, sourceJsonPath);
        } else {
            Schema inner = getAdditionalProperties(schema);
            if (inner == null) {
                LOGGER.error("No inner type supplied for map parameter `{}`. Default to type:string", schema.getName());
                inner = new StringSchema().description("//TODO automatically added by openapi-generator");
                schema.setAdditionalProperties(inner);
            }
            CodegenSchema codegenSchema = fromSchema(schema, sourceJsonPath, sourceJsonPath);

            if (!addSchemaImportsFromV3SpecLocations) {
                CodegenSchema innerCp = codegenSchema;
                while (innerCp != null) {
                    if (innerCp.refClass != null) {
                        imports.add(innerCp.refClass);
                    }
                    innerCp = innerCp.items;
                }
            }

            if (StringUtils.isEmpty(bodyParameterName)) {
                codegenParameter.baseName = "request_body";
            } else {
                codegenParameter.baseName = bodyParameterName;
            }
            codegenParameter.paramName = toParamName(codegenParameter.baseName);
        }
    }

    protected void updateRequestBodyForPrimitiveType(CodegenParameter codegenParameter, Schema schema, String bodyParameterName, Set<String> imports, String sourceJsonPath) {
        CodegenSchema codegenSchema = fromSchema(schema, sourceJsonPath, sourceJsonPath);
        if (codegenSchema != null) {
            if (StringUtils.isEmpty(bodyParameterName)) {
                codegenParameter.baseName = "body";  // default to body
            } else {
                codegenParameter.baseName = bodyParameterName;
            }
            codegenParameter.description = codegenSchema.description;
            codegenParameter.paramName = toParamName(codegenParameter.baseName);

            if (!addSchemaImportsFromV3SpecLocations) {
                if (codegenSchema.refClass != null) {
                    imports.add(codegenSchema.refClass);
                }
            }
        }
    }

    protected void updateRequestBodyForObject(CodegenParameter codegenParameter, Schema schema, String name, Set<String> imports, String bodyParameterName, String sourceJsonPath) {
        if (ModelUtils.isMapSchema(schema)) {
            // Schema with additionalproperties: true (including composed schemas with additionalproperties: true)
            updateRequestBodyForMap(codegenParameter, schema, name, imports, bodyParameterName, sourceJsonPath);
        } else if (ModelUtils.isObjectSchema(schema)) {
            // object type schema or composed schema with properties defined
            this.addBodyModelSchema(codegenParameter, name, schema, imports, bodyParameterName, false, sourceJsonPath);
        }
    }

    protected void updateRequestBodyForArray(CodegenParameter codegenParameter, Schema schema, String name, Set<String> imports, String bodyParameterName, String sourceJsonPath) {
        if (StringUtils.isNotBlank(name)) {
            this.addBodyModelSchema(codegenParameter, name, schema, imports, bodyParameterName, true, sourceJsonPath);
        } else {
            final ArraySchema arraySchema = (ArraySchema) schema;
            CodegenSchema codegenSchema = fromSchema(arraySchema, sourceJsonPath, sourceJsonPath);
            if (codegenSchema == null) {
               throw new RuntimeException("CodegenSchema cannot be null. arraySchema for debugging: " + arraySchema);
            }

            CodegenSchema innerCp = codegenSchema;
            CodegenSchema mostInnerItem = innerCp;
            // loop through multidimensional array to add proper import
            // also find the most inner item
            while (innerCp != null) {
                if (!addSchemaImportsFromV3SpecLocations) {
                    if (innerCp.refClass != null) {
                        imports.add(innerCp.refClass);
                    }
                }
                mostInnerItem = innerCp;
                innerCp = innerCp.items;
            }

            if (mostInnerItem == null) {
                throw new RuntimeException("mostInnerItem (codegen property of array item) cannot be null. " + arraySchema);
            }

            if (StringUtils.isEmpty(bodyParameterName)) {
                if (StringUtils.isEmpty(mostInnerItem.refClass)) {
                    codegenParameter.baseName = "request_body";
                } else {
                    codegenParameter.baseName = mostInnerItem.refClass;
                }
            } else {
                codegenParameter.baseName = bodyParameterName;
            }
            codegenParameter.paramName = toArrayModelParamName(codegenParameter.baseName);
        }
    }

    protected void updateRequestBodyForString(CodegenParameter codegenParameter, Schema schema, Set<String> imports, String bodyParameterName, String sourceJsonPath) {
        updateRequestBodyForPrimitiveType(codegenParameter, schema, bodyParameterName, imports, sourceJsonPath);
    }

    protected LinkedHashMap<String, CodegenMediaType> getContent(Content content, Set<String> imports, String schemaName, String sourceJsonPath) {
        if (content == null) {
            return null;
        }
        LinkedHashMap<String, CodegenMediaType> cmtContent = new LinkedHashMap<>();
        for (Entry<String, MediaType> contentEntry : content.entrySet()) {
            String contentType = contentEntry.getKey();
            MediaType mt = contentEntry.getValue();
            LinkedHashMap<String, CodegenEncoding> ceMap = null;
            if (mt.getEncoding() != null) {
                ceMap = new LinkedHashMap<>();
                Map<String, Encoding> encMap = mt.getEncoding();
                for (Entry<String, Encoding> encodingEntry : encMap.entrySet()) {
                    String encodingPropertyName = encodingEntry.getKey();
                    Encoding enc = encodingEntry.getValue();
                    Map<String, CodegenHeader> headers = new HashMap<>();
                    if (enc.getHeaders() != null) {
                        Map<String, Header> encHeaders = enc.getHeaders();
                        for (Entry<String, Header> headerEntry : encHeaders.entrySet()) {
                            String headerName = headerEntry.getKey();
                            Header header = headerEntry.getValue();
                            String usedSourceJsonPath = sourceJsonPath + "/" + ModelUtils.encodeSlashes(contentType) + "/encoding/" + encodingPropertyName + "/headers/" + headerName;
                            CodegenHeader codegenHeader = fromHeader(header, usedSourceJsonPath);
                            headers.put(headerName, codegenHeader);
                        }
                    }
                    CodegenEncoding ce = new CodegenEncoding(
                            enc.getContentType(),
                            headers,
                            enc.getStyle().toString(),
                            enc.getExplode() == null ? false : enc.getExplode().booleanValue(),
                            enc.getAllowReserved() == null ? false : enc.getAllowReserved().booleanValue()
                    );
                    ceMap.put(encodingPropertyName, ce);
                }
            }
            CodegenSchema schemaProp = null;
            String usedSchemaName = schemaName;
            if (usedSchemaName.equals("")) {
                usedSchemaName = contentType;
            }
            if (mt.getSchema() != null) {
                String usedSourceJsonPath = sourceJsonPath + "/" + ModelUtils.encodeSlashes(contentType) + "/schema";
                schemaProp = fromSchema(mt.getSchema(), usedSourceJsonPath, usedSourceJsonPath);
            }
            HashMap<String, SchemaTestCase> schemaTestCases = null;
            if (mt.getExtensions() != null && mt.getExtensions().containsKey(xSchemaTestExamplesKey)) {
                Object objNodeWithRef = mt.getExtensions().get(xSchemaTestExamplesKey);
                if (objNodeWithRef instanceof LinkedHashMap) {
                    LinkedHashMap<String, String> nodeWithRef = (LinkedHashMap<String, String>) objNodeWithRef;
                    String refKey = "$ref";
                    String refToTestCases = nodeWithRef.getOrDefault(refKey, null);
                    if (refToTestCases != null) {
                        schemaTestCases = extractSchemaTestCases(refToTestCases);
                    }
                }
            }

            CodegenMediaType codegenMt = new CodegenMediaType(schemaProp, ceMap, schemaTestCases);
            cmtContent.put(contentType, codegenMt);
            if (schemaProp != null) {
                if (addSchemaImportsFromV3SpecLocations) {
                    addImports(imports, getImports(schemaProp, generatorMetadata.getFeatureSet()));
                }
            }
        }
        return cmtContent;
    }

    private String toRequestBodyFileName(String name) {
        return toModuleFilename(name) + "_request_body";
    }

    protected String toRefModule(String ref, String expectedComponentType, String sourceJsonPath) {
        // ref #/components/schemas/SomeModel -> some_model
        // ref #/components/requestBodies/SomeBody -> some_body
        // ref #/components/parameters/SomeParam -> some_param
        // ref #/components/headers/SomeHeader -> some_header

        String[] refPieces = ref.split("/");
        if (!ref.startsWith("#/components/")) {
            throw new RuntimeException("The ref must be to a component");
        }
        if (refPieces.length != 4) {
            throw new RuntimeException("The ref must be to a named key in one of the components");
        }
        if (!refPieces[2].equals(expectedComponentType)) {
            throw new RuntimeException("Incorrect component type in ref, expected "+expectedComponentType+" and saw "+refPieces[2]);
        }
        switch (expectedComponentType) {
            case "requestBodies":
                return toRequestBodyFileName(refPieces[3]);
            case "responses":
                return toResponseModuleName(refPieces[3]);
            case "headers":
                return toHeaderFilename(refPieces[3]);
            case "parameters":
                return toParameterFilename(refPieces[3]);
            case "schemas":
                if (ref.equals(sourceJsonPath)) {
                    // property is of type self
                    return null;
                }
                return toModelFilename(refPieces[3]);
        }
        return null;
    }

    public CodegenParameter fromRequestBody(RequestBody body, String bodyParameterName, String sourceJsonPath) {
        // process body parameter
        RequestBody usedBody = body;
        String usedSourceJsonPath = sourceJsonPath;
        String bodyRef = body.get$ref();
        if (bodyRef != null) {
            usedBody = ModelUtils.getReferencedRequestBody(this.openAPI, body);
            usedSourceJsonPath = bodyRef;
        }
        if (usedBody == null) {
            LOGGER.error("body in fromRequestBody cannot be null!");
            throw new RuntimeException("body in fromRequestBody cannot be null!");
        }
        CodegenParameter codegenParameter = new CodegenParameter();
        if (sourceJsonPath != null) {
            String[] refPieces = sourceJsonPath.split("/");
            if (sourceJsonPath.startsWith("#/components/requestBodies/") && refPieces.length == 4) {
                String componentName = refPieces[3];
                codegenParameter.setComponentModule(toComponentModule(componentName, "requestBodies"));
            }
        }
        if (bodyRef != null) {
            String refModule = toRefModule(bodyRef, "requestBodies", sourceJsonPath);
            codegenParameter.setRefModule(refModule);
        }
        codegenParameter.baseName = "UNKNOWN_BASE_NAME";
        codegenParameter.paramName = "UNKNOWN_PARAM_NAME";
        codegenParameter.description = escapeText(usedBody.getDescription());
        codegenParameter.required = usedBody.getRequired() != null ? usedBody.getRequired() : Boolean.FALSE;
        codegenParameter.isBodyParam = Boolean.TRUE;
        if (bodyRef != null) {
            String refModule = toRefModule(bodyRef, "requestBodies", sourceJsonPath);
            codegenParameter.setRefModule(refModule);
        }
        if (usedBody.getExtensions() != null) {
            codegenParameter.vendorExtensions.putAll(usedBody.getExtensions());
        }

        String name = null;
        LOGGER.debug("Request body = {}", usedBody);
        Schema schema = ModelUtils.getSchemaFromRequestBody(usedBody);
        if (schema == null) {
            throw new RuntimeException("Request body cannot be null. Possible cause: missing schema in body parameter (OAS v2): " + usedBody);
        }
        codegenParameter.setContent(getContent(usedBody.getContent(), codegenParameter.imports, "", usedSourceJsonPath + "/content"));

        if (StringUtils.isNotBlank(schema.get$ref())) {
            name = ModelUtils.getSimpleRef(schema.get$ref());
        }

        Schema unaliasedSchema = unaliasSchema(schema);
        schema = ModelUtils.getReferencedSchema(this.openAPI, schema);

        // TODO in the future switch al the below schema usages to unaliasedSchema
        // because it keeps models as refs and will not get their referenced schemas
        String schemaSourceJsonPath = usedSourceJsonPath + "/schema";
        if (ModelUtils.isArraySchema(schema)) {
            updateRequestBodyForArray(codegenParameter, schema, name, codegenParameter.imports, bodyParameterName, schemaSourceJsonPath);
        } else if (ModelUtils.isTypeObjectSchema(schema)) {
            updateRequestBodyForObject(codegenParameter, schema, name, codegenParameter.imports, bodyParameterName, schemaSourceJsonPath);
        } else if (ModelUtils.isIntegerSchema(schema)) { // integer type
            updateRequestBodyForPrimitiveType(codegenParameter, schema, bodyParameterName, codegenParameter.imports, schemaSourceJsonPath);
        } else if (ModelUtils.isBooleanSchema(schema)) { // boolean type
            updateRequestBodyForPrimitiveType(codegenParameter, schema, bodyParameterName, codegenParameter.imports, schemaSourceJsonPath);
        } else if (ModelUtils.isFileSchema(schema) && !ModelUtils.isStringSchema(schema)) {
            // swagger v2 only, type file
        } else if (ModelUtils.isStringSchema(schema)) {
            updateRequestBodyForString(codegenParameter, schema, codegenParameter.imports, bodyParameterName, schemaSourceJsonPath);
        } else if (ModelUtils.isNumberSchema(schema)) {
            updateRequestBodyForPrimitiveType(codegenParameter, schema, bodyParameterName, codegenParameter.imports, schemaSourceJsonPath);
        } else if (ModelUtils.isNullType(schema)) {
            updateRequestBodyForPrimitiveType(codegenParameter, schema, bodyParameterName, codegenParameter.imports, schemaSourceJsonPath);
        } else if (ModelUtils.isAnyType(schema)) {
            if (ModelUtils.isMapSchema(schema)) {
                // Schema with additionalproperties: true (including composed schemas with additionalproperties: true)
                updateRequestBodyForMap(codegenParameter, schema, name, codegenParameter.imports, bodyParameterName, schemaSourceJsonPath);
            } else if (ModelUtils.isComposedSchema(schema)) {
                this.addBodyModelSchema(codegenParameter, name, schema, codegenParameter.imports, bodyParameterName, false, schemaSourceJsonPath);
            } else if (ModelUtils.isObjectSchema(schema)) {
                // object type schema OR (AnyType schema with properties defined)
                this.addBodyModelSchema(codegenParameter, name, schema, codegenParameter.imports, bodyParameterName, false, schemaSourceJsonPath);
            } else {
                updateRequestBodyForPrimitiveType(codegenParameter, schema, bodyParameterName, codegenParameter.imports, schemaSourceJsonPath);
            }
        } else {
            // referenced schemas
            updateRequestBodyForPrimitiveType(codegenParameter, schema, bodyParameterName, codegenParameter.imports, schemaSourceJsonPath);
        }


        addJsonSchemaForBodyRequestInCaseItsNotPresent(codegenParameter, usedBody);

        // set the parameter's example value
        // should be overridden by lang codegen
        setParameterExampleValue(codegenParameter, usedBody);

        return codegenParameter;
    }

    public CodegenKey getKey(String key) {
        String usedKey = handleSpecialCharacters(key);
        boolean isValid = isValid(usedKey);
        CodegenKey ck = new CodegenKey(
                usedKey,
                isValid,
                toVarName(usedKey),
                toModelName(usedKey)
        );
        return ck;
    }

    protected void addRequiredProperties(Schema schema, JsonSchema property, String sourceJsonPath, String currentJsonPath) {
        /*
        this should be called after vars and additionalProperties are set
        Features added by storing codegenProperty values:
        - refClass stores reference to additionalProperties definition
        - baseName stores original name (can be invalid in a programming language)
        - nameInSnakeCase can store valid name for a programming language
         */
        Map<String, Schema> properties = schema.getProperties();
        LinkedHashMap<CodegenKey, CodegenSchema> requiredProperties = new LinkedHashMap<>();
        List<String> requiredPropertyNames = schema.getRequired();
        if (requiredPropertyNames == null) {
            return;
        }
        for (String requiredPropertyName: requiredPropertyNames) {
            // required property is defined in properties, value is that CodegenSchema
            CodegenKey ck = getKey(requiredPropertyName);
            if (properties != null && properties.containsKey(requiredPropertyName)) {
                // get cp from property
                CodegenSchema cp = property.getProperties().get(ck);
                if (cp != null) {
                    requiredProperties.put(ck, cp);
                } else {
                    throw new RuntimeException("Property " + requiredPropertyName + " is missing from getVars");
                }
            } else if (schema.getAdditionalProperties() instanceof Boolean && Boolean.FALSE.equals(schema.getAdditionalProperties())) {
                // TODO add processing for requiredPropertyName
                // required property is not defined in properties, and additionalProperties is false, value is null
                requiredProperties.put(ck, null);
            } else {
                // required property is not defined in properties, and additionalProperties is true or unset value is CodegenSchema made from empty schema
                // required property is not defined in properties, and additionalProperties is schema, value is CodegenSchema made from schema
                if (supportsAdditionalPropertiesWithComposedSchema && !disallowAdditionalPropertiesIfNotPresent) {
                    CodegenSchema cp;
                    String addPropsJsonPath = currentJsonPath + "/additionalProperties";
                    if (schema.getAdditionalProperties() == null) {
                        // additionalProperties is null
                        // there is NO schema definition for this so the json paths are null
                        cp = fromSchema(new Schema(), null, null);
                    } else if (schema.getAdditionalProperties() instanceof Boolean && Boolean.TRUE.equals(schema.getAdditionalProperties())) {
                        // additionalProperties is True
                        cp = fromSchema(new Schema(), sourceJsonPath, addPropsJsonPath);
                    } else {
                        // additionalProperties is schema
                        cp = fromSchema((Schema) schema.getAdditionalProperties(), sourceJsonPath, addPropsJsonPath);
                    }
                    requiredProperties.put(ck, cp);
                }
            }
        }
        if (!requiredProperties.isEmpty()) {
            property.setRequiredProperties(requiredProperties);
        }
    }

    protected void addVarsRequiredVarsAdditionalProps(Schema schema, JsonSchema property, String sourceJsonPath, String currentJsonPath) {
        setAddProps(schema, property, sourceJsonPath, currentJsonPath);
        Set<String> mandatory = schema.getRequired() == null ? Collections.emptySet()
                : new TreeSet<>(schema.getRequired());
        addProperties(property, schema.getProperties(), mandatory, sourceJsonPath, currentJsonPath);
        addRequiredProperties(schema, property, sourceJsonPath, currentJsonPath);
    }

    private void addJsonSchemaForBodyRequestInCaseItsNotPresent(CodegenParameter codegenParameter, RequestBody body) {
        if (codegenParameter.jsonSchema == null)
            codegenParameter.jsonSchema = Json.pretty(body);
    }

    protected void addOption(String key, String description, String defaultValue) {
        CliOption option = new CliOption(key, description);
        if (defaultValue != null)
            option.defaultValue(defaultValue);
        cliOptions.add(option);
    }

    protected void updateOption(String key, String defaultValue) {
        for (CliOption cliOption : cliOptions) {
            if (cliOption.getOpt().equals(key)) {
                cliOption.setDefault(defaultValue);
                break;
            }
        }
    }

    protected void removeOption(String key) {
        for (int i = 0; i < cliOptions.size(); i++) {
            if (key.equals(cliOptions.get(i).getOpt())) {
                cliOptions.remove(i);
                break;
            }
        }
    }

    protected void addSwitch(String key, String description, Boolean defaultValue) {
        CliOption option = CliOption.newBoolean(key, description);
        if (defaultValue != null)
            option.defaultValue(defaultValue.toString());
        cliOptions.add(option);
    }

    /**
     * generates OpenAPI specification file in YAML format
     *
     * @param objs map of object
     */
    public void generateYAMLSpecFile(Map<String, Object> objs) {
        OpenAPI openAPI = (OpenAPI) objs.get("openAPI");
        String yaml = SerializerUtils.toYamlString(openAPI);
        if (yaml != null) {
            objs.put("openapi-yaml", yaml);
        }
    }

    @Override
    public List<CodegenServer> fromServers(List<Server> servers) {
        if (servers == null) {
            return Collections.emptyList();
        }
        List<CodegenServer> codegenServers = new LinkedList<>();
        for (Server server : servers) {
            CodegenServer cs = new CodegenServer();
            cs.description = escapeText(server.getDescription());
            cs.url = server.getUrl();
            cs.variables = this.fromServerVariables(server.getVariables());
            codegenServers.add(cs);
        }
        return codegenServers;
    }

    @Override
    public List<CodegenServerVariable> fromServerVariables(Map<String, ServerVariable> variables) {
        if (variables == null) {
            return Collections.emptyList();
        }

        Map<String, String> variableOverrides = serverVariableOverrides();

        List<CodegenServerVariable> codegenServerVariables = new LinkedList<>();
        for (Entry<String, ServerVariable> variableEntry : variables.entrySet()) {
            CodegenServerVariable codegenServerVariable = new CodegenServerVariable();
            ServerVariable variable = variableEntry.getValue();
            List<String> enums = variable.getEnum();

            codegenServerVariable.defaultValue = variable.getDefault();
            codegenServerVariable.description = escapeText(variable.getDescription());
            codegenServerVariable.enumValues = enums;
            codegenServerVariable.name = variableEntry.getKey();

            // Sets the override value for a server variable pattern.
            // NOTE: OpenAPI Specification doesn't prevent multiple server URLs with variables. If multiple objects have the same
            //       variables pattern, user overrides will apply to _all_ of these patterns. We may want to consider indexed overrides.
            if (variableOverrides != null && !variableOverrides.isEmpty()) {
                String value = variableOverrides.getOrDefault(variableEntry.getKey(), variable.getDefault());
                codegenServerVariable.value = value;

                if (enums != null && !enums.isEmpty() && !enums.contains(value)) {
                    if (LOGGER.isWarnEnabled()) { // prevents calculating StringUtils.join when debug isn't enabled
                        LOGGER.warn("Variable override of '{}' is not listed in the enum of allowed values ({}).", value, StringUtils.join(enums, ","));
                    }
                }
            } else {
                codegenServerVariable.value = variable.getDefault();
            }

            codegenServerVariables.add(codegenServerVariable);
        }
        return codegenServerVariables;
    }

    /**
     * Post-process the auto-generated file, e.g. using go-fmt to format the Go code. The file type can be "model-test",
     * "model-doc", "model", "api", "api-test", "api-doc", "supporting-mustache", "supporting-common",
     * "openapi-generator-ignore", "openapi-generator-version"
     * <p>
     * TODO: store these values in enum instead
     *
     * @param file     file to be processed
     * @param fileType file type
     */
    @Override
    public void postProcessFile(File file, String fileType) {
        LOGGER.debug("Post processing file {} ({})", file, fileType);
    }

    /**
     * Boolean value indicating the state of the option for post-processing file using environment variables.
     *
     * @return true if the option is enabled
     */
    @Override
    public boolean isEnablePostProcessFile() {
        return enablePostProcessFile;
    }

    /**
     * Set the boolean value indicating the state of the option for post-processing file using environment variables.
     *
     * @param enablePostProcessFile true to enable post-processing file
     */
    @Override
    public void setEnablePostProcessFile(boolean enablePostProcessFile) {
        this.enablePostProcessFile = enablePostProcessFile;
    }

    /**
     * Get the boolean value indicating the state of the option for updating only changed files
     */
    @Override
    public boolean isEnableMinimalUpdate() {
        return enableMinimalUpdate;
    }

    /**
     * Set the boolean value indicating the state of the option for updating only changed files
     *
     * @param enableMinimalUpdate true to enable minimal update
     */
    @Override
    public void setEnableMinimalUpdate(boolean enableMinimalUpdate) {
        this.enableMinimalUpdate = enableMinimalUpdate;
    }

    /**
     * Indicates whether the codegen configuration should treat documents as strictly defined by the OpenAPI specification.
     *
     * @return true to act strictly upon spec documents, potentially modifying the spec to strictly fit the spec.
     */
    @Override
    public boolean isStrictSpecBehavior() {
        return this.strictSpecBehavior;
    }

    /**
     * Sets the boolean valid indicating whether generation will work strictly against the specification, potentially making
     * minor changes to the input document.
     *
     * @param strictSpecBehavior true if we will behave strictly, false to allow specification documents which pass validation to be loosely interpreted against the spec.
     */
    @Override
    public void setStrictSpecBehavior(final boolean strictSpecBehavior) {
        this.strictSpecBehavior = strictSpecBehavior;
    }

    @Override
    public FeatureSet getFeatureSet() {
        return this.generatorMetadata.getFeatureSet();
    }

    /**
     * Get the boolean value indicating whether to remove enum value prefixes
     */
    @Override
    public boolean isRemoveEnumValuePrefix() {
        return this.removeEnumValuePrefix;
    }

    /**
     * Set the boolean value indicating whether to remove enum value prefixes
     *
     * @param removeEnumValuePrefix true to enable enum value prefix removal
     */
    @Override
    public void setRemoveEnumValuePrefix(final boolean removeEnumValuePrefix) {
        this.removeEnumValuePrefix = removeEnumValuePrefix;
    }

    //// Following methods are related to the "useOneOfInterfaces" feature

    /**
     * Add "x-one-of-name" extension to a given oneOf schema (assuming it has at least 1 oneOf elements)
     *
     * @param s    schema to add the extension to
     * @param name name of the parent oneOf schema
     */
    public void addOneOfNameExtension(ComposedSchema s, String name) {
        if (s.getOneOf() != null && s.getOneOf().size() > 0) {
            s.addExtension("x-one-of-name", name);
        }
    }

    public void addImportsToOneOfInterface(List<Map<String, String>> imports) {
    }
    //// End of methods related to the "useOneOfInterfaces" feature

    protected void modifyFeatureSet(Consumer<FeatureSet.Builder> processor) {
        FeatureSet.Builder builder = getFeatureSet().modify();
        processor.accept(builder);
        this.generatorMetadata = GeneratorMetadata.newBuilder(generatorMetadata)
                .featureSet(builder.build()).build();
    }

    /**
     * An map entry for cached sanitized names.
     */
    private static class SanitizeNameOptions {
        public SanitizeNameOptions(String name, String removeCharRegEx, List<String> exceptions) {
            this.name = name;
            this.removeCharRegEx = removeCharRegEx;
            if (exceptions != null) {
                this.exceptions = Collections.unmodifiableList(exceptions);
            } else {
                this.exceptions = Collections.emptyList();
            }
        }

        public String getName() {
            return name;
        }

        public String getRemoveCharRegEx() {
            return removeCharRegEx;
        }

        public List<String> getExceptions() {
            return exceptions;
        }

        private String name;
        private String removeCharRegEx;
        private List<String> exceptions;

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;
            SanitizeNameOptions that = (SanitizeNameOptions) o;
            return Objects.equals(getName(), that.getName()) &&
                    Objects.equals(getRemoveCharRegEx(), that.getRemoveCharRegEx()) &&
                    Objects.equals(getExceptions(), that.getExceptions());
        }

        @Override
        public int hashCode() {
            return Objects.hash(getName(), getRemoveCharRegEx(), getExceptions());
        }
    }

    /**
     * Returns the additionalProperties Schema for the specified input schema.
     * <p>
     * The additionalProperties keyword is used to control the handling of additional, undeclared
     * properties, that is, properties whose names are not listed in the properties keyword.
     * The additionalProperties keyword may be either a boolean or an object.
     * If additionalProperties is a boolean and set to false, no additional properties are allowed.
     * By default when the additionalProperties keyword is not specified in the input schema,
     * any additional properties are allowed. This is equivalent to setting additionalProperties
     * to the boolean value True or setting additionalProperties: {}
     *
     * @param schema the input schema that may or may not have the additionalProperties keyword.
     * @return the Schema of the additionalProperties. The null value is returned if no additional
     * properties are allowed.
     */
    protected Schema getAdditionalProperties(Schema schema) {
        return ModelUtils.getAdditionalProperties(openAPI, schema);
    }

    /**
     * Check if the given MIME is a JSON MIME.
     * JSON MIME examples:
     * application/json
     * application/json; charset=UTF8
     * APPLICATION/JSON
     *
     * @param mime MIME string
     * @return true if the input matches the JSON MIME
     */
    protected static boolean isJsonMimeType(String mime) {
        return mime != null && (JSON_MIME_PATTERN.matcher(mime).matches());
    }

    /**
     * Check if the given MIME is a JSON Vendor MIME.
     * JSON MIME examples:
     * application/vnd.mycompany+json
     * application/vnd.mycompany.resourceA.version1+json
     *
     * @param mime MIME string
     * @return true if the input matches the JSON vendor MIME
     */
    protected static boolean isJsonVendorMimeType(String mime) {
        return mime != null && JSON_VENDOR_MIME_PATTERN.matcher(mime).matches();
    }

    private List<CodegenSchema> getComposedProperties(List<Schema> xOfCollection, String collectionName, String sourceJsonPath, String currentJsonPath) {
        if (xOfCollection == null) {
            return null;
        }
        List<CodegenSchema> xOf = new ArrayList<>();
        int i = 0;
        for (Schema xOfSchema : xOfCollection) {
            CodegenSchema cp = fromSchema(xOfSchema, sourceJsonPath, currentJsonPath + "/" + collectionName + "/" + String.valueOf(i));
            xOf.add(cp);
            i += 1;
        }
        return xOf;
    }

    @Override
    public String requestBodyFileFolder() {
        return outputFolder + File.separatorChar + packageName() + File.separatorChar + "components" + File.separatorChar + "request_bodies";
    }

    @Override
    public String responseFileFolder(String componentName) {
        return outputFolder + File.separatorChar + packageName() + File.separatorChar + "components" + File.separatorChar + "responses" + File.separatorChar + toResponseModuleName(componentName);
    }

    @Override
    public String defaultTemplatingEngine() {
        return "mustache";
    }

    @Override
    public GeneratorLanguage generatorLanguage() {
        return GeneratorLanguage.JAVA;
    }

    @Override
    public String generatorLanguageVersion() {
        return null;
    }

    @Override
    public List<VendorExtension> getSupportedVendorExtensions() {
        return new ArrayList<>();
    }

    @Override
    public boolean getUseInlineModelResolver() { return true; }

    /*
    A function to convert yaml or json ingested strings like property names
    And convert special characters like newline, tab, carriage return
    Into strings that can be rendered in the language that the generator will output to
    */
    protected String handleSpecialCharacters(String name) { return name; }

    public String getItemsName(Schema containingSchema, String containingSchemaName) {
        if (containingSchema.getExtensions() != null && containingSchema.getExtensions().get("x-item-name") != null) {
            return containingSchema.getExtensions().get("x-item-name").toString();
        }
        return toVarName(containingSchemaName);
    }

    public String getAdditionalPropertiesName() {
        return "additional_properties";
    }


    /**
     * Used to ensure that null or Schema is returned given an input Boolean/Schema/null
     * This will be used in openapi 3.1.0 spec processing to ensure that Booleans become Schemas
     * Because our generators only understand Schemas
     * Note: use getIsBooleanSchemaTrue or getIsBooleanSchemaFalse on the JsonSchema
     * if you need to be able to detect if the original schema's value was true or false
     *
     * @param schema the input Boolean or Schema data to convert to a Schema
     * @return Schema the input data converted to a Schema if possible
     */
    protected Schema getSchemaFromBooleanOrSchema(Object schema) {
        if (schema instanceof Boolean) {
            if (Boolean.TRUE.equals(schema)) {
                return trueSchema;
            } else if (Boolean.FALSE.equals(schema)) {
                return falseSchema;
            }
            // null case
            return null;
        } else if (schema instanceof Schema) {
            if (schema == null) {
                return null;
            }
            return (Schema) schema;
        } else if (schema == null) {
            return null;
        }
        throw new IllegalArgumentException("Invalid schema type; type must be Boolean or Schema");
    }
}
