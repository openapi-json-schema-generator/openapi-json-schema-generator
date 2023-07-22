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

import org.openapijsonschematools.codegen.common.ModelUtils;

import java.util.LinkedHashMap;
import java.util.Map;
import java.util.Objects;
import java.util.TreeSet;

/**
 * Describes a single operation parameter in the OAS specification.
 * A unique parameter is defined by a combination of a name and location.
 * Parameters may be located in a path, query, header or cookie.
 */
public class CodegenHeader {
    public final String description;
    public final String unescapedDescription;
    public final String example; // example value (x-example)
    public final Map<String, Object> vendorExtensions;
    public final Boolean required;
    public final LinkedHashMap<CodegenKey, CodegenMediaType> content;
    public final TreeSet<String> imports;
    public final boolean componentModule;
    public final CodegenKey jsonPathPiece;
    public final Boolean explode;
    public final String style;
    public final Boolean deprecated;
    public final CodegenSchema schema;
    public final CodegenRefInfo<CodegenHeader> refInfo;

    public CodegenHeader(String description, String unescapedDescription, String example, Map<String, Object> vendorExtensions, Boolean required, LinkedHashMap<CodegenKey, CodegenMediaType> content, TreeSet<String> imports, boolean componentModule, CodegenKey jsonPathPiece, Boolean explode, String style, Boolean deprecated, CodegenSchema schema, CodegenRefInfo<CodegenHeader> refInfo) {
        this.description = description;
        this.unescapedDescription = unescapedDescription;
        this.example = example;
        this.vendorExtensions = vendorExtensions;
        this.required = required;
        this.content = content;
        this.imports = imports;
        this.componentModule = componentModule;
        this.jsonPathPiece = jsonPathPiece;
        this.explode = explode;
        this.style = style;
        this.deprecated = deprecated;
        this.schema = schema;
        this.refInfo = refInfo;
    }

    public CodegenHeader getSelfOrDeepestRef() {
        CodegenHeader selfOrRefParam = this;
        while (selfOrRefParam.refInfo != null) {
            selfOrRefParam = selfOrRefParam.refInfo.ref;
        }
        return selfOrRefParam;
    }

    public String getSchemaJsonPath() {
        CodegenHeader selfOrRefParam = this;
        while (selfOrRefParam.refInfo != null) {
            selfOrRefParam = selfOrRefParam.refInfo.ref;
        }
        // parameter is now de-referenced
        CodegenSchema schema = null;
        if (selfOrRefParam.schema != null) {
            schema = selfOrRefParam.schema;
        } else {
            CodegenKey contentTypeKey = selfOrRefParam.content.keySet().iterator().next();
            schema = selfOrRefParam.content.get(contentTypeKey).schema;
        }
        schema = schema.getSelfOrDeepestRef();
        return schema.jsonPath;
    }

    @Override
    public int hashCode() {
        return Objects.hash(jsonPathPiece, explode, description, unescapedDescription, style, example, vendorExtensions, deprecated, required, schema, content, refInfo, imports, componentModule);
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof CodegenHeader)) return false;
        CodegenHeader that = (CodegenHeader) o;
        return required == that.required &&
                Objects.equals(jsonPathPiece, that.jsonPathPiece) &&
                Objects.equals(componentModule, that.componentModule) &&
                Objects.equals(imports, that.imports) &&
                Objects.equals(content, that.content) &&
                Objects.equals(description, that.description) &&
                Objects.equals(unescapedDescription, that.unescapedDescription) &&
                Objects.equals(example, that.example) &&
                Objects.equals(vendorExtensions, that.vendorExtensions) &&
                explode == that.explode &&
                deprecated == that.deprecated &&
                Objects.equals(schema, that.schema) &&
                Objects.equals(style, that.style) &&
                Objects.equals(refInfo, that.refInfo);
    }

    protected void addInstanceInfo(StringBuilder sb) {
        sb.append("name='").append(jsonPathPiece).append('\'');
        sb.append(", description='").append(description).append('\'');
        sb.append(", unescapedDescription='").append(unescapedDescription).append('\'');
        sb.append(", example='").append(example).append('\'');
        sb.append(", vendorExtensions=").append(vendorExtensions);
        sb.append(", required=").append(required);
        sb.append(", content=").append(content);
        sb.append(", imports=").append(imports);
        sb.append(", componentModule=").append(componentModule);
        sb.append(", explode=").append(explode);
        sb.append(", style='").append(style).append('\'');
        sb.append(", deprecated=").append(deprecated);
        sb.append(", schema=").append(schema);
        sb.append(", refInfo=").append(refInfo);
    }

    @Override
    public String toString() {
        final StringBuilder sb = new StringBuilder("CodegenHeader{");
        addInstanceInfo(sb);
        sb.append('}');
        return sb.toString();
    }

    public CodegenHeader getDeepestRef() {
        if (refInfo == null) {
            return null;
        }
        CodegenHeader refObject = refInfo.ref;
        while (refObject.refInfo != null) {
            refObject = refObject.refInfo.ref;
        }
        return refObject;
    }

    public CodegenSchema getSetSchema() {
        if (schema != null) {
            return schema;
        }
        if (content != null) {
            for (CodegenMediaType codegenMediaType: content.values()) {
                return codegenMediaType.schema;
            }
        }
        return null;
    }

    public String getSetSchemaJsonPath(String jsonPath) {
        if (schema != null) {
            return jsonPath + "/schema";
        }
        if (content != null) {
            for (Map.Entry<CodegenKey, CodegenMediaType> entry: content.entrySet()) {
                if (entry.getValue().schema != null) {
                    String contentType = entry.getKey().original;
                    return jsonPath + "/content/" + ModelUtils.encodeSlashes(contentType) + "/schema";
                }
            }
        }
        return null;
    }
}

