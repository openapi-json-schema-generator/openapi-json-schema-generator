package unit_test_api.components.schemas;

import org.junit.Assert;
import org.junit.Test;
import unit_test_api.configurations.JsonSchemaKeywordFlags;
import unit_test_api.configurations.SchemaConfiguration;
import unit_test_api.exceptions.ValidationException;
import unit_test_api.schemas.validation.MapUtils;
import org.checkerframework.checker.nullness.qual.Nullable;

import java.util.Arrays;
import java.util.List;
import java.util.Map;
import java.util.AbstractMap;

public class TypeAsArrayWithOneItemTest {
    static final SchemaConfiguration configuration = new SchemaConfiguration(new JsonSchemaKeywordFlags.Builder().format().build());

    @Test
    public void testNumberIsInvalidFails() {
        // number is invalid
        final var schema = TypeAsArrayWithOneItem.TypeAsArrayWithOneItem1.getInstance();
        try {
            schema.validate(
                123,
                configuration
            );
            throw new RuntimeException("A different exception must be thrown");
        } catch (ValidationException ignored) {
            ;
        }
    }

    @Test
    public void testStringIsValidPasses() throws ValidationException {
        // string is valid
        final var schema = TypeAsArrayWithOneItem.TypeAsArrayWithOneItem1.getInstance();
        schema.validate(
            "foo",
            configuration
        );
    }
}
