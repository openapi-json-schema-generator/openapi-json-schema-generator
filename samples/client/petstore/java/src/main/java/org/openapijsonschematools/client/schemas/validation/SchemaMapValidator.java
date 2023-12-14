package org.openapijsonschematools.client.schemas.validation;

import org.openapijsonschematools.client.configurations.SchemaConfiguration;
import org.openapijsonschematools.client.exceptions.InvalidTypeException;
import org.openapijsonschematools.client.exceptions.ValidationException;

import java.util.List;
import java.util.Map;
import java.util.Set;

public interface SchemaMapValidator <InType, CastType, OutType> {
    FrozenMap<CastType> castToAllowedTypes(Map<String, InType> arg, List<Object> pathToItem, Set<List<Object>> pathSet);
    OutType getNewInstance(FrozenMap<CastType> arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas);
    OutType validate(Map<String, InType> arg, SchemaConfiguration configuration) throws ValidationException, InvalidTypeException;
}