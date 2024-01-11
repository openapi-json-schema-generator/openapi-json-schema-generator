package org.openapijsonschematools.client.schemas.validation;

import org.openapijsonschematools.client.exceptions.ValidationException;
import org.checkerframework.checker.nullness.qual.Nullable;

import java.util.List;
import java.util.Map;

public class MaxPropertiesValidator implements KeywordValidator {
    public final int maxProperties;

    public MaxPropertiesValidator(int maxProperties) {
        this.maxProperties = maxProperties;
    }

    @Override
    public @Nullable PathToSchemasMap validate(
        JsonSchema schema,
        @Nullable Object arg,
        ValidationMetadata validationMetadata,
        List<PathToSchemasMap> containsPathToSchemas
    ) {
        if (!(arg instanceof Map)) {
            return null;
        }
        if (((Map) arg).size() > maxProperties) {
            throw new ValidationException("Value " + arg + " is invalid because has > the maxProperties of " + maxProperties);
        }
        return null;
    }
}
