package org.openapijsonschematools.paths.faketestqueryparamters.put.parameters.parameter0;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Set;
import org.openapijsonschematools.configurations.SchemaConfiguration;
import org.openapijsonschematools.schemas.StringJsonSchema;
import org.openapijsonschematools.schemas.validation.FrozenList;
import org.openapijsonschematools.schemas.validation.JsonSchema;

public class Schema0 {
    // nest classes so all schemas and input/output classes can be public
    
    
    public class Items0 extends StringJsonSchema {}
    
    
    public static class SchemaList0 extends FrozenList<Object> {
        SchemaList0(FrozenList<Object> m) {
            super(m);
        }
    }    
    
    public class Schema01 extends JsonSchema {
        public static final LinkedHashSet<Class<?>> type = new LinkedHashSet<>(Set.of(
            FrozenList.class
        ));
        public static final Class<?> items = Items0.class;
        protected static SchemaList0 getListOutputInstance(FrozenList<Object> arg) {
            return new SchemaList0(arg);
        }
        public static SchemaList0 validate(List<Object> arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(Schema01.class, arg, configuration);
        }
    }}
