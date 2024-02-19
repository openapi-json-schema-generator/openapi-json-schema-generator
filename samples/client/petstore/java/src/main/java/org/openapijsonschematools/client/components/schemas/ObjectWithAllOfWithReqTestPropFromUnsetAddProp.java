package org.openapijsonschematools.client.components.schemas;
import java.time.LocalDate;
import java.time.ZonedDateTime;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.LinkedHashMap;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Map;
import java.util.Objects;
import java.util.Set;
import java.util.UUID;
import org.checkerframework.checker.nullness.qual.Nullable;
import org.openapijsonschematools.client.configurations.JsonSchemaKeywordFlags;
import org.openapijsonschematools.client.configurations.SchemaConfiguration;
import org.openapijsonschematools.client.exceptions.InvalidAdditionalPropertyException;
import org.openapijsonschematools.client.exceptions.InvalidTypeException;
import org.openapijsonschematools.client.exceptions.UnsetPropertyException;
import org.openapijsonschematools.client.exceptions.ValidationException;
import org.openapijsonschematools.client.schemas.GenericBuilder;
import org.openapijsonschematools.client.schemas.StringJsonSchema;
import org.openapijsonschematools.client.schemas.UnsetAddPropsSetter;
import org.openapijsonschematools.client.schemas.validation.BooleanSchemaValidator;
import org.openapijsonschematools.client.schemas.validation.FrozenList;
import org.openapijsonschematools.client.schemas.validation.FrozenMap;
import org.openapijsonschematools.client.schemas.validation.JsonSchema;
import org.openapijsonschematools.client.schemas.validation.JsonSchemaInfo;
import org.openapijsonschematools.client.schemas.validation.ListSchemaValidator;
import org.openapijsonschematools.client.schemas.validation.MapSchemaValidator;
import org.openapijsonschematools.client.schemas.validation.NullSchemaValidator;
import org.openapijsonschematools.client.schemas.validation.NumberSchemaValidator;
import org.openapijsonschematools.client.schemas.validation.PathToSchemasMap;
import org.openapijsonschematools.client.schemas.validation.PropertyEntry;
import org.openapijsonschematools.client.schemas.validation.StringSchemaValidator;
import org.openapijsonschematools.client.schemas.validation.ValidationMetadata;

public class ObjectWithAllOfWithReqTestPropFromUnsetAddProp {
    // nest classes so all schemas and input/output classes can be public
    
    
    public static class Name extends StringJsonSchema.StringJsonSchema1 {
        private static @Nullable Name instance = null;
        public static Name getInstance() {
            if (instance == null) {
                instance = new Name();
            }
            return instance;
        }
    }
    
    
    public static class Schema1Map extends FrozenMap<@Nullable Object> {
        protected Schema1Map(FrozenMap<@Nullable Object> m) {
            super(m);
        }
        public static final Set<String> requiredKeys = Set.of(
            "test"
        );
        public static final Set<String> optionalKeys = Set.of(
            "name"
        );
        public static Schema1Map of(Map<String, ? extends @Nullable Object> arg, SchemaConfiguration configuration) throws ValidationException {
            return Schema1.getInstance().validate(arg, configuration);
        }
        
        public @Nullable Object test() {
            return getOrThrow("test");
        }
        
        public String name() throws UnsetPropertyException {
            String key = "name";
            throwIfKeyNotPresent(key);
            @Nullable Object value = get(key);
            if (!(value instanceof String)) {
                throw new InvalidTypeException("Invalid value stored for name");
            }
            return (String) value;
        }
        
        public @Nullable Object getAdditionalProperty(String name) throws UnsetPropertyException, InvalidAdditionalPropertyException {
            throwIfKeyKnown(name, requiredKeys, optionalKeys);
            throwIfKeyNotPresent(name);
            return get(name);
        }
    }
    
    public interface SetterForTest <T> {
        Map<String, @Nullable Object> getInstance();
        T getBuilderAfterTest(Map<String, @Nullable Object> instance);
        
        default T test(Void value) {
            var instance = getInstance();
            instance.put("test", null);
            return getBuilderAfterTest(instance);
        }
        
