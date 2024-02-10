package org.openapijsonschematools.client.components.schemas;
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
import org.openapijsonschematools.client.schemas.NumberJsonSchema;
import org.openapijsonschematools.client.schemas.StringJsonSchema;
import org.openapijsonschematools.client.schemas.validation.FrozenList;
import org.openapijsonschematools.client.schemas.validation.JsonSchema;
import org.openapijsonschematools.client.schemas.validation.JsonSchemaInfo;
import org.openapijsonschematools.client.schemas.validation.ListSchemaValidator;
import org.openapijsonschematools.client.schemas.validation.PathToSchemasMap;
import org.openapijsonschematools.client.schemas.validation.ValidationMetadata;

public class UnevaluateditemsWithItems {
    // nest classes so all schemas and input/output classes can be public
    
    
    public static class Items extends NumberJsonSchema.NumberJsonSchema1 {
        private static @Nullable Items instance = null;
        public static Items getInstance() {
            if (instance == null) {
                instance = new Items();
            }
            return instance;
        }
    }
    
    
    public static class UnevaluateditemsWithItemsList extends FrozenList<Number> {
        protected UnevaluateditemsWithItemsList(FrozenList<Number> m) {
            super(m);
        }
        public static UnevaluateditemsWithItemsList of(List<Number> arg, SchemaConfiguration configuration) throws ValidationException {
            return UnevaluateditemsWithItems1.getInstance().validate(arg, configuration);
        }
    }
    
    public static class UnevaluateditemsWithItemsListBuilder {
        // class to build List<Number>
        private final List<Number> list;
    
        public UnevaluateditemsWithItemsListBuilder() {
            list = new ArrayList<>();
        }
    
        public UnevaluateditemsWithItemsListBuilder(List<Number> list) {
            this.list = list;
        }
        
        public UnevaluateditemsWithItemsListBuilder add(int item) {
            list.add(item);
            return this;
        }
        
        public UnevaluateditemsWithItemsListBuilder add(float item) {
            list.add(item);
            return this;
        }
        
        public UnevaluateditemsWithItemsListBuilder add(long item) {
            list.add(item);
            return this;
        }
        
        public UnevaluateditemsWithItemsListBuilder add(double item) {
            list.add(item);
            return this;
        }
    
        public List<Number> build() {
            return list;
        }
    }
    
    
    public static class UnevaluatedItems extends StringJsonSchema.StringJsonSchema1 {
        private static @Nullable UnevaluatedItems instance = null;
        public static UnevaluatedItems getInstance() {
            if (instance == null) {
                instance = new UnevaluatedItems();
            }
            return instance;
        }
    }
    
    
    public static abstract sealed class UnevaluateditemsWithItems1Boxed permits UnevaluateditemsWithItems1BoxedList {}
    
    public static final class UnevaluateditemsWithItems1BoxedList extends UnevaluateditemsWithItems1Boxed {
        public final UnevaluateditemsWithItemsList data;
        private UnevaluateditemsWithItems1BoxedList(UnevaluateditemsWithItemsList data) {
            this.data = data;
        }
    }
    
    
    
    public static class UnevaluateditemsWithItems1 extends JsonSchema implements ListSchemaValidator<UnevaluateditemsWithItemsList, UnevaluateditemsWithItems1BoxedList> {
        /*
        NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
        Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
    
        Do not edit the class manually.
        */
        private static @Nullable UnevaluateditemsWithItems1 instance = null;
    
        protected UnevaluateditemsWithItems1() {
            super(new JsonSchemaInfo()
                .type(Set.of(List.class))
                .items(Items.class)
                .unevaluatedItems(UnevaluatedItems.class)
            );
        }
    
        public static UnevaluateditemsWithItems1 getInstance() {
            if (instance == null) {
                instance = new UnevaluateditemsWithItems1();
            }
            return instance;
        }
        
        @Override
        public UnevaluateditemsWithItemsList getNewInstance(List<?> arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) {
            List<Number> items = new ArrayList<>();
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
                if (!(itemInstance instanceof Number)) {
                    throw new InvalidTypeException("Invalid instantiated value");
                }
                items.add((Number) itemInstance);
                i += 1;
            }
            FrozenList<Number> newInstanceItems = new FrozenList<>(items);
            return new UnevaluateditemsWithItemsList(newInstanceItems);
        }
        
        public UnevaluateditemsWithItemsList validate(List<?> arg, SchemaConfiguration configuration) throws ValidationException {
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
        @Override
        public UnevaluateditemsWithItems1BoxedList validateAndBox(List<?> arg, SchemaConfiguration configuration) throws ValidationException, InvalidTypeException {
            return new UnevaluateditemsWithItems1BoxedList(validate(arg, configuration));
        }
    }
}
