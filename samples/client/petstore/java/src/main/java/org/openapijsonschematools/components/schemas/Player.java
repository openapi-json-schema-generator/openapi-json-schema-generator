package org.openapijsonschematools.components.schemas;
import java.util.AbstractMap;
import java.util.LinkedHashMap;
import java.util.LinkedHashSet;
import java.util.Map;
import java.util.Set;
import org.openapijsonschematools.configurations.SchemaConfiguration;
import org.openapijsonschematools.schemas.StringJsonSchema;
import org.openapijsonschematools.schemas.validation.FrozenMap;
import org.openapijsonschematools.schemas.validation.JsonSchema;

public class Player {
    // nest classes so all schemas and input/output classes can be public
    
    
    public class Name extends StringJsonSchema {}
    
    
    public static class PlayerMap extends FrozenMap<String, Object> {
        PlayerMap(FrozenMap<? extends String, ?> m) {
            super(m);
        }
        public static PlayerMap of(Map<String, Object> arg, SchemaConfiguration configuration) {
            return Player1.validate(arg, configuration);
        }
    }    
    
    public class Player1 extends JsonSchema {
        /*
        NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
        Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
    
        Do not edit the class manually.
    
        a model that includes a self reference this forces properties and additionalProperties to be lazy loaded in python models because the Player class has not fully loaded when defining properties
        */
        public static final LinkedHashSet<Class<?>> type = new LinkedHashSet<>(Set.of(
            FrozenMap.class
        ));
        public static final LinkedHashMap<String, Class<?>> properties = new LinkedHashMap<>(Map.ofEntries(
            new AbstractMap.SimpleEntry<String, Class<?>>("name", Name.class),
            new AbstractMap.SimpleEntry<String, Class<?>>("enemyPlayer", Player1.class)
        ));
        protected static PlayerMap getMapOutputInstance(FrozenMap<? extends String, ?> arg) {
            return new PlayerMap(arg);
        }
        public static PlayerMap validate(Map<String, Object> arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(Player1.class, arg, configuration);
        }
    }
}
