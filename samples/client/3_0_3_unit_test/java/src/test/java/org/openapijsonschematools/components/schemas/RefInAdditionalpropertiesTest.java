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

public class RefInAdditionalpropertiesTest {
    static final SchemaConfiguration configuration = new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone());

    @Test
    public void testPropertyNamedRefValidPasses() {
        // property named $ref valid
        RefInAdditionalproperties.RefInAdditionalproperties1.validate(
            MapMaker.makeMap(
                new AbstractMap.SimpleEntry<>(
                    "someProp",
                    MapMaker.makeMap(
                        new AbstractMap.SimpleEntry<>(
                            "$ref",
                            "a"
                        )
                    )
                )
            ),
            configuration
        );
    }

    @Test
    public void testPropertyNamedRefInvalidFails() {
        // property named $ref invalid
        Assert.assertThrows(ValidationException.class, () -> JsonSchema.validateObject(
            RefInAdditionalproperties.RefInAdditionalproperties1.class,
            MapMaker.makeMap(
                new AbstractMap.SimpleEntry<>(
                    "someProp",
                    MapMaker.makeMap(
                        new AbstractMap.SimpleEntry<>(
                            "$ref",
                            2
                        )
                    )
                )
            ),
            configuration
        ));
    }
}
