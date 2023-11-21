package org.openapijsonschematools.components.schemas;
import java.time.LocalDate;
import java.time.ZonedDateTime;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Set;
import org.openapijsonschematools.configurations.SchemaConfiguration;
import org.openapijsonschematools.schemas.MapJsonSchema;
import org.openapijsonschematools.schemas.validation.AdditionalPropertiesValidator;
import org.openapijsonschematools.schemas.validation.FormatValidator;
import org.openapijsonschematools.schemas.validation.FrozenList;
import org.openapijsonschematools.schemas.validation.FrozenMap;
import org.openapijsonschematools.schemas.validation.ItemsValidator;
import org.openapijsonschematools.schemas.validation.JsonSchema;
import org.openapijsonschematools.schemas.validation.KeywordEntry;
import org.openapijsonschematools.schemas.validation.KeywordValidator;
import org.openapijsonschematools.schemas.validation.PropertiesValidator;
import org.openapijsonschematools.schemas.validation.PropertyEntry;
import org.openapijsonschematools.schemas.validation.TypeValidator;

public class NullableClass {
    // nest classes so all schemas and input/output classes can be public
    
    
    public class AdditionalProperties3 extends JsonSchema {
        public static final LinkedHashMap<String, KeywordValidator> keywordToValidator = new LinkedHashMap<>(Map.ofEntries(
            new KeywordEntry("type", new TypeValidator(Set.of(
                Void.class,
                FrozenMap.class
            )))
        ));
        public static Void validate(Void arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(AdditionalProperties3.class, arg, configuration);
        }
        public static <T extends FrozenMap> T validate(Map<String, Object> arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(AdditionalProperties3.class, arg, configuration);
        }
    }    
    
    public class IntegerProp extends JsonSchema {
        public static final LinkedHashMap<String, KeywordValidator> keywordToValidator = new LinkedHashMap<>(Map.ofEntries(
            new KeywordEntry("type", new TypeValidator(Set.of(
                Void.class,
                Integer.class,
                Long.class,
                Float.class,
                Double.class
            )))
        ));
        public static Void validate(Void arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(IntegerProp.class, arg, configuration);
        }
        public static Long validate(Integer arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(IntegerProp.class, Long.valueOf(arg), configuration);
        }
        
        public static Long validate(Float arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(IntegerProp.class, Long.parseLong(arg.toString()), configuration);
        }
        
        public static Long validate(Long arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(IntegerProp.class, arg, configuration);
        }
        
        public static Long validate(Double arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(IntegerProp.class, Long.parseLong(arg.toString()), configuration);
        }
    }    
    
    public class NumberProp extends JsonSchema {
        public static final LinkedHashMap<String, KeywordValidator> keywordToValidator = new LinkedHashMap<>(Map.ofEntries(
            new KeywordEntry("type", new TypeValidator(Set.of(
                Void.class,
                Integer.class,
                Long.class,
                Float.class,
                Double.class
            )))
        ));
        public static Void validate(Void arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(NumberProp.class, arg, configuration);
        }
        public static Number validate(Integer arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(NumberProp.class, arg, configuration);
        }
        
        public static Number validate(Long arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(NumberProp.class, arg, configuration);
        }
        
        public static Number validate(Float arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(NumberProp.class, arg, configuration);
        }
        
        public static Number validate(Double arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(NumberProp.class, arg, configuration);
        }
    }    
    
    public class BooleanProp extends JsonSchema {
        public static final LinkedHashMap<String, KeywordValidator> keywordToValidator = new LinkedHashMap<>(Map.ofEntries(
            new KeywordEntry("type", new TypeValidator(Set.of(
                Void.class,
                Boolean.class
            )))
        ));
        public static Void validate(Void arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(BooleanProp.class, arg, configuration);
        }
        public static Boolean validate(Boolean arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(BooleanProp.class, arg, configuration);
        }
    }    
    
