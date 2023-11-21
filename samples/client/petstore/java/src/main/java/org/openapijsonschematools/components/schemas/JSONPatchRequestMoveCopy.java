package org.openapijsonschematools.components.schemas;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.Set;
import org.openapijsonschematools.configurations.SchemaConfiguration;
import org.openapijsonschematools.schemas.AnyTypeJsonSchema;
import org.openapijsonschematools.schemas.NotAnyTypeJsonSchema;
import org.openapijsonschematools.schemas.StringJsonSchema;
import org.openapijsonschematools.schemas.validation.AdditionalPropertiesValidator;
import org.openapijsonschematools.schemas.validation.FrozenMap;
import org.openapijsonschematools.schemas.validation.JsonSchema;
import org.openapijsonschematools.schemas.validation.KeywordEntry;
import org.openapijsonschematools.schemas.validation.KeywordValidator;
import org.openapijsonschematools.schemas.validation.PropertiesEntry;
import org.openapijsonschematools.schemas.validation.PropertiesValidator;
import org.openapijsonschematools.schemas.validation.RequiredValidator;
import org.openapijsonschematools.schemas.validation.TypeValidator;

public class JSONPatchRequestMoveCopy {
    // nest classes so all schemas and input/output classes can be public
    
    
    public class AdditionalProperties extends NotAnyTypeJsonSchema {}
        // NotAnyTypeSchema
    
    
    public class From extends StringJsonSchema {}
    
    
    public class Path extends StringJsonSchema {}
    
    
    public class Op extends JsonSchema {
        public static final LinkedHashMap<String, KeywordValidator> keywordToValidator = new LinkedHashMap<>(Map.ofEntries(
            new KeywordEntry("type", new TypeValidator(Set.of(
                String.class
            ))
        ));
        public static String validate(String arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(Op.class, arg, configuration);
        }
    }    
    
    public static class JSONPatchRequestMoveCopyMap extends FrozenMap<String, Object> {
        JSONPatchRequestMoveCopyMap(FrozenMap<? extends String, ?> m) {
            super(m);
        }
        public static JSONPatchRequestMoveCopyMap of(Map<String, Object> arg, SchemaConfiguration configuration) {
            return JSONPatchRequestMoveCopy1.validate(arg, configuration);
        }
    }    
    
    public class JSONPatchRequestMoveCopy1 extends JsonSchema {
        /*
        NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
        Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
    
        Do not edit the class manually.
        */
        public static final LinkedHashMap<String, KeywordValidator> keywordToValidator = new LinkedHashMap<>(Map.ofEntries(
            new KeywordEntry("type", new TypeValidator(Set.of(FrozenMap.class)),
            new KeywordEntry("properties", new PropertiesValidator(Map.ofEntries(
                new PropertyEntry("from", From.class),
                new PropertyEntry("path", Path.class),
                new PropertyEntry("op", Op.class)
            )),
        ));
        public static final Set<String> required = new LinkedHashSet<>(Set.of(
            "from",
            "op",
            "path"
        ));
        static final Class<?> additionalProperties = AdditionalProperties.class;
        protected static JSONPatchRequestMoveCopyMap getMapOutputInstance(FrozenMap<? extends String, ?> arg) {
            return new JSONPatchRequestMoveCopyMap(arg);
        }
        public static JSONPatchRequestMoveCopyMap validate(Map<String, Object> arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(JSONPatchRequestMoveCopy1.class, arg, configuration);
        }
    }
}
