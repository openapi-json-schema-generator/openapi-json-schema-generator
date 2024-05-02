package org.openapijsonschematools.client.schemas.validation;

import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

@SuppressWarnings("serial")
public class PathToSchemasMap extends LinkedHashMap<List<Object>, LinkedHashMap<JsonSchema<?>, Nothing?>> {

    public void update(PathToSchemasMap other) {
        for (Map.Entry<List<Object>, LinkedHashMap<JsonSchema<?>, Nothing?>> entry: other.entrySet()) {
            List<Object> pathToItem = entry.getKey();
            LinkedHashMap<JsonSchema<?>, Nothing?> otherSchemas = entry.getValue();
            if (containsKey(pathToItem)) {
                get(pathToItem).putAll(otherSchemas);
            } else {
                put(pathToItem, otherSchemas);
            }
        }
    }
}