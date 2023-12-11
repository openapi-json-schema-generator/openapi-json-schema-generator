package org.openapijsonschematools.client.schemas;

import org.openapijsonschematools.client.schemas.validation.FrozenMap;
import org.openapijsonschematools.client.schemas.validation.FrozenList;
import org.openapijsonschematools.client.schemas.validation.JsonSchema;
import org.openapijsonschematools.client.schemas.validation.FrozenMap;
import org.openapijsonschematools.client.schemas.validation.FrozenList;
import org.openapijsonschematools.client.configurations.SchemaConfiguration;
import org.openapijsonschematools.client.exceptions.ValidationException;

import java.time.LocalDate;
import java.time.ZonedDateTime;
import java.util.List;
import java.util.Map;

public class AnyTypeJsonSchema extends JsonSchema<Object, Object, FrozenMap<String, Object>, Object, Object, FrozenList<Object>> {
    public AnyTypeJsonSchema() {
        super(null);
    }

    Void validate(Void arg, SchemaConfiguration configuration) {
        return validateVoid(arg, configuration);
    }

    boolean validate(boolean arg, SchemaConfiguration configuration) {
        return validateBoolean(arg, configuration);
    }

    int validate(int arg, SchemaConfiguration configuration) {
        return validateInt(arg, configuration);
    }

    long validate(long arg, SchemaConfiguration configuration) {
        return validateLong(arg, configuration);
    }

    float validate(float arg, SchemaConfiguration configuration) {
        return validateFloat(arg, configuration);
    }

    double validate(double arg, SchemaConfiguration configuration) {
        return validateDouble(arg, configuration);
    }

    String validate(String arg, SchemaConfiguration configuration) {
        return validateString(arg, configuration);
    }

    String validate(ZonedDateTime arg, SchemaConfiguration configuration) {
        return validateZonedDateTime(arg, configuration);
    }

    String validate(LocalDate arg, SchemaConfiguration configuration) {
        return validateLocalDate(arg, configuration);
    }

    FrozenMap<String, Object> validate(Map<String, Object> arg, SchemaConfiguration configuration) {
        return validateMap(arg, configuration);
    }

    FrozenList<Object> validate(List<Object> arg, SchemaConfiguration configuration) {
        return validateList(arg, configuration);
    }
}
