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

public class InvalidStringValueForDefaultTest {
    static final SchemaConfiguration configuration = new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone());

    @Test
    public void testValidWhenPropertyIsSpecifiedPasses() {
        // valid when property is specified
        InvalidStringValueForDefault.InvalidStringValueForDefault1.validate(
            MapMaker.makeMap(
                new AbstractMap.SimpleEntry<>(
                    "bar",
                    "good"
                )
            ),
            configuration
        );
    }

    @Test
    public void testStillValidWhenTheInvalidDefaultIsUsedPasses() {
        // still valid when the invalid default is used
        InvalidStringValueForDefault.InvalidStringValueForDefault1.validate(
            MapMaker.makeMap(
            ),
            configuration
        );
    }
}
