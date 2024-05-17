package org.openapijsonschematools.client.schemas.validation

import java.time.ZonedDateTime
import java.time.LocalDate

class CustomIsoparser {
    companion object {
        fun parseIsodatetime(dateTime: String): ZonedDateTime {
            return ZonedDateTime.parse(dateTime)
        }

        fun parseIsodate(date: String): LocalDate {
            return LocalDate.parse(date)
        }
    }
}