package org.openapijsonschematools.client.components.schemas;

import org.junit.Test;
import org.openapijsonschematools.client.configurations.JsonSchemaKeywordFlags;
import org.openapijsonschematools.client.configurations.SchemaConfiguration;
import org.openapijsonschematools.client.exceptions.ValidationException;
import org.openapijsonschematools.client.exceptions.InvalidTypeException;
import org.openapijsonschematools.client.schemas.validation.MapMaker;

import java.util.AbstractMap;

public class RequiredWithEscapedCharactersTest {
    static final SchemaConfiguration configuration = new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone());

    @Test
    public void testObjectWithSomePropertiesMissingIsInvalidFails() {
        // object with some properties missing is invalid
        final var schema = RequiredWithEscapedCharacters.RequiredWithEscapedCharacters1.getInstance();
        try {
            schema.validate(
                MapMaker.makeMap(
                    new AbstractMap.SimpleEntry<String, String>(
                        "foo\nbar",
                        "1"
                    ),
                    new AbstractMap.SimpleEntry<String, String>(
                        "foo\"bar",
                        "1"
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
    public void testObjectWithAllPropertiesPresentIsValidPasses() {
        // object with all properties present is valid
        final var schema = RequiredWithEscapedCharacters.RequiredWithEscapedCharacters1.getInstance();
        schema.validate(
            MapMaker.makeMap(
                new AbstractMap.SimpleEntry<String, Number>(
                    "foo\nbar",
                    1
                ),
                new AbstractMap.SimpleEntry<String, Number>(
                    "foo\"bar",
                    1
                ),
                new AbstractMap.SimpleEntry<String, Number>(
                    "foo\\bar",
                    1
                ),
                new AbstractMap.SimpleEntry<String, Number>(
                    "foo\rbar",
                    1
                ),
                new AbstractMap.SimpleEntry<String, Number>(
                    "foo\tbar",
                    1
                ),
                new AbstractMap.SimpleEntry<String, Number>(
                    "foo\fbar",
                    1
                )
            ),
            configuration
        );
    }
}
