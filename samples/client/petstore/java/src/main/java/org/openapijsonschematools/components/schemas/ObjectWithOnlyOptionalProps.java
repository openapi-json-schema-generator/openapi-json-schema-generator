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
public class ObjectWithOnlyOptionalProps {
    // nest classes so all schemas and input/output classes can be public
    
    
    public record AdditionalProperties() implements JsonSchema {
        public static JsonSchemas.NotAnyTypeSchema withDefaults() {
            return JsonSchemas.NotAnyTypeSchema.withDefaults();
        }
    
        // NotAnyTypeSchema
    }
    
    
    public record A(LinkedHashSet<Class<?>> type) implements JsonSchema {
        public static A withDefaults() {
            LinkedHashSet<Class<?>> type = new LinkedHashSet<>();
            type.add(String.class);
            return new A(type);
        }
        public static String validate(String arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(A.class, arg, configuration);
        }
    }    
    
    public record B() implements JsonSchema {
        public static JsonSchemas.NumberSchema withDefaults() {
            return JsonSchemas.NumberSchema.withDefaults();
        }
    
        public static Number validate(Integer arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(JsonSchemas.NumberSchema.class, arg, configuration);
        }
    
        public static Number validate(Long arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(JsonSchemas.NumberSchema.class, arg, configuration);
        }
    
        public static Number validate(Float arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(JsonSchemas.NumberSchema.class, arg, configuration);
        }
    
        public static Number validate(Double arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(JsonSchemas.NumberSchema.class, arg, configuration);
        }
    }
}
