package unit_test_api.schemas.validation;

import unit_test_api.exceptions.ValidationException;
import org.checkerframework.checker.nullness.qual.Nullable;

import java.util.List;

public class MinItemsValidator implements KeywordValidator {
    @Override
    public @Nullable PathToSchemasMap validate(
        ValidationData data
    ) throws ValidationException {
        var minItems = data.schema().minItems;
        if (minItems == null) {
            return null;
        }
        if (!(data.arg() instanceof List<?> listArg)) {
            return null;
        }
        if (listArg.size() < minItems) {
            throw new ValidationException("Value " + listArg + " is invalid because has < the minItems of " + minItems);
        }
        return null;
    }
}
