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
import org.openapijsonschematools.client.schemas.BooleanJsonSchema;
import org.openapijsonschematools.client.schemas.validation.AdditionalPropertiesValidator;
import org.openapijsonschematools.client.schemas.validation.FrozenMap;
import org.openapijsonschematools.client.schemas.validation.JsonSchema;
import org.openapijsonschematools.client.schemas.validation.JsonSchemaInfo;
import org.openapijsonschematools.client.schemas.validation.MapSchemaValidator;
import org.openapijsonschematools.client.schemas.validation.PathToSchemasMap;
import org.openapijsonschematools.client.schemas.validation.ValidationMetadata;

public class AdditionalpropertiesCanExistByItself {
    // nest classes so all schemas and input/output classes can be public
    
    
    public static class AdditionalProperties extends BooleanJsonSchema {}
    
    
    public static class AdditionalpropertiesCanExistByItselfMap extends FrozenMap<Boolean> {
        AdditionalpropertiesCanExistByItselfMap(FrozenMap<Boolean> m) {
            super(m);
        }
        public static final Set<String> requiredKeys = Set.of();
        public static final Set<String> optionalKeys = Set.of();
        public static AdditionalpropertiesCanExistByItselfMap of(Map<String, Boolean> arg, SchemaConfiguration configuration) throws ValidationException {
            return AdditionalpropertiesCanExistByItself1.getInstance().validate(arg, configuration);
        }
        
        public boolean getAdditionalProperty(String name) {
            throwIfKeyNotPresent(name);
            return get(name);
        }
    }
    public static class AdditionalpropertiesCanExistByItselfMapInput {
        // Map<String, additionalProperties>
    }
    
    
    public static class AdditionalpropertiesCanExistByItself1 extends JsonSchema implements MapSchemaValidator<Boolean, AdditionalpropertiesCanExistByItselfMap> {
        /*
        NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
        Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
    
        Do not edit the class manually.
        */
        private static AdditionalpropertiesCanExistByItself1 instance;
    
        protected AdditionalpropertiesCanExistByItself1() {
            super(new JsonSchemaInfo()
                .type(Set.of(FrozenMap.class))
                .additionalProperties(AdditionalProperties.class)
            );
        }
    
        public static AdditionalpropertiesCanExistByItself1 getInstance() {
            if (instance == null) {
                instance = new AdditionalpropertiesCanExistByItself1();
            }
            return instance;
        }
        
        public AdditionalpropertiesCanExistByItselfMap getNewInstance(FrozenMap<?> arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) {
            LinkedHashMap<String, Boolean> properties = new LinkedHashMap<>();
            for(Map.Entry<String, ?> entry: arg.entrySet()) {
                String propertyName = entry.getKey();
                List<Object> propertyPathToItem = new ArrayList<>(pathToItem);
                propertyPathToItem.add(propertyName);
                Object value = entry.getValue();
                JsonSchema propertySchema = pathToSchemas.get(propertyPathToItem).entrySet().iterator().next().getKey();
                Boolean castValue = (Boolean) propertySchema.getNewInstance(value, propertyPathToItem, pathToSchemas);
                properties.put(propertyName, castValue);
            }
            FrozenMap<Boolean> castProperties = new FrozenMap<>(properties);
            return new AdditionalpropertiesCanExistByItselfMap(castProperties);
        }
        
        @Override
        public AdditionalpropertiesCanExistByItselfMap validate(Map<String, Boolean> arg, SchemaConfiguration configuration) throws ValidationException, InvalidTypeException {
            Set<List<Object>> pathSet = new HashSet<>();
            List<Object> pathToItem = List.of("args[0");
            FrozenMap<?> castArg = castToAllowedTypes(arg, pathToItem, pathSet);
            SchemaConfiguration usedConfiguration = Objects.requireNonNullElseGet(configuration, () -> new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone()));
            ValidationMetadata validationMetadata = new ValidationMetadata(pathToItem, usedConfiguration, new PathToSchemasMap(), new LinkedHashSet<>());
            PathToSchemasMap pathToSchemasMap = getPathToSchemas(this, castArg, validationMetadata, pathSet);
            return getNewInstance(castArg, validationMetadata.pathToItem(), pathToSchemasMap);
        }
        
        
        @Override
        public Object getNewInstance(Object arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) {
            if (arg instanceof FrozenMap) {
                @SuppressWarnings("unchecked") FrozenMap<Boolean> castArg = (FrozenMap<Boolean>) arg;
                return getNewInstance(castArg, pathToItem, pathToSchemas);
            }
            throw new InvalidTypeException("Invalid input type="+arg.getClass()+". It can't be instantiated by this schema");
        }
    }

}
