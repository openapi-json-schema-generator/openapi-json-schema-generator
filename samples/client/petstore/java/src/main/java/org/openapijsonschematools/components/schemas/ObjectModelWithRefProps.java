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
import org.openapijsonschematools.schemas.validation.PropertiesValidator;
import org.openapijsonschematools.schemas.validation.PropertyEntry;
import org.openapijsonschematools.schemas.validation.TypeValidator;

public class ObjectModelWithRefProps {
    // nest classes so all schemas and input/output classes can be public
    
    
    public static class ObjectModelWithRefPropsMap extends FrozenMap<String, Object> {

        ObjectModelWithRefPropsMap(FrozenMap<String, Object> m) {

            super(m);
        }
        public static final Set<String> requiredKeys = Set.of();
        public static final Set<String> optionalKeys = Set.of(
            "myNumber",
            "myString",
            "myBoolean"
        );
        public static ObjectModelWithRefPropsMap of(Map<String, Object> arg, SchemaConfiguration configuration) throws ValidationException {
            return ObjectModelWithRefProps1.validate(arg, configuration);
        }
        
        public Number myNumber() {

            String key = "myNumber";
            throwIfKeyNotPresent(key);
            return (Number) get(key);

        }
        
        public String myString() {

            String key = "myString";
            throwIfKeyNotPresent(key);
            return (String) get(key);

        }
        
        public boolean myBoolean() {

            String key = "myBoolean";
            throwIfKeyNotPresent(key);
            return (boolean) get(key);

        }
        
        public Object getAdditionalProperty(String name) {
            throwIfKeyKnown(name, requiredKeys, optionalKeys);
            throwIfKeyNotPresent(name);
            return get(name);
        }
    }    
    
    public class ObjectModelWithRefProps1 extends JsonSchema {
        /*
        NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
        Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
    
        Do not edit the class manually.
    
        a model that includes properties which should stay primitive (String + Boolean) and one which is defined as a class, NumberWithValidations
        */
        public static final LinkedHashMap<String, KeywordValidator> keywordToValidator = new LinkedHashMap<>(Map.ofEntries(
            new KeywordEntry("type", new TypeValidator(Set.of(FrozenMap.class))),
            new KeywordEntry("properties", new PropertiesValidator(Map.ofEntries(
                new PropertyEntry("myNumber", NumberWithValidations.NumberWithValidations1.class),
                new PropertyEntry("myString", StringSchema.StringSchema1.class),
                new PropertyEntry("myBoolean", BooleanSchema.BooleanSchema1.class)
            )))
        ));
        protected static ObjectModelWithRefPropsMap getMapOutputInstance(FrozenMap<String, Object> arg) {

            return new ObjectModelWithRefPropsMap(arg);
        }
        public static ObjectModelWithRefPropsMap validate(Map<String, Object> arg, SchemaConfiguration configuration) throws ValidationException {
            return JsonSchema.validate(ObjectModelWithRefProps1.class, arg, configuration);
        }
    }
}
