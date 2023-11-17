package org.openapijsonschematools.components.headers.numberheader;
import org.openapijsonschematools.configurations.SchemaConfiguration;
import org.openapijsonschematools.schemas.JsonSchema;
import org.openapijsonschematools.schemas.JsonSchemas;
import org.openapijsonschematools.schemas.FrozenList;
import org.openapijsonschematools.schemas.FrozenMap;

import java.time.LocalDate;
import java.time.ZonedDateTime;
import java.util.AbstractMap;
import java.util.LinkedHashMap;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

public class NumberHeaderSchema {
    // nest classes so all schemas and input/output classes can be public
    
    
    public class NumberHeaderSchema1 implements JsonSchema {
        static final LinkedHashSet<Class<?>> type = new LinkedHashSet<>(Set.of(
            String.class
        ));
        static final String format = "number";
        public static String validate(String arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(NumberHeaderSchema1.class, arg, configuration);
        }
    }}
