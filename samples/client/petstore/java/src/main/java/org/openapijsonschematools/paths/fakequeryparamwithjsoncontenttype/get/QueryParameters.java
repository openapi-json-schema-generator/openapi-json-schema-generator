package org.openapijsonschematools.paths.fakequeryparamwithjsoncontenttype.get;
import org.openapijsonschematools.configurations.SchemaConfiguration;
import org.openapijsonschematools.schemas.JsonSchema;
import org.openapijsonschematools.schemas.AnyTypeSchema;

import java.util.LinkedHashSet;
public class QueryParameters {
    // nest classes so all schemas and input/output classes can be public
    
    
    public record class AdditionalProperties implements JsonSchema {
        public static NotAnyTypeSchema withDefaults() {
            return NotAnyTypeSchema.withDefaults();
        }
    
        // NotAnyTypeSchema
    }
}
