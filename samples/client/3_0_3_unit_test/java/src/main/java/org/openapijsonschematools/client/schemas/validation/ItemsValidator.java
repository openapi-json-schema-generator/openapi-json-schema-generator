package org.openapijsonschematools.client.schemas.validation;

import org.checkerframework.checker.nullness.qual.Nullable;

import java.util.ArrayList;
import java.util.List;

public class ItemsValidator implements KeywordValidator {
    public final Class<? extends JsonSchema> items;

    public ItemsValidator(Class<? extends JsonSchema> items) {
        this.items = items;
    }

    @Override
    public @Nullable PathToSchemasMap validate(
        JsonSchema schema,
        @Nullable Object arg,
        ValidationMetadata validationMetadata,
        @Nullable List<PathToSchemasMap> containsPathToSchemas,
        @Nullable PathToSchemasMap patternPropertiesPathToSchemas
    ) {
        if (!(arg instanceof List)) {
            return null;
        }
        PathToSchemasMap pathToSchemas = new PathToSchemasMap();
        // todo add handling for prefixItems
        int i = 0;
        for(Object itemValue: (List<?>) arg) {
            List<Object> itemPathToItem = new ArrayList<>(validationMetadata.pathToItem());
            itemPathToItem.add(i);
            ValidationMetadata itemValidationMetadata = new ValidationMetadata(
                    itemPathToItem,
                    validationMetadata.configuration(),
                    validationMetadata.validatedPathToSchemas(),
                    validationMetadata.seenClasses()
            );
            JsonSchema itemsSchema = JsonSchemaFactory.getInstance(items);
            if (itemValidationMetadata.validationRanEarlier(itemsSchema)) {
                // todo add_deeper_validated_schemas
                i +=1;
                continue;
            }
            PathToSchemasMap otherPathToSchemas = JsonSchema.validate(itemsSchema, itemValue, itemValidationMetadata);
            pathToSchemas.update(otherPathToSchemas);
            i += 1;
        }
        return pathToSchemas;
    }
}
