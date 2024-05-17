package org.openapijsonschematools.client.schemas

import org.openapijsonschematools.client.configurations.JsonSchemaKeywordFlags
import org.openapijsonschematools.client.configurations.SchemaConfiguration
import org.openapijsonschematools.client.exceptions.ValidationException
import org.openapijsonschematools.client.schemas.validation.FrozenList
import org.openapijsonschematools.client.schemas.validation.FrozenMap
import org.openapijsonschematools.client.schemas.validation.JsonSchema
import org.openapijsonschematools.client.schemas.validation.JsonSchemaInfo
import org.openapijsonschematools.client.schemas.validation.PathToSchemasMap
import org.openapijsonschematools.client.schemas.validation.NullSchemaValidator
import org.openapijsonschematools.client.schemas.validation.BooleanSchemaValidator
import org.openapijsonschematools.client.schemas.validation.NumberSchemaValidator
import org.openapijsonschematools.client.schemas.validation.StringSchemaValidator
import org.openapijsonschematools.client.schemas.validation.ListSchemaValidator
import org.openapijsonschematools.client.schemas.validation.MapSchemaValidator
import org.openapijsonschematools.client.schemas.validation.ValidationMetadata

import java.time.LocalDate
import java.time.ZonedDateTime
import java.util.UUID

open class NotAnyTypeJsonSchema {
    sealed interface NotAnyTypeJsonSchema1Boxed {
        fun getData(): Any?
    }


    data class NotAnyTypeJsonSchema1BoxedVoid(val data: Void?) : NotAnyTypeJsonSchema1Boxed {
        override fun getData(): Any? {
            return data
        }
    }


    data class NotAnyTypeJsonSchema1BoxedBoolean(val data: Boolean) : NotAnyTypeJsonSchema1Boxed {
        override fun getData(): Any? {
            return data
        }

    }


    data class NotAnyTypeJsonSchema1BoxedNumber(val data: Number) : NotAnyTypeJsonSchema1Boxed {
        override fun getData(): Any? {
            return data
        }
    }


    data class NotAnyTypeJsonSchema1BoxedString(val data: String) : NotAnyTypeJsonSchema1Boxed {
        override fun getData(): Any? {
            return data
        }
    }


    data class NotAnyTypeJsonSchema1BoxedList(val data: FrozenList<Any?>) : NotAnyTypeJsonSchema1Boxed {
        override fun getData(): Any? {
            return data
        }
    }


    data class NotAnyTypeJsonSchema1BoxedMap(val data: FrozenMap<Any?>) : NotAnyTypeJsonSchema1Boxed {
        override fun getData(): Any? {
            return data
        }
    }

