package org.openapijsonschematools.client.schemas;

import org.openapijsonschematools.client.configurations.JsonSchemaKeywordFlags;
import org.openapijsonschematools.client.exceptions.InvalidTypeException;
import org.openapijsonschematools.client.schemas.validation.JsonSchema;
import org.openapijsonschematools.client.configurations.SchemaConfiguration;
import org.openapijsonschematools.client.schemas.validation.KeywordEntry;
import org.openapijsonschematools.client.schemas.validation.PathToSchemasMap;
import org.openapijsonschematools.client.schemas.validation.SchemaNumberValidator;
import org.openapijsonschematools.client.schemas.validation.TypeValidator;
import org.openapijsonschematools.client.exceptions.ValidationException;
import org.openapijsonschematools.client.schemas.validation.ValidationMetadata;

import java.util.HashSet;
import java.util.LinkedHashMap;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Objects;
import java.util.Set;
import java.util.Map;

public class NumberJsonSchema extends JsonSchema implements SchemaNumberValidator {
    public NumberJsonSchema() {
        super(new LinkedHashMap<>(Map.ofEntries(
                new KeywordEntry("type", new TypeValidator(Set.of(
                        Integer.class,
                        Long.class,
                        Float.class,
                        Double.class
                )))
        )));
    }

    public int validate(int arg, SchemaConfiguration configuration) {
        return (int) validate((Number) arg, configuration);
    }

    public long validate(long arg, SchemaConfiguration configuration) {
        return (long) validate((Number) arg, configuration);
    }

    public float validate(float arg, SchemaConfiguration configuration) {
        return (float) validate((Number) arg, configuration);
    }

    public double validate(double arg, SchemaConfiguration configuration) {
        return (double) validate((Number) arg, configuration);
    }

    @Override
    public Number castToAllowedTypes(Number arg, List<Object> pathToItem, Set<List<Object>> pathSet) {
        return castToAllowedNumberTypes(arg, pathToItem, pathSet);
    }

    @Override
    public Number getNewInstance(Number arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) {
        return arg;
    }

    @Override
    public Number validate(Number arg, SchemaConfiguration configuration) throws ValidationException, InvalidTypeException {
        Set<List<Object>> pathSet = new HashSet<>();
        List<Object> pathToItem = List.of("args[0");
        Number castArg = castToAllowedTypes(arg, pathToItem, pathSet);
        SchemaConfiguration usedConfiguration = Objects.requireNonNullElseGet(configuration, () -> new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone()));
        ValidationMetadata validationMetadata = new ValidationMetadata(pathToItem, usedConfiguration, new PathToSchemasMap(), new LinkedHashSet<>());
        PathToSchemasMap pathToSchemasMap = getPathToSchemas(this, castArg, validationMetadata, pathSet);
        return getNewInstance(castArg, validationMetadata.pathToItem(), pathToSchemasMap);
    }
}