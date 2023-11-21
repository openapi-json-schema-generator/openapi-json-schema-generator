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
import org.openapijsonschematools.schemas.validation.TypeValidator;

public class Foo {
    // nest classes so all schemas and input/output classes can be public
    
    
    public static class FooMap extends FrozenMap<String, Object> {
        FooMap(FrozenMap<? extends String, ?> m) {
            super(m);
        }
        public static FooMap of(Map<String, Object> arg, SchemaConfiguration configuration) {
            return Foo1.validate(arg, configuration);
        }
    }    
    
    public class Foo1 extends JsonSchema {
        /*
        NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
        Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
    
        Do not edit the class manually.
        */
        public static final LinkedHashMap<String, KeywordValidator> keywordToValidator = new LinkedHashMap<>(Map.ofEntries(
            new KeywordEntry("type", new TypeValidator(Set.of(FrozenMap.class)),
            new KeywordEntry("properties", new PropertiesValidator(Map.ofEntries(
                new PropertyEntry("bar", Bar.Bar1.class)
            ))
        ));
        protected static FooMap getMapOutputInstance(FrozenMap<? extends String, ?> arg) {
            return new FooMap(arg);
        }
        public static FooMap validate(Map<String, Object> arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(Foo1.class, arg, configuration);
        }
    }
}
