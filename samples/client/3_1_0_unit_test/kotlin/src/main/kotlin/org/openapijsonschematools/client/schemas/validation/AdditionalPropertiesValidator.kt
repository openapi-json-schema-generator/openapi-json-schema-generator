package org.openapijsonschematools.client.schemas.validation

import org.openapijsonschematools.client.exceptions.ValidationException

class AdditionalPropertiesValidator : KeywordValidator {
    @Throws(ValidationException::class)
    override fun validate(
        data: ValidationData
    ): PathToSchemasMap? {
        if (data.arg !is Map<*, *>) {
            return null
        }
        val additionalProperties: Class<out JsonSchema<*>> = data.schema.additionalProperties ?: return null
        val presentAdditionalProperties: MutableSet<String> = LinkedHashSet()
        for (key in data.arg.keys) {
            if (key is String) {
                presentAdditionalProperties.add(key)
            }
        }
        val properties: Map<String, Class<out JsonSchema<*>>>? = data.schema.properties
        if (properties != null) {
            presentAdditionalProperties.removeAll(properties.keys)
        }
        val pathToSchemas = PathToSchemasMap()
        for (addPropName in presentAdditionalProperties) {
            val propValue: Any? = data.arg.get(addPropName)
            val propPathToItem: List<Any> = data.validationMetadata.pathToItem + addPropName
            if (data.patternPropertiesPathToSchemas != null && data.patternPropertiesPathToSchemas
                    .containsKey(propPathToItem)
            ) {
                continue
            }
            val propValidationMetadata = ValidationMetadata(
                propPathToItem,
                data.validationMetadata.configuration,
                data.validationMetadata.validatedPathToSchemas,
                data.validationMetadata.seenClasses
            )
            val addPropsSchema = JsonSchemaFactory.getInstance(additionalProperties)
            if (propValidationMetadata.validationRanEarlier(addPropsSchema)) {
                // todo add_deeper_validated_schemas
                continue
            }
            val otherPathToSchemas = JsonSchema.validate(addPropsSchema, propValue, propValidationMetadata)
            pathToSchemas.update(otherPathToSchemas)
        }
        return pathToSchemas
    }
}
