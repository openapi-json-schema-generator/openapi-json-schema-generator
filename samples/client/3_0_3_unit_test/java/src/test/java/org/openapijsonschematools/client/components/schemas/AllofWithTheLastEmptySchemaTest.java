package org.openapijsonschematools.client.components.schemas;

import org.junit.Test;
import org.openapijsonschematools.client.configurations.JsonSchemaKeywordFlags;
import org.openapijsonschematools.client.configurations.SchemaConfiguration;
import org.openapijsonschematools.client.exceptions.ValidationException;
import org.openapijsonschematools.client.exceptions.InvalidTypeException;

public class AllofWithTheLastEmptySchemaTest {
    static final SchemaConfiguration configuration = new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone());

    @Test
    public void testStringIsInvalidFails() {
        // string is invalid
        final var schema = AllofWithTheLastEmptySchema.AllofWithTheLastEmptySchema1.getInstance();
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
    public void testNumberIsValidPasses() {
        // number is valid
        final var schema = AllofWithTheLastEmptySchema.AllofWithTheLastEmptySchema1.getInstance();
        schema.validate(
            1,
            configuration
        );
    }
}
