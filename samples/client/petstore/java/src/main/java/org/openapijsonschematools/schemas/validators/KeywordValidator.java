package org.openapijsonschematools.schemas.validators;

import org.openapijsonschematools.schemas.PathToSchemasMap;
import org.openapijsonschematools.schemas.SchemaValidator;
import org.openapijsonschematools.schemas.ValidationMetadata;

public interface KeywordValidator {
    PathToSchemasMap validate(
            Object arg,
            Object value,
            Object extra,
            Class<SchemaValidator> cls,
            ValidationMetadata validationMetadata);
}
