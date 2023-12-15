package org.openapijsonschematools.client.components.schemas;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.LinkedHashMap;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Map;
import java.util.Objects;
import java.util.Set;
import org.openapijsonschematools.client.configurations.JsonSchemaKeywordFlags;
import org.openapijsonschematools.client.configurations.SchemaConfiguration;
import org.openapijsonschematools.client.exceptions.InvalidTypeException;
import org.openapijsonschematools.client.exceptions.ValidationException;
import org.openapijsonschematools.client.schemas.NumberJsonSchema;
import org.openapijsonschematools.client.schemas.validation.FrozenList;
import org.openapijsonschematools.client.schemas.validation.JsonSchema;
import org.openapijsonschematools.client.schemas.validation.JsonSchemaInfo;
import org.openapijsonschematools.client.schemas.validation.ListSchemaValidator;
import org.openapijsonschematools.client.schemas.validation.PathToSchemasMap;
import org.openapijsonschematools.client.schemas.validation.ValidationMetadata;

public class NestedItems {
    // nest classes so all schemas and input/output classes can be public
    
    
    public static class Items3 extends NumberJsonSchema {}
    
    
    public static class ItemsList extends FrozenList<Number> {
        ItemsList(FrozenList<Number> m) {
            super(m);
        }
        public static ItemsList of(List<Number> arg, SchemaConfiguration configuration) throws ValidationException {
            return Items2.getInstance().validate(arg, configuration);
        }
    }
    
    public static class ItemsListInput {
        // class to build List<Number>
    }
    
    
    public static class Items2 extends JsonSchema implements ListSchemaValidator<Number, Number, ItemsList> {
        private static Items2 instance;
    
        protected Items2() {
            super(new JsonSchemaInfo()
                .type(Set.of(FrozenList.class))
                .items(Items3.class)
            );
        }
    
        public static Items2 getInstance() {
            if (instance == null) {
                instance = new Items2();
            }
            return instance;
        }
        
        @Override
        public FrozenList<Number> castToAllowedTypes(List<Number> arg, List<Object> pathToItem, Set<List<Object>> pathSet) {
            pathSet.add(pathToItem);
            List<Number> argFixed = new ArrayList<>();
            int i =0;
            for (Number item: arg) {
                List<Object> newPathToItem = new ArrayList<>(pathToItem);
                newPathToItem.add(i);
                                Number fixedVal = (Number) castToAllowedObjectTypes(item, newPathToItem, pathSet);
                argFixed.add(fixedVal);
                i += 1;
            }
            return new FrozenList<>(argFixed);
        }
        
        @Override
        public ItemsList getNewInstance(FrozenList<Number> arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) {
            ArrayList<Number> items = new ArrayList<>();
            int i = 0;
            for (Number item: arg) {
                List<Object> itemPathToItem = new ArrayList<>(pathToItem);
                itemPathToItem.add(i);
                JsonSchema itemSchema = pathToSchemas.get(itemPathToItem).entrySet().iterator().next().getKey();
                                Number castItem = (Number) itemSchema.getNewInstance(item, itemPathToItem, pathToSchemas);
                items.add(castItem);
                i += 1;
            }
            FrozenList<Number> newInstanceItems = new FrozenList<>(items);
            return new ItemsList(newInstanceItems);
        }
        
        @Override
        public ItemsList validate(List<Number> arg, SchemaConfiguration configuration) throws ValidationException {
            Set<List<Object>> pathSet = new HashSet<>();
            List<Object> pathToItem = List.of("args[0");
            FrozenList<Number> castArg = castToAllowedTypes(arg, pathToItem, pathSet);
            SchemaConfiguration usedConfiguration = Objects.requireNonNullElseGet(configuration, () -> new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone()));
            ValidationMetadata validationMetadata = new ValidationMetadata(pathToItem, usedConfiguration, new PathToSchemasMap(), new LinkedHashSet<>());
            PathToSchemasMap pathToSchemasMap = getPathToSchemas(this, castArg, validationMetadata, pathSet);
            return getNewInstance(castArg, validationMetadata.pathToItem(), pathToSchemasMap);
        }
        
