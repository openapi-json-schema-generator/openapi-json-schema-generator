package org.openapijsonschematools.schemas.validation;

import org.openapijsonschematools.schemas.JsonSchema;

import java.lang.reflect.Field;
import java.util.AbstractMap;
import java.util.HashMap;
import java.util.LinkedHashSet;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

public abstract class SchemaValidator {
    static HashMap<String, KeywordValidator> keywordToValidator = new HashMap<>(Map.ofEntries(
        new AbstractMap.SimpleEntry<String, KeywordValidator>("allOf", new FakeValidator()),
        new AbstractMap.SimpleEntry<String, KeywordValidator>("anyOf", new FakeValidator()),
        new AbstractMap.SimpleEntry<String, KeywordValidator>("const", new FakeValidator()),
        new AbstractMap.SimpleEntry<String, KeywordValidator>("contains", new FakeValidator()),
        new AbstractMap.SimpleEntry<String, KeywordValidator>("default", new FakeValidator()),
        new AbstractMap.SimpleEntry<String, KeywordValidator>("dependentRequired", new FakeValidator()),
        new AbstractMap.SimpleEntry<String, KeywordValidator>("dependentSchemas", new FakeValidator()),
        new AbstractMap.SimpleEntry<String, KeywordValidator>("discriminator", new FakeValidator()),
        new AbstractMap.SimpleEntry<String, KeywordValidator>("enumInfo", new FakeValidator()),
        new AbstractMap.SimpleEntry<String, KeywordValidator>("exclusiveMaximum", new FakeValidator()),
        new AbstractMap.SimpleEntry<String, KeywordValidator>("exclusiveMinimum", new FakeValidator()),
        new AbstractMap.SimpleEntry<String, KeywordValidator>("format", new FormatValidator()),
        new AbstractMap.SimpleEntry<String, KeywordValidator>("if_", new FakeValidator()),
        new AbstractMap.SimpleEntry<String, KeywordValidator>("then", new FakeValidator()),
        new AbstractMap.SimpleEntry<String, KeywordValidator>("else_", new FakeValidator()),
        new AbstractMap.SimpleEntry<String, KeywordValidator>("maxContains", new FakeValidator()),
        new AbstractMap.SimpleEntry<String, KeywordValidator>("maxItems", new FakeValidator()),
        new AbstractMap.SimpleEntry<String, KeywordValidator>("maxLength", new FakeValidator()),
        new AbstractMap.SimpleEntry<String, KeywordValidator>("maxProperties", new FakeValidator()),
        new AbstractMap.SimpleEntry<String, KeywordValidator>("maximum", new FakeValidator()),
        new AbstractMap.SimpleEntry<String, KeywordValidator>("minContains", new FakeValidator()),
        new AbstractMap.SimpleEntry<String, KeywordValidator>("minItems", new FakeValidator()),
        new AbstractMap.SimpleEntry<String, KeywordValidator>("minLength", new FakeValidator()),
        new AbstractMap.SimpleEntry<String, KeywordValidator>("minProperties", new FakeValidator()),
        new AbstractMap.SimpleEntry<String, KeywordValidator>("minimum", new FakeValidator()),
        new AbstractMap.SimpleEntry<String, KeywordValidator>("multipleOf", new FakeValidator()),
        new AbstractMap.SimpleEntry<String, KeywordValidator>("not", new FakeValidator()),
        new AbstractMap.SimpleEntry<String, KeywordValidator>("oneOf", new FakeValidator()),
        new AbstractMap.SimpleEntry<String, KeywordValidator>("pattern", new FakeValidator()),
        new AbstractMap.SimpleEntry<String, KeywordValidator>("patternProperties", new FakeValidator()),
        new AbstractMap.SimpleEntry<String, KeywordValidator>("prefixItems", new FakeValidator()),
        new AbstractMap.SimpleEntry<String, KeywordValidator>("required", new RequiredValidator()),
        new AbstractMap.SimpleEntry<String, KeywordValidator>("type", new TypeValidator()),
        new AbstractMap.SimpleEntry<String, KeywordValidator>("uniqueItems", new FakeValidator()),
        new AbstractMap.SimpleEntry<String, KeywordValidator>("items", new ItemsValidator()),
        new AbstractMap.SimpleEntry<String, KeywordValidator>("unevaluatedItems", new FakeValidator()),
        new AbstractMap.SimpleEntry<String, KeywordValidator>("properties", new PropertiesValidator()),
        new AbstractMap.SimpleEntry<String, KeywordValidator>("propertyNames", new FakeValidator()),
        new AbstractMap.SimpleEntry<String, KeywordValidator>("additionalProperties", new AdditionalPropertiesValidator()),
        new AbstractMap.SimpleEntry<String, KeywordValidator>("unevaluatedProperties", new FakeValidator())
    ));

    protected static PathToSchemasMap validate(
            Class<? extends SchemaValidator> schemaCls,
            Object arg,
            ValidationMetadata validationMetadata
    ) {
        HashMap<String, Object> fieldsToValues = new HashMap<>();
        LinkedHashSet<String> disabledKeywords = validationMetadata.configuration().disabledKeywordFlags().getKeywords();
        Class<? extends SchemaValidator> usedSchemaCls = schemaCls;
        Class<?> superclass = schemaCls.getSuperclass();
        if (superclass != JsonSchema.class) {
            // only ref with no adjacent properties supported at this time
            usedSchemaCls = (Class<? extends SchemaValidator>) superclass;
        }
        Field[] fields = usedSchemaCls.getDeclaredFields();
        for (Field field : fields) {
            String fieldName = field.getName();
            if (fieldName.equals("keywordToValidator")) {
                continue;
            }
            if (fieldName.equals("this$0")) {
                continue;
            }
            if (disabledKeywords.contains(fieldName)) {
                continue;
            }
            try {
                Object value = field.get(null);
                fieldsToValues.put(fieldName, value);
            } catch (IllegalAccessException | IllegalArgumentException e) {
                throw new RuntimeException(e);
            }
        }
        Object extra = null;
        PathToSchemasMap pathToSchemas = new PathToSchemasMap();
        for (Map.Entry<String, Object> entry: fieldsToValues.entrySet()) {
            String jsonKeyword = entry.getKey();
            Object constraint = entry.getValue();
            if (jsonKeyword.equals("additionalProperties") && fieldsToValues.containsKey("properties")) {
                extra = fieldsToValues.get("properties");
            }
            KeywordValidator validatorClass = keywordToValidator.get(jsonKeyword);
            PathToSchemasMap otherPathToSchemas = validatorClass.validate(
                    schemaCls,
                    arg,
                    constraint,
                    validationMetadata,
                    extra
            );
            if (otherPathToSchemas == null) {
                continue;
            }
            pathToSchemas.update(otherPathToSchemas);
        }
        Class<?> baseClass;
        if (arg == null) {
            baseClass = Void.class;
        } else {
            baseClass = arg.getClass();
        }
        List<Object> pathToItem = validationMetadata.pathToItem();
        if (!pathToSchemas.containsKey(pathToItem)) {
            pathToSchemas.put(validationMetadata.pathToItem(), new LinkedHashMap<>());
        }
        pathToSchemas.get(pathToItem).put(baseClass, null);
        pathToSchemas.get(pathToItem).put(schemaCls, null);

        return pathToSchemas;
    }
}
