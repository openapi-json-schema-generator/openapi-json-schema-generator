package org.openapijsonschematools.client.schemas;

import org.openapijsonschematools.client.schemas.validation.JsonSchema;
import org.openapijsonschematools.client.configurations.SchemaConfiguration;
import org.openapijsonschematools.client.schemas.validation.KeywordValidator;
import org.openapijsonschematools.client.schemas.validation.KeywordEntry;
import org.openapijsonschematools.client.schemas.validation.TypeValidator;
import org.openapijsonschematools.client.exceptions.ValidationException;

import java.time.LocalDate;
import java.time.ZonedDateTime;
import java.util.LinkedHashMap;
import java.util.Set;
import java.util.Map;
import java.util.UUID;

public class StringJsonSchema extends JsonSchema {
    public static final LinkedHashMap<String, KeywordValidator> keywordToValidator = new LinkedHashMap<>(Map.ofEntries(
        new KeywordEntry("type", new TypeValidator(Set.of(String.class)))
    ));

    public static String validate(String arg, SchemaConfiguration configuration) throws ValidationException {
        return JsonSchema.validateString(StringJsonSchema.class, arg, configuration);
    }

    public static String validate(ZonedDateTime arg, SchemaConfiguration configuration) throws ValidationException {
        return JsonSchema.validateZonedDateTime(StringJsonSchema.class, arg, configuration);
    }

    public static String validate(LocalDate arg, SchemaConfiguration configuration) throws ValidationException {
        return JsonSchema.validateLocalDate(StringJsonSchema.class, arg, configuration);
    }

    public static String validate(UUID arg, SchemaConfiguration configuration) throws ValidationException {
        return JsonSchema.validateUUID(StringJsonSchema.class, arg, configuration);
    }
}
