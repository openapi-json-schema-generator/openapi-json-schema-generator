package org.openapijsonschematools.components.schemas;
import java.time.LocalDate;
import java.time.ZonedDateTime;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.UUID;
import org.openapijsonschematools.configurations.SchemaConfiguration;
import org.openapijsonschematools.exceptions.ValidationException;
import org.openapijsonschematools.schemas.StringJsonSchema;
import org.openapijsonschematools.schemas.validation.FrozenList;
import org.openapijsonschematools.schemas.validation.FrozenMap;
import org.openapijsonschematools.schemas.validation.JsonSchema;
import org.openapijsonschematools.schemas.validation.KeywordEntry;
import org.openapijsonschematools.schemas.validation.KeywordValidator;
import org.openapijsonschematools.schemas.validation.PropertiesValidator;
import org.openapijsonschematools.schemas.validation.PropertyEntry;
import org.openapijsonschematools.schemas.validation.RequiredValidator;
import org.openapijsonschematools.schemas.validation.TypeValidator;

public class TriangleInterface {
    // nest classes so all schemas and input/output classes can be public
    
    
    public class ShapeType extends JsonSchema {
        public static final LinkedHashMap<String, KeywordValidator> keywordToValidator = new LinkedHashMap<>(Map.ofEntries(
            new KeywordEntry("type", new TypeValidator(Set.of(
                String.class
            )))
        ));
        public static String validate(String arg, SchemaConfiguration configuration) throws ValidationException {
            return JsonSchema.validate(ShapeType.class, arg, configuration);
        }
    }    
    
    public class TriangleType extends StringJsonSchema {}
    
    
    public static class TriangleInterfaceMap extends FrozenMap<String, Object
        TriangleInterfaceMap(FrozenMap<String, Object
            super(m);
        }
        public static final Set<String> requiredKeys = Set.of(
            "shapeType",
            "triangleType"
        );
        public static final Set<String> optionalKeys = Set.of();
        public static TriangleInterfaceMap of(Map<String, Object> arg, SchemaConfiguration configuration) throws ValidationException {
            return TriangleInterface1.validate(arg, configuration);
        }
        
        public String
            return (String
        }
        
        public String
            return (String
        }
        
        public Object getAdditionalProperty(String name) {
            throwIfKeyKnown(name, requiredKeys, optionalKeys);
            throwIfKeyNotPresent(name);
            return get(name);
        }
    }    
    
    public class TriangleInterface1 extends JsonSchema {
        /*
        NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
        Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
    
        Do not edit the class manually.
        */
        public static final LinkedHashMap<String, KeywordValidator> keywordToValidator = new LinkedHashMap<>(Map.ofEntries(
            new KeywordEntry("properties", new PropertiesValidator(Map.ofEntries(
                new PropertyEntry("shapeType", ShapeType.class),
                new PropertyEntry("triangleType", TriangleType.class)
            ))),
            new KeywordEntry("required", new RequiredValidator(Set.of(
                "shapeType",
                "triangleType"
            )))
        ));
        public static Void validate(Void arg, SchemaConfiguration configuration) throws ValidationException {
            return JsonSchema.validate(TriangleInterface1.class, arg, configuration);
        }
        
        public static boolean validate(boolean arg, SchemaConfiguration configuration) throws ValidationException {
            return JsonSchema.validate(TriangleInterface1.class, arg, configuration);
        }
        
        public static int validate(int arg, SchemaConfiguration configuration) throws ValidationException {
            return JsonSchema.validate(TriangleInterface1.class, arg, configuration);
        }
        
        public static long validate(long arg, SchemaConfiguration configuration) throws ValidationException {
            return JsonSchema.validate(TriangleInterface1.class, arg, configuration);
        }
        
        public static float validate(float arg, SchemaConfiguration configuration) throws ValidationException {
            return JsonSchema.validate(TriangleInterface1.class, arg, configuration);
        }
        
        public static double validate(double arg, SchemaConfiguration configuration) throws ValidationException {
            return JsonSchema.validate(TriangleInterface1.class, arg, configuration);
        }
        
        public static String validate(String arg, SchemaConfiguration configuration) throws ValidationException {
            return JsonSchema.validate(TriangleInterface1.class, arg, configuration);
        }
        
        public static String validate(ZonedDateTime arg, SchemaConfiguration configuration) throws ValidationException {
            return JsonSchema.validate(TriangleInterface1.class, arg, configuration);
        }
        
        public static String validate(LocalDate arg, SchemaConfiguration configuration) throws ValidationException {
            return JsonSchema.validate(TriangleInterface1.class, arg, configuration);
        }
        
        public static String validate(UUID arg, SchemaConfiguration configuration) throws ValidationException {
            return JsonSchema.validate(TriangleInterface1.class, arg, configuration);
        }
        
        public static <T extends FrozenMap> T validate(Map<String, Object> arg, SchemaConfiguration configuration) throws ValidationException {
            return JsonSchema.validate(TriangleInterface1.class, arg, configuration);
        }
        
        public static <U extends FrozenList> U validate(List<Object> arg, SchemaConfiguration configuration) throws ValidationException {
            return JsonSchema.validate(TriangleInterface1.class, arg, configuration);
        }
    }}
