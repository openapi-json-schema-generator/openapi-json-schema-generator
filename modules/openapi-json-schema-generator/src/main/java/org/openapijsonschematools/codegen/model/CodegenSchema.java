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

import io.swagger.v3.oas.models.media.Schema;
import org.openapijsonschematools.codegen.utils.ModelUtils;

import java.util.*;

public class CodegenSchema extends OpenApiSchema {
    // testCases are for autogenerated tests of schemas
    public HashMap<String, SchemaTestCase> testCases = new HashMap<>();
    public String componentModule;
    public TreeSet<String> imports;
    public CodegenKey name;
    public String unescapedDescription;

    public boolean isString;
    public boolean isNumeric;
    public boolean isInteger;
    public boolean isShort;
    public boolean isLong;
    public boolean isUnboundedInteger;
    public boolean isNumber;
    public boolean isFloat;
    public boolean isDouble;
    public boolean isDecimal;
    public boolean isByteArray;
    public boolean isBinary;
    public boolean isFile;
    public boolean isBoolean;
    public boolean isDate; // full-date notation as defined by RFC 3339, section 5.6, for example, 2017-07-21
    public boolean isDateTime; // the date-time notation as defined by RFC 3339, section 5.6, for example, 2017-07-21T17:32:28Z
    public boolean isUuid;
    public boolean isUri;
    public boolean isEmail;
    public boolean isNull;
    public boolean isArray;
    public boolean isMap;
    public boolean isNullable;
    public boolean isSelfReference;
    public boolean isCircularReference;
    public String discriminatorValue;
    // todo make this calculated from types
    public boolean hasMultipleTypes = false;
    public LinkedHashMap<CodegenKey, CodegenSchema> optionalProperties;
    public CodegenRefInfo<CodegenSchema> refInfo;
    public boolean schemaIsFromAdditionalProperties;
    public boolean isBooleanSchemaTrue;
    public boolean isBooleanSchemaFalse;
    public LinkedHashMap<String, List<String>> dependentRequired;
    public CodegenSchema contains;

    public boolean hasValidation() {
        if (maxItems != null || minItems != null || minProperties != null || maxProperties != null || minLength != null || maxLength != null || multipleOf != null || pattern != null || minimum != null || maximum != null || exclusiveMinimum != null || exclusiveMaximum != null || uniqueItems != null) {
            return true;
        }
        return false;
    }

    public boolean isAnyType() {
        return types == null;
    }

    /**
     * Syncs all the schema's type properties into the OpenApiSchema instance
     * for now this only supports types without format information
     * TODO: in the future move the format handling in here too
     * @param p the schema which contains the type info
     */
    public void setTypeProperties(Schema p) {
        if (ModelUtils.isTypeObjectSchema(p)) {
            isMap = true;
        } else if (ModelUtils.isArraySchema(p)) {
            isArray = true;
        } else if (ModelUtils.isFileSchema(p) && !ModelUtils.isStringSchema(p)) {
            // swagger v2 only, type file
            ;
        } else if (ModelUtils.isStringSchema(p)) {
            isString = true;
            if (ModelUtils.isByteArraySchema(p)) {
                ;
            } else if (ModelUtils.isBinarySchema(p)) {
                // openapi v3 way of representing binary + file data
                // for backward compatibility with 2.x file type
                isString = false;
            } else if (ModelUtils.isUUIDSchema(p)) {
                // keep isString to true to make it backward compatible
                ;
            } else if (ModelUtils.isURISchema(p)) {
                ;
            } else if (ModelUtils.isEmailSchema(p)) {
                ;
            } else if (ModelUtils.isDateSchema(p)) {
                ;
            } else if (ModelUtils.isDateTimeSchema(p)) {
                ;
            } else if (ModelUtils.isDecimalSchema(p)) { // type: string, format: number
                ;
            }
        } else if (ModelUtils.isNumberSchema(p)) {
            if (ModelUtils.isFloatSchema(p)) { // float
                ;
            } else if (ModelUtils.isDoubleSchema(p)) { // double
                ;
            } else { // type is number and without format
                isNumber = true;
            }
        } else if (ModelUtils.isIntegerSchema(p)) { // integer type
            if (ModelUtils.isLongSchema(p)) { // int64/long format
                ;
            } else if (ModelUtils.isShortSchema(p)) { // int32/short format
                ;
            } else { // unbounded integer
                isUnboundedInteger = true;
            }
        } else if (ModelUtils.isBooleanSchema(p)) { // boolean type
            isBoolean = true;
        } else if (ModelUtils.isNullType(p)) {
            isNull = true;
        }
    }

