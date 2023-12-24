package org.openapijsonschematools.client.components.schemas;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.LinkedHashMap;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Map;
import java.util.Objects;
import java.util.Set;
import org.checkerframework.checker.nullness.qual.NonNull;
import org.checkerframework.checker.nullness.qual.Nullable;
import org.openapijsonschematools.client.configurations.JsonSchemaKeywordFlags;
import org.openapijsonschematools.client.configurations.SchemaConfiguration;
import org.openapijsonschematools.client.exceptions.InvalidTypeException;
import org.openapijsonschematools.client.exceptions.UnsetPropertyException;
import org.openapijsonschematools.client.exceptions.ValidationException;
import org.openapijsonschematools.client.schemas.AnyTypeJsonSchema;
import org.openapijsonschematools.client.schemas.IntJsonSchema;
import org.openapijsonschematools.client.schemas.NotAnyTypeJsonSchema;
import org.openapijsonschematools.client.schemas.validation.FrozenList;
import org.openapijsonschematools.client.schemas.validation.FrozenMap;
import org.openapijsonschematools.client.schemas.validation.JsonSchema;
import org.openapijsonschematools.client.schemas.validation.JsonSchemaInfo;
import org.openapijsonschematools.client.schemas.validation.ListSchemaValidator;
import org.openapijsonschematools.client.schemas.validation.MapSchemaValidator;
import org.openapijsonschematools.client.schemas.validation.PathToSchemasMap;
import org.openapijsonschematools.client.schemas.validation.PropertyEntry;
import org.openapijsonschematools.client.schemas.validation.ValidationMetadata;

public class PaginatedResultMyObjectDto {
    // nest classes so all schemas and input/output classes can be public
    
    
    public static class AdditionalProperties extends NotAnyTypeJsonSchema {
        // NotAnyTypeSchema
        private static @Nullable AdditionalProperties instance = null;
        public static AdditionalProperties getInstance() {
            if (instance == null) {
                instance = new AdditionalProperties();
            }
            return instance;
        }
    }
    
    
    public static class Count extends IntJsonSchema {
        private static @Nullable Count instance = null;
        public static Count getInstance() {
            if (instance == null) {
                instance = new Count();
            }
            return instance;
        }
    }
    
    
    public static class ResultsList extends FrozenList<MyObjectDto.MyObjectDtoMap> {
        protected ResultsList(FrozenList<MyObjectDto.MyObjectDtoMap> m) {
            super(m);
        }
        public static ResultsList of(List<Map<String, String>> arg, SchemaConfiguration configuration) throws ValidationException {
            return Results.getInstance().validate(arg, configuration);
        }
    }
    
    public static class ResultsListInput {
        // class to build List<Map<String, String>>
    }
    
    
    public static class Results extends JsonSchema implements ListSchemaValidator<ResultsList> {
        private static @Nullable Results instance = null;
    
        protected Results() {
            super(new JsonSchemaInfo()
                .type(Set.of(List.class))
                .items(MyObjectDto.MyObjectDto1.class)
            );
        }
    
        public static Results getInstance() {
            if (instance == null) {
                instance = new Results();
            }
            return instance;
        }
        
        @Override
        public ResultsList getNewInstance(List<?> arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) {
            List<MyObjectDto.MyObjectDtoMap> items = new ArrayList<>();
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
                if (!(itemInstance instanceof MyObjectDto.MyObjectDtoMap)) {
                    throw new InvalidTypeException("Invalid instantiated value");
                }
                items.add((MyObjectDto.MyObjectDtoMap) itemInstance);
                i += 1;
            }
            FrozenList<MyObjectDto.MyObjectDtoMap> newInstanceItems = new FrozenList<>(items);
            return new ResultsList(newInstanceItems);
        }
        
