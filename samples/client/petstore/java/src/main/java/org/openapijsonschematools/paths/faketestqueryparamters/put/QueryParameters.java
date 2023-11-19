package org.openapijsonschematools.paths.faketestqueryparamters.put;
import java.util.AbstractMap;
import java.util.LinkedHashMap;
import java.util.LinkedHashSet;
import java.util.Map;
import java.util.Set;
import org.openapijsonschematools.components.schemas.StringWithValidation;
import org.openapijsonschematools.configurations.SchemaConfiguration;
import org.openapijsonschematools.paths.faketestqueryparamters.put.parameters.parameter0.Schema0;
import org.openapijsonschematools.paths.faketestqueryparamters.put.parameters.parameter1.Schema1;
import org.openapijsonschematools.paths.faketestqueryparamters.put.parameters.parameter2.Schema2;
import org.openapijsonschematools.paths.faketestqueryparamters.put.parameters.parameter3.Schema3;
import org.openapijsonschematools.paths.faketestqueryparamters.put.parameters.parameter4.Schema4;
import org.openapijsonschematools.schemas.AnyTypeJsonSchema;
import org.openapijsonschematools.schemas.FrozenMap;
import org.openapijsonschematools.schemas.JsonSchema;
import org.openapijsonschematools.schemas.NotAnyTypeJsonSchema;

public class QueryParameters {
    // nest classes so all schemas and input/output classes can be public
    
    
    public class AdditionalProperties extends NotAnyTypeJsonSchema {}
        // NotAnyTypeSchema
    
    
    public class QueryParameters1 implements JsonSchema {
        static final LinkedHashSet<Class<?>> type = new LinkedHashSet<>(Set.of(
            FrozenMap.class
        ));
        static final LinkedHashMap<String, Class<?>> properties = new LinkedHashMap<>(Map.ofEntries(
            new AbstractMap.SimpleEntry<String, Class<?>>("refParam", StringWithValidation.StringWithValidation1.class),
            new AbstractMap.SimpleEntry<String, Class<?>>("ioutil", Schema1.Schema11.class),
            new AbstractMap.SimpleEntry<String, Class<?>>("context", Schema4.Schema41.class),
            new AbstractMap.SimpleEntry<String, Class<?>>("http", Schema2.Schema21.class),
            new AbstractMap.SimpleEntry<String, Class<?>>("pipe", Schema0.Schema01.class),
            new AbstractMap.SimpleEntry<String, Class<?>>("url", Schema3.Schema31.class)
        ));
        static final Set<String> required = new LinkedHashSet<>(Set.of(
            "context",
            "http",
            "ioutil",
            "pipe",
            "refParam",
            "url"
        ));
        static final Class<?> additionalProperties = AdditionalProperties.class;
        public static <T extends FrozenMap> T validate(Map<String, Object> arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(QueryParameters1.class, arg, configuration);
        }
    }
}
