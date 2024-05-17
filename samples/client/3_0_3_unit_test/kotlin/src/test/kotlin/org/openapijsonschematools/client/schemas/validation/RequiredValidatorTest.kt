package org.openapijsonschematools.client.schemas.validation

import org.openapijsonschematools.client.configurations.JsonSchemaKeywordFlags
import org.openapijsonschematools.client.configurations.SchemaConfiguration
import org.openapijsonschematools.client.exceptions.ValidationException

import kotlin.test.Test
import kotlin.test.assertFailsWith
import kotlin.test.assertNull

class RequiredValidatorTest {
    interface ObjectWithRequiredSchemaBoxed
    class ObjectWithRequiredSchemaBoxedMap : ObjectWithRequiredSchemaBoxed
    class ObjectWithRequiredSchema : JsonSchema<ObjectWithRequiredSchemaBoxed?>(
        JsonSchemaInfo()
            .type(setOf(Map::class.java))
            .required(setOf("someString"))
    ) {
        override fun getNewInstance(arg: Any?, pathToItem: List<Any>, pathToSchemas: PathToSchemasMap): Any? {
            if (arg is Map<*, *>) {
                return getNewInstance(arg, pathToItem, pathToSchemas)
            }
            throw RuntimeException("Invalid input type=$javaClass. It can't be instantiated by this schema")
        }

        @Throws(ValidationException::class)
        override fun validate(arg: Any?, configuration: SchemaConfiguration?): Any? {
            if (arg is Map<*, *>) {
                return validate(arg, configuration)
            }
            throw ValidationException("Invalid input type=$javaClass. It can't be validated by this schema")
        }

        @Throws(ValidationException::class)
        override fun validateAndBox(arg: Any?, configuration: SchemaConfiguration?): ObjectWithRequiredSchemaBoxed {
            return ObjectWithRequiredSchemaBoxedMap()
        }
    }

    @Test
    @Throws(ValidationException::class)
    fun testCorrectPropertySucceeds() {
        val pathToItem = listOf<Any>("args[0]")
        val validationMetadata = ValidationMetadata(
            pathToItem,
            SchemaConfiguration(JsonSchemaKeywordFlags.Builder().build()),
            PathToSchemasMap(),
            LinkedHashSet()
        )
        val mutableMap = LinkedHashMap<String, Any>()
        mutableMap["someString"] = "abc"
        val arg = FrozenMap(mutableMap)
        val validator = RequiredValidator()
        val pathToSchemas = validator.validate(
            ValidationData(
                ObjectWithRequiredSchema(),
                arg,
                validationMetadata
            )
        )
        assertNull(pathToSchemas)
    }

    @Test
    @Throws(ValidationException::class)
    fun testNotApplicableTypeReturnsNull() {
        val pathToItem = listOf<Any>("args[0]")
        val validationMetadata = ValidationMetadata(
            pathToItem,
            SchemaConfiguration(JsonSchemaKeywordFlags.Builder().build()),
            PathToSchemasMap(),
            LinkedHashSet()
        )
        val validator = RequiredValidator()
        val pathToSchemas = validator.validate(
            ValidationData(
                ObjectWithRequiredSchema(),
                1,
                validationMetadata
            )
        )
        assertNull(pathToSchemas)
    }

    @Test
    fun testIncorrectPropertyFails() {
        val pathToItem = listOf<Any>("args[0]")
        val validationMetadata = ValidationMetadata(
            pathToItem,
            SchemaConfiguration(JsonSchemaKeywordFlags.Builder().build()),
            PathToSchemasMap(),
            LinkedHashSet()
        )
        val mutableMap = LinkedHashMap<String, Any>()
        mutableMap["aDifferentProp"] = 1
        val arg = FrozenMap(mutableMap)
        val validator = RequiredValidator()
        assertFailsWith<ValidationException>(
            block = {
                validator.validate(
                    ValidationData(
                        ObjectWithRequiredSchema(),
                        arg,
                        validationMetadata
                    )
                )
            }
        )
    }
}