    public boolean hasDiscriminatorWithNonEmptyMapping() {
        if (discriminator == null) {
            return false;
        }
        if (discriminator.mappedModels == null) {
            return false;
        } else if (discriminator.mappedModels.isEmpty()) {
            return false;
        }
        return true;
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

    public boolean isComplicated() {
        // used by templates
        if (isArray || isMap || allOf != null || anyOf != null || oneOf != null || not != null) {
            return true;
        }
        return false;
    }

    protected void addInstanceInfo(StringBuilder sb) {
        sb.append(", description='").append(description).append('\'');
        sb.append(", name='").append(name).append('\'');
        sb.append(", defaultValue='").append(defaultValue).append('\'');
        sb.append(", title='").append(title).append('\'');
        sb.append(", unescapedDescription='").append(unescapedDescription).append('\'');
        sb.append(", maxLength=").append(maxLength);
        sb.append(", minLength=").append(minLength);
        sb.append(", pattern='").append(pattern).append('\'');
        sb.append(", example='").append(example).append('\'');
        sb.append(", minimum='").append(minimum).append('\'');
        sb.append(", maximum='").append(maximum).append('\'');
        sb.append(", exclusiveMinimum=").append(exclusiveMinimum);
        sb.append(", exclusiveMaximum=").append(exclusiveMaximum);
        sb.append(", deprecated=").append(deprecated);
        sb.append(", types=").append(types);
        sb.append(", isString=").append(isString);
        sb.append(", isNumeric=").append(isNumeric);
        sb.append(", isInteger=").append(isInteger);
        sb.append(", isShort=").append(isShort);
        sb.append(", isLong=").append(isLong);
        sb.append(", isUnboundedInteger=").append(isUnboundedInteger);
        sb.append(", isNumber=").append(isNumber);
        sb.append(", isFloat=").append(isFloat);
        sb.append(", isDouble=").append(isDouble);
        sb.append(", isDecimal=").append(isDecimal);
        sb.append(", isByteArray=").append(isByteArray);
        sb.append(", isBinary=").append(isBinary);
        sb.append(", isFile=").append(isFile);
        sb.append(", isBoolean=").append(isBoolean);
        sb.append(", isDate=").append(isDate);
        sb.append(", isDateTime=").append(isDateTime);
        sb.append(", isUuid=").append(isUuid);
        sb.append(", isUri=").append(isUri);
        sb.append(", isEmail=").append(isEmail);
        sb.append(", isArray=").append(isArray);
        sb.append(", isMap=").append(isMap);
        sb.append(", isAnyType=").append(isAnyType());
        sb.append(", isReadOnly=").append(isReadOnly);
        sb.append(", isWriteOnly=").append(isWriteOnly);
        sb.append(", isNullable=").append(isNullable);
        sb.append(", isSelfReference=").append(isSelfReference);
        sb.append(", isCircularReference=").append(isCircularReference);
        sb.append(", allowableValues=").append(enumNameToValue);
        sb.append(", items=").append(items);
        sb.append(", additionalProperties=").append(additionalProperties);
        sb.append(", vendorExtensions=").append(vendorExtensions);
        sb.append(", hasValidation=").append(hasValidation());
        sb.append(", discriminatorValue='").append(discriminatorValue).append('\'');
        sb.append(", maxItems=").append(maxItems);
        sb.append(", minItems=").append(minItems);
        sb.append(", maxProperties=").append(maxProperties);
        sb.append(", minProperties=").append(minProperties);
        sb.append(", uniqueItems=").append(uniqueItems);
        sb.append(", multipleOf=").append(multipleOf);
        sb.append(", isXmlAttribute=").append(isXmlAttribute);
        sb.append(", xmlPrefix='").append(xmlPrefix).append('\'');
        sb.append(", xmlName='").append(xmlName).append('\'');
        sb.append(", xmlNamespace='").append(xmlNamespace).append('\'');
        sb.append(", isXmlWrapped=").append(isXmlWrapped);
        sb.append(", isNull=").append(isNull);
        sb.append(", hasMultipleTypes=").append(hasMultipleTypes);
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
                isString == that.isString &&
                isNumeric == that.isNumeric &&
                isInteger == that.isInteger &&
                isShort == that.isShort &&
                isLong == that.isLong &&
                isUnboundedInteger == that.isUnboundedInteger &&
                isNumber == that.isNumber &&
                isFloat == that.isFloat &&
                isDouble == that.isDouble &&
                isDecimal == that.isDecimal &&
                isByteArray == that.isByteArray &&
                isBinary == that.isBinary &&
                isFile == that.isFile &&
                isBoolean == that.isBoolean &&
                isDate == that.isDate &&
                isDateTime == that.isDateTime &&
                isUuid == that.isUuid &&
                isUri == that.isUri &&
                isEmail == that.isEmail &&
                isArray == that.isArray &&
                isMap == that.isMap &&
                isReadOnly == that.isReadOnly &&
                isWriteOnly == that.isWriteOnly &&
                isNullable == that.isNullable &&
                isSelfReference == that.isSelfReference &&
                isCircularReference == that.isCircularReference &&
                isXmlAttribute == that.isXmlAttribute &&
                isXmlWrapped == that.isXmlWrapped &&
                isNull == that.isNull &&
                hasMultipleTypes == that.hasMultipleTypes &&
                isBooleanSchemaTrue == that.isBooleanSchemaTrue &&
                isBooleanSchemaFalse == that.isBooleanSchemaFalse &&
                schemaIsFromAdditionalProperties == that.schemaIsFromAdditionalProperties &&
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
                Objects.equals(name, that.name) &&
                Objects.equals(defaultValue, that.defaultValue) &&
                Objects.equals(title, that.title) &&
                Objects.equals(unescapedDescription, that.unescapedDescription) &&
                Objects.equals(maxLength, that.maxLength) &&
                Objects.equals(minLength, that.minLength) &&
                Objects.equals(pattern, that.pattern) &&
                Objects.equals(example, that.example) &&
                Objects.equals(minimum, that.minimum) &&
                Objects.equals(maximum, that.maximum) &&
                Objects.equals(enumNameToValue, that.enumNameToValue) &&
                Objects.equals(items, that.items) &&
                Objects.equals(additionalProperties, that.additionalProperties) &&
                Objects.equals(vendorExtensions, that.vendorExtensions) &&
                Objects.equals(discriminatorValue, that.discriminatorValue) &&
                Objects.equals(maxItems, that.maxItems) &&
                Objects.equals(minItems, that.minItems) &&
                Objects.equals(xmlPrefix, that.xmlPrefix) &&
                Objects.equals(xmlName, that.xmlName) &&
                Objects.equals(xmlNamespace, that.xmlNamespace) &&
                Objects.equals(multipleOf, that.multipleOf);
    }

    @Override
    public int hashCode() {
        return Objects.hash(description,
                name, defaultValue,
                title, unescapedDescription,
                maxLength, minLength, pattern, example, minimum, maximum,
                exclusiveMinimum, exclusiveMaximum, deprecated, types,
                isString, isNumeric,
                isInteger, isLong, isNumber, isFloat, isDouble, isDecimal, isByteArray, isBinary, isFile,
                isBoolean, isDate, isDateTime, isUuid, isUri, isEmail,
                isArray, isMap, isReadOnly, isWriteOnly, isNullable, isShort,
                isUnboundedInteger, isSelfReference, isCircularReference,
                enumNameToValue, items, additionalProperties,
                vendorExtensions, discriminatorValue,
                maxItems, minItems, isXmlAttribute, xmlPrefix, xmlName,
                xmlNamespace, isXmlWrapped, isNull,
                hasMultipleTypes,
                schemaIsFromAdditionalProperties, isBooleanSchemaTrue, isBooleanSchemaFalse,
                format, dependentRequired, contains, allOf, anyOf, oneOf, not,
                properties, optionalProperties, requiredProperties, externalDocumentation,
                discriminator, imports, componentModule, testCases, refInfo);
    }
}
