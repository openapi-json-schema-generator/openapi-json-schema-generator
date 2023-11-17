package org.openapijsonschematools.paths.fakerefsstring.post.responses.response200.content.applicationjson;
import org.openapijsonschematools.configurations.SchemaConfiguration;
import org.openapijsonschematools.schemas.JsonSchema;
import org.openapijsonschematools.schemas.JsonSchemas;
import org.openapijsonschematools.schemas.FrozenList;
import org.openapijsonschematools.schemas.FrozenMap;

import java.time.LocalDate;
import java.time.ZonedDateTime;
import java.util.AbstractMap;
import java.util.LinkedHashMap;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;
import org.openapijsonschematools.components.schemas.StringSchema;

public class Schema {
    // $refed class
    
    
    public class Schema1 implements JsonSchema {
        public static String validate(String arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(StringSchema.StringSchema1.class, arg, configuration);
        }
    }
}
