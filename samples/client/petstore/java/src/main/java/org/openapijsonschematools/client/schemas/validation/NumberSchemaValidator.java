package org.openapijsonschematools.client.schemas.validation;

import org.openapijsonschematools.client.configurations.SchemaConfiguration;
import org.openapijsonschematools.client.exceptions.InvalidTypeException;
import org.openapijsonschematools.client.exceptions.ValidationException;

public interface NumberSchemaValidator<T> {
    Number validate(Number arg, SchemaConfiguration configuration) throws ValidationException, InvalidTypeException;
    T validateAndBox(Number arg, SchemaConfiguration configuration) throws ValidationException, InvalidTypeException;
}