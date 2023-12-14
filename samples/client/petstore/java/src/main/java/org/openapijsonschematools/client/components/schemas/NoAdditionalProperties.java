package org.openapijsonschematools.client.components.schemas;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.LinkedHashMap;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Map;
import java.util.Objects;
import java.util.Set;
import org.openapijsonschematools.client.configurations.JsonSchemaKeywordFlags;
import org.openapijsonschematools.client.configurations.SchemaConfiguration;
import org.openapijsonschematools.client.exceptions.InvalidTypeException;
import org.openapijsonschematools.client.exceptions.ValidationException;
import org.openapijsonschematools.client.schemas.AnyTypeJsonSchema;
import org.openapijsonschematools.client.schemas.Int64JsonSchema;
import org.openapijsonschematools.client.schemas.NotAnyTypeJsonSchema;
import org.openapijsonschematools.client.schemas.validation.AdditionalPropertiesValidator;
import org.openapijsonschematools.client.schemas.validation.FrozenMap;
import org.openapijsonschematools.client.schemas.validation.JsonSchema;
import org.openapijsonschematools.client.schemas.validation.KeywordEntry;
import org.openapijsonschematools.client.schemas.validation.PathToSchemasMap;
import org.openapijsonschematools.client.schemas.validation.PropertiesValidator;
import org.openapijsonschematools.client.schemas.validation.PropertyEntry;
import org.openapijsonschematools.client.schemas.validation.RequiredValidator;
import org.openapijsonschematools.client.schemas.validation.SchemaMapValidator;
import org.openapijsonschematools.client.schemas.validation.TypeValidator;
import org.openapijsonschematools.client.schemas.validation.ValidationMetadata;

public class NoAdditionalProperties {
    // nest classes so all schemas and input/output classes can be public
    
    
    public static class AdditionalProperties extends NotAnyTypeJsonSchema {}
        // NotAnyTypeSchema
    
    
    public static class Id extends Int64JsonSchema {}
    
    
    public static class PetId extends Int64JsonSchema {}
    
    
    public static class NoAdditionalPropertiesMap extends FrozenMap<Long> {
        NoAdditionalPropertiesMap(FrozenMap<Long> m) {
            super(m);
        }
        public static final Set<String> requiredKeys = Set.of(
            "id"
        );
        public static final Set<String> optionalKeys = Set.of(
            "petId"
        );
        public static NoAdditionalPropertiesMap of(Map<String, Long> arg, SchemaConfiguration configuration) throws ValidationException {
            return NoAdditionalProperties1.getInstance().validate(arg, configuration);
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
    public static class NoAdditionalPropertiesMapInput {
        // requiredProperties, optionalProperties, NO additionalProperties
    }
    
    
    public static class NoAdditionalProperties1 extends JsonSchema implements SchemaMapValidator<Long, Long, NoAdditionalPropertiesMap> {
        /*
        NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
        Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
    
        Do not edit the class manually.
        */
        private static NoAdditionalProperties1 instance;
        protected NoAdditionalProperties1() {
            super(new LinkedHashMap<>(Map.ofEntries(
                new KeywordEntry("type", new TypeValidator(Set.of(FrozenMap.class))),
                new KeywordEntry("properties", new PropertiesValidator(Map.ofEntries(
                    new PropertyEntry("id", Id.class),
                    new PropertyEntry("petId", PetId.class)
                ))),
                new KeywordEntry("required", new RequiredValidator(Set.of(
                    "id"
                ))),
                new KeywordEntry("additionalProperties", new AdditionalPropertiesValidator(AdditionalProperties.class))
            )));
        }
    
        public static NoAdditionalProperties1 getInstance() {
            if (instance == null) {
                instance = new NoAdditionalProperties1();
            }
            return instance;
        }
    
        @Override
        public FrozenMap<Long> castToAllowedTypes(Map<String, Long> arg, List<Object> pathToItem, Set<List<Object>> pathSet) {
            pathSet.add(pathToItem);
            LinkedHashMap<String, Long> argFixed = new LinkedHashMap<>();
            for (Map.Entry<String, Long> entry: arg.entrySet()) {
                String key = entry.getKey();
                                Long val = entry.getValue();
                List<Object> newPathToItem = new ArrayList<>(pathToItem);
                newPathToItem.add(key);
                                Long fixedVal = (Long) castToAllowedObjectTypes(val, newPathToItem, pathSet);
                argFixed.put(key, fixedVal);
            }
            return new FrozenMap<>(argFixed);
        }
    
        public NoAdditionalPropertiesMap getNewInstance(FrozenMap<Long> arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) {
            LinkedHashMap<String, Long> properties = new LinkedHashMap<>();
            for(Map.Entry<String, Long> entry: arg.entrySet()) {
                String propertyName = entry.getKey();
                List<Object> propertyPathToItem = new ArrayList<>(pathToItem);
                propertyPathToItem.add(propertyName);
                Long value = entry.getValue();
                JsonSchema propertySchema = pathToSchemas.get(propertyPathToItem).entrySet().iterator().next().getKey();
                Long castValue = (Long) propertySchema.getNewInstance(value, propertyPathToItem, pathToSchemas);
                properties.put(propertyName, castValue);
            }
            FrozenMap<Long> castProperties = new FrozenMap<>(properties);
            return new NoAdditionalPropertiesMap(castProperties);
        }
    
        @Override
        public Object getNewInstance(Object arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) {
            if (arg instanceof FrozenMap) {
                @SuppressWarnings("unchecked") FrozenMap<Long> castArg = (FrozenMap<Long>) arg;
                return getNewInstance(castArg, pathToItem, pathToSchemas);
            }
            throw new InvalidTypeException("Invalid input type="+arg.getClass()+". It can't be instantiated by this schema");
        }
    
        @Override
        public NoAdditionalPropertiesMap validate(Map<String, Long> arg, SchemaConfiguration configuration) throws ValidationException, InvalidTypeException {
            Set<List<Object>> pathSet = new HashSet<>();
            List<Object> pathToItem = List.of("args[0");
            FrozenMap<Long> castArg = castToAllowedTypes(arg, pathToItem, pathSet);
            SchemaConfiguration usedConfiguration = Objects.requireNonNullElseGet(configuration, () -> new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone()));
            ValidationMetadata validationMetadata = new ValidationMetadata(pathToItem, usedConfiguration, new PathToSchemasMap(), new LinkedHashSet<>());
            PathToSchemasMap pathToSchemasMap = getPathToSchemas(this, castArg, validationMetadata, pathSet);
            return getNewInstance(castArg, validationMetadata.pathToItem(), pathToSchemasMap);
        }
    }

}
