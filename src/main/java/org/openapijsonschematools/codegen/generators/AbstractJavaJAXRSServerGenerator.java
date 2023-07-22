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

package org.openapijsonschematools.codegen.generators;

import com.google.common.annotations.VisibleForTesting;
import io.swagger.v3.oas.models.OpenAPI;
import io.swagger.v3.oas.models.Operation;
import io.swagger.v3.oas.models.PathItem;
import org.apache.commons.lang3.StringUtils;
import org.openapijsonschematools.codegen.generators.models.CliOption;
import org.openapijsonschematools.codegen.common.CodegenConstants;
import org.openapijsonschematools.codegen.generators.generatormetadata.GeneratorType;
import org.openapijsonschematools.codegen.generators.openapimodels.CodegenOperation;
import org.openapijsonschematools.codegen.generators.features.BeanValidationFeatures;
import org.openapijsonschematools.codegen.common.URLPathUtils;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.net.URL;
import java.util.*;

public abstract class AbstractJavaJAXRSServerGenerator extends AbstractJavaGenerator implements BeanValidationFeatures {
    public static final String SERVER_PORT = "serverPort";
    public static final String USE_TAGS = "useTags";

    /**
     * Name of the sub-directory in "src/main/resource" where to find the
     * Mustache template for the JAX-RS Codegen.
     */
    protected static final String JAXRS_TEMPLATE_DIRECTORY_NAME = "JavaJaxRS";
    protected String implFolder = "src/main/java";
    protected String testResourcesFolder = "src/test/resources";
    protected String title = "OpenAPI Server";
    protected String serverPort = "8080";

    protected boolean useBeanValidation = true;
    protected boolean useTags = false;

    private final Logger LOGGER = LoggerFactory.getLogger(AbstractJavaJAXRSServerGenerator.class);

    public AbstractJavaJAXRSServerGenerator() {
        super();

        sourceFolder = "src/gen/java";
        invokerPackage = "org.openapijsonschematools.api";
        artifactId = "openapi-jaxrs-server";
        dateLibrary = "legacy"; //TODO: add joda support to all jax-rs
        apiPackage = "org.openapijsonschematools.api";
        modelPackage = "org.openapijsonschematools.model";

        // clioOptions default redefinition need to be updated
        updateOption(CodegenConstants.INVOKER_PACKAGE, this.getInvokerPackage());
        updateOption(CodegenConstants.ARTIFACT_ID, this.getArtifactId());
        updateOption(CodegenConstants.API_PACKAGE, apiPackage);
        updateOption(CodegenConstants.MODEL_PACKAGE, modelPackage);
        updateOption(DATE_LIBRARY, this.getDateLibrary());
        updateOption(CodegenConstants.SOURCE_FOLDER, this.getSourceFolder());

        additionalProperties.put("title", title);
        // java inflector uses the jackson lib
        additionalProperties.put(JACKSON, "true");

        cliOptions.add(new CliOption(CodegenConstants.IMPL_FOLDER, CodegenConstants.IMPL_FOLDER_DESC).defaultValue(implFolder));
        cliOptions.add(new CliOption("title", "a title describing the application").defaultValue(title));
        cliOptions.add(CliOption.newBoolean(USE_BEANVALIDATION, "Use BeanValidation API annotations",useBeanValidation));
        cliOptions.add(new CliOption(SERVER_PORT, "The port on which the server should be started").defaultValue(serverPort));
        cliOptions.add(CliOption.newBoolean(USE_TAGS, "use tags for creating interface and controller classnames"));
    }


    // ===============
    // COMMONS METHODS
    // ===============

    @Override
    public GeneratorType getTag() {
        return GeneratorType.SERVER;
    }

    @Override
    public void processOpts() {
        super.processOpts();

        if (additionalProperties.containsKey(CodegenConstants.IMPL_FOLDER)) {
            implFolder = (String) additionalProperties.get(CodegenConstants.IMPL_FOLDER);
        }

        if (additionalProperties.containsKey(USE_BEANVALIDATION)) {
            setUseBeanValidation(convertPropertyToBoolean(USE_BEANVALIDATION));
        }

        if (additionalProperties.containsKey(USE_TAGS)) {
            setUseTags(convertPropertyToBoolean(USE_TAGS));
        }

        writePropertyBack(USE_BEANVALIDATION, useBeanValidation);
    }

    @Override
    public void addOperationToGroup(String tag, String resourcePath, Operation operation, CodegenOperation co, Map<String, List<CodegenOperation>> operations) {
        if (useTags) {
            super.addOperationToGroup(tag, resourcePath, operation, co, operations);
        }
    }

    @Override
    public void preprocessOpenAPI(OpenAPI openAPI) {
        super.preprocessOpenAPI(openAPI);
        /* TODO there should be no need for the following logic
        if ("/".equals(swagger.getBasePath())) {
            swagger.setBasePath("");
        }
        */

        if (!this.additionalProperties.containsKey(SERVER_PORT)) {
            URL url = URLPathUtils.getServerURL(openAPI, serverVariableOverrides());
            // 8080 is the default value for a JEE Server:
            this.additionalProperties.put(SERVER_PORT, URLPathUtils.getPort(url, serverPort));
        }

        if (openAPI.getPaths() != null) {
            for (Map.Entry<String, PathItem> openAPIGetPathsEntry : openAPI.getPaths().entrySet()) {
                String pathname = openAPIGetPathsEntry.getKey();
                PathItem path = openAPIGetPathsEntry.getValue();
                if (path.readOperations() != null) {
                    for (Operation operation : path.readOperations()) {
                        if (operation.getTags() != null) {
                            List<Map<String, String>> tags = new ArrayList<Map<String, String>>();
                            for (String tag : operation.getTags()) {
                                Map<String, String> value = new HashMap<String, String>();
                                value.put("tag", tag);
                                tags.add(value);
                            }
                            if (operation.getTags().size() > 0) {
                                String tag = operation.getTags().get(0);
                                operation.setTags(Arrays.asList(tag));
                            }
                            operation.addExtension("x-tags", tags);
                        }
                    }
                }
            }
        }
    }

    @Override
    public String toApiName(final String name) {
        String computed = name;
        if (computed.length() > 0) {
            computed = sanitizeName(computed);
        }
        return super.toApiName(computed);
    }

    private static String getCommonPath(String path1, String path2) {
        final String[] parts1 = StringUtils.split(path1, "/");
        final String[] parts2 = StringUtils.split(path2, "/");
        StringBuilder builder = new StringBuilder();
        for (int i = 0; i < Math.min(parts1.length, parts2.length); i++) {
            if (!parts1[i].equals(parts2[i])) {
                break;
            }
            builder.append("/").append(parts1[i]);
        }
        return builder.toString();
    }

    private String implFileFolder(String output) {
        return outputFolder + "/" + output + "/" + apiPackage().replace('.', '/');
    }

    @Override
    public void setUseBeanValidation(boolean useBeanValidation) {
        this.useBeanValidation = useBeanValidation;
    }

    @VisibleForTesting
    public void setUseTags(boolean useTags) {
        this.useTags = useTags;
    }
}
