package org.openapijsonschematools.components.schemas;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.Set;
import org.openapijsonschematools.configurations.SchemaConfiguration;
import org.openapijsonschematools.schemas.validation.FormatValidator;
import org.openapijsonschematools.schemas.validation.FrozenMap;
import org.openapijsonschematools.schemas.validation.JsonSchema;
import org.openapijsonschematools.schemas.validation.KeywordEntry;
import org.openapijsonschematools.schemas.validation.KeywordValidator;
import org.openapijsonschematools.schemas.validation.PropertiesValidator;
import org.openapijsonschematools.schemas.validation.PropertyEntry;
import org.openapijsonschematools.schemas.validation.RequiredValidator;
import org.openapijsonschematools.schemas.validation.TypeValidator;

public class EnumTest {
    // nest classes so all schemas and input/output classes can be public
    
    
    public class EnumString extends JsonSchema {
        public static final LinkedHashMap<String, KeywordValidator> keywordToValidator = new LinkedHashMap<>(Map.ofEntries(
            new KeywordEntry("type", new TypeValidator(Set.of(
                String.class
            )))
        ));
        public static String validate(String arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(EnumString.class, arg, configuration);
        }
    }    
    
    public class EnumStringRequired extends JsonSchema {
        public static final LinkedHashMap<String, KeywordValidator> keywordToValidator = new LinkedHashMap<>(Map.ofEntries(
            new KeywordEntry("type", new TypeValidator(Set.of(
                String.class
            )))
        ));
        public static String validate(String arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(EnumStringRequired.class, arg, configuration);
        }
    }    
    
    public class EnumInteger extends JsonSchema {
        public static final LinkedHashMap<String, KeywordValidator> keywordToValidator = new LinkedHashMap<>(Map.ofEntries(
            new KeywordEntry("type", new TypeValidator(Set.of(
                Integer.class,
                Long.class,
                Float.class,
                Double.class
            ))),
            new KeywordEntry("format", new FormatValidator("int32"))
        ));
        public static long validate(int arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(EnumInteger.class, Long.valueOf(arg), configuration);
        }
        
        public static long validate(float arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(EnumInteger.class, Long.parseLong(String.valueOf(arg)), configuration);
        }
        
        public static long validate(long arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(EnumInteger.class, arg, configuration);
        }
        
        public static long validate(double arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(EnumInteger.class, Long.parseLong(String.valueOf(arg)), configuration);
        }
    }    
    
    public class EnumNumber extends JsonSchema {
        public static final LinkedHashMap<String, KeywordValidator> keywordToValidator = new LinkedHashMap<>(Map.ofEntries(
            new KeywordEntry("type", new TypeValidator(Set.of(
                Integer.class,
                Long.class,
                Float.class,
                Double.class
            ))),
            new KeywordEntry("format", new FormatValidator("double"))
        ));
        public static double validate(double arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(EnumNumber.class, arg, configuration);
        }
    }    
    
    public static class EnumTestMap extends FrozenMap<String, Object> {

        EnumTestMap(FrozenMap<String, Object> m) {

            super(m);
        }
        public static final Set<String> requiredKeys = Set.of(
            "enum_string_required"
        );
        public static final Set<String> optionalKeys = Set.of(
            "enum_string",
            "enum_integer",
            "enum_number",
            "stringEnum",
            "IntegerEnum",
            "StringEnumWithDefaultValue",
            "IntegerEnumWithDefaultValue",
            "IntegerEnumOneValue"
        );
        public static EnumTestMap of(Map<String, Object> arg, SchemaConfiguration configuration) {

            return EnumTest1.validate(arg, configuration);
        }
        
        public String enum_string_required() {

            return (String) get("enum_string_required");

        }
        
        public String enum_string() {

            String key = "enum_string";
            throwIfKeyNotPresent(key);
            return (String) get(key);

        }
        
        public int enum_integer() {

            String key = "enum_integer";
            throwIfKeyNotPresent(key);
            return (int) get(key);

        }
        
        public double enum_number() {

            String key = "enum_number";
            throwIfKeyNotPresent(key);
            return (double) get(key);

        }
        
        public String stringEnum() {

            String key = "stringEnum";
            throwIfKeyNotPresent(key);
            return (String) get(key);

        }
        
        public long IntegerEnum() {

            String key = "IntegerEnum";
            throwIfKeyNotPresent(key);
            return (long) get(key);

        }
        
        public String StringEnumWithDefaultValue() {

            String key = "StringEnumWithDefaultValue";
            throwIfKeyNotPresent(key);
            return (String) get(key);

        }
        
        public long IntegerEnumWithDefaultValue() {

            String key = "IntegerEnumWithDefaultValue";
            throwIfKeyNotPresent(key);
            return (long) get(key);

        }
        
        public long IntegerEnumOneValue() {

            String key = "IntegerEnumOneValue";
            throwIfKeyNotPresent(key);
            return (long) get(key);

        }
        
        public Object getAdditionalProperty(String name) {
            throwIfKeyKnown(name, requiredKeys, optionalKeys);
            throwIfKeyNotPresent(name);
            return get(name);
        }
    }    
    
    public class EnumTest1 extends JsonSchema {
        /*
        NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
        Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
    
        Do not edit the class manually.
        */
        public static final LinkedHashMap<String, KeywordValidator> keywordToValidator = new LinkedHashMap<>(Map.ofEntries(
            new KeywordEntry("type", new TypeValidator(Set.of(FrozenMap.class))),
            new KeywordEntry("properties", new PropertiesValidator(Map.ofEntries(
                new PropertyEntry("enum_string", EnumString.class),
                new PropertyEntry("enum_string_required", EnumStringRequired.class),
                new PropertyEntry("enum_integer", EnumInteger.class),
                new PropertyEntry("enum_number", EnumNumber.class),
                new PropertyEntry("stringEnum", StringEnum.StringEnum1.class),
                new PropertyEntry("IntegerEnum", IntegerEnum.IntegerEnum1.class),
                new PropertyEntry("StringEnumWithDefaultValue", StringEnumWithDefaultValue.StringEnumWithDefaultValue1.class),
                new PropertyEntry("IntegerEnumWithDefaultValue", IntegerEnumWithDefaultValue.IntegerEnumWithDefaultValue1.class),
                new PropertyEntry("IntegerEnumOneValue", IntegerEnumOneValue.IntegerEnumOneValue1.class)
            ))),
            new KeywordEntry("required", new RequiredValidator(Set.of(
                "enum_string_required"
            )))
        ));
        protected static EnumTestMap getMapOutputInstance(FrozenMap<String, Object> arg) {

            return new EnumTestMap(arg);
        }
        public static EnumTestMap validate(Map<String, Object> arg, SchemaConfiguration configuration) {

            return JsonSchema.validate(EnumTest1.class, arg, configuration);
        }
    }
}
