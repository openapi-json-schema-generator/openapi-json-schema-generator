package org.openapijsonschematools.components.schemas;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.Set;
import org.openapijsonschematools.configurations.SchemaConfiguration;
import org.openapijsonschematools.exceptions.ValidationException;
import org.openapijsonschematools.schemas.StringJsonSchema;
import org.openapijsonschematools.schemas.validation.FrozenMap;
import org.openapijsonschematools.schemas.validation.JsonSchema;
import org.openapijsonschematools.schemas.validation.KeywordEntry;
import org.openapijsonschematools.schemas.validation.KeywordValidator;
import org.openapijsonschematools.schemas.validation.PropertiesValidator;
import org.openapijsonschematools.schemas.validation.PropertyEntry;
import org.openapijsonschematools.schemas.validation.TypeValidator;

public class Capitalization {
    // nest classes so all schemas and input/output classes can be public
    
    
    public class SmallCamel extends StringJsonSchema {}
    
    
    public class CapitalCamel extends StringJsonSchema {}
    
    
    public class SmallSnake extends StringJsonSchema {}
    
    
    public class CapitalSnake extends StringJsonSchema {}
    
    
    public class SCAETHFlowPoints extends StringJsonSchema {}
    
    
    public class ATTNAME extends StringJsonSchema {}
    
    
    public static class CapitalizationMap extends FrozenMap<String, Object
        CapitalizationMap(FrozenMap<String, Object
            super(m);
        }
        public static final Set<String> requiredKeys = Set.of();
        public static final Set<String> optionalKeys = Set.of(
            "smallCamel",
            "CapitalCamel",
            "small_Snake",
            "Capital_Snake",
            "SCA_ETH_Flow_Points",
            "ATT_NAME"
        );
        public static CapitalizationMap of(Map<String, Object> arg, SchemaConfiguration configuration) throws ValidationException {
            return Capitalization1.validate(arg, configuration);
        }
        
        public String
            String key = "smallCamel";
            throwIfKeyNotPresent(key);
            return (String
        }
        
        public String
            String key = "CapitalCamel";
            throwIfKeyNotPresent(key);
            return (String
        }
        
        public String
            String key = "small_Snake";
            throwIfKeyNotPresent(key);
            return (String
        }
        
        public String
            String key = "Capital_Snake";
            throwIfKeyNotPresent(key);
            return (String
        }
        
        public String
            String key = "SCA_ETH_Flow_Points";
            throwIfKeyNotPresent(key);
            return (String
        }
        
        public String
            String key = "ATT_NAME";
            throwIfKeyNotPresent(key);
            return (String
        }
        
        public Object getAdditionalProperty(String name) {
            throwIfKeyKnown(name, requiredKeys, optionalKeys);
            throwIfKeyNotPresent(name);
            return get(name);
        }
    }    
    
    public class Capitalization1 extends JsonSchema {
        /*
        NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
        Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
    
        Do not edit the class manually.
        */
        public static final LinkedHashMap<String, KeywordValidator> keywordToValidator = new LinkedHashMap<>(Map.ofEntries(
            new KeywordEntry("type", new TypeValidator(Set.of(FrozenMap.class))),
            new KeywordEntry("properties", new PropertiesValidator(Map.ofEntries(
                new PropertyEntry("smallCamel", SmallCamel.class),
                new PropertyEntry("CapitalCamel", CapitalCamel.class),
                new PropertyEntry("small_Snake", SmallSnake.class),
                new PropertyEntry("Capital_Snake", CapitalSnake.class),
                new PropertyEntry("SCA_ETH_Flow_Points", SCAETHFlowPoints.class),
                new PropertyEntry("ATT_NAME", ATTNAME.class)
            )))
        ));
        protected static CapitalizationMap getMapOutputInstance(FrozenMap<String, Object
            return new CapitalizationMap(arg);
        }
        public static CapitalizationMap validate(Map<String, Object> arg, SchemaConfiguration configuration) throws ValidationException {
            return JsonSchema.validate(Capitalization1.class, arg, configuration);
        }
    }
}
