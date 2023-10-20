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

package org.openapijsonschematools.codegen.generators.openapimodels;

import io.swagger.v3.oas.models.ExternalDocumentation;
import com.fasterxml.jackson.annotation.JsonIgnore;

import java.util.*;

public class CodegenOperation {
    public final Boolean deprecated;
    public final LinkedHashSet<String> nonErrorStatusCodes; // values like 201
    public final LinkedHashSet<Integer> nonErrorWildcardStatusCodes; // values like 2 for @2XX
    public final LinkedHashSet<String> errorStatusCodes; // values like 401
    public final LinkedHashSet<Integer> errorWildcardStatusCodes; // values like 4 for 4XX
    public final String summary, unescapedDescription, description;
    public final LinkedHashSet<String> produces;
    public final List<CodegenServer> servers;
    public final CodegenRequestBody requestBody;
    // properties where key is contentType, value is a ref schema, encapsulates imports
    public final CodegenSchema requestBodySchema;
    public final ParameterCollection parameters;
    public final CodegenSchema pathParametersSchema;
    public final CodegenSchema queryParametersSchema;
    public final CodegenSchema headerParametersSchema;
    public final CodegenSchema cookieParametersSchema;
    public final ParameterCollection pathItemParameters;

    public final boolean hasRequiredParamOrBody;
    public final boolean hasOptionalParamOrBody;
    public final List<HashMap<String, CodegenSecurityRequirementValue>> security;
    public final Map<String, CodegenTag> tags;
    public final TreeMap<String, CodegenResponse> responses;
    public final TreeMap<Integer, CodegenResponse> statusCodeResponses;
    public final TreeMap<Integer, CodegenResponse> wildcardCodeResponses;
    public final TreeMap<String, CodegenResponse> nonDefaultResponses;
    public final CodegenResponse defaultResponse;
    public final List<CodegenCallback> callbacks;
    public final ExternalDocumentation externalDocs;
    public final Map<String, Object> vendorExtensions;
    public final CodegenKey operationId;
    public final CodegenKey jsonPathPiece;

    public CodegenOperation(
            Boolean deprecated,
            LinkedHashSet<String> nonErrorStatusCodes,
            LinkedHashSet<Integer> nonErrorWildcardStatusCodes,
            LinkedHashSet<String> errorStatusCodes,
            LinkedHashSet<Integer> errorWildcardStatusCodes,
            String summary,
            String unescapedDescription,
            String description,
            LinkedHashSet<String> produces,
            List<CodegenServer> servers,
            CodegenRequestBody requestBody,
            ParameterCollection parameters,
            CodegenSchema pathParametersSchema,
            CodegenSchema queryParametersSchema,
            CodegenSchema headerParametersSchema,
            CodegenSchema cookieParametersSchema,
            boolean hasRequiredParamOrBody,
            boolean hasOptionalParamOrBody,
            List<HashMap<String, CodegenSecurityRequirementValue>> security,
            Map<String, CodegenTag> tags,
            TreeMap<String, CodegenResponse> responses,
            TreeMap<Integer, CodegenResponse> statusCodeResponses,
            TreeMap<Integer, CodegenResponse> wildcardCodeResponses,
            TreeMap<String, CodegenResponse> nonDefaultResponses,
            CodegenResponse defaultResponse,
            List<CodegenCallback> callbacks,
            ExternalDocumentation externalDocs,
            Map<String, Object> vendorExtensions,
            CodegenKey operationId,
            CodegenKey jsonPathPiece,
            CodegenSchema requestBodySchema,
            ParameterCollection pathItemParameters
) {
        this.deprecated = deprecated;
        this.nonErrorStatusCodes = nonErrorStatusCodes;
        this.nonErrorWildcardStatusCodes = nonErrorWildcardStatusCodes;
        this.errorStatusCodes = errorStatusCodes;
        this.errorWildcardStatusCodes = errorWildcardStatusCodes;
        this.summary = summary;
        this.unescapedDescription = unescapedDescription;
        this.description = description;
        this.produces = produces;
        this.servers = servers;
        this.requestBody = requestBody;
        this.parameters = parameters;
        this.pathParametersSchema = pathParametersSchema;
        this.queryParametersSchema = queryParametersSchema;
        this.headerParametersSchema = headerParametersSchema;
        this.cookieParametersSchema = cookieParametersSchema;
        this.hasRequiredParamOrBody = hasRequiredParamOrBody;
        this.hasOptionalParamOrBody = hasOptionalParamOrBody;
        this.security = security;
        this.tags = tags;
        this.responses = responses;
        this.statusCodeResponses = statusCodeResponses;
        this.wildcardCodeResponses = wildcardCodeResponses;
        this.nonDefaultResponses = nonDefaultResponses;
        this.defaultResponse = defaultResponse;
        this.callbacks = callbacks;
        this.externalDocs = externalDocs;
        this.vendorExtensions = vendorExtensions;
        this.operationId = operationId;
        this.jsonPathPiece = jsonPathPiece;
        this.requestBodySchema = requestBodySchema;
        this.pathItemParameters = pathItemParameters;
    }

