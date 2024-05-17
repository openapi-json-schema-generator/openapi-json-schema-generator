package org.openapijsonschematools.client.schemas.validation

import org.openapijsonschematools.client.exceptions.ValidationException

class ItemsValidator : KeywordValidator {
    @Throws(ValidationException::class)
    override fun validate(
        data: ValidationData
    ): PathToSchemasMap? {
        val items: Class<out JsonSchema<*>> = data.schema.items ?: return null
        if (data.arg !is List<*>) {
            return null
        }
        if (data.arg.isEmpty()) {
            return null
        }
        val pathToSchemas = PathToSchemasMap()
        val minIndex = if (data.schema.prefixItems != null) data.schema.prefixItems.size else 0
        val itemsSchema = JsonSchemaFactory.getInstance(items)
        for (i in minIndex until data.arg.size) {
            val itemPathToItem: MutableList<Any> = ArrayList(data.validationMetadata.pathToItem)
            itemPathToItem.add(i)
            val itemValidationMetadata = ValidationMetadata(
                itemPathToItem,
                data.validationMetadata.configuration,
                data.validationMetadata.validatedPathToSchemas,
                data.validationMetadata.seenClasses
            )
            if (itemValidationMetadata.validationRanEarlier(itemsSchema)) {
                // todo add_deeper_validated_schemas
                continue
            }
            val otherPathToSchemas = JsonSchema.validate(itemsSchema, data.arg[i], itemValidationMetadata)
            pathToSchemas.update(otherPathToSchemas)
        }
        return pathToSchemas
    }
}
