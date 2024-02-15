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
import org.openapijsonschematools.client.schemas.validation.FrozenList;
import org.openapijsonschematools.client.schemas.validation.JsonSchema;
import org.openapijsonschematools.client.schemas.validation.JsonSchemaInfo;
import org.openapijsonschematools.client.schemas.validation.ListSchemaValidator;
import org.openapijsonschematools.client.schemas.validation.PathToSchemasMap;
import org.openapijsonschematools.client.schemas.validation.ValidationMetadata;

public class ArrayOfEnums {
    // nest classes so all schemas and input/output classes can be public
    
    
    public static class ArrayOfEnumsList extends FrozenList<@Nullable String> {
        protected ArrayOfEnumsList(FrozenList<@Nullable String> m) {
            super(m);
        }
        public static ArrayOfEnumsList of(List<? extends @Nullable String> arg, SchemaConfiguration configuration) throws ValidationException {
            return ArrayOfEnums1.getInstance().validate(arg, configuration);
        }
    }
    
    public static class ArrayOfEnumsListBuilder {
        // class to build List<@Nullable String>
        private final List<@Nullable String> list;
    
        public ArrayOfEnumsListBuilder() {
            list = new ArrayList<>();
        }
    
        public ArrayOfEnumsListBuilder(List<@Nullable String> list) {
            this.list = list;
        }
        
        public ArrayOfEnumsListBuilder add(Void item) {
            list.add(null);
            return this;
        }
        
        public ArrayOfEnumsListBuilder add(String item) {
            list.add(item);
            return this;
        }
        
        public ArrayOfEnumsListBuilder add(StringEnum.StringStringEnumEnums item) {
            list.add(item.value());
            return this;
        }
        
        public ArrayOfEnumsListBuilder add(StringEnum.NullStringEnumEnums item) {
            list.add(null);
            return this;
        }
    
        public List<@Nullable String> build() {
            return list;
        }
    }
    
    
    public static abstract sealed class ArrayOfEnums1Boxed permits ArrayOfEnums1BoxedList {
        public abstract @Nullable Object data();
    }
    
    public static final class ArrayOfEnums1BoxedList extends ArrayOfEnums1Boxed {
        public final ArrayOfEnumsList data;
        private ArrayOfEnums1BoxedList(ArrayOfEnumsList data) {
            this.data = data;
        }
        @Override
        public @Nullable Object data() {
            return data;
        }
    }
    
    
    
    public static class ArrayOfEnums1 extends JsonSchema implements ListSchemaValidator<ArrayOfEnumsList, ArrayOfEnums1BoxedList> {
        /*
        NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
        Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
    
        Do not edit the class manually.
        */
        private static @Nullable ArrayOfEnums1 instance = null;
    
        protected ArrayOfEnums1() {
            super(new JsonSchemaInfo()
                .type(Set.of(List.class))
                .items(StringEnum.StringEnum1.class)
            );
        }
    
        public static ArrayOfEnums1 getInstance() {
            if (instance == null) {
                instance = new ArrayOfEnums1();
            }
            return instance;
        }
        
        @Override
        public ArrayOfEnumsList getNewInstance(List<?> arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) {
            List<@Nullable String> items = new ArrayList<>();
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
                items.add((@Nullable String) itemInstance);
                i += 1;
            }
            FrozenList<@Nullable String> newInstanceItems = new FrozenList<>(items);
            return new ArrayOfEnumsList(newInstanceItems);
        }
        
        public ArrayOfEnumsList validate(List<?> arg, SchemaConfiguration configuration) throws ValidationException {
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
        public ArrayOfEnums1BoxedList validateAndBox(List<?> arg, SchemaConfiguration configuration) throws ValidationException, InvalidTypeException {
            return new ArrayOfEnums1BoxedList(validate(arg, configuration));
        }
    }
}
