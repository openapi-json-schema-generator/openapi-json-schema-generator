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
import org.openapijsonschematools.schemas.validation.AllOfValidator;
import org.openapijsonschematools.schemas.validation.EnumValidator;
import org.openapijsonschematools.schemas.validation.FrozenList;
import org.openapijsonschematools.schemas.validation.FrozenMap;
import org.openapijsonschematools.schemas.validation.JsonSchema;
import org.openapijsonschematools.schemas.validation.KeywordEntry;
import org.openapijsonschematools.schemas.validation.KeywordValidator;
import org.openapijsonschematools.schemas.validation.PropertiesValidator;
import org.openapijsonschematools.schemas.validation.PropertyEntry;
import org.openapijsonschematools.schemas.validation.TypeValidator;

public class ComplexQuadrilateral {
    // nest classes so all schemas and input/output classes can be public
    
    
    public static class QuadrilateralType extends JsonSchema {
        public static final LinkedHashMap<String, KeywordValidator> keywordToValidator = new LinkedHashMap<>(Map.ofEntries(
            new KeywordEntry("type", new TypeValidator(Set.of(
                String.class
            ))),
            new KeywordEntry("enum", new EnumValidator(Set.of(
                "ComplexQuadrilateral"
            )))
        ));
        public static String validate(String arg, SchemaConfiguration configuration) throws ValidationException {
            return JsonSchema.validate(QuadrilateralType.class, arg, configuration);
        }
    }    
    
    public static class Schema1Map extends FrozenMap<String, Object> {
        Schema1Map(FrozenMap<String, Object> m) {
            super(m);
        }
        public static final Set<String> requiredKeys = Set.of();
        public static final Set<String> optionalKeys = Set.of(
            "quadrilateralType"
        );
        public static Schema1Map of(Map<String, Object> arg, SchemaConfiguration configuration) throws ValidationException {
            return Schema1.validate(arg, configuration);
        }
        
        public String quadrilateralType() {
            String key = "quadrilateralType";
            throwIfKeyNotPresent(key);
            return (String) get(key);
        }
        
        public Object getAdditionalProperty(String name) {
            throwIfKeyKnown(name, requiredKeys, optionalKeys);
            throwIfKeyNotPresent(name);
            return get(name);
        }
    }    
    
    public static class Schema1 extends JsonSchema {
        public static final LinkedHashMap<String, KeywordValidator> keywordToValidator = new LinkedHashMap<>(Map.ofEntries(
            new KeywordEntry("type", new TypeValidator(Set.of(FrozenMap.class))),
            new KeywordEntry("properties", new PropertiesValidator(Map.ofEntries(
                new PropertyEntry("quadrilateralType", QuadrilateralType.class)
            )))
        ));
        
        protected static Schema1Map getMapOutputInstance(FrozenMap<String, Object> arg) {
            return new Schema1Map(arg);
        }
        public static Schema1Map validate(Map<String, Object> arg, SchemaConfiguration configuration) throws ValidationException {
            return JsonSchema.validate(Schema1.class, arg, configuration);
        }
    }
    
    
    public static class ComplexQuadrilateral1 extends JsonSchema {
        /*
        NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
        Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
    
        Do not edit the class manually.
        */
        public static final LinkedHashMap<String, KeywordValidator> keywordToValidator = new LinkedHashMap<>(Map.ofEntries(
            new KeywordEntry("allOf", new AllOfValidator(List.of(
                QuadrilateralInterface.QuadrilateralInterface1.class,
                Schema1.class
            )))
        ));
        public static Void validate(Void arg, SchemaConfiguration configuration) throws ValidationException {
            return JsonSchema.validate(ComplexQuadrilateral1.class, arg, configuration);
        }
        
        public static boolean validate(boolean arg, SchemaConfiguration configuration) throws ValidationException {
            return JsonSchema.validate(ComplexQuadrilateral1.class, arg, configuration);
        }
        
        public static int validate(int arg, SchemaConfiguration configuration) throws ValidationException {
            return JsonSchema.validate(ComplexQuadrilateral1.class, arg, configuration);
        }
        
        public static long validate(long arg, SchemaConfiguration configuration) throws ValidationException {
            return JsonSchema.validate(ComplexQuadrilateral1.class, arg, configuration);
        }
        
        public static float validate(float arg, SchemaConfiguration configuration) throws ValidationException {
            return JsonSchema.validate(ComplexQuadrilateral1.class, arg, configuration);
        }
        
        public static double validate(double arg, SchemaConfiguration configuration) throws ValidationException {
            return JsonSchema.validate(ComplexQuadrilateral1.class, arg, configuration);
        }
        
        public static String validate(String arg, SchemaConfiguration configuration) throws ValidationException {
            return JsonSchema.validate(ComplexQuadrilateral1.class, arg, configuration);
        }
        
        public static String validate(ZonedDateTime arg, SchemaConfiguration configuration) throws ValidationException {
            return JsonSchema.validate(ComplexQuadrilateral1.class, arg, configuration);
        }
        
        public static String validate(LocalDate arg, SchemaConfiguration configuration) throws ValidationException {
            return JsonSchema.validate(ComplexQuadrilateral1.class, arg, configuration);
        }
        
        public static String validate(UUID arg, SchemaConfiguration configuration) throws ValidationException {
            return JsonSchema.validate(ComplexQuadrilateral1.class, arg, configuration);
        }
        
        public static FrozenMap<String, Object> validate(Map<String, Object> arg, SchemaConfiguration configuration) throws ValidationException {
            return JsonSchema.validate(ComplexQuadrilateral1.class, arg, configuration);
        }
        
        public static FrozenList<Object> validate(List<Object> arg, SchemaConfiguration configuration) throws ValidationException {
            return JsonSchema.validate(ComplexQuadrilateral1.class, arg, configuration);
        }
    }}