        default T test(boolean value) {
            var instance = getInstance();
            instance.put("test", value);
            return getBuilderAfterTest(instance);
        }
        
        default T test(String value) {
            var instance = getInstance();
            instance.put("test", value);
            return getBuilderAfterTest(instance);
        }
        
        default T test(int value) {
            var instance = getInstance();
            instance.put("test", value);
            return getBuilderAfterTest(instance);
        }
        
        default T test(float value) {
            var instance = getInstance();
            instance.put("test", value);
            return getBuilderAfterTest(instance);
        }
        
        default T test(long value) {
            var instance = getInstance();
            instance.put("test", value);
            return getBuilderAfterTest(instance);
        }
        
        default T test(double value) {
            var instance = getInstance();
            instance.put("test", value);
            return getBuilderAfterTest(instance);
        }
        
        default T test(List<?> value) {
            var instance = getInstance();
            instance.put("test", value);
            return getBuilderAfterTest(instance);
        }
        
        default T test(Map<String, ?> value) {
            var instance = getInstance();
            instance.put("test", value);
            return getBuilderAfterTest(instance);
        }
    }
    
    public interface SetterForName <T> {
        Map<String, @Nullable Object> getInstance();
        T getBuilderAfterName(Map<String, @Nullable Object> instance);
        
        default T name(String value) {
            var instance = getInstance();
            instance.put("name", value);
            return getBuilderAfterName(instance);
        }
    }
    
    public static class Schema1Map0Builder extends UnsetAddPropsSetter<Schema1Map0Builder> implements GenericBuilder<Map<String, @Nullable Object>>, SetterForName<Schema1Map0Builder> {
        private final Map<String, @Nullable Object> instance;
        private static final Set<String> knownKeys = Set.of(
            "test",
            "name"
        );
        public Set<String> getKnownKeys() {
            return knownKeys;
        }
        public Schema1Map0Builder(Map<String, @Nullable Object> instance) {
            this.instance = instance;
        }
        public Map<String, @Nullable Object> build() {
            return instance;
        }
        public Map<String, @Nullable Object> getInstance() {
            return instance;
        }
        public Schema1Map0Builder getBuilderAfterName(Map<String, @Nullable Object> instance) {
            return this;
        }
        public Schema1Map0Builder getBuilderAfterAdditionalProperty(Map<String, @Nullable Object> instance) {
            return this;
        }
    }
    
    public static class Schema1MapBuilder implements SetterForTest<Schema1Map0Builder> {
        private final Map<String, @Nullable Object> instance;
        public Schema1MapBuilder() {
            this.instance = new LinkedHashMap<>();
        }
        public Map<String, @Nullable Object> getInstance() {
            return instance;
        }
        public Schema1Map0Builder getBuilderAfterTest(Map<String, @Nullable Object> instance) {
            return new Schema1Map0Builder(instance);
        }
    }
    
    
    public sealed interface Schema1Boxed permits Schema1BoxedMap {
        @Nullable Object data();
    }
    
    public static final class Schema1BoxedMap implements Schema1Boxed {
        public final Schema1Map data;
        private Schema1BoxedMap(Schema1Map data) {
            this.data = data;
        }
        @Override
        public @Nullable Object data() {
            return data;
        }
    }
    
    
    public static class Schema1 extends JsonSchema implements MapSchemaValidator<Schema1Map, Schema1BoxedMap> {
        private static @Nullable Schema1 instance = null;
    
        protected Schema1() {
            super(new JsonSchemaInfo()
                .type(Set.of(Map.class))
                .properties(Map.ofEntries(
                    new PropertyEntry("name", Name.class)
                ))
                .required(Set.of(
                    "test"
                ))
            );
        }
    
        public static Schema1 getInstance() {
            if (instance == null) {
                instance = new Schema1();
            }
            return instance;
        }
        
        public Schema1Map getNewInstance(Map<?, ?> arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) {
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
            return new Schema1Map(castProperties);
        }
        