        @Override
        public Object getNewInstance(Object arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) {
            if (arg instanceof FrozenList) {
                @SuppressWarnings("unchecked") FrozenList<Number> castArg = (FrozenList<Number>) arg;
                return getNewInstance(castArg, pathToItem, pathToSchemas);
            }
            throw new InvalidTypeException("Invalid input type="+arg.getClass()+". It can't be instantiated by this schema");
        }
    }    
    
    public static class ItemsList1 extends FrozenList<ItemsList> {
        ItemsList1(FrozenList<ItemsList> m) {
            super(m);
        }
        public static ItemsList1 of(List<List<Number>> arg, SchemaConfiguration configuration) throws ValidationException {
            return Items1.getInstance().validate(arg, configuration);
        }
    }
    
    public static class ItemsListInput1 {
        // class to build List<List<Number>>
    }
    
    
    public static class Items1 extends JsonSchema implements ListSchemaValidator<List<Number>, FrozenList<Number>, ItemsList1> {
        private static Items1 instance;
    
        protected Items1() {
            super(new JsonSchemaInfo()
                .type(Set.of(FrozenList.class))
                .items(Items2.class)
            );
        }
    
        public static Items1 getInstance() {
            if (instance == null) {
                instance = new Items1();
            }
            return instance;
        }
        
        @Override
        public FrozenList<FrozenList<Number>> castToAllowedTypes(List<List<Number>> arg, List<Object> pathToItem, Set<List<Object>> pathSet) {
            pathSet.add(pathToItem);
            List<FrozenList<Number>> argFixed = new ArrayList<>();
            int i =0;
            for (List<Number> item: arg) {
                List<Object> newPathToItem = new ArrayList<>(pathToItem);
                newPathToItem.add(i);
                                FrozenList<Number> fixedVal = (FrozenList<Number>) castToAllowedObjectTypes(item, newPathToItem, pathSet);
                argFixed.add(fixedVal);
                i += 1;
            }
            return new FrozenList<>(argFixed);
        }
        
        @Override
        public ItemsList1 getNewInstance(FrozenList<FrozenList<Number>> arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) {
            ArrayList<ItemsList> items = new ArrayList<>();
            int i = 0;
            for (FrozenList<Number> item: arg) {
                List<Object> itemPathToItem = new ArrayList<>(pathToItem);
                itemPathToItem.add(i);
                JsonSchema itemSchema = pathToSchemas.get(itemPathToItem).entrySet().iterator().next().getKey();
                                ItemsList castItem = (ItemsList) itemSchema.getNewInstance(item, itemPathToItem, pathToSchemas);
                items.add(castItem);
                i += 1;
            }
            FrozenList<ItemsList> newInstanceItems = new FrozenList<>(items);
            return new ItemsList1(newInstanceItems);
        }
        
        @Override
        public ItemsList1 validate(List<List<Number>> arg, SchemaConfiguration configuration) throws ValidationException {
            Set<List<Object>> pathSet = new HashSet<>();
            List<Object> pathToItem = List.of("args[0");
            FrozenList<FrozenList<Number>> castArg = castToAllowedTypes(arg, pathToItem, pathSet);
            SchemaConfiguration usedConfiguration = Objects.requireNonNullElseGet(configuration, () -> new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone()));
            ValidationMetadata validationMetadata = new ValidationMetadata(pathToItem, usedConfiguration, new PathToSchemasMap(), new LinkedHashSet<>());
            PathToSchemasMap pathToSchemasMap = getPathToSchemas(this, castArg, validationMetadata, pathSet);
            return getNewInstance(castArg, validationMetadata.pathToItem(), pathToSchemasMap);
        }
        
        @Override
        public Object getNewInstance(Object arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) {
            if (arg instanceof FrozenList) {
                @SuppressWarnings("unchecked") FrozenList<FrozenList<Number>> castArg = (FrozenList<FrozenList<Number>>) arg;
                return getNewInstance(castArg, pathToItem, pathToSchemas);
            }
            throw new InvalidTypeException("Invalid input type="+arg.getClass()+". It can't be instantiated by this schema");
        }
    }    
    
    public static class ItemsList2 extends FrozenList<ItemsList1> {
        ItemsList2(FrozenList<ItemsList1> m) {
            super(m);
        }
        public static ItemsList2 of(List<List<List<Number>>> arg, SchemaConfiguration configuration) throws ValidationException {
            return Items.getInstance().validate(arg, configuration);
        }
    }
    
    public static class ItemsListInput2 {
        // class to build List<List<List<Number>>>
    }
    
    
    public static class Items extends JsonSchema implements ListSchemaValidator<List<List<Number>>, FrozenList<FrozenList<Number>>, ItemsList2> {
        private static Items instance;
    
        protected Items() {
            super(new JsonSchemaInfo()
                .type(Set.of(FrozenList.class))
                .items(Items1.class)
            );
        }
    
        public static Items getInstance() {
            if (instance == null) {
                instance = new Items();
            }
            return instance;
        }
        
        @Override
        public FrozenList<FrozenList<FrozenList<Number>>> castToAllowedTypes(List<List<List<Number>>> arg, List<Object> pathToItem, Set<List<Object>> pathSet) {
            pathSet.add(pathToItem);
            List<FrozenList<FrozenList<Number>>> argFixed = new ArrayList<>();
            int i =0;
            for (List<List<Number>> item: arg) {
                List<Object> newPathToItem = new ArrayList<>(pathToItem);
                newPathToItem.add(i);
                                FrozenList<FrozenList<Number>> fixedVal = (FrozenList<FrozenList<Number>>) castToAllowedObjectTypes(item, newPathToItem, pathSet);
                argFixed.add(fixedVal);
                i += 1;
            }
            return new FrozenList<>(argFixed);
        }
        
        @Override
        public ItemsList2 getNewInstance(FrozenList<FrozenList<FrozenList<Number>>> arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) {
            ArrayList<ItemsList1> items = new ArrayList<>();
            int i = 0;
            for (FrozenList<FrozenList<Number>> item: arg) {
                List<Object> itemPathToItem = new ArrayList<>(pathToItem);
                itemPathToItem.add(i);
                JsonSchema itemSchema = pathToSchemas.get(itemPathToItem).entrySet().iterator().next().getKey();
                                ItemsList1 castItem = (ItemsList1) itemSchema.getNewInstance(item, itemPathToItem, pathToSchemas);
                items.add(castItem);
                i += 1;
            }
            FrozenList<ItemsList1> newInstanceItems = new FrozenList<>(items);
            return new ItemsList2(newInstanceItems);
        }
        
        @Override
        public ItemsList2 validate(List<List<List<Number>>> arg, SchemaConfiguration configuration) throws ValidationException {
            Set<List<Object>> pathSet = new HashSet<>();
            List<Object> pathToItem = List.of("args[0");
            FrozenList<FrozenList<FrozenList<Number>>> castArg = castToAllowedTypes(arg, pathToItem, pathSet);
            SchemaConfiguration usedConfiguration = Objects.requireNonNullElseGet(configuration, () -> new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone()));
            ValidationMetadata validationMetadata = new ValidationMetadata(pathToItem, usedConfiguration, new PathToSchemasMap(), new LinkedHashSet<>());
            PathToSchemasMap pathToSchemasMap = getPathToSchemas(this, castArg, validationMetadata, pathSet);
            return getNewInstance(castArg, validationMetadata.pathToItem(), pathToSchemasMap);
        }
        
        @Override
        public Object getNewInstance(Object arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) {
            if (arg instanceof FrozenList) {
                @SuppressWarnings("unchecked") FrozenList<FrozenList<FrozenList<Number>>> castArg = (FrozenList<FrozenList<FrozenList<Number>>>) arg;
                return getNewInstance(castArg, pathToItem, pathToSchemas);
            }
            throw new InvalidTypeException("Invalid input type="+arg.getClass()+". It can't be instantiated by this schema");
        }
    }    
    
    public static class NestedItemsList extends FrozenList<ItemsList2> {
        NestedItemsList(FrozenList<ItemsList2> m) {
            super(m);
        }
        public static NestedItemsList of(List<List<List<List<Number>>>> arg, SchemaConfiguration configuration) throws ValidationException {
            return NestedItems1.getInstance().validate(arg, configuration);
        }
    }
    
    public static class NestedItemsListInput {
        // class to build List<List<List<List<Number>>>>
    }
    
    
    public static class NestedItems1 extends JsonSchema implements ListSchemaValidator<List<List<List<Number>>>, FrozenList<FrozenList<FrozenList<Number>>>, NestedItemsList> {
        /*
        NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
        Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
    
        Do not edit the class manually.
        */
        private static NestedItems1 instance;
    
        protected NestedItems1() {
            super(new JsonSchemaInfo()
                .type(Set.of(FrozenList.class))
                .items(Items.class)
            );
        }
    
        public static NestedItems1 getInstance() {
            if (instance == null) {
                instance = new NestedItems1();
            }
            return instance;
        }
        
        @Override
        public FrozenList<FrozenList<FrozenList<FrozenList<Number>>>> castToAllowedTypes(List<List<List<List<Number>>>> arg, List<Object> pathToItem, Set<List<Object>> pathSet) {
            pathSet.add(pathToItem);
            List<FrozenList<FrozenList<FrozenList<Number>>>> argFixed = new ArrayList<>();
            int i =0;
            for (List<List<List<Number>>> item: arg) {
                List<Object> newPathToItem = new ArrayList<>(pathToItem);
                newPathToItem.add(i);
                                FrozenList<FrozenList<FrozenList<Number>>> fixedVal = (FrozenList<FrozenList<FrozenList<Number>>>) castToAllowedObjectTypes(item, newPathToItem, pathSet);
                argFixed.add(fixedVal);
                i += 1;
            }
            return new FrozenList<>(argFixed);
        }
        
        @Override
        public NestedItemsList getNewInstance(FrozenList<FrozenList<FrozenList<FrozenList<Number>>>> arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) {
            ArrayList<ItemsList2> items = new ArrayList<>();
            int i = 0;
            for (FrozenList<FrozenList<FrozenList<Number>>> item: arg) {
                List<Object> itemPathToItem = new ArrayList<>(pathToItem);
                itemPathToItem.add(i);
                JsonSchema itemSchema = pathToSchemas.get(itemPathToItem).entrySet().iterator().next().getKey();
                                ItemsList2 castItem = (ItemsList2) itemSchema.getNewInstance(item, itemPathToItem, pathToSchemas);
                items.add(castItem);
                i += 1;
            }
            FrozenList<ItemsList2> newInstanceItems = new FrozenList<>(items);
            return new NestedItemsList(newInstanceItems);
        }
        
        @Override
        public NestedItemsList validate(List<List<List<List<Number>>>> arg, SchemaConfiguration configuration) throws ValidationException {
            Set<List<Object>> pathSet = new HashSet<>();
            List<Object> pathToItem = List.of("args[0");
            FrozenList<FrozenList<FrozenList<FrozenList<Number>>>> castArg = castToAllowedTypes(arg, pathToItem, pathSet);
            SchemaConfiguration usedConfiguration = Objects.requireNonNullElseGet(configuration, () -> new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone()));
            ValidationMetadata validationMetadata = new ValidationMetadata(pathToItem, usedConfiguration, new PathToSchemasMap(), new LinkedHashSet<>());
            PathToSchemasMap pathToSchemasMap = getPathToSchemas(this, castArg, validationMetadata, pathSet);
            return getNewInstance(castArg, validationMetadata.pathToItem(), pathToSchemasMap);
        }
        
        @Override
        public Object getNewInstance(Object arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) {
            if (arg instanceof FrozenList) {
                @SuppressWarnings("unchecked") FrozenList<FrozenList<FrozenList<FrozenList<Number>>>> castArg = (FrozenList<FrozenList<FrozenList<FrozenList<Number>>>>) arg;
                return getNewInstance(castArg, pathToItem, pathToSchemas);
            }
            throw new InvalidTypeException("Invalid input type="+arg.getClass()+". It can't be instantiated by this schema");
        }
    }
}
