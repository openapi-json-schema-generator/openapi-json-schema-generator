package org.openapijsonschematools.components.schemas;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.Set;
import org.openapijsonschematools.configurations.SchemaConfiguration;
import org.openapijsonschematools.schemas.NumberJsonSchema;
import org.openapijsonschematools.schemas.StringJsonSchema;
import org.openapijsonschematools.schemas.validation.AdditionalPropertiesValidator;
import org.openapijsonschematools.schemas.validation.FrozenMap;
import org.openapijsonschematools.schemas.validation.JsonSchema;
import org.openapijsonschematools.schemas.validation.KeywordEntry;
import org.openapijsonschematools.schemas.validation.KeywordValidator;
import org.openapijsonschematools.schemas.validation.PropertiesValidator;
import org.openapijsonschematools.schemas.validation.PropertyEntry;
import org.openapijsonschematools.schemas.validation.TypeValidator;

public class ObjectWithNonIntersectingValues {
    // nest classes so all schemas and input/output classes can be public
    
    
    public class AdditionalProperties extends StringJsonSchema {}
    
    
    public class A extends NumberJsonSchema {}
    
    
    public static class ObjectWithNonIntersectingValuesMap extends FrozenMap<String, Object> {
        ObjectWithNonIntersectingValuesMap(FrozenMap<? extends String, ?> m) {
            super(m);
        }
        public static ObjectWithNonIntersectingValuesMap of(Map<String, Object> arg, SchemaConfiguration configuration) {
            return ObjectWithNonIntersectingValues1.validate(arg, configuration);
        }
    }    
    
    public class ObjectWithNonIntersectingValues1 extends JsonSchema {
        /*
        NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
        Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
    
        Do not edit the class manually.
        */
        public static final LinkedHashMap<String, KeywordValidator> keywordToValidator = new LinkedHashMap<>(Map.ofEntries(
            new KeywordEntry("type", new TypeValidator(Set.of(FrozenMap.class))),
            new KeywordEntry("properties", new PropertiesValidator(Map.ofEntries(
                new PropertyEntry("a", A.class)
            ))),
            new KeywordEntry("additionalProperties", new AdditionalPropertiesValidator(AdditionalProperties.class))
        ));
        protected static ObjectWithNonIntersectingValuesMap getMapOutputInstance(FrozenMap<? extends String, ?> arg) {
            return new ObjectWithNonIntersectingValuesMap(arg);
        }
        public static ObjectWithNonIntersectingValuesMap validate(Map<String, Object> arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(ObjectWithNonIntersectingValues1.class, arg, configuration);
        }
    }
}
