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
public class User {
    // nest classes so all schemas and input/output classes can be public
    
    
    public record Id() implements JsonSchema {
        public static JsonSchemas.Int64Schema withDefaults() {
            return JsonSchemas.Int64Schema.withDefaults();
        }
    
        public static Long validate(Integer arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(JsonSchemas.Int64Schema.class, Long.valueOf(arg), configuration);
        }
    
        public static Long validate(Float arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(JsonSchemas.Int64Schema.class, Long.parseLong(arg.toString()), configuration);
        }
    
        public static Long validate(Long arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(JsonSchemas.Int64Schema.class, arg, configuration);
        }
    
        public static Long validate(Double arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(JsonSchemas.Int64Schema.class, Long.parseLong(arg.toString()), configuration);
        }
    }
    
    
    public record Username(LinkedHashSet<Class<?>> type) implements JsonSchema {
        public static Username withDefaults() {
            LinkedHashSet<Class<?>> type = new LinkedHashSet<>();
            type.add(String.class);
            return new Username(type);
        }
        public static String validate(String arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(Username.class, arg, configuration);
        }
    }    
    
    public record FirstName(LinkedHashSet<Class<?>> type) implements JsonSchema {
        public static FirstName withDefaults() {
            LinkedHashSet<Class<?>> type = new LinkedHashSet<>();
            type.add(String.class);
            return new FirstName(type);
        }
        public static String validate(String arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(FirstName.class, arg, configuration);
        }
    }    
    
    public record LastName(LinkedHashSet<Class<?>> type) implements JsonSchema {
        public static LastName withDefaults() {
            LinkedHashSet<Class<?>> type = new LinkedHashSet<>();
            type.add(String.class);
            return new LastName(type);
        }
        public static String validate(String arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(LastName.class, arg, configuration);
        }
    }    
    
    public record Email(LinkedHashSet<Class<?>> type) implements JsonSchema {
        public static Email withDefaults() {
            LinkedHashSet<Class<?>> type = new LinkedHashSet<>();
            type.add(String.class);
            return new Email(type);
        }
        public static String validate(String arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(Email.class, arg, configuration);
        }
    }    
    
    public record Password(LinkedHashSet<Class<?>> type) implements JsonSchema {
        public static Password withDefaults() {
            LinkedHashSet<Class<?>> type = new LinkedHashSet<>();
            type.add(String.class);
            return new Password(type);
        }
        public static String validate(String arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(Password.class, arg, configuration);
        }
    }    
    
    public record Phone(LinkedHashSet<Class<?>> type) implements JsonSchema {
        public static Phone withDefaults() {
            LinkedHashSet<Class<?>> type = new LinkedHashSet<>();
            type.add(String.class);
            return new Phone(type);
        }
        public static String validate(String arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(Phone.class, arg, configuration);
        }
    }    
    
    public record UserStatus() implements JsonSchema {
        public static JsonSchemas.Int32Schema withDefaults() {
            return JsonSchemas.Int32Schema.withDefaults();
        }
    
        public static Integer validate(Integer arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(JsonSchemas.Int32Schema.class, arg, configuration);
        }
    
        public static Integer validate(Float arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(JsonSchemas.Int32Schema.class, Integer.parseInt(arg.toString()), configuration);
        }
    }
    
    
    public record ObjectWithNoDeclaredProps() implements JsonSchema {
        public static JsonSchemas.MapSchema withDefaults() {
            return JsonSchemas.MapSchema.withDefaults();
        }
    
        public static FrozenMap<String, Object> validate(Map<String, Object> arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(JsonSchemas.MapSchema.class, arg, configuration);
        }
    }
    
    
    public record Not(LinkedHashSet<Class<?>> type) implements JsonSchema {
        public static Not withDefaults() {
            LinkedHashSet<Class<?>> type = new LinkedHashSet<>();
            type.add(Void.class);
            return new Not(type);
        }
        public static Void validate(Void arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(Not.class, arg, configuration);
        }
    }}