        public Schema1Map validate(Map<?, ?> arg, SchemaConfiguration configuration) throws ValidationException, InvalidTypeException {
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
        public Schema1BoxedMap validateAndBox(Map<?, ?> arg, SchemaConfiguration configuration) throws ValidationException, InvalidTypeException {
            return new Schema1BoxedMap(validate(arg, configuration));
        }
    }
    
    
    public sealed interface ObjectWithAllOfWithReqTestPropFromUnsetAddProp1Boxed permits ObjectWithAllOfWithReqTestPropFromUnsetAddProp1BoxedVoid, ObjectWithAllOfWithReqTestPropFromUnsetAddProp1BoxedBoolean, ObjectWithAllOfWithReqTestPropFromUnsetAddProp1BoxedNumber, ObjectWithAllOfWithReqTestPropFromUnsetAddProp1BoxedString, ObjectWithAllOfWithReqTestPropFromUnsetAddProp1BoxedList, ObjectWithAllOfWithReqTestPropFromUnsetAddProp1BoxedMap {
        @Nullable Object data();
    }
    
    public static final class ObjectWithAllOfWithReqTestPropFromUnsetAddProp1BoxedVoid implements ObjectWithAllOfWithReqTestPropFromUnsetAddProp1Boxed {
        public final Void data;
        private ObjectWithAllOfWithReqTestPropFromUnsetAddProp1BoxedVoid(Void data) {
            this.data = data;
        }
        @Override
        public @Nullable Object data() {
            return data;
        }
    }
    
    public static final class ObjectWithAllOfWithReqTestPropFromUnsetAddProp1BoxedBoolean implements ObjectWithAllOfWithReqTestPropFromUnsetAddProp1Boxed {
        public final boolean data;
        private ObjectWithAllOfWithReqTestPropFromUnsetAddProp1BoxedBoolean(boolean data) {
            this.data = data;
        }
        @Override
        public @Nullable Object data() {
            return data;
        }
    }
    
    public static final class ObjectWithAllOfWithReqTestPropFromUnsetAddProp1BoxedNumber implements ObjectWithAllOfWithReqTestPropFromUnsetAddProp1Boxed {
        public final Number data;
        private ObjectWithAllOfWithReqTestPropFromUnsetAddProp1BoxedNumber(Number data) {
            this.data = data;
        }
        @Override
        public @Nullable Object data() {
            return data;
        }
    }
    
    public static final class ObjectWithAllOfWithReqTestPropFromUnsetAddProp1BoxedString implements ObjectWithAllOfWithReqTestPropFromUnsetAddProp1Boxed {
        public final String data;
        private ObjectWithAllOfWithReqTestPropFromUnsetAddProp1BoxedString(String data) {
            this.data = data;
        }
        @Override
        public @Nullable Object data() {
            return data;
        }
    }
    
    public static final class ObjectWithAllOfWithReqTestPropFromUnsetAddProp1BoxedList implements ObjectWithAllOfWithReqTestPropFromUnsetAddProp1Boxed {
        public final FrozenList<@Nullable Object> data;
        private ObjectWithAllOfWithReqTestPropFromUnsetAddProp1BoxedList(FrozenList<@Nullable Object> data) {
            this.data = data;
        }
        @Override
        public @Nullable Object data() {
            return data;
        }
    }
    
    public static final class ObjectWithAllOfWithReqTestPropFromUnsetAddProp1BoxedMap implements ObjectWithAllOfWithReqTestPropFromUnsetAddProp1Boxed {
        public final FrozenMap<@Nullable Object> data;
        private ObjectWithAllOfWithReqTestPropFromUnsetAddProp1BoxedMap(FrozenMap<@Nullable Object> data) {
            this.data = data;
        }
        @Override
        public @Nullable Object data() {
            return data;
        }
    }
    
    
    public static class ObjectWithAllOfWithReqTestPropFromUnsetAddProp1 extends JsonSchema implements NullSchemaValidator<ObjectWithAllOfWithReqTestPropFromUnsetAddProp1BoxedVoid>, BooleanSchemaValidator<ObjectWithAllOfWithReqTestPropFromUnsetAddProp1BoxedBoolean>, NumberSchemaValidator<ObjectWithAllOfWithReqTestPropFromUnsetAddProp1BoxedNumber>, StringSchemaValidator<ObjectWithAllOfWithReqTestPropFromUnsetAddProp1BoxedString>, ListSchemaValidator<FrozenList<@Nullable Object>, ObjectWithAllOfWithReqTestPropFromUnsetAddProp1BoxedList>, MapSchemaValidator<FrozenMap<@Nullable Object>, ObjectWithAllOfWithReqTestPropFromUnsetAddProp1BoxedMap> {
        /*
        NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
        Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
    
        Do not edit the class manually.
        */
        private static @Nullable ObjectWithAllOfWithReqTestPropFromUnsetAddProp1 instance = null;
    
