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
        if (data.arg is Int) {
            if (data.arg.compareTo(exclusiveMaximum.toInt()) > -1) {
                throw ValidationException(msg)
            }
            return null
        }
        if (data.arg is Long) {
            if (data.arg.compareTo(exclusiveMaximum.toLong()) > -1) {
                throw ValidationException(msg)
            }
            return null
        }
        if (data.arg is Float) {
            if (data.arg.compareTo(exclusiveMaximum.toFloat()) > -1) {
                throw ValidationException(msg)
            }
            return null
        }
        if (data.arg is Double) {
            if (data.arg.compareTo(exclusiveMaximum.toDouble()) > -1) {
                throw ValidationException(msg)
            }
            return null
        }
        return null
    }
}