    // used by operation templates
    public Map<String, CodegenResponse> getNonErrorResponses() {
        HashMap<String,CodegenResponse> nonErrorResponses = new HashMap<>();
        if (statusCodeResponses != null) {
            for (Map.Entry<Integer, CodegenResponse> entry: statusCodeResponses.entrySet()) {
                if (entry.getKey() >= 200 && entry.getKey() <= 399) {
                    nonErrorResponses.put(entry.getKey().toString(), entry.getValue());
                }
            }
        }
        if (wildcardCodeResponses != null) {
            for (Map.Entry<Integer, CodegenResponse> entry: wildcardCodeResponses.entrySet()) {
                if (entry.getKey() == 2 || entry.getKey() == 3) {
                    nonErrorResponses.put(entry.getKey().toString(), entry.getValue());
                }
            }
        }
        if (defaultResponse != null) {
            if (nonErrorResponses.isEmpty()) {
                /* default response should be non-error because
                The Responses Object MUST contain at least one response code, and if only one response code
                is provided it SHOULD be the response for a successful operation call.
                 */
                nonErrorResponses.put("default", defaultResponse);
            } else {
                // the code does not know if this is an error response or non-error
                // TODO add generation option that specifies it?
                nonErrorResponses.put("default", defaultResponse);
            }
        }
        if (nonErrorResponses.isEmpty()) {
            return null;
        }
        return nonErrorResponses;
    }

    public boolean getAllResponsesAreErrors() {
        if (responses.size() == 1 && defaultResponse != null) {
            return false;
        }
        for (String code: nonDefaultResponses.keySet()) {
            String firstNumber = code.substring(0, 1);
            switch (firstNumber) {
                case "1": case "2": case "3":
                    return false;
            }
        }
        if (defaultResponse != null) {
            // 404 + default, unable to tell if default is a success or an error status code
            return false;
        }
        return true;
    }

    @Override
    public String toString() {
        final StringBuffer sb = new StringBuffer("CodegenOperation{");
        sb.append(", deprecated=").append(deprecated);
        sb.append(", operationId='").append(operationId).append('\'');
        sb.append(", summary='").append(summary).append('\'');
        sb.append(", unescapedNotes='").append(unescapedDescription).append('\'');
        sb.append(", notes='").append(description).append('\'');
        sb.append(", defaultResponse='").append(defaultResponse).append('\'');
        sb.append(", produces=").append(produces);
        sb.append(", servers=").append(servers);
        sb.append(", requestBody=").append(requestBody);
        sb.append(", parameters=").append(parameters);
        sb.append(", hasRequiredParamOrBody=").append(hasRequiredParamOrBody);
        sb.append(", hasOptionalParamOrBody=").append(hasOptionalParamOrBody);
        sb.append(", security=").append(security);
        sb.append(", tags=").append(tags);
        sb.append(", responses=").append(responses);
        sb.append(", statusCodeResponses=").append(statusCodeResponses);
        sb.append(", wildcardCodeResponses=").append(wildcardCodeResponses);
        sb.append(", nonDefaultResponses=").append(nonDefaultResponses);
        sb.append(", callbacks=").append(callbacks);
        sb.append(", externalDocs=").append(externalDocs);
        sb.append(", vendorExtensions=").append(vendorExtensions);
        sb.append(", jsonPathPiece=").append(jsonPathPiece);
        sb.append('}');
        return sb.toString();
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        CodegenOperation that = (CodegenOperation) o;
        return deprecated == that.deprecated &&
                Objects.equals(operationId, that.operationId) &&
                Objects.equals(summary, that.summary) &&
                Objects.equals(unescapedDescription, that.unescapedDescription) &&
                Objects.equals(description, that.description) &&
                Objects.equals(defaultResponse, that.defaultResponse) &&
                Objects.equals(produces, that.produces) &&
                Objects.equals(servers, that.servers) &&
                Objects.equals(requestBody, that.requestBody) &&
                Objects.equals(parameters, that.parameters) &&
                Objects.equals(hasRequiredParamOrBody, that.hasRequiredParamOrBody) &&
                Objects.equals(hasOptionalParamOrBody, that.hasOptionalParamOrBody) &&
                Objects.equals(security, that.security) &&
                Objects.equals(tags, that.tags) &&
                Objects.equals(responses, that.responses) &&
                Objects.equals(statusCodeResponses, that.statusCodeResponses) &&
                Objects.equals(wildcardCodeResponses, that.wildcardCodeResponses) &&
                Objects.equals(nonDefaultResponses, that.nonDefaultResponses) &&
                Objects.equals(callbacks, that.callbacks) &&
                Objects.equals(externalDocs, that.externalDocs) &&
                Objects.equals(jsonPathPiece, that.jsonPathPiece) &&
                Objects.equals(vendorExtensions, that.vendorExtensions);
    }

    @Override
    public int hashCode() {

        return Objects.hash(deprecated, operationId,
                summary, unescapedDescription, description, defaultResponse,
                produces, servers, requestBody, parameters,
                hasRequiredParamOrBody, hasOptionalParamOrBody,
                security, tags, responses, callbacks, externalDocs,
                vendorExtensions, statusCodeResponses, wildcardCodeResponses,
                nonDefaultResponses, jsonPathPiece);
    }
}
