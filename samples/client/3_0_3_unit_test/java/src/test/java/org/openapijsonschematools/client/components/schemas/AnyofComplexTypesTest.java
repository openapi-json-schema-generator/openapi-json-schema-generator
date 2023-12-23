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
import org.checkerframework.checker.nullness.qual.Nullable;

import java.util.Arrays;
import java.util.List;
import java.util.Map;
import java.util.AbstractMap;
import java.util.LinkedHashSet;

public class AnyofComplexTypesTest {
    static final SchemaConfiguration configuration = new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone());
    static final ValidationMetadata validationMetadata = new ValidationMetadata(
            List.of("args[0"),
            configuration,
            new PathToSchemasMap(),
            new LinkedHashSet<>()
    );

    @Test
    public void testSecondAnyofValidComplexPasses() {
        // second anyOf valid (complex)
        final var schema = AnyofComplexTypes.AnyofComplexTypes1.getInstance();
        schema.validate(
            MapMaker.makeMap(
                new AbstractMap.SimpleEntry<String, String>(
                    "foo",
                    "baz"
                )
            ),
            configuration
        );
    }

    @Test
    public void testBothAnyofValidComplexPasses() {
        // both anyOf valid (complex)
        final var schema = AnyofComplexTypes.AnyofComplexTypes1.getInstance();
        schema.validate(
            MapMaker.makeMap(
                new AbstractMap.SimpleEntry<String, Object>(
                    "foo",
                    "baz"
                ),
                new AbstractMap.SimpleEntry<String, Object>(
                    "bar",
                    2L
                )
            ),
            configuration
        );
    }

    @Test
    public void testFirstAnyofValidComplexPasses() {
        // first anyOf valid (complex)
        final var schema = AnyofComplexTypes.AnyofComplexTypes1.getInstance();
        schema.validate(
            MapMaker.makeMap(
                new AbstractMap.SimpleEntry<String, Long>(
                    "bar",
                    2L
                )
            ),
            configuration
        );
    }

    @Test
    public void testNeitherAnyofValidComplexFails() {
        // neither anyOf valid (complex)
        final var schema = AnyofComplexTypes.AnyofComplexTypes1.getInstance();
        Assert.assertThrows(ValidationException.class, () -> JsonSchema.validate(
            schema,
            MapMaker.makeMap(
                new AbstractMap.SimpleEntry<String, Object>(
                    "foo",
                    2L
                ),
                new AbstractMap.SimpleEntry<String, Object>(
                    "bar",
                    "quux"
                )
            ),
            validationMetadata
        ));
    }
}
