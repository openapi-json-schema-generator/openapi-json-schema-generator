package org.openapijsonschematools.components.schemas;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.Set;
import org.openapijsonschematools.configurations.SchemaConfiguration;
import org.openapijsonschematools.exceptions.ValidationException;
import org.openapijsonschematools.schemas.AnyTypeJsonSchema;
import org.openapijsonschematools.schemas.BooleanJsonSchema;
import org.openapijsonschematools.schemas.NotAnyTypeJsonSchema;
import org.openapijsonschematools.schemas.StringJsonSchema;
import org.openapijsonschematools.schemas.validation.AdditionalPropertiesValidator;
import org.openapijsonschematools.schemas.validation.FrozenMap;
import org.openapijsonschematools.schemas.validation.JsonSchema;
import org.openapijsonschematools.schemas.validation.KeywordEntry;
import org.openapijsonschematools.schemas.validation.KeywordValidator;
import org.openapijsonschematools.schemas.validation.PropertiesValidator;
import org.openapijsonschematools.schemas.validation.PropertyEntry;
import org.openapijsonschematools.schemas.validation.RequiredValidator;
import org.openapijsonschematools.schemas.validation.TypeValidator;

public class AppleReq {
    // nest classes so all schemas and input/output classes can be public
    
    
    public class AdditionalProperties extends NotAnyTypeJsonSchema {}
        // NotAnyTypeSchema
    
    
    public class Cultivar extends StringJsonSchema {}
    
    
    public class Mealy extends BooleanJsonSchema {}
    
    
    public static class AppleReqMap extends FrozenMap<String, Object
        AppleReqMap(FrozenMap<String, Object
            super(m);
        }
        public static final Set<String> requiredKeys = Set.of(
            "cultivar"
        );
        public static final Set<String> optionalKeys = Set.of(
            "mealy"
        );
        public static AppleReqMap of(Map<String, Object> arg, SchemaConfiguration configuration) throws ValidationException {
            return AppleReq1.validate(arg, configuration);
        }
        
        public String
            return (String
        }
        
        public boolean
            String key = "mealy";
            throwIfKeyNotPresent(key);
            return (boolean
        }
    }    
    
    public class AppleReq1 extends JsonSchema {
        /*
        NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
        Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
    
        Do not edit the class manually.
        */
        public static final LinkedHashMap<String, KeywordValidator> keywordToValidator = new LinkedHashMap<>(Map.ofEntries(
            new KeywordEntry("type", new TypeValidator(Set.of(FrozenMap.class))),
            new KeywordEntry("properties", new PropertiesValidator(Map.ofEntries(
                new PropertyEntry("cultivar", Cultivar.class),
                new PropertyEntry("mealy", Mealy.class)
            ))),
            new KeywordEntry("required", new RequiredValidator(Set.of(
                "cultivar"
            ))),
            new KeywordEntry("additionalProperties", new AdditionalPropertiesValidator(AdditionalProperties.class))
        ));
        protected static AppleReqMap getMapOutputInstance(FrozenMap<String, Object
            return new AppleReqMap(arg);
        }
        public static AppleReqMap validate(Map<String, Object> arg, SchemaConfiguration configuration) throws ValidationException {
            return JsonSchema.validate(AppleReq1.class, arg, configuration);
        }
    }
}
