package unit_test_api.schemas.validation;

import unit_test_api.exceptions.ValidationException;
import org.checkerframework.checker.nullness.qual.Nullable;

import java.util.Map;

public class MinPropertiesValidator implements KeywordValidator {
    @Override
    public @Nullable PathToSchemasMap validate(
        ValidationData data
    ) throws ValidationException {
        var minProperties = data.schema().minProperties;
        if (minProperties == null) {
            return null;
        }
        if (!(data.arg() instanceof Map<?, ?> mapArg)) {
            return null;
        }
        if (mapArg.size() < minProperties) {
            throw new ValidationException("Value " + mapArg + " is invalid because has < the minProperties of " + minProperties);
        }
        return null;
    }
}
