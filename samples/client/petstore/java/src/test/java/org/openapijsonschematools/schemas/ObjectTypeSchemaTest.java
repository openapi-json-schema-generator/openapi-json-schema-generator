package org.openapijsonschematools.schemas;

import org.junit.Assert;
import org.junit.Test;
import org.openapijsonschematools.configurations.JsonSchemaKeywordFlags;
import org.openapijsonschematools.configurations.SchemaConfiguration;
import org.openapijsonschematools.schemas.validation.JsonSchema;
import org.openapijsonschematools.schemas.validation.FrozenMap;

import java.util.LinkedHashMap;
import java.util.LinkedHashSet;
import java.util.AbstractMap;
import java.util.Map;
import java.util.Set;


public class ObjectTypeSchemaTest {
    static final SchemaConfiguration configuration = new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone());

    public class ObjectWithPropsSchema extends JsonSchema {
        public static final LinkedHashSet<Class<?>> type = new LinkedHashSet<>(Set.of(
            FrozenMap.class
        ));
        public static final LinkedHashMap<String, Class<?>> properties = new LinkedHashMap<>(Map.ofEntries(
            new AbstractMap.SimpleEntry<String, Class<?>>("someString", StringJsonSchema.class)
        ));

        public static FrozenMap<String, Object> validate(Map<String, Object> arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(ObjectWithPropsSchema.class, arg, configuration);
        }
    }

    public class ObjectWithAddpropsSchema extends JsonSchema {
        public static final LinkedHashSet<Class<?>> type = new LinkedHashSet<>(Set.of(
            FrozenMap.class
        ));
        public static final Class<?> additionalProperties = StringJsonSchema.class;

        public static FrozenMap<String, Object> validate(Map<String, Object> arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(ObjectWithAddpropsSchema.class, arg, configuration);
        }
    }

    public class ObjectWithPropsAndAddpropsSchema extends JsonSchema {
        public static final LinkedHashSet<Class<?>> type = new LinkedHashSet<>(Set.of(
            FrozenMap.class
        ));
        public static final LinkedHashMap<String, Class<?>> properties = new LinkedHashMap<>(Map.ofEntries(
            new AbstractMap.SimpleEntry<String, Class<?>>("someString", StringJsonSchema.class)
        ));
        public static final Class<?> additionalProperties = BooleanJsonSchema.class;

        public static FrozenMap<String, Object> validate(Map<String, Object> arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(ObjectWithPropsAndAddpropsSchema.class, arg, configuration);
        }
    }

    public static class ObjectWithOutputTypeSchemaMap extends FrozenMap<String, Object> {
        ObjectWithOutputTypeSchemaMap(FrozenMap<? extends String, ?> m) {
            super(m);
        }

        public static ObjectWithOutputTypeSchemaMap of(Map<String, Object> arg, SchemaConfiguration configuration) {
            return ObjectWithOutputTypeSchema.validate(arg, configuration);
        }
    }


    public class ObjectWithOutputTypeSchema extends JsonSchema {
        public static final LinkedHashSet<Class<?>> type = new LinkedHashSet<>(Set.of(
            FrozenMap.class
        ));
        public static final LinkedHashMap<String, Class<?>> properties = new LinkedHashMap<>(Map.ofEntries(
            new AbstractMap.SimpleEntry<String, Class<?>>("someString", StringJsonSchema.class)
        ));

        protected static ObjectWithOutputTypeSchemaMap getMapOutputInstance(FrozenMap<? extends String, ?> arg) {
            return new ObjectWithOutputTypeSchemaMap(arg);
        }

        public static ObjectWithOutputTypeSchemaMap validate(Map<String, Object> arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(ObjectWithOutputTypeSchema.class, arg, configuration);
        }
    }

    @Test
    public void testExceptionThrownForInvalidType() {
        Assert.assertThrows(RuntimeException.class, () -> JsonSchema.validateObject(
                ObjectWithPropsSchema.class, (Void) null, configuration
        ));
    }

    @Test
    public void testValidateObjectWithPropsSchema() {
        // map with only property works
        Map<String, Object> inMap = new LinkedHashMap<>();
        inMap.put("someString", "abc");
        FrozenMap<String, Object> validatedValue = ObjectWithPropsSchema.validate(inMap, configuration);
        LinkedHashMap<String, String> outMap = new LinkedHashMap<>();
        outMap.put("someString", "abc");
        Assert.assertEquals(validatedValue, outMap);

        // map with additional unvalidated property works
        inMap = new LinkedHashMap<>();
        inMap.put("someString", "abc");
        inMap.put("someOtherString", "def");
        validatedValue = ObjectWithPropsSchema.validate(inMap, configuration);
        outMap = new LinkedHashMap<>();
        outMap.put("someString", "abc");
        outMap.put("someOtherString", "def");
        Assert.assertEquals(validatedValue, outMap);

        // invalid prop type fails
        inMap = new LinkedHashMap<>();
        inMap.put("someString", 1);
        Map<String, Object> finalInMap = inMap;
        Assert.assertThrows(RuntimeException.class, () -> ObjectWithPropsSchema.validate(
                finalInMap, configuration
        ));
    }

    @Test
    public void testValidateObjectWithAddpropsSchema() {
        // map with only property works
        Map<String, Object> inMap = new LinkedHashMap<>();
        inMap.put("someString", "abc");
        FrozenMap<String, Object> validatedValue = ObjectWithAddpropsSchema.validate(inMap, configuration);
        LinkedHashMap<String, String> outMap = new LinkedHashMap<>();
        outMap.put("someString", "abc");
        Assert.assertEquals(validatedValue, outMap);

        // map with additional properties works
        inMap = new LinkedHashMap<>();
        inMap.put("someString", "abc");
        inMap.put("someOtherString", "def");
        validatedValue = ObjectWithAddpropsSchema.validate(inMap, configuration);
        outMap = new LinkedHashMap<>();
        outMap.put("someString", "abc");
        outMap.put("someOtherString", "def");
        Assert.assertEquals(validatedValue, outMap);

        // invalid addProp type fails
        inMap = new LinkedHashMap<>();
        inMap.put("someString", 1);
        Map<String, Object> finalInMap = inMap;
        Assert.assertThrows(RuntimeException.class, () -> ObjectWithAddpropsSchema.validate(
                finalInMap, configuration
        ));
    }

    @Test
    public void testValidateObjectWithPropsAndAddpropsSchema() {
        // map with only property works
        Map<String, Object> inMap = new LinkedHashMap<>();
        inMap.put("someString", "abc");
        FrozenMap<String, Object> validatedValue = ObjectWithPropsAndAddpropsSchema.validate(inMap, configuration);
        LinkedHashMap<String, Object> outMap = new LinkedHashMap<>();
        outMap.put("someString", "abc");
        Assert.assertEquals(validatedValue, outMap);

        // map with additional properties works
        inMap = new LinkedHashMap<>();
        inMap.put("someString", "abc");
        inMap.put("someAddProp", true);
        validatedValue = ObjectWithPropsAndAddpropsSchema.validate(inMap, configuration);
        outMap = new LinkedHashMap<>();
        outMap.put("someString", "abc");
        outMap.put("someAddProp", true);
        Assert.assertEquals(validatedValue, outMap);

        // invalid prop type fails
        inMap = new LinkedHashMap<>();
        inMap.put("someString", 1);
        Map<String, Object> invalidPropMap = inMap;
        Assert.assertThrows(RuntimeException.class, () -> ObjectWithPropsAndAddpropsSchema.validate(
                invalidPropMap, configuration
        ));

        // invalid addProp type fails
        inMap = new LinkedHashMap<>();
        inMap.put("someAddProp", 1);
        Map<String, Object> invalidAddpropMap = inMap;
        Assert.assertThrows(RuntimeException.class, () -> ObjectWithPropsAndAddpropsSchema.validate(
                invalidAddpropMap, configuration
        ));
    }

    @Test
    public void testValidateObjectWithOutputTypeSchema() {
        // map with only property works
        Map<String, Object> inMap = new LinkedHashMap<>();
        inMap.put("someString", "abc");
        ObjectWithOutputTypeSchemaMap validatedValue = ObjectWithOutputTypeSchema.validate(inMap, configuration);
        LinkedHashMap<String, String> outMap = new LinkedHashMap<>();
        outMap.put("someString", "abc");
        Assert.assertEquals(validatedValue, outMap);

        // map with additional unvalidated property works
        inMap = new LinkedHashMap<>();
        inMap.put("someString", "abc");
        inMap.put("someOtherString", "def");
        validatedValue = ObjectWithOutputTypeSchema.validate(inMap, configuration);
        outMap = new LinkedHashMap<>();
        outMap.put("someString", "abc");
        outMap.put("someOtherString", "def");
        Assert.assertEquals(validatedValue, outMap);

        // invalid prop type fails
        inMap = new LinkedHashMap<>();
        inMap.put("someString", 1);
        Map<String, Object> finalInMap = inMap;
        Assert.assertThrows(RuntimeException.class, () -> ObjectWithOutputTypeSchema.validate(
                finalInMap, configuration
        ));

        // using output class directly works
        inMap = new LinkedHashMap<>();
        inMap.put("someString", "abc");
        validatedValue = ObjectWithOutputTypeSchemaMap.of(inMap, configuration);
        outMap = new LinkedHashMap<>();
        outMap.put("someString", "abc");
        Assert.assertEquals(validatedValue, outMap);
    }
}
