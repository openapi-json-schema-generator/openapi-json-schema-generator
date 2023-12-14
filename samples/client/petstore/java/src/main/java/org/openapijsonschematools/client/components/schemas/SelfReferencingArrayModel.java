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
import org.openapijsonschematools.client.schemas.validation.FrozenList;
import org.openapijsonschematools.client.schemas.validation.ItemsValidator;
import org.openapijsonschematools.client.schemas.validation.JsonSchema;
import org.openapijsonschematools.client.schemas.validation.KeywordEntry;
import org.openapijsonschematools.client.schemas.validation.PathToSchemasMap;
import org.openapijsonschematools.client.schemas.validation.SchemaListValidator;
import org.openapijsonschematools.client.schemas.validation.TypeValidator;
import org.openapijsonschematools.client.schemas.validation.ValidationMetadata;

public class SelfReferencingArrayModel {
    // nest classes so all schemas and input/output classes can be public
    
    
    public static class SelfReferencingArrayModelList extends FrozenList<SelfReferencingArrayModelList> {
        SelfReferencingArrayModelList(FrozenList<SelfReferencingArrayModelList> m) {
            super(m);
        }
        public static SelfReferencingArrayModelList of(List<List> arg, SchemaConfiguration configuration) throws ValidationException {
            return SelfReferencingArrayModel1.getInstance().validate(arg, configuration);
        }
    }
    
    public static class SelfReferencingArrayModelListInput {
        // class to build List<List>
    }
    
    
    public static class SelfReferencingArrayModel1 extends JsonSchema implements SchemaListValidator<List, FrozenList, SelfReferencingArrayModelList> {
        /*
        NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
        Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
    
        Do not edit the class manually.
        */
        private static SelfReferencingArrayModel1 instance;
        protected SelfReferencingArrayModel1() {
            super(new LinkedHashMap<>(Map.ofEntries(
                new KeywordEntry("type", new TypeValidator(Set.of(FrozenList.class))),
                new KeywordEntry("items", new ItemsValidator(SelfReferencingArrayModel1.class))
            )));
        }
    
        public static SelfReferencingArrayModel1 getInstance() {
            if (instance == null) {
                instance = new SelfReferencingArrayModel1();
            }
            return instance;
        }
    
        @Override
        public FrozenList<FrozenList> castToAllowedTypes(List<List> arg, List<Object> pathToItem, Set<List<Object>> pathSet) {
            pathSet.add(pathToItem);
            List<FrozenList> argFixed = new ArrayList<>();
            int i =0;
            for (List item: arg) {
                List<Object> newPathToItem = new ArrayList<>(pathToItem);
                newPathToItem.add(i);
                                FrozenList fixedVal = (FrozenList) castToAllowedObjectTypes(item, newPathToItem, pathSet);
                argFixed.add(fixedVal);
                i += 1;
            }
            return new FrozenList<>(argFixed);
        }
    
        @Override
        public SelfReferencingArrayModelList getNewInstance(FrozenList<FrozenList> arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) {
            ArrayList<SelfReferencingArrayModelList> items = new ArrayList<>();
            int i = 0;
            for (FrozenList item: arg) {
                List<Object> itemPathToItem = new ArrayList<>(pathToItem);
                itemPathToItem.add(i);
                JsonSchema itemSchema = pathToSchemas.get(itemPathToItem).entrySet().iterator().next().getKey();
                SelfReferencingArrayModelList castItem = (SelfReferencingArrayModelList) itemSchema.getNewInstance(item, itemPathToItem, pathToSchemas);
                items.add(castItem);
                i += 1;
            }
            FrozenList<SelfReferencingArrayModelList> newInstanceItems = new FrozenList<>(items);
            return new SelfReferencingArrayModelList(newInstanceItems);
        }
    
        @Override
        public Object getNewInstance(Object arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) {
            if (arg instanceof FrozenList) {
                @SuppressWarnings("unchecked") FrozenList<FrozenList> castArg = (FrozenList<FrozenList>) arg;
                return getNewInstance(castArg, pathToItem, pathToSchemas);
            }
            throw new InvalidTypeException("Invalid input type="+arg.getClass()+". It can't be instantiated by this schema");
        }
    
        @Override
        public SelfReferencingArrayModelList validate(List<List> arg, SchemaConfiguration configuration) throws ValidationException {
            Set<List<Object>> pathSet = new HashSet<>();
            List<Object> pathToItem = List.of("args[0");
            FrozenList<FrozenList> castArg = castToAllowedTypes(arg, pathToItem, pathSet);
            SchemaConfiguration usedConfiguration = Objects.requireNonNullElseGet(configuration, () -> new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone()));
            ValidationMetadata validationMetadata = new ValidationMetadata(pathToItem, usedConfiguration, new PathToSchemasMap(), new LinkedHashSet<>());
            PathToSchemasMap pathToSchemasMap = getPathToSchemas(this, castArg, validationMetadata, pathSet);
            return getNewInstance(castArg, validationMetadata.pathToItem(), pathToSchemasMap);
        }
    }
}
