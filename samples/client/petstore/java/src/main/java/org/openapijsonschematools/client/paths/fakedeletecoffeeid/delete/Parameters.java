package org.openapijsonschematools.client.paths.fakedeletecoffeeid.delete;

import org.openapijsonschematools.client.paths.fakedeletecoffeeid.delete.parameters.Parameter0;

import org.openapijsonschematools.client.parameter.Parameter;

import java.util.Map;
import java.util.AbstractMap;

public class Parameters {

    public static class PathParametersSerializer extends PathSerializer {
        public PathParametersSerializer() {
            super(
                Map.ofEntries(
                    new AbstractMap.SimpleEntry<>("id", new Parameter0.Parameter01())
                )
            );
        }
    }
}
