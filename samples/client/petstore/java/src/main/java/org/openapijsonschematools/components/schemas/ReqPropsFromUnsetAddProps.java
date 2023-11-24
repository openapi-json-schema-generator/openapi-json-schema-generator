package org.openapijsonschematools.components.schemas;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.Set;
import org.openapijsonschematools.configurations.SchemaConfiguration;
import org.openapijsonschematools.schemas.validation.FrozenMap;
import org.openapijsonschematools.schemas.validation.JsonSchema;
import org.openapijsonschematools.schemas.validation.KeywordEntry;
import org.openapijsonschematools.schemas.validation.KeywordValidator;
import org.openapijsonschematools.schemas.validation.RequiredValidator;
import org.openapijsonschematools.schemas.validation.TypeValidator;

public class ReqPropsFromUnsetAddProps {
    // nest classes so all schemas and input/output classes can be public
    
    
    public static class ReqPropsFromUnsetAddPropsMap extends FrozenMap<String, Object> {

        ReqPropsFromUnsetAddPropsMap(FrozenMap<String, Object> m) {

            super(m);
        }
        public static final Set<String> requiredKeys = Set.of(
            "invalid-name",
            "validName"
        );
        public static final Set<String> optionalKeys = Set.of(
        );
        public static ReqPropsFromUnsetAddPropsMap of(Map<String, Object> arg, SchemaConfiguration configuration) {

            return ReqPropsFromUnsetAddProps1.validate(arg, configuration);
        }
        
        public Object validName() {
            return get("validName");
        }
        
        public Object getAdditionalProperty(String name) {
            schemas.raise_if_key_known(name, self.__required_keys__, self.__optional_keys__)
            return self.get(name, schemas.unset)
        }
    }    
    
    public class ReqPropsFromUnsetAddProps1 extends JsonSchema {
        /*
        NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
        Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
    
        Do not edit the class manually.
        */
        public static final LinkedHashMap<String, KeywordValidator> keywordToValidator = new LinkedHashMap<>(Map.ofEntries(
            new KeywordEntry("type", new TypeValidator(Set.of(FrozenMap.class))),
            new KeywordEntry("required", new RequiredValidator(Set.of(
                "invalid-name",
                "validName"
            )))
        ));
        protected static ReqPropsFromUnsetAddPropsMap getMapOutputInstance(FrozenMap<String, Object> arg) {

            return new ReqPropsFromUnsetAddPropsMap(arg);
        }
        public static ReqPropsFromUnsetAddPropsMap validate(Map<String, Object> arg, SchemaConfiguration configuration) {

            return JsonSchema.validate(ReqPropsFromUnsetAddProps1.class, arg, configuration);
        }
    }
}
