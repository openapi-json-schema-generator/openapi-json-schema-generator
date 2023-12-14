package org.openapijsonschematools.client.components.schemas;

import org.junit.Assert;
import org.junit.Test;
import org.openapijsonschematools.client.configurations.JsonSchemaKeywordFlags;
import org.openapijsonschematools.client.configurations.SchemaConfiguration;
import org.openapijsonschematools.client.exceptions.ValidationException;
import org.openapijsonschematools.client.schemas.MapMaker;
import org.openapijsonschematools.client.schemas.validation.JsonSchema;
import org.openapijsonschematools.client.schemas.validation.FrozenMap;
import org.openapijsonschematools.client.schemas.validation.FrozenList;
import org.openapijsonschematools.client.schemas.validation.PathToSchemasMap;
import org.openapijsonschematools.client.schemas.validation.ValidationMetadata;

import java.util.Arrays;
import java.util.List;
import java.util.AbstractMap;
import java.util.LinkedHashSet;

public class AnyofTest {
    static final SchemaConfiguration configuration = new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone());
    static final ValidationMetadata validationMetadata = new ValidationMetadata(
            List.of("args[0"),
            configuration,
            new PathToSchemasMap(),
            new LinkedHashSet<>()
    );

    @Test
    public void testBothAnyofValidPasses() {
        // both anyOf valid
        final var schema = Anyof.Anyof1.getInstance();
        schema.validate(
            3,
            configuration
        );
    }

    @Test
    public void testNeitherAnyofValidFails() {
        // neither anyOf valid
        final var schema = Anyof.Anyof1.getInstance();
        Assert.assertThrows(ValidationException.class, () -> JsonSchema.validate(
            schema,
            1.5d,
            validationMetadata
        ));
    }

    @Test
    public void testFirstAnyofValidPasses() {
        // first anyOf valid
        final var schema = Anyof.Anyof1.getInstance();
        schema.validate(
            1,
            configuration
        );
    }

    @Test
    public void testSecondAnyofValidPasses() {
        // second anyOf valid
        final var schema = Anyof.Anyof1.getInstance();
        schema.validate(
            2.5d,
            configuration
        );
    }
}
