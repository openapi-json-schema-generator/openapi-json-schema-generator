package org.openapijsonschematools.client.components.schemas;

import org.junit.Test;
import org.openapijsonschematools.client.configurations.JsonSchemaKeywordFlags;
import org.openapijsonschematools.client.configurations.SchemaConfiguration;
import org.openapijsonschematools.client.exceptions.ValidationException;
import org.openapijsonschematools.client.exceptions.InvalidTypeException;
import org.openapijsonschematools.client.schemas.validation.MapMaker;

import java.util.AbstractMap;

public class Maxproperties0MeansTheObjectIsEmptyTest {
    static final SchemaConfiguration configuration = new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone());

    @Test
    public void testOnePropertyIsInvalidFails() {
        // one property is invalid
        final var schema = Maxproperties0MeansTheObjectIsEmpty.Maxproperties0MeansTheObjectIsEmpty1.getInstance();
        try {
            schema.validate(
                MapMaker.makeMap(
                    new AbstractMap.SimpleEntry<>(
                        "foo",
                        1
                    )
                ),
                configuration
            );
            throw new RuntimeException("A different exception must be thrown");
        } catch (ValidationException | InvalidTypeException ignored) {
            ;
        }
    }

    @Test
    public void testNoPropertiesIsValidPasses() {
        // no properties is valid
        final var schema = Maxproperties0MeansTheObjectIsEmpty.Maxproperties0MeansTheObjectIsEmpty1.getInstance();
        schema.validate(
            MapMaker.makeMap(
            ),
            configuration
        );
    }
}
