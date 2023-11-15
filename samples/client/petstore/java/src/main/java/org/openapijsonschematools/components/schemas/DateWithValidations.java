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
public class DateWithValidations {
    // nest classes so all schemas and input/output classes can be public
    
    
    public record DateWithValidations2(LinkedHashSet<Class<?>> type, String format) implements JsonSchema {
        /*
        NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
        Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
    
        Do not edit the class manually.
        */
        public static DateWithValidations2 withDefaults() {
            LinkedHashSet<Class<?>> type = new LinkedHashSet<>();
            type.add(String.class);
            String format = "date";
            return new DateWithValidations2(type, format);
        }
        public static String validate(String arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(DateWithValidations2.class, arg, configuration);
        }
    }}
