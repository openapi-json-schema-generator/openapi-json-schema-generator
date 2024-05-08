package org.openapijsonschematools.client.schemas.validation

import org.openapijsonschematools.client.exceptions.ValidationException
import java.math.BigDecimal

abstract class BigDecimalValidator {
    @Throws(ValidationException::class)
    protected fun getBigDecimal(arg: Number): BigDecimal {
        return when (arg) {
            is Int -> {
                BigDecimal(arg)
            }

            is Long -> {
                BigDecimal(arg)
            }

            is Float -> {
                BigDecimal(arg.toString())
            }

            is Double -> {
                BigDecimal(arg.toString())
            }

            else -> {
                throw ValidationException("Invalid type input for arg")
            }
        }
    }
}
