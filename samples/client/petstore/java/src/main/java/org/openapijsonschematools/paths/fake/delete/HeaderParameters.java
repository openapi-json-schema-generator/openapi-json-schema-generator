package org.openapijsonschematools.paths.fake.delete;
import org.openapijsonschematools.configurations.SchemaConfiguration;
import org.openapijsonschematools.schemas.JsonSchema;
import org.openapijsonschematools.schemas.JsonSchemas;
import org.openapijsonschematools.schemas.FrozenList;
import org.openapijsonschematools.schemas.FrozenMap;

import java.time.LocalDate;
import java.time.ZonedDateTime;
import java.util.LinkedHashMap;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;
import org.openapijsonschematools.paths.fake.delete.parameters.parameter1.Schema1;
import org.openapijsonschematools.paths.fake.delete.parameters.parameter4.Schema4;

public class HeaderParameters {
    // nest classes so all schemas and input/output classes can be public
    
    
    public record AdditionalProperties() implements JsonSchema {
        public static JsonSchemas.NotAnyTypeSchema withDefaults() {
            return JsonSchemas.NotAnyTypeSchema.withDefaults();
        }
    
        // NotAnyTypeSchema
    }
    
    
    public record HeaderParameters1(LinkedHashSet<Class<?>> type, LinkedHashMap<String, Class<?>> properties, Set<String> required, Class<?> additionalProperties) implements JsonSchema {
        public static HeaderParameters1 withDefaults() {
            LinkedHashSet<Class<?>> type = new LinkedHashSet<>();
            type.add(FrozenMap.class);
            LinkedHashMap<String, Class<?>> properties = new LinkedHashMap<>();
            properties.put("required_boolean_group", Schema1.Schema11.class);
            properties.put("boolean_group", Schema4.Schema41.class);
            Set<String> required = new LinkedHashSet<>();
            required.add("required_boolean_group");
            Class<?> additionalProperties = AdditionalProperties.class;
            return new HeaderParameters1(type, properties, required, additionalProperties);
        }
        public static <T extends FrozenMap> T validate(Map<String, Object> arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(HeaderParameters1.class, arg, configuration);
        }
    }
}
