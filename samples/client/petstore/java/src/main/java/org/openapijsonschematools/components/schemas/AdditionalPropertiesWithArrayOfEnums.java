package org.openapijsonschematools.components.schemas;
import org.openapijsonschematools.configurations.SchemaConfiguration;
import org.openapijsonschematools.schemas.JsonSchema;
import org.openapijsonschematools.schemas.JsonSchemas;
import org.openapijsonschematools.schemas.FrozenList;
import org.openapijsonschematools.schemas.FrozenMap;

import java.time.LocalDate;
import java.time.ZonedDateTime;
import java.util.LinkedHashMap;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

public class AdditionalPropertiesWithArrayOfEnums {
    // nest classes so all schemas and input/output classes can be public
    
    
    public record AdditionalProperties(LinkedHashSet<Class<?>> type, Class<?> items) implements JsonSchema {
        public static AdditionalProperties withDefaults() {
            LinkedHashSet<Class<?>> type = new LinkedHashSet<>();
            type.add(FrozenList.class);
            Class<?> items = EnumClass.EnumClass1.class;
            return new AdditionalProperties(type, items);
        }
        public static <U extends FrozenList> U validate(List<Object> arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(AdditionalProperties.class, arg, configuration);
        }
    }    
    
    public record AdditionalPropertiesWithArrayOfEnums1(LinkedHashSet<Class<?>> type, Class<?> additionalProperties) implements JsonSchema {
        /*
        NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
        Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
    
        Do not edit the class manually.
        */
        public static AdditionalPropertiesWithArrayOfEnums1 withDefaults() {
            LinkedHashSet<Class<?>> type = new LinkedHashSet<>();
            type.add(FrozenMap.class);
            Class<?> additionalProperties = AdditionalProperties.class;
            return new AdditionalPropertiesWithArrayOfEnums1(type, additionalProperties);
        }
        public static <T extends FrozenMap> T validate(Map<String, Object> arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(AdditionalPropertiesWithArrayOfEnums1.class, arg, configuration);
        }
    }
}
