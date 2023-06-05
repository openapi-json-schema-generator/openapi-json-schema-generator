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

package org.openapijsonschematools.codegen.model;

import io.swagger.v3.oas.models.ExternalDocumentation;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Map;
import java.util.Objects;
import java.util.TreeSet;

public class CodegenSchema {
    // 3.0.0
    public String title;
    public Number multipleOf;
    public String maximum;
    public Boolean exclusiveMaximum;
    public String minimum;
    public Boolean exclusiveMinimum;
    public Integer maxLength;
    public Integer minLength;
    public CodegenPatternInfo patternInfo;
    public Integer maxItems;
    public Integer minItems;
    public Boolean uniqueItems;
    public Integer maxProperties;
    public Integer minProperties;
    public LinkedHashMap<CodegenKey, CodegenSchema> requiredProperties; // used to store required info
    public LinkedHashMap<EnumValue, String> enumValueToName; // enum info
    public String type;
    public ArrayListWithContext<CodegenSchema> allOf = null;
    public ArrayListWithContext<CodegenSchema> anyOf = null;
    public ArrayListWithContext<CodegenSchema> oneOf = null;
    public CodegenSchema not = null;
    public CodegenSchema items;
    public LinkedHashMapWithContext<CodegenKey, CodegenSchema> properties;
    public CodegenSchema additionalProperties;
    public String description;
    public String format;
    public EnumValue defaultValue;
    public CodegenRefInfo<CodegenSchema> refInfo;  // $ref

    // openapi 3.0.0
    // note: null is added to types when nullable is true
    public Boolean nullable;
    public CodegenDiscriminator discriminator;
    public Boolean readOnly;
    public Boolean writeOnly;
    public CodegenXml xml;
    public ExternalDocumentation externalDocumentation;
    public String example;
    public Boolean deprecated;
    // openapi Specification Extensions
    public Map<String, Object> vendorExtensions;

    // 3.1.0
    public LinkedHashSet<String> types;
    public CodegenSchema contains;
    public LinkedHashMap<String, List<String>> dependentRequired;
    public boolean isBooleanSchemaTrue;  // supports boolean schemas
    public boolean isBooleanSchemaFalse;  // supports boolean schemas

    // Extra needed fields
    public boolean componentModule;
    public TreeSet<String> imports;
    public CodegenKey jsonPathPiece;
    public String unescapedDescription;
    public LinkedHashMap<CodegenKey, CodegenSchema> optionalProperties;
    public boolean schemaIsFromAdditionalProperties;
    public HashMap<String, SchemaTestCase> testCases = new HashMap<>();
    /**
     * schema/allOfType/anyOfType/oneOfType/propertiesType
     * used in getAllSchemas to write type definitions for allOfType/anyOfType/oneOfType/propertiesType
     */
    public String instanceType;

    public boolean hasValidation() {
        return maxItems != null || minItems != null || minProperties != null || maxProperties != null || minLength != null || maxLength != null || multipleOf != null || patternInfo != null || minimum != null || maximum != null || exclusiveMinimum != null || exclusiveMaximum != null || uniqueItems != null;
    }

    public boolean hasMultipleTypes() {
        return (types != null && types.size() > 1);
    }

    public boolean hasDiscriminatorWithNonEmptyMapping() {
        if (discriminator == null) {
            return false;
        }
        if (discriminator.mappedModels == null) {
            return false;
        } else return !discriminator.mappedModels.isEmpty();
    }

    public CodegenSchema getDeepestRef() {
        if (refInfo == null) {
            return null;
        }
        CodegenSchema refObject = refInfo.ref;
        while (refObject.refInfo != null) {
            refObject = refObject.refInfo.ref;
        }
        return refObject;
    }

    public CodegenSchema getSelfOrDeepestRef() {
        if (refInfo == null) {
            return this;
        }
        CodegenSchema refObject = refInfo.ref;
        while (refObject.refInfo != null) {
            refObject = refObject.refInfo.ref;
        }
        return refObject;
    }

