package org.openapijsonschematools.client.schemas.validation;

import org.checkerframework.checker.nullness.qual.Nullable;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;

public class DependentRequiredValidator implements KeywordValidator {
    public final Map<String, Set<String>> dependentRequired;

    public DependentRequiredValidator(Map<String, Set<String>> dependentRequired) {
        this.dependentRequired = dependentRequired;
    }

    @Override
    public @Nullable PathToSchemasMap validate(
        JsonSchema schema,
        @Nullable Object arg,
        ValidationMetadata validationMetadata,
        @Nullable List<PathToSchemasMap> containsPathToSchemas
    ) {
        if (!(arg instanceof Map)) {
            return null;
        }
        // todo implement this
        return null;
    }
}
