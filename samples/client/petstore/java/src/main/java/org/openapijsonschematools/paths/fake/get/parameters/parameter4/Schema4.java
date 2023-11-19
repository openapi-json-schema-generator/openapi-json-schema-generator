package org.openapijsonschematools.paths.fake.get.parameters.parameter4;
import java.util.LinkedHashSet;
import java.util.Set;
import org.openapijsonschematools.configurations.SchemaConfiguration;
import org.openapijsonschematools.schemas.JsonSchema;

public class Schema4 {
    // nest classes so all schemas and input/output classes can be public
    
    
    public class Schema41 implements JsonSchema {
        static final LinkedHashSet<Class<?>> type = new LinkedHashSet<>(Set.of(
            Integer.class,
            Long.class,
            Float.class,
            Double.class
        ));
        static final String format = "int32";
        public static Long validate(Integer arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(Schema41.class, Long.valueOf(arg), configuration);
        }
        
        public static Long validate(Float arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(Schema41.class, Long.parseLong(arg.toString()), configuration);
        }
        
        public static Long validate(Long arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(Schema41.class, arg, configuration);
        }
        
        public static Long validate(Double arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(Schema41.class, Long.parseLong(arg.toString()), configuration);
        }
    }}