    /**
     * Returns all schemas in post order traversal, used by templates to write schema classes
     * @param schemas the input list that stores this and all required schemas
     * @return the list that stores this and all required schemas
     */
    private ArrayList<CodegenSchema> getAllSchemas(ArrayList<CodegenSchema> schemas, int level) {
        /*
        post order traversal using alphabetic json schema keywords as the order
        keywords with schemas:
        additionalProperties
        allOf
        anyOf
        items
        not
        oneOf
        properties

        excluded:
        discriminator (not actually applicable because all values would be refs and do not need to be defined)
        $ref (because it is an import)
         */
        if (isBooleanSchemaFalse) {
            // return early for isBooleanSchemaFalse so not_ will not be written
            schemas.add(this);
            return schemas;
        }
        if (additionalProperties != null) {
            additionalProperties.getAllSchemas(schemas, level + 1);
        }
        if (allOf != null) {
            for (CodegenSchema someSchema: allOf) {
                someSchema.getAllSchemas(schemas, level + 1);
            }
        }
        if (anyOf != null) {
            for (CodegenSchema someSchema: anyOf) {
                someSchema.getAllSchemas(schemas, level + 1);
            }
        }
        if (items != null) {
            items.getAllSchemas(schemas, level + 1);
        }
        if (not != null) {
            not.getAllSchemas(schemas, level + 1);
        }
        if (oneOf != null) {
            for (CodegenSchema someSchema: oneOf) {
                someSchema.getAllSchemas(schemas, level + 1);
            }
        }
        if (properties != null) {
            for (CodegenSchema someSchema: properties.values()) {
                someSchema.getAllSchemas(schemas, level + 1);
            }
        }
        if (refInfo != null && level > 0) {
            // do not add ref to schemas
            return schemas;
        }
        schemas.add(this);
        return schemas;
    }

    public ArrayList<CodegenSchema> getSchemas() {
        ArrayList<CodegenSchema> schemas = new ArrayList<>();
        return getAllSchemas(schemas, 0);
    }

    public boolean isComplicated() {
        // used by templates

        if (allOf != null || anyOf != null || oneOf != null || not != null) {
            return true;
        }
        return types != null && (types.contains("array") || types.contains("object"));
    }

    protected void addInstanceInfo(StringBuilder sb) {
        sb.append(", description='").append(description).append('\'');
        sb.append(", name='").append(jsonPathPiece).append('\'');
        sb.append(", defaultValue='").append(defaultValue).append('\'');
        sb.append(", title='").append(title).append('\'');
        sb.append(", unescapedDescription='").append(unescapedDescription).append('\'');
        sb.append(", maxLength=").append(maxLength);
        sb.append(", minLength=").append(minLength);
        sb.append(", patternInfo='").append(patternInfo).append('\'');
        sb.append(", example='").append(example).append('\'');
        sb.append(", minimum='").append(minimum).append('\'');
        sb.append(", maximum='").append(maximum).append('\'');
        sb.append(", exclusiveMinimum=").append(exclusiveMinimum);
        sb.append(", exclusiveMaximum=").append(exclusiveMaximum);
        sb.append(", deprecated=").append(deprecated);
        sb.append(", types=").append(types);
        sb.append(", hasMultipleTypes=").append(hasMultipleTypes());
        sb.append(", readOnly=").append(readOnly);
        sb.append(", writeOnly=").append(writeOnly);
        sb.append(", nullable=").append(nullable);
        sb.append(", allowableValues=").append(enumValueToName);
        sb.append(", items=").append(items);
        sb.append(", additionalProperties=").append(additionalProperties);
        sb.append(", vendorExtensions=").append(vendorExtensions);
        sb.append(", hasValidation=").append(hasValidation());
        sb.append(", maxItems=").append(maxItems);
        sb.append(", minItems=").append(minItems);
        sb.append(", maxProperties=").append(maxProperties);
        sb.append(", minProperties=").append(minProperties);
        sb.append(", uniqueItems=").append(uniqueItems);
        sb.append(", multipleOf=").append(multipleOf);
        sb.append(", xml=").append(xml);
        sb.append(", requiredProperties=").append(requiredProperties);
        sb.append(", optionalProperties=").append(optionalProperties);
        sb.append(", properties=").append(properties);
        sb.append(", refInfo=").append(refInfo);
        sb.append(", schemaIsFromAdditionalProperties=").append(schemaIsFromAdditionalProperties);
        sb.append(", isBooleanSchemaTrue=").append(isBooleanSchemaTrue);
        sb.append(", isBooleanSchemaFalse=").append(isBooleanSchemaFalse);
        sb.append(", format=").append(format);
        sb.append(", dependentRequired=").append(dependentRequired);
        sb.append(", contains=").append(contains);
        sb.append(", allOf=").append(allOf);
        sb.append(", anyOf=").append(anyOf);
        sb.append(", oneOf=").append(oneOf);
        sb.append(", not=").append(not);
        sb.append(", externalDocumentation=").append(externalDocumentation);
        sb.append(", discriminator=").append(discriminator);
        sb.append(", imports=").append(imports);
        sb.append(", componentModule=").append(componentModule);
        sb.append(", testCases=").append(testCases);
    }

