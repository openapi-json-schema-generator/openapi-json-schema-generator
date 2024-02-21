package org.openapijsonschematools.client.paths.fake.get;
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
import org.openapijsonschematools.client.paths.fake.get.parameters.parameter0.Schema0;
import org.openapijsonschematools.client.paths.fake.get.parameters.parameter1.Schema1;
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

public class HeaderParameters {
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
    
    
    public static class HeaderParametersMap extends FrozenMap<@Nullable Object> {
        protected HeaderParametersMap(FrozenMap<@Nullable Object> m) {
            super(m);
        }
        public static final Set<String> requiredKeys = Set.of();
        public static final Set<String> optionalKeys = Set.of(
            "enum_header_string",
            "enum_header_string_array"
        );
        public static HeaderParametersMap of(Map<String, ? extends @Nullable Object> arg, SchemaConfiguration configuration) throws ValidationException {
            return HeaderParameters1.getInstance().validate(arg, configuration);
        }
        
        public String enum_header_string() throws UnsetPropertyException {
            String key = "enum_header_string";
            throwIfKeyNotPresent(key);
            @Nullable Object value = get(key);
            if (!(value instanceof String)) {
                throw new InvalidTypeException("Invalid value stored for enum_header_string");
            }
            return (String) value;
        }
        
        public Schema0.SchemaList0 enum_header_string_array() throws UnsetPropertyException {
            String key = "enum_header_string_array";
            throwIfKeyNotPresent(key);
            @Nullable Object value = get(key);
            if (!(value instanceof Schema0.SchemaList0)) {
                throw new InvalidTypeException("Invalid value stored for enum_header_string_array");
            }
            return (Schema0.SchemaList0) value;
        }
    }
    
    public interface SetterForEnumHeaderString <T> {
        Map<String, @Nullable Object> getInstance();
        T getBuilderAfterEnumHeaderString(Map<String, @Nullable Object> instance);
        
        default T enum_header_string(String value) {
            var instance = getInstance();
            instance.put("enum_header_string", value);
            return getBuilderAfterEnumHeaderString(instance);
        }
        
        default T enum_header_string(Schema1.StringSchemaEnums1 value) {
            var instance = getInstance();
            instance.put("enum_header_string", value.value());
            return getBuilderAfterEnumHeaderString(instance);
        }
    }
    
    public interface SetterForEnumHeaderStringArray <T> {
        Map<String, @Nullable Object> getInstance();
        T getBuilderAfterEnumHeaderStringArray(Map<String, @Nullable Object> instance);
        
        default T enum_header_string_array(List<String> value) {
            var instance = getInstance();
            instance.put("enum_header_string_array", value);
            return getBuilderAfterEnumHeaderStringArray(instance);
        }
    }
    
    public static class HeaderParametersMapBuilder implements GenericBuilder<Map<String, @Nullable Object>>, SetterForEnumHeaderString<HeaderParametersMapBuilder>, SetterForEnumHeaderStringArray<HeaderParametersMapBuilder> {
        private final Map<String, @Nullable Object> instance;
        private static final Set<String> knownKeys = Set.of(
            "enum_header_string",
            "enum_header_string_array"
        );
        public Set<String> getKnownKeys() {
            return knownKeys;
        }
        public HeaderParametersMapBuilder() {
            this.instance = new LinkedHashMap<>();
        }
        public Map<String, @Nullable Object> build() {
            return instance;
        }
        public Map<String, @Nullable Object> getInstance() {
            return instance;
        }
        public HeaderParametersMapBuilder getBuilderAfterEnumHeaderString(Map<String, @Nullable Object> instance) {
            return this;
        }
        public HeaderParametersMapBuilder getBuilderAfterEnumHeaderStringArray(Map<String, @Nullable Object> instance) {
            return this;
        }
    }
    
    
    public sealed interface HeaderParameters1Boxed permits HeaderParameters1BoxedMap {
        @Nullable Object getData();
    }
    
    public record HeaderParameters1BoxedMap(HeaderParametersMap data) implements HeaderParameters1Boxed {
        @Override
        public @Nullable Object getData() {
            return data;
        }
    }
    
    
    public static class HeaderParameters1 extends JsonSchema<HeaderParameters1Boxed> implements MapSchemaValidator<HeaderParametersMap, HeaderParameters1BoxedMap> {
        private static @Nullable HeaderParameters1 instance = null;
    
        protected HeaderParameters1() {
            super(new JsonSchemaInfo()
                .type(Set.of(Map.class))
                .properties(Map.ofEntries(
                    new PropertyEntry("enum_header_string", Schema1.Schema11.class),
                    new PropertyEntry("enum_header_string_array", Schema0.Schema01.class)
                ))
                .additionalProperties(AdditionalProperties.class)
            );
        }
    
        public static HeaderParameters1 getInstance() {
            if (instance == null) {
                instance = new HeaderParameters1();
            }
            return instance;
        }
        
        public HeaderParametersMap getNewInstance(Map<?, ?> arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) {
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
                LinkedHashMap<JsonSchema<?>, Void> schemas = pathToSchemas.get(propertyPathToItem);
                if (schemas == null) {
                    throw new InvalidTypeException("Validation result is invalid, schemas must exist for a pathToItem");
                }
                JsonSchema<?> propertySchema = schemas.entrySet().iterator().next().getKey();
                @Nullable Object propertyInstance = propertySchema.getNewInstance(value, propertyPathToItem, pathToSchemas);
                properties.put(propertyName, propertyInstance);
            }
            FrozenMap<@Nullable Object> castProperties = new FrozenMap<>(properties);
            return new HeaderParametersMap(castProperties);
        }
        
        public HeaderParametersMap validate(Map<?, ?> arg, SchemaConfiguration configuration) throws ValidationException, InvalidTypeException {
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
        public HeaderParameters1BoxedMap validateAndBox(Map<?, ?> arg, SchemaConfiguration configuration) throws ValidationException, InvalidTypeException {
            return new HeaderParameters1BoxedMap(validate(arg, configuration));
        }
        @Override
        public HeaderParameters1Boxed validateAndBox(@Nullable Object arg, SchemaConfiguration configuration) throws ValidationException, InvalidTypeException {
            if (arg instanceof Map<?, ?> castArg) {
                return validateAndBox(castArg, configuration);
            }
            throw new InvalidTypeException("Invalid input type="+getClass(arg)+". It can't be validated by this schema");
        }
    }

}
