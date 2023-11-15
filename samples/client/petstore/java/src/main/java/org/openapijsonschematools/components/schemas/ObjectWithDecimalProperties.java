package org.openapijsonschematools.components.schemas;
import org.openapijsonschematools.configurations.SchemaConfiguration;
import org.openapijsonschematools.schemas.JsonSchema;
import org.openapijsonschematools.schemas.JsonSchemas;
import org.openapijsonschematools.schemas.FrozenList;
import org.openapijsonschematools.schemas.FrozenMap;

import java.time.LocalDate;
import java.time.ZonedDateTime;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Map;
public class ObjectWithDecimalProperties {
    // nest classes so all schemas and input/output classes can be public
    
    
    public record Width(LinkedHashSet<Class<?>> type, String format) implements JsonSchema {
        public static Width withDefaults() {
            LinkedHashSet<Class<?>> type = new LinkedHashSet<>();
            type.add(String.class);
            String format = "number";
            return new Width(type, format);
        }
        public static String validate(String arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(Width.class, arg, configuration);
        }
    }}
