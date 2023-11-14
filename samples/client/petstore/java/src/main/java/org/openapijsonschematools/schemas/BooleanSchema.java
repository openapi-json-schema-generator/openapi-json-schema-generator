package org.openapijsonschematools.schemas;

import org.openapijsonschematools.configurations.SchemaConfiguration;

import java.util.LinkedHashSet;

public record BooleanSchema(LinkedHashSet<Class<?>> type) implements JsonSchema {
    public static BooleanSchema withDefaults() {
        LinkedHashSet<Class<?>> type = new LinkedHashSet<>();
        type.add(Boolean.class);
        return new BooleanSchema(type);
    }

    public static Boolean validate(Boolean arg, SchemaConfiguration configuration) {
        return JsonSchema.validate(BooleanSchema.class, arg, configuration);
    }
}
