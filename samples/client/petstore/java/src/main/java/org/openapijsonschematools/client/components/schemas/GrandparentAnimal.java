package org.openapijsonschematools.client.components.schemas;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.Set;
import org.openapijsonschematools.client.configurations.SchemaConfiguration;
import org.openapijsonschematools.client.exceptions.ValidationException;
import org.openapijsonschematools.client.schemas.StringJsonSchema;
import org.openapijsonschematools.client.schemas.validation.FrozenList;
import org.openapijsonschematools.client.schemas.validation.FrozenMap;
import org.openapijsonschematools.client.schemas.validation.JsonSchema;
import org.openapijsonschematools.client.schemas.validation.JsonSchemaFactory;
import org.openapijsonschematools.client.schemas.validation.KeywordEntry;
import org.openapijsonschematools.client.schemas.validation.KeywordValidator;
import org.openapijsonschematools.client.schemas.validation.PropertiesValidator;
import org.openapijsonschematools.client.schemas.validation.PropertyEntry;
import org.openapijsonschematools.client.schemas.validation.RequiredValidator;
import org.openapijsonschematools.client.schemas.validation.TypeValidator;

public class GrandparentAnimal {
    // nest classes so all schemas and input/output classes can be public
    
    
    public static class PetType extends StringJsonSchema {}
    
    
    public static class GrandparentAnimalMap extends FrozenMap<String, Object> {
        GrandparentAnimalMap(FrozenMap<String, Object> m) {
            super(m);
        }
        public static final Set<String> requiredKeys = Set.of(
            "pet_type"
        );
        public static final Set<String> optionalKeys = Set.of();
        public static GrandparentAnimalMap of(Map<String, Object> arg, SchemaConfiguration configuration) throws ValidationException {
            return JsonSchemaFactory.getInstance(GrandparentAnimal1.class).validate(arg, configuration);
        }
        
        public String pet_type() {
            return (String) get("pet_type");
        }
        
        public Object getAdditionalProperty(String name) {
            throwIfKeyKnown(name, requiredKeys, optionalKeys);
            throwIfKeyNotPresent(name);
            return get(name);
        }
    }
    public class GrandparentAnimalMapInput {
        // Map<String, Object> because addProps is unset
    }
    
    
    public static class GrandparentAnimal1 extends JsonSchema<GrandparentAnimalMap, FrozenList> {
        /*
        NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
        Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
    
        Do not edit the class manually.
        */
        public GrandparentAnimal1() {
            super(new LinkedHashMap<>(Map.ofEntries(
                new KeywordEntry("type", new TypeValidator(Set.of(FrozenMap.class))),
                new KeywordEntry("properties", new PropertiesValidator(Map.ofEntries(
                    new PropertyEntry("pet_type", PetType.class)
                ))),
                new KeywordEntry("required", new RequiredValidator(Set.of(
                    "pet_type"
                )))
            )));
        }
        
        @Override
        protected GrandparentAnimalMap getMapOutputInstance(FrozenMap<?, ?> arg) {
            return new GrandparentAnimalMap((FrozenMap<String, Object>) arg);
        }
        public GrandparentAnimalMap validate(Map<String, Object> arg, SchemaConfiguration configuration) throws ValidationException {
            return validateMap(arg, configuration);
        }
    }
}
