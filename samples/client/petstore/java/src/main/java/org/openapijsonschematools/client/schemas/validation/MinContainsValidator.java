package org.openapijsonschematools.client.schemas.validation;

import org.checkerframework.checker.nullness.qual.Nullable;
import org.openapijsonschematools.client.exceptions.ValidationException;

import java.util.List;

public class MinContainsValidator implements KeywordValidator {
    public final int minContains;

    public MinContainsValidator(int minContains) {
        this.minContains = minContains;
    }

    @Override
    public @Nullable PathToSchemasMap validate(
        JsonSchema schema,
        @Nullable Object arg,
        ValidationMetadata validationMetadata,
        @Nullable List<PathToSchemasMap> containsPathToSchemas
    ) {
        if (!(arg instanceof List)) {
            return null;
        }
        if (containsPathToSchemas == null) {
            return null;
        }
        if (containsPathToSchemas.size() < minContains) {
            throw new ValidationException(
                "Validation failed for minContains keyword in class="+schema.getClass()+
                " at pathToItem="+validationMetadata.pathToItem()+". Too few items validated to the contains schema."
            );
        }
        return null;
    }
}