        public ResultsList validate(List<?> arg, SchemaConfiguration configuration) throws ValidationException {
            Set<List<Object>> pathSet = new HashSet<>();
            List<Object> pathToItem = List.of("args[0");
            List<?> castArg = castToAllowedTypes(arg, pathToItem, pathSet);
            SchemaConfiguration usedConfiguration = Objects.requireNonNullElseGet(configuration, () -> new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone()));
            ValidationMetadata validationMetadata = new ValidationMetadata(pathToItem, usedConfiguration, new PathToSchemasMap(), new LinkedHashSet<>());
            PathToSchemasMap pathToSchemasMap = getPathToSchemas(this, castArg, validationMetadata, pathSet);
            return getNewInstance(castArg, validationMetadata.pathToItem(), pathToSchemasMap);
        }
        
        @Override
        public @Nullable Object validate(@Nullable Object arg, SchemaConfiguration configuration) throws ValidationException, InvalidTypeException {
            if (arg instanceof List) {
                return validate((List<?>) arg, configuration);
            }
            throw new InvalidTypeException("Invalid input type="+getClass(arg)+". It can't be validated by this schema");
        }        
        @Override
        public @Nullable Object getNewInstance(@Nullable Object arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) throws InvalidTypeException {
            if (arg instanceof List) {
                return getNewInstance((List<?>) arg, pathToItem, pathToSchemas);
            }
            throw new InvalidTypeException("Invalid input type="+getClass(arg)+". It can't be instantiated by this schema");
        }
    }    
    
    public static class PaginatedResultMyObjectDtoMap extends FrozenMap<Object> {
        protected PaginatedResultMyObjectDtoMap(FrozenMap<Object> m) {
            super(m);
        }
        public static final Set<String> requiredKeys = Set.of(
            "count",
            "results"
        );
        public static final Set<String> optionalKeys = Set.of();
        public static PaginatedResultMyObjectDtoMap of(Map<String, Object> arg, SchemaConfiguration configuration) throws ValidationException {
            return PaginatedResultMyObjectDto1.getInstance().validate(arg, configuration);
        }
        
        public long count() {
                        Object value = get("count");
            if (!(value instanceof Long)) {
                throw new InvalidTypeException("Invalid value stored for count");
            }
            return (long) value;
        }
        
        public ResultsList results() {
                        Object value = get("results");
            if (!(value instanceof ResultsList)) {
                throw new InvalidTypeException("Invalid value stored for results");
            }
            return (ResultsList) value;
        }
    }
    public static class PaginatedResultMyObjectDtoMapInput {
        // empty mapping
    }
    
    
    public static class PaginatedResultMyObjectDto1 extends JsonSchema implements MapSchemaValidator<PaginatedResultMyObjectDtoMap> {
        /*
        NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
        Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
    
        Do not edit the class manually.
        */
        private static @Nullable PaginatedResultMyObjectDto1 instance = null;
    
        protected PaginatedResultMyObjectDto1() {
            super(new JsonSchemaInfo()
                .type(Set.of(Map.class))
                .properties(Map.ofEntries(
                    new PropertyEntry("count", Count.class),
                    new PropertyEntry("results", Results.class)
                ))
                .required(Set.of(
                    "count",
                    "results"
                ))
                .additionalProperties(AdditionalProperties.class)
            );
        }
    
        public static PaginatedResultMyObjectDto1 getInstance() {
            if (instance == null) {
                instance = new PaginatedResultMyObjectDto1();
            }
            return instance;
        }
        
        public PaginatedResultMyObjectDtoMap getNewInstance(Map<?, ?> arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) {
            LinkedHashMap<String, Object> properties = new LinkedHashMap<>();
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
                if (!(propertyInstance instanceof Object)) {
                    throw new InvalidTypeException("Invalid instantiated value");
                }
                properties.put(propertyName, (Object) propertyInstance);
            }
            FrozenMap<Object> castProperties = new FrozenMap<>(properties);
            return new PaginatedResultMyObjectDtoMap(castProperties);
        }
        
        public PaginatedResultMyObjectDtoMap validate(Map<?, ?> arg, SchemaConfiguration configuration) throws ValidationException, InvalidTypeException {
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
