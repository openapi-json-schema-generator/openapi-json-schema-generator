package org.openapijsonschematools.client.components.schemas;

import org.junit.Test;
import org.openapijsonschematools.client.configurations.JsonSchemaKeywordFlags;
import org.openapijsonschematools.client.configurations.SchemaConfiguration;
import org.openapijsonschematools.client.exceptions.ValidationException;
import org.openapijsonschematools.client.exceptions.InvalidTypeException;
import org.openapijsonschematools.client.schemas.validation.MapMaker;

import java.util.AbstractMap;

public class ForbiddenPropertyTest {
    static final SchemaConfiguration configuration = new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone());

    @Test
    public void testPropertyPresentFails() {
        // property present
        final var schema = ForbiddenProperty.ForbiddenProperty1.getInstance();
        try {
            schema.validate(
                MapMaker.makeMap(
                    new AbstractMap.SimpleEntry<String, Number>(
                        "foo",
                        1
                    ),
                    new AbstractMap.SimpleEntry<String, Number>(
                        "bar",
                        2
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
    public void testPropertyAbsentPasses() {
        // property absent
        final var schema = ForbiddenProperty.ForbiddenProperty1.getInstance();
        schema.validate(
            MapMaker.makeMap(
                new AbstractMap.SimpleEntry<String, Number>(
                    "bar",
                    1
                ),
                new AbstractMap.SimpleEntry<String, Number>(
                    "baz",
                    2
                )
            ),
            configuration
        );
    }
}
