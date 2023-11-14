package org.openapijsonschematools.schemas;

import org.openapijsonschematools.configurations.SchemaConfiguration;

import java.util.LinkedHashSet;

public record FloatSchema(LinkedHashSet<Class<?>> type, String format) implements JsonSchema {
    public static FloatSchema withDefaults() {
        LinkedHashSet<Class<?>> type = new LinkedHashSet<>();
        type.add(Float.class);
        String format = "float";
        return new FloatSchema(type, format);
    }

    public static Float validate(Float arg, SchemaConfiguration configuration) {
        return JsonSchema.validate(FloatSchema.class, arg, configuration);
    }
}
