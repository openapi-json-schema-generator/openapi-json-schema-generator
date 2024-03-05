package org.openapijsonschematools.client.paths.userusername.delete;

import org.openapijsonschematools.client.paths.userusername.delete.parameters.Parameter0;
import org.openapijsonschematools.client.parameter.NonQueryParameter;

import java.util.Map;
import java.util.AbstractMap;

public class Parameters {

    public static class PathParametersDeserializer {
        Map<String, NonQueryParameter> parameters;

        public PathParametersDeserializer() {
            parameters = Map.ofEntries(
                new AbstractMap.SimpleEntry<>("", new Parameter0.Parameter01())
            );
        }

        // deserialize PathParameters
    }
}
