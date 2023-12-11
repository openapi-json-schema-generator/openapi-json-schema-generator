package org.openapijsonschematools.client.components.schemas;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.Set;
import org.openapijsonschematools.client.configurations.SchemaConfiguration;
import org.openapijsonschematools.client.exceptions.ValidationException;
import org.openapijsonschematools.client.schemas.validation.AdditionalPropertiesValidator;
import org.openapijsonschematools.client.schemas.validation.FrozenList;
import org.openapijsonschematools.client.schemas.validation.FrozenMap;
import org.openapijsonschematools.client.schemas.validation.JsonSchema;
import org.openapijsonschematools.client.schemas.validation.JsonSchemaFactory;
import org.openapijsonschematools.client.schemas.validation.KeywordEntry;
import org.openapijsonschematools.client.schemas.validation.KeywordValidator;
import org.openapijsonschematools.client.schemas.validation.TypeValidator;

public class RefInAdditionalproperties {
    // nest classes so all schemas and input/output classes can be public
    
    
    public static class RefInAdditionalpropertiesMap extends FrozenMap<String, Object> {
        RefInAdditionalpropertiesMap(FrozenMap<String, Object> m) {
            super(m);
        }
        public static final Set<String> requiredKeys = Set.of();
        public static final Set<String> optionalKeys = Set.of();
        public static RefInAdditionalpropertiesMap of(Map<String, Object> arg, SchemaConfiguration configuration) throws ValidationException {
            return JsonSchemaFactory.getInstance(RefInAdditionalproperties1.class).validate(arg, configuration);
        }
        
        public Object getAdditionalProperty(String name) {
            throwIfKeyNotPresent(name);
            return get(name);
        }
    }
    public class RefInAdditionalpropertiesMapInput {
        // Map<String, additionalProperties>
    }
    
    
    public static class RefInAdditionalproperties1 extends JsonSchema<Object, Object, RefInAdditionalpropertiesMap, Object, Object, FrozenList<Object>> {
        /*
        NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
        Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
    
        Do not edit the class manually.
        */
        public RefInAdditionalproperties1() {
            super(new LinkedHashMap<>(Map.ofEntries(
                new KeywordEntry("type", new TypeValidator(Set.of(FrozenMap.class))),
                new KeywordEntry("additionalProperties", new AdditionalPropertiesValidator(PropertyNamedRefThatIsNotAReference.PropertyNamedRefThatIsNotAReference1.class))
            )));
        }
        
        @Override
        protected RefInAdditionalpropertiesMap getMapOutputInstance(FrozenMap<String, ?> arg) {
            return new RefInAdditionalpropertiesMap((FrozenMap<String, Object>) arg);
        }
        public RefInAdditionalpropertiesMap validate(Map<String, Object> arg, SchemaConfiguration configuration) throws ValidationException {
            return validateMap(arg, configuration);
        }
    }
}
