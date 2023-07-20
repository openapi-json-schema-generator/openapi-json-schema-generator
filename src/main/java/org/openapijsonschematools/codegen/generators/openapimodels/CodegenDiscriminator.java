package org.openapijsonschematools.codegen.generators.openapimodels;

import java.util.Map;
import java.util.Objects;
import java.util.TreeSet;

/**
 * This class encapsulates the OpenAPI discriminator construct, as specified at
 * https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.3.md#discriminatorObject.
 *
 * When request bodies or response payloads may be one of a number of different schemas,
 * a discriminator object can be used to aid in serialization, deserialization, and validation.
 * The discriminator is a specific object in a schema which is used to inform the consumer of
 * the specification of an alternative schema based on the value associated with it.
 */
public class CodegenDiscriminator {
    // The name of the property in the payload that will hold the discriminator value.
    // This is the propertyName as specified in the OpenAPI discriminator object.
    public final CodegenKey propertyName;
    public final Map<String, String> mapping;

    // mappedModels is populated differently if legacyDiscriminatorBehavior is
    // True or False. When:
    //
    // legacyDiscriminatorBehavior == False, this contains:
    // - the name to schema map info in the discriminator mapping entry in your openapi spec OR
    // - child schemas that allOf inherit self schema
    //
    // legacyDiscriminatorBehavior == True, this contains:
    // - the name to schema map info in the discriminMappedModelator mapping entry in your openapi spec AND
    // - x-discriminator-value mappings in child oneOf + anyOf schemas + descendant schemas that allOf inherit self schema AND
    // - descendant schemas that allOf inherit self schema AND
    // - child oneOf + anyOf schemas
    //
    // see the method createDiscriminator in DefaultGenerator.java

    public final TreeSet<MappedModel> mappedModels;

    public CodegenDiscriminator(CodegenKey propertyName, Map<String, String> mapping, TreeSet<MappedModel> mappedModels) {
        this.propertyName = propertyName;
        this.mapping = mapping;
        this.mappedModels = mappedModels;
    }


    /**
     * An object to hold discriminator mappings between payload values and schema names or
     * references.
     *
     * In the OpenAPI document, the discriminator "mapping" attribute is optional.
     * In scenarios where the value of the discriminator field does not match the schema name
     * or implicit mapping is not possible, an optional mapping definition MAY be used.
     * In OpenAPITools codegen, the MappedModel is the union of all the discriminator mappings,
     * both explicitly defined in the OpenAPI document and inherited from oneOf/allOf/anyOf.
     */
    public static class MappedModel implements Comparable<MappedModel>{
        // The value of the discriminator property in the payload.
        public final String mappingName;
        // The OAS schema name. It is obtained from the OAS document, and the string value
        // is converted to a sanitized, internal representation within codegen.
        public final String modelName;

        public MappedModel(String mappingName, String modelName) {
            this.mappingName = mappingName;
            this.modelName = modelName;
        }

        @Override
        public int compareTo(MappedModel other) {
            if (mappingName == null && other.mappingName == null) {
                return 0;
            } else if (mappingName == null) {
                return 1;
            } else if (other.mappingName == null) {
                return -1;
            }
            return mappingName.compareTo(other.mappingName);
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;
            MappedModel that = (MappedModel) o;
            return Objects.equals(mappingName, that.mappingName) &&
                    Objects.equals(modelName, that.modelName);
        }

        @Override
        public int hashCode() {
            return Objects.hash(mappingName, modelName);
        }
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        CodegenDiscriminator that = (CodegenDiscriminator) o;
        return Objects.equals(propertyName, that.propertyName) &&
                Objects.equals(mapping, that.mapping) &&
                Objects.equals(mappedModels, that.mappedModels);
    }

    @Override
    public int hashCode() {
        return Objects.hash(propertyName, mapping, mappedModels);
    }

    @Override
    public String toString() {
        final StringBuffer sb = new StringBuffer("CodegenDiscriminator{");
        sb.append("propertyName='").append(propertyName).append('\'');
        sb.append(", mapping=").append(mapping);
        sb.append(", mappedModels=").append(mappedModels);
        sb.append('}');
        return sb.toString();
    }
}