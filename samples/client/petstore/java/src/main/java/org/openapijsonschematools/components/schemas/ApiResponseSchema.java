package org.openapijsonschematools.components.schemas;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.Set;
import org.openapijsonschematools.configurations.SchemaConfiguration;
import org.openapijsonschematools.schemas.Int32JsonSchema;
import org.openapijsonschematools.schemas.StringJsonSchema;
import org.openapijsonschematools.schemas.validation.FrozenMap;
import org.openapijsonschematools.schemas.validation.JsonSchema;
import org.openapijsonschematools.schemas.validation.KeywordEntry;
import org.openapijsonschematools.schemas.validation.KeywordValidator;
import org.openapijsonschematools.schemas.validation.PropertiesValidator;
import org.openapijsonschematools.schemas.validation.PropertyEntry;
import org.openapijsonschematools.schemas.validation.TypeValidator;

public class ApiResponseSchema {
    // nest classes so all schemas and input/output classes can be public
    
    
    public class Code extends Int32JsonSchema {}
    
    
    public class Type extends StringJsonSchema {}
    
    
    public class Message extends StringJsonSchema {}
    
    
    public static class ApiResponseMap extends FrozenMap<String, Object> {

        ApiResponseMap(FrozenMap<String, Object> m) {

            super(m);
        }
        public static final Set<String> requiredKeys = Set.of(
        );
        public static final Set<String> optionalKeys = Set.of(
            "code",
            "type",
            "message"
        );
        public static ApiResponseMap of(Map<String, Object> arg, SchemaConfiguration configuration) {

            return ApiResponseSchema1.validate(arg, configuration);
        }
        
        public int code() {

            String key = "code";
            if (!containsKey(key)) {
                throw new RuntimeException("code is unset");
            }
            return (int) get(key);

        }
        
        public String type() {

            String key = "type";
            if (!containsKey(key)) {
                throw new RuntimeException("type is unset");
            }
            return (String) get(key);

        }
        
        public String message() {

            String key = "message";
            if (!containsKey(key)) {
                throw new RuntimeException("message is unset");
            }
            return (String) get(key);

        }
        
        public Object getAdditionalProperty(String name) {
            schemas.raise_if_key_known(name, self.__required_keys__, self.__optional_keys__)
            return self.get(name, schemas.unset)
        }
    }    
    
    public class ApiResponseSchema1 extends JsonSchema {
        /*
        NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
        Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
    
        Do not edit the class manually.
        */
        public static final LinkedHashMap<String, KeywordValidator> keywordToValidator = new LinkedHashMap<>(Map.ofEntries(
            new KeywordEntry("type", new TypeValidator(Set.of(FrozenMap.class))),
            new KeywordEntry("properties", new PropertiesValidator(Map.ofEntries(
                new PropertyEntry("code", Code.class),
                new PropertyEntry("type", Type.class),
                new PropertyEntry("message", Message.class)
            )))
        ));
        protected static ApiResponseMap getMapOutputInstance(FrozenMap<String, Object> arg) {

            return new ApiResponseMap(arg);
        }
        public static ApiResponseMap validate(Map<String, Object> arg, SchemaConfiguration configuration) {

            return JsonSchema.validate(ApiResponseSchema1.class, arg, configuration);
        }
    }
}
