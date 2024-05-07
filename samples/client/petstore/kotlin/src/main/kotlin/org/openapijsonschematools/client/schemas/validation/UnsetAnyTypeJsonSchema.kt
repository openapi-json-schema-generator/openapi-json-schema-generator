package org.openapijsonschematools.client.schemas.validation

import org.openapijsonschematools.client.configurations.JsonSchemaKeywordFlags
import org.openapijsonschematools.client.configurations.SchemaConfiguration
import org.openapijsonschematools.client.exceptions.ValidationException

import java.time.LocalDate
import java.time.ZonedDateTime
import java.util.UUID

class UnsetAnyTypeJsonSchema {
    interface UnsetAnyTypeJsonSchema1Boxed {
        val data: Any?
    }

    data class UnsetAnyTypeJsonSchema1BoxedVoid(override val data: Nothing?) : UnsetAnyTypeJsonSchema1Boxed {
        fun getData(): Any? {
            return data
        }
    }

    data class UnsetAnyTypeJsonSchema1BoxedBoolean(override val data: Boolean) : UnsetAnyTypeJsonSchema1Boxed {
        fun getData(): Any? {
            return data
        }
    }

    data class UnsetAnyTypeJsonSchema1BoxedNumber(override val data: Number?) : UnsetAnyTypeJsonSchema1Boxed {
        fun getData(): Any? {
            return data
        }
    }

    data class UnsetAnyTypeJsonSchema1BoxedString(override val data: String?) : UnsetAnyTypeJsonSchema1Boxed {
        fun getData(): Any? {
            return data
        }
    }

    data class UnsetAnyTypeJsonSchema1BoxedList(override val data: FrozenList<Any>) : UnsetAnyTypeJsonSchema1Boxed {
        fun getData(): Any? {
            return data
        }
    }

    data class UnsetAnyTypeJsonSchema1BoxedMap(override val data: FrozenMap<Any>) : UnsetAnyTypeJsonSchema1Boxed {
        fun getData(): Any? {
            return data
        }
    }

