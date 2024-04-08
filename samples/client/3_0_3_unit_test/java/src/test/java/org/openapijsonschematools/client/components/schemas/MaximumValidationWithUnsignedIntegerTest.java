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

public class MaximumValidationWithUnsignedIntegerTest {
    static final SchemaConfiguration configuration = new SchemaConfiguration(new JsonSchemaKeywordFlags.Builder().format().build());

    @Test
    public void testAboveTheMaximumIsInvalidFails() {
        // above the maximum is invalid
        final var schema = MaximumValidationWithUnsignedInteger.MaximumValidationWithUnsignedInteger1.getInstance();
        try {
            schema.validate(
                300.5d,
                configuration
            );
            throw new RuntimeException("A different exception must be thrown");
        } catch (ValidationException ignored) {
            ;
        }
    }

    @Test
    public void testBelowTheMaximumIsInvalidPasses() throws ValidationException {
        // below the maximum is invalid
        final var schema = MaximumValidationWithUnsignedInteger.MaximumValidationWithUnsignedInteger1.getInstance();
        schema.validate(
            299.97d,
            configuration
        );
    }

    @Test
    public void testBoundaryPointIntegerIsValidPasses() throws ValidationException {
        // boundary point integer is valid
        final var schema = MaximumValidationWithUnsignedInteger.MaximumValidationWithUnsignedInteger1.getInstance();
        schema.validate(
            300,
            configuration
        );
    }

    @Test
    public void testBoundaryPointFloatIsValidPasses() throws ValidationException {
        // boundary point float is valid
        final var schema = MaximumValidationWithUnsignedInteger.MaximumValidationWithUnsignedInteger1.getInstance();
        schema.validate(
            300.0d,
            configuration
        );
    }
}