        protected ObjectWithAllOfWithReqTestPropFromUnsetAddProp1() {
            super(new JsonSchemaInfo()
                .allOf(List.of(
                    ObjectWithOptionalTestProp.ObjectWithOptionalTestProp1.class,
                    Schema1.class
                ))
            );
        }
    
        public static ObjectWithAllOfWithReqTestPropFromUnsetAddProp1 getInstance() {
            if (instance == null) {
                instance = new ObjectWithAllOfWithReqTestPropFromUnsetAddProp1();
            }
            return instance;
        }
        
        @Override
        public Void validate(Void arg, SchemaConfiguration configuration) throws ValidationException, InvalidTypeException {
            Set<List<Object>> pathSet = new HashSet<>();
            List<Object> pathToItem = List.of("args[0]");
            Void castArg = castToAllowedTypes(arg, pathToItem, pathSet);
            SchemaConfiguration usedConfiguration = Objects.requireNonNullElseGet(configuration, () -> new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone()));
            PathToSchemasMap validatedPathToSchemas = new PathToSchemasMap();
            ValidationMetadata validationMetadata = new ValidationMetadata(pathToItem, usedConfiguration, validatedPathToSchemas, new LinkedHashSet<>());
            getPathToSchemas(this, castArg, validationMetadata, pathSet);
            return castArg;
        }
        
        @Override
        public boolean validate(boolean arg, SchemaConfiguration configuration) throws ValidationException, InvalidTypeException {
            Set<List<Object>> pathSet = new HashSet<>();
            List<Object> pathToItem = List.of("args[0]");
            boolean castArg = castToAllowedTypes(arg, pathToItem, pathSet);
            SchemaConfiguration usedConfiguration = Objects.requireNonNullElseGet(configuration, () -> new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone()));
            PathToSchemasMap validatedPathToSchemas = new PathToSchemasMap();
            ValidationMetadata validationMetadata = new ValidationMetadata(pathToItem, usedConfiguration, validatedPathToSchemas, new LinkedHashSet<>());
            getPathToSchemas(this, castArg, validationMetadata, pathSet);
            return castArg;
        }
        
