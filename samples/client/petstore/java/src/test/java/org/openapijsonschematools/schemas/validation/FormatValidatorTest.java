package org.openapijsonschematools.schemas.validation;

import org.junit.Assert;
import org.junit.Test;
import org.openapijsonschematools.configurations.JsonSchemaKeywordFlags;
import org.openapijsonschematools.configurations.SchemaConfiguration;

import java.math.BigDecimal;
import java.math.BigInteger;
import java.util.ArrayList;
import java.util.LinkedHashSet;

public class FormatValidatorTest {
    static final ValidationMetadata validationMetadata = new ValidationMetadata(
            new ArrayList<>(),
            new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone()),
            new PathToSchemasMap(),
            new LinkedHashSet<>()
    );

    @Test
    public void testIntFormatSucceedsWithFloat() {
        final FormatValidator validator = new FormatValidator();
        PathToSchemasMap pathToSchemasMap = validator.validate(
                JsonSchema.class,
                1.0f,
                "int",
                validationMetadata,
                null
        );
        Assert.assertNull(pathToSchemasMap);
    }

    @Test
    public void testIntFormatFailsWithFloat() {
        final FormatValidator validator = new FormatValidator();
        Assert.assertThrows(RuntimeException.class, () -> validator.validate(
                JsonSchema.class,
                3.14f,
                "int",
                validationMetadata,
                null
        ));
    }

    @Test
    public void testIntFormatSucceedsWithInt() {
        final FormatValidator validator = new FormatValidator();
        PathToSchemasMap pathToSchemasMap = validator.validate(
                JsonSchema.class,
                1,
                "int",
                validationMetadata,
                null
        );
        Assert.assertNull(pathToSchemasMap);
    }

    @Test
    public void testInt32UnderMinFails() {
        final FormatValidator validator = new FormatValidator();
        Assert.assertThrows(RuntimeException.class, () -> validator.validate(
                JsonSchema.class,
                -2147483649L,
                "int32",
                validationMetadata,
                null
        ));
    }

    @Test
    public void testInt32InclusiveMinSucceeds() {
        final FormatValidator validator = new FormatValidator();
        PathToSchemasMap pathToSchemasMap = validator.validate(
                JsonSchema.class,
                -2147483648,
                "int32",
                validationMetadata,
                null
        );
        Assert.assertNull(pathToSchemasMap);
    }

    @Test
    public void testInt32InclusiveMaxSucceeds() {
        final FormatValidator validator = new FormatValidator();
        PathToSchemasMap pathToSchemasMap = validator.validate(
                JsonSchema.class,
                2147483647,
                "int32",
                validationMetadata,
                null
        );
        Assert.assertNull(pathToSchemasMap);
    }

    @Test
    public void testInt32OverMaxFails() {
        final FormatValidator validator = new FormatValidator();
        Assert.assertThrows(RuntimeException.class, () -> validator.validate(
                JsonSchema.class,
                2147483648L,
                "int32",
                validationMetadata,
                null
        ));
    }

    @Test
    public void testInt64UnderMinFails() {
        final FormatValidator validator = new FormatValidator();

        Assert.assertThrows(RuntimeException.class, () -> validator.validate(
                JsonSchema.class,
                new BigInteger("-9223372036854775809"),
                "int64",
                validationMetadata,
                null
        ));
    }

    @Test
    public void testInt64InclusiveMinSucceeds() {
        final FormatValidator validator = new FormatValidator();
        PathToSchemasMap pathToSchemasMap = validator.validate(
                JsonSchema.class,
                -9223372036854775808L,
                "int64",
                validationMetadata,
                null
        );
        Assert.assertNull(pathToSchemasMap);
    }

    @Test
    public void testInt64InclusiveMaxSucceeds() {
        final FormatValidator validator = new FormatValidator();
        PathToSchemasMap pathToSchemasMap = validator.validate(
                JsonSchema.class,
                9223372036854775807L,
                "int64",
                validationMetadata,
                null
        );
        Assert.assertNull(pathToSchemasMap);
    }

    @Test
    public void testInt64OverMaxFails() {
        final FormatValidator validator = new FormatValidator();

        Assert.assertThrows(RuntimeException.class, () -> validator.validate(
                JsonSchema.class,
                new BigInteger("9223372036854775808"),
                "int64",
                validationMetadata,
                null
        ));
    }

    @Test
    public void testFloatUnderMinFails() {
        final FormatValidator validator = new FormatValidator();
        Assert.assertThrows(RuntimeException.class, () -> validator.validate(
                JsonSchema.class,
                -3.402823466385289e+38d,
                "float",
                validationMetadata,
                null
        ));
    }

    @Test
    public void testFloatInclusiveMinSucceeds() {
        final FormatValidator validator = new FormatValidator();
        PathToSchemasMap pathToSchemasMap = validator.validate(
                JsonSchema.class,
                -3.4028234663852886e+38f,
                "float",
                validationMetadata,
                null
        );
        Assert.assertNull(pathToSchemasMap);
    }

    @Test
    public void testFloatInclusiveMaxSucceeds() {
        final FormatValidator validator = new FormatValidator();
        PathToSchemasMap pathToSchemasMap = validator.validate(
                JsonSchema.class,
                3.4028234663852886e+38f,
                "float",
                validationMetadata,
                null
        );
        Assert.assertNull(pathToSchemasMap);
    }

    @Test
    public void testFloatOverMaxFails() {
        final FormatValidator validator = new FormatValidator();
        Assert.assertThrows(RuntimeException.class, () -> validator.validate(
                JsonSchema.class,
                3.402823466385289e+38d,
                "float",
                validationMetadata,
                null
        ));
    }

    @Test
    public void testDoubleUnderMinFails() {
        final FormatValidator validator = new FormatValidator();
        Assert.assertThrows(RuntimeException.class, () -> validator.validate(
                JsonSchema.class,
                new BigDecimal("-1.7976931348623157082e+308"),
                "double",
                validationMetadata,
                null
        ));
    }

    @Test
    public void testDoubleInclusiveMinSucceeds() {
        final FormatValidator validator = new FormatValidator();
        PathToSchemasMap pathToSchemasMap = validator.validate(
                JsonSchema.class,
                -1.7976931348623157E+308d,
                "double",
                validationMetadata,
                null
        );
        Assert.assertNull(pathToSchemasMap);
    }

    @Test
    public void testDoubleInclusiveMaxSucceeds() {
        final FormatValidator validator = new FormatValidator();
        PathToSchemasMap pathToSchemasMap = validator.validate(
                JsonSchema.class,
                1.7976931348623157E+308d,
                "double",
                validationMetadata,
                null
        );
        Assert.assertNull(pathToSchemasMap);
    }

    @Test
    public void testDoubleOverMaxFails() {
        final FormatValidator validator = new FormatValidator();
        Assert.assertThrows(RuntimeException.class, () -> validator.validate(
                JsonSchema.class,
                new BigDecimal("1.7976931348623157082e+308"),
                "double",
                validationMetadata,
                null
        ));
    }

    @Test
    public void testInvalidNumberStringFails() {
        final FormatValidator validator = new FormatValidator();
        Assert.assertThrows(RuntimeException.class, () -> validator.validate(
                JsonSchema.class,
                "abc",
                "number",
                validationMetadata,
                null
        ));
    }

    @Test
    public void testValidFloatNumberStringSucceeds() {
        final FormatValidator validator = new FormatValidator();
        PathToSchemasMap pathToSchemasMap = validator.validate(
                JsonSchema.class,
                "3.14",
                "number",
                validationMetadata,
                null
        );
        Assert.assertNull(pathToSchemasMap);
    }

    @Test
    public void testValidIntNumberStringSucceeds() {
        final FormatValidator validator = new FormatValidator();
        PathToSchemasMap pathToSchemasMap = validator.validate(
                JsonSchema.class,
                "1",
                "number",
                validationMetadata,
                null
        );
        Assert.assertNull(pathToSchemasMap);
    }

    @Test
    public void testInvalidDateStringFails() {
        final FormatValidator validator = new FormatValidator();
        Assert.assertThrows(RuntimeException.class, () -> validator.validate(
                JsonSchema.class,
                "abc",
                "date",
                validationMetadata,
                null
        ));
    }

    @Test
    public void testValidDateStringSucceeds() {
        final FormatValidator validator = new FormatValidator();
        PathToSchemasMap pathToSchemasMap = validator.validate(
                JsonSchema.class,
                "2017-01-20",
                "date",
                validationMetadata,
                null
        );
        Assert.assertNull(pathToSchemasMap);
    }

    @Test
    public void testInvalidDateTimeStringFails() {
        final FormatValidator validator = new FormatValidator();
        Assert.assertThrows(RuntimeException.class, () -> validator.validate(
                JsonSchema.class,
                "abc",
                "date-time",
                validationMetadata,
                null
        ));
    }

    @Test
    public void testValidDateTimeStringSucceeds() {
        final FormatValidator validator = new FormatValidator();
        PathToSchemasMap pathToSchemasMap = validator.validate(
                JsonSchema.class,
                "2017-07-21T17:32:28Z",
                "date-time",
                validationMetadata,
                null
        );
        Assert.assertNull(pathToSchemasMap);
    }
}
