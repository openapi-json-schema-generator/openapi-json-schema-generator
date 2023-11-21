package org.openapijsonschematools.paths.fake.get.parameters.parameter5;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.Set;
import org.openapijsonschematools.configurations.SchemaConfiguration;
import org.openapijsonschematools.schemas.validation.JsonSchema;
import org.openapijsonschematools.schemas.validation.KeywordEntry;
import org.openapijsonschematools.schemas.validation.KeywordValidator;
import org.openapijsonschematools.schemas.validation.TypeValidator;

public class Schema5 {
    // nest classes so all schemas and input/output classes can be public
    
    
    public class Schema51 extends JsonSchema {
        public static final LinkedHashMap<String, KeywordValidator> keywordToValidator = new LinkedHashMap<>(Map.ofEntries(
            new KeywordEntry("type", new TypeValidator(Set.of(
                Integer.class,
                Long.class,
                Float.class,
                Double.class
            )),
        ));
        public static final String format = "double";
        public static Double validate(Double arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(Schema51.class, arg, configuration);
        }
    }}
