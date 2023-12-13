package org.openapijsonschematools.client.schemas.validation;

import org.openapijsonschematools.client.configurations.SchemaConfiguration;
import org.openapijsonschematools.client.exceptions.InvalidTypeException;
import org.openapijsonschematools.client.exceptions.ValidationException;

import java.util.List;
import java.util.Set;

public interface SchemaNumberValidator {
    Number castToAllowedTypes(Number arg, List<Object> pathToItem, Set<List<Object>> pathSet);
    Number getNewInstance(Number arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas);
    Number validate(Number arg, SchemaConfiguration configuration) throws ValidationException, InvalidTypeException;
}