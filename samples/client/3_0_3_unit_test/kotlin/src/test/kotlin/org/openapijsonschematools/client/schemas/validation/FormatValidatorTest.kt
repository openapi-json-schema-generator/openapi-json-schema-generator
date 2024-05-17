package org.openapijsonschematools.client.schemas.validation

import org.openapijsonschematools.client.configurations.JsonSchemaKeywordFlags
import org.openapijsonschematools.client.configurations.SchemaConfiguration
import org.openapijsonschematools.client.exceptions.ValidationException
import org.openapijsonschematools.client.schemas.IntJsonSchema
import org.openapijsonschematools.client.schemas.Int32JsonSchema
import org.openapijsonschematools.client.schemas.Int64JsonSchema
import org.openapijsonschematools.client.schemas.FloatJsonSchema
import org.openapijsonschematools.client.schemas.DoubleJsonSchema
import org.openapijsonschematools.client.schemas.DecimalJsonSchema
import org.openapijsonschematools.client.schemas.DateJsonSchema
import org.openapijsonschematools.client.schemas.DateTimeJsonSchema

import java.math.BigDecimal
import java.math.BigInteger
import kotlin.test.Test
import kotlin.test.assertFailsWith
import kotlin.test.assertNull

class FormatValidatorTest {
    @Test
    @Throws(ValidationException::class)
    fun testIntFormatSucceedsWithFloat() {
        val validator = FormatValidator()
        val pathToSchemasMap = validator.validate(
            ValidationData(
                IntJsonSchema.IntJsonSchema1.getInstance(),
                1.0f,
                validationMetadata
            )
        )
        assertNull(pathToSchemasMap)
    }

    @Test
    fun testIntFormatFailsWithFloat() {
        val validator = FormatValidator()
        assertFailsWith<ValidationException>(
            block = {
                validator.validate(
                    ValidationData(
                        IntJsonSchema.IntJsonSchema1.getInstance(),
                        3.14f,
                        validationMetadata
                    )
                )
            }
        )
    }

    @Test
    @Throws(ValidationException::class)
    fun testIntFormatSucceedsWithInt() {
        val validator = FormatValidator()
        val pathToSchemasMap = validator.validate(
            ValidationData(
                IntJsonSchema.IntJsonSchema1.getInstance(),
                1,
                validationMetadata
            )
        )
        assertNull(pathToSchemasMap)
    }

    @Test
    fun testInt32UnderMinFails() {
        val validator = FormatValidator()
        assertFailsWith<ValidationException>(
            block = {
                validator.validate(
                    ValidationData(
                        Int32JsonSchema.Int32JsonSchema1.getInstance(),
                        -2147483649L,
                        validationMetadata
                    )
                )
            }
        )
    }

    @Test
    @Throws(ValidationException::class)
    fun testInt32InclusiveMinSucceeds() {
        val validator = FormatValidator()
        val pathToSchemasMap = validator.validate(
            ValidationData(
                Int32JsonSchema.Int32JsonSchema1.getInstance(),
                -2147483648,
                validationMetadata
            )
        )
        assertNull(pathToSchemasMap)
    }

    @Test
    @Throws(ValidationException::class)
    fun testInt32InclusiveMaxSucceeds() {
        val validator = FormatValidator()
        val pathToSchemasMap = validator.validate(
            ValidationData(
                Int32JsonSchema.Int32JsonSchema1.getInstance(),
                2147483647,
                validationMetadata
            )
        )
        assertNull(pathToSchemasMap)
    }

    @Test
    fun testInt32OverMaxFails() {
        val validator = FormatValidator()
        assertFailsWith<ValidationException>(
            block = {
                validator.validate(
                    ValidationData(
                        Int32JsonSchema.Int32JsonSchema1.getInstance(),
                        2147483648L,
                        validationMetadata
                    )
                )
            }
        )
    }

    @Test
    fun testInt64UnderMinFails() {
        val validator = FormatValidator()
        assertFailsWith<ValidationException>(
            block = {
                validator.validate(
                    ValidationData(
                        Int64JsonSchema.Int64JsonSchema1.getInstance(),
                        BigInteger("-9223372036854775809"),
                        validationMetadata
                    )
                )
            }
        )
    }

    @Test
    @Throws(ValidationException::class)
    fun testInt64InclusiveMinSucceeds() {
        val validator = FormatValidator()
        val pathToSchemasMap = validator.validate(
            ValidationData(
                Int64JsonSchema.Int64JsonSchema1.getInstance(),
                Long.MIN_VALUE,
                validationMetadata
            )
        )
        assertNull(pathToSchemasMap)
    }

    @Test
    @Throws(ValidationException::class)
    fun testInt64InclusiveMaxSucceeds() {
        val validator = FormatValidator()
        val pathToSchemasMap = validator.validate(
            ValidationData(
                Int64JsonSchema.Int64JsonSchema1.getInstance(),
                9223372036854775807L,
                validationMetadata
            )
        )
        assertNull(pathToSchemasMap)
    }

    @Test
    fun testInt64OverMaxFails() {
        val validator = FormatValidator()
        assertFailsWith<ValidationException>(
            block = {
                validator.validate(
                    ValidationData(
                        Int64JsonSchema.Int64JsonSchema1.getInstance(),
                        BigInteger("9223372036854775808"),
                        validationMetadata
                    )
                )
            }
        )
    }

    @Test
    fun testFloatUnderMinFails() {
        val validator = FormatValidator()
        assertFailsWith<ValidationException>(
            block = {
                validator.validate(
                    ValidationData(
                        FloatJsonSchema.FloatJsonSchema1.getInstance(),
                        -3.402823466385289e+38,
                        validationMetadata
                    )
                )
            }
        )
    }

