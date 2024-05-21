package unit_test_api.schemas.validation;

import unit_test_api.exceptions.ValidationException;
import org.checkerframework.checker.nullness.qual.Nullable;

import java.util.Map;

public class MaxPropertiesValidator implements KeywordValidator {
    @Override
    public @Nullable PathToSchemasMap validate(
        ValidationData data
    ) throws ValidationException {
        var maxProperties = data.schema().maxProperties;
        if (maxProperties == null) {
            return null;
        }
        if (!(data.arg() instanceof Map<?, ?> mapArg)) {
            return null;
        }
        if (mapArg.size() > maxProperties) {
            throw new ValidationException("Value " + mapArg + " is invalid because has > the maxProperties of " + maxProperties);
        }
        return null;
    }
}
