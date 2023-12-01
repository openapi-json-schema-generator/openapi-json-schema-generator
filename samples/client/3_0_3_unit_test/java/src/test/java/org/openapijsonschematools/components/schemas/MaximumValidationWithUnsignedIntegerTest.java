package org.openapijsonschematools.components.schemas;

import org.junit.Assert;
import org.junit.Test;
import org.openapijsonschematools.configurations.JsonSchemaKeywordFlags;
import org.openapijsonschematools.configurations.SchemaConfiguration;
import org.openapijsonschematools.exceptions.ValidationException;
import org.openapijsonschematools.schemas.validation.JsonSchema;
import org.openapijsonschematools.schemas.MapMaker;

import java.util.Arrays;
import java.util.List;
import java.util.AbstractMap;

public class MaximumValidationWithUnsignedIntegerTest {
    static final SchemaConfiguration configuration = new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone());

    @Test
    public void testAboveTheMaximumIsInvalidFails() {
        // above the maximum is invalid
        Assert.assertThrows(ValidationException.class, () -> JsonSchema.validateObject(
            MaximumValidationWithUnsignedInteger.MaximumValidationWithUnsignedInteger1.class,
            300.5,
            configuration
        ));
    }

    @Test
    public void testBelowTheMaximumIsInvalidPasses() {
        // below the maximum is invalid
        MaximumValidationWithUnsignedInteger.MaximumValidationWithUnsignedInteger1.validate(
            299.97,
            configuration
        );
    }

    @Test
    public void testBoundaryPointIntegerIsValidPasses() {
        // boundary point integer is valid
        MaximumValidationWithUnsignedInteger.MaximumValidationWithUnsignedInteger1.validate(
            300,
            configuration
        );
    }

    @Test
    public void testBoundaryPointFloatIsValidPasses() {
        // boundary point float is valid
        MaximumValidationWithUnsignedInteger.MaximumValidationWithUnsignedInteger1.validate(
            300.0,
            configuration
        );
    }
}
