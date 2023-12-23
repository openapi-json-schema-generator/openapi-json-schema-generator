package org.openapijsonschematools.client.schemas.validation;

import org.openapijsonschematools.client.exceptions.ValidationException;
import org.checkerframework.checker.nullness.qual.Nullable;

import java.util.ArrayList;
import java.util.List;

public class OneOfValidator implements KeywordValidator {
    public final List<Class<? extends JsonSchema>> oneOf;

    public OneOfValidator(List<Class<? extends JsonSchema>> oneOf) {
        this.oneOf = oneOf;
    }

    @Override
    public @Nullable PathToSchemasMap validate(JsonSchema schema, @Nullable Object arg, ValidationMetadata validationMetadata) {
        PathToSchemasMap pathToSchemas = new PathToSchemasMap();
        List<Class<? extends JsonSchema>> validatedOneOfClasses = new ArrayList<>();
        for(Class<? extends JsonSchema> oneOfClass: oneOf) {
            if (oneOfClass == schema.getClass()) {
                /*
                optimistically assume that schema will pass validation
                do not invoke validate on it because that is recursive
                */
                validatedOneOfClasses.add(oneOfClass);
                continue;
            }
            try {
                JsonSchema oneOfSchema = JsonSchemaFactory.getInstance(oneOfClass);
                PathToSchemasMap otherPathToSchemas = JsonSchema.validate(oneOfSchema, arg, validationMetadata);
                validatedOneOfClasses.add(oneOfClass);
                pathToSchemas.update(otherPathToSchemas);
            } catch (ValidationException e) {
                // silence exceptions because the code needs to accumulate validatedOneOfClasses
            }
        }
        if (validatedOneOfClasses.isEmpty()) {
            throw new ValidationException("Invalid inputs given to generate an instance of "+schema.getClass()+". None "+
                    "of the oneOf schemas matched the input data."
            );
        }
        if (validatedOneOfClasses.size() > 1) {
            throw new ValidationException("Invalid inputs given to generate an instance of "+schema.getClass()+". Multiple "+
                    "oneOf schemas validated the data, but a max of one is allowed."
            );
        }
        return pathToSchemas;
    }
}
