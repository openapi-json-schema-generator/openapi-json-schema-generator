package org.openapijsonschematools.client.schemas.validation;
import org.checkerframework.checker.nullness.qual.Nullable;

public class AllOfValidator implements KeywordValidator {
    @Override
    public @Nullable PathToSchemasMap validate(
        ValidationData data
    ) {
        var allOf = data.schema().allOf;
        if (allOf == null) {
            return null;
        }
        PathToSchemasMap pathToSchemas = new PathToSchemasMap();
        for(Class<? extends JsonSchema> allOfClass: allOf) {
            JsonSchema allOfSchema = JsonSchemaFactory.getInstance(allOfClass);
            PathToSchemasMap otherPathToSchemas = JsonSchema.validate(allOfSchema, data.arg(), data.validationMetadata());
            pathToSchemas.update(otherPathToSchemas);
        }
        return pathToSchemas;
    }
}
