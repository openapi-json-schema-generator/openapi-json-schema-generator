package org.openapijsonschematools.client.schemas;

import org.openapijsonschematools.client.configurations.JsonSchemaKeywordFlags;
import org.openapijsonschematools.client.exceptions.InvalidTypeException;
import org.openapijsonschematools.client.schemas.validation.FormatValidator;
import org.openapijsonschematools.client.schemas.validation.JsonSchema;
import org.openapijsonschematools.client.schemas.validation.JsonSchemaInfo;
import org.openapijsonschematools.client.configurations.SchemaConfiguration;
import org.openapijsonschematools.client.schemas.validation.KeywordEntry;
import org.openapijsonschematools.client.schemas.validation.PathToSchemasMap;
import org.openapijsonschematools.client.schemas.validation.NumberSchemaValidator;
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

public class Int32JsonSchema extends JsonSchema implements NumberSchemaValidator {
    private static Int32JsonSchema instance;

    protected Int32JsonSchema() {
        super(new JsonSchemaInfo()
            .type(Set.of(
                    Integer.class,
                    Float.class
            ))
            .format("int32")
        );
    }

    public static Int32JsonSchema getInstance() {
        if (instance == null) {
            instance = new Int32JsonSchema();
        }
        return instance;
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

    public int validate(int arg, SchemaConfiguration configuration) {
        return (int) validate((Number) arg, configuration);
    }

    public float validate(float arg, SchemaConfiguration configuration) throws ValidationException {
        return (float) validate((Number) arg, configuration);
    }

    @Override
    public Object getNewInstance(Object arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) {
        if (arg instanceof Number) {
            return getNewInstance((Number) arg, pathToItem, pathToSchemas);
        }
        throw new InvalidTypeException("Invalid input type="+arg.getClass()+". It can't be instantiated by this schema");
    }
}