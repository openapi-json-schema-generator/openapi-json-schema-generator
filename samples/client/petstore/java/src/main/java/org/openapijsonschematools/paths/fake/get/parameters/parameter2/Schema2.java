package org.openapijsonschematools.paths.fake.get.parameters.parameter2;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Set;
import org.openapijsonschematools.configurations.SchemaConfiguration;
import org.openapijsonschematools.schemas.FrozenList;
import org.openapijsonschematools.schemas.JsonSchema;

public class Schema2 {
    // nest classes so all schemas and input/output classes can be public
    
    
    public class Items2 implements JsonSchema {
        static final LinkedHashSet<Class<?>> type = new LinkedHashSet<>(Set.of(
            String.class
        ));
        public static String validate(String arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(Items2.class, arg, configuration);
        }
    }    
    
    public class Schema21 implements JsonSchema {
        static final LinkedHashSet<Class<?>> type = new LinkedHashSet<>(Set.of(
            FrozenList.class
        ));
        static final Class<?> items = Items2.class;
        public static <U extends FrozenList> U validate(List<Object> arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(Schema21.class, arg, configuration);
        }
    }}
