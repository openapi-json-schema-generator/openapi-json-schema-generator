package org.openapijsonschematools.paths.fakejsonformdata.get.requestbody.content.applicationxwwwformurlencoded;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.Set;
import org.openapijsonschematools.configurations.SchemaConfiguration;
import org.openapijsonschematools.exceptions.ValidationException;
import org.openapijsonschematools.schemas.StringJsonSchema;
import org.openapijsonschematools.schemas.validation.FrozenMap;
import org.openapijsonschematools.schemas.validation.JsonSchema;
import org.openapijsonschematools.schemas.validation.KeywordEntry;
import org.openapijsonschematools.schemas.validation.KeywordValidator;
import org.openapijsonschematools.schemas.validation.PropertiesValidator;
import org.openapijsonschematools.schemas.validation.PropertyEntry;
import org.openapijsonschematools.schemas.validation.RequiredValidator;
import org.openapijsonschematools.schemas.validation.TypeValidator;

public class Schema {
    // nest classes so all schemas and input/output classes can be public
    
    
    public class Param extends StringJsonSchema {}
    
    
    public class Param2 extends StringJsonSchema {}
    
    
    public static class SchemaMap extends FrozenMap<String, Object> {

        SchemaMap(FrozenMap<String, Object> m) {

            super(m);
        }
        public static final Set<String> requiredKeys = Set.of(
            "param",
            "param2"
        );
        public static final Set<String> optionalKeys = Set.of();
        public static SchemaMap of(Map<String, Object> arg, SchemaConfiguration configuration) throws ValidationException {

            return Schema1.validate(arg, configuration);
        }
        
        public String param() {

            return (String) get("param");

        }
        
        public String param2() {

            return (String) get("param2");

        }
        
        public Object getAdditionalProperty(String name) {
            throwIfKeyKnown(name, requiredKeys, optionalKeys);
            throwIfKeyNotPresent(name);
            return get(name);
        }
    }    
    
    public class Schema1 extends JsonSchema {
        public static final LinkedHashMap<String, KeywordValidator> keywordToValidator = new LinkedHashMap<>(Map.ofEntries(
            new KeywordEntry("type", new TypeValidator(Set.of(FrozenMap.class))),
            new KeywordEntry("properties", new PropertiesValidator(Map.ofEntries(
                new PropertyEntry("param", Param.class),
                new PropertyEntry("param2", Param2.class)
            ))),
            new KeywordEntry("required", new RequiredValidator(Set.of(
                "param",
                "param2"
            )))
        ));
        protected static SchemaMap getMapOutputInstance(FrozenMap<String, Object> arg) {

            return new SchemaMap(arg);
        }
        public static SchemaMap validate(Map<String, Object> arg, SchemaConfiguration configuration) throws ValidationException {

            return JsonSchema.validate(Schema1.class, arg, configuration);
        }
    }
}
