package org.openapijsonschematools.components.schemas;
import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Set;
import org.openapijsonschematools.configurations.SchemaConfiguration;
import org.openapijsonschematools.schemas.validation.FrozenList;
import org.openapijsonschematools.schemas.validation.FrozenMap;
import org.openapijsonschematools.schemas.validation.ItemsValidator;
import org.openapijsonschematools.schemas.validation.JsonSchema;
import org.openapijsonschematools.schemas.validation.KeywordEntry;
import org.openapijsonschematools.schemas.validation.KeywordValidator;
import org.openapijsonschematools.schemas.validation.PropertiesValidator;
import org.openapijsonschematools.schemas.validation.PropertyEntry;
import org.openapijsonschematools.schemas.validation.TypeValidator;

public class EnumArrays {
    // nest classes so all schemas and input/output classes can be public
    
    
    public class JustSymbol extends JsonSchema {
        public static final LinkedHashMap<String, KeywordValidator> keywordToValidator = new LinkedHashMap<>(Map.ofEntries(
            new KeywordEntry("type", new TypeValidator(Set.of(
                String.class
            )))
        ));
        public static String validate(String arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(JustSymbol.class, arg, configuration);
        }
    }    
    
    public class Items extends JsonSchema {
        public static final LinkedHashMap<String, KeywordValidator> keywordToValidator = new LinkedHashMap<>(Map.ofEntries(
            new KeywordEntry("type", new TypeValidator(Set.of(
                String.class
            )))
        ));
        public static String validate(String arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(Items.class, arg, configuration);
        }
    }    
    
    public static class ArrayEnumList extends FrozenList<String> {

        ArrayEnumList(FrozenList<String> m) {

            super(m);
        }
        public static ArrayEnumList of(List<String> arg, SchemaConfiguration configuration) {

            return ArrayEnum.validate(arg, configuration);
        }
    }
    
    
    public class ArrayEnumListInput extends ArrayList<String> {

    }
    
    
    public class ArrayEnum extends JsonSchema {
        public static final LinkedHashMap<String, KeywordValidator> keywordToValidator = new LinkedHashMap<>(Map.ofEntries(
            new KeywordEntry("type", new TypeValidator(Set.of(FrozenList.class))),
            new KeywordEntry("items", new ItemsValidator(Items.class))
        ));
        protected static ArrayEnumList getListOutputInstance(FrozenList<String> arg) {

            return new ArrayEnumList(arg);
        }
        public static ArrayEnumList validate(List<String> arg, SchemaConfiguration configuration) {

            return JsonSchema.validate(ArrayEnum.class, arg, configuration);
        }
    }    
    
    public static class EnumArraysMap extends FrozenMap<String, Object> {
        EnumArraysMap(FrozenMap<? extends String, ?> m) {
            super(m);
        }
        public static EnumArraysMap of(Map<String, Object> arg, SchemaConfiguration configuration) {
            return EnumArrays1.validate(arg, configuration);
        }
    }    
    
    public class EnumArrays1 extends JsonSchema {
        /*
        NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
        Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
    
        Do not edit the class manually.
        */
        public static final LinkedHashMap<String, KeywordValidator> keywordToValidator = new LinkedHashMap<>(Map.ofEntries(
            new KeywordEntry("type", new TypeValidator(Set.of(FrozenMap.class))),
            new KeywordEntry("properties", new PropertiesValidator(Map.ofEntries(
                new PropertyEntry("just_symbol", JustSymbol.class),
                new PropertyEntry("array_enum", ArrayEnum.class)
            )))
        ));
        protected static EnumArraysMap getMapOutputInstance(FrozenMap<? extends String, ?> arg) {
            return new EnumArraysMap(arg);
        }
        public static EnumArraysMap validate(Map<String, Object> arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(EnumArrays1.class, arg, configuration);
        }
    }
}