    public class StringProp extends JsonSchema {
        public static final LinkedHashMap<String, KeywordValidator> keywordToValidator = new LinkedHashMap<>(Map.ofEntries(
            new KeywordEntry("type", new TypeValidator(Set.of(
                Void.class,
                String.class
            )))
        ));
        public static Void validate(Void arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(StringProp.class, arg, configuration);
        }
        public static String validate(String arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(StringProp.class, arg, configuration);
        }
    }    
    
    public class DateProp extends JsonSchema {
        public static final LinkedHashMap<String, KeywordValidator> keywordToValidator = new LinkedHashMap<>(Map.ofEntries(
            new KeywordEntry("type", new TypeValidator(Set.of(
                Void.class,
                String.class
            ))),
            new KeywordEntry("format", new FormatValidator("date"))
        ));
        public static Void validate(Void arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(DateProp.class, arg, configuration);
        }
        public static String validate(String arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(DateProp.class, arg, configuration);
        }
    }    
    
    public class DatetimeProp extends JsonSchema {
        public static final LinkedHashMap<String, KeywordValidator> keywordToValidator = new LinkedHashMap<>(Map.ofEntries(
            new KeywordEntry("type", new TypeValidator(Set.of(
                Void.class,
                String.class
            ))),
            new KeywordEntry("format", new FormatValidator("date-time"))
        ));
        public static Void validate(Void arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(DatetimeProp.class, arg, configuration);
        }
        public static String validate(String arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(DatetimeProp.class, arg, configuration);
        }
    }    
    
    public class Items extends MapJsonSchema {}
    
    
    public static class ArrayNullablePropList extends FrozenList<Object> {
        ArrayNullablePropList(FrozenList<Object> m) {
            super(m);
        }
    }    
    
    public class ArrayNullableProp extends JsonSchema {
        public static final LinkedHashMap<String, KeywordValidator> keywordToValidator = new LinkedHashMap<>(Map.ofEntries(
            new KeywordEntry("type", new TypeValidator(Set.of(
                Void.class,
                FrozenList.class
            ))),
            new KeywordEntry("items", new ItemsValidator(Items.class))
        ));
        public static Void validate(Void arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(ArrayNullableProp.class, arg, configuration);
        }
        public static ArrayNullablePropList validate(List<Object> arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(ArrayNullableProp.class, arg, configuration);
        }
    }    
    
    public class Items1 extends JsonSchema {
        public static final LinkedHashMap<String, KeywordValidator> keywordToValidator = new LinkedHashMap<>(Map.ofEntries(
            new KeywordEntry("type", new TypeValidator(Set.of(
                Void.class,
                FrozenMap.class
            )))
        ));
        public static Void validate(Void arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(Items1.class, arg, configuration);
        }
        public static <T extends FrozenMap> T validate(Map<String, Object> arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(Items1.class, arg, configuration);
        }
    }    
    
    public static class ArrayAndItemsNullablePropList extends FrozenList<Object> {
        ArrayAndItemsNullablePropList(FrozenList<Object> m) {
            super(m);
        }
    }    
    
    public class ArrayAndItemsNullableProp extends JsonSchema {
        public static final LinkedHashMap<String, KeywordValidator> keywordToValidator = new LinkedHashMap<>(Map.ofEntries(
            new KeywordEntry("type", new TypeValidator(Set.of(
                Void.class,
                FrozenList.class
            ))),
            new KeywordEntry("items", new ItemsValidator(Items1.class))
        ));
        public static Void validate(Void arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(ArrayAndItemsNullableProp.class, arg, configuration);
        }
        public static ArrayAndItemsNullablePropList validate(List<Object> arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(ArrayAndItemsNullableProp.class, arg, configuration);
        }
    }    
    
