package org.openapijsonschematools.client.components.schemas

import org.openapijsonschematools.client.configurations.JsonSchemaKeywordFlags
import org.openapijsonschematools.client.configurations.SchemaConfiguration
import org.openapijsonschematools.client.exceptions.ValidationException

import kotlin.test.Test
import kotlin.test.assertFailsWith

class TypeArrayObjectOrNullTest {
    companion object {
        val configuration = SchemaConfiguration(JsonSchemaKeywordFlags.Builder().format().build())
    }

    @Test
    fun testNumberIsInvalidFails() {
        // number is invalid
        val schema = TypeArrayObjectOrNull.TypeArrayObjectOrNull1.getInstance()
        assertFailsWith<ValidationException>(
            block = {
                schema.validate(
                    123,
                    configuration
                )
            }
        )
    }

    @Test
    fun testNullIsValidPasses() {
        // null is valid
        val schema = TypeArrayObjectOrNull.TypeArrayObjectOrNull1.getInstance()
        schema.validate(
            null,
            configuration
        )
    }

    @Test
    fun testStringIsInvalidFails() {
        // string is invalid
        val schema = TypeArrayObjectOrNull.TypeArrayObjectOrNull1.getInstance()
        assertFailsWith<ValidationException>(
            block = {
                schema.validate(
                    "foo",
                    configuration
                )
            }
        )
    }

    @Test
    fun testArrayIsValidPasses() {
        // array is valid
        val schema = TypeArrayObjectOrNull.TypeArrayObjectOrNull1.getInstance()
        schema.validate(
            listOf(
                1,
                2,
                3
            ),
            configuration
        )
    }

    @Test
    fun testObjectIsValidPasses() {
        // object is valid
        val schema = TypeArrayObjectOrNull.TypeArrayObjectOrNull1.getInstance()
        schema.validate(
            mapOf(
                Pair(
                    "foo",
                    123
                )
            ),
            configuration
        )
    }
}
