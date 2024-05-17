package org.openapijsonschematools.client.schemas.validation

class PathToSchemasMap : LinkedHashMap<List<Any>, LinkedHashMap<JsonSchema<*>, Nothing?>>() {
    fun update(other: PathToSchemasMap) {
        for ((pathToItem, otherSchemas) in other) {
            if (containsKey(pathToItem)) {
                get(pathToItem)!!.putAll(otherSchemas)
            } else {
                put(pathToItem, otherSchemas)
            }
        }
    }
}