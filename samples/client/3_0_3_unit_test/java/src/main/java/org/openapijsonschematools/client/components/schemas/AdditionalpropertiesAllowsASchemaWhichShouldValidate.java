package org.openapijsonschematools.client.components.schemas;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.Set;
import org.openapijsonschematools.client.configurations.SchemaConfiguration;
import org.openapijsonschematools.client.exceptions.ValidationException;
import org.openapijsonschematools.client.schemas.AnyTypeJsonSchema;
import org.openapijsonschematools.client.schemas.BooleanJsonSchema;
import org.openapijsonschematools.client.schemas.validation.AdditionalPropertiesValidator;
import org.openapijsonschematools.client.schemas.validation.FrozenList;
import org.openapijsonschematools.client.schemas.validation.FrozenMap;
import org.openapijsonschematools.client.schemas.validation.JsonSchema;
import org.openapijsonschematools.client.schemas.validation.JsonSchemaFactory;
import org.openapijsonschematools.client.schemas.validation.KeywordEntry;
import org.openapijsonschematools.client.schemas.validation.KeywordValidator;
import org.openapijsonschematools.client.schemas.validation.PropertiesValidator;
import org.openapijsonschematools.client.schemas.validation.PropertyEntry;
import org.openapijsonschematools.client.schemas.validation.TypeValidator;

public class AdditionalpropertiesAllowsASchemaWhichShouldValidate {
    // nest classes so all schemas and input/output classes can be public
    
    
    public static class AdditionalProperties extends BooleanJsonSchema {}
    
    
    public static class Foo extends AnyTypeJsonSchema {}
    
    
    public static class Bar extends AnyTypeJsonSchema {}
    
    
    public static class AdditionalpropertiesAllowsASchemaWhichShouldValidateMap extends FrozenMap<String, Object> {
        AdditionalpropertiesAllowsASchemaWhichShouldValidateMap(FrozenMap<String, Object> m) {
            super(m);
        }
        public static final Set<String> requiredKeys = Set.of();
        public static final Set<String> optionalKeys = Set.of(
            "foo",
            "bar"
        );
        public static AdditionalpropertiesAllowsASchemaWhichShouldValidateMap of(Map<String, Object> arg, SchemaConfiguration configuration) throws ValidationException {
            return JsonSchemaFactory.getInstance(AdditionalpropertiesAllowsASchemaWhichShouldValidate1.class).validate(arg, configuration);
        }
        
        public Object foo() {
            String key = "foo";
            throwIfKeyNotPresent(key);
            return get(key);
        }
        
        public Object bar() {
            String key = "bar";
            throwIfKeyNotPresent(key);
            return get(key);
        }
        
        public boolean getAdditionalProperty(String name) {
            throwIfKeyNotPresent(name);
            return (boolean) get(name);
        }
    }
    public class AdditionalpropertiesAllowsASchemaWhichShouldValidateMapInput {
        // optionalProperties + additionalProperties
    }
    
    
    public static class AdditionalpropertiesAllowsASchemaWhichShouldValidate1 extends JsonSchema<Object, Object, AdditionalpropertiesAllowsASchemaWhichShouldValidateMap, Object, Object, FrozenList<Object>> {
        /*
        NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
        Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
    
        Do not edit the class manually.
        */
        public AdditionalpropertiesAllowsASchemaWhichShouldValidate1() {
            super(new LinkedHashMap<>(Map.ofEntries(
                new KeywordEntry("type", new TypeValidator(Set.of(FrozenMap.class))),
                new KeywordEntry("properties", new PropertiesValidator(Map.ofEntries(
                    new PropertyEntry("foo", Foo.class),
                    new PropertyEntry("bar", Bar.class)
                ))),
                new KeywordEntry("additionalProperties", new AdditionalPropertiesValidator(AdditionalProperties.class))
            )));
        }
        
        @Override
        protected AdditionalpropertiesAllowsASchemaWhichShouldValidateMap getMapOutputInstance(FrozenMap<String, ?> arg) {
            return new AdditionalpropertiesAllowsASchemaWhichShouldValidateMap((FrozenMap<String, Object>) arg);
        }
        public AdditionalpropertiesAllowsASchemaWhichShouldValidateMap validate(Map<String, Object> arg, SchemaConfiguration configuration) throws ValidationException {
            return validateMap(arg, configuration);
        }
    }
}
