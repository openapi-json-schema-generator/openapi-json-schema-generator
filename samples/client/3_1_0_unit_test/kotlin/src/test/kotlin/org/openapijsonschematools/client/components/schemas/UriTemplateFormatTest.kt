package org.openapijsonschematools.client.components.schemas

import org.openapijsonschematools.client.configurations.JsonSchemaKeywordFlags
import org.openapijsonschematools.client.configurations.SchemaConfiguration
import org.openapijsonschematools.client.exceptions.ValidationException

import kotlin.test.Test
import kotlin.test.assertFailsWith

class UriTemplateFormatTest {
    companion object {
        val configuration = SchemaConfiguration(JsonSchemaKeywordFlags.Builder().format().build())
    }

    @Test
    fun testAllStringFormatsIgnoreIntegersPasses() {
        // all string formats ignore integers
        val schema = UriTemplateFormat.UriTemplateFormat1.getInstance()
        schema.validate(
            12,
            configuration
        )
    }

    @Test
    fun testAllStringFormatsIgnoreNullsPasses() {
        // all string formats ignore nulls
        val schema = UriTemplateFormat.UriTemplateFormat1.getInstance()
        schema.validate(
            null,
            configuration
        )
    }

    @Test
    fun testAllStringFormatsIgnoreObjectsPasses() {
        // all string formats ignore objects
        val schema = UriTemplateFormat.UriTemplateFormat1.getInstance()
        schema.validate(
            mapOf<Any?, Any?>(
            ),
            configuration
        )
    }

    @Test
    fun testAllStringFormatsIgnoreFloatsPasses() {
        // all string formats ignore floats
        val schema = UriTemplateFormat.UriTemplateFormat1.getInstance()
        schema.validate(
            13.7,
            configuration
        )
    }

    @Test
    fun testAllStringFormatsIgnoreArraysPasses() {
        // all string formats ignore arrays
        val schema = UriTemplateFormat.UriTemplateFormat1.getInstance()
        schema.validate(
            listOf<Any?>(
            ),
            configuration
        )
    }

    @Test
    fun testAllStringFormatsIgnoreBooleansPasses() {
        // all string formats ignore booleans
        val schema = UriTemplateFormat.UriTemplateFormat1.getInstance()
        schema.validate(
            false,
            configuration
        )
    }

    @Test
    fun testInvalidUriTemplateStringIsOnlyAnAnnotationByDefaultPasses() {
        // invalid uri-template string is only an annotation by default
        val schema = UriTemplateFormat.UriTemplateFormat1.getInstance()
        schema.validate(
            "http://example.com/dictionary/{term:1}/{term",
            configuration
        )
    }
}
