package org.openapijsonschematools.components.requestbodies.userarray.content.applicationjson;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Set;
import org.openapijsonschematools.components.schemas.User;
import org.openapijsonschematools.configurations.SchemaConfiguration;
import org.openapijsonschematools.schemas.validation.FrozenList;
import org.openapijsonschematools.schemas.validation.JsonSchema;

public class Schema {
    // nest classes so all schemas and input/output classes can be public
    
    
    public static class SchemaTuple extends FrozenList<Object> {
        SchemaTuple(FrozenList<Object> m) {
            super(m);
        }
    }    
    
    public class Schema1 extends JsonSchema {
        public static final LinkedHashSet<Class<?>> type = new LinkedHashSet<>(Set.of(
            FrozenList.class
        ));
        public static final Class<?> items = User.User1.class;
        protected static SchemaTuple getListOutputInstance(FrozenList<Object> arg) {
            return new SchemaTuple(arg);
        }
        public static <U extends FrozenList> U validate(List<Object> arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(Schema1.class, arg, configuration);
        }
    }}
