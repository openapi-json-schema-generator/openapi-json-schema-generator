package org.openapijsonschematools.components.schemas;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Set;
import org.openapijsonschematools.configurations.SchemaConfiguration;
import org.openapijsonschematools.exceptions.ValidationException;
import org.openapijsonschematools.schemas.validation.FormatValidator;
import org.openapijsonschematools.schemas.validation.FrozenList;
import org.openapijsonschematools.schemas.validation.ItemsValidator;
import org.openapijsonschematools.schemas.validation.JsonSchema;
import org.openapijsonschematools.schemas.validation.KeywordEntry;
import org.openapijsonschematools.schemas.validation.KeywordValidator;
import org.openapijsonschematools.schemas.validation.TypeValidator;

public class ArrayWithValidationsInItems {
    // nest classes so all schemas and input/output classes can be public
    
    
    public static class Items extends JsonSchema {
        public static final LinkedHashMap<String, KeywordValidator> keywordToValidator = new LinkedHashMap<>(Map.ofEntries(
            new KeywordEntry("type", new TypeValidator(Set.of(
                Integer.class,
                Long.class,
                Float.class,
                Double.class
            ))),
            new KeywordEntry("format", new FormatValidator("int64"))
        ));
        public static long validate(int arg, SchemaConfiguration configuration) throws ValidationException {
            return JsonSchema.validate(Items.class, Long.valueOf(arg), configuration);
        }
        
        public static long validate(float arg, SchemaConfiguration configuration) throws ValidationException {
            return JsonSchema.validate(Items.class, Long.parseLong(String.valueOf(arg)), configuration);
        }
        
        public static long validate(long arg, SchemaConfiguration configuration) throws ValidationException {
            return JsonSchema.validate(Items.class, arg, configuration);
        }
        
        public static long validate(double arg, SchemaConfiguration configuration) throws ValidationException {
            return JsonSchema.validate(Items.class, Long.parseLong(String.valueOf(arg)), configuration);
        }
    }    
    
    public static class ArrayWithValidationsInItemsList extends FrozenList<Long> {
        ArrayWithValidationsInItemsList(FrozenList<Long> m) {
            super(m);
        }
        public static ArrayWithValidationsInItemsList of(List<Long> arg, SchemaConfiguration configuration) throws ValidationException {
            return ArrayWithValidationsInItems1.validate(arg, configuration);
        }
    }
    
    
    public static class ArrayWithValidationsInItems1 extends JsonSchema {
        /*
        NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
        Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
    
        Do not edit the class manually.
        */
        public static final LinkedHashMap<String, KeywordValidator> keywordToValidator = new LinkedHashMap<>(Map.ofEntries(
            new KeywordEntry("type", new TypeValidator(Set.of(FrozenList.class))),
            new KeywordEntry("items", new ItemsValidator(Items.class))
            
        ));
        protected static ArrayWithValidationsInItemsList getListOutputInstance(FrozenList<Long> arg) {
            return new ArrayWithValidationsInItemsList(arg);
        }
        public static ArrayWithValidationsInItemsList validate(List<Long> arg, SchemaConfiguration configuration) throws ValidationException {
            return JsonSchema.validate(ArrayWithValidationsInItems1.class, arg, configuration);
        }
    }}
