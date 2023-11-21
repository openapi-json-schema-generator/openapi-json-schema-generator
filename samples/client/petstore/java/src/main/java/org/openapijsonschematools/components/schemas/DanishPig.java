package org.openapijsonschematools.components.schemas;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.Set;
import org.openapijsonschematools.configurations.SchemaConfiguration;
import org.openapijsonschematools.schemas.validation.FrozenMap;
import org.openapijsonschematools.schemas.validation.JsonSchema;
import org.openapijsonschematools.schemas.validation.KeywordEntry;
import org.openapijsonschematools.schemas.validation.KeywordValidator;
import org.openapijsonschematools.schemas.validation.PropertiesEntry;
import org.openapijsonschematools.schemas.validation.PropertiesValidator;
import org.openapijsonschematools.schemas.validation.RequiredValidator;
import org.openapijsonschematools.schemas.validation.TypeValidator;

public class DanishPig {
    // nest classes so all schemas and input/output classes can be public
    
    
    public class ClassName extends JsonSchema {
        public static final LinkedHashMap<String, KeywordValidator> keywordToValidator = new LinkedHashMap<>(Map.ofEntries(
            new KeywordEntry("type", new TypeValidator(Set.of(
                String.class
            ))
        ));
        public static String validate(String arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(ClassName.class, arg, configuration);
        }
    }    
    
    public static class DanishPigMap extends FrozenMap<String, Object> {
        DanishPigMap(FrozenMap<? extends String, ?> m) {
            super(m);
        }
        public static DanishPigMap of(Map<String, Object> arg, SchemaConfiguration configuration) {
            return DanishPig1.validate(arg, configuration);
        }
    }    
    
    public class DanishPig1 extends JsonSchema {
        /*
        NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
        Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
    
        Do not edit the class manually.
        */
        public static final LinkedHashMap<String, KeywordValidator> keywordToValidator = new LinkedHashMap<>(Map.ofEntries(
            new KeywordEntry("type", new TypeValidator(Set.of(FrozenMap.class)),
            new KeywordEntry("properties", new PropertiesValidator(Map.ofEntries(
                new PropertyEntry("className", ClassName.class)
            )),
        ));
        public static final Set<String> required = new LinkedHashSet<>(Set.of(
            "className"
        ));
        protected static DanishPigMap getMapOutputInstance(FrozenMap<? extends String, ?> arg) {
            return new DanishPigMap(arg);
        }
        public static DanishPigMap validate(Map<String, Object> arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(DanishPig1.class, arg, configuration);
        }
    }
}
