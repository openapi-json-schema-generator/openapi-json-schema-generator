package org.openapijsonschematools.client.schemas.validation

import org.openapijsonschematools.client.configurations.SchemaConfiguration

data class ValidationMetadata(
    val pathToItem: List<Any>,
    val configuration: SchemaConfiguration,
    val validatedPathToSchemas: PathToSchemasMap,
    val seenClasses: Set<Class<*>>
) {
    fun validationRanEarlier(schema: JsonSchema<*>): Boolean {
        val validatedSchemas: Map<JsonSchema<*>, Nothing?>? = validatedPathToSchemas[pathToItem]
        if (validatedSchemas != null && validatedSchemas.containsKey(schema)) {
            return true
        }
        return seenClasses.contains(schema.javaClass)
    }
}