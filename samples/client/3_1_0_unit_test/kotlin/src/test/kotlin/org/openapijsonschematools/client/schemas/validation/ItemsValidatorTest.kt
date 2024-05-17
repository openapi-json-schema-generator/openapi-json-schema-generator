package org.openapijsonschematools.client.schemas.validation

import org.openapijsonschematools.client.configurations.JsonSchemaKeywordFlags
import org.openapijsonschematools.client.configurations.SchemaConfiguration
import org.openapijsonschematools.client.schemas.StringJsonSchema
import org.openapijsonschematools.client.exceptions.ValidationException

import kotlin.test.Test
import kotlin.test.assertEquals
import kotlin.test.assertFailsWith
import kotlin.test.assertNull

class ItemsValidatorTest {
    interface ArrayWithItemsSchemaBoxed
    class ArrayWithItemsSchemaBoxedList : ArrayWithItemsSchemaBoxed
    class ArrayWithItemsSchema : JsonSchema<ArrayWithItemsSchemaBoxed>(
        JsonSchemaInfo()
            .type(setOf(List::class.java))
            .items(StringJsonSchema.StringJsonSchema1::class.java)
    ) {
        override fun getNewInstance(arg: Any?, pathToItem: List<Any>, pathToSchemas: PathToSchemasMap): Any? {
            if (arg is List<*>) {
                return getNewInstance(arg, pathToItem, pathToSchemas)
            }
            throw RuntimeException("Invalid input type=$javaClass. It can't be instantiated by this schema")
        }

        @Throws(ValidationException::class)
        override fun validate(arg: Any?, configuration: SchemaConfiguration?): Any? {
            if (arg is List<*>) {
                return validate(arg, configuration)
            }
            throw ValidationException("Invalid input type=$javaClass. It can't be validated by this schema")
        }

        @Throws(ValidationException::class)
        override fun validateAndBox(arg: Any?, configuration: SchemaConfiguration?): ArrayWithItemsSchemaBoxed {
            return ArrayWithItemsSchemaBoxedList()
        }
    }

    @Test
    @Throws(ValidationException::class)
    fun testCorrectItemsSucceeds() {
        val pathToItem = listOf<Any>("args[0]")
        val validationMetadata = ValidationMetadata(
            pathToItem,
            SchemaConfiguration(JsonSchemaKeywordFlags.Builder().build()),
            PathToSchemasMap(),
            LinkedHashSet()
        )
        val mutableList: MutableList<Any> = ArrayList()
        mutableList.add("a")
        val arg = FrozenList(mutableList)
        val validator = ItemsValidator()
        val pathToSchemas = validator.validate(
            ValidationData(
                ArrayWithItemsSchema(),
                arg,
                validationMetadata
            )
        ) ?: throw RuntimeException("Invalid null value in pathToSchemas for this test case")
        val expectedPathToItem: MutableList<Any> = ArrayList()
        expectedPathToItem.add("args[0]")
        expectedPathToItem.add(0)
        val expectedClasses = LinkedHashMap<JsonSchema<*>, Nothing?>()
        val schema = JsonSchemaFactory.getInstance(StringJsonSchema.StringJsonSchema1::class.java)
        expectedClasses[schema] = null
        val expectedPathToSchemas = PathToSchemasMap()
        expectedPathToSchemas[expectedPathToItem] = expectedClasses
        assertEquals(pathToSchemas, expectedPathToSchemas)
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
        val validator = ItemsValidator()
        val pathToSchemas = validator.validate(
            ValidationData(
                ArrayWithItemsSchema(),
                1,
                validationMetadata
            )
        )
        assertNull(pathToSchemas)
    }

    @Test
    fun testIncorrectItemFails() {
        val pathToItem = listOf<Any>("args[0]")
        val validationMetadata = ValidationMetadata(
            pathToItem,
            SchemaConfiguration(JsonSchemaKeywordFlags.Builder().build()),
            PathToSchemasMap(),
            LinkedHashSet()
        )
        val mutableList: MutableList<Any> = ArrayList()
        mutableList.add(1)
        val arg = FrozenList(mutableList)
        val validator = ItemsValidator()
        assertFailsWith<ValidationException>(
            block = {
                validator.validate(
                    ValidationData(
                        ArrayWithItemsSchema(),
                        arg,
                        validationMetadata
                    )
                )
            }
        )
    }
}