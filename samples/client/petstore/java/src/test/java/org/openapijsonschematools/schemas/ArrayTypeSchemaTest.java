package org.openapijsonschematools.schemas;

import org.junit.Assert;
import org.junit.Test;
import org.openapijsonschematools.configurations.JsonSchemaKeywordFlags;
import org.openapijsonschematools.configurations.SchemaConfiguration;
import org.openapijsonschematools.schemas.validation.ItemsValidator;
import org.openapijsonschematools.schemas.validation.JsonSchema;
import org.openapijsonschematools.schemas.validation.FrozenList;
import org.openapijsonschematools.schemas.validation.KeywordEntry;
import org.openapijsonschematools.schemas.validation.KeywordValidator;
import org.openapijsonschematools.schemas.validation.TypeValidator;
import org.openapijsonschematools.exceptions.ValidationException;

import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Set;


public class ArrayTypeSchemaTest {
    static final SchemaConfiguration configuration = new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone());

    public class ArrayWithItemsSchema extends JsonSchema {
        public static final LinkedHashMap<String, KeywordValidator> keywordToValidator = new LinkedHashMap<>(Map.ofEntries(
            new KeywordEntry("type", new TypeValidator(Set.of(FrozenList.class))),
            new KeywordEntry("items", new ItemsValidator(StringJsonSchema.class))
        ));

        public static FrozenList<Object> validate(List<Object> arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(ArrayWithItemsSchema.class, arg, configuration);
        }
    }

    public static class ArrayWithOutputClsSchemaList extends FrozenList<String> {
        ArrayWithOutputClsSchemaList(FrozenList<? extends String> m) {
            super(m);
        }

        public static ArrayWithOutputClsSchemaList of(List<Object> arg, SchemaConfiguration configuration) {
            return ArrayWithOutputClsSchema.validate(arg, configuration);
        }
    }

    public class ArrayWithOutputClsSchema extends JsonSchema {
        public static final LinkedHashMap<String, KeywordValidator> keywordToValidator = new LinkedHashMap<>(Map.ofEntries(
            new KeywordEntry("type", new TypeValidator(Set.of(FrozenList.class))),
            new KeywordEntry("items", new ItemsValidator(StringJsonSchema.class))
        ));

        protected static ArrayWithOutputClsSchemaList getListOutputInstance(FrozenList<? extends String> arg) {
            return new ArrayWithOutputClsSchemaList(arg);
        }

        public static ArrayWithOutputClsSchemaList validate(List<Object> arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(ArrayWithOutputClsSchema.class, arg, configuration);
        }
    }

    @Test
    public void testExceptionThrownForInvalidType() {
        Assert.assertThrows(ValidationException.class, () -> JsonSchema.validateObject(
                ArrayWithItemsSchema.class, (Void) null, configuration
        ));
    }

    @Test
    public void testValidateArrayWithItemsSchema() {
        // map with only item works
        List<Object> inList = new ArrayList<>();
        inList.add("abc");
        FrozenList<Object> validatedValue = ArrayWithItemsSchema.validate(inList, configuration);
        List<Object> outList = new ArrayList<>();
        outList.add("abc");
        Assert.assertEquals(validatedValue, outList);

        // map with no items works
        inList = new ArrayList<>();
        validatedValue = ArrayWithItemsSchema.validate(inList, configuration);
        outList = new ArrayList<>();
        Assert.assertEquals(validatedValue, outList);

        // invalid prop type fails
        inList = new ArrayList<>();
        inList.add(1);
        List<Object> finalInList = inList;
        Assert.assertThrows(ValidationException.class, () -> ArrayWithItemsSchema.validate(
                finalInList, configuration
        ));
    }

    @Test
    public void testValidateArrayWithOutputClsSchema() {
        // map with only item works
        List<Object> inList = new ArrayList<>();
        inList.add("abc");
        ArrayWithOutputClsSchemaList validatedValue = ArrayWithOutputClsSchema.validate(inList, configuration);
        List<Object> outList = new ArrayList<>();
        outList.add("abc");
        Assert.assertEquals(validatedValue, outList);

        // map with no items works
        inList = new ArrayList<>();
        validatedValue = ArrayWithOutputClsSchema.validate(inList, configuration);
        outList = new ArrayList<>();
        Assert.assertEquals(validatedValue, outList);

        // invalid prop type fails
        inList = new ArrayList<>();
        inList.add(1);
        List<Object> finalInList = inList;
        Assert.assertThrows(ValidationException.class, () -> ArrayWithOutputClsSchema.validate(
                finalInList, configuration
        ));
    }
}
