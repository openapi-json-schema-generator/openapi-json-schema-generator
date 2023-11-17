package org.openapijsonschematools.schemas;

import org.openapijsonschematools.configurations.SchemaConfiguration;

import java.time.LocalDate;
import java.time.ZonedDateTime;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.UUID;


public class DoubleJsonSchema implements JsonSchema {
    static final LinkedHashSet<Class<?>> type = new LinkedHashSet<>(Set.of(
        Double.class
    ));
    static final String format = "double";

    public static Double validate(Double arg, SchemaConfiguration configuration) {
        return JsonSchema.validate(DoubleJsonSchema.class, arg, configuration);
    }
}
