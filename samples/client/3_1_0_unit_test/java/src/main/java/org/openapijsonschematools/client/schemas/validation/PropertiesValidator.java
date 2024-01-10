package org.openapijsonschematools.client.schemas.validation;

import org.checkerframework.checker.nullness.qual.Nullable;

import java.util.ArrayList;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

public class PropertiesValidator implements KeywordValidator {
    public final Map<String, Class<? extends JsonSchema>> properties;

    public PropertiesValidator(Map<String, Class<? extends JsonSchema>> properties) {
        this.properties = properties;
    }

    @Override
    public @Nullable PathToSchemasMap validate(JsonSchema schema, @Nullable Object arg, ValidationMetadata validationMetadata) {
        if (!(arg instanceof Map<?, ?> mapArg)) {
            return null;
        }
        PathToSchemasMap pathToSchemas = new PathToSchemasMap();
        Set<String> presentProperties = new LinkedHashSet<>();
        for (Object key: mapArg.keySet()) {
            if (key instanceof String) {
                presentProperties.add((String) key);
            }
        }
        for(Map.Entry<String, Class<? extends JsonSchema>> entry: properties.entrySet()) {
            String propName = entry.getKey();
            if (!presentProperties.contains(propName)) {
                continue;
            }
            @Nullable Object propValue = ((Map<?, ?>) arg).get(propName);
            List<Object> propPathToItem = new ArrayList<>(validationMetadata.pathToItem());
            propPathToItem.add(propName);
            ValidationMetadata propValidationMetadata = new ValidationMetadata(
                    propPathToItem,
                    validationMetadata.configuration(),
                    validationMetadata.validatedPathToSchemas(),
                    validationMetadata.seenClasses()
            );
            Class<? extends JsonSchema> propClass = entry.getValue();
            JsonSchema propSchema = JsonSchemaFactory.getInstance(propClass);
            if (propValidationMetadata.validationRanEarlier(propSchema)) {
                // todo add_deeper_validated_schemas
                continue;
            }
            PathToSchemasMap otherPathToSchemas = JsonSchema.validate(propSchema, propValue, propValidationMetadata);
            pathToSchemas.update(otherPathToSchemas);
        }
        return pathToSchemas;
    }
}

