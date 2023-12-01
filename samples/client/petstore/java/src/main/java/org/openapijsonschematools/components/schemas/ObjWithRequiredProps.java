package org.openapijsonschematools.components.schemas;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Set;
import org.openapijsonschematools.configurations.SchemaConfiguration;
import org.openapijsonschematools.exceptions.ValidationException;
import org.openapijsonschematools.schemas.StringJsonSchema;
import org.openapijsonschematools.schemas.validation.AllOfValidator;
import org.openapijsonschematools.schemas.validation.FrozenMap;
import org.openapijsonschematools.schemas.validation.JsonSchema;
import org.openapijsonschematools.schemas.validation.KeywordEntry;
import org.openapijsonschematools.schemas.validation.KeywordValidator;
import org.openapijsonschematools.schemas.validation.PropertiesValidator;
import org.openapijsonschematools.schemas.validation.PropertyEntry;
import org.openapijsonschematools.schemas.validation.RequiredValidator;
import org.openapijsonschematools.schemas.validation.TypeValidator;

public class ObjWithRequiredProps {
    // nest classes so all schemas and input/output classes can be public
    
    
    public static class A extends StringJsonSchema {}
    
    
    public static class ObjWithRequiredPropsMap extends FrozenMap<String, Object> {
        ObjWithRequiredPropsMap(FrozenMap<String, Object> m) {
            super(m);
        }
        public static final Set<String> requiredKeys = Set.of(
            "a"
        );
        public static final Set<String> optionalKeys = Set.of();
        public static ObjWithRequiredPropsMap of(Map<String, Object> arg, SchemaConfiguration configuration) throws ValidationException {
            return ObjWithRequiredProps1.validate(arg, configuration);
        }
        
        public String a() {
            return (String) get("a");
        }
        
        public Object getAdditionalProperty(String name) {
            throwIfKeyKnown(name, requiredKeys, optionalKeys);
            throwIfKeyNotPresent(name);
            return get(name);
        }
    }    
    
    public static class ObjWithRequiredProps1 extends JsonSchema {
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
            new KeywordEntry("required", new RequiredValidator(Set.of(
                "a"
            ))),
            new KeywordEntry("allOf", new AllOfValidator(List.of(
                ObjWithRequiredPropsBase.ObjWithRequiredPropsBase1.class
            )))
        ));
        
        protected static ObjWithRequiredPropsMap getMapOutputInstance(FrozenMap<String, Object> arg) {
            return new ObjWithRequiredPropsMap(arg);
        }
        public static ObjWithRequiredPropsMap validate(Map<String, Object> arg, SchemaConfiguration configuration) throws ValidationException {
            return JsonSchema.validate(ObjWithRequiredProps1.class, arg, configuration);
        }
    }
}
