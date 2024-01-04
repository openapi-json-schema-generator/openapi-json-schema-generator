package org.openapijsonschematools.client.components.schemas;

import org.junit.Test;
import org.openapijsonschematools.client.configurations.JsonSchemaKeywordFlags;
import org.openapijsonschematools.client.configurations.SchemaConfiguration;
import org.openapijsonschematools.client.exceptions.ValidationException;
import org.openapijsonschematools.client.exceptions.InvalidTypeException;

public class MinlengthValidationTest {
    static final SchemaConfiguration configuration = new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone());

    @Test
    public void testExactLengthIsValidPasses() {
        // exact length is valid
        final var schema = MinlengthValidation.MinlengthValidation1.getInstance();
        schema.validate(
            "fo",
            configuration
        );
    }

    @Test
    public void testLongerIsValidPasses() {
        // longer is valid
        final var schema = MinlengthValidation.MinlengthValidation1.getInstance();
        schema.validate(
            "foo",
            configuration
        );
    }

    @Test
    public void testIgnoresNonStringsPasses() {
        // ignores non-strings
        final var schema = MinlengthValidation.MinlengthValidation1.getInstance();
        schema.validate(
            1,
            configuration
        );
    }

    @Test
    public void testTooShortIsInvalidFails() {
        // too short is invalid
        final var schema = MinlengthValidation.MinlengthValidation1.getInstance();
        try {
            schema.validate(
                "f",
                configuration
            );
            throw new RuntimeException("A different exception must be thrown");
        } catch (ValidationException | InvalidTypeException ignored) {
            ;
        }
    }

    @Test
    public void testOneSupplementaryUnicodeCodePointIsNotLongEnoughFails() {
        // one supplementary Unicode code point is not long enough
        final var schema = MinlengthValidation.MinlengthValidation1.getInstance();
        try {
            schema.validate(
                "💩",
                configuration
            );
            throw new RuntimeException("A different exception must be thrown");
        } catch (ValidationException | InvalidTypeException ignored) {
            ;
        }
    }
}
