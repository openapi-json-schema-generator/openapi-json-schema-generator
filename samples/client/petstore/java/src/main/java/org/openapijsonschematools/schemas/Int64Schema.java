package org.openapijsonschematools.schemas;

import org.openapijsonschematools.configurations.SchemaConfiguration;

import java.util.LinkedHashSet;
import java.math.BigDecimal;

public record Int64Schema(LinkedHashSet<Class<?>> type, String format) implements Schema {
    public static Int64Schema withDefaults() {
        LinkedHashSet<Class<?>> type = new LinkedHashSet<>();
        type.add(BigDecimal.class);
        String format = "int64";
        return new Int64Schema(type, format);
    }

    public static Long validate(Integer arg, SchemaConfiguration configuration) {
        return Schema.validate(Int64Schema.class, Long.valueOf(arg), configuration);
    }

    public static Long validate(Float arg, SchemaConfiguration configuration) {
        return Schema.validate(Int64Schema.class, Long.parseLong(arg.toString()), configuration);
    }

    public static Long validate(Long arg, SchemaConfiguration configuration) {
        return Schema.validate(Int64Schema.class, arg, configuration);
    }

    public static Long validate(Double arg, SchemaConfiguration configuration) {
        return Schema.validate(Int64Schema.class, Long.parseLong(arg.toString()), configuration);
    }
}
