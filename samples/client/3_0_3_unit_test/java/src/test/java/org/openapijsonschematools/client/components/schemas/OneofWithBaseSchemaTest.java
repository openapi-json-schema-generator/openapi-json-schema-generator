package org.openapijsonschematools.client.components.schemas;

import org.junit.Test;
import org.openapijsonschematools.client.configurations.JsonSchemaKeywordFlags;
import org.openapijsonschematools.client.configurations.SchemaConfiguration;
import org.openapijsonschematools.client.exceptions.ValidationException;
import org.openapijsonschematools.client.exceptions.InvalidTypeException;

public class OneofWithBaseSchemaTest {
    static final SchemaConfiguration configuration = new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone());

    @Test
    public void testMismatchBaseSchemaFails() {
        // mismatch base schema
        final var schema = OneofWithBaseSchema.OneofWithBaseSchema1.getInstance();
        try {
            schema.validate(
                3,
                configuration
            );
            throw new RuntimeException("A different exception must be thrown");
        } catch (ValidationException | InvalidTypeException ignored) {
            ;
        }
    }

    @Test
    public void testOneOneofValidPasses() {
        // one oneOf valid
        final var schema = OneofWithBaseSchema.OneofWithBaseSchema1.getInstance();
        schema.validate(
            "foobar",
            configuration
        );
    }

    @Test
    public void testBothOneofValidFails() {
        // both oneOf valid
        final var schema = OneofWithBaseSchema.OneofWithBaseSchema1.getInstance();
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
}
