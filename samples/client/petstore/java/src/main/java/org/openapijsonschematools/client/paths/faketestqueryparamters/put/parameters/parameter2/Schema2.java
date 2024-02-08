package org.openapijsonschematools.client.paths.faketestqueryparamters.put.parameters.parameter2;
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
import org.openapijsonschematools.client.exceptions.InvalidTypeException;
import org.openapijsonschematools.client.exceptions.ValidationException;
import org.openapijsonschematools.client.schemas.StringJsonSchema;
import org.openapijsonschematools.client.schemas.validation.FrozenList;
import org.openapijsonschematools.client.schemas.validation.JsonSchema;
import org.openapijsonschematools.client.schemas.validation.JsonSchemaInfo;
import org.openapijsonschematools.client.schemas.validation.ListSchemaValidator;
import org.openapijsonschematools.client.schemas.validation.PathToSchemasMap;
import org.openapijsonschematools.client.schemas.validation.ValidationMetadata;

public class Schema2 {
    // nest classes so all schemas and input/output classes can be public
    
    
    public static class Items2 extends StringJsonSchema {
        private static @Nullable Items2 instance = null;
        public static Items2 getInstance() {
            if (instance == null) {
                instance = new Items2();
            }
            return instance;
        }
    }
    
    
    public static class SchemaList2 extends FrozenList<String> {
        protected SchemaList2(FrozenList<String> m) {
            super(m);
        }
        public static SchemaList2 of(List<String> arg, SchemaConfiguration configuration) throws ValidationException {
            return Schema21.getInstance().validate(arg, configuration);
        }
    }
    
    public static class SchemaListBuilder2 {
        // class to build List<String>
        private final List<String> list;
    
        public SchemaListBuilder2() {
            list = new ArrayList<>();
        }
    
        public SchemaListBuilder2(List<String> list) {
            this.list = list;
        }
        
        public SchemaListBuilder2 add(String item) {
            list.add(item);
            return this;
        }
    
        public List<String> build() {
            return list;
        }
    }
    
    
    public static class Schema21 extends JsonSchema implements ListSchemaValidator<SchemaList2> {
        private static @Nullable Schema21 instance = null;
    
        protected Schema21() {
            super(new JsonSchemaInfo()
                .type(Set.of(List.class))
                .items(Items2.class)
            );
        }
    
        public static Schema21 getInstance() {
            if (instance == null) {
                instance = new Schema21();
            }
            return instance;
        }
        
        @Override
        public SchemaList2 getNewInstance(List<?> arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) {
            List<String> items = new ArrayList<>();
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
                if (!(itemInstance instanceof String)) {
                    throw new InvalidTypeException("Invalid instantiated value");
                }
                items.add((String) itemInstance);
                i += 1;
            }
            FrozenList<String> newInstanceItems = new FrozenList<>(items);
            return new SchemaList2(newInstanceItems);
        }
        
        public SchemaList2 validate(List<?> arg, SchemaConfiguration configuration) throws ValidationException {
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
        public static abstract sealed class Schema21Boxed permits Schema21BoxedList {}
        public static final class Schema21BoxedList extends Schema21Boxed {
            public final SchemaList2 data;
            private Schema21BoxedList(SchemaList2 data) {
                this.data = data;
            }
        }
        public Schema21BoxedList validateAndBox(List<?> arg, SchemaConfiguration configuration) throws ValidationException, InvalidTypeException {
            return new Schema21BoxedList(validate(arg, configuration));
        }
    }
}