    public class Items2 extends JsonSchema {
        public static final LinkedHashMap<String, KeywordValidator> keywordToValidator = new LinkedHashMap<>(Map.ofEntries(
            new KeywordEntry("type", new TypeValidator(Set.of(
                Void.class,
                FrozenMap.class
            )))
        ));
        public static Void validate(Void arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(Items2.class, arg, configuration);
        }
        public static <T extends FrozenMap> T validate(Map<String, Object> arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(Items2.class, arg, configuration);
        }
    }    
    
    public static class ArrayItemsNullableList extends FrozenList<Object> {
        ArrayItemsNullableList(FrozenList<Object> m) {
            super(m);
        }
    }    
    
    public class ArrayItemsNullable extends JsonSchema {
        public static final LinkedHashMap<String, KeywordValidator> keywordToValidator = new LinkedHashMap<>(Map.ofEntries(
            new KeywordEntry("type", new TypeValidator(Set.of(FrozenList.class))),
            new KeywordEntry("items", new ItemsValidator(Items2.class))
        ));
        protected static ArrayItemsNullableList getListOutputInstance(FrozenList<Object> arg) {
            return new ArrayItemsNullableList(arg);
        }
        public static ArrayItemsNullableList validate(List<Object> arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(ArrayItemsNullable.class, arg, configuration);
        }
    }    
    
    public class AdditionalProperties extends MapJsonSchema {}
    
    
    public static class ObjectNullablePropMap extends FrozenMap<String, Object> {
        ObjectNullablePropMap(FrozenMap<? extends String, ?> m) {
            super(m);
        }
        public static ObjectNullablePropMap of(Map<String, Object> arg, SchemaConfiguration configuration) {
            return ObjectNullableProp.validate(arg, configuration);
        }
    }    
    
    public class ObjectNullableProp extends JsonSchema {
        public static final LinkedHashMap<String, KeywordValidator> keywordToValidator = new LinkedHashMap<>(Map.ofEntries(
            new KeywordEntry("type", new TypeValidator(Set.of(
                Void.class,
                FrozenMap.class
            ))),
            new KeywordEntry("additionalProperties", new AdditionalPropertiesValidator(AdditionalProperties.class))
        ));
        public static Void validate(Void arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(ObjectNullableProp.class, arg, configuration);
        }
        public static ObjectNullablePropMap validate(Map<String, Object> arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(ObjectNullableProp.class, arg, configuration);
        }
    }    
    
    public class AdditionalProperties1 extends JsonSchema {
        public static final LinkedHashMap<String, KeywordValidator> keywordToValidator = new LinkedHashMap<>(Map.ofEntries(
            new KeywordEntry("type", new TypeValidator(Set.of(
                Void.class,
                FrozenMap.class
            )))
        ));
        public static Void validate(Void arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(AdditionalProperties1.class, arg, configuration);
        }
        public static <T extends FrozenMap> T validate(Map<String, Object> arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(AdditionalProperties1.class, arg, configuration);
        }
    }    
    
    public static class ObjectAndItemsNullablePropMap extends FrozenMap<String, Object> {
        ObjectAndItemsNullablePropMap(FrozenMap<? extends String, ?> m) {
            super(m);
        }
        public static ObjectAndItemsNullablePropMap of(Map<String, Object> arg, SchemaConfiguration configuration) {
            return ObjectAndItemsNullableProp.validate(arg, configuration);
        }
    }    
    
    public class ObjectAndItemsNullableProp extends JsonSchema {
        public static final LinkedHashMap<String, KeywordValidator> keywordToValidator = new LinkedHashMap<>(Map.ofEntries(
            new KeywordEntry("type", new TypeValidator(Set.of(
                Void.class,
                FrozenMap.class
            ))),
            new KeywordEntry("additionalProperties", new AdditionalPropertiesValidator(AdditionalProperties1.class))
        ));
        public static Void validate(Void arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(ObjectAndItemsNullableProp.class, arg, configuration);
        }
        public static ObjectAndItemsNullablePropMap validate(Map<String, Object> arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(ObjectAndItemsNullableProp.class, arg, configuration);
        }
    }    
    
