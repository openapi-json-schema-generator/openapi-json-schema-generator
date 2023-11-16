package org.openapijsonschematools.components.schemas;
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

public class ObjectWithOptionalTestProp {
    // nest classes so all schemas and input/output classes can be public
    
    
    public record Test(LinkedHashSet<Class<?>> type) implements JsonSchema {
        public static Test withDefaults() {
            LinkedHashSet<Class<?>> type = new LinkedHashSet<>();
            type.add(String.class);
            return new Test(type);
        }
        public static String validate(String arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(Test.class, arg, configuration);
        }
    }    
    
    public record ObjectWithOptionalTestProp1(LinkedHashSet<Class<?>> type, LinkedHashMap<String, Class<?>> properties) implements JsonSchema {
        /*
        NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
        Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
    
        Do not edit the class manually.
        */
        public static ObjectWithOptionalTestProp1 withDefaults() {
            LinkedHashSet<Class<?>> type = new LinkedHashSet<>();
            type.add(FrozenMap.class);
            LinkedHashMap<String, Class<?>> properties = new LinkedHashMap<>();
            properties.put("test", Test.class);
            return new ObjectWithOptionalTestProp1(type, properties);
        }
        public static <T extends FrozenMap> T validate(Map<String, Object> arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(ObjectWithOptionalTestProp1.class, arg, configuration);
        }
    }
}
