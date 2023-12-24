package org.openapijsonschematools.client.components.schemas;

import org.junit.Assert;
import org.junit.Test;
import org.openapijsonschematools.client.configurations.JsonSchemaKeywordFlags;
import org.openapijsonschematools.client.configurations.SchemaConfiguration;
import org.openapijsonschematools.client.exceptions.ValidationException;
import org.openapijsonschematools.client.exceptions.InvalidTypeException;
import org.openapijsonschematools.client.schemas.MapMaker;
import org.checkerframework.checker.nullness.qual.Nullable;

import java.util.Arrays;
import java.util.List;
import java.util.Map;
import java.util.AbstractMap;

public class NulCharactersInStringsTest {
    static final SchemaConfiguration configuration = new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone());

    @Test
    public void testMatchStringWithNulPasses() {
        // match string with nul
        final var schema = NulCharactersInStrings.NulCharactersInStrings1.getInstance();
        schema.validate(
            "hello\0there",
            configuration
        );
    }

    @Test
    public void testDoNotMatchStringLackingNulFails() {
        // do not match string lacking nul
        final var schema = NulCharactersInStrings.NulCharactersInStrings1.getInstance();
        try {
            schema.validate(
                "hellothere",
                configuration
            );
            throw new RuntimeException("A different exception must be thrown");
        } catch (ValidationException | InvalidTypeException ignored) {
            ;
        }
    }
}