    public class AdditionalProperties2 extends JsonSchema {
        public static final LinkedHashMap<String, KeywordValidator> keywordToValidator = new LinkedHashMap<>(Map.ofEntries(
            new KeywordEntry("type", new TypeValidator(Set.of(
                Void.class,
                FrozenMap.class
            )))
        ));
        public static Void validate(Void arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(AdditionalProperties2.class, arg, configuration);
        }
        public static <T extends FrozenMap> T validate(Map<String, Object> arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(AdditionalProperties2.class, arg, configuration);
        }
    }    
    
    public static class ObjectItemsNullableMap extends FrozenMap<String, Object> {
        ObjectItemsNullableMap(FrozenMap<? extends String, ?> m) {
            super(m);
        }
        public static ObjectItemsNullableMap of(Map<String, Object> arg, SchemaConfiguration configuration) {
            return ObjectItemsNullable.validate(arg, configuration);
        }
    }    
    
    public class ObjectItemsNullable extends JsonSchema {
        public static final LinkedHashMap<String, KeywordValidator> keywordToValidator = new LinkedHashMap<>(Map.ofEntries(
            new KeywordEntry("type", new TypeValidator(Set.of(FrozenMap.class))),
            new KeywordEntry("additionalProperties", new AdditionalPropertiesValidator(AdditionalProperties2.class))
        ));
        protected static ObjectItemsNullableMap getMapOutputInstance(FrozenMap<? extends String, ?> arg) {
            return new ObjectItemsNullableMap(arg);
        }
        public static ObjectItemsNullableMap validate(Map<String, Object> arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(ObjectItemsNullable.class, arg, configuration);
        }
    }
    
    
    public static class NullableClassMap extends FrozenMap<String, Object> {
        NullableClassMap(FrozenMap<? extends String, ?> m) {
            super(m);
        }
        public static NullableClassMap of(Map<String, Object> arg, SchemaConfiguration configuration) {
            return NullableClass1.validate(arg, configuration);
        }
    }    
    
    public class NullableClass1 extends JsonSchema {
        /*
        NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
        Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
    
        Do not edit the class manually.
        */
        public static final LinkedHashMap<String, KeywordValidator> keywordToValidator = new LinkedHashMap<>(Map.ofEntries(
            new KeywordEntry("type", new TypeValidator(Set.of(FrozenMap.class))),
            new KeywordEntry("properties", new PropertiesValidator(Map.ofEntries(
                new PropertyEntry("integer_prop", IntegerProp.class),
                new PropertyEntry("number_prop", NumberProp.class),
                new PropertyEntry("boolean_prop", BooleanProp.class),
                new PropertyEntry("string_prop", StringProp.class),
                new PropertyEntry("date_prop", DateProp.class),
                new PropertyEntry("datetime_prop", DatetimeProp.class),
                new PropertyEntry("array_nullable_prop", ArrayNullableProp.class),
                new PropertyEntry("array_and_items_nullable_prop", ArrayAndItemsNullableProp.class),
                new PropertyEntry("array_items_nullable", ArrayItemsNullable.class),
                new PropertyEntry("object_nullable_prop", ObjectNullableProp.class),
                new PropertyEntry("object_and_items_nullable_prop", ObjectAndItemsNullableProp.class),
                new PropertyEntry("object_items_nullable", ObjectItemsNullable.class)
            ))),
            new KeywordEntry("additionalProperties", new AdditionalPropertiesValidator(AdditionalProperties3.class))
        ));
        protected static NullableClassMap getMapOutputInstance(FrozenMap<? extends String, ?> arg) {
            return new NullableClassMap(arg);
        }
        public static NullableClassMap validate(Map<String, Object> arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(NullableClass1.class, arg, configuration);
        }
    }
}
