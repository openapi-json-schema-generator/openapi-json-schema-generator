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
import org.openapijsonschematools.client.exceptions.InvalidAdditionalPropertyException;
import org.openapijsonschematools.client.exceptions.InvalidTypeException;
import org.openapijsonschematools.client.exceptions.UnsetPropertyException;
import org.openapijsonschematools.client.exceptions.ValidationException;
import org.openapijsonschematools.client.schemas.GenericBuilder;
import org.openapijsonschematools.client.schemas.NumberJsonSchema;
import org.openapijsonschematools.client.schemas.UnsetAddPropsSetter;
import org.openapijsonschematools.client.schemas.validation.FrozenMap;
import org.openapijsonschematools.client.schemas.validation.JsonSchema;
import org.openapijsonschematools.client.schemas.validation.JsonSchemaInfo;
import org.openapijsonschematools.client.schemas.validation.MapSchemaValidator;
import org.openapijsonschematools.client.schemas.validation.PathToSchemasMap;
import org.openapijsonschematools.client.schemas.validation.PropertyEntry;
import org.openapijsonschematools.client.schemas.validation.ValidationMetadata;

public class NumberOnly {
    // nest classes so all schemas and input/output classes can be public
    
    
    public static class JustNumber extends NumberJsonSchema.NumberJsonSchema1 {
        private static @Nullable JustNumber instance = null;
        public static JustNumber getInstance() {
            if (instance == null) {
                instance = new JustNumber();
            }
            return instance;
        }
    }
    
    
    public static class NumberOnlyMap extends FrozenMap<@Nullable Object> {
        protected NumberOnlyMap(FrozenMap<@Nullable Object> m) {
            super(m);
        }
        public static final Set<String> requiredKeys = Set.of();
        public static final Set<String> optionalKeys = Set.of(
            "JustNumber"
        );
        public static NumberOnlyMap of(Map<String, ? extends @Nullable Object> arg, SchemaConfiguration configuration) throws ValidationException {
            return NumberOnly1.getInstance().validate(arg, configuration);
        }
        
        public Number JustNumber() throws UnsetPropertyException {
            String key = "JustNumber";
            throwIfKeyNotPresent(key);
            @Nullable Object value = get(key);
            if (!(value instanceof Number)) {
                throw new InvalidTypeException("Invalid value stored for JustNumber");
            }
            return (Number) value;
        }
        
        public @Nullable Object getAdditionalProperty(String name) throws UnsetPropertyException, InvalidAdditionalPropertyException {
            throwIfKeyKnown(name, requiredKeys, optionalKeys);
            throwIfKeyNotPresent(name);
            return get(name);
        }
    }
    
    public interface SetterForJustNumber <T> {
        Map<String, @Nullable Object> getInstance();
        T getBuilderAfterJustNumber(Map<String, @Nullable Object> instance);
        
        default T JustNumber(int value) {
            var instance = getInstance();
            instance.put("JustNumber", value);
            return getBuilderAfterJustNumber(instance);
        }
        
        default T JustNumber(float value) {
            var instance = getInstance();
            instance.put("JustNumber", value);
            return getBuilderAfterJustNumber(instance);
        }
        
        default T JustNumber(long value) {
            var instance = getInstance();
            instance.put("JustNumber", value);
            return getBuilderAfterJustNumber(instance);
        }
        
        default T JustNumber(double value) {
            var instance = getInstance();
            instance.put("JustNumber", value);
            return getBuilderAfterJustNumber(instance);
        }
    }
    
    public static class NumberOnlyMapBuilder extends UnsetAddPropsSetter<NumberOnlyMapBuilder> implements GenericBuilder<Map<String, @Nullable Object>>, SetterForJustNumber<NumberOnlyMapBuilder> {
        private final Map<String, @Nullable Object> instance;
        private static final Set<String> knownKeys = Set.of(
            "JustNumber"
        );
        public Set<String> getKnownKeys() {
            return knownKeys;
        }
        public NumberOnlyMapBuilder() {
            this.instance = new LinkedHashMap<>();
        }
        public Map<String, @Nullable Object> build() {
            return instance;
        }
        public Map<String, @Nullable Object> getInstance() {
            return instance;
        }
        public NumberOnlyMapBuilder getBuilderAfterJustNumber(Map<String, @Nullable Object> instance) {
            return this;
        }
        public NumberOnlyMapBuilder getBuilderAfterAdditionalProperty(Map<String, @Nullable Object> instance) {
            return this;
        }
    }
    
    
    public static abstract sealed class NumberOnly1Boxed permits NumberOnly1BoxedMap {
        public abstract @Nullable Object data();
    }
    
    public static final class NumberOnly1BoxedMap extends NumberOnly1Boxed {
        public final NumberOnlyMap data;
        private NumberOnly1BoxedMap(NumberOnlyMap data) {
            this.data = data;
        }
        @Override
        public @Nullable Object data() {
            return data;
        }
    }
    
    
    public static class NumberOnly1 extends JsonSchema implements MapSchemaValidator<NumberOnlyMap, NumberOnly1BoxedMap> {
        /*
        NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
        Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
    
        Do not edit the class manually.
        */
        private static @Nullable NumberOnly1 instance = null;
    
        protected NumberOnly1() {
            super(new JsonSchemaInfo()
                .type(Set.of(Map.class))
                .properties(Map.ofEntries(
                    new PropertyEntry("JustNumber", JustNumber.class)
                ))
            );
        }
    
        public static NumberOnly1 getInstance() {
            if (instance == null) {
                instance = new NumberOnly1();
            }
            return instance;
        }
        
        public NumberOnlyMap getNewInstance(Map<?, ?> arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) {
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
            return new NumberOnlyMap(castProperties);
        }
        
        public NumberOnlyMap validate(Map<?, ?> arg, SchemaConfiguration configuration) throws ValidationException, InvalidTypeException {
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
        public NumberOnly1BoxedMap validateAndBox(Map<?, ?> arg, SchemaConfiguration configuration) throws ValidationException, InvalidTypeException {
            return new NumberOnly1BoxedMap(validate(arg, configuration));
        }
    }

}
