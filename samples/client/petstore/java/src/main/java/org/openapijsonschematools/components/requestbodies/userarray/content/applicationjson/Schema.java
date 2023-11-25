package org.openapijsonschematools.components.requestbodies.userarray.content.applicationjson;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Set;
import org.openapijsonschematools.components.schemas.User;
import org.openapijsonschematools.configurations.SchemaConfiguration;
import org.openapijsonschematools.exceptions.ValidationException;
import org.openapijsonschematools.schemas.validation.FrozenList;
import org.openapijsonschematools.schemas.validation.ItemsValidator;
import org.openapijsonschematools.schemas.validation.JsonSchema;
import org.openapijsonschematools.schemas.validation.KeywordEntry;
import org.openapijsonschematools.schemas.validation.KeywordValidator;
import org.openapijsonschematools.schemas.validation.TypeValidator;

public class Schema {
    // nest classes so all schemas and input/output classes can be public
    
    
    public static class SchemaList extends FrozenList<User.UserMap> {

        SchemaList(FrozenList<User.UserMap> m) {

            super(m);
        }
        public static SchemaList of(List<Map<String, Object>> arg, SchemaConfiguration configuration) throws ValidationException {


            return Schema1.validate(arg, configuration);
        }
    }
    
    
    public class Schema1 extends JsonSchema {
        public static final LinkedHashMap<String, KeywordValidator> keywordToValidator = new LinkedHashMap<>(Map.ofEntries(
            new KeywordEntry("type", new TypeValidator(Set.of(FrozenList.class))),
            new KeywordEntry("items", new ItemsValidator(User.User1.class))
        ));
        protected static SchemaList getListOutputInstance(FrozenList<User.UserMap> arg) {

            return new SchemaList(arg);
        }
        public static SchemaList validate(List<Map<String, Object>> arg, SchemaConfiguration configuration) throws ValidationException {


            return JsonSchema.validate(Schema1.class, arg, configuration);
        }
    }}