    open class NotAnyTypeJsonSchema1 protected constructor() : JsonSchema<NotAnyTypeJsonSchema1Boxed?>(
        JsonSchemaInfo()
            .not(AnyTypeJsonSchema.AnyTypeJsonSchema1::class.java)
    ), NullSchemaValidator<NotAnyTypeJsonSchema1BoxedVoid>, BooleanSchemaValidator<NotAnyTypeJsonSchema1BoxedBoolean>,
        NumberSchemaValidator<NotAnyTypeJsonSchema1BoxedNumber>,
        StringSchemaValidator<NotAnyTypeJsonSchema1BoxedString>,
        ListSchemaValidator<FrozenList<Any?>, NotAnyTypeJsonSchema1BoxedList>,
        MapSchemaValidator<FrozenMap<Any?>, NotAnyTypeJsonSchema1BoxedMap> {
        @Throws(ValidationException::class)
        override fun validate(arg: Nothing?, configuration: SchemaConfiguration?): Nothing? {
            val pathSet: MutableSet<List<Any>> = HashSet()
            val pathToItem = listOf<Any>("args[0]")
            val castArg: Nothing? = castToAllowedTypes(arg, pathToItem, pathSet)
            val usedConfiguration = configuration ?: SchemaConfiguration(JsonSchemaKeywordFlags.Builder().build())
            val validatedPathToSchemas = PathToSchemasMap()
            val validationMetadata =
                ValidationMetadata(pathToItem, usedConfiguration, validatedPathToSchemas, LinkedHashSet())
            val pathToSchemasMap = getPathToSchemas(this, castArg, validationMetadata, pathSet)
            return getNewInstance(castArg, validationMetadata.pathToItem, pathToSchemasMap)
        }

        @Throws(ValidationException::class)
        override fun validate(arg: Boolean, configuration: SchemaConfiguration?): Boolean {
            val pathSet: MutableSet<List<Any>> = HashSet()
            val pathToItem = listOf<Any>("args[0]")
            val castArg: Boolean = castToAllowedTypes(arg, pathToItem, pathSet)
            val usedConfiguration = configuration ?: SchemaConfiguration(JsonSchemaKeywordFlags.Builder().build())
            val validatedPathToSchemas = PathToSchemasMap()
            val validationMetadata =
                ValidationMetadata(pathToItem, usedConfiguration, validatedPathToSchemas, LinkedHashSet())
            val pathToSchemasMap = getPathToSchemas(this, castArg, validationMetadata, pathSet)
            return getNewInstance(castArg, validationMetadata.pathToItem, pathToSchemasMap)
        }

        @Throws(ValidationException::class)
        override fun validate(arg: Number, configuration: SchemaConfiguration?): Number {
            val pathSet: MutableSet<List<Any>> = HashSet()
            val pathToItem = listOf<Any>("args[0]")
            val castArg: Number = castToAllowedTypes(arg, pathToItem, pathSet)
            val usedConfiguration = configuration ?: SchemaConfiguration(JsonSchemaKeywordFlags.Builder().build())
            val validatedPathToSchemas = PathToSchemasMap()
            val validationMetadata =
                ValidationMetadata(pathToItem, usedConfiguration, validatedPathToSchemas, LinkedHashSet())
            val pathToSchemasMap = getPathToSchemas(this, castArg, validationMetadata, pathSet)
            return getNewInstance(castArg, validationMetadata.pathToItem, pathToSchemasMap)
        }

        @Throws(ValidationException::class)
        fun validate(arg: Int, configuration: SchemaConfiguration?): Int {
            return validate(arg as Number, configuration) as Int
        }

        @Throws(ValidationException::class)
        fun validate(arg: Long, configuration: SchemaConfiguration?): Long {
            return validate(arg as Number, configuration) as Long
        }

        @Throws(ValidationException::class)
        fun validate(arg: Float, configuration: SchemaConfiguration?): Float {
            return validate(arg as Number, configuration) as Float
        }

        @Throws(ValidationException::class)
        fun validate(arg: Double, configuration: SchemaConfiguration?): Double {
            return validate(arg as Number, configuration) as Double
        }

        @Throws(ValidationException::class)
        override fun validate(arg: String, configuration: SchemaConfiguration?): String {
            val pathSet: MutableSet<List<Any>> = HashSet()
            val pathToItem = listOf<Any>("args[0]")
            val castArg: String = castToAllowedTypes(arg, pathToItem, pathSet)
            val usedConfiguration = configuration ?: SchemaConfiguration(JsonSchemaKeywordFlags.Builder().build())
            val validatedPathToSchemas = PathToSchemasMap()
            val validationMetadata =
                ValidationMetadata(pathToItem, usedConfiguration, validatedPathToSchemas, LinkedHashSet())
            val pathToSchemasMap = getPathToSchemas(this, castArg, validationMetadata, pathSet)
            return getNewInstance(castArg, validationMetadata.pathToItem, pathToSchemasMap)
        }

        @Throws(ValidationException::class)
        fun validate(arg: LocalDate, configuration: SchemaConfiguration?): String {
            return validate(arg.toString(), configuration)
        }

        @Throws(ValidationException::class)
        fun validate(arg: ZonedDateTime, configuration: SchemaConfiguration?): String {
            return validate(arg.toString(), configuration)
        }

        @Throws(ValidationException::class)
        fun validate(arg: UUID, configuration: SchemaConfiguration?): String {
            return validate(arg.toString(), configuration)
        }

        override fun getNewInstance(
            arg: List<*>,
            pathToItem: List<Any>,
            pathToSchemas: PathToSchemasMap
        ): FrozenList<Any?> {
            val items: MutableList<Any?> = ArrayList()
            var i = 0
            for (item in arg) {
                val itemPathToItem: MutableList<Any> = ArrayList(pathToItem)
                itemPathToItem.add(i)
                val schemas = pathToSchemas[itemPathToItem]
                    ?: throw RuntimeException("Validation result is invalid, schemas must exist for a pathToItem")
                val itemSchema = schemas.entries.iterator().next().key
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

        override fun getNewInstance(
            arg: Map<*, *>,
            pathToItem: List<Any>,
            pathToSchemas: PathToSchemasMap
        ): FrozenMap<Any?> {
            val properties = LinkedHashMap<String, Any?>()
            for ((entryKey, value1) in arg) {
                if (entryKey !is String) {
                    throw RuntimeException("Invalid non-string key value")
                }
                val propertyPathToItem: MutableList<Any> = ArrayList(pathToItem)
                propertyPathToItem.add(entryKey)
                val schemas = pathToSchemas[propertyPathToItem]
                    ?: throw RuntimeException("Validation result is invalid, schemas must exist for a pathToItem")
                val propertySchema = schemas.entries.iterator().next().key
                val castValue = propertySchema.getNewInstance(value1, propertyPathToItem, pathToSchemas)
                properties[entryKey] = castValue
            }
            return FrozenMap(properties)
        }

        @Throws(ValidationException::class)
        override fun validate(arg: Map<*, *>, configuration: SchemaConfiguration?): FrozenMap<Any?> {
            val pathSet: MutableSet<List<Any>> = HashSet()
            val pathToItem = listOf<Any>("args[0]")
            val castArg: Map<*, *> = castToAllowedTypes(arg, pathToItem, pathSet)
            val usedConfiguration = configuration ?: SchemaConfiguration(JsonSchemaKeywordFlags.Builder().build())
            val validatedPathToSchemas = PathToSchemasMap()
            val validationMetadata =
                ValidationMetadata(pathToItem, usedConfiguration, validatedPathToSchemas, LinkedHashSet())
            val pathToSchemasMap = getPathToSchemas(this, castArg, validationMetadata, pathSet)
            return getNewInstance(castArg, validationMetadata.pathToItem, pathToSchemasMap)
        }

        override fun getNewInstance(arg: Any?, pathToItem: List<Any>, pathToSchemas: PathToSchemasMap): Any? {
            when (arg) {
                null -> {
                    return getNewInstance(null as Void?, pathToItem, pathToSchemas)
                }
                is Boolean -> {
                    return getNewInstance(arg, pathToItem, pathToSchemas)
                }

                is Number -> {
                    return getNewInstance(arg, pathToItem, pathToSchemas)
                }

                is String -> {
                    return getNewInstance(arg, pathToItem, pathToSchemas)
                }

                is List<*> -> {
                    return getNewInstance(arg, pathToItem, pathToSchemas)
                }

                is Map<*, *> -> {
                    return getNewInstance(arg, pathToItem, pathToSchemas)
                }

                else -> throw RuntimeException("Invalid input type=$javaClass. It can't be instantiated by this schema")
            }
        }

        @Throws(ValidationException::class)
        override fun validate(arg: Any?, configuration: SchemaConfiguration?): Any? {
            when (arg) {
                null -> {
                    return validate(null as Void?, configuration)
                }
                is Boolean -> {
                    return validate(arg, configuration)
                }

                is Number -> {
                    return validate(arg, configuration)
                }

                is String -> {
                    return validate(arg, configuration)
                }

                is List<*> -> {
                    return validate(arg, configuration)
                }

                is Map<*, *> -> {
                    return validate(arg, configuration)
                }

                else -> throw ValidationException("Invalid input type=$javaClass. It can't be validated by this schema")
            }
        }

        @Throws(ValidationException::class)
        override fun validateAndBox(arg: Nothing?, configuration: SchemaConfiguration?): NotAnyTypeJsonSchema1BoxedVoid {
            return NotAnyTypeJsonSchema1BoxedVoid(validate(arg, configuration))
        }

        @Throws(ValidationException::class)
        override fun validateAndBox(
            arg: Boolean,
            configuration: SchemaConfiguration?
        ): NotAnyTypeJsonSchema1BoxedBoolean {
            return NotAnyTypeJsonSchema1BoxedBoolean(validate(arg, configuration))
        }

        @Throws(ValidationException::class)
        override fun validateAndBox(
            arg: Number,
            configuration: SchemaConfiguration?
        ): NotAnyTypeJsonSchema1BoxedNumber {
            return NotAnyTypeJsonSchema1BoxedNumber(validate(arg, configuration))
        }

        @Throws(ValidationException::class)
        override fun validateAndBox(
            arg: String,
            configuration: SchemaConfiguration?
        ): NotAnyTypeJsonSchema1BoxedString {
            return NotAnyTypeJsonSchema1BoxedString(validate(arg, configuration))
        }

        @Throws(ValidationException::class)
        override fun validateAndBox(
            arg: List<*>,
            configuration: SchemaConfiguration?
        ): NotAnyTypeJsonSchema1BoxedList {
            return NotAnyTypeJsonSchema1BoxedList(validate(arg, configuration))
        }

        @Throws(ValidationException::class)
        override fun validateAndBox(
            arg: Map<*, *>,
            configuration: SchemaConfiguration?
        ): NotAnyTypeJsonSchema1BoxedMap {
            return NotAnyTypeJsonSchema1BoxedMap(validate(arg, configuration))
        }

        @Throws(ValidationException::class)
        override fun validateAndBox(arg: Any?, configuration: SchemaConfiguration?): NotAnyTypeJsonSchema1Boxed {
            when (arg) {
                null -> {
                    return validateAndBox(null, configuration)
                }
                is Boolean -> {
                    val castArg: Boolean = arg
                    return validateAndBox(castArg, configuration)
                }

                is String -> {
                    return validateAndBox(arg, configuration)
                }

                is Number -> {
                    return validateAndBox(arg, configuration)
                }

                is List<*> -> {
                    return validateAndBox(arg, configuration)
                }

                is Map<*, *> -> {
                    return validateAndBox(arg, configuration)
                }

                else -> throw ValidationException("Invalid input type=$javaClass. It can't be validated by this schema")
            }
        }

        companion object {
            var instance: NotAnyTypeJsonSchema1? = null
                get() {
                    if (field == null) {
                        field = NotAnyTypeJsonSchema1()
                    }
                    return field
                }
                private set
        }
    }
}