    @Test
    @Throws(ValidationException::class)
    fun testFloatInclusiveMinSucceeds() {
        val validator = FormatValidator()
        val pathToSchemasMap = validator.validate(
            ValidationData(
                FloatJsonSchema.FloatJsonSchema1.getInstance(),
                Float.MIN_VALUE,
                validationMetadata
            )
        )
        assertNull(pathToSchemasMap)
    }

    @Test
    @Throws(ValidationException::class)
    fun testFloatInclusiveMaxSucceeds() {
        val validator = FormatValidator()
        val pathToSchemasMap = validator.validate(
            ValidationData(
                FloatJsonSchema.FloatJsonSchema1.getInstance(),
                Float.MAX_VALUE,
                validationMetadata
            )
        )
        assertNull(pathToSchemasMap)
    }

    @Test
    fun testFloatOverMaxFails() {
        val validator = FormatValidator()
        assertFailsWith<ValidationException>(
            block = {
                validator.validate(
                    ValidationData(
                        FloatJsonSchema.FloatJsonSchema1.getInstance(),
                        3.402823466385289e+38,
                        validationMetadata
                    )
                )
            }
        )
    }

    @Test
    fun testDoubleUnderMinFails() {
        val validator = FormatValidator()
        assertFailsWith<ValidationException>(
            block = {
                validator.validate(
                    ValidationData(
                        DoubleJsonSchema.DoubleJsonSchema1.getInstance(),
                        BigDecimal("-1.7976931348623157082e+308"),
                        validationMetadata
                    )
                )
            }
        )
    }

    @Test
    @Throws(ValidationException::class)
    fun testDoubleInclusiveMinSucceeds() {
        val validator = FormatValidator()
        val pathToSchemasMap = validator.validate(
            ValidationData(
                DoubleJsonSchema.DoubleJsonSchema1.getInstance(),
                -1.7976931348623157E+308,
                validationMetadata
            )
        )
        assertNull(pathToSchemasMap)
    }

    @Test
    @Throws(ValidationException::class)
    fun testDoubleInclusiveMaxSucceeds() {
        val validator = FormatValidator()
        val pathToSchemasMap = validator.validate(
            ValidationData(
                DoubleJsonSchema.DoubleJsonSchema1.getInstance(),
                1.7976931348623157E+308,
                validationMetadata
            )
        )
        assertNull(pathToSchemasMap)
    }

    @Test
    fun testDoubleOverMaxFails() {
        val validator = FormatValidator()
        assertFailsWith<ValidationException>(
            block = {
                validator.validate(
                    ValidationData(
                        DoubleJsonSchema.DoubleJsonSchema1.getInstance(),
                        BigDecimal("1.7976931348623157082e+308"),
                        validationMetadata
                    )
                )
            }
        )
    }

    @Test
    fun testInvalidNumberStringFails() {
        val validator = FormatValidator()
        assertFailsWith<ValidationException>(
            block = {
                validator.validate(
                    ValidationData(
                        DecimalJsonSchema.DecimalJsonSchema1.getInstance(),
                        "abc",
                        validationMetadata
                    )
                )
            }
        )
    }

    @Test
    @Throws(ValidationException::class)
    fun testValidFloatNumberStringSucceeds() {
        val validator = FormatValidator()
        val pathToSchemasMap = validator.validate(
            ValidationData(
                DecimalJsonSchema.DecimalJsonSchema1.getInstance(),
                "3.14",
                validationMetadata
            )
        )
        assertNull(pathToSchemasMap)
    }

    @Test
    @Throws(ValidationException::class)
    fun testValidIntNumberStringSucceeds() {
        val validator = FormatValidator()
        val pathToSchemasMap = validator.validate(
            ValidationData(
                DecimalJsonSchema.DecimalJsonSchema1.getInstance(),
                "1",
                validationMetadata
            )
        )
        assertNull(pathToSchemasMap)
    }

    @Test
    fun testInvalidDateStringFails() {
        val validator = FormatValidator()
        assertFailsWith<ValidationException>(
            block = {
                validator.validate(
                    ValidationData(
                        DateJsonSchema.DateJsonSchema1.getInstance(),
                        "abc",
                        validationMetadata
                    )
                )
            }
        )
    }

    @Test
    @Throws(ValidationException::class)
    fun testValidDateStringSucceeds() {
        val validator = FormatValidator()
        val pathToSchemasMap = validator.validate(
            ValidationData(
                DateJsonSchema.DateJsonSchema1.getInstance(),
                "2017-01-20",
                validationMetadata
            )
        )
        assertNull(pathToSchemasMap)
    }

    @Test
    fun testInvalidDateTimeStringFails() {
        val validator = FormatValidator()
        assertFailsWith<ValidationException>(
            block = {
                validator.validate(
                    ValidationData(
                        DateTimeJsonSchema.DateTimeJsonSchema1.getInstance(),
                        "abc",
                        validationMetadata
                    )
                )
            }
        )
    }

    @Test
    @Throws(ValidationException::class)
    fun testValidDateTimeStringSucceeds() {
        val validator = FormatValidator()
        val pathToSchemasMap = validator.validate(
            ValidationData(
                DateTimeJsonSchema.DateTimeJsonSchema1.getInstance(),
                "2017-07-21T17:32:28Z",
                validationMetadata
            )
        )
        assertNull(pathToSchemasMap)
    }

    companion object {
        val validationMetadata = ValidationMetadata(
            ArrayList(),
            SchemaConfiguration(JsonSchemaKeywordFlags.Builder().build()),
            PathToSchemasMap(),
            LinkedHashSet()
        )
    }
}