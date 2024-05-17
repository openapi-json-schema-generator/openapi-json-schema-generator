package org.openapijsonschematools.client.schemas

import org.openapijsonschematools.client.configurations.JsonSchemaKeywordFlags
import org.openapijsonschematools.client.exceptions.ValidationException
import org.openapijsonschematools.client.schemas.validation.FrozenList
import org.openapijsonschematools.client.schemas.validation.JsonSchema
import org.openapijsonschematools.client.schemas.validation.JsonSchemaInfo
import org.openapijsonschematools.client.configurations.SchemaConfiguration
import org.openapijsonschematools.client.schemas.validation.PathToSchemasMap
import org.openapijsonschematools.client.schemas.validation.ListSchemaValidator
import org.openapijsonschematools.client.schemas.validation.ValidationMetadata

open class ListJsonSchema {
    sealed interface ListJsonSchema1Boxed {
        fun getData(): Any?
    }

    data class ListJsonSchema1BoxedList(val data: FrozenList<Any?>) : ListJsonSchema1Boxed {
        override fun getData(): Any? {
            return data
        }
    }

    open class ListJsonSchema1 protected constructor() : JsonSchema<ListJsonSchema1Boxed>(
        JsonSchemaInfo()
            .type(setOf(List::class.java))
    ), ListSchemaValidator<FrozenList<Any?>, ListJsonSchema1BoxedList> {
        override fun getNewInstance(
            arg: List<*>,
            pathToItem: List<Any>,
            pathToSchemas: PathToSchemasMap
        ): FrozenList<Any?> {
            val items: MutableList<Any?> = ArrayList()
            var i = 0
            for (item in arg) {
                val itemPathToItem: List<Any> = pathToItem + i
                val schemas: LinkedHashMap<JsonSchema<*>, Nothing?> = pathToSchemas[itemPathToItem]
                    ?: throw RuntimeException("Validation result is invalid, schemas must exist for a pathToItem")
                val itemSchema: JsonSchema<*> = schemas.entries.iterator().next().key
                val castItem = itemSchema.getNewInstance(item, itemPathToItem, pathToSchemas)
                items.add(castItem)
                i += 1
            }
            return FrozenList(items)
        }

        @Throws(ValidationException::class)
        override fun validate(arg: List<*>, configuration: SchemaConfiguration?): FrozenList<Any?> {
            val pathSet: MutableSet<List<Any>> = HashSet()
            val pathToItem = listOf<Any>("args[0]")
            val castArg: List<*> = castToAllowedTypes(arg, pathToItem, pathSet)
            val usedConfiguration = configuration ?: SchemaConfiguration(JsonSchemaKeywordFlags.Builder().build())
            val validatedPathToSchemas = PathToSchemasMap()
            val validationMetadata =
                ValidationMetadata(pathToItem, usedConfiguration, validatedPathToSchemas, LinkedHashSet())
            val pathToSchemasMap = getPathToSchemas(this, castArg, validationMetadata, pathSet)
            return getNewInstance(castArg, validationMetadata.pathToItem, pathToSchemasMap)
        }

        override fun getNewInstance(arg: Any?, pathToItem: List<Any>, pathToSchemas: PathToSchemasMap): FrozenList<Any?> {
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
            throw ValidationException("Invalid input type=$javaClass. It can't be instantiated by this schema")
        }

        @Throws(ValidationException::class)
        override fun validateAndBox(arg: List<*>, configuration: SchemaConfiguration?): ListJsonSchema1BoxedList {
            return ListJsonSchema1BoxedList(validate(arg, configuration))
        }

        @Throws(ValidationException::class)
        override fun validateAndBox(arg: Any?, configuration: SchemaConfiguration?): ListJsonSchema1Boxed {
            if (arg is List<*>) {
                return validateAndBox(arg, configuration)
            }
            throw ValidationException("Invalid input type=$javaClass. It can't be validated by this schema")
        }

        companion object {
            @Volatile
            private var instance: ListJsonSchema1? = null

            fun getInstance() =
                instance ?: synchronized(this) {
                    instance ?: ListJsonSchema1().also { instance = it }
                }
        }
    }
}