package org.openapijsonschematools.components.schemas;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.Set;
import org.openapijsonschematools.configurations.SchemaConfiguration;
import org.openapijsonschematools.exceptions.ValidationException;
import org.openapijsonschematools.schemas.validation.FrozenMap;
import org.openapijsonschematools.schemas.validation.JsonSchema;
import org.openapijsonschematools.schemas.validation.KeywordEntry;
import org.openapijsonschematools.schemas.validation.KeywordValidator;
import org.openapijsonschematools.schemas.validation.MaximumValidator;
import org.openapijsonschematools.schemas.validation.PropertiesValidator;
import org.openapijsonschematools.schemas.validation.PropertyEntry;
import org.openapijsonschematools.schemas.validation.TypeValidator;

public class TheDefaultKeywordDoesNotDoAnythingIfThePropertyIsMissing {
    // nest classes so all schemas and input/output classes can be public
    
    
    public static class Alpha extends JsonSchema {
        public static final LinkedHashMap<String, KeywordValidator> keywordToValidator = new LinkedHashMap<>(Map.ofEntries(
            new KeywordEntry("type", new TypeValidator(Set.of(
                Integer.class,
                Long.class,
                Float.class,
                Double.class
            ))),
            new KeywordEntry("maximum", new MaximumValidator(3))
        ));
        public static Number validate(int arg, SchemaConfiguration configuration) throws ValidationException {
            return JsonSchema.validate(Alpha.class, arg, configuration);
        }
        
        public static Number validate(long arg, SchemaConfiguration configuration) throws ValidationException {
            return JsonSchema.validate(Alpha.class, arg, configuration);
        }
        
        public static Number validate(float arg, SchemaConfiguration configuration) throws ValidationException {
            return JsonSchema.validate(Alpha.class, arg, configuration);
        }
        
        public static Number validate(double arg, SchemaConfiguration configuration) throws ValidationException {
            return JsonSchema.validate(Alpha.class, arg, configuration);
        }
    }    
    
    public static class TheDefaultKeywordDoesNotDoAnythingIfThePropertyIsMissingMap extends FrozenMap<String, Object> {
        TheDefaultKeywordDoesNotDoAnythingIfThePropertyIsMissingMap(FrozenMap<String, Object> m) {
            super(m);
        }
        public static final Set<String> requiredKeys = Set.of();
        public static final Set<String> optionalKeys = Set.of(
            "alpha"
        );
        public static TheDefaultKeywordDoesNotDoAnythingIfThePropertyIsMissingMap of(Map<String, Object> arg, SchemaConfiguration configuration) throws ValidationException {
            return TheDefaultKeywordDoesNotDoAnythingIfThePropertyIsMissing1.validate(arg, configuration);
        }
        
        public Number alpha() {
            String key = "alpha";
            throwIfKeyNotPresent(key);
            return (Number) get(key);
        }
        
        public Object getAdditionalProperty(String name) {
            throwIfKeyKnown(name, requiredKeys, optionalKeys);
            throwIfKeyNotPresent(name);
            return get(name);
        }
    }    
    
    public static class TheDefaultKeywordDoesNotDoAnythingIfThePropertyIsMissing1 extends JsonSchema {
        /*
        NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
        Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
    
        Do not edit the class manually.
        */
        public static final LinkedHashMap<String, KeywordValidator> keywordToValidator = new LinkedHashMap<>(Map.ofEntries(
            new KeywordEntry("type", new TypeValidator(Set.of(FrozenMap.class))),
            new KeywordEntry("properties", new PropertiesValidator(Map.ofEntries(
                new PropertyEntry("alpha", Alpha.class)
            )))
        ));
        protected static TheDefaultKeywordDoesNotDoAnythingIfThePropertyIsMissingMap getMapOutputInstance(FrozenMap<String, Object> arg) {
            return new TheDefaultKeywordDoesNotDoAnythingIfThePropertyIsMissingMap(arg);
        }
        public static TheDefaultKeywordDoesNotDoAnythingIfThePropertyIsMissingMap validate(Map<String, Object> arg, SchemaConfiguration configuration) throws ValidationException {
            return JsonSchema.validate(TheDefaultKeywordDoesNotDoAnythingIfThePropertyIsMissing1.class, arg, configuration);
        }
    }
}
