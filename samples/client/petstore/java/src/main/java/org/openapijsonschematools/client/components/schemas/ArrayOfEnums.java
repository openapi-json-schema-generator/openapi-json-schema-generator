package org.openapijsonschematools.client.components.schemas;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Set;
import org.openapijsonschematools.client.configurations.SchemaConfiguration;
import org.openapijsonschematools.client.exceptions.ValidationException;
import org.openapijsonschematools.client.schemas.validation.FrozenList;
import org.openapijsonschematools.client.schemas.validation.ItemsValidator;
import org.openapijsonschematools.client.schemas.validation.JsonSchema;
import org.openapijsonschematools.client.schemas.validation.KeywordEntry;
import org.openapijsonschematools.client.schemas.validation.KeywordValidator;
import org.openapijsonschematools.client.schemas.validation.TypeValidator;

public class ArrayOfEnums {
    // nest classes so all schemas and input/output classes can be public
    
    
    public static class ArrayOfEnumsList extends FrozenList<String> {
        ArrayOfEnumsList(FrozenList<String> m) {
            super(m);
        }
        public static ArrayOfEnumsList of(ArrayOfEnumsListInput arg, SchemaConfiguration configuration) throws ValidationException {
            return ArrayOfEnums1.validate(arg, configuration);
        }
    }
    
    public interface ArrayOfEnumsListInput extends List<String> {}
    
    
    public static class ArrayOfEnums1 extends JsonSchema {
        /*
        NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
        Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
    
        Do not edit the class manually.
        */
        public static final LinkedHashMap<String, KeywordValidator> keywordToValidator = new LinkedHashMap<>(Map.ofEntries(
            new KeywordEntry("type", new TypeValidator(Set.of(FrozenList.class))),
            new KeywordEntry("items", new ItemsValidator(StringEnum.StringEnum1.class))
        ));
        
        protected static ArrayOfEnumsList getListOutputInstance(FrozenList<String> arg) {
            return new ArrayOfEnumsList(arg);
        }
        public static ArrayOfEnumsList validate(ArrayOfEnumsListInput arg, SchemaConfiguration configuration) throws ValidationException {
            return JsonSchema.validateList(ArrayOfEnums1.class, arg, configuration);
        }
    }}
