package org.openapijsonschematools.paths.faketestqueryparamters.put;
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
import org.openapijsonschematools.components.schemas.StringWithValidation;
import org.openapijsonschematools.paths.faketestqueryparamters.put.parameters.parameter0.Schema0;
import org.openapijsonschematools.paths.faketestqueryparamters.put.parameters.parameter1.Schema1;
import org.openapijsonschematools.paths.faketestqueryparamters.put.parameters.parameter2.Schema2;
import org.openapijsonschematools.paths.faketestqueryparamters.put.parameters.parameter3.Schema3;
import org.openapijsonschematools.paths.faketestqueryparamters.put.parameters.parameter4.Schema4;

public class QueryParameters {
    // nest classes so all schemas and input/output classes can be public
    
    
    public record AdditionalProperties() implements JsonSchema {
        public static JsonSchemas.NotAnyTypeSchema withDefaults() {
            return JsonSchemas.NotAnyTypeSchema.withDefaults();
        }
    
        // NotAnyTypeSchema
    }
    
    
    public record QueryParameters1(LinkedHashSet<Class<?>> type, LinkedHashMap<String, Class<?>> properties, Set<String> required, Class<?> additionalProperties) implements JsonSchema {
        public static QueryParameters1 withDefaults() {
            LinkedHashSet<Class<?>> type = new LinkedHashSet<>();
            type.add(FrozenMap.class);
            LinkedHashMap<String, Class<?>> properties = new LinkedHashMap<>();
            properties.put("refParam", StringWithValidation.StringWithValidation1.class);
            properties.put("ioutil", Schema1.Schema11.class);
            properties.put("context", Schema4.Schema41.class);
            properties.put("http", Schema2.Schema21.class);
            properties.put("pipe", Schema0.Schema01.class);
            properties.put("url", Schema3.Schema31.class);
            Set<String> required = new LinkedHashSet<>();
            required.add("context");
            required.add("http");
            required.add("ioutil");
            required.add("pipe");
            required.add("refParam");
            required.add("url");
            Class<?> additionalProperties = AdditionalProperties.class;
            return new QueryParameters1(type, properties, required, additionalProperties);
        }
        public static <T extends FrozenMap> T validate(Map<String, Object> arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(QueryParameters1.class, arg, configuration);
        }
    }
}
