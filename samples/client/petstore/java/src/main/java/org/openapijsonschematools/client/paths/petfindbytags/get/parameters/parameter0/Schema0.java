package org.openapijsonschematools.client.paths.petfindbytags.get.parameters.parameter0;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.LinkedHashMap;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Objects;
import java.util.Set;
import org.checkerframework.checker.nullness.qual.Nullable;
import org.openapijsonschematools.client.configurations.JsonSchemaKeywordFlags;
import org.openapijsonschematools.client.configurations.SchemaConfiguration;
import org.openapijsonschematools.client.exceptions.ValidationException;
import org.openapijsonschematools.client.schemas.StringJsonSchema;
import org.openapijsonschematools.client.schemas.validation.FrozenList;
import org.openapijsonschematools.client.schemas.validation.JsonSchema;
import org.openapijsonschematools.client.schemas.validation.JsonSchemaInfo;
import org.openapijsonschematools.client.schemas.validation.ListSchemaValidator;
import org.openapijsonschematools.client.schemas.validation.PathToSchemasMap;
import org.openapijsonschematools.client.schemas.validation.ValidationMetadata;

public class Schema0 {
    // nest classes so all schemas and input/output classes can be public
    
    
    public static class Items0 extends StringJsonSchema.StringJsonSchema1 {
        private static @Nullable Items0 instance = null;
        public static Items0 getInstance() {
            if (instance == null) {
                instance = new Items0();
            }
            return instance;
        }
    }
    
    
    public static class SchemaList0 extends FrozenList<String> {
        protected SchemaList0(FrozenList<String> m) {
            super(m);
        }
        public static SchemaList0 of(List<String> arg, SchemaConfiguration configuration) throws ValidationException {
            return Schema01.getInstance().validate(arg, configuration);
        }
    }
    
    public static class SchemaListBuilder0 {
        // class to build List<String>
        private final List<String> list;
    
        public SchemaListBuilder0() {
            list = new ArrayList<>();
        }
    
        public SchemaListBuilder0(List<String> list) {
            this.list = list;
        }
        
        public SchemaListBuilder0 add(String item) {
            list.add(item);
            return this;
        }
    
        public List<String> build() {
            return list;
        }
    }
    
    
    public sealed interface Schema01Boxed permits Schema01BoxedList {
        @Nullable Object getData();
    }
    
    public record Schema01BoxedList(SchemaList0 data) implements Schema01Boxed {
        @Override
        public @Nullable Object getData() {
            return data;
        }
    }
    
    
    
    public static class Schema01 extends JsonSchema<Schema01Boxed> implements ListSchemaValidator<SchemaList0, Schema01BoxedList> {
        private static @Nullable Schema01 instance = null;
    
        protected Schema01() {
            super(new JsonSchemaInfo()
                .type(Set.of(List.class))
                .items(Items0.class)
            );
        }
    
        public static Schema01 getInstance() {
            if (instance == null) {
                instance = new Schema01();
            }
            return instance;
        }
        
        @Override
        public SchemaList0 getNewInstance(List<?> arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) {
            List<String> items = new ArrayList<>();
            int i = 0;
            for (Object item: arg) {
                List<Object> itemPathToItem = new ArrayList<>(pathToItem);
                itemPathToItem.add(i);
                LinkedHashMap<JsonSchema<?>, Void> schemas = pathToSchemas.get(itemPathToItem);
                if (schemas == null) {
                    throw new RuntimeException("Validation result is invalid, schemas must exist for a pathToItem");
                }
                JsonSchema<?> itemSchema = schemas.entrySet().iterator().next().getKey();
                @Nullable Object itemInstance = itemSchema.getNewInstance(item, itemPathToItem, pathToSchemas);
                if (!(itemInstance instanceof String)) {
                    throw new RuntimeException("Invalid instantiated value");
                }
                items.add((String) itemInstance);
                i += 1;
            }
            FrozenList<String> newInstanceItems = new FrozenList<>(items);
            return new SchemaList0(newInstanceItems);
        }
        
        public SchemaList0 validate(List<?> arg, SchemaConfiguration configuration) throws ValidationException {
            Set<List<Object>> pathSet = new HashSet<>();
            List<Object> pathToItem = List.of("args[0");
            List<?> castArg = castToAllowedTypes(arg, pathToItem, pathSet);
            SchemaConfiguration usedConfiguration = Objects.requireNonNullElseGet(configuration, () -> new SchemaConfiguration(new JsonSchemaKeywordFlags.Builder().build()));
            ValidationMetadata validationMetadata = new ValidationMetadata(pathToItem, usedConfiguration, new PathToSchemasMap(), new LinkedHashSet<>());
            PathToSchemasMap pathToSchemasMap = getPathToSchemas(this, castArg, validationMetadata, pathSet);
            return getNewInstance(castArg, validationMetadata.pathToItem(), pathToSchemasMap);
        }
        
        @Override
        public @Nullable Object validate(@Nullable Object arg, SchemaConfiguration configuration) throws ValidationException {
            if (arg instanceof List) {
                return validate((List<?>) arg, configuration);
            }
            throw new ValidationException("Invalid input type="+getClass(arg)+". It can't be validated by this schema");
        }        
        @Override
        public @Nullable Object getNewInstance(@Nullable Object arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) {
            if (arg instanceof List) {
                return getNewInstance((List<?>) arg, pathToItem, pathToSchemas);
            }
            throw new RuntimeException("Invalid input type="+getClass(arg)+". It can't be instantiated by this schema");
        }
        @Override
        public Schema01BoxedList validateAndBox(List<?> arg, SchemaConfiguration configuration) throws ValidationException {
            return new Schema01BoxedList(validate(arg, configuration));
        }
        @Override
        public Schema01Boxed validateAndBox(@Nullable Object arg, SchemaConfiguration configuration) throws ValidationException {
            if (arg instanceof List<?> castArg) {
                return validateAndBox(castArg, configuration);
            }
            throw new ValidationException("Invalid input type="+getClass(arg)+". It can't be validated by this schema");
        }
    }
}
