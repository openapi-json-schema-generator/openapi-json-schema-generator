package org.openapijsonschematools.client.schemas.validation

import org.openapijsonschematools.client.exceptions.ValidationException

class ExclusiveMaximumValidator : KeywordValidator {
    @Throws(ValidationException::class)
    override fun validate(
        data: ValidationData
    ): PathToSchemasMap? {
        val exclusiveMaximum: Number = data.schema.exclusiveMaximum ?: return null
        if (data.arg !is Number) {
            return null
        }
        val msg =
            "Value " + data.arg + " is invalid because it is >= the exclusiveMaximum of " + exclusiveMaximum
        when (data.arg) {
            is Int -> {
                if (data.arg.compareTo(exclusiveMaximum.toInt()) > -1) {
                    throw ValidationException(msg)
                }
            }

            is Long -> {
                if (data.arg.compareTo(exclusiveMaximum.toLong()) > -1) {
                    throw ValidationException(msg)
                }
            }

            is Float -> {
                if (data.arg.compareTo(exclusiveMaximum.toFloat()) > -1) {
                    throw ValidationException(msg)
                }
            }

            is Double -> {
                if (data.arg.compareTo(exclusiveMaximum.toDouble()) > -1) {
                    throw ValidationException(msg)
                }
            }
        }
        return null
    }
}
