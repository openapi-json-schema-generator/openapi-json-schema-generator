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
import org.openapijsonschematools.client.schemas.AnyTypeJsonSchema;
import org.openapijsonschematools.client.schemas.GenericBuilder;
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

public class RequiredValidation {
    // nest classes so all schemas and input/output classes can be public
    
    
    public static class Foo extends AnyTypeJsonSchema.AnyTypeJsonSchema1 {
        private static @Nullable Foo instance = null;
        public static Foo getInstance() {
            if (instance == null) {
                instance = new Foo();
            }
            return instance;
        }
    }
    
    
    public static class Bar extends AnyTypeJsonSchema.AnyTypeJsonSchema1 {
        private static @Nullable Bar instance = null;
        public static Bar getInstance() {
            if (instance == null) {
                instance = new Bar();
            }
            return instance;
        }
    }
    
    
    public static class RequiredValidationMap extends FrozenMap<@Nullable Object> {
        protected RequiredValidationMap(FrozenMap<@Nullable Object> m) {
            super(m);
        }
        public static final Set<String> requiredKeys = Set.of(
            "foo"
        );
        public static final Set<String> optionalKeys = Set.of(
            "bar"
        );
        public static RequiredValidationMap of(Map<String, ? extends @Nullable Object> arg, SchemaConfiguration configuration) throws ValidationException {
            return RequiredValidation1.getInstance().validate(arg, configuration);
        }
        
        public @Nullable Object foo() {
            return getOrThrow("foo");
        }
        
        public @Nullable Object bar() throws UnsetPropertyException {
            return getOrThrow("bar");
        }
        
        public @Nullable Object getAdditionalProperty(String name) throws UnsetPropertyException, InvalidAdditionalPropertyException {
            throwIfKeyKnown(name, requiredKeys, optionalKeys);
            throwIfKeyNotPresent(name);
            return get(name);
        }
    }
    
    public interface SetterForFoo <T> {
        Map<String, @Nullable Object> getInstance();
        T getBuilderAfterFoo(Map<String, @Nullable Object> instance);
        
        default T foo(Void value) {
            var instance = getInstance();
            instance.put("foo", null);
            return getBuilderAfterFoo(instance);
        }
        
        default T foo(boolean value) {
            var instance = getInstance();
            instance.put("foo", value);
            return getBuilderAfterFoo(instance);
        }
        
        default T foo(String value) {
            var instance = getInstance();
            instance.put("foo", value);
            return getBuilderAfterFoo(instance);
        }
        
        default T foo(int value) {
            var instance = getInstance();
            instance.put("foo", value);
            return getBuilderAfterFoo(instance);
        }
        
        default T foo(float value) {
            var instance = getInstance();
            instance.put("foo", value);
            return getBuilderAfterFoo(instance);
        }
        
        default T foo(long value) {
            var instance = getInstance();
            instance.put("foo", value);
            return getBuilderAfterFoo(instance);
        }
        
        default T foo(double value) {
            var instance = getInstance();
            instance.put("foo", value);
            return getBuilderAfterFoo(instance);
        }
        
        default T foo(List<?> value) {
            var instance = getInstance();
            instance.put("foo", value);
            return getBuilderAfterFoo(instance);
        }
        
        default T foo(Map<String, ?> value) {
            var instance = getInstance();
            instance.put("foo", value);
            return getBuilderAfterFoo(instance);
        }
    }
    
    public interface SetterForBar <T> {
        Map<String, @Nullable Object> getInstance();
        T getBuilderAfterBar(Map<String, @Nullable Object> instance);
        
        default T bar(Void value) {
            var instance = getInstance();
            instance.put("bar", null);
            return getBuilderAfterBar(instance);
        }
        
        default T bar(boolean value) {
            var instance = getInstance();
            instance.put("bar", value);
            return getBuilderAfterBar(instance);
        }
        
        default T bar(String value) {
            var instance = getInstance();
            instance.put("bar", value);
            return getBuilderAfterBar(instance);
        }
        
