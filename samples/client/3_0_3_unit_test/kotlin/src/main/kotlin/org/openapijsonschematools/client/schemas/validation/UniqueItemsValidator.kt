package org.openapijsonschematools.client.schemas.validation

import org.openapijsonschematools.client.exceptions.ValidationException

class UniqueItemsValidator : KeywordValidator {
    @Throws(ValidationException::class)
    override fun validate(
        data: ValidationData
    ): PathToSchemasMap? {
        val uniqueItems: Boolean = data.schema.uniqueItems ?: return null
        if (data.arg !is List<*>) {
            return null
        }
        if (!uniqueItems) {
            return null
        }
        val seenItems: MutableSet<Any?> = HashSet()
        for (item in data.arg) {
            val startingSeenItemsSize = seenItems.size
            seenItems.add(item)
            if (seenItems.size == startingSeenItemsSize) {
                throw ValidationException("Invalid list value, list contains duplicate items when uniqueItems is true")
            }
        }
        return null
    }
}
