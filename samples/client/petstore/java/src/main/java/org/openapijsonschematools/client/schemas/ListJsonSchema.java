package org.openapijsonschematools.client.schemas;

import org.openapijsonschematools.client.configurations.JsonSchemaKeywordFlags;
import org.openapijsonschematools.client.exceptions.InvalidTypeException;
import org.openapijsonschematools.client.schemas.validation.FrozenList;
import org.openapijsonschematools.client.schemas.validation.JsonSchema;
import org.openapijsonschematools.client.schemas.validation.JsonSchemaInfo;
import org.openapijsonschematools.client.configurations.SchemaConfiguration;
import org.openapijsonschematools.client.schemas.validation.PathToSchemasMap;
import org.openapijsonschematools.client.schemas.validation.ListSchemaValidator;
import org.openapijsonschematools.client.exceptions.ValidationException;
import org.openapijsonschematools.client.schemas.validation.ValidationMetadata;
import org.checkerframework.checker.nullness.qual.Nullable;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.LinkedHashMap;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Objects;
import java.util.Set;

public class ListJsonSchema extends JsonSchema implements ListSchemaValidator<FrozenList<@Nullable Object>> {
    private static @Nullable ListJsonSchema instance = null;

    protected ListJsonSchema() {
        super(new JsonSchemaInfo()
            .type(Set.of(List.class))
        );
    }

    public static ListJsonSchema getInstance() {
        if (instance == null) {
            instance = new ListJsonSchema();
        }
        return instance;
    }

    @Override
    public FrozenList<@Nullable Object> getNewInstance(List<?> arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) {
        List<@Nullable Object> items = new ArrayList<>();
        int i = 0;
        for (Object item: arg) {
            List<Object> itemPathToItem = new ArrayList<>(pathToItem);
            itemPathToItem.add(i);
            LinkedHashMap<JsonSchema, Void> schemas = pathToSchemas.get(itemPathToItem);
            if (schemas == null) {
                throw new InvalidTypeException("Validation result is invalid, schemas must exist for a pathToItem");
            }
            JsonSchema itemSchema = schemas.entrySet().iterator().next().getKey();
            @Nullable Object castItem = itemSchema.getNewInstance(item, itemPathToItem, pathToSchemas);
            items.add(castItem);
            i += 1;
        }
        return new FrozenList<>(items);
    }

    public FrozenList<@Nullable Object> validate(List<?> arg, SchemaConfiguration configuration) throws ValidationException, InvalidTypeException {
        Set<List<Object>> pathSet = new HashSet<>();
        List<Object> pathToItem = new ArrayList<>();
        pathToItem.add("args[0]");
        List<?> castArg = castToAllowedTypes(arg, pathToItem, pathSet);
        SchemaConfiguration usedConfiguration = Objects.requireNonNullElseGet(configuration, () -> new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone()));
        PathToSchemasMap validatedPathToSchemas = new PathToSchemasMap();
        ValidationMetadata validationMetadata = new ValidationMetadata(pathToItem, usedConfiguration, validatedPathToSchemas, new LinkedHashSet<>());
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

    @Override
    public @Nullable Object validate(@Nullable Object arg, SchemaConfiguration configuration) throws InvalidTypeException, ValidationException {
        if (arg instanceof List) {
            return validate((List<?>) arg, configuration);
        }
        throw new InvalidTypeException("Invalid input type="+getClass(arg)+". It can't be instantiated by this schema");
    }
}
