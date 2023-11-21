package org.openapijsonschematools.components.schemas;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.Set;
import org.openapijsonschematools.configurations.SchemaConfiguration;
import org.openapijsonschematools.schemas.Int64JsonSchema;
import org.openapijsonschematools.schemas.IntJsonSchema;
import org.openapijsonschematools.schemas.StringJsonSchema;
import org.openapijsonschematools.schemas.validation.FrozenMap;
import org.openapijsonschematools.schemas.validation.JsonSchema;
import org.openapijsonschematools.schemas.validation.KeywordEntry;
import org.openapijsonschematools.schemas.validation.KeywordValidator;
import org.openapijsonschematools.schemas.validation.PropertiesEntry;
import org.openapijsonschematools.schemas.validation.PropertiesValidator;
import org.openapijsonschematools.schemas.validation.RequiredValidator;
import org.openapijsonschematools.schemas.validation.TypeValidator;

public class ObjectWithDifficultlyNamedProps {
    // nest classes so all schemas and input/output classes can be public
    
    
    public class Specialpropertyname extends Int64JsonSchema {}
    
    
    public class Schema123list extends StringJsonSchema {}
    
    
    public class Schema123Number extends IntJsonSchema {}
    
    
    public static class ObjectWithDifficultlyNamedPropsMap extends FrozenMap<String, Object> {
        ObjectWithDifficultlyNamedPropsMap(FrozenMap<? extends String, ?> m) {
            super(m);
        }
        public static ObjectWithDifficultlyNamedPropsMap of(Map<String, Object> arg, SchemaConfiguration configuration) {
            return ObjectWithDifficultlyNamedProps1.validate(arg, configuration);
        }
    }    
    
    public class ObjectWithDifficultlyNamedProps1 extends JsonSchema {
        /*
        NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
        Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
    
        Do not edit the class manually.
    
        model with properties that have invalid names for python
        */
        public static final LinkedHashMap<String, KeywordValidator> keywordToValidator = new LinkedHashMap<>(Map.ofEntries(
            new KeywordEntry("type", new TypeValidator(Set.of(FrozenMap.class)),
            new KeywordEntry("properties", new PropertiesValidator(Map.ofEntries(
                new PropertyEntry("$special[property.name]", Specialpropertyname.class),
                new PropertyEntry("123-list", Schema123list.class),
                new PropertyEntry("123Number", Schema123Number.class)
            )),
        ));
        public static final Set<String> required = new LinkedHashSet<>(Set.of(
            "123-list"
        ));
        protected static ObjectWithDifficultlyNamedPropsMap getMapOutputInstance(FrozenMap<? extends String, ?> arg) {
            return new ObjectWithDifficultlyNamedPropsMap(arg);
        }
        public static ObjectWithDifficultlyNamedPropsMap validate(Map<String, Object> arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(ObjectWithDifficultlyNamedProps1.class, arg, configuration);
        }
    }
}
