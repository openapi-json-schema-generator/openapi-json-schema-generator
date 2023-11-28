package org.openapijsonschematools.paths.fakecasesensitiveparams.put;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.Set;
import org.openapijsonschematools.configurations.SchemaConfiguration;
import org.openapijsonschematools.exceptions.ValidationException;
import org.openapijsonschematools.paths.fakecasesensitiveparams.put.parameters.parameter0.Schema0;
import org.openapijsonschematools.paths.fakecasesensitiveparams.put.parameters.parameter1.Schema1;
import org.openapijsonschematools.paths.fakecasesensitiveparams.put.parameters.parameter2.Schema2;
import org.openapijsonschematools.schemas.AnyTypeJsonSchema;
import org.openapijsonschematools.schemas.NotAnyTypeJsonSchema;
import org.openapijsonschematools.schemas.validation.AdditionalPropertiesValidator;
import org.openapijsonschematools.schemas.validation.FrozenMap;
import org.openapijsonschematools.schemas.validation.JsonSchema;
import org.openapijsonschematools.schemas.validation.KeywordEntry;
import org.openapijsonschematools.schemas.validation.KeywordValidator;
import org.openapijsonschematools.schemas.validation.PropertiesValidator;
import org.openapijsonschematools.schemas.validation.PropertyEntry;
import org.openapijsonschematools.schemas.validation.RequiredValidator;
import org.openapijsonschematools.schemas.validation.TypeValidator;

public class QueryParameters {
    // nest classes so all schemas and input/output classes can be public
    
    
    public static class AdditionalProperties extends NotAnyTypeJsonSchema {}
        // NotAnyTypeSchema
    
    
    public static class QueryParametersMap extends FrozenMap<String, Object> {
        QueryParametersMap(FrozenMap<String, Object> m) {
            super(m);
        }
        public static final Set<String> requiredKeys = Set.of(
            "SomeVar",
            "someVar",
            "some_var"
        );
        public static final Set<String> optionalKeys = Set.of();
        public static QueryParametersMap of(Map<String, Object> arg, SchemaConfiguration configuration) throws ValidationException {
            return QueryParameters1.validate(arg, configuration);
        }
        
        public String SomeVar() {
            return (String) get("SomeVar");
        }
        
        public String someVar() {
            return (String) get("someVar");
        }
        
        public String some_var() {
            return (String) get("some_var");
        }
    }    
    
    public static class QueryParameters1 extends JsonSchema {
        public static final LinkedHashMap<String, KeywordValidator> keywordToValidator = new LinkedHashMap<>(Map.ofEntries(
            new KeywordEntry("type", new TypeValidator(Set.of(FrozenMap.class))),
            new KeywordEntry("properties", new PropertiesValidator(Map.ofEntries(
                new PropertyEntry("someVar", Schema0.Schema01.class),
                new PropertyEntry("some_var", Schema2.Schema21.class),
                new PropertyEntry("SomeVar", Schema1.Schema11.class)
            ))),
            new KeywordEntry("required", new RequiredValidator(Set.of(
                "SomeVar",
                "someVar",
                "some_var"
            ))),
            new KeywordEntry("additionalProperties", new AdditionalPropertiesValidator(AdditionalProperties.class))
            
        ));
        protected static QueryParametersMap getMapOutputInstance(FrozenMap<String, Object> arg) {
            return new QueryParametersMap(arg);
        }
        public static QueryParametersMap validate(Map<String, Object> arg, SchemaConfiguration configuration) throws ValidationException {
            return JsonSchema.validate(QueryParameters1.class, arg, configuration);
        }
    }
}
