package org.openapijsonschematools.client.schemas.validation;

import org.openapijsonschematools.client.exceptions.ValidationException;

public interface KeywordValidator {
    PathToSchemasMap validate(
            JsonSchema schema,
            Object arg,
            ValidationMetadata validationMetadata) throws ValidationException;

    Object getConstraint();
}