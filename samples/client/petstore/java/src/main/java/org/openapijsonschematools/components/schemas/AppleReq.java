package org.openapijsonschematools.components.schemas;
import org.openapijsonschematools.configurations.SchemaConfiguration;
import org.openapijsonschematools.schemas.Schema;
import org.openapijsonschematools.schemas.AnyTypeSchema;

import java.util.LinkedHashSet;
public class AppleReq {
    // nest classes so all schemas and input/output classes can be public
    public record class AdditionalProperties implements Schema {
        public static NotAnyTypeSchema withDefaults() {
            return NotAnyTypeSchema.withDefaults();
        }
    
        // NotAnyTypeSchema
    }
    
    
    public record Cultivar(LinkedHashSet<Class<?>> type) implements Schema {
        public static Cultivar withDefaults() {
            LinkedHashSet<Class<?>> type = new LinkedHashSet<>();
            type.add(String.class);
            return new Cultivar(type);
        }
    }    public record class Mealy implements Schema {
        public static BooleanSchema withDefaults() {
            return BooleanSchema.withDefaults();
        }
    
        public static Boolean validate(Boolean arg, SchemaConfiguration configuration) {
            return Schema.validate(BooleanSchema.class, arg, configuration);
        }
    }
}
