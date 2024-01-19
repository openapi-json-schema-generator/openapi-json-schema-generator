package org.openapijsonschematools.client.schemas.validation;

import org.checkerframework.checker.nullness.qual.Nullable;
import org.openapijsonschematools.client.exceptions.InvalidTypeException;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.regex.Pattern;

public class PatternPropertiesValidator implements KeywordValidator {
    public final Map<Pattern, Class<? extends JsonSchema>> patternProperties;

    public PatternPropertiesValidator(Map<Pattern, Class<? extends JsonSchema>> patternProperties) {
        this.patternProperties = patternProperties;
    }

    @Override
    public @Nullable PathToSchemasMap validate(
        JsonSchema schema,
        @Nullable Object arg,
        ValidationMetadata validationMetadata,
        @Nullable List<PathToSchemasMap> containsPathToSchemas,
        @Nullable PathToSchemasMap patternPropertiesPathToSchemas,
        @Nullable PathToSchemasMap ifPathToSchemas
    ) {
        if (!(arg instanceof Map<?, ?>)) {
            return null;
        }
        return patternPropertiesPathToSchemas;
    }

    public PathToSchemasMap getPatternPropertiesPathToSchemas(
            @Nullable Object arg,
            ValidationMetadata validationMetadata
    ) {
        if (!(arg instanceof Map<?, ?> mapArg)) {
            return new PathToSchemasMap();
        }
        PathToSchemasMap pathToSchemas = new PathToSchemasMap();
        for (Map.Entry<?, ?> entry: mapArg.entrySet()) {
            Object entryKey = entry.getKey();
            if (!(entryKey instanceof String key)) {
                throw new InvalidTypeException("Invalid non-string type for map key");
            }
            List<Object> propPathToItem = new ArrayList<>(validationMetadata.pathToItem());
            propPathToItem.add(key);
            ValidationMetadata propValidationMetadata = new ValidationMetadata(
                    propPathToItem,
                    validationMetadata.configuration(),
                    validationMetadata.validatedPathToSchemas(),
                    validationMetadata.seenClasses()
            );
            for (Map.Entry<Pattern, Class<? extends JsonSchema>> patternPropEntry: patternProperties.entrySet()) {
                if (!patternPropEntry.getKey().matcher(key).find()) {
                    continue;
                }

                Class<? extends JsonSchema> patternPropClass = patternPropEntry.getValue();
                JsonSchema patternPropSchema = JsonSchemaFactory.getInstance(patternPropClass);
                PathToSchemasMap otherPathToSchemas = JsonSchema.validate(patternPropSchema, entry.getValue(), propValidationMetadata);
                pathToSchemas.update(otherPathToSchemas);
            }
        }
        return pathToSchemas;
    }
}

