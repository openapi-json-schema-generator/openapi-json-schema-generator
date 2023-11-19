package org.openapijsonschematools.components.schemas;
import java.util.AbstractMap;
import java.util.LinkedHashMap;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;
import org.openapijsonschematools.configurations.SchemaConfiguration;
import org.openapijsonschematools.schemas.FrozenList;
import org.openapijsonschematools.schemas.FrozenMap;
import org.openapijsonschematools.schemas.Int64JsonSchema;
import org.openapijsonschematools.schemas.JsonSchema;
import org.openapijsonschematools.schemas.StringJsonSchema;

public class Pet {
    // nest classes so all schemas and input/output classes can be public
    
    
    public class Id extends Int64JsonSchema {}
    
    
    public class Name extends StringJsonSchema {}
    
    
    public class Items extends StringJsonSchema {}
    
    
    public static class PhotoUrlsTuple extends FrozenList<Object> {
        PhotoUrlsTuple(FrozenList<Object> m) {
            super(m);
        }
    }    
    
    public class PhotoUrls implements JsonSchema {
        static final LinkedHashSet<Class<?>> type = new LinkedHashSet<>(Set.of(
            FrozenList.class
        ));
        static final Class<?> items = Items.class;
        public static <U extends FrozenList> U validate(List<Object> arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(PhotoUrls.class, arg, configuration);
        }
    }    
    
    public class Status implements JsonSchema {
        static final LinkedHashSet<Class<?>> type = new LinkedHashSet<>(Set.of(
            String.class
        ));
        public static String validate(String arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(Status.class, arg, configuration);
        }
    }    
    
    public static class TagsTuple extends FrozenList<Object> {
        TagsTuple(FrozenList<Object> m) {
            super(m);
        }
    }    
    
    public class Tags implements JsonSchema {
        static final LinkedHashSet<Class<?>> type = new LinkedHashSet<>(Set.of(
            FrozenList.class
        ));
        static final Class<?> items = Tag.Tag1.class;
        public static <U extends FrozenList> U validate(List<Object> arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(Tags.class, arg, configuration);
        }
    }    
    
    public static class PetMap extends FrozenMap<String, Object> {
        PetMap(FrozenMap<? extends String, ?> m) {
            super(m);
        }
        public static PetMap of(Map<String, Object> arg, SchemaConfiguration configuration) {
            return Pet1.validate(arg, configuration);
        }
    }    
    
    public class Pet1 implements JsonSchema {
        /*
        NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
        Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
    
        Do not edit the class manually.
    
        Pet object that needs to be added to the store
        */
        static final LinkedHashSet<Class<?>> type = new LinkedHashSet<>(Set.of(
            FrozenMap.class
        ));
        static final LinkedHashMap<String, Class<?>> properties = new LinkedHashMap<>(Map.ofEntries(
            new AbstractMap.SimpleEntry<String, Class<?>>("id", Id.class),
            new AbstractMap.SimpleEntry<String, Class<?>>("category", Category.Category1.class),
            new AbstractMap.SimpleEntry<String, Class<?>>("name", Name.class),
            new AbstractMap.SimpleEntry<String, Class<?>>("photoUrls", PhotoUrls.class),
            new AbstractMap.SimpleEntry<String, Class<?>>("tags", Tags.class),
            new AbstractMap.SimpleEntry<String, Class<?>>("status", Status.class)
        ));
        static final Set<String> required = new LinkedHashSet<>(Set.of(
            "name",
            "photoUrls"
        ));
        protected static PetMap getMapOutputInstance(FrozenMap<? extends String, ?> arg) {
            return new PetMap(arg);
        }
        public static <T extends FrozenMap> T validate(Map<String, Object> arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(Pet1.class, arg, configuration);
        }
    }
}
