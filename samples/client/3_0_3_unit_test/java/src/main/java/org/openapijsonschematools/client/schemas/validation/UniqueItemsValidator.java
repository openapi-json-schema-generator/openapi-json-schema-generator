package org.openapijsonschematools.client.schemas.validation;

import org.openapijsonschematools.client.exceptions.ValidationException;
import org.checkerframework.checker.nullness.qual.Nullable;

import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class UniqueItemsValidator implements KeywordValidator {
    public final boolean uniqueItems;

    public UniqueItemsValidator(boolean uniqueItems) {
        this.uniqueItems = uniqueItems;
    }

    @Override
    public @Nullable PathToSchemasMap validate(
        JsonSchema schema,
        @Nullable Object arg,
        ValidationMetadata validationMetadata,
        List<PathToSchemasMap> containsPathToSchemas
    ) {
        if (!(arg instanceof List)) {
            return null;
        }
        if (!uniqueItems) {
            return null;
        }
        Set<@Nullable Object> seenItems = new HashSet<>();
        for (@Nullable Object item: (List<?>) arg) {
            int startingSeenItemsSize = seenItems.size();
            seenItems.add(item);
            if (seenItems.size() == startingSeenItemsSize) {
                throw new ValidationException("Invalid list value, list contains duplicate items when uniqueItems is true");
            }
        }
        return null;
    }
}
