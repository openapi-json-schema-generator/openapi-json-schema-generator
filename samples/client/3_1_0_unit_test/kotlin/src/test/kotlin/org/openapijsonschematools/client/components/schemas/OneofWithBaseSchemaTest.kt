package org.openapijsonschematools.client.components.schemas

import org.openapijsonschematools.client.configurations.JsonSchemaKeywordFlags
import org.openapijsonschematools.client.configurations.SchemaConfiguration
import org.openapijsonschematools.client.exceptions.ValidationException

import kotlin.test.Test
import kotlin.test.assertFailsWith

class OneofWithBaseSchemaTest {
    companion object {
        val configuration = SchemaConfiguration(JsonSchemaKeywordFlags.Builder().format().build())
    }

    @Test
    fun testMismatchBaseSchemaFails() {
        // mismatch base schema
        val schema = OneofWithBaseSchema.OneofWithBaseSchema1.getInstance()
        assertFailsWith<ValidationException>(
            block = {
                schema.validate(
                    3,
                    configuration
                )
            }
        )
    }

    @Test
    fun testOneOneofValidPasses() {
        // one oneOf valid
        val schema = OneofWithBaseSchema.OneofWithBaseSchema1.getInstance()
        schema.validate(
            "foobar",
            configuration
        )
    }

    @Test
    fun testBothOneofValidFails() {
        // both oneOf valid
        val schema = OneofWithBaseSchema.OneofWithBaseSchema1.getInstance()
        assertFailsWith<ValidationException>(
            block = {
                schema.validate(
                    "foo",
                    configuration
                )
            }
        )
    }
}
