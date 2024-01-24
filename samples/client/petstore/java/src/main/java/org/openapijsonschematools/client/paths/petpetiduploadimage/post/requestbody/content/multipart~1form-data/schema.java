package org.openapijsonschematools.client.paths.petpetiduploadimage.post.requestbody.content.multipart~1form-data;
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
import org.openapijsonschematools.client.exceptions.InvalidAdditionalPropertyException;
import org.openapijsonschematools.client.exceptions.InvalidTypeException;
import org.openapijsonschematools.client.exceptions.UnsetPropertyException;
import org.openapijsonschematools.client.exceptions.ValidationException;
import org.openapijsonschematools.client.schemas.BaseBuilder;
import org.openapijsonschematools.client.schemas.StringJsonSchema;
import org.openapijsonschematools.client.schemas.UnsetAddPropsSetter;
import org.openapijsonschematools.client.schemas.validation.FrozenMap;
import org.openapijsonschematools.client.schemas.validation.JsonSchema;
import org.openapijsonschematools.client.schemas.validation.JsonSchemaInfo;
import org.openapijsonschematools.client.schemas.validation.MapSchemaValidator;
import org.openapijsonschematools.client.schemas.validation.PathToSchemasMap;
import org.openapijsonschematools.client.schemas.validation.PropertyEntry;
import org.openapijsonschematools.client.schemas.validation.ValidationMetadata;

public class Schema {
    // nest classes so all schemas and input/output classes can be public
    
    
    public static class AdditionalMetadata extends StringJsonSchema {
        private static @Nullable AdditionalMetadata instance = null;
        public static AdditionalMetadata getInstance() {
            if (instance == null) {
                instance = new AdditionalMetadata();
            }
            return instance;
        }
    }
    
    
    public static class File extends StringJsonSchema {
        // BinarySchema
        private static @Nullable File instance = null;
        public static File getInstance() {
            if (instance == null) {
                instance = new File();
            }
            return instance;
        }
    }
    
    
    public static class SchemaMap extends FrozenMap<@Nullable Object> {
        protected SchemaMap(FrozenMap<@Nullable Object> m) {
            super(m);
        }
        public static final Set<String> requiredKeys = Set.of();
        public static final Set<String> optionalKeys = Set.of(
            "additionalMetadata",
            "file"
        );
        public static SchemaMap of(Map<String, ? extends @Nullable Object> arg, SchemaConfiguration configuration) throws ValidationException {
            return Schema1.getInstance().validate(arg, configuration);
        }
        
        public String additionalMetadata() throws UnsetPropertyException {
            String key = "additionalMetadata";
            throwIfKeyNotPresent(key);
            @Nullable Object value = get(key);
            if (!(value instanceof String)) {
                throw new InvalidTypeException("Invalid value stored for additionalMetadata");
            }
            return (String) value;
        }
        
        public String file() throws UnsetPropertyException {
            String key = "file";
            throwIfKeyNotPresent(key);
            @Nullable Object value = get(key);
            if (!(value instanceof String)) {
                throw new InvalidTypeException("Invalid value stored for file");
            }
            return (String) value;
        }
        
        public @Nullable Object getAdditionalProperty(String name) throws UnsetPropertyException, InvalidAdditionalPropertyException {
            throwIfKeyKnown(name, requiredKeys, optionalKeys);
            throwIfKeyNotPresent(name);
            return get(name);
        }
    }
    
    public interface SetterForAdditionalMetadata <T> {
        Map<String, @Nullable Object> getInstance();
        T getBuilderAfterAdditionalMetadata(Map<String, @Nullable Object> instance);
        
        default T additionalMetadata(String value) {
            var instance = getInstance();
            instance.put("additionalMetadata", value);
            return getBuilderAfterAdditionalMetadata(instance);
        }
    }
    
    public interface SetterForFile <T> {
        Map<String, @Nullable Object> getInstance();
        T getBuilderAfterFile(Map<String, @Nullable Object> instance);
        
        default T file(String value) {
            var instance = getInstance();
            instance.put("file", value);
            return getBuilderAfterFile(instance);
        }
    }
    
