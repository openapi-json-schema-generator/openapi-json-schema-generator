package org.openapijsonschematools.client.components.schemas;

import org.junit.Test;
import org.openapijsonschematools.client.configurations.JsonSchemaKeywordFlags;
import org.openapijsonschematools.client.configurations.SchemaConfiguration;
import org.openapijsonschematools.client.exceptions.ValidationException;
import org.openapijsonschematools.client.exceptions.InvalidTypeException;

public class EnumWithTrueDoesNotMatch1Test {
    static final SchemaConfiguration configuration = new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone());

    @Test
    public void testFloatOneIsInvalidFails() {
        // float one is invalid
        final var schema = EnumWithTrueDoesNotMatch1.EnumWithTrueDoesNotMatch11.getInstance();
        try {
            schema.validate(
                1.0d,
                configuration
            );
            throw new RuntimeException("A different exception must be thrown");
        } catch (ValidationException | InvalidTypeException ignored) {
            ;
        }
    }

    @Test
    public void testIntegerOneIsInvalidFails() {
        // integer one is invalid
        final var schema = EnumWithTrueDoesNotMatch1.EnumWithTrueDoesNotMatch11.getInstance();
        try {
            schema.validate(
                1,
                configuration
            );
            throw new RuntimeException("A different exception must be thrown");
        } catch (ValidationException | InvalidTypeException ignored) {
            ;
        }
    }

    @Test
    public void testTrueIsValidPasses() {
        // true is valid
        final var schema = EnumWithTrueDoesNotMatch1.EnumWithTrueDoesNotMatch11.getInstance();
        schema.validate(
            true,
            configuration
        );
    }
}
