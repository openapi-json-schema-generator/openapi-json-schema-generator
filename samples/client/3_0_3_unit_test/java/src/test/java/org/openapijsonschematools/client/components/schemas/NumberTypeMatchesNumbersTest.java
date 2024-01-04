package org.openapijsonschematools.client.components.schemas;

import org.junit.Test;
import org.openapijsonschematools.client.configurations.JsonSchemaKeywordFlags;
import org.openapijsonschematools.client.configurations.SchemaConfiguration;
import org.openapijsonschematools.client.exceptions.ValidationException;
import org.openapijsonschematools.client.exceptions.InvalidTypeException;
import org.openapijsonschematools.client.schemas.validation.MapMaker;

import java.util.Arrays;

public class NumberTypeMatchesNumbersTest {
    static final SchemaConfiguration configuration = new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone());

    @Test
    public void testAFloatIsANumberPasses() {
        // a float is a number
        final var schema = NumberTypeMatchesNumbers.NumberTypeMatchesNumbers1.getInstance();
        schema.validate(
            1.1d,
            configuration
        );
    }

    @Test
    public void testAnIntegerIsANumberPasses() {
        // an integer is a number
        final var schema = NumberTypeMatchesNumbers.NumberTypeMatchesNumbers1.getInstance();
        schema.validate(
            1,
            configuration
        );
    }

    @Test
    public void testAStringIsStillNotANumberEvenIfItLooksLikeOneFails() {
        // a string is still not a number, even if it looks like one
        final var schema = NumberTypeMatchesNumbers.NumberTypeMatchesNumbers1.getInstance();
        try {
            schema.validate(
                "1",
                configuration
            );
            throw new RuntimeException("A different exception must be thrown");
        } catch (ValidationException | InvalidTypeException ignored) {
            ;
        }
    }

    @Test
    public void testABooleanIsNotANumberFails() {
        // a boolean is not a number
        final var schema = NumberTypeMatchesNumbers.NumberTypeMatchesNumbers1.getInstance();
        try {
            schema.validate(
                true,
                configuration
            );
            throw new RuntimeException("A different exception must be thrown");
        } catch (ValidationException | InvalidTypeException ignored) {
            ;
        }
    }

    @Test
    public void testAFloatWithZeroFractionalPartIsANumberAndAnIntegerPasses() {
        // a float with zero fractional part is a number (and an integer)
        final var schema = NumberTypeMatchesNumbers.NumberTypeMatchesNumbers1.getInstance();
        schema.validate(
            1.0d,
            configuration
        );
    }

    @Test
    public void testNullIsNotANumberFails() {
        // null is not a number
        final var schema = NumberTypeMatchesNumbers.NumberTypeMatchesNumbers1.getInstance();
        try {
            schema.validate(
                (Void) null,
                configuration
            );
            throw new RuntimeException("A different exception must be thrown");
        } catch (ValidationException | InvalidTypeException ignored) {
            ;
        }
    }

    @Test
    public void testAStringIsNotANumberFails() {
        // a string is not a number
        final var schema = NumberTypeMatchesNumbers.NumberTypeMatchesNumbers1.getInstance();
        try {
            schema.validate(
                "foo",
                configuration
            );
            throw new RuntimeException("A different exception must be thrown");
        } catch (ValidationException | InvalidTypeException ignored) {
            ;
        }
    }

    @Test
    public void testAnArrayIsNotANumberFails() {
        // an array is not a number
        final var schema = NumberTypeMatchesNumbers.NumberTypeMatchesNumbers1.getInstance();
        try {
            schema.validate(
                Arrays.asList(
                ),
                configuration
            );
            throw new RuntimeException("A different exception must be thrown");
        } catch (ValidationException | InvalidTypeException ignored) {
            ;
        }
    }

    @Test
    public void testAnObjectIsNotANumberFails() {
        // an object is not a number
        final var schema = NumberTypeMatchesNumbers.NumberTypeMatchesNumbers1.getInstance();
        try {
            schema.validate(
                MapMaker.makeMap(
                ),
                configuration
            );
            throw new RuntimeException("A different exception must be thrown");
        } catch (ValidationException | InvalidTypeException ignored) {
            ;
        }
    }
}