    public static class SchemaMapBuilder extends UnsetAddPropsSetter<SchemaMapBuilder> implements BaseBuilder<@Nullable Object>, SetterForAdditionalMetadata<SchemaMapBuilder>, SetterForFile<SchemaMapBuilder> {
        private final Map<String, @Nullable Object> instance;
        private static final Set<String> knownKeys = Set.of(
            "additionalMetadata",
            "file"
        );
        public Set<String> getKnownKeys() {
            return knownKeys;
        }
        public SchemaMapBuilder() {
            this.instance = new LinkedHashMap<>();
        }
        public Map<String, @Nullable Object> build() {
            return instance;
        }
        public Map<String, @Nullable Object> getInstance() {
            return instance;
        }
        public SchemaMapBuilder getBuilderAfterAdditionalMetadata(Map<String, @Nullable Object> instance) {
            return this;
        }
        public SchemaMapBuilder getBuilderAfterFile(Map<String, @Nullable Object> instance) {
            return this;
        }
        public SchemaMapBuilder getBuilderAfterAdditionalProperty(Map<String, @Nullable Object> instance) {
            return this;
        }
    }
    
    
    public static class Schema1 extends JsonSchema implements MapSchemaValidator<SchemaMap> {
        private static @Nullable Schema1 instance = null;
    
        protected Schema1() {
            super(new JsonSchemaInfo()
                .type(Set.of(Map.class))
                .properties(Map.ofEntries(
                    new PropertyEntry("additionalMetadata", AdditionalMetadata.class),
                    new PropertyEntry("file", File.class)
                ))
            );
        }
    
        public static Schema1 getInstance() {
            if (instance == null) {
                instance = new Schema1();
            }
            return instance;
        }
        
        public SchemaMap getNewInstance(Map<?, ?> arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) {
            LinkedHashMap<String, @Nullable Object> properties = new LinkedHashMap<>();
            for(Map.Entry<?, ?> entry: arg.entrySet()) {
                @Nullable Object entryKey = entry.getKey();
                if (!(entryKey instanceof String)) {
                    throw new InvalidTypeException("Invalid non-string key value");
                }
                String propertyName = (String) entryKey;
                List<Object> propertyPathToItem = new ArrayList<>(pathToItem);
                propertyPathToItem.add(propertyName);
                Object value = entry.getValue();
                LinkedHashMap<JsonSchema, Void> schemas = pathToSchemas.get(propertyPathToItem);
                if (schemas == null) {
                    throw new InvalidTypeException("Validation result is invalid, schemas must exist for a pathToItem");
                }
                JsonSchema propertySchema = schemas.entrySet().iterator().next().getKey();
                @Nullable Object propertyInstance = propertySchema.getNewInstance(value, propertyPathToItem, pathToSchemas);
                properties.put(propertyName, propertyInstance);
            }
            FrozenMap<@Nullable Object> castProperties = new FrozenMap<>(properties);
            return new SchemaMap(castProperties);
        }
        
        public SchemaMap validate(Map<?, ?> arg, SchemaConfiguration configuration) throws ValidationException, InvalidTypeException {
            Set<List<Object>> pathSet = new HashSet<>();
            List<Object> pathToItem = List.of("args[0");
            Map<?, ?> castArg = castToAllowedTypes(arg, pathToItem, pathSet);
            SchemaConfiguration usedConfiguration = Objects.requireNonNullElseGet(configuration, () -> new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone()));
            ValidationMetadata validationMetadata = new ValidationMetadata(pathToItem, usedConfiguration, new PathToSchemasMap(), new LinkedHashSet<>());
            PathToSchemasMap pathToSchemasMap = getPathToSchemas(this, castArg, validationMetadata, pathSet);
            return getNewInstance(castArg, validationMetadata.pathToItem(), pathToSchemasMap);
        }
        
        
        @Override
        public @Nullable Object validate(@Nullable Object arg, SchemaConfiguration configuration) throws ValidationException, InvalidTypeException {
            if (arg instanceof Map) {
                return validate((Map<?, ?>) arg, configuration);
            }
            throw new InvalidTypeException("Invalid input type="+getClass(arg)+". It can't be validated by this schema");
        }        
        @Override
        public @Nullable Object getNewInstance(@Nullable Object arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) throws InvalidTypeException {
            if (arg instanceof Map) {
                return getNewInstance((Map<?, ?>) arg, pathToItem, pathToSchemas);
            }
            throw new InvalidTypeException("Invalid input type="+getClass(arg)+". It can't be instantiated by this schema");
        }
    }

}
