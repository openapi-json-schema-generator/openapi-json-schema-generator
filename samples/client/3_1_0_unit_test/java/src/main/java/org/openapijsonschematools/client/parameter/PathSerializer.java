package org.openapijsonschematools.client.parameter;

import org.checkerframework.checker.nullness.qual.Nullable;

import java.util.AbstractMap;
import java.util.Map;

public abstract class PathSerializer {
    private final Map<String, Parameter> parameters;

    protected PathSerializer(Map<String, Parameter> parameters) {
        this.parameters = parameters;
    }

    public String serialize(Map<String, @Nullable Object> inData, String pathWithPlaceholders) {
        String result = pathWithPlaceholders;
        for (Map.Entry<String, @Nullable Object> entry: inData.entrySet()) {
            String mapKey = entry.getKey();
            @Nullable Parameter parameter = parameters.get(mapKey);
            if (parameter == null) {
                throw new RuntimeException("Invalid state, a parameter must exist for every key");
            }
            @Nullable Object value = entry.getValue();
            AbstractMap.SimpleEntry<String, String> serialized = parameter.serialize(value);
            result = result.replace("{" + mapKey + "}", serialized.getValue());
        }
        return result;
    }
}