        @Override
        public Number validate(Number arg, SchemaConfiguration configuration) throws ValidationException, InvalidTypeException {
            Set<List<Object>> pathSet = new HashSet<>();
            List<Object> pathToItem = List.of("args[0]");
            Number castArg = castToAllowedTypes(arg, pathToItem, pathSet);
            SchemaConfiguration usedConfiguration = Objects.requireNonNullElseGet(configuration, () -> new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone()));
            PathToSchemasMap validatedPathToSchemas = new PathToSchemasMap();
            ValidationMetadata validationMetadata = new ValidationMetadata(pathToItem, usedConfiguration, validatedPathToSchemas, new LinkedHashSet<>());
            getPathToSchemas(this, castArg, validationMetadata, pathSet);
            return castArg;
        }
        
        public int validate(int arg, SchemaConfiguration configuration) {
            return (int) validate((Number) arg, configuration);
        }
        
        public long validate(long arg, SchemaConfiguration configuration) {
            return (long) validate((Number) arg, configuration);
        }
        
        public float validate(float arg, SchemaConfiguration configuration) {
            return (float) validate((Number) arg, configuration);
        }
        
        public double validate(double arg, SchemaConfiguration configuration) {
            return (double) validate((Number) arg, configuration);
        }
        
        @Override
        public String validate(String arg, SchemaConfiguration configuration) throws ValidationException, InvalidTypeException {
            Set<List<Object>> pathSet = new HashSet<>();
            List<Object> pathToItem = List.of("args[0]");
            String castArg = castToAllowedTypes(arg, pathToItem, pathSet);
            SchemaConfiguration usedConfiguration = Objects.requireNonNullElseGet(configuration, () -> new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone()));
            PathToSchemasMap validatedPathToSchemas = new PathToSchemasMap();
            ValidationMetadata validationMetadata = new ValidationMetadata(pathToItem, usedConfiguration, validatedPathToSchemas, new LinkedHashSet<>());
            getPathToSchemas(this, castArg, validationMetadata, pathSet);
            return castArg;
        }
        
        public String validate(LocalDate arg, SchemaConfiguration configuration) throws ValidationException {
            return validate(arg.toString(), configuration);
        }
        
        public String validate(ZonedDateTime arg, SchemaConfiguration configuration) throws ValidationException {
            return validate(arg.toString(), configuration);
        }
        
        public String validate(UUID arg, SchemaConfiguration configuration) throws ValidationException {
            return validate(arg.toString(), configuration);
        }
        
        @Override
        public FrozenList<@Nullable Object> getNewInstance(List<?> arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) {
            List<@Nullable Object> items = new ArrayList<>();
            int i = 0;
            for (Object item: arg) {
                List<Object> itemPathToItem = new ArrayList<>(pathToItem);
                itemPathToItem.add(i);
                LinkedHashMap<JsonSchema, Void> schemas = pathToSchemas.get(itemPathToItem);
                if (schemas == null) {
                    throw new InvalidTypeException("Validation result is invalid, schemas must exist for a pathToItem");
                }
                JsonSchema itemSchema = schemas.entrySet().iterator().next().getKey();
                @Nullable Object itemInstance = itemSchema.getNewInstance(item, itemPathToItem, pathToSchemas);
                items.add(itemInstance);
                i += 1;
            }
            FrozenList<@Nullable Object> newInstanceItems = new FrozenList<>(items);
            return newInstanceItems;
        }
        
        public FrozenList<@Nullable Object> validate(List<?> arg, SchemaConfiguration configuration) throws ValidationException {
            Set<List<Object>> pathSet = new HashSet<>();
            List<Object> pathToItem = List.of("args[0");
            List<?> castArg = castToAllowedTypes(arg, pathToItem, pathSet);
            SchemaConfiguration usedConfiguration = Objects.requireNonNullElseGet(configuration, () -> new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone()));
            ValidationMetadata validationMetadata = new ValidationMetadata(pathToItem, usedConfiguration, new PathToSchemasMap(), new LinkedHashSet<>());
            PathToSchemasMap pathToSchemasMap = getPathToSchemas(this, castArg, validationMetadata, pathSet);
            return getNewInstance(castArg, validationMetadata.pathToItem(), pathToSchemasMap);
        }
        
        @Override
        public FrozenMap<@Nullable Object> getNewInstance(Map<?, ?> arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) {
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
            return castProperties;
        }
        
        public FrozenMap<@Nullable Object> validate(Map<?, ?> arg, SchemaConfiguration configuration) throws ValidationException, InvalidTypeException {
            Set<List<Object>> pathSet = new HashSet<>();
            List<Object> pathToItem = List.of("args[0]");
            Map<?, ?> castArg = castToAllowedTypes(arg, pathToItem, pathSet);
            SchemaConfiguration usedConfiguration = Objects.requireNonNullElseGet(configuration, () -> new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone()));
            PathToSchemasMap validatedPathToSchemas = new PathToSchemasMap();
            ValidationMetadata validationMetadata = new ValidationMetadata(pathToItem, usedConfiguration, validatedPathToSchemas, new LinkedHashSet<>());
            PathToSchemasMap pathToSchemasMap = getPathToSchemas(this, castArg, validationMetadata, pathSet);
            return getNewInstance(castArg, validationMetadata.pathToItem(), pathToSchemasMap);
        }
        
        @Override
        public @Nullable Object validate(@Nullable Object arg, SchemaConfiguration configuration) throws ValidationException, InvalidTypeException {
            if (arg == null) {
                return validate((Void) null, configuration);
            } else if (arg instanceof Boolean) {
                boolean boolArg = (Boolean) arg;
                return validate(boolArg, configuration);
            } else if (arg instanceof Number) {
                return validate((Number) arg, configuration);
            } else if (arg instanceof String) {
                return validate((String) arg, configuration);
            } else if (arg instanceof List) {
                return validate((List<?>) arg, configuration);
            } else if (arg instanceof Map) {
                return validate((Map<?, ?>) arg, configuration);
            }
            throw new InvalidTypeException("Invalid input type="+getClass(arg)+". It can't be validated by this schema");
        }        
        @Override
        public @Nullable Object getNewInstance(@Nullable Object arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) throws InvalidTypeException {
            if (arg == null) {
                return getNewInstance((Void) null, pathToItem, pathToSchemas);
            } else if (arg instanceof Boolean) {
                boolean boolArg = (Boolean) arg;
                return getNewInstance(boolArg, pathToItem, pathToSchemas);
            } else if (arg instanceof Number) {
                return getNewInstance((Number) arg, pathToItem, pathToSchemas);
            } else if (arg instanceof String) {
                return getNewInstance((String) arg, pathToItem, pathToSchemas);
            } else if (arg instanceof List) {
                return getNewInstance((List<?>) arg, pathToItem, pathToSchemas);
            } else if (arg instanceof Map) {
                return getNewInstance((Map<?, ?>) arg, pathToItem, pathToSchemas);
            }
            throw new InvalidTypeException("Invalid input type="+getClass(arg)+". It can't be instantiated by this schema");
        }
        @Override
        public ObjectWithAllOfWithReqTestPropFromUnsetAddProp1BoxedVoid validateAndBox(Void arg, SchemaConfiguration configuration) throws ValidationException, InvalidTypeException {
            return new ObjectWithAllOfWithReqTestPropFromUnsetAddProp1BoxedVoid(validate(arg, configuration));
        }
        @Override
        public ObjectWithAllOfWithReqTestPropFromUnsetAddProp1BoxedBoolean validateAndBox(boolean arg, SchemaConfiguration configuration) throws ValidationException, InvalidTypeException {
            return new ObjectWithAllOfWithReqTestPropFromUnsetAddProp1BoxedBoolean(validate(arg, configuration));
        }
        @Override
        public ObjectWithAllOfWithReqTestPropFromUnsetAddProp1BoxedNumber validateAndBox(Number arg, SchemaConfiguration configuration) throws ValidationException, InvalidTypeException {
            return new ObjectWithAllOfWithReqTestPropFromUnsetAddProp1BoxedNumber(validate(arg, configuration));
        }
        @Override
        public ObjectWithAllOfWithReqTestPropFromUnsetAddProp1BoxedString validateAndBox(String arg, SchemaConfiguration configuration) throws ValidationException, InvalidTypeException {
            return new ObjectWithAllOfWithReqTestPropFromUnsetAddProp1BoxedString(validate(arg, configuration));
        }
        @Override
        public ObjectWithAllOfWithReqTestPropFromUnsetAddProp1BoxedList validateAndBox(List<?> arg, SchemaConfiguration configuration) throws ValidationException, InvalidTypeException {
            return new ObjectWithAllOfWithReqTestPropFromUnsetAddProp1BoxedList(validate(arg, configuration));
        }
        @Override
        public ObjectWithAllOfWithReqTestPropFromUnsetAddProp1BoxedMap validateAndBox(Map<?, ?> arg, SchemaConfiguration configuration) throws ValidationException, InvalidTypeException {
            return new ObjectWithAllOfWithReqTestPropFromUnsetAddProp1BoxedMap(validate(arg, configuration));
        }
    }
}
