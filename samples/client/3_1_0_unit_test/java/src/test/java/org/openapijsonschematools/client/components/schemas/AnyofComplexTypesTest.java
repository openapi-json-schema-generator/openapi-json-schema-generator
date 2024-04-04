package org.openapijsonschematools.client.components.schemas;

import org.junit.Assert;
import org.junit.Test;
import org.openapijsonschematools.client.configurations.JsonSchemaKeywordFlags;
import org.openapijsonschematools.client.configurations.SchemaConfiguration;
import org.openapijsonschematools.client.exceptions.ValidationException;
import org.openapijsonschematools.client.schemas.validation.MapUtils;
import org.checkerframework.checker.nullness.qual.Nullable;

import java.util.Arrays;
import java.util.List;
import java.util.Map;
import java.util.AbstractMap;

public class AnyofComplexTypesTest {
    static final SchemaConfiguration configuration = new SchemaConfiguration(JsonSchemaKeywordFlags.onlyFormat());

    @Test
    public void testSecondAnyofValidComplexPasses() throws ValidationException {
        // second anyOf valid (complex)
        final var schema = AnyofComplexTypes.AnyofComplexTypes1.getInstance();
        schema.validate(
            MapUtils.makeMap(
                new AbstractMap.SimpleEntry<String, String>(
                    "foo",
                    "baz"
                )
            ),
            configuration
        );
    }

    @Test
    public void testBothAnyofValidComplexPasses() throws ValidationException {
        // both anyOf valid (complex)
        final var schema = AnyofComplexTypes.AnyofComplexTypes1.getInstance();
        schema.validate(
            MapUtils.makeMap(
                new AbstractMap.SimpleEntry<String, Object>(
                    "foo",
                    "baz"
                ),
                new AbstractMap.SimpleEntry<String, Object>(
                    "bar",
                    2
                )
            ),
            configuration
        );
    }

    @Test
    public void testFirstAnyofValidComplexPasses() throws ValidationException {
        // first anyOf valid (complex)
        final var schema = AnyofComplexTypes.AnyofComplexTypes1.getInstance();
        schema.validate(
            MapUtils.makeMap(
                new AbstractMap.SimpleEntry<String, Number>(
                    "bar",
                    2
                )
            ),
            configuration
        );
    }

    @Test
    public void testNeitherAnyofValidComplexFails() {
        // neither anyOf valid (complex)
        final var schema = AnyofComplexTypes.AnyofComplexTypes1.getInstance();
        try {
            schema.validate(
                MapUtils.makeMap(
                    new AbstractMap.SimpleEntry<String, Object>(
                        "foo",
                        2
                    ),
                    new AbstractMap.SimpleEntry<String, Object>(
                        "bar",
                        "quux"
                    )
                ),
                configuration
            );
            throw new RuntimeException("A different exception must be thrown");
        } catch (ValidationException ignored) {
            ;
        }
    }
}
