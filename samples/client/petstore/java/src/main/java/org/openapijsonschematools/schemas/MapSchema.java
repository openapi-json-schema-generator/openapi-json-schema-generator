package org.openapijsonschematools.schemas;

import org.openapijsonschematools.configurations.SchemaConfiguration;

import java.util.LinkedHashSet;
import java.util.Map;

record MapSchema(LinkedHashSet<Class<?>> type) implements Schema {
    public static MapSchema withDefaults() {
        LinkedHashSet<Class<?>> type = new LinkedHashSet<>();
        // can't use ImmutableMap because it does not allow null values in entries
        // can't use Collections.unmodifiableMap because Collections.UnmodifiableMap is not public + extensible
        type.add(FrozenMap.class);
        return new MapSchema(type);
    }

    public static FrozenMap<String, Object> validate(Map<String, Object> arg, SchemaConfiguration configuration) {
        return Schema.validate(MapSchema.class, arg, configuration);
    }
}
