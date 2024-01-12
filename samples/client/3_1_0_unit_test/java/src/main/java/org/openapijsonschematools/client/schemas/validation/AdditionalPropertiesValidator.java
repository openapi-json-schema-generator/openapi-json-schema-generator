package org.openapijsonschematools.client.schemas.validation;
import org.checkerframework.checker.nullness.qual.Nullable;

import java.util.ArrayList;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

public class AdditionalPropertiesValidator implements KeywordValidator {
    public final Class<? extends JsonSchema> additionalProperties;

    public AdditionalPropertiesValidator(Class<? extends JsonSchema> additionalProperties) {
        this.additionalProperties = additionalProperties;
    }

    @Override
    public @Nullable PathToSchemasMap validate(
        JsonSchema schema,
        @Nullable Object arg,
        ValidationMetadata validationMetadata,
        @Nullable List<PathToSchemasMap> containsPathToSchemas
    ) {
        if (!(arg instanceof Map<?, ?> mapArg)) {
            return null;
        }
        Set<String> presentAdditionalProperties = new LinkedHashSet<>();
        for (Object key: mapArg.keySet()) {
            if (key instanceof String) {
                presentAdditionalProperties.add((String) key);
            }
        }
        if (schema.properties != null) {
            presentAdditionalProperties.removeAll(schema.properties.keySet());
        }
        PathToSchemasMap pathToSchemas = new PathToSchemasMap();
        // todo add handling for validatedPatternProperties
        for(String addPropName: presentAdditionalProperties) {
            @Nullable Object propValue = mapArg.get(addPropName);
            List<Object> propPathToItem = new ArrayList<>(validationMetadata.pathToItem());
            propPathToItem.add(addPropName);
            ValidationMetadata propValidationMetadata = new ValidationMetadata(
                    propPathToItem,
                    validationMetadata.configuration(),
                    validationMetadata.validatedPathToSchemas(),
                    validationMetadata.seenClasses()
            );
            JsonSchema addPropsSchema = JsonSchemaFactory.getInstance(additionalProperties);
            if (propValidationMetadata.validationRanEarlier(addPropsSchema)) {
                // todo add_deeper_validated_schemas
                continue;
            }
            PathToSchemasMap otherPathToSchemas = JsonSchema.validate(addPropsSchema, propValue, propValidationMetadata);
            pathToSchemas.update(otherPathToSchemas);
        }
        return pathToSchemas;
    }
}
