package org.openapijsonschematools.client.schemas.validation

import org.openapijsonschematools.client.exceptions.ValidationException

class RequiredValidator : KeywordValidator {
    @Throws(ValidationException::class)
    override fun validate(
        data: ValidationData
    ): PathToSchemasMap? {
        val required: Set<String> = data.schema.required ?: return null
        if (data.arg !is Map<*, *>) {
            return null
        }
        val missingRequiredProperties: MutableSet<String> = HashSet(required)
        for (key in data.arg.keys) {
            if (key is String) {
                missingRequiredProperties.remove(key)
            }
        }
        if (missingRequiredProperties.isNotEmpty()) {
            val missingReqProps: List<String> = missingRequiredProperties.toList().sorted()
            var pluralChar = ""
            if (missingRequiredProperties.size > 1) {
                pluralChar = "s"
            }
            throw ValidationException(
                data.schema.javaClass.simpleName + " is missing " + missingRequiredProperties.size + " required argument" + pluralChar + ": " + missingReqProps
            )
        }
        return null
    }
}
