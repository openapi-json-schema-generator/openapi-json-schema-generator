package org.openapijsonschematools.components.schemas;
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

public class MixedPropertiesAndAdditionalPropertiesClass {
    // nest classes so all schemas and input/output classes can be public
    
    
    public class UuidSchema implements JsonSchema {
        static final LinkedHashSet<Class<?>> type = new LinkedHashSet<>(Set.of(
            String.class
        ));
        static final String format = "uuid";
        public static String validate(String arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(UuidSchema.class, arg, configuration);
        }
    }    
    
    public class DateTime implements JsonSchema {
        static final LinkedHashSet<Class<?>> type = new LinkedHashSet<>(Set.of(
            String.class
        ));
        static final String format = "date-time";
        public static String validate(String arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(DateTime.class, arg, configuration);
        }
    }    
    
    public class MapSchema implements JsonSchema {
        static final LinkedHashSet<Class<?>> type = new LinkedHashSet<>(Set.of(
            FrozenMap.class
        ));
        static final Class<?> additionalProperties = Animal.Animal1.class;
        public static <T extends FrozenMap> T validate(Map<String, Object> arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(MapSchema.class, arg, configuration);
        }
    }
    
    
    public class MixedPropertiesAndAdditionalPropertiesClass1 implements JsonSchema {
        /*
        NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
        Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
    
        Do not edit the class manually.
        */
        static final LinkedHashSet<Class<?>> type = new LinkedHashSet<>(Set.of(
            FrozenMap.class
        ));
        static LinkedHashMap<String, Class<?>> properties = new LinkedHashMap<>(Map.ofEntries(
            new AbstractMap.SimpleEntry<String, Class<?>>("uuid", UuidSchema.class),
            new AbstractMap.SimpleEntry<String, Class<?>>("dateTime", DateTime.class),
            new AbstractMap.SimpleEntry<String, Class<?>>("map", MapSchema.class)
        ));
        public static <T extends FrozenMap> T validate(Map<String, Object> arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(MixedPropertiesAndAdditionalPropertiesClass1.class, arg, configuration);
        }
    }
}
