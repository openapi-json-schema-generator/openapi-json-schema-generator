package org.openapijsonschematools.client.components.schemas;
import java.util.HashSet;
import java.util.LinkedHashMap;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Map;
import java.util.Objects;
import java.util.Set;
import org.openapijsonschematools.client.configurations.JsonSchemaKeywordFlags;
import org.openapijsonschematools.client.configurations.SchemaConfiguration;
import org.openapijsonschematools.client.exceptions.ValidationException;
import org.openapijsonschematools.client.schemas.validation.FrozenMap;
import org.openapijsonschematools.client.schemas.validation.JsonSchema;
import org.openapijsonschematools.client.schemas.validation.JsonSchemaFactory;
import org.openapijsonschematools.client.schemas.validation.KeywordEntry;
import org.openapijsonschematools.client.schemas.validation.MaximumValidator;
import org.openapijsonschematools.client.schemas.validation.PathToSchemasMap;
import org.openapijsonschematools.client.schemas.validation.PropertiesValidator;
import org.openapijsonschematools.client.schemas.validation.PropertyEntry;
import org.openapijsonschematools.client.schemas.validation.SchemaMapValidator;
import org.openapijsonschematools.client.schemas.validation.SchemaNumberValidator;
import org.openapijsonschematools.client.schemas.validation.TypeValidator;
import org.openapijsonschematools.client.schemas.validation.ValidationMetadata;

public class TheDefaultKeywordDoesNotDoAnythingIfThePropertyIsMissing {
    // nest classes so all schemas and input/output classes can be public
    
    
    public static class Alpha extends JsonSchema implements SchemaNumberValidator {
        public Alpha() {
            super(new LinkedHashMap<>(Map.ofEntries(
                new KeywordEntry("type", new TypeValidator(Set.of(
                    Integer.class,
                    Long.class,
                    Float.class,
                    Double.class
                ))),
                new KeywordEntry("maximum", new MaximumValidator(3))
            )));
        }
    
        @Override
        public Number castToAllowedTypes(Number arg, List<Object> pathToItem, Set<List<Object>> pathSet) {
            return castToAllowedNumberTypes(arg, pathToItem, pathSet);
        }
    
        @Override
        public Number getNewInstance(Number arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) {
            return arg;
        }
    
        @Override
        public Number validate(Number arg, SchemaConfiguration configuration) throws ValidationException {
            Set<List<Object>> pathSet = new HashSet<>();
            List<Object> pathToItem = List.of("args[0");
            Number castArg = castToAllowedTypes(arg, pathToItem, pathSet);
            SchemaConfiguration usedConfiguration = Objects.requireNonNullElseGet(configuration, () -> new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone()));
            ValidationMetadata validationMetadata = new ValidationMetadata(pathToItem, usedConfiguration, new PathToSchemasMap(), new LinkedHashSet<>());
            PathToSchemasMap pathToSchemasMap = getPathToSchemas(this, castArg, validationMetadata, pathSet);
            return getNewInstance(castArg, validationMetadata.pathToItem(), pathToSchemasMap);
        }
        public int validate(int arg, SchemaConfiguration configuration) throws ValidationException {
            return (int) validate((Number) arg, configuration);
        }
        
        public long validate(long arg, SchemaConfiguration configuration) throws ValidationException {
            return (long) validate((Number) arg, configuration);
        }
        
        public float validate(float arg, SchemaConfiguration configuration) throws ValidationException {
            return (float) validate((Number) arg, configuration);
        }
        
        public double validate(double arg, SchemaConfiguration configuration) throws ValidationException {
            return (double) validate((Number) arg, configuration);
        }
    }    
    
    public static class TheDefaultKeywordDoesNotDoAnythingIfThePropertyIsMissingMap extends FrozenMap<Object> {
        TheDefaultKeywordDoesNotDoAnythingIfThePropertyIsMissingMap(FrozenMap<Object> m) {
            super(m);
        }
        public static final Set<String> requiredKeys = Set.of();
        public static final Set<String> optionalKeys = Set.of(
            "alpha"
        );
        public static TheDefaultKeywordDoesNotDoAnythingIfThePropertyIsMissingMap of(Map<String, Object> arg, SchemaConfiguration configuration) throws ValidationException {
            return JsonSchemaFactory.getInstance(TheDefaultKeywordDoesNotDoAnythingIfThePropertyIsMissing1.class).validate(arg, configuration);
        }
        
        public Number alpha() {
            String key = "alpha";
            throwIfKeyNotPresent(key);
            return (Number) get(key);
        }
        
        public Object getAdditionalProperty(String name) {
            throwIfKeyKnown(name, requiredKeys, optionalKeys);
            throwIfKeyNotPresent(name);
            return get(name);
        }
    }
    public class TheDefaultKeywordDoesNotDoAnythingIfThePropertyIsMissingMapInput {
        // Map<String, Object> because addProps is unset
    }
    
    
    public static class TheDefaultKeywordDoesNotDoAnythingIfThePropertyIsMissing1 extends JsonSchema implements SchemaMapValidator<Object, Object, TheDefaultKeywordDoesNotDoAnythingIfThePropertyIsMissingMap<Object>> {
        /*
        NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
        Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
    
        Do not edit the class manually.
        */
        public TheDefaultKeywordDoesNotDoAnythingIfThePropertyIsMissing1() {
            super(new LinkedHashMap<>(Map.ofEntries(
                new KeywordEntry("type", new TypeValidator(Set.of(FrozenMap.class))),
                new KeywordEntry("properties", new PropertiesValidator(Map.ofEntries(
                    new PropertyEntry("alpha", Alpha.class)
                )))
            )));
        }
        
        @Override
        protected TheDefaultKeywordDoesNotDoAnythingIfThePropertyIsMissingMap getMapOutputInstance(FrozenMap<String, Object> arg) {
            return new TheDefaultKeywordDoesNotDoAnythingIfThePropertyIsMissingMap(arg);
        }
        public TheDefaultKeywordDoesNotDoAnythingIfThePropertyIsMissingMap validate(Map<String, Object> arg, SchemaConfiguration configuration) throws ValidationException {
            return validateMap(arg, configuration);
        }
    }

}
