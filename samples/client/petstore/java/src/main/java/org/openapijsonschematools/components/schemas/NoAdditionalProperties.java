package org.openapijsonschematools.components.schemas;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.Set;
import org.openapijsonschematools.configurations.SchemaConfiguration;
import org.openapijsonschematools.exceptions.ValidationException;
import org.openapijsonschematools.schemas.AnyTypeJsonSchema;
import org.openapijsonschematools.schemas.Int64JsonSchema;
import org.openapijsonschematools.schemas.NotAnyTypeJsonSchema;
import org.openapijsonschematools.schemas.validation.AdditionalPropertiesValidator;
import org.openapijsonschematools.schemas.validation.FrozenMap;
import org.openapijsonschematools.schemas.validation.JsonSchema;
import org.openapijsonschematools.schemas.validation.KeywordEntry;
import org.openapijsonschematools.schemas.validation.KeywordValidator;
import org.openapijsonschematools.schemas.validation.PropertiesValidator;
import org.openapijsonschematools.schemas.validation.PropertyEntry;
import org.openapijsonschematools.schemas.validation.RequiredValidator;
import org.openapijsonschematools.schemas.validation.TypeValidator;

public class NoAdditionalProperties {
    // nest classes so all schemas and input/output classes can be public
    
    
    public static class AdditionalProperties extends NotAnyTypeJsonSchema {}
        // NotAnyTypeSchema
    
    
    public static class Id extends Int64JsonSchema {}
    
    
    public static class PetId extends Int64JsonSchema {}
    
    
    public static class NoAdditionalPropertiesMap extends FrozenMap<String, Long> {
        NoAdditionalPropertiesMap(FrozenMap<String, Long> m) {
            super(m);
        }
        public static final Set<String> requiredKeys = Set.of(
            "id"
        );
        public static final Set<String> optionalKeys = Set.of(
            "petId"
        );
        public static NoAdditionalPropertiesMap of(Map<String, Long> arg, SchemaConfiguration configuration) throws ValidationException {
            return NoAdditionalProperties1.validate(arg, configuration);
        }
        
        public long id() {
            return get("id");
        }
        
        public long petId() {
            String key = "petId";
            throwIfKeyNotPresent(key);
            return get(key);
        }
    }    
    
    public static class NoAdditionalProperties1 extends JsonSchema {
        /*
        NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
        Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
    
        Do not edit the class manually.
        */
        public static final LinkedHashMap<String, KeywordValidator> keywordToValidator = new LinkedHashMap<>(Map.ofEntries(
            new KeywordEntry("type", new TypeValidator(Set.of(FrozenMap.class))),
            new KeywordEntry("properties", new PropertiesValidator(Map.ofEntries(
                new PropertyEntry("id", Id.class),
                new PropertyEntry("petId", PetId.class)
            ))),
            new KeywordEntry("required", new RequiredValidator(Set.of(
                "id"
            ))),
            new KeywordEntry("additionalProperties", new AdditionalPropertiesValidator(AdditionalProperties.class))
        ));
        
        protected static NoAdditionalPropertiesMap getMapOutputInstance(FrozenMap<String, Long> arg) {
            return new NoAdditionalPropertiesMap(arg);
        }
        public static NoAdditionalPropertiesMap validate(Map<String, Long> arg, SchemaConfiguration configuration) throws ValidationException {
            return JsonSchema.validate(NoAdditionalProperties1.class, arg, configuration);
        }
    }
}
