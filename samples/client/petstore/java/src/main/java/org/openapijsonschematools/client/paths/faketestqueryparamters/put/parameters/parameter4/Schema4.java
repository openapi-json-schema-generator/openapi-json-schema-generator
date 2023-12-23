package org.openapijsonschematools.client.paths.faketestqueryparamters.put.parameters.parameter4;
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
import org.openapijsonschematools.client.exceptions.ValidationException;
import org.openapijsonschematools.client.schemas.StringJsonSchema;
import org.openapijsonschematools.client.schemas.validation.FrozenList;
import org.openapijsonschematools.client.schemas.validation.JsonSchema;
import org.openapijsonschematools.client.schemas.validation.JsonSchemaInfo;
import org.openapijsonschematools.client.schemas.validation.ListSchemaValidator;
import org.openapijsonschematools.client.schemas.validation.PathToSchemasMap;
import org.openapijsonschematools.client.schemas.validation.ValidationMetadata;

public class Schema4 {
    // nest classes so all schemas and input/output classes can be public
    
    
    public static class Items4 extends StringJsonSchema {
        private static @Nullable Items4 instance = null;
        public static Items4 getInstance() {
            if (instance == null) {
                instance = new Items4();
            }
            return instance;
        }
    }
    
    
    public static class SchemaList4 extends FrozenList<String> {
        protected SchemaList4(FrozenList<String> m) {
            super(m);
        }
        public static SchemaList4 of(List<String> arg, SchemaConfiguration configuration) throws ValidationException {
            return Schema41.getInstance().validate(arg, configuration);
        }
    }
    
    public static class SchemaListInput4 {
        // class to build List<String>
    }
    
    
    public static class Schema41 extends JsonSchema implements ListSchemaValidator<SchemaList4> {
        private static @Nullable Schema41 instance = null;
    
        protected Schema41() {
            super(new JsonSchemaInfo()
                .type(Set.of(List.class))
                .items(Items4.class)
            );
        }
    
        public static Schema41 getInstance() {
            if (instance == null) {
                instance = new Schema41();
            }
            return instance;
        }
        
        @Override
        public SchemaList4 getNewInstance(List<?> arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) {
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
            return new SchemaList4(newInstanceItems);
        }
        
        public SchemaList4 validate(List<String> arg, SchemaConfiguration configuration) throws ValidationException {
            Set<List<Object>> pathSet = new HashSet<>();
            List<Object> pathToItem = List.of("args[0");
            List<?> castArg = castToAllowedTypes(arg, pathToItem, pathSet);
            SchemaConfiguration usedConfiguration = Objects.requireNonNullElseGet(configuration, () -> new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone()));
            ValidationMetadata validationMetadata = new ValidationMetadata(pathToItem, usedConfiguration, new PathToSchemasMap(), new LinkedHashSet<>());
            PathToSchemasMap pathToSchemasMap = getPathToSchemas(this, castArg, validationMetadata, pathSet);
            return getNewInstance(castArg, validationMetadata.pathToItem(), pathToSchemasMap);
        }
        
        @Override
        public @Nullable Object getNewInstance(@Nullable Object arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) {
            if (arg instanceof List) {
                return getNewInstance((List<?>) arg, pathToItem, pathToSchemas);
            }
            throw new InvalidTypeException("Invalid input type="+getClass(arg)+". It can't be instantiated by this schema");
        }
    }
}
