package org.openapijsonschematools.paths.fake.post.requestbody.content.applicationxwwwformurlencoded;
import java.time.ZonedDateTime;
import java.util.AbstractMap;
import java.util.LinkedHashMap;
import java.util.LinkedHashSet;
import java.util.Map;
import java.util.Set;
import org.openapijsonschematools.configurations.SchemaConfiguration;
import org.openapijsonschematools.schemas.DateJsonSchema;
import org.openapijsonschematools.schemas.Int64JsonSchema;
import org.openapijsonschematools.schemas.StringJsonSchema;
import org.openapijsonschematools.schemas.validation.FrozenMap;
import org.openapijsonschematools.schemas.validation.JsonSchema;

public class Schema {
    // nest classes so all schemas and input/output classes can be public
    
    
    public class IntegerSchema extends JsonSchema {
        public static final LinkedHashSet<Class<?>> type = new LinkedHashSet<>(Set.of(
            Integer.class,
            Long.class,
            Float.class,
            Double.class
        ));
        public static Long validate(Integer arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(IntegerSchema.class, Long.valueOf(arg), configuration);
        }
        
        public static Long validate(Float arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(IntegerSchema.class, Long.parseLong(arg.toString()), configuration);
        }
        
        public static Long validate(Long arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(IntegerSchema.class, arg, configuration);
        }
        
        public static Long validate(Double arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(IntegerSchema.class, Long.parseLong(arg.toString()), configuration);
        }
    }    
    
    public class Int32 extends JsonSchema {
        public static final LinkedHashSet<Class<?>> type = new LinkedHashSet<>(Set.of(
            Integer.class,
            Long.class,
            Float.class,
            Double.class
        ));
        public static final String format = "int32";
        public static Long validate(Integer arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(Int32.class, Long.valueOf(arg), configuration);
        }
        
        public static Long validate(Float arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(Int32.class, Long.parseLong(arg.toString()), configuration);
        }
        
        public static Long validate(Long arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(Int32.class, arg, configuration);
        }
        
        public static Long validate(Double arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(Int32.class, Long.parseLong(arg.toString()), configuration);
        }
    }    
    
    public class Int64 extends Int64JsonSchema {}
    
    
    public class NumberSchema extends JsonSchema {
        public static final LinkedHashSet<Class<?>> type = new LinkedHashSet<>(Set.of(
            Integer.class,
            Long.class,
            Float.class,
            Double.class
        ));
        public static Number validate(Integer arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(NumberSchema.class, arg, configuration);
        }
        
        public static Number validate(Long arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(NumberSchema.class, arg, configuration);
        }
        
        public static Number validate(Float arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(NumberSchema.class, arg, configuration);
        }
        
        public static Number validate(Double arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(NumberSchema.class, arg, configuration);
        }
    }    
    
    public class FloatSchema extends JsonSchema {
        public static final LinkedHashSet<Class<?>> type = new LinkedHashSet<>(Set.of(
            Integer.class,
            Long.class,
            Float.class,
            Double.class
        ));
        public static final String format = "float";
        public static Float validate(Float arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(FloatSchema.class, arg, configuration);
        }
    }    
    
    public class DoubleSchema extends JsonSchema {
        public static final LinkedHashSet<Class<?>> type = new LinkedHashSet<>(Set.of(
            Integer.class,
            Long.class,
            Float.class,
            Double.class
        ));
        public static final String format = "double";
        public static Double validate(Double arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(DoubleSchema.class, arg, configuration);
        }
    }    
    
    public class StringSchema extends JsonSchema {
        public static final LinkedHashSet<Class<?>> type = new LinkedHashSet<>(Set.of(
            String.class
        ));
        public static String validate(String arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(StringSchema.class, arg, configuration);
        }
    }    
    
    public class PatternWithoutDelimiter extends JsonSchema {
        public static final LinkedHashSet<Class<?>> type = new LinkedHashSet<>(Set.of(
            String.class
        ));
        public static String validate(String arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(PatternWithoutDelimiter.class, arg, configuration);
        }
    }    
    
    public class ByteSchema extends StringJsonSchema {}
    
    
    public class Binary extends JsonSchema {
        // BinarySchema
    }
    
    
    public class Date extends DateJsonSchema {}
    
    
    public class DateTime extends JsonSchema {
        public static final LinkedHashSet<Class<?>> type = new LinkedHashSet<>(Set.of(
            String.class
        ));
        public static final String format = "date-time";
        public static String validate(String arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(DateTime.class, arg, configuration);
        }
    }    
    
    public class Password extends JsonSchema {
        public static final LinkedHashSet<Class<?>> type = new LinkedHashSet<>(Set.of(
            String.class
        ));
        public static final String format = "password";
        public static String validate(String arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(Password.class, arg, configuration);
        }
    }    
    
    public class Callback extends StringJsonSchema {}
    
    
    public static class SchemaMap extends FrozenMap<String, Object> {
        SchemaMap(FrozenMap<? extends String, ?> m) {
            super(m);
        }
        public static SchemaMap of(Map<String, Object> arg, SchemaConfiguration configuration) {
            return Schema1.validate(arg, configuration);
        }
    }    
    
    public class Schema1 extends JsonSchema {
        public static final LinkedHashSet<Class<?>> type = new LinkedHashSet<>(Set.of(
            FrozenMap.class
        ));
        public static final LinkedHashMap<String, Class<?>> properties = new LinkedHashMap<>(Map.ofEntries(
            new AbstractMap.SimpleEntry<String, Class<?>>("integer", IntegerSchema.class),
            new AbstractMap.SimpleEntry<String, Class<?>>("int32", Int32.class),
            new AbstractMap.SimpleEntry<String, Class<?>>("int64", Int64.class),
            new AbstractMap.SimpleEntry<String, Class<?>>("number", NumberSchema.class),
            new AbstractMap.SimpleEntry<String, Class<?>>("float", FloatSchema.class),
            new AbstractMap.SimpleEntry<String, Class<?>>("double", DoubleSchema.class),
            new AbstractMap.SimpleEntry<String, Class<?>>("string", StringSchema.class),
            new AbstractMap.SimpleEntry<String, Class<?>>("pattern_without_delimiter", PatternWithoutDelimiter.class),
            new AbstractMap.SimpleEntry<String, Class<?>>("byte", ByteSchema.class),
            new AbstractMap.SimpleEntry<String, Class<?>>("binary", Binary.class),
            new AbstractMap.SimpleEntry<String, Class<?>>("date", Date.class),
            new AbstractMap.SimpleEntry<String, Class<?>>("dateTime", DateTime.class),
            new AbstractMap.SimpleEntry<String, Class<?>>("password", Password.class),
            new AbstractMap.SimpleEntry<String, Class<?>>("callback", Callback.class)
        ));
        public static final Set<String> required = new LinkedHashSet<>(Set.of(
            "byte",
            "double",
            "number",
            "pattern_without_delimiter"
        ));
        protected static SchemaMap getMapOutputInstance(FrozenMap<? extends String, ?> arg) {
            return new SchemaMap(arg);
        }
        public static SchemaMap validate(Map<String, Object> arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(Schema1.class, arg, configuration);
        }
    }
}
