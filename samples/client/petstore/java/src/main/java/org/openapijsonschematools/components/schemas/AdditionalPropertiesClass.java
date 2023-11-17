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

public class AdditionalPropertiesClass {
    // nest classes so all schemas and input/output classes can be public
    
    
    public class AdditionalProperties implements JsonSchema {
        static final LinkedHashSet<Class<?>> type = new LinkedHashSet<>(Set.of(
            String.class
        ));
        public static String validate(String arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(AdditionalProperties.class, arg, configuration);
        }
    }    
    
    public class MapProperty implements JsonSchema {
        static final LinkedHashSet<Class<?>> type = new LinkedHashSet<>(Set.of(
            FrozenMap.class
        ));
        static final Class<?> additionalProperties = AdditionalProperties.class;
        public static <T extends FrozenMap> T validate(Map<String, Object> arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(MapProperty.class, arg, configuration);
        }
    }
    
    
    public class AdditionalProperties2 implements JsonSchema {
        static final LinkedHashSet<Class<?>> type = new LinkedHashSet<>(Set.of(
            String.class
        ));
        public static String validate(String arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(AdditionalProperties2.class, arg, configuration);
        }
    }    
    
    public class AdditionalProperties1 implements JsonSchema {
        static final LinkedHashSet<Class<?>> type = new LinkedHashSet<>(Set.of(
            FrozenMap.class
        ));
        static final Class<?> additionalProperties = AdditionalProperties2.class;
        public static <T extends FrozenMap> T validate(Map<String, Object> arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(AdditionalProperties1.class, arg, configuration);
        }
    }
    
    
    public class MapOfMapProperty implements JsonSchema {
        static final LinkedHashSet<Class<?>> type = new LinkedHashSet<>(Set.of(
            FrozenMap.class
        ));
        static final Class<?> additionalProperties = AdditionalProperties1.class;
        public static <T extends FrozenMap> T validate(Map<String, Object> arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(MapOfMapProperty.class, arg, configuration);
        }
    }
    
    
    public class Anytype1 implements JsonSchema {
        public static Void validate(Void arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(JsonSchemas.AnyTypeSchema.class, arg, configuration);
        }
    
        public static Boolean validate(Boolean arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(JsonSchemas.AnyTypeSchema.class, arg, configuration);
        }
    
        public static Integer validate(Integer arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(JsonSchemas.AnyTypeSchema.class, arg, configuration);
        }
    
        public static Long validate(Long arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(JsonSchemas.AnyTypeSchema.class, arg, configuration);
        }
    
        public static Float validate(Float arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(JsonSchemas.AnyTypeSchema.class, arg, configuration);
        }
    
        public static Double validate(Double arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(JsonSchemas.AnyTypeSchema.class, arg, configuration);
        }
    
        public static String validate(String arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(JsonSchemas.AnyTypeSchema.class, arg, configuration);
        }
    
        public static String validate(ZonedDateTime arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(JsonSchemas.AnyTypeSchema.class, arg, configuration);
        }
    
        public static String validate(LocalDate arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(JsonSchemas.AnyTypeSchema.class, arg, configuration);
        }
    
        public static <T extends FrozenMap> T validate(Map<String, Object> arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(JsonSchemas.AnyTypeSchema.class, arg, configuration);
        }
    
        public static <U extends FrozenList> U validate(List<Object> arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(JsonSchemas.AnyTypeSchema.class, arg, configuration);
        }
    }
    
    
    public class MapWithUndeclaredPropertiesAnytype1 implements JsonSchema {
        public static FrozenMap<String, Object> validate(Map<String, Object> arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(JsonSchemas.MapSchema.class, arg, configuration);
        }
    }
    
    
    public class MapWithUndeclaredPropertiesAnytype2 implements JsonSchema {
        public static FrozenMap<String, Object> validate(Map<String, Object> arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(JsonSchemas.MapSchema.class, arg, configuration);
        }
    }
    
    
    public class AdditionalProperties3 implements JsonSchema {
        public static Void validate(Void arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(JsonSchemas.AnyTypeSchema.class, arg, configuration);
        }
    
        public static Boolean validate(Boolean arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(JsonSchemas.AnyTypeSchema.class, arg, configuration);
        }
    
        public static Integer validate(Integer arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(JsonSchemas.AnyTypeSchema.class, arg, configuration);
        }
    