    class UnsetAnyTypeJsonSchema1 protected constructor() : JsonSchema<UnsetAnyTypeJsonSchema1Boxed?>(JsonSchemaInfo()),
        NullSchemaValidator<UnsetAnyTypeJsonSchema1BoxedVoid?>,
        BooleanSchemaValidator<UnsetAnyTypeJsonSchema1BoxedBoolean?>,
        NumberSchemaValidator<UnsetAnyTypeJsonSchema1BoxedNumber?>,
        StringSchemaValidator<UnsetAnyTypeJsonSchema1BoxedString?>,
        ListSchemaValidator<FrozenList<Any?>?, UnsetAnyTypeJsonSchema1BoxedList?>,
        MapSchemaValidator<FrozenMap<Any?>?, UnsetAnyTypeJsonSchema1BoxedMap?> {
        @Throws(ValidationException::class)
        fun validate(arg: Nothing?, configuration: SchemaConfiguration?): Nothing? {
            val pathSet: MutableSet<List<Any>> = HashSet()
            val pathToItem = listOf<Any>("args[0]")
            val castArg: Nothing? = castToAllowedTypes(arg, pathToItem, pathSet)
            val usedConfiguration = Objects.requireNonNullElseGet(configuration) {
                SchemaConfiguration(
                    JsonSchemaKeywordFlags.Builder().build()
                )
            }
            val validatedPathToSchemas = PathToSchemasMap()
            val validationMetadata =
                ValidationMetadata(pathToItem, usedConfiguration!!, validatedPathToSchemas, LinkedHashSet())
            val pathToSchemasMap = getPathToSchemas(this, castArg, validationMetadata, pathSet)
            return getNewInstance(castArg, validationMetadata.pathToItem, pathToSchemasMap)
        }

        @Throws(ValidationException::class)
        fun validate(arg: Boolean, configuration: SchemaConfiguration?): Boolean {
            val pathSet: MutableSet<List<Any>> = HashSet()
            val pathToItem = listOf<Any>("args[0]")
            val castArg: Boolean = castToAllowedTypes(arg, pathToItem, pathSet)
            val usedConfiguration = Objects.requireNonNullElseGet(configuration) {
                SchemaConfiguration(
                    JsonSchemaKeywordFlags.Builder().build()
                )
            }
            val validatedPathToSchemas = PathToSchemasMap()
            val validationMetadata =
                ValidationMetadata(pathToItem, usedConfiguration!!, validatedPathToSchemas, LinkedHashSet())
            val pathToSchemasMap = getPathToSchemas(this, castArg, validationMetadata, pathSet)
            return getNewInstance(castArg, validationMetadata.pathToItem, pathToSchemasMap)
        }

        @Throws(ValidationException::class)
        fun validate(arg: Number, configuration: SchemaConfiguration?): Number? {
            val pathSet: MutableSet<List<Any>> = HashSet()
            val pathToItem = listOf<Any>("args[0]")
            val castArg: Number = castToAllowedTypes(arg, pathToItem, pathSet)
            val usedConfiguration = Objects.requireNonNullElseGet(configuration) {
                SchemaConfiguration(
                    JsonSchemaKeywordFlags.Builder().build()
                )
            }
            val validatedPathToSchemas = PathToSchemasMap()
            val validationMetadata =
                ValidationMetadata(pathToItem, usedConfiguration!!, validatedPathToSchemas, LinkedHashSet())
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
        fun validate(arg: String, configuration: SchemaConfiguration?): String? {
            val pathSet: MutableSet<List<Any>> = HashSet()
            val pathToItem = listOf<Any>("args[0]")
            val castArg: String = castToAllowedTypes(arg, pathToItem, pathSet)
            val usedConfiguration = Objects.requireNonNullElseGet(configuration) {
                SchemaConfiguration(
                    JsonSchemaKeywordFlags.Builder().build()
                )
            }
            val validatedPathToSchemas = PathToSchemasMap()
            val validationMetadata =
                ValidationMetadata(pathToItem, usedConfiguration!!, validatedPathToSchemas, LinkedHashSet())
            val pathToSchemasMap = getPathToSchemas(this, castArg, validationMetadata, pathSet)
            return getNewInstance(castArg, validationMetadata.pathToItem, pathToSchemasMap)
        }

        @Throws(ValidationException::class)
        fun validate(arg: LocalDate, configuration: SchemaConfiguration?): String? {
            return validate(arg.toString(), configuration)
        }

        @Throws(ValidationException::class)
        fun validate(arg: ZonedDateTime, configuration: SchemaConfiguration?): String? {
            return validate(arg.toString(), configuration)
        }

        @Throws(ValidationException::class)
        fun validate(arg: UUID, configuration: SchemaConfiguration?): String? {
            return validate(arg.toString(), configuration)
        }

        fun getNewInstance(arg: List<*>, pathToItem: List<Any>, pathToSchemas: PathToSchemasMap): FrozenList<Any> {
            val items: MutableList<Any?> = ArrayList()
            var i = 0
            for (item in arg) {
                val itemPathToItem: MutableList<Any> = ArrayList(pathToItem)
                itemPathToItem.add(i)
                val schemas = pathToSchemas.get(itemPathToItem)
                    ?: throw RuntimeException("Validation result is invalid, schemas must exist for a pathToItem")
                val itemSchema = schemas.entries.iterator().next().key
                val castItem = itemSchema.getNewInstance(item, itemPathToItem, pathToSchemas)
                items.add(castItem)
                i += 1
            }
            return FrozenList(items)
        }

        @Throws(ValidationException::class)
        fun validate(arg: List<*>, configuration: SchemaConfiguration?): FrozenList<Any> {
            val pathSet: MutableSet<List<Any>> = HashSet()
            val pathToItem = listOf<Any>("args[0]")
            val castArg: List<*> = castToAllowedTypes(arg, pathToItem, pathSet)
            val usedConfiguration = Objects.requireNonNullElseGet(configuration) {
                SchemaConfiguration(
                    JsonSchemaKeywordFlags.Builder().build()
                )
            }
            val validatedPathToSchemas = PathToSchemasMap()
            val validationMetadata =
                ValidationMetadata(pathToItem, usedConfiguration!!, validatedPathToSchemas, LinkedHashSet())
            val pathToSchemasMap = getPathToSchemas(this, castArg, validationMetadata, pathSet)
            return getNewInstance(castArg, validationMetadata.pathToItem, pathToSchemasMap)
        }

        fun getNewInstance(arg: Map<*, *>, pathToItem: List<Any>, pathToSchemas: PathToSchemasMap): FrozenMap<Any> {
            val properties = LinkedHashMap<String, Any?>()
            for ((entryKey, value1) in arg) {
                if (entryKey !is String) {
                    throw RuntimeException("Invalid non-string key value")
                }
                val propertyName = entryKey
                val propertyPathToItem: MutableList<Any> = ArrayList(pathToItem)
                propertyPathToItem.add(propertyName)
                val value = value1!!
                val schemas = pathToSchemas.get(propertyPathToItem)
                    ?: throw RuntimeException("Validation result is invalid, schemas must exist for a pathToItem")
                val propertySchema = schemas.entries.iterator().next().key
                val castValue = propertySchema.getNewInstance(value, propertyPathToItem, pathToSchemas)
                properties[propertyName] = castValue
            }
            return FrozenMap(properties)
        }

        @Throws(ValidationException::class)
        fun validate(arg: Map<*, *>, configuration: SchemaConfiguration?): FrozenMap<Any> {
            val pathSet: MutableSet<List<Any>> = HashSet()
            val pathToItem = listOf<Any>("args[0]")
            val castArg: Map<*, *> = castToAllowedTypes(arg, pathToItem, pathSet)
            val usedConfiguration = Objects.requireNonNullElseGet(configuration) {
                SchemaConfiguration(
                    JsonSchemaKeywordFlags.Builder().build()
                )
            }
            val validatedPathToSchemas = PathToSchemasMap()
            val validationMetadata =
                ValidationMetadata(pathToItem, usedConfiguration!!, validatedPathToSchemas, LinkedHashSet())
            val pathToSchemasMap = getPathToSchemas(this, castArg, validationMetadata, pathSet)
            return getNewInstance(castArg, validationMetadata.pathToItem, pathToSchemasMap)
        }

        override fun getNewInstance(arg: Any?, pathToItem: List<Any>, pathToSchemas: PathToSchemasMap): Any? {
            if (arg == null) {
                return getNewInstance(arg, pathToItem, pathToSchemas)
            } else if (arg is Boolean) {
                return getNewInstance(arg, pathToItem, pathToSchemas)
            } else if (arg is Number) {
                return getNewInstance(arg as Number?, pathToItem, pathToSchemas)
            } else if (arg is String) {
                return getNewInstance(arg as String?, pathToItem, pathToSchemas)
            } else if (arg is List<*>) {
                return getNewInstance(arg, pathToItem, pathToSchemas)
            } else if (arg is Map<*, *>) {
                return getNewInstance(arg, pathToItem, pathToSchemas)
            }
            throw RuntimeException("Invalid input type=$javaClass. It can't be instantiated by this schema")
        }

        @Throws(ValidationException::class)
        override fun validate(arg: Any?, configuration: SchemaConfiguration?): Any? {
            if (arg == null) {
                return validate(null as Nothing?, configuration)
            } else if (arg is Boolean) {
                return validate(arg, configuration)
            } else if (arg is Number) {
                return validate(arg as Number?, configuration)
            } else if (arg is String) {
                return validate(arg as String?, configuration)
            } else if (arg is List<*>) {
                return validate(arg as List<*>?, configuration)
            } else if (arg is Map<*, *>) {
                return validate(arg as Map<*, *>?, configuration)
            }
            throw ValidationException("Invalid input type=$javaClass. It can't be validated by this schema")
        }

        @Throws(ValidationException::class)
        fun validateAndBox(arg: Nothing?, configuration: SchemaConfiguration?): UnsetAnyTypeJsonSchema1BoxedVoid {
            return UnsetAnyTypeJsonSchema1BoxedVoid(validate(arg, configuration))
        }

        @Throws(ValidationException::class)
        fun validateAndBox(arg: Boolean, configuration: SchemaConfiguration?): UnsetAnyTypeJsonSchema1BoxedBoolean {
            return UnsetAnyTypeJsonSchema1BoxedBoolean(validate(arg, configuration))
        }

        @Throws(ValidationException::class)
        fun validateAndBox(arg: Number, configuration: SchemaConfiguration?): UnsetAnyTypeJsonSchema1BoxedNumber {
            return UnsetAnyTypeJsonSchema1BoxedNumber(validate(arg, configuration))
        }

        @Throws(ValidationException::class)
        fun validateAndBox(arg: String, configuration: SchemaConfiguration?): UnsetAnyTypeJsonSchema1BoxedString {
            return UnsetAnyTypeJsonSchema1BoxedString(validate(arg, configuration))
        }

        @Throws(ValidationException::class)
        fun validateAndBox(arg: List<*>, configuration: SchemaConfiguration?): UnsetAnyTypeJsonSchema1BoxedList {
            return UnsetAnyTypeJsonSchema1BoxedList(validate(arg, configuration))
        }

        @Throws(ValidationException::class)
        fun validateAndBox(arg: Map<*, *>, configuration: SchemaConfiguration?): UnsetAnyTypeJsonSchema1BoxedMap {
            return UnsetAnyTypeJsonSchema1BoxedMap(validate(arg, configuration))
        }

        @Throws(ValidationException::class)
        override fun validateAndBox(arg: Any?, configuration: SchemaConfiguration?): UnsetAnyTypeJsonSchema1Boxed {
            if (arg == null) {
                return validateAndBox(arg, configuration)
            } else if (arg is Boolean) {
                val castArg: Boolean = arg
                return validateAndBox(castArg, configuration)
            } else if (arg is String) {
                return validateAndBox(arg, configuration)
            } else if (arg is Number) {
                return validateAndBox(arg, configuration)
            } else if (arg is List<*>) {
                return validateAndBox(arg, configuration)
            } else if (arg is Map<*, *>) {
                return validateAndBox(arg, configuration)
            }
            throw ValidationException("Invalid input type=$javaClass. It can't be validated by this schema")
        }

        companion object {
            var instance: UnsetAnyTypeJsonSchema1? = null
                get() {
                    if (field == null) {
                        field = UnsetAnyTypeJsonSchema1()
                    }
                    return field
                }
                private set
        }
    }
}