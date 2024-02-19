package org.openapijsonschematools.client.components.schemas;
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
import org.openapijsonschematools.client.exceptions.InvalidTypeException;
import org.openapijsonschematools.client.exceptions.UnsetPropertyException;
import org.openapijsonschematools.client.exceptions.ValidationException;
import org.openapijsonschematools.client.schemas.AnyTypeJsonSchema;
import org.openapijsonschematools.client.schemas.GenericBuilder;
import org.openapijsonschematools.client.schemas.NotAnyTypeJsonSchema;
import org.openapijsonschematools.client.schemas.UuidJsonSchema;
import org.openapijsonschematools.client.schemas.validation.FrozenMap;
import org.openapijsonschematools.client.schemas.validation.JsonSchema;
import org.openapijsonschematools.client.schemas.validation.JsonSchemaInfo;
import org.openapijsonschematools.client.schemas.validation.MapSchemaValidator;
import org.openapijsonschematools.client.schemas.validation.MapUtils;
import org.openapijsonschematools.client.schemas.validation.PathToSchemasMap;
import org.openapijsonschematools.client.schemas.validation.PropertyEntry;
import org.openapijsonschematools.client.schemas.validation.ValidationMetadata;

public class MyObjectDto {
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
    
    
    public static class Id extends UuidJsonSchema.UuidJsonSchema1 {
        private static @Nullable Id instance = null;
        public static Id getInstance() {
            if (instance == null) {
                instance = new Id();
            }
            return instance;
        }
    }
    
    
    public static class MyObjectDtoMap extends FrozenMap<String> {
        protected MyObjectDtoMap(FrozenMap<String> m) {
            super(m);
        }
        public static final Set<String> requiredKeys = Set.of();
        public static final Set<String> optionalKeys = Set.of(
            "id"
        );
        public static MyObjectDtoMap of(Map<String, String> arg, SchemaConfiguration configuration) throws ValidationException {
            return MyObjectDto1.getInstance().validate(arg, configuration);
        }
        
        public String id() throws UnsetPropertyException {
            return getOrThrow("id");
        }
    }
    
    public interface SetterForId <T> {
        Map<String, String> getInstance();
        T getBuilderAfterId(Map<String, String> instance);
        
        default T id(String value) {
            var instance = getInstance();
            instance.put("id", value);
            return getBuilderAfterId(instance);
        }
    }
    
    public static class MyObjectDtoMapBuilder implements GenericBuilder<Map<String, String>>, SetterForId<MyObjectDtoMapBuilder> {
        private final Map<String, String> instance;
        private static final Set<String> knownKeys = Set.of(
            "id"
        );
        public Set<String> getKnownKeys() {
            return knownKeys;
        }
        public MyObjectDtoMapBuilder() {
            this.instance = new LinkedHashMap<>();
        }
        public Map<String, String> build() {
            return instance;
        }
        public Map<String, String> getInstance() {
            return instance;
        }
        public MyObjectDtoMapBuilder getBuilderAfterId(Map<String, String> instance) {
            return this;
        }
    }
    
    
    public sealed interface MyObjectDto1Boxed permits MyObjectDto1BoxedMap {
        @Nullable Object data();
    }
    
    public static final class MyObjectDto1BoxedMap implements MyObjectDto1Boxed {
        public final MyObjectDtoMap data;
        private MyObjectDto1BoxedMap(MyObjectDtoMap data) {
            this.data = data;
        }
        @Override
        public @Nullable Object data() {
            return data;
        }
    }
    
    
    public static class MyObjectDto1 extends JsonSchema implements MapSchemaValidator<MyObjectDtoMap, MyObjectDto1BoxedMap> {
        /*
        NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
        Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
    
        Do not edit the class manually.
        */
        private static @Nullable MyObjectDto1 instance = null;
    
        protected MyObjectDto1() {
            super(new JsonSchemaInfo()
                .type(Set.of(Map.class))
                .properties(Map.ofEntries(
                    new PropertyEntry("id", Id.class)
                ))
                .additionalProperties(AdditionalProperties.class)
            );
        }
    
        public static MyObjectDto1 getInstance() {
            if (instance == null) {
                instance = new MyObjectDto1();
            }
            return instance;
        }
        
        public MyObjectDtoMap getNewInstance(Map<?, ?> arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) {
            LinkedHashMap<String, String> properties = new LinkedHashMap<>();
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
                if (!(propertyInstance instanceof String)) {
                    throw new InvalidTypeException("Invalid instantiated value");
                }
                properties.put(propertyName, (String) propertyInstance);
            }
            FrozenMap<String> castProperties = new FrozenMap<>(properties);
            return new MyObjectDtoMap(castProperties);
        }
        
        public MyObjectDtoMap validate(Map<?, ?> arg, SchemaConfiguration configuration) throws ValidationException, InvalidTypeException {
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
        @Override
        public MyObjectDto1BoxedMap validateAndBox(Map<?, ?> arg, SchemaConfiguration configuration) throws ValidationException, InvalidTypeException {
            return new MyObjectDto1BoxedMap(validate(arg, configuration));
        }
    }

}
