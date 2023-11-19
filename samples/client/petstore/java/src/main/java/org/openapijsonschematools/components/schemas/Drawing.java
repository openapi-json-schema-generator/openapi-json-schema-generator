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
import org.openapijsonschematools.schemas.JsonSchema;

public class Drawing {
    // nest classes so all schemas and input/output classes can be public
    
    
    public static class ShapesTuple extends FrozenList<Object> {
        ShapesTuple(FrozenList<Object> m) {
            super(m);
        }
    }    
    
    public class Shapes implements JsonSchema {
        static final LinkedHashSet<Class<?>> type = new LinkedHashSet<>(Set.of(
            FrozenList.class
        ));
        static final Class<?> items = Shape.Shape1.class;
        public static <U extends FrozenList> U validate(List<Object> arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(Shapes.class, arg, configuration);
        }
    }    
    
    public static class DrawingMap extends FrozenMap<String, Object> {
        DrawingMap(FrozenMap<? extends String, ?> m) {
            super(m);
        }
        public static DrawingMap of(Map<String, Object> arg, SchemaConfiguration configuration) {
            return Drawing1.validate(arg, configuration);
        }
    }    
    
    public class Drawing1 implements JsonSchema {
        /*
        NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
        Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
    
        Do not edit the class manually.
        */
        static final LinkedHashSet<Class<?>> type = new LinkedHashSet<>(Set.of(
            FrozenMap.class
        ));
        static final LinkedHashMap<String, Class<?>> properties = new LinkedHashMap<>(Map.ofEntries(
            new AbstractMap.SimpleEntry<String, Class<?>>("mainShape", Shape.Shape1.class),
            new AbstractMap.SimpleEntry<String, Class<?>>("shapeOrNull", ShapeOrNull.ShapeOrNull1.class),
            new AbstractMap.SimpleEntry<String, Class<?>>("nullableShape", NullableShape.NullableShape1.class),
            new AbstractMap.SimpleEntry<String, Class<?>>("shapes", Shapes.class)
        ));
        static final Class<?> additionalProperties = Fruit.Fruit1.class;
        protected static DrawingMap getMapOutputInstance(FrozenMap<? extends String, ?> arg) {
            return new DrawingMap(arg);
        }
        public static <T extends FrozenMap> T validate(Map<String, Object> arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(Drawing1.class, arg, configuration);
        }
    }
}
