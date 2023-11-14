package org.openapijsonschematools.components.schemas;
import org.openapijsonschematools.configurations.SchemaConfiguration;
import org.openapijsonschematools.schemas.Schema;
import org.openapijsonschematools.schemas.AnyTypeSchema;

import java.util.LinkedHashSet;
public class ComposedOneOfDifferentTypes {
    // nest classes so all schemas and input/output classes can be public
    
    
    public record Schema2(LinkedHashSet<Class<?>> type) implements Schema {
        public static Schema2 withDefaults() {
            LinkedHashSet<Class<?>> type = new LinkedHashSet<>();
                type(None),
            return new Schema2(type);
        }
    }    
    
    public record Schema3(LinkedHashSet<Class<?>> type) implements Schema {
        public static Schema3 withDefaults() {
            LinkedHashSet<Class<?>> type = new LinkedHashSet<>();
            type.add(String.class);
            return new Schema3(type);
        }
    }    public record class Items implements Schema {
        public static AnyTypeSchema withDefaults() {
            return AnyTypeSchema.withDefaults();
        }
    
        public static Void validate(Void arg, SchemaConfiguration configuration) {
            return Schema.validate(AnyTypeSchema.class, arg, configuration);
        }
    
        public static Boolean validate(Boolean arg, SchemaConfiguration configuration) {
            return Schema.validate(AnyTypeSchema.class, arg, configuration);
        }
    
        public static Integer validate(Integer arg, SchemaConfiguration configuration) {
            return Schema.validate(AnyTypeSchema.class, arg, configuration);
        }
    
        public static Long validate(Long arg, SchemaConfiguration configuration) {
            return Schema.validate(AnyTypeSchema.class, arg, configuration);
        }
    
        public static Float validate(Float arg, SchemaConfiguration configuration) {
            return Schema.validate(AnyTypeSchema.class, arg, configuration);
        }
    
        public static Double validate(Double arg, SchemaConfiguration configuration) {
            return Schema.validate(AnyTypeSchema.class, arg, configuration);
        }
    
        public static String validate(String arg, SchemaConfiguration configuration) {
            return Schema.validate(AnyTypeSchema.class, arg, configuration);
        }
    
        public static String validate(ZonedDateTime arg, SchemaConfiguration configuration) {
            return Schema.validate(AnyTypeSchema.class, arg, configuration);
        }
    
        public static String validate(LocalDate arg, SchemaConfiguration configuration) {
            return Schema.validate(AnyTypeSchema.class, arg, configuration);
        }
    
        public static <T extends FrozenMap> T validate(Map<String, Object> arg, SchemaConfiguration configuration) {
            return Schema.validate(AnyTypeSchema.class, arg, configuration);
        }
    
        public static <U extends FrozenList> U validate(List<Object> arg, SchemaConfiguration configuration) {
            return Schema.validate(AnyTypeSchema.class, arg, configuration);
        }
    }
    
    
    public record Schema6(LinkedHashSet<Class<?>> type) implements Schema {
        public static Schema6 withDefaults() {
            LinkedHashSet<Class<?>> type = new LinkedHashSet<>();
            type.add(String.class);
            return new Schema6(type);
        }
    }}
