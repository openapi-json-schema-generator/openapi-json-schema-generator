package org.openapijsonschematools.schemas;

import org.openapijsonschematools.configurations.SchemaConfiguration;

import java.util.LinkedHashSet;
import java.util.List;

public record ListSchema(LinkedHashSet<Class<?>> type) implements JsonSchema {
    public static ListSchema withDefaults() {
        LinkedHashSet<Class<?>> type = new LinkedHashSet<>();
        type.add(FrozenList.class);
        return new ListSchema(type);
    }

    public static FrozenList<Object> validate(List<Object> arg, SchemaConfiguration configuration) {
        return JsonSchema.validate(ListSchema.class, arg, configuration);
    }
}
