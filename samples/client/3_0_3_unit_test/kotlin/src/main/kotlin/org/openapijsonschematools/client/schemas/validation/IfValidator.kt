package org.openapijsonschematools.client.schemas.validation

import org.openapijsonschematools.client.exceptions.ValidationException

class IfValidator : KeywordValidator {
    @Throws(ValidationException::class)
    override fun validate(
        data: ValidationData
    ): PathToSchemasMap? {
        if (data.schema.ifSchema == null) {
            return null
        }
        if (data.ifPathToSchemas == null) {
            throw ValidationException("Invalid type for ifPathToSchemas")
        }
        /*
        if is false use case
        ifPathToSchemas == {}
        no need to add any data to pathToSchemas

        if true, then true -> true for whole schema
        so validate_then will add ifPathToSchemas data to pathToSchemas
        */
        return null
    }
}