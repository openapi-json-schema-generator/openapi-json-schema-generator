package org.openapijsonschematools.components.schemas;
import org.openapijsonschematools.configurations.SchemaConfiguration;
import org.openapijsonschematools.schemas.JsonSchema;
import org.openapijsonschematools.schemas.JsonSchemas;
import org.openapijsonschematools.schemas.FrozenList;
import org.openapijsonschematools.schemas.FrozenMap;

import java.time.LocalDate;
import java.time.ZonedDateTime;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Map;
public class IntegerEnumBig {
    // nest classes so all schemas and input/output classes can be public
    
    
    public record IntegerEnumBig2(LinkedHashSet<Class<?>> type) implements JsonSchema {
        /*
        NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
        Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
    
        Do not edit the class manually.
        */
        public static IntegerEnumBig2 withDefaults() {
            LinkedHashSet<Class<?>> type = new LinkedHashSet<>();
            type.add(Integer.class);
            type.add(Long.class);
            type.add(Float.class);
            type.add(Double.class);
            return new IntegerEnumBig2(type);
        }
        public static Long validate(Integer arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(IntegerEnumBig2.class, Long.valueOf(arg), configuration);
        }
        
        public static Long validate(Float arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(IntegerEnumBig2.class, Long.parseLong(arg.toString()), configuration);
        }
        
        public static Long validate(Long arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(IntegerEnumBig2.class, arg, configuration);
        }
        
        public static Long validate(Double arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(IntegerEnumBig2.class, Long.parseLong(arg.toString()), configuration);
        }
    }}
