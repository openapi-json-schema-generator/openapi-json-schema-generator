package org.openapijsonschematools.client.components.schemas;

import org.junit.Assert;
import org.junit.Test;
import org.openapijsonschematools.client.configurations.JsonSchemaKeywordFlags;
import org.openapijsonschematools.client.configurations.SchemaConfiguration;
import org.openapijsonschematools.client.exceptions.ValidationException;
import org.openapijsonschematools.client.schemas.validation.JsonSchema;
import org.openapijsonschematools.client.schemas.MapMaker;

import java.util.Arrays;
import java.util.List;
import java.util.AbstractMap;

public class MinlengthValidationTest {
    static final SchemaConfiguration configuration = new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone());

    @Test
    public void testExactLengthIsValidPasses() {
        // exact length is valid
        MinlengthValidation.MinlengthValidation1.validate(
            "fo",
            configuration
        );
    }

    @Test
    public void testLongerIsValidPasses() {
        // longer is valid
        MinlengthValidation.MinlengthValidation1.validate(
            "foo",
            configuration
        );
    }

    @Test
    public void testIgnoresNonStringsPasses() {
        // ignores non-strings
        MinlengthValidation.MinlengthValidation1.validate(
            1,
            configuration
        );
    }

    @Test
    public void testTooShortIsInvalidFails() {
        // too short is invalid
        Assert.assertThrows(ValidationException.class, () -> JsonSchema.validate(
            MinlengthValidation.MinlengthValidation1.class,
            "f",
            configuration
        ));
    }

    @Test
    public void testOneSupplementaryUnicodeCodePointIsNotLongEnoughFails() {
        // one supplementary Unicode code point is not long enough
        Assert.assertThrows(ValidationException.class, () -> JsonSchema.validate(
            MinlengthValidation.MinlengthValidation1.class,
            "💩",
            configuration
        ));
    }
}
