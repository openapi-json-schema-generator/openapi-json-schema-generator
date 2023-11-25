package org.openapijsonschematools.components.schemas;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Set;
import org.openapijsonschematools.configurations.SchemaConfiguration;
import org.openapijsonschematools.exceptions.ValidationException;
import org.openapijsonschematools.schemas.validation.FrozenList;
import org.openapijsonschematools.schemas.validation.ItemsValidator;
import org.openapijsonschematools.schemas.validation.JsonSchema;
import org.openapijsonschematools.schemas.validation.KeywordEntry;
import org.openapijsonschematools.schemas.validation.KeywordValidator;
import org.openapijsonschematools.schemas.validation.TypeValidator;

public class SelfReferencingArrayModel {
    // nest classes so all schemas and input/output classes can be public
    
    
    public static class SelfReferencingArrayModelList extends FrozenList<SelfReferencingArrayModelList> {

        SelfReferencingArrayModelList(FrozenList<SelfReferencingArrayModelList> m) {

            super(m);
        }
        public static SelfReferencingArrayModelList of(List<List> arg, SchemaConfiguration configuration) throws ValidationException {
            return SelfReferencingArrayModel1.validate(arg, configuration);
        }
    }
    
    
    public class SelfReferencingArrayModel1 extends JsonSchema {
        /*
        NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
        Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
    
        Do not edit the class manually.
        */
        public static final LinkedHashMap<String, KeywordValidator> keywordToValidator = new LinkedHashMap<>(Map.ofEntries(
            new KeywordEntry("type", new TypeValidator(Set.of(FrozenList.class))),
            new KeywordEntry("items", new ItemsValidator(SelfReferencingArrayModel1.class))
        ));
        protected static SelfReferencingArrayModelList getListOutputInstance(FrozenList<SelfReferencingArrayModelList> arg) {

            return new SelfReferencingArrayModelList(arg);
        }
        public static SelfReferencingArrayModelList validate(List<List> arg, SchemaConfiguration configuration) throws ValidationException {
            return JsonSchema.validate(SelfReferencingArrayModel1.class, arg, configuration);
        }
    }}