        public static Long validate(Long arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(JsonSchemas.AnyTypeSchema.class, arg, configuration);
        }
    
        public static Float validate(Float arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(JsonSchemas.AnyTypeSchema.class, arg, configuration);
        }
    
        public static Double validate(Double arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(JsonSchemas.AnyTypeSchema.class, arg, configuration);
        }
    
        public static String validate(String arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(JsonSchemas.AnyTypeSchema.class, arg, configuration);
        }
    
        public static String validate(ZonedDateTime arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(JsonSchemas.AnyTypeSchema.class, arg, configuration);
        }
    
        public static String validate(LocalDate arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(JsonSchemas.AnyTypeSchema.class, arg, configuration);
        }
    
        public static <T extends FrozenMap> T validate(Map<String, Object> arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(JsonSchemas.AnyTypeSchema.class, arg, configuration);
        }
    
        public static <U extends FrozenList> U validate(List<Object> arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(JsonSchemas.AnyTypeSchema.class, arg, configuration);
        }
    }
    
    
    public class MapWithUndeclaredPropertiesAnytype3 implements JsonSchema {
        static final LinkedHashSet<Class<?>> type = new LinkedHashSet<>(Set.of(
            FrozenMap.class
        ));
        static final Class<?> additionalProperties = AdditionalProperties3.class;
        public static <T extends FrozenMap> T validate(Map<String, Object> arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(MapWithUndeclaredPropertiesAnytype3.class, arg, configuration);
        }
    }
    
    
    public class AdditionalProperties4 implements JsonSchema {
        // NotAnyTypeSchema
    }
    
    
    public class EmptyMap implements JsonSchema {
        static final LinkedHashSet<Class<?>> type = new LinkedHashSet<>(Set.of(
            FrozenMap.class
        ));
        static final Class<?> additionalProperties = AdditionalProperties4.class;
        public static <T extends FrozenMap> T validate(Map<String, Object> arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(EmptyMap.class, arg, configuration);
        }
    }
    
    
    public class AdditionalProperties5 implements JsonSchema {
        static final LinkedHashSet<Class<?>> type = new LinkedHashSet<>(Set.of(
            String.class
        ));
        public static String validate(String arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(AdditionalProperties5.class, arg, configuration);
        }
    }    
    
    public class MapWithUndeclaredPropertiesString implements JsonSchema {
        static final LinkedHashSet<Class<?>> type = new LinkedHashSet<>(Set.of(
            FrozenMap.class
        ));
        static final Class<?> additionalProperties = AdditionalProperties5.class;
        public static <T extends FrozenMap> T validate(Map<String, Object> arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(MapWithUndeclaredPropertiesString.class, arg, configuration);
        }
    }
    
    
    public class AdditionalPropertiesClass1 implements JsonSchema {
        /*
        NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
        Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
    
        Do not edit the class manually.
        */
        static final LinkedHashSet<Class<?>> type = new LinkedHashSet<>(Set.of(
            FrozenMap.class
        ));
        static final LinkedHashMap<String, Class<?>> properties = new LinkedHashMap<>(Map.ofEntries(
            new AbstractMap.SimpleEntry<String, Class<?>>("map_property", MapProperty.class),
            new AbstractMap.SimpleEntry<String, Class<?>>("map_of_map_property", MapOfMapProperty.class),
            new AbstractMap.SimpleEntry<String, Class<?>>("anytype_1", Anytype1.class),
            new AbstractMap.SimpleEntry<String, Class<?>>("map_with_undeclared_properties_anytype_1", MapWithUndeclaredPropertiesAnytype1.class),
            new AbstractMap.SimpleEntry<String, Class<?>>("map_with_undeclared_properties_anytype_2", MapWithUndeclaredPropertiesAnytype2.class),
            new AbstractMap.SimpleEntry<String, Class<?>>("map_with_undeclared_properties_anytype_3", MapWithUndeclaredPropertiesAnytype3.class),
            new AbstractMap.SimpleEntry<String, Class<?>>("empty_map", EmptyMap.class),
            new AbstractMap.SimpleEntry<String, Class<?>>("map_with_undeclared_properties_string", MapWithUndeclaredPropertiesString.class)
        ));
        public static <T extends FrozenMap> T validate(Map<String, Object> arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(AdditionalPropertiesClass1.class, arg, configuration);
        }
    }
}
