package org.openapijsonschematools.client.schemas.validation;

import org.junit.Assert;
import org.junit.Test;
import org.openapijsonschematools.client.configurations.JsonSchemaKeywordFlags;
import org.openapijsonschematools.client.configurations.SchemaConfiguration;
import org.openapijsonschematools.client.exceptions.InvalidTypeException;
import org.openapijsonschematools.client.schemas.MapJsonSchema;
import org.openapijsonschematools.client.schemas.StringJsonSchema;
import org.openapijsonschematools.client.exceptions.ValidationException;

import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

public class AdditionalPropertiesValidatorTest {

    public static class ObjectWithPropsSchema extends JsonSchema {
        private static ObjectWithPropsSchema instance;
        private ObjectWithPropsSchema() {
            super(new JsonSchemaInfo()
                .type(Set.of(FrozenMap.class))
                .properties(Map.ofEntries(
                    new PropertyEntry("someString", StringJsonSchema.class)
                ))
            );

        }

        public static ObjectWithPropsSchema getInstance() {
            if (instance == null) {
                instance = new ObjectWithPropsSchema();
            }
            return instance;
        }

        @Override
        public Object getNewInstance(Object arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) {
            if (arg instanceof FrozenMap) {
                @SuppressWarnings("unchecked") FrozenMap<Object> castArg = (FrozenMap<Object>) arg;
                return castArg;
            }
            throw new InvalidTypeException("Invalid input type="+arg.getClass()+". It can't be instantiated by this schema");
        }
    }

    @Test
    public void testCorrectPropertySucceeds() {
        List<Object> pathToItem = new ArrayList<>();
        pathToItem.add("args[0]");
        ValidationMetadata validationMetadata = new ValidationMetadata(
                pathToItem,
                new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone()),
                new PathToSchemasMap(),
                new LinkedHashSet<>()
        );
        LinkedHashMap<String, Object> mutableMap = new LinkedHashMap<>();
        mutableMap.put("someString", "abc");
        mutableMap.put("someAddProp", "def");
        FrozenMap<Object> arg = new FrozenMap<>(mutableMap);
        final AdditionalPropertiesValidator validator = new AdditionalPropertiesValidator(StringJsonSchema.class);
        PathToSchemasMap pathToSchemas = validator.validate(
                ObjectWithPropsSchema.getInstance(),
                arg,
                validationMetadata
        );
        List<Object> expectedPathToItem = new ArrayList<>();
        expectedPathToItem.add("args[0]");
        expectedPathToItem.add("someAddProp");
        LinkedHashMap<JsonSchema, Void> expectedClasses = new LinkedHashMap<>();
        StringJsonSchema schema = JsonSchemaFactory.getInstance(StringJsonSchema.class);
        expectedClasses.put(schema, null);
        PathToSchemasMap expectedPathToSchemas = new PathToSchemasMap();
        expectedPathToSchemas.put(expectedPathToItem, expectedClasses);
        Assert.assertEquals(pathToSchemas, expectedPathToSchemas);
    }

    @Test
    public void testNotApplicableTypeReturnsNull() {
        List<Object> pathToItem = new ArrayList<>();
        pathToItem.add("args[0]");
        ValidationMetadata validationMetadata = new ValidationMetadata(
                pathToItem,
                new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone()),
                new PathToSchemasMap(),
                new LinkedHashSet<>()
        );
        final AdditionalPropertiesValidator validator = new AdditionalPropertiesValidator(StringJsonSchema.class);
        PathToSchemasMap pathToSchemas = validator.validate(
                MapJsonSchema.getInstance(),
                1,
                validationMetadata
        );
        Assert.assertNull(pathToSchemas);
    }

    @Test
    public void testIncorrectPropertyValueFails() {
        List<Object> pathToItem = new ArrayList<>();
        pathToItem.add("args[0]");
        ValidationMetadata validationMetadata = new ValidationMetadata(
                pathToItem,
                new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone()),
                new PathToSchemasMap(),
                new LinkedHashSet<>()
        );
        LinkedHashMap<String, Object> mutableMap = new LinkedHashMap<>();
        mutableMap.put("someString", "abc");
        mutableMap.put("someAddProp", 1);
        FrozenMap<Object> arg = new FrozenMap<>(mutableMap);
        final AdditionalPropertiesValidator validator = new AdditionalPropertiesValidator(StringJsonSchema.class);
        Assert.assertThrows(ValidationException.class, () -> validator.validate(
                ObjectWithPropsSchema.getInstance(),
                arg,
                validationMetadata
        ));
    }
}