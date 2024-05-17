package org.openapijsonschematools.client.components.schemas

import org.openapijsonschematools.client.configurations.JsonSchemaKeywordFlags
import org.openapijsonschematools.client.configurations.SchemaConfiguration
import org.openapijsonschematools.client.exceptions.ValidationException

import kotlin.test.Test
import kotlin.test.assertFailsWith

class AllofWithTwoEmptySchemasTest {
    companion object {
        val configuration = SchemaConfiguration(JsonSchemaKeywordFlags.Builder().format().build())
    }

    @Test
    fun testAnyDataIsValidPasses() {
        // any data is valid
        val schema = AllofWithTwoEmptySchemas.AllofWithTwoEmptySchemas1.getInstance()
        schema.validate(
            1,
            configuration
        )
    }
}
