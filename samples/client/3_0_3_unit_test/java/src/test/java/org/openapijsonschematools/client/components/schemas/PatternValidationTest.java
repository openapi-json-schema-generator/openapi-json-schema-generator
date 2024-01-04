package org.openapijsonschematools.client.components.schemas;

import org.junit.Test;
import org.openapijsonschematools.client.configurations.JsonSchemaKeywordFlags;
import org.openapijsonschematools.client.configurations.SchemaConfiguration;
import org.openapijsonschematools.client.exceptions.ValidationException;
import org.openapijsonschematools.client.exceptions.InvalidTypeException;
import org.openapijsonschematools.client.schemas.validation.MapMaker;

import java.util.Arrays;

public class PatternValidationTest {
    static final SchemaConfiguration configuration = new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone());

    @Test
    public void testIgnoresBooleansPasses() {
        // ignores booleans
        final var schema = PatternValidation.PatternValidation1.getInstance();
        schema.validate(
            true,
            configuration
        );
    }

    @Test
    public void testIgnoresFloatsPasses() {
        // ignores floats
        final var schema = PatternValidation.PatternValidation1.getInstance();
        schema.validate(
            1.0d,
            configuration
        );
    }

    @Test
    public void testANonMatchingPatternIsInvalidFails() {
        // a non-matching pattern is invalid
        final var schema = PatternValidation.PatternValidation1.getInstance();
        try {
            schema.validate(
                "abc",
                configuration
            );
            throw new RuntimeException("A different exception must be thrown");
        } catch (ValidationException | InvalidTypeException ignored) {
            ;
        }
    }

    @Test
    public void testIgnoresIntegersPasses() {
        // ignores integers
        final var schema = PatternValidation.PatternValidation1.getInstance();
        schema.validate(
            123,
            configuration
        );
    }

    @Test
    public void testAMatchingPatternIsValidPasses() {
        // a matching pattern is valid
        final var schema = PatternValidation.PatternValidation1.getInstance();
        schema.validate(
            "aaa",
            configuration
        );
    }

    @Test
    public void testIgnoresArraysPasses() {
        // ignores arrays
        final var schema = PatternValidation.PatternValidation1.getInstance();
        schema.validate(
            Arrays.asList(
            ),
            configuration
        );
    }

    @Test
    public void testIgnoresObjectsPasses() {
        // ignores objects
        final var schema = PatternValidation.PatternValidation1.getInstance();
        schema.validate(
            MapMaker.makeMap(
            ),
            configuration
        );
    }

    @Test
    public void testIgnoresNullPasses() {
        // ignores null
        final var schema = PatternValidation.PatternValidation1.getInstance();
        schema.validate(
            (Void) null,
            configuration
        );
    }
}
