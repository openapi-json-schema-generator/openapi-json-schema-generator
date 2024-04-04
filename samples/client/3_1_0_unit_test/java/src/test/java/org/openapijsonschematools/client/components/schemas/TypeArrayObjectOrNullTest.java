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

public class TypeArrayObjectOrNullTest {
    static final SchemaConfiguration configuration = new SchemaConfiguration(JsonSchemaKeywordFlags.onlyFormat());

    @Test
    public void testNumberIsInvalidFails() {
        // number is invalid
        final var schema = TypeArrayObjectOrNull.TypeArrayObjectOrNull1.getInstance();
        try {
            schema.validate(
                123,
                configuration
            );
            throw new RuntimeException("A different exception must be thrown");
        } catch (ValidationException ignored) {
            ;
        }
    }

    @Test
    public void testNullIsValidPasses() throws ValidationException {
        // null is valid
        final var schema = TypeArrayObjectOrNull.TypeArrayObjectOrNull1.getInstance();
        schema.validate(
            (Void) null,
            configuration
        );
    }

    @Test
    public void testStringIsInvalidFails() {
        // string is invalid
        final var schema = TypeArrayObjectOrNull.TypeArrayObjectOrNull1.getInstance();
        try {
            schema.validate(
                "foo",
                configuration
            );
            throw new RuntimeException("A different exception must be thrown");
        } catch (ValidationException ignored) {
            ;
        }
    }

    @Test
    public void testArrayIsValidPasses() throws ValidationException {
        // array is valid
        final var schema = TypeArrayObjectOrNull.TypeArrayObjectOrNull1.getInstance();
        schema.validate(
            Arrays.asList(
                1,
                2,
                3
            ),
            configuration
        );
    }

    @Test
    public void testObjectIsValidPasses() throws ValidationException {
        // object is valid
        final var schema = TypeArrayObjectOrNull.TypeArrayObjectOrNull1.getInstance();
        schema.validate(
            MapUtils.makeMap(
                new AbstractMap.SimpleEntry<String, Number>(
                    "foo",
                    123
                )
            ),
            configuration
        );
    }
}
