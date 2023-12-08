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

public class RefInItems {
    // nest classes so all schemas and input/output classes can be public
    
    
    public static class RefInItemsList extends FrozenList<Object> {
        RefInItemsList(FrozenList<Object> m) {
            super(m);
        }
        public static RefInItemsList of(List<Object> arg, SchemaConfiguration configuration) throws ValidationException {
            return RefInItems1.validate(arg, configuration);
        }
    }
    
    public class RefInItemsListInput {
        // class to build List<Object>
    }
    
    
    public static class RefInItems1 extends JsonSchema {
        /*
        NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
        Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
    
        Do not edit the class manually.
        */
        public static final LinkedHashMap<String, KeywordValidator> keywordToValidator = new LinkedHashMap<>(Map.ofEntries(
            new KeywordEntry("type", new TypeValidator(Set.of(FrozenList.class))),
            new KeywordEntry("items", new ItemsValidator(PropertyNamedRefThatIsNotAReference.PropertyNamedRefThatIsNotAReference1.class))
        ));
        
        protected static RefInItemsList getListOutputInstance(FrozenList<Object> arg) {
            return new RefInItemsList(arg);
        }
        public RefInItemsList validate(List<Object> arg, SchemaConfiguration configuration) throws ValidationException {
            return validateList(arg, configuration);
        }
    }}
