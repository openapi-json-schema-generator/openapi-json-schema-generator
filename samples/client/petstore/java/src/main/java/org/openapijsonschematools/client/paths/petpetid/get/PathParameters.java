package org.openapijsonschematools.client.paths.petpetid.get;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.LinkedHashMap;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Map;
import java.util.Objects;
import java.util.Set;
import org.checkerframework.checker.nullness.qual.Nullable;
import org.openapijsonschematools.client.configurations.JsonSchemaKeywordFlags;
import org.openapijsonschematools.client.configurations.SchemaConfiguration;
import org.openapijsonschematools.client.exceptions.UnsetPropertyException;
import org.openapijsonschematools.client.exceptions.ValidationException;
import org.openapijsonschematools.client.paths.petpetid.get.parameters.parameter0.Schema0;
import org.openapijsonschematools.client.schemas.AnyTypeJsonSchema;
import org.openapijsonschematools.client.schemas.GenericBuilder;
import org.openapijsonschematools.client.schemas.NotAnyTypeJsonSchema;
import org.openapijsonschematools.client.schemas.validation.FrozenMap;
import org.openapijsonschematools.client.schemas.validation.JsonSchema;
import org.openapijsonschematools.client.schemas.validation.JsonSchemaInfo;
import org.openapijsonschematools.client.schemas.validation.MapSchemaValidator;
import org.openapijsonschematools.client.schemas.validation.MapUtils;
import org.openapijsonschematools.client.schemas.validation.PathToSchemasMap;
import org.openapijsonschematools.client.schemas.validation.PropertyEntry;
import org.openapijsonschematools.client.schemas.validation.ValidationMetadata;

public class PathParameters {
    // nest classes so all schemas and input/output classes can be public
    
    
    public static class AdditionalProperties extends NotAnyTypeJsonSchema.NotAnyTypeJsonSchema1 {
        // NotAnyTypeSchema
        private static @Nullable AdditionalProperties instance = null;
        public static AdditionalProperties getInstance() {
            if (instance == null) {
                instance = new AdditionalProperties();
            }
            return instance;
        }
    }
    
    
    public static class PathParametersMap extends FrozenMap<Number> {
        protected PathParametersMap(FrozenMap<Number> m) {
            super(m);
        }
        public static final Set<String> requiredKeys = Set.of(
            "petId"
        );
        public static final Set<String> optionalKeys = Set.of();
        public static PathParametersMap of(Map<String, Number> arg, SchemaConfiguration configuration) throws ValidationException {
            return PathParameters1.getInstance().validate(arg, configuration);
        }
        
        public Number petId() {
            try {
                return getOrThrow("version");
            } catch (UnsetPropertyException e) {
                throw new RuntimeException(e);
            }
        }
    }
    
    public interface SetterForPetId <T> {
        Map<String, Number> getInstance();
        T getBuilderAfterPetId(Map<String, Number> instance);
        
        default T petId(int value) {
            var instance = getInstance();
            instance.put("petId", value);
            return getBuilderAfterPetId(instance);
        }
        
        default T petId(float value) {
            var instance = getInstance();
            instance.put("petId", value);
            return getBuilderAfterPetId(instance);
        }
        
        default T petId(long value) {
            var instance = getInstance();
            instance.put("petId", value);
            return getBuilderAfterPetId(instance);
        }
        
        default T petId(double value) {
            var instance = getInstance();
            instance.put("petId", value);
            return getBuilderAfterPetId(instance);
        }
    }
    
    public static class PathParametersMap0Builder implements GenericBuilder<Map<String, Number>> {
        private final Map<String, Number> instance;
        private static final Set<String> knownKeys = Set.of(
            "petId"
        );
        public Set<String> getKnownKeys() {
            return knownKeys;
        }
        public PathParametersMap0Builder(Map<String, Number> instance) {
            this.instance = instance;
        }
        public Map<String, Number> build() {
            return instance;
        }
    }
    
    public static class PathParametersMapBuilder implements SetterForPetId<PathParametersMap0Builder> {
        private final Map<String, Number> instance;
        public PathParametersMapBuilder() {
            this.instance = new LinkedHashMap<>();
        }
        public Map<String, Number> getInstance() {
            return instance;
        }
        public PathParametersMap0Builder getBuilderAfterPetId(Map<String, Number> instance) {
            return new PathParametersMap0Builder(instance);
        }
    }
    
    
    public sealed interface PathParameters1Boxed permits PathParameters1BoxedMap {
        @Nullable Object getData();
    }
    
    public record PathParameters1BoxedMap(PathParametersMap data) implements PathParameters1Boxed {
        @Override
        public @Nullable Object getData() {
            return data;
        }
    }
    
    
    public static class PathParameters1 extends JsonSchema<PathParameters1Boxed> implements MapSchemaValidator<PathParametersMap, PathParameters1BoxedMap> {
        private static @Nullable PathParameters1 instance = null;
    
        protected PathParameters1() {
            super(new JsonSchemaInfo()
                .type(Set.of(Map.class))
                .properties(Map.ofEntries(
                    new PropertyEntry("petId", Schema0.Schema01.class)
                ))
                .required(Set.of(
                    "petId"
                ))
                .additionalProperties(AdditionalProperties.class)
            );
        }
    
        public static PathParameters1 getInstance() {
            if (instance == null) {
                instance = new PathParameters1();
            }
            return instance;
        }
        
        public PathParametersMap getNewInstance(Map<?, ?> arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) {
            LinkedHashMap<String, Number> properties = new LinkedHashMap<>();
            for(Map.Entry<?, ?> entry: arg.entrySet()) {
                @Nullable Object entryKey = entry.getKey();
                if (!(entryKey instanceof String)) {
                    throw new RuntimeException("Invalid non-string key value");
                }
                String propertyName = (String) entryKey;
                List<Object> propertyPathToItem = new ArrayList<>(pathToItem);
                propertyPathToItem.add(propertyName);
                Object value = entry.getValue();
                LinkedHashMap<JsonSchema<?>, Void> schemas = pathToSchemas.get(propertyPathToItem);
                if (schemas == null) {
                    throw new RuntimeException("Validation result is invalid, schemas must exist for a pathToItem");
                }
                JsonSchema<?> propertySchema = schemas.entrySet().iterator().next().getKey();
                @Nullable Object propertyInstance = propertySchema.getNewInstance(value, propertyPathToItem, pathToSchemas);
                if (!(propertyInstance instanceof Number)) {
                    throw new RuntimeException("Invalid instantiated value");
                }
                properties.put(propertyName, (Number) propertyInstance);
            }
            FrozenMap<Number> castProperties = new FrozenMap<>(properties);
            return new PathParametersMap(castProperties);
        }
        
        public PathParametersMap validate(Map<?, ?> arg, SchemaConfiguration configuration) throws ValidationException {
            Set<List<Object>> pathSet = new HashSet<>();
            List<Object> pathToItem = List.of("args[0");
            Map<?, ?> castArg = castToAllowedTypes(arg, pathToItem, pathSet);
            SchemaConfiguration usedConfiguration = Objects.requireNonNullElseGet(configuration, () -> new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone()));
            ValidationMetadata validationMetadata = new ValidationMetadata(pathToItem, usedConfiguration, new PathToSchemasMap(), new LinkedHashSet<>());
            PathToSchemasMap pathToSchemasMap = getPathToSchemas(this, castArg, validationMetadata, pathSet);
            return getNewInstance(castArg, validationMetadata.pathToItem(), pathToSchemasMap);
        }
        
        
        @Override
        public @Nullable Object validate(@Nullable Object arg, SchemaConfiguration configuration) throws ValidationException {
            if (arg instanceof Map) {
                return validate((Map<?, ?>) arg, configuration);
            }
            throw new ValidationException("Invalid input type="+getClass(arg)+". It can't be validated by this schema");
        }        
        @Override
        public @Nullable Object getNewInstance(@Nullable Object arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) {
            if (arg instanceof Map) {
                return getNewInstance((Map<?, ?>) arg, pathToItem, pathToSchemas);
            }
            throw new RuntimeException("Invalid input type="+getClass(arg)+". It can't be instantiated by this schema");
        }
        @Override
        public PathParameters1BoxedMap validateAndBox(Map<?, ?> arg, SchemaConfiguration configuration) throws ValidationException {
            return new PathParameters1BoxedMap(validate(arg, configuration));
        }
        @Override
        public PathParameters1Boxed validateAndBox(@Nullable Object arg, SchemaConfiguration configuration) throws ValidationException {
            if (arg instanceof Map<?, ?> castArg) {
                return validateAndBox(castArg, configuration);
            }
            throw new ValidationException("Invalid input type="+getClass(arg)+". It can't be validated by this schema");
        }
    }

}
