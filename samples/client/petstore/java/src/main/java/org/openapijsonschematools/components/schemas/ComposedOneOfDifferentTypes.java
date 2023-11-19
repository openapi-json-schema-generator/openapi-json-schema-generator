package org.openapijsonschematools.components.schemas;
import java.time.LocalDate;
import java.time.ZonedDateTime;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.UUID;
import org.openapijsonschematools.configurations.SchemaConfiguration;
import org.openapijsonschematools.schemas.AnyTypeJsonSchema;
import org.openapijsonschematools.schemas.DateJsonSchema;
import org.openapijsonschematools.schemas.FrozenList;
import org.openapijsonschematools.schemas.FrozenMap;
import org.openapijsonschematools.schemas.JsonSchema;
import org.openapijsonschematools.schemas.NullJsonSchema;

public class ComposedOneOfDifferentTypes {
    // nest classes so all schemas and input/output classes can be public
    
    
    public class Schema2 extends NullJsonSchema {}
    
    
    public class Schema3 extends DateJsonSchema {}
    
    
    public class Schema4 implements JsonSchema {
        static final LinkedHashSet<Class<?>> type = new LinkedHashSet<>(Set.of(
            FrozenMap.class
        ));
        public static <T extends FrozenMap> T validate(Map<String, Object> arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(Schema4.class, arg, configuration);
        }
    }
    
    
    public class Items extends AnyTypeJsonSchema {}
    
    
    public static class Schema5Tuple extends FrozenList<Object> {
        Schema5Tuple(FrozenList<Object> m) {
            super(m);
        }
    }    
    
    public class Schema5 implements JsonSchema {
        static final LinkedHashSet<Class<?>> type = new LinkedHashSet<>(Set.of(
            FrozenList.class
        ));
        static final Class<?> items = Items.class;
        public static <U extends FrozenList> U validate(List<Object> arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(Schema5.class, arg, configuration);
        }
    }    
    
    public class Schema6 implements JsonSchema {
        static final LinkedHashSet<Class<?>> type = new LinkedHashSet<>(Set.of(
            String.class
        ));
        static final String format = "date-time";
        public static String validate(String arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(Schema6.class, arg, configuration);
        }
    }    
    
    public class ComposedOneOfDifferentTypes1 implements JsonSchema {
        /*
        NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
        Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
    
        Do not edit the class manually.
    
        this is a model that allows payloads of type object or number
        */
        public static Void validate(Void arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(ComposedOneOfDifferentTypes1.class, arg, configuration);
        }
        
        public static Boolean validate(Boolean arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(ComposedOneOfDifferentTypes1.class, arg, configuration);
        }
        
        public static Integer validate(Integer arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(ComposedOneOfDifferentTypes1.class, arg, configuration);
        }
        
        public static Long validate(Long arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(ComposedOneOfDifferentTypes1.class, arg, configuration);
        }
        
        public static Float validate(Float arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(ComposedOneOfDifferentTypes1.class, arg, configuration);
        }
        
        public static Double validate(Double arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(ComposedOneOfDifferentTypes1.class, arg, configuration);
        }
        
        public static String validate(String arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(ComposedOneOfDifferentTypes1.class, arg, configuration);
        }
        
        public static String validate(ZonedDateTime arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(ComposedOneOfDifferentTypes1.class, arg, configuration);
        }
        
        public static String validate(LocalDate arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(ComposedOneOfDifferentTypes1.class, arg, configuration);
        }
        
        public static String validate(UUID arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(ComposedOneOfDifferentTypes1.class, arg, configuration);
        }
        
        public static <T extends FrozenMap> T validate(Map<String, Object> arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(ComposedOneOfDifferentTypes1.class, arg, configuration);
        }
        
        public static <U extends FrozenList> U validate(List<Object> arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(ComposedOneOfDifferentTypes1.class, arg, configuration);
        }
    }}
