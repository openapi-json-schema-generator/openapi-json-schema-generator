package org.openapijsonschematools.schemas;

import org.openapijsonschematools.schemas.validation.JsonSchema;
import org.openapijsonschematools.schemas.validation.FrozenMap;
import org.openapijsonschematools.schemas.validation.FrozenList;
import org.openapijsonschematools.configurations.SchemaConfiguration;
import org.openapijsonschematools.exceptions.ValidationException;

import java.time.LocalDate;
import java.time.ZonedDateTime;
import java.util.List;
import java.util.Map;
import java.util.UUID;


public class AnyTypeJsonSchema extends JsonSchema {
    public static Void validate(Void arg, SchemaConfiguration configuration) throws ValidationException {
        return JsonSchema.validateVoid(AnyTypeJsonSchema.class, arg, configuration);
    }

    public static boolean validate(boolean arg, SchemaConfiguration configuration) throws ValidationException {
        return JsonSchema.validateBoolean(AnyTypeJsonSchema.class, arg, configuration);
    }

    public static int validate(int arg, SchemaConfiguration configuration) throws ValidationException {
        return JsonSchema.validateInt(AnyTypeJsonSchema.class, arg, configuration);
    }

    public static long validate(long arg, SchemaConfiguration configuration) throws ValidationException {
        return JsonSchema.validateLong(AnyTypeJsonSchema.class, arg, configuration);
    }

    public static float validate(float arg, SchemaConfiguration configuration) throws ValidationException {
        return JsonSchema.validateFloat(AnyTypeJsonSchema.class, arg, configuration);
    }

    public static double validate(double arg, SchemaConfiguration configuration) throws ValidationException {
        return JsonSchema.validateDouble(AnyTypeJsonSchema.class, arg, configuration);
    }

    public static String validate(String arg, SchemaConfiguration configuration) throws ValidationException {
        return JsonSchema.validateString(AnyTypeJsonSchema.class, arg, configuration);
    }

    public static String validate(ZonedDateTime arg, SchemaConfiguration configuration) throws ValidationException {
        return JsonSchema.validateZonedDateTime(AnyTypeJsonSchema.class, arg, configuration);
    }

    public static String validate(LocalDate arg, SchemaConfiguration configuration) throws ValidationException {
        return JsonSchema.validateLocalDate(AnyTypeJsonSchema.class, arg, configuration);
    }

    public static String validate(UUID arg, SchemaConfiguration configuration) throws ValidationException {
        return JsonSchema.validateUUID(AnyTypeJsonSchema.class, arg, configuration);
    }

    public static FrozenMap<String, Object> validate(Map<String, Object> arg, SchemaConfiguration configuration) throws ValidationException {
        return JsonSchema.validateMap(AnyTypeJsonSchema.class, arg, configuration);
    }

    public static FrozenList<Object> validate(List<Object> arg, SchemaConfiguration configuration) throws ValidationException {
        return JsonSchema.validateList(AnyTypeJsonSchema.class, arg, configuration);
    }
}