        default T bar(int value) {
            var instance = getInstance();
            instance.put("bar", value);
            return getBuilderAfterBar(instance);
        }
        
        default T bar(float value) {
            var instance = getInstance();
            instance.put("bar", value);
            return getBuilderAfterBar(instance);
        }
        
        default T bar(long value) {
            var instance = getInstance();
            instance.put("bar", value);
            return getBuilderAfterBar(instance);
        }
        
        default T bar(double value) {
            var instance = getInstance();
            instance.put("bar", value);
            return getBuilderAfterBar(instance);
        }
        
        default T bar(List<?> value) {
            var instance = getInstance();
            instance.put("bar", value);
            return getBuilderAfterBar(instance);
        }
        
        default T bar(Map<String, ?> value) {
            var instance = getInstance();
            instance.put("bar", value);
            return getBuilderAfterBar(instance);
        }
    }
    
    public static class RequiredValidationMap0Builder extends UnsetAddPropsSetter<RequiredValidationMap0Builder> implements GenericBuilder<Map<String, @Nullable Object>>, SetterForBar<RequiredValidationMap0Builder> {
        private final Map<String, @Nullable Object> instance;
        private static final Set<String> knownKeys = Set.of(
            "foo",
            "bar"
        );
        public Set<String> getKnownKeys() {
            return knownKeys;
        }
        public RequiredValidationMap0Builder(Map<String, @Nullable Object> instance) {
            this.instance = instance;
        }
        public Map<String, @Nullable Object> build() {
            return instance;
        }
        public Map<String, @Nullable Object> getInstance() {
            return instance;
        }
        public RequiredValidationMap0Builder getBuilderAfterBar(Map<String, @Nullable Object> instance) {
            return this;
        }
        public RequiredValidationMap0Builder getBuilderAfterAdditionalProperty(Map<String, @Nullable Object> instance) {
            return this;
        }
    }
    
    public static class RequiredValidationMapBuilder implements SetterForFoo<RequiredValidationMap0Builder> {
        private final Map<String, @Nullable Object> instance;
        public RequiredValidationMapBuilder() {
            this.instance = new LinkedHashMap<>();
        }
        public Map<String, @Nullable Object> getInstance() {
            return instance;
        }
        public RequiredValidationMap0Builder getBuilderAfterFoo(Map<String, @Nullable Object> instance) {
            return new RequiredValidationMap0Builder(instance);
        }
    }
    
    
    public sealed interface RequiredValidation1Boxed permits RequiredValidation1BoxedVoid, RequiredValidation1BoxedBoolean, RequiredValidation1BoxedNumber, RequiredValidation1BoxedString, RequiredValidation1BoxedList, RequiredValidation1BoxedMap {
        @Nullable Object getData();
    }
    
    public record RequiredValidation1BoxedVoid(Void data) implements RequiredValidation1Boxed {
        @Override
        public @Nullable Object getData() {
            return data;
        }
    }
    
    public record RequiredValidation1BoxedBoolean(boolean data) implements RequiredValidation1Boxed {
        @Override
        public @Nullable Object getData() {
            return data;
        }
    }
    
    public record RequiredValidation1BoxedNumber(Number data) implements RequiredValidation1Boxed {
        @Override
        public @Nullable Object getData() {
            return data;
        }
    }
    
    public record RequiredValidation1BoxedString(String data) implements RequiredValidation1Boxed {
        @Override
        public @Nullable Object getData() {
            return data;
        }
    }
    
    public record RequiredValidation1BoxedList(FrozenList<@Nullable Object> data) implements RequiredValidation1Boxed {
        @Override
        public @Nullable Object getData() {
            return data;
        }
    }
    
