package org.openapijsonschematools.paths.fake.get.parameters.parameter2;
import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Set;
import org.openapijsonschematools.configurations.SchemaConfiguration;
import org.openapijsonschematools.schemas.validation.FrozenList;
import org.openapijsonschematools.schemas.validation.ItemsValidator;
import org.openapijsonschematools.schemas.validation.JsonSchema;
import org.openapijsonschematools.schemas.validation.KeywordEntry;
import org.openapijsonschematools.schemas.validation.KeywordValidator;
import org.openapijsonschematools.schemas.validation.TypeValidator;

public class Schema2 {
    // nest classes so all schemas and input/output classes can be public
    
    
    public class Items2 extends JsonSchema {
        public static final LinkedHashMap<String, KeywordValidator> keywordToValidator = new LinkedHashMap<>(Map.ofEntries(
            new KeywordEntry("type", new TypeValidator(Set.of(
                String.class
            )))
        ));
        public static String validate(String arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(Items2.class, arg, configuration);
        }
    }    
    
    public static class SchemaList2 extends FrozenList<String> {

        SchemaList2(FrozenList<String> m) {

            super(m);
        }
        public static SchemaList2 of(List<String> arg, SchemaConfiguration configuration) {

            return Schema21.validate(arg, configuration);
        }
    }
    
    
    public class Schema21 extends JsonSchema {
        public static final LinkedHashMap<String, KeywordValidator> keywordToValidator = new LinkedHashMap<>(Map.ofEntries(
            new KeywordEntry("type", new TypeValidator(Set.of(FrozenList.class))),
            new KeywordEntry("items", new ItemsValidator(Items2.class))
        ));
        protected static SchemaList2 getListOutputInstance(FrozenList<String> arg) {

            return new SchemaList2(arg);
        }
        public static SchemaList2 validate(SchemaListInput2 arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(Schema21.class, arg, configuration);
        }
    }}
