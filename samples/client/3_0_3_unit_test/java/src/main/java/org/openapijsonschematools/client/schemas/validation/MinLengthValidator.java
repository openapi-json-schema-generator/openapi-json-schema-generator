package org.openapijsonschematools.client.schemas.validation;

import org.openapijsonschematools.client.exceptions.ValidationException;
import org.checkerframework.checker.nullness.qual.Nullable;

import java.util.List;

public class MinLengthValidator extends LengthValidator implements KeywordValidator {
    public final int minLength;

    public MinLengthValidator(int minLength) {
        this.minLength = minLength;
    }

    @Override
    public @Nullable PathToSchemasMap validate(
        JsonSchema schema,
        @Nullable Object arg,
        ValidationMetadata validationMetadata,
        List<PathToSchemasMap> containsPathToSchemas
    ) {
        if (!(arg instanceof String)) {
            return null;
        }
        int length = getLength((String) arg);
        if (length < minLength) {
            throw new ValidationException("Value " + arg + " is invalid because has < the minLength of " + minLength);
        }
        return null;
    }
}