    public record RequiredValidation1BoxedMap(RequiredValidationMap data) implements RequiredValidation1Boxed {
        @Override
        public @Nullable Object getData() {
            return data;
        }
    }
    
    
    public static class RequiredValidation1 extends JsonSchema<RequiredValidation1Boxed> implements NullSchemaValidator<RequiredValidation1BoxedVoid>, BooleanSchemaValidator<RequiredValidation1BoxedBoolean>, NumberSchemaValidator<RequiredValidation1BoxedNumber>, StringSchemaValidator<RequiredValidation1BoxedString>, ListSchemaValidator<FrozenList<@Nullable Object>, RequiredValidation1BoxedList>, MapSchemaValidator<RequiredValidationMap, RequiredValidation1BoxedMap> {
        /*
        NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
        Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
    
        Do not edit the class manually.
        */
        private static @Nullable RequiredValidation1 instance = null;
    
        protected RequiredValidation1() {
            super(new JsonSchemaInfo()
                .properties(Map.ofEntries(
                    new PropertyEntry("foo", Foo.class),
                    new PropertyEntry("bar", Bar.class)
                ))
                .required(Set.of(
                    "foo"
                ))
            );
        }
    
        public static RequiredValidation1 getInstance() {
            if (instance == null) {
                instance = new RequiredValidation1();
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
                LinkedHashMap<JsonSchema<?>, Void> schemas = pathToSchemas.get(itemPathToItem);
                if (schemas == null) {
                    throw new InvalidTypeException("Validation result is invalid, schemas must exist for a pathToItem");
                }
                JsonSchema<?> itemSchema = schemas.entrySet().iterator().next().getKey();
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
        public RequiredValidationMap getNewInstance(Map<?, ?> arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) {
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
            return new RequiredValidationMap(castProperties);
        }
        
        public RequiredValidationMap validate(Map<?, ?> arg, SchemaConfiguration configuration) throws ValidationException, InvalidTypeException {
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
        public RequiredValidation1BoxedVoid validateAndBox(Void arg, SchemaConfiguration configuration) throws ValidationException, InvalidTypeException {
            return new RequiredValidation1BoxedVoid(validate(arg, configuration));
        }
        @Override
        public RequiredValidation1BoxedBoolean validateAndBox(boolean arg, SchemaConfiguration configuration) throws ValidationException, InvalidTypeException {
            return new RequiredValidation1BoxedBoolean(validate(arg, configuration));
        }
        @Override
        public RequiredValidation1BoxedNumber validateAndBox(Number arg, SchemaConfiguration configuration) throws ValidationException, InvalidTypeException {
            return new RequiredValidation1BoxedNumber(validate(arg, configuration));
        }
        @Override
        public RequiredValidation1BoxedString validateAndBox(String arg, SchemaConfiguration configuration) throws ValidationException, InvalidTypeException {
            return new RequiredValidation1BoxedString(validate(arg, configuration));
        }
        @Override
        public RequiredValidation1BoxedList validateAndBox(List<?> arg, SchemaConfiguration configuration) throws ValidationException, InvalidTypeException {
            return new RequiredValidation1BoxedList(validate(arg, configuration));
        }
        @Override
        public RequiredValidation1BoxedMap validateAndBox(Map<?, ?> arg, SchemaConfiguration configuration) throws ValidationException, InvalidTypeException {
            return new RequiredValidation1BoxedMap(validate(arg, configuration));
        }
        @Override
        public RequiredValidation1Boxed validateAndBox(@Nullable Object arg, SchemaConfiguration configuration) throws ValidationException, InvalidTypeException {
            if (arg == null) {
                Void castArg = (Void) arg;
                return validateAndBox(castArg, configuration);
            } else if (arg instanceof Boolean booleanArg) {
                boolean castArg = booleanArg;
                return validateAndBox(castArg, configuration);
            } else if (arg instanceof String castArg) {
                return validateAndBox(castArg, configuration);
            } else if (arg instanceof Number castArg) {
                return validateAndBox(castArg, configuration);
            } else if (arg instanceof List<?> castArg) {
                return validateAndBox(castArg, configuration);
            } else if (arg instanceof Map<?, ?> castArg) {
                return validateAndBox(castArg, configuration);
            }
            throw new InvalidTypeException("Invalid input type="+getClass(arg)+". It can't be validated by this schema");
        }
    }
}
