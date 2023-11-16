package org.openapijsonschematools.paths.fakebodywithfileschema.put.requestbody.content.applicationjson;
import org.openapijsonschematools.configurations.SchemaConfiguration;
import org.openapijsonschematools.schemas.JsonSchema;
import org.openapijsonschematools.schemas.JsonSchemas;
import org.openapijsonschematools.schemas.FrozenList;
import org.openapijsonschematools.schemas.FrozenMap;

import java.time.LocalDate;
import java.time.ZonedDateTime;
import java.util.LinkedHashMap;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;
import org.openapijsonschematools.components.schemas.FileSchemaTestClass;

public class Schema {
    // $refed class
    
    
    public record Schema1() implements JsonSchema {
        public static FileSchemaTestClass.FileSchemaTestClass1 withDefaults() {
            return FileSchemaTestClass.FileSchemaTestClass1.withDefaults();
        }
    
        public static <T extends FrozenMap> T validate(Map<String, Object> arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(FileSchemaTestClass.FileSchemaTestClass1.class, arg, configuration);
        }
    }
}
