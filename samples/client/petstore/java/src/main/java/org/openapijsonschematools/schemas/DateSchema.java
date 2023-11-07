package org.openapijsonschematools.schemas;

import org.openapijsonschematools.configurations.SchemaConfiguration;

import java.util.LinkedHashSet;
import java.time.LocalDate;

record DateSchema(LinkedHashSet<Class<?>> type, String format) implements Schema {
    public static DateSchema withDefaults() {
        LinkedHashSet<Class<?>> type = new LinkedHashSet<>();
        type.add(String.class);
        String format = "date";
        return new DateSchema(type, format);
    }

    public static String validate(String arg, SchemaConfiguration configuration) {
        return Schema.validate(DateSchema.class, arg, configuration);
    }

    public static String validate(LocalDate arg, SchemaConfiguration configuration) {
        return Schema.validate(DateSchema.class, arg, configuration);
    }
}
