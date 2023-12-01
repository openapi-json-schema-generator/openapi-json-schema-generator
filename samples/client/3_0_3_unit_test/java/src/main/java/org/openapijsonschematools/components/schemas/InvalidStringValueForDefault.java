package org.openapijsonschematools.components.schemas;
import java.time.LocalDate;
import java.time.ZonedDateTime;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.UUID;
import org.openapijsonschematools.configurations.SchemaConfiguration;
import org.openapijsonschematools.exceptions.ValidationException;
import org.openapijsonschematools.schemas.validation.FrozenList;
import org.openapijsonschematools.schemas.validation.FrozenMap;
import org.openapijsonschematools.schemas.validation.JsonSchema;
import org.openapijsonschematools.schemas.validation.KeywordEntry;
import org.openapijsonschematools.schemas.validation.KeywordValidator;
import org.openapijsonschematools.schemas.validation.MinLengthValidator;
import org.openapijsonschematools.schemas.validation.PropertiesValidator;
import org.openapijsonschematools.schemas.validation.PropertyEntry;
import org.openapijsonschematools.schemas.validation.TypeValidator;

public class InvalidStringValueForDefault {
    // nest classes so all schemas and input/output classes can be public
    
    
    public static class Bar extends JsonSchema {
        public static final LinkedHashMap<String, KeywordValidator> keywordToValidator = new LinkedHashMap<>(Map.ofEntries(
            new KeywordEntry("type", new TypeValidator(Set.of(
                String.class
            ))),
            new KeywordEntry("minLength", new MinLengthValidator(4))
        ));
        public static String validate(String arg, SchemaConfiguration configuration) throws ValidationException {
            return JsonSchema.validateString(Bar.class, arg, configuration);
        }
    }    
    
    public static class InvalidStringValueForDefaultMap extends FrozenMap<String, Object> {
        InvalidStringValueForDefaultMap(FrozenMap<String, Object> m) {
            super(m);
        }
        public static final Set<String> requiredKeys = Set.of();
        public static final Set<String> optionalKeys = Set.of(
            "bar"
        );
        public static InvalidStringValueForDefaultMap of(Map<String, Object> arg, SchemaConfiguration configuration) throws ValidationException {
            return InvalidStringValueForDefault1.validate(arg, configuration);
        }
        
        public String bar() {
            String key = "bar";
            throwIfKeyNotPresent(key);
            return (String) get(key);
        }
        
        public Object getAdditionalProperty(String name) {
            throwIfKeyKnown(name, requiredKeys, optionalKeys);
            throwIfKeyNotPresent(name);
            return get(name);
        }
    }    
    
    public static class InvalidStringValueForDefault1 extends JsonSchema {
        /*
        NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
        Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
    
        Do not edit the class manually.
        */
        public static final LinkedHashMap<String, KeywordValidator> keywordToValidator = new LinkedHashMap<>(Map.ofEntries(
            new KeywordEntry("properties", new PropertiesValidator(Map.ofEntries(
                new PropertyEntry("bar", Bar.class)
            )))
        ));
        
        protected static InvalidStringValueForDefaultMap getMapOutputInstance(FrozenMap<String, Object> arg) {
            return new InvalidStringValueForDefaultMap(arg);
        }
        public static Void validate(Void arg, SchemaConfiguration configuration) throws ValidationException {
            return JsonSchema.validateVoid(InvalidStringValueForDefault1.class, arg, configuration);
        }
        
        public static boolean validate(boolean arg, SchemaConfiguration configuration) throws ValidationException {
            return JsonSchema.validateBoolean(InvalidStringValueForDefault1.class, arg, configuration);
        }
        
        public static int validate(int arg, SchemaConfiguration configuration) throws ValidationException {
            return JsonSchema.validateInt(InvalidStringValueForDefault1.class, arg, configuration);
        }
        
        public static long validate(long arg, SchemaConfiguration configuration) throws ValidationException {
            return JsonSchema.validateLong(InvalidStringValueForDefault1.class, arg, configuration);
        }
        
        public static float validate(float arg, SchemaConfiguration configuration) throws ValidationException {
            return JsonSchema.validateFloat(InvalidStringValueForDefault1.class, arg, configuration);
        }
        
        public static double validate(double arg, SchemaConfiguration configuration) throws ValidationException {
            return JsonSchema.validateDouble(InvalidStringValueForDefault1.class, arg, configuration);
        }
        
        public static String validate(String arg, SchemaConfiguration configuration) throws ValidationException {
            return JsonSchema.validateString(InvalidStringValueForDefault1.class, arg, configuration);
        }
        
        public static String validate(ZonedDateTime arg, SchemaConfiguration configuration) throws ValidationException {
            return JsonSchema.validateZonedDateTime(InvalidStringValueForDefault1.class, arg, configuration);
        }
        
        public static String validate(LocalDate arg, SchemaConfiguration configuration) throws ValidationException {
            return JsonSchema.validateLocalDate(InvalidStringValueForDefault1.class, arg, configuration);
        }
        
        public static String validate(UUID arg, SchemaConfiguration configuration) throws ValidationException {
            return JsonSchema.validateUUID(InvalidStringValueForDefault1.class, arg, configuration);
        }
        
        public static InvalidStringValueForDefaultMap validate(Map<String, Object> arg, SchemaConfiguration configuration) throws ValidationException {
            return JsonSchema.validateMap(InvalidStringValueForDefault1.class, arg, configuration);
        }
        
        public static FrozenList<Object> validate(List<Object> arg, SchemaConfiguration configuration) throws ValidationException {
            return JsonSchema.validateList(InvalidStringValueForDefault1.class, arg, configuration);
        }
    }}