    @Override
    public String toString() {
        final StringBuilder sb = new StringBuilder("CodegenSchema{");
        addInstanceInfo(sb);
        sb.append('}');
        return sb.toString();
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        CodegenSchema that = (CodegenSchema) o;
        return exclusiveMinimum == that.exclusiveMinimum &&
                exclusiveMaximum == that.exclusiveMaximum &&
                deprecated == that.deprecated &&
                readOnly == that.readOnly &&
                writeOnly == that.writeOnly &&
                nullable == that.nullable &&
                isBooleanSchemaTrue == that.isBooleanSchemaTrue &&
                isBooleanSchemaFalse == that.isBooleanSchemaFalse &&
                schemaIsFromAdditionalProperties == that.schemaIsFromAdditionalProperties &&
                Objects.equals(xml, that.xml) &&
                Objects.equals(types, that.types) &&
                Objects.equals(testCases, that.testCases) &&
                Objects.equals(componentModule, that.componentModule) &&
                Objects.equals(imports, that.imports) &&
                Objects.equals(discriminator, that.discriminator) &&
                Objects.equals(externalDocumentation, that.externalDocumentation) &&
                Objects.equals(allOf, that.allOf) &&
                Objects.equals(anyOf, that.anyOf) &&
                Objects.equals(oneOf, that.oneOf) &&
                Objects.equals(not, that.not) &&
                Objects.equals(contains, that.contains) &&
                Objects.equals(dependentRequired, that.dependentRequired) &&
                Objects.equals(format, that.format) &&
                Objects.equals(refInfo, that.refInfo) &&
                Objects.equals(requiredProperties, that.requiredProperties) &&
                Objects.equals(optionalProperties, that.optionalProperties) &&
                Objects.equals(properties, that.properties) &&
                Objects.equals(description, that.description) &&
                Objects.equals(jsonPathPiece, that.jsonPathPiece) &&
                Objects.equals(defaultValue, that.defaultValue) &&
                Objects.equals(title, that.title) &&
                Objects.equals(unescapedDescription, that.unescapedDescription) &&
                Objects.equals(maxLength, that.maxLength) &&
                Objects.equals(minLength, that.minLength) &&
                Objects.equals(patternInfo, that.patternInfo) &&
                Objects.equals(example, that.example) &&
                Objects.equals(minimum, that.minimum) &&
                Objects.equals(maximum, that.maximum) &&
                Objects.equals(enumValueToName, that.enumValueToName) &&
                Objects.equals(items, that.items) &&
                Objects.equals(additionalProperties, that.additionalProperties) &&
                Objects.equals(vendorExtensions, that.vendorExtensions) &&
                Objects.equals(maxItems, that.maxItems) &&
                Objects.equals(minItems, that.minItems) &&
                Objects.equals(multipleOf, that.multipleOf);
    }

    @Override
    public int hashCode() {
        return Objects.hash(description,
                jsonPathPiece, defaultValue,
                title, unescapedDescription,
                maxLength, minLength, patternInfo, example, minimum, maximum,
                exclusiveMinimum, exclusiveMaximum, deprecated, types,
                readOnly, writeOnly, nullable,
                enumValueToName, items, additionalProperties,
                vendorExtensions, maxItems, minItems, xml,
                schemaIsFromAdditionalProperties, isBooleanSchemaTrue, isBooleanSchemaFalse,
                format, dependentRequired, contains, allOf, anyOf, oneOf, not,
                properties, optionalProperties, requiredProperties, externalDocumentation,
                discriminator, imports, componentModule, testCases, refInfo);
    }
}
