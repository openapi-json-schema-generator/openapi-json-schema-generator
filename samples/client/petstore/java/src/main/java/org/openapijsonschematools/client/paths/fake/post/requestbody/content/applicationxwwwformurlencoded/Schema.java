package org.openapijsonschematools.client.paths.fake.post.requestbody.content.applicationxwwwformurlencoded;
import java.time.ZonedDateTime;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.Set;
import java.util.regex.Pattern;
import org.openapijsonschematools.client.configurations.SchemaConfiguration;
import org.openapijsonschematools.client.exceptions.ValidationException;
import org.openapijsonschematools.client.schemas.DateJsonSchema;
import org.openapijsonschematools.client.schemas.Int64JsonSchema;
import org.openapijsonschematools.client.schemas.StringJsonSchema;
import org.openapijsonschematools.client.schemas.validation.FormatValidator;
import org.openapijsonschematools.client.schemas.validation.FrozenList;
import org.openapijsonschematools.client.schemas.validation.FrozenMap;
import org.openapijsonschematools.client.schemas.validation.JsonSchema;
import org.openapijsonschematools.client.schemas.validation.JsonSchemaFactory;
import org.openapijsonschematools.client.schemas.validation.KeywordEntry;
import org.openapijsonschematools.client.schemas.validation.KeywordValidator;
import org.openapijsonschematools.client.schemas.validation.MaxLengthValidator;
import org.openapijsonschematools.client.schemas.validation.MaximumValidator;
import org.openapijsonschematools.client.schemas.validation.MinLengthValidator;
import org.openapijsonschematools.client.schemas.validation.MinimumValidator;
import org.openapijsonschematools.client.schemas.validation.NonCollectionJsonSchema;
import org.openapijsonschematools.client.schemas.validation.PatternValidator;
import org.openapijsonschematools.client.schemas.validation.PropertiesValidator;
import org.openapijsonschematools.client.schemas.validation.PropertyEntry;
import org.openapijsonschematools.client.schemas.validation.RequiredValidator;
import org.openapijsonschematools.client.schemas.validation.TypeValidator;

public class Schema {
    // nest classes so all schemas and input/output classes can be public
    
    
    public static class IntegerSchema extends NonCollectionJsonSchema {
        public IntegerSchema() {
            super(new LinkedHashMap<>(Map.ofEntries(
                new KeywordEntry("type", new TypeValidator(Set.of(
                    Integer.class,
                    Long.class,
                    Float.class,
                    Double.class
                ))),
                new KeywordEntry("maximum", new MaximumValidator(100)),
                new KeywordEntry("minimum", new MinimumValidator(10))
            )));
        }
        public int validate(int arg, SchemaConfiguration configuration) throws ValidationException {
            return validateInt(arg, configuration);
        }
        
        public float validate(float arg, SchemaConfiguration configuration) throws ValidationException {
            return validateFloat(arg, configuration);
        }
        
        public long validate(long arg, SchemaConfiguration configuration) throws ValidationException {
            return validateLong(arg, configuration);
        }
        
        public double validate(double arg, SchemaConfiguration configuration) throws ValidationException {
            return validateDouble(arg, configuration);
        }
    }    
    
    public static class Int32 extends NonCollectionJsonSchema {
        public Int32() {
            super(new LinkedHashMap<>(Map.ofEntries(
                new KeywordEntry("type", new TypeValidator(Set.of(
                    Integer.class,
                    Long.class,
                    Float.class,
                    Double.class
                ))),
                new KeywordEntry("format", new FormatValidator("int32")),
                new KeywordEntry("maximum", new MaximumValidator(200)),
                new KeywordEntry("minimum", new MinimumValidator(20))
            )));
        }
        public int validate(int arg, SchemaConfiguration configuration) throws ValidationException {
            return validateInt(arg, configuration);
        }
        
        public float validate(float arg, SchemaConfiguration configuration) throws ValidationException {
            return validateFloat(arg, configuration);
        }
        
        public long validate(long arg, SchemaConfiguration configuration) throws ValidationException {
            return validateLong(arg, configuration);
        }
        
        public double validate(double arg, SchemaConfiguration configuration) throws ValidationException {
            return validateDouble(arg, configuration);
        }
    }    
    
    public static class Int64 extends Int64JsonSchema {}
    
    
    public static class NumberSchema extends NonCollectionJsonSchema {
        public NumberSchema() {
            super(new LinkedHashMap<>(Map.ofEntries(
                new KeywordEntry("type", new TypeValidator(Set.of(
                    Integer.class,
                    Long.class,
                    Float.class,
                    Double.class
                ))),
                new KeywordEntry("maximum", new MaximumValidator(543.2)),
                new KeywordEntry("minimum", new MinimumValidator(32.1))
            )));
        }
        public int validate(int arg, SchemaConfiguration configuration) throws ValidationException {
            return validateInt(arg, configuration);
        }
        
        public long validate(long arg, SchemaConfiguration configuration) throws ValidationException {
            return validateLong(arg, configuration);
        }
        
        public float validate(float arg, SchemaConfiguration configuration) throws ValidationException {
            return validateFloat(arg, configuration);
        }
        
        public double validate(double arg, SchemaConfiguration configuration) throws ValidationException {
            return validateDouble(arg, configuration);
        }
    }    
    
    public static class FloatSchema extends NonCollectionJsonSchema {
        public FloatSchema() {
            super(new LinkedHashMap<>(Map.ofEntries(
                new KeywordEntry("type", new TypeValidator(Set.of(
                    Integer.class,
                    Long.class,
                    Float.class,
                    Double.class
                ))),
                new KeywordEntry("format", new FormatValidator("float")),
                new KeywordEntry("maximum", new MaximumValidator(987.6))
            )));
        }
        public float validate(float arg, SchemaConfiguration configuration) throws ValidationException {
            return validateFloat(arg, configuration);
        }
    }    
    
    public static class DoubleSchema extends NonCollectionJsonSchema {
        public DoubleSchema() {
            super(new LinkedHashMap<>(Map.ofEntries(
                new KeywordEntry("type", new TypeValidator(Set.of(
                    Integer.class,
                    Long.class,
                    Float.class,
                    Double.class
                ))),
                new KeywordEntry("format", new FormatValidator("double")),
                new KeywordEntry("maximum", new MaximumValidator(123.4)),
                new KeywordEntry("minimum", new MinimumValidator(67.8))
            )));
        }
        public double validate(double arg, SchemaConfiguration configuration) throws ValidationException {
            return validateDouble(arg, configuration);
        }
    }    
    
    public static class StringSchema extends NonCollectionJsonSchema {
        public StringSchema() {
            super(new LinkedHashMap<>(Map.ofEntries(
                new KeywordEntry("type", new TypeValidator(Set.of(
                    String.class
                ))),
                new KeywordEntry("pattern", new PatternValidator(Pattern.compile(
                    "[a-z]",
                    Pattern.CASE_INSENSITIVE
                )))
            )));
        }
        public String validate(String arg, SchemaConfiguration configuration) throws ValidationException {
            return validateString(arg, configuration);
        }
    }    
    
    public static class PatternWithoutDelimiter extends NonCollectionJsonSchema {
        public PatternWithoutDelimiter() {
            super(new LinkedHashMap<>(Map.ofEntries(
                new KeywordEntry("type", new TypeValidator(Set.of(
                    String.class
                ))),
                new KeywordEntry("pattern", new PatternValidator(Pattern.compile(
                    "^[A-Z].*"
                )))
            )));
        }
        public String validate(String arg, SchemaConfiguration configuration) throws ValidationException {
            return validateString(arg, configuration);
        }
    }    
    
    public static class ByteSchema extends StringJsonSchema {}
    
    
    public static class Binary extends StringJsonSchema {
        // BinarySchema
    }
    
    
    public static class Date extends DateJsonSchema {}
    
    
    public static class DateTime extends NonCollectionJsonSchema {
        public DateTime() {
            super(new LinkedHashMap<>(Map.ofEntries(
                new KeywordEntry("type", new TypeValidator(Set.of(
                    String.class
                ))),
                new KeywordEntry("format", new FormatValidator("date-time"))
            )));
        }
        public String validate(String arg, SchemaConfiguration configuration) throws ValidationException {
            return validateString(arg, configuration);
        }
    }    
    
    public static class Password extends NonCollectionJsonSchema {
        public Password() {
            super(new LinkedHashMap<>(Map.ofEntries(
                new KeywordEntry("type", new TypeValidator(Set.of(
                    String.class
                ))),
                new KeywordEntry("format", new FormatValidator("password")),
                new KeywordEntry("maxLength", new MaxLengthValidator(64)),
                new KeywordEntry("minLength", new MinLengthValidator(10))
            )));
        }
        public String validate(String arg, SchemaConfiguration configuration) throws ValidationException {
            return validateString(arg, configuration);
        }
    }    
    
    public static class Callback extends StringJsonSchema {}
    
    
    public static class SchemaMap extends FrozenMap<String, Object> {
        SchemaMap(FrozenMap<String, Object> m) {
            super(m);
        }
        public static final Set<String> requiredKeys = Set.of(
            "byte",
            "double",
            "number",
            "pattern_without_delimiter"
        );
        public static final Set<String> optionalKeys = Set.of(
            "integer",
            "int32",
            "int64",
            "float",
            "string",
            "binary",
            "date",
            "dateTime",
            "password",
            "callback"
        );
        public static SchemaMap of(Map<String, Object> arg, SchemaConfiguration configuration) throws ValidationException {
            return JsonSchemaFactory.getInstance(Schema1.class).validate(arg, configuration);
        }
        
        public String pattern_without_delimiter() {
            return (String) get("pattern_without_delimiter");
        }
        
        public int int32() {
            String key = "int32";
            throwIfKeyNotPresent(key);
            return (int) get(key);
        }
        
        public long int64() {
            String key = "int64";
            throwIfKeyNotPresent(key);
            return (long) get(key);
        }
        
        public String binary() {
            String key = "binary";
            throwIfKeyNotPresent(key);
            return (String) get(key);
        }
        
        public String date() {
            String key = "date";
            throwIfKeyNotPresent(key);
            return (String) get(key);
        }
        
        public String dateTime() {
            String key = "dateTime";
            throwIfKeyNotPresent(key);
            return (String) get(key);
        }
        
        public String password() {
            String key = "password";
            throwIfKeyNotPresent(key);
            return (String) get(key);
        }
        
        public String callback() {
            String key = "callback";
            throwIfKeyNotPresent(key);
            return (String) get(key);
        }
        
        public Object getAdditionalProperty(String name) {
            throwIfKeyKnown(name, requiredKeys, optionalKeys);
            throwIfKeyNotPresent(name);
            return get(name);
        }
    }
    public class SchemaMapInput {
        // Map<String, Object> because addProps is unset
    }
    
    
    public static class Schema1 extends JsonSchema<Object, Object, SchemaMap, Object, Object, FrozenList<Object>> {
        public Schema1() {
            super(new LinkedHashMap<>(Map.ofEntries(
                new KeywordEntry("type", new TypeValidator(Set.of(FrozenMap.class))),
                new KeywordEntry("properties", new PropertiesValidator(Map.ofEntries(
                    new PropertyEntry("integer", IntegerSchema.class),
                    new PropertyEntry("int32", Int32.class),
                    new PropertyEntry("int64", Int64.class),
                    new PropertyEntry("number", NumberSchema.class),
                    new PropertyEntry("float", FloatSchema.class),
                    new PropertyEntry("double", DoubleSchema.class),
                    new PropertyEntry("string", StringSchema.class),
                    new PropertyEntry("pattern_without_delimiter", PatternWithoutDelimiter.class),
                    new PropertyEntry("byte", ByteSchema.class),
                    new PropertyEntry("binary", Binary.class),
                    new PropertyEntry("date", Date.class),
                    new PropertyEntry("dateTime", DateTime.class),
                    new PropertyEntry("password", Password.class),
                    new PropertyEntry("callback", Callback.class)
                ))),
                new KeywordEntry("required", new RequiredValidator(Set.of(
                    "byte",
                    "double",
                    "number",
                    "pattern_without_delimiter"
                )))
            )));
        }
        
        @Override
        protected SchemaMap getMapOutputInstance(FrozenMap<String, Object> arg) {
            return new SchemaMap(arg);
        }
        public SchemaMap validate(Map<String, Object> arg, SchemaConfiguration configuration) throws ValidationException {
            return validateMap(arg, configuration);
        }
    }
}
