package org.openapijsonschematools.schemas.validators;

import org.openapijsonschematools.schemas.PathToSchemasMap;
import org.openapijsonschematools.schemas.SchemaValidator;
import org.openapijsonschematools.schemas.ValidationMetadata;

import java.util.HashSet;

public class TypeValidator implements KeywordValidator {
    @Override
    public PathToSchemasMap validate(Class<SchemaValidator> cls, Object arg, Object constraint, ValidationMetadata validationMetadata, Object extra) {
        HashSet<Class<?>> types = (HashSet<Class<?>>) constraint;
        Class<?> argClass;
        if (arg == null) {
            argClass = Void.class;
        } else {
            argClass = arg.getClass();
        }
        if (!types.contains(argClass)) {
            throw new RuntimeException("invalid type");
        }
        return null;
    }
}
