package org.openapijsonschematools.paths.storeorderorderid.get.parameters.parameter0;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.Set;
import org.openapijsonschematools.configurations.SchemaConfiguration;
import org.openapijsonschematools.schemas.validation.FormatValidator;
import org.openapijsonschematools.schemas.validation.JsonSchema;
import org.openapijsonschematools.schemas.validation.KeywordEntry;
import org.openapijsonschematools.schemas.validation.KeywordValidator;
import org.openapijsonschematools.schemas.validation.TypeValidator;

public class Schema0 {
    // nest classes so all schemas and input/output classes can be public
    
    
    public class Schema01 extends JsonSchema {
        public static final LinkedHashMap<String, KeywordValidator> keywordToValidator = new LinkedHashMap<>(Map.ofEntries(
            new KeywordEntry("type", new TypeValidator(Set.of(
                Integer.class,
                Long.class,
                Float.class,
                Double.class
            ))),
            new KeywordEntry("format", new FormatValidator("int64"))
        ));
        public static long validate(int arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(Schema01.class, Long.valueOf(arg), configuration);
        }
        
        public static long validate(float arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(Schema01.class, Long.parseLong(String.valueOf(arg)), configuration);
        }
        
        public static long validate(long arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(Schema01.class, arg, configuration);
        }
        
        public static long validate(double arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(Schema01.class, Long.parseLong(String.valueOf(arg)), configuration);
        }
    }}
