package org.openapijsonschematools.components.schemas;
import java.util.AbstractMap;
import java.util.LinkedHashMap;
import java.util.LinkedHashSet;
import java.util.Map;
import java.util.Set;
import org.openapijsonschematools.configurations.SchemaConfiguration;
import org.openapijsonschematools.schemas.AnyTypeJsonSchema;
import org.openapijsonschematools.schemas.NotAnyTypeJsonSchema;
import org.openapijsonschematools.schemas.StringJsonSchema;
import org.openapijsonschematools.schemas.validation.FrozenMap;
import org.openapijsonschematools.schemas.validation.JsonSchema;

public class JSONPatchRequestAddReplaceTest {
    // nest classes so all schemas and input/output classes can be public
    
    
    public class AdditionalProperties extends NotAnyTypeJsonSchema {}
        // NotAnyTypeSchema
    
    
    public class Path extends StringJsonSchema {}
    
    
    public class Value extends AnyTypeJsonSchema {}
    
    
    public class Op extends JsonSchema {
        public static final LinkedHashSet<Class<?>> type = new LinkedHashSet<>(Set.of(
            String.class
        ));
        public static String validate(String arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(Op.class, arg, configuration);
        }
    }    
    
    public static class JSONPatchRequestAddReplaceTestMap extends FrozenMap<String, Object> {
        JSONPatchRequestAddReplaceTestMap(FrozenMap<? extends String, ?> m) {
            super(m);
        }
        public static JSONPatchRequestAddReplaceTestMap of(Map<String, Object> arg, SchemaConfiguration configuration) {
            return JSONPatchRequestAddReplaceTest1.validate(arg, configuration);
        }
    }    
    
    public class JSONPatchRequestAddReplaceTest1 extends JsonSchema {
        /*
        NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
        Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
    
        Do not edit the class manually.
        */
        public static final LinkedHashSet<Class<?>> type = new LinkedHashSet<>(Set.of(
            FrozenMap.class
        ));
        public static final LinkedHashMap<String, Class<?>> properties = new LinkedHashMap<>(Map.ofEntries(
            new AbstractMap.SimpleEntry<String, Class<?>>("path", Path.class),
            new AbstractMap.SimpleEntry<String, Class<?>>("value", Value.class),
            new AbstractMap.SimpleEntry<String, Class<?>>("op", Op.class)
        ));
        public static final Set<String> required = new LinkedHashSet<>(Set.of(
            "op",
            "path",
            "value"
        ));
        static final Class<?> additionalProperties = AdditionalProperties.class;
        protected static JSONPatchRequestAddReplaceTestMap getMapOutputInstance(FrozenMap<? extends String, ?> arg) {
            return new JSONPatchRequestAddReplaceTestMap(arg);
        }
        public static <T extends FrozenMap> T validate(Map<String, Object> arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(JSONPatchRequestAddReplaceTest1.class, arg, configuration);
        }
    }
}
