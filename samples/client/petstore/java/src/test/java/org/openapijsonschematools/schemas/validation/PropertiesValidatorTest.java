package org.openapijsonschematools.schemas.validation;

import org.junit.Assert;
import org.junit.Test;
import org.openapijsonschematools.configurations.JsonSchemaKeywordFlags;
import org.openapijsonschematools.configurations.SchemaConfiguration;
import org.openapijsonschematools.schemas.StringJsonSchema;

import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Map;

public class PropertiesValidatorTest {

    @Test
    public void testCorrectPropertySucceeds() {
        Map<String, Class<?>> properties = new LinkedHashMap<>();
        properties.put("someString", StringJsonSchema.class);

        final PropertiesValidator validator = new PropertiesValidator();
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
        FrozenMap<String, Object> arg = new FrozenMap<>(mutableMap);
        PathToSchemasMap pathToSchemas = validator.validate(
                JsonSchema.class,
                arg,
                properties,
                validationMetadata,
                null
        );
        List<Object> expectedPathToItem = new ArrayList<>();
        expectedPathToItem.add("args[0]");
        expectedPathToItem.add("someString");
        LinkedHashMap<Class<? extends JsonSchema>, Void> expectedClasses = new LinkedHashMap<>();
        expectedClasses.put(StringJsonSchema.class, null);
        PathToSchemasMap expectedPathToSchemas = new PathToSchemasMap();
        expectedPathToSchemas.put(expectedPathToItem, expectedClasses);
        Assert.assertEquals(pathToSchemas, expectedPathToSchemas);
    }

    @Test
    public void testNotApplicableTypeReturnsNull() {
        Map<String, Class<?>> properties = new LinkedHashMap<>();
        properties.put("someString", StringJsonSchema.class);

        final PropertiesValidator validator = new PropertiesValidator();
        List<Object> pathToItem = new ArrayList<>();
        pathToItem.add("args[0]");
        ValidationMetadata validationMetadata = new ValidationMetadata(
                pathToItem,
                new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone()),
                new PathToSchemasMap(),
                new LinkedHashSet<>()
        );
        PathToSchemasMap pathToSchemas = validator.validate(
                JsonSchema.class,
                1,
                properties,
                validationMetadata,
                null
        );
        Assert.assertNull(pathToSchemas);
    }

    @Test
    public void testIncorrectPropertyValueFails() {
        Map<String, Class<?>> properties = new LinkedHashMap<>();
        properties.put("someString", StringJsonSchema.class);

        final PropertiesValidator validator = new PropertiesValidator();
        List<Object> pathToItem = new ArrayList<>();
        pathToItem.add("args[0]");
        ValidationMetadata validationMetadata = new ValidationMetadata(
                pathToItem,
                new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone()),
                new PathToSchemasMap(),
                new LinkedHashSet<>()
        );
        LinkedHashMap<String, Object> mutableMap = new LinkedHashMap<>();
        mutableMap.put("someString", 1);
        FrozenMap<String, Object> arg = new FrozenMap<>(mutableMap);
        Assert.assertThrows(RuntimeException.class, () -> validator.validate(
                JsonSchema.class,
                arg,
                properties,
                validationMetadata,
                null
        ));
    }
}
