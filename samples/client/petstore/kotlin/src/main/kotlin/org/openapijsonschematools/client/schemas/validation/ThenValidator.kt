package org.openapijsonschematools.client.schemas.validation

import org.openapijsonschematools.client.exceptions.ValidationException

class ThenValidator : KeywordValidator {
    @Throws(ValidationException::class)
    override fun validate(
        data: ValidationData
    ): PathToSchemasMap? {
        val then: Class<out JsonSchema<*>> = data.schema.then ?: return null
        val ifPathToSchemas: PathToSchemasMap = data.ifPathToSchemas
            ?: // if unset
            return null
        if (ifPathToSchemas.isEmpty()) {
            // if validation is false
            return null
        }
        val thenSchema = JsonSchemaFactory.getInstance(then)
        val pathToSchemas = PathToSchemasMap()
        val thenPathToSchemas = JsonSchema.validate(thenSchema, data.arg, data.validationMetadata)
        // todo capture validation error and describe it as an then error?
        pathToSchemas.update(ifPathToSchemas)
        pathToSchemas.update(thenPathToSchemas)
        return pathToSchemas
    }
}
