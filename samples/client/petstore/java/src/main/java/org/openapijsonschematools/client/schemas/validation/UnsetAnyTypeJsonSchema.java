package org.openapijsonschematools.client.schemas.validation;

import org.openapijsonschematools.client.configurations.JsonSchemaKeywordFlags;
import org.openapijsonschematools.client.configurations.SchemaConfiguration;
import org.openapijsonschematools.client.exceptions.InvalidTypeException;
import org.openapijsonschematools.client.exceptions.ValidationException;
import org.checkerframework.checker.nullness.qual.Nullable;

import java.time.LocalDate;
import java.time.ZonedDateTime;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.HashSet;
import java.util.ArrayList;
import java.util.LinkedHashSet;
import java.util.Set;
import java.util.Map;
import java.util.Objects;
import java.util.UUID;

public class UnsetAnyTypeJsonSchema {
    public sealed interface UnsetAnyTypeJsonSchema1Boxed permits UnsetAnyTypeJsonSchema1BoxedVoid, UnsetAnyTypeJsonSchema1BoxedBoolean, UnsetAnyTypeJsonSchema1BoxedNumber, UnsetAnyTypeJsonSchema1BoxedString, UnsetAnyTypeJsonSchema1BoxedList, UnsetAnyTypeJsonSchema1BoxedMap {
        @Nullable Object data();
    }
    public static final class UnsetAnyTypeJsonSchema1BoxedVoid implements UnsetAnyTypeJsonSchema1Boxed {
        public final Void data;
        private UnsetAnyTypeJsonSchema1BoxedVoid(Void data) {
            this.data = data;
        }
        @Override
        public @Nullable Object data() {
            return data;
        }
    }
    public static final class UnsetAnyTypeJsonSchema1BoxedBoolean implements UnsetAnyTypeJsonSchema1Boxed {
        public final boolean data;
        private UnsetAnyTypeJsonSchema1BoxedBoolean(boolean data) {
            this.data = data;
        }
        @Override
        public @Nullable Object data() {
            return data;
        }
    }
    public static final class UnsetAnyTypeJsonSchema1BoxedNumber implements UnsetAnyTypeJsonSchema1Boxed {
        public final Number data;
        private UnsetAnyTypeJsonSchema1BoxedNumber(Number data) {
            this.data = data;
        }
        @Override
        public @Nullable Object data() {
            return data;
        }
    }
    public static final class UnsetAnyTypeJsonSchema1BoxedString implements UnsetAnyTypeJsonSchema1Boxed {
        public final String data;
        private UnsetAnyTypeJsonSchema1BoxedString(String data) {
            this.data = data;
        }
        @Override
        public @Nullable Object data() {
            return data;
        }
    }
    public static final class UnsetAnyTypeJsonSchema1BoxedList implements UnsetAnyTypeJsonSchema1Boxed {
        public final FrozenList<@Nullable Object> data;
        private UnsetAnyTypeJsonSchema1BoxedList(FrozenList<@Nullable Object> data) {
            this.data = data;
        }
        @Override
        public @Nullable Object data() {
            return data;
        }
    }
    public static final class UnsetAnyTypeJsonSchema1BoxedMap implements UnsetAnyTypeJsonSchema1Boxed {
        public final FrozenMap<@Nullable Object> data;
        private UnsetAnyTypeJsonSchema1BoxedMap(FrozenMap<@Nullable Object> data) {
            this.data = data;
        }
        @Override
        public @Nullable Object data() {
            return data;
        }
    }
    public static class UnsetAnyTypeJsonSchema1 extends JsonSchema implements NullSchemaValidator<UnsetAnyTypeJsonSchema1BoxedVoid>, BooleanSchemaValidator<UnsetAnyTypeJsonSchema1BoxedBoolean>, NumberSchemaValidator<UnsetAnyTypeJsonSchema1BoxedNumber>, StringSchemaValidator<UnsetAnyTypeJsonSchema1BoxedString>, ListSchemaValidator<FrozenList<@Nullable Object>, UnsetAnyTypeJsonSchema1BoxedList>, MapSchemaValidator<FrozenMap<@Nullable Object>, UnsetAnyTypeJsonSchema1BoxedMap> {
        private static @Nullable UnsetAnyTypeJsonSchema1 instance = null;

        protected UnsetAnyTypeJsonSchema1() {
            super(new JsonSchemaInfo());
        }

        public static UnsetAnyTypeJsonSchema1 getInstance() {
            if (instance == null) {
                instance = new UnsetAnyTypeJsonSchema1();
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
            PathToSchemasMap pathToSchemasMap = getPathToSchemas(this, castArg, validationMetadata, pathSet);
            return getNewInstance(castArg, validationMetadata.pathToItem(), pathToSchemasMap);
        }

        @Override
        public boolean validate(boolean arg, SchemaConfiguration configuration) throws ValidationException, InvalidTypeException {
            Set<List<Object>> pathSet = new HashSet<>();
            List<Object> pathToItem = List.of("args[0]");
            boolean castArg = castToAllowedTypes(arg, pathToItem, pathSet);
            SchemaConfiguration usedConfiguration = Objects.requireNonNullElseGet(configuration, () -> new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone()));
            PathToSchemasMap validatedPathToSchemas = new PathToSchemasMap();
            ValidationMetadata validationMetadata = new ValidationMetadata(pathToItem, usedConfiguration, validatedPathToSchemas, new LinkedHashSet<>());
            PathToSchemasMap pathToSchemasMap = getPathToSchemas(this, castArg, validationMetadata, pathSet);
            return getNewInstance(castArg, validationMetadata.pathToItem(), pathToSchemasMap);
        }

        @Override
        public Number validate(Number arg, SchemaConfiguration configuration) throws ValidationException, InvalidTypeException {
            Set<List<Object>> pathSet = new HashSet<>();
            List<Object> pathToItem = List.of("args[0]");
            Number castArg = castToAllowedTypes(arg, pathToItem, pathSet);
            SchemaConfiguration usedConfiguration = Objects.requireNonNullElseGet(configuration, () -> new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone()));
            PathToSchemasMap validatedPathToSchemas = new PathToSchemasMap();
            ValidationMetadata validationMetadata = new ValidationMetadata(pathToItem, usedConfiguration, validatedPathToSchemas, new LinkedHashSet<>());
            PathToSchemasMap pathToSchemasMap = getPathToSchemas(this, castArg, validationMetadata, pathSet);
            return getNewInstance(castArg, validationMetadata.pathToItem(), pathToSchemasMap);
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
            PathToSchemasMap pathToSchemasMap = getPathToSchemas(this, castArg, validationMetadata, pathSet);
            return getNewInstance(castArg, validationMetadata.pathToItem(), pathToSchemasMap);
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
                @Nullable Object castItem = itemSchema.getNewInstance(item, itemPathToItem, pathToSchemas);
                items.add(castItem);
                i += 1;
            }
            return new FrozenList<>(items);
        }

        public FrozenList<@Nullable Object> validate(List<?> arg, SchemaConfiguration configuration) throws ValidationException, InvalidTypeException {
            Set<List<Object>> pathSet = new HashSet<>();
            List<Object> pathToItem = List.of("args[0]");
            List<?> castArg = castToAllowedTypes(arg, pathToItem, pathSet);
            SchemaConfiguration usedConfiguration = Objects.requireNonNullElseGet(configuration, () -> new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone()));
            PathToSchemasMap validatedPathToSchemas = new PathToSchemasMap();
            ValidationMetadata validationMetadata = new ValidationMetadata(pathToItem, usedConfiguration, validatedPathToSchemas, new LinkedHashSet<>());
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
                @Nullable Object castValue = propertySchema.getNewInstance(value, propertyPathToItem, pathToSchemas);
                properties.put(propertyName, castValue);
            }
            return new FrozenMap<>(properties);
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
        public @Nullable Object getNewInstance(@Nullable Object arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) {
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
        public UnsetAnyTypeJsonSchema1BoxedVoid validateAndBox(Void arg, SchemaConfiguration configuration) throws ValidationException, InvalidTypeException {
            return new UnsetAnyTypeJsonSchema1BoxedVoid(validate(arg, configuration));
        }
        @Override
        public UnsetAnyTypeJsonSchema1BoxedBoolean validateAndBox(boolean arg, SchemaConfiguration configuration) throws ValidationException, InvalidTypeException {
            return new UnsetAnyTypeJsonSchema1BoxedBoolean(validate(arg, configuration));
        }
        @Override
        public UnsetAnyTypeJsonSchema1BoxedNumber validateAndBox(Number arg, SchemaConfiguration configuration) throws ValidationException, InvalidTypeException {
            return new UnsetAnyTypeJsonSchema1BoxedNumber(validate(arg, configuration));
        }
        @Override
        public UnsetAnyTypeJsonSchema1BoxedString validateAndBox(String arg, SchemaConfiguration configuration) throws ValidationException, InvalidTypeException {
            return new UnsetAnyTypeJsonSchema1BoxedString(validate(arg, configuration));
        }
        @Override
        public UnsetAnyTypeJsonSchema1BoxedList validateAndBox(List<?> arg, SchemaConfiguration configuration) throws ValidationException, InvalidTypeException {
            return new UnsetAnyTypeJsonSchema1BoxedList(validate(arg, configuration));
        }
        @Override
        public UnsetAnyTypeJsonSchema1BoxedMap validateAndBox(Map<?, ?> arg, SchemaConfiguration configuration) throws ValidationException, InvalidTypeException {
            return new UnsetAnyTypeJsonSchema1BoxedMap(validate(arg, configuration));
        }
    }
}