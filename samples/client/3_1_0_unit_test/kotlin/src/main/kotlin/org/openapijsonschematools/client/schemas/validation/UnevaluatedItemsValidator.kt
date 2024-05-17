package org.openapijsonschematools.client.schemas.validation

import org.openapijsonschematools.client.exceptions.ValidationException

class UnevaluatedItemsValidator : KeywordValidator {
    @Throws(ValidationException::class)
    override fun validate(
        data: ValidationData
    ): PathToSchemasMap? {
        val unevaluatedItems: Class<out JsonSchema<*>> = data.schema.unevaluatedItems ?: return null
        val knownPathToSchemas: PathToSchemasMap = data.knownPathToSchemas ?: return null
        if (data.arg !is List<*>) {
            return null
        }
        if (data.arg.isEmpty()) {
            return null
        }
        val pathToSchemas = PathToSchemasMap()
        val minIndex = if (data.schema.prefixItems != null) data.schema.prefixItems.size else 0
        val unevaluatedItemsSchema = JsonSchemaFactory.getInstance(unevaluatedItems)
        for (i in minIndex until data.arg.size) {
            val itemPathToItem: List<Any> = data.validationMetadata.pathToItem + i
            if (knownPathToSchemas.containsKey(itemPathToItem)) {
                continue
            }
            val itemValidationMetadata = ValidationMetadata(
                itemPathToItem,
                data.validationMetadata.configuration,
                data.validationMetadata.validatedPathToSchemas,
                data.validationMetadata.seenClasses
            )
            if (itemValidationMetadata.validationRanEarlier(unevaluatedItemsSchema)) {
                // todo add_deeper_validated_schemas
                continue
            }
            val otherPathToSchemas = JsonSchema.validate(unevaluatedItemsSchema, data.arg[i], itemValidationMetadata)
            pathToSchemas.update(otherPathToSchemas)
        }
        return pathToSchemas
    }
}