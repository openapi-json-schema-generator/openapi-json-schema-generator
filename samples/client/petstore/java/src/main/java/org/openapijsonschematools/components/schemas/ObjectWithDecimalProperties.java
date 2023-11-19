package org.openapijsonschematools.components.schemas;
import java.util.AbstractMap;
import java.util.LinkedHashMap;
import java.util.LinkedHashSet;
import java.util.Map;
import java.util.Set;
import org.openapijsonschematools.configurations.SchemaConfiguration;
import org.openapijsonschematools.schemas.DecimalJsonSchema;
import org.openapijsonschematools.schemas.FrozenMap;
import org.openapijsonschematools.schemas.JsonSchema;

public class ObjectWithDecimalProperties {
    // nest classes so all schemas and input/output classes can be public
    
    
    public class Width extends DecimalJsonSchema {}
    
    
    class ObjectWithDecimalPropertiesMap extends FrozenMap<String, Object> {
        ObjectWithDecimalPropertiesMap(FrozenMap<? extends String, ?> m) {
            super(m);
        }
    }    
    
    public class ObjectWithDecimalProperties1 implements JsonSchema {
        /*
        NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
        Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
    
        Do not edit the class manually.
        */
        static final LinkedHashSet<Class<?>> type = new LinkedHashSet<>(Set.of(
            FrozenMap.class
        ));
        static final LinkedHashMap<String, Class<?>> properties = new LinkedHashMap<>(Map.ofEntries(
            new AbstractMap.SimpleEntry<String, Class<?>>("length", DecimalPayload.DecimalPayload1.class),
            new AbstractMap.SimpleEntry<String, Class<?>>("width", Width.class),
            new AbstractMap.SimpleEntry<String, Class<?>>("cost", Money.Money1.class)
        ));
        public static <T extends FrozenMap> T validate(Map<String, Object> arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(ObjectWithDecimalProperties1.class, arg, configuration);
        }
    }
}
