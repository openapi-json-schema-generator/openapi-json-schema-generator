package org.openapijsonschematools.client.components.schemas;

import org.junit.Assert;
import org.junit.Test;
import org.openapijsonschematools.client.configurations.JsonSchemaKeywordFlags;
import org.openapijsonschematools.client.configurations.SchemaConfiguration;
import org.openapijsonschematools.client.exceptions.ValidationException;
import org.openapijsonschematools.client.exceptions.InvalidTypeException;
import org.openapijsonschematools.client.schemas.validation.MapUtils;
import org.checkerframework.checker.nullness.qual.Nullable;

import java.util.Arrays;
import java.util.List;
import java.util.Map;
import java.util.AbstractMap;

public class UniqueitemsWithAnArrayOfItemsTest {
    static final SchemaConfiguration configuration = new SchemaConfiguration(JsonSchemaKeywordFlags.onlyFormat());

    @Test
    public void testTrueTrueFromItemsArrayIsNotValidFails() {
        // [true, true] from items array is not valid
        final var schema = UniqueitemsWithAnArrayOfItems.UniqueitemsWithAnArrayOfItems1.getInstance();
        try {
            schema.validate(
                Arrays.asList(
                    true,
                    true
                ),
                configuration
            );
            throw new RuntimeException("A different exception must be thrown");
        } catch (ValidationException | InvalidTypeException ignored) {
            ;
        }
    }

    @Test
    public void testUniqueArrayExtendedFromFalseTrueIsValidPasses() {
        // unique array extended from [false, true] is valid
        final var schema = UniqueitemsWithAnArrayOfItems.UniqueitemsWithAnArrayOfItems1.getInstance();
        schema.validate(
            Arrays.asList(
                false,
                true,
                "foo",
                "bar"
            ),
            configuration
        );
    }

    @Test
    public void testFalseFalseFromItemsArrayIsNotValidFails() {
        // [false, false] from items array is not valid
        final var schema = UniqueitemsWithAnArrayOfItems.UniqueitemsWithAnArrayOfItems1.getInstance();
        try {
            schema.validate(
                Arrays.asList(
                    false,
                    false
                ),
                configuration
            );
            throw new RuntimeException("A different exception must be thrown");
        } catch (ValidationException | InvalidTypeException ignored) {
            ;
        }
    }

    @Test
    public void testUniqueArrayExtendedFromTrueFalseIsValidPasses() {
        // unique array extended from [true, false] is valid
        final var schema = UniqueitemsWithAnArrayOfItems.UniqueitemsWithAnArrayOfItems1.getInstance();
        schema.validate(
            Arrays.asList(
                true,
                false,
                "foo",
                "bar"
            ),
            configuration
        );
    }

    @Test
    public void testNonUniqueArrayExtendedFromFalseTrueIsNotValidFails() {
        // non-unique array extended from [false, true] is not valid
        final var schema = UniqueitemsWithAnArrayOfItems.UniqueitemsWithAnArrayOfItems1.getInstance();
        try {
            schema.validate(
                Arrays.asList(
                    false,
                    true,
                    "foo",
                    "foo"
                ),
                configuration
            );
            throw new RuntimeException("A different exception must be thrown");
        } catch (ValidationException | InvalidTypeException ignored) {
            ;
        }
    }

    @Test
    public void testNonUniqueArrayExtendedFromTrueFalseIsNotValidFails() {
        // non-unique array extended from [true, false] is not valid
        final var schema = UniqueitemsWithAnArrayOfItems.UniqueitemsWithAnArrayOfItems1.getInstance();
        try {
            schema.validate(
                Arrays.asList(
                    true,
                    false,
                    "foo",
                    "foo"
                ),
                configuration
            );
            throw new RuntimeException("A different exception must be thrown");
        } catch (ValidationException | InvalidTypeException ignored) {
            ;
        }
    }

    @Test
    public void testFalseTrueFromItemsArrayIsValidPasses() {
        // [false, true] from items array is valid
        final var schema = UniqueitemsWithAnArrayOfItems.UniqueitemsWithAnArrayOfItems1.getInstance();
        schema.validate(
            Arrays.asList(
                false,
                true
            ),
            configuration
        );
    }

    @Test
    public void testTrueFalseFromItemsArrayIsValidPasses() {
        // [true, false] from items array is valid
        final var schema = UniqueitemsWithAnArrayOfItems.UniqueitemsWithAnArrayOfItems1.getInstance();
        schema.validate(
            Arrays.asList(
                true,
                false
            ),
            configuration
        );
    }
}
