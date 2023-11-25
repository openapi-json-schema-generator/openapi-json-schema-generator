package org.openapijsonschematools.components.schemas;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.Set;
import org.openapijsonschematools.configurations.SchemaConfiguration;
import org.openapijsonschematools.exceptions.ValidationException;
import org.openapijsonschematools.schemas.AnyTypeJsonSchema;
import org.openapijsonschematools.schemas.NotAnyTypeJsonSchema;
import org.openapijsonschematools.schemas.NumberJsonSchema;
import org.openapijsonschematools.schemas.StringJsonSchema;
import org.openapijsonschematools.schemas.validation.AdditionalPropertiesValidator;
import org.openapijsonschematools.schemas.validation.FrozenMap;
import org.openapijsonschematools.schemas.validation.JsonSchema;
import org.openapijsonschematools.schemas.validation.KeywordEntry;
import org.openapijsonschematools.schemas.validation.KeywordValidator;
import org.openapijsonschematools.schemas.validation.PropertiesValidator;
import org.openapijsonschematools.schemas.validation.PropertyEntry;
import org.openapijsonschematools.schemas.validation.TypeValidator;

public class ObjectWithOnlyOptionalProps {
    // nest classes so all schemas and input/output classes can be public
    
    
    public class AdditionalProperties extends NotAnyTypeJsonSchema {}
        // NotAnyTypeSchema
    
    
    public class A extends StringJsonSchema {}
    
    
    public class B extends NumberJsonSchema {}
    
    
    public static class ObjectWithOnlyOptionalPropsMap extends FrozenMap<String, Object> {

        ObjectWithOnlyOptionalPropsMap(FrozenMap<String, Object> m) {

            super(m);
        }
        public static final Set<String> requiredKeys = Set.of();
        public static final Set<String> optionalKeys = Set.of(
            "a",
            "b"
        );
        public static ObjectWithOnlyOptionalPropsMap of(Map<String, Object> arg, SchemaConfiguration configuration) {

            return ObjectWithOnlyOptionalProps1.validate(arg, configuration);
        }
        
        public String a() {

            String key = "a";
            throwIfKeyNotPresent(key);
            return (String) get(key);

        }
        
        public Number b() {

            String key = "b";
            throwIfKeyNotPresent(key);
            return (Number) get(key);

        }
    }    
    
    public class ObjectWithOnlyOptionalProps1 extends JsonSchema {
        /*
        NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
        Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
    
        Do not edit the class manually.
        */
        public static final LinkedHashMap<String, KeywordValidator> keywordToValidator = new LinkedHashMap<>(Map.ofEntries(
            new KeywordEntry("type", new TypeValidator(Set.of(FrozenMap.class))),
            new KeywordEntry("properties", new PropertiesValidator(Map.ofEntries(
                new PropertyEntry("a", A.class),
                new PropertyEntry("b", B.class)
            ))),
            new KeywordEntry("additionalProperties", new AdditionalPropertiesValidator(AdditionalProperties.class))
        ));
        protected static ObjectWithOnlyOptionalPropsMap getMapOutputInstance(FrozenMap<String, Object> arg) {

            return new ObjectWithOnlyOptionalPropsMap(arg);
        }
        public static ObjectWithOnlyOptionalPropsMap validate(Map<String, Object> arg, SchemaConfiguration configuration) throws ValidationException {

            return JsonSchema.validate(ObjectWithOnlyOptionalProps1.class, arg, configuration);
        }
    }
}
