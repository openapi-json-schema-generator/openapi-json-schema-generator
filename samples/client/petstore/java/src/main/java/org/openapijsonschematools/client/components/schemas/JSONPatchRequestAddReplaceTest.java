package org.openapijsonschematools.client.components.schemas;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.LinkedHashMap;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Map;
import java.util.Objects;
import java.util.Set;
import org.checkerframework.checker.nullness.qual.Nullable;
import org.openapijsonschematools.client.configurations.JsonSchemaKeywordFlags;
import org.openapijsonschematools.client.configurations.SchemaConfiguration;
import org.openapijsonschematools.client.exceptions.UnsetPropertyException;
import org.openapijsonschematools.client.exceptions.ValidationException;
import org.openapijsonschematools.client.schemas.AnyTypeJsonSchema;
import org.openapijsonschematools.client.schemas.GenericBuilder;
import org.openapijsonschematools.client.schemas.NotAnyTypeJsonSchema;
import org.openapijsonschematools.client.schemas.SetMaker;
import org.openapijsonschematools.client.schemas.StringJsonSchema;
import org.openapijsonschematools.client.schemas.validation.FrozenMap;
import org.openapijsonschematools.client.schemas.validation.JsonSchema;
import org.openapijsonschematools.client.schemas.validation.JsonSchemaInfo;
import org.openapijsonschematools.client.schemas.validation.MapSchemaValidator;
import org.openapijsonschematools.client.schemas.validation.MapUtils;
import org.openapijsonschematools.client.schemas.validation.PathToSchemasMap;
import org.openapijsonschematools.client.schemas.validation.PropertyEntry;
import org.openapijsonschematools.client.schemas.validation.StringEnumValidator;
import org.openapijsonschematools.client.schemas.validation.StringSchemaValidator;
import org.openapijsonschematools.client.schemas.validation.StringValueMethod;
import org.openapijsonschematools.client.schemas.validation.ValidationMetadata;

public class JSONPatchRequestAddReplaceTest {
    // nest classes so all schemas and input/output classes can be public
    
    
    public static class AdditionalProperties extends NotAnyTypeJsonSchema.NotAnyTypeJsonSchema1 {
        // NotAnyTypeSchema
        private static @Nullable AdditionalProperties instance = null;
        public static AdditionalProperties getInstance() {
            if (instance == null) {
                instance = new AdditionalProperties();
            }
            return instance;
        }
    }
    
    
    public static class Path extends StringJsonSchema.StringJsonSchema1 {
        private static @Nullable Path instance = null;
        public static Path getInstance() {
            if (instance == null) {
                instance = new Path();
            }
            return instance;
        }
    }
    
    
    public static class Value extends AnyTypeJsonSchema.AnyTypeJsonSchema1 {
        private static @Nullable Value instance = null;
        public static Value getInstance() {
            if (instance == null) {
                instance = new Value();
            }
            return instance;
        }
    }
    
    public enum StringOpEnums implements StringValueMethod {
        ADD("add"),
        REPLACE("replace"),
        TEST("test");
        private final String value;
    
        StringOpEnums(String value) {
            this.value = value;
        }
        public String value() {
            return this.value;
        }
    }
    
    
    public sealed interface OpBoxed permits OpBoxedString {
        @Nullable Object getData();
    }
    
    public record OpBoxedString(String data) implements OpBoxed {
        @Override
        public @Nullable Object getData() {
            return data;
        }
    }
    
    
    
    public static class Op extends JsonSchema<OpBoxed> implements StringSchemaValidator<OpBoxedString>, StringEnumValidator<StringOpEnums> {
        private static @Nullable Op instance = null;
    
        protected Op() {
            super(new JsonSchemaInfo()
                .type(Set.of(
                    String.class
                ))
                .enumValues(SetMaker.makeSet(
                    "add",
                    "replace",
                    "test"
                ))
            );
        }
    
        public static Op getInstance() {
            if (instance == null) {
                instance = new Op();
            }
            return instance;
        }
        
        @Override
        public String validate(String arg, SchemaConfiguration configuration) throws ValidationException {
            Set<List<Object>> pathSet = new HashSet<>();
            List<Object> pathToItem = List.of("args[0");
            String castArg = castToAllowedTypes(arg, pathToItem, pathSet);
            SchemaConfiguration usedConfiguration = Objects.requireNonNullElseGet(configuration, () -> new SchemaConfiguration(new JsonSchemaKeywordFlags.Builder().build()));
            ValidationMetadata validationMetadata = new ValidationMetadata(pathToItem, usedConfiguration, new PathToSchemasMap(), new LinkedHashSet<>());
            getPathToSchemas(this, castArg, validationMetadata, pathSet);
            return castArg;
        }
        
        @Override
        public String validate(StringOpEnums arg,SchemaConfiguration configuration) throws ValidationException {
            return validate(arg.value(), configuration);
        }
        
        @Override
        public @Nullable Object validate(@Nullable Object arg, SchemaConfiguration configuration) throws ValidationException {
            if (arg instanceof String) {
                return validate((String) arg, configuration);
            }
            throw new ValidationException("Invalid input type="+getClass(arg)+". It can't be validated by this schema");
        }        
        @Override
        public @Nullable Object getNewInstance(@Nullable Object arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) {
            if (arg instanceof String) {
                return getNewInstance((String) arg, pathToItem, pathToSchemas);
            }
            throw new RuntimeException("Invalid input type="+getClass(arg)+". It can't be instantiated by this schema");
        }
        @Override
        public OpBoxedString validateAndBox(String arg, SchemaConfiguration configuration) throws ValidationException {
            return new OpBoxedString(validate(arg, configuration));
        }
        @Override
        public OpBoxed validateAndBox(@Nullable Object arg, SchemaConfiguration configuration) throws ValidationException {
            if (arg instanceof String castArg) {
                return validateAndBox(castArg, configuration);
            }
            throw new ValidationException("Invalid input type="+getClass(arg)+". It can't be validated by this schema");
        }
    }    
    
    public static class JSONPatchRequestAddReplaceTestMap extends FrozenMap<@Nullable Object> {
        protected JSONPatchRequestAddReplaceTestMap(FrozenMap<@Nullable Object> m) {
            super(m);
        }
        public static final Set<String> requiredKeys = Set.of(
            "op",
            "path",
            "value"
        );
        public static final Set<String> optionalKeys = Set.of();
        public static JSONPatchRequestAddReplaceTestMap of(Map<String, ? extends @Nullable Object> arg, SchemaConfiguration configuration) throws ValidationException {
            return JSONPatchRequestAddReplaceTest1.getInstance().validate(arg, configuration);
        }
        
        public String op() {
                        @Nullable Object value = get("op");
            if (!(value instanceof String)) {
                throw new RuntimeException("Invalid value stored for op");
            }
            return (String) value;
        }
        
        public String path() {
                        @Nullable Object value = get("path");
            if (!(value instanceof String)) {
                throw new RuntimeException("Invalid value stored for path");
            }
            return (String) value;
        }
        
        public @Nullable Object value() {
            try {
                return getOrThrow("version");
            } catch (UnsetPropertyException e) {
                throw new RuntimeException(e);
            }
        }
    }
    
    public interface SetterForOp <T> {
        Map<String, @Nullable Object> getInstance();
        T getBuilderAfterOp(Map<String, @Nullable Object> instance);
        
        default T op(String value) {
            var instance = getInstance();
            instance.put("op", value);
            return getBuilderAfterOp(instance);
        }
        
        default T op(StringOpEnums value) {
            var instance = getInstance();
            instance.put("op", value.value());
            return getBuilderAfterOp(instance);
        }
    }
    
    public interface SetterForPath <T> {
        Map<String, @Nullable Object> getInstance();
        T getBuilderAfterPath(Map<String, @Nullable Object> instance);
        
        default T path(String value) {
            var instance = getInstance();
            instance.put("path", value);
            return getBuilderAfterPath(instance);
        }
    }
    
    public interface SetterForValue <T> {
        Map<String, @Nullable Object> getInstance();
        T getBuilderAfterValue(Map<String, @Nullable Object> instance);
        
        default T value(Void value) {
            var instance = getInstance();
            instance.put("value", null);
            return getBuilderAfterValue(instance);
        }
        
        default T value(boolean value) {
            var instance = getInstance();
            instance.put("value", value);
            return getBuilderAfterValue(instance);
        }
        
        default T value(String value) {
            var instance = getInstance();
            instance.put("value", value);
            return getBuilderAfterValue(instance);
        }
        
        default T value(int value) {
            var instance = getInstance();
            instance.put("value", value);
            return getBuilderAfterValue(instance);
        }
        
        default T value(float value) {
            var instance = getInstance();
            instance.put("value", value);
            return getBuilderAfterValue(instance);
        }
        
        default T value(long value) {
            var instance = getInstance();
            instance.put("value", value);
            return getBuilderAfterValue(instance);
        }
        
        default T value(double value) {
            var instance = getInstance();
            instance.put("value", value);
            return getBuilderAfterValue(instance);
        }
        
        default T value(List<?> value) {
            var instance = getInstance();
            instance.put("value", value);
            return getBuilderAfterValue(instance);
        }
        
        default T value(Map<String, ?> value) {
            var instance = getInstance();
            instance.put("value", value);
            return getBuilderAfterValue(instance);
        }
    }
    
    public static class JSONPatchRequestAddReplaceTestMap000Builder implements GenericBuilder<Map<String, @Nullable Object>> {
        private final Map<String, @Nullable Object> instance;
        private static final Set<String> knownKeys = Set.of(
            "op",
            "path",
            "value"
        );
        public Set<String> getKnownKeys() {
            return knownKeys;
        }
        public JSONPatchRequestAddReplaceTestMap000Builder(Map<String, @Nullable Object> instance) {
            this.instance = instance;
        }
        public Map<String, @Nullable Object> build() {
            return instance;
        }
    }
    
    public static class JSONPatchRequestAddReplaceTestMap001Builder implements SetterForValue<JSONPatchRequestAddReplaceTestMap000Builder> {
        private final Map<String, @Nullable Object> instance;
        public JSONPatchRequestAddReplaceTestMap001Builder(Map<String, @Nullable Object> instance) {
            this.instance = instance;
        }
        public Map<String, @Nullable Object> getInstance() {
            return instance;
        }
        public JSONPatchRequestAddReplaceTestMap000Builder getBuilderAfterValue(Map<String, @Nullable Object> instance) {
            return new JSONPatchRequestAddReplaceTestMap000Builder(instance);
        }
    }
    
    public static class JSONPatchRequestAddReplaceTestMap010Builder implements SetterForPath<JSONPatchRequestAddReplaceTestMap000Builder> {
        private final Map<String, @Nullable Object> instance;
        public JSONPatchRequestAddReplaceTestMap010Builder(Map<String, @Nullable Object> instance) {
            this.instance = instance;
        }
        public Map<String, @Nullable Object> getInstance() {
            return instance;
        }
        public JSONPatchRequestAddReplaceTestMap000Builder getBuilderAfterPath(Map<String, @Nullable Object> instance) {
            return new JSONPatchRequestAddReplaceTestMap000Builder(instance);
        }
    }
    
    public static class JSONPatchRequestAddReplaceTestMap011Builder implements SetterForPath<JSONPatchRequestAddReplaceTestMap001Builder>, SetterForValue<JSONPatchRequestAddReplaceTestMap010Builder> {
        private final Map<String, @Nullable Object> instance;
        public JSONPatchRequestAddReplaceTestMap011Builder(Map<String, @Nullable Object> instance) {
            this.instance = instance;
        }
        public Map<String, @Nullable Object> getInstance() {
            return instance;
        }
        public JSONPatchRequestAddReplaceTestMap001Builder getBuilderAfterPath(Map<String, @Nullable Object> instance) {
            return new JSONPatchRequestAddReplaceTestMap001Builder(instance);
        }
        public JSONPatchRequestAddReplaceTestMap010Builder getBuilderAfterValue(Map<String, @Nullable Object> instance) {
            return new JSONPatchRequestAddReplaceTestMap010Builder(instance);
        }
    }
    
    public static class JSONPatchRequestAddReplaceTestMap100Builder implements SetterForOp<JSONPatchRequestAddReplaceTestMap000Builder> {
        private final Map<String, @Nullable Object> instance;
        public JSONPatchRequestAddReplaceTestMap100Builder(Map<String, @Nullable Object> instance) {
            this.instance = instance;
        }
        public Map<String, @Nullable Object> getInstance() {
            return instance;
        }
        public JSONPatchRequestAddReplaceTestMap000Builder getBuilderAfterOp(Map<String, @Nullable Object> instance) {
            return new JSONPatchRequestAddReplaceTestMap000Builder(instance);
        }
    }
    
    public static class JSONPatchRequestAddReplaceTestMap101Builder implements SetterForOp<JSONPatchRequestAddReplaceTestMap001Builder>, SetterForValue<JSONPatchRequestAddReplaceTestMap100Builder> {
        private final Map<String, @Nullable Object> instance;
        public JSONPatchRequestAddReplaceTestMap101Builder(Map<String, @Nullable Object> instance) {
            this.instance = instance;
        }
        public Map<String, @Nullable Object> getInstance() {
            return instance;
        }
        public JSONPatchRequestAddReplaceTestMap001Builder getBuilderAfterOp(Map<String, @Nullable Object> instance) {
            return new JSONPatchRequestAddReplaceTestMap001Builder(instance);
        }
        public JSONPatchRequestAddReplaceTestMap100Builder getBuilderAfterValue(Map<String, @Nullable Object> instance) {
            return new JSONPatchRequestAddReplaceTestMap100Builder(instance);
        }
    }
    
    public static class JSONPatchRequestAddReplaceTestMap110Builder implements SetterForOp<JSONPatchRequestAddReplaceTestMap010Builder>, SetterForPath<JSONPatchRequestAddReplaceTestMap100Builder> {
        private final Map<String, @Nullable Object> instance;
        public JSONPatchRequestAddReplaceTestMap110Builder(Map<String, @Nullable Object> instance) {
            this.instance = instance;
        }
        public Map<String, @Nullable Object> getInstance() {
            return instance;
        }
        public JSONPatchRequestAddReplaceTestMap010Builder getBuilderAfterOp(Map<String, @Nullable Object> instance) {
            return new JSONPatchRequestAddReplaceTestMap010Builder(instance);
        }
        public JSONPatchRequestAddReplaceTestMap100Builder getBuilderAfterPath(Map<String, @Nullable Object> instance) {
            return new JSONPatchRequestAddReplaceTestMap100Builder(instance);
        }
    }
    
    public static class JSONPatchRequestAddReplaceTestMapBuilder implements SetterForOp<JSONPatchRequestAddReplaceTestMap011Builder>, SetterForPath<JSONPatchRequestAddReplaceTestMap101Builder>, SetterForValue<JSONPatchRequestAddReplaceTestMap110Builder> {
        private final Map<String, @Nullable Object> instance;
        public JSONPatchRequestAddReplaceTestMapBuilder() {
            this.instance = new LinkedHashMap<>();
        }
        public Map<String, @Nullable Object> getInstance() {
            return instance;
        }
        public JSONPatchRequestAddReplaceTestMap011Builder getBuilderAfterOp(Map<String, @Nullable Object> instance) {
            return new JSONPatchRequestAddReplaceTestMap011Builder(instance);
        }
        public JSONPatchRequestAddReplaceTestMap101Builder getBuilderAfterPath(Map<String, @Nullable Object> instance) {
            return new JSONPatchRequestAddReplaceTestMap101Builder(instance);
        }
        public JSONPatchRequestAddReplaceTestMap110Builder getBuilderAfterValue(Map<String, @Nullable Object> instance) {
            return new JSONPatchRequestAddReplaceTestMap110Builder(instance);
        }
    }
    
    
    public sealed interface JSONPatchRequestAddReplaceTest1Boxed permits JSONPatchRequestAddReplaceTest1BoxedMap {
        @Nullable Object getData();
    }
    
    public record JSONPatchRequestAddReplaceTest1BoxedMap(JSONPatchRequestAddReplaceTestMap data) implements JSONPatchRequestAddReplaceTest1Boxed {
        @Override
        public @Nullable Object getData() {
            return data;
        }
    }
    
    
    public static class JSONPatchRequestAddReplaceTest1 extends JsonSchema<JSONPatchRequestAddReplaceTest1Boxed> implements MapSchemaValidator<JSONPatchRequestAddReplaceTestMap, JSONPatchRequestAddReplaceTest1BoxedMap> {
        /*
        NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
        Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
    
        Do not edit the class manually.
        */
        private static @Nullable JSONPatchRequestAddReplaceTest1 instance = null;
    
        protected JSONPatchRequestAddReplaceTest1() {
            super(new JsonSchemaInfo()
                .type(Set.of(Map.class))
                .properties(Map.ofEntries(
                    new PropertyEntry("path", Path.class),
                    new PropertyEntry("value", Value.class),
                    new PropertyEntry("op", Op.class)
                ))
                .required(Set.of(
                    "op",
                    "path",
                    "value"
                ))
                .additionalProperties(AdditionalProperties.class)
            );
        }
    
        public static JSONPatchRequestAddReplaceTest1 getInstance() {
            if (instance == null) {
                instance = new JSONPatchRequestAddReplaceTest1();
            }
            return instance;
        }
        
        public JSONPatchRequestAddReplaceTestMap getNewInstance(Map<?, ?> arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) {
            LinkedHashMap<String, @Nullable Object> properties = new LinkedHashMap<>();
            for(Map.Entry<?, ?> entry: arg.entrySet()) {
                @Nullable Object entryKey = entry.getKey();
                if (!(entryKey instanceof String)) {
                    throw new RuntimeException("Invalid non-string key value");
                }
                String propertyName = (String) entryKey;
                List<Object> propertyPathToItem = new ArrayList<>(pathToItem);
                propertyPathToItem.add(propertyName);
                Object value = entry.getValue();
                LinkedHashMap<JsonSchema<?>, Void> schemas = pathToSchemas.get(propertyPathToItem);
                if (schemas == null) {
                    throw new RuntimeException("Validation result is invalid, schemas must exist for a pathToItem");
                }
                JsonSchema<?> propertySchema = schemas.entrySet().iterator().next().getKey();
                @Nullable Object propertyInstance = propertySchema.getNewInstance(value, propertyPathToItem, pathToSchemas);
                properties.put(propertyName, propertyInstance);
            }
            FrozenMap<@Nullable Object> castProperties = new FrozenMap<>(properties);
            return new JSONPatchRequestAddReplaceTestMap(castProperties);
        }
        
        public JSONPatchRequestAddReplaceTestMap validate(Map<?, ?> arg, SchemaConfiguration configuration) throws ValidationException {
            Set<List<Object>> pathSet = new HashSet<>();
            List<Object> pathToItem = List.of("args[0");
            Map<?, ?> castArg = castToAllowedTypes(arg, pathToItem, pathSet);
            SchemaConfiguration usedConfiguration = Objects.requireNonNullElseGet(configuration, () -> new SchemaConfiguration(new JsonSchemaKeywordFlags.Builder().build()));
            ValidationMetadata validationMetadata = new ValidationMetadata(pathToItem, usedConfiguration, new PathToSchemasMap(), new LinkedHashSet<>());
            PathToSchemasMap pathToSchemasMap = getPathToSchemas(this, castArg, validationMetadata, pathSet);
            return getNewInstance(castArg, validationMetadata.pathToItem(), pathToSchemasMap);
        }
        
        
        @Override
        public @Nullable Object validate(@Nullable Object arg, SchemaConfiguration configuration) throws ValidationException {
            if (arg instanceof Map) {
                return validate((Map<?, ?>) arg, configuration);
            }
            throw new ValidationException("Invalid input type="+getClass(arg)+". It can't be validated by this schema");
        }        
        @Override
        public @Nullable Object getNewInstance(@Nullable Object arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) {
            if (arg instanceof Map) {
                return getNewInstance((Map<?, ?>) arg, pathToItem, pathToSchemas);
            }
            throw new RuntimeException("Invalid input type="+getClass(arg)+". It can't be instantiated by this schema");
        }
        @Override
        public JSONPatchRequestAddReplaceTest1BoxedMap validateAndBox(Map<?, ?> arg, SchemaConfiguration configuration) throws ValidationException {
            return new JSONPatchRequestAddReplaceTest1BoxedMap(validate(arg, configuration));
        }
        @Override
        public JSONPatchRequestAddReplaceTest1Boxed validateAndBox(@Nullable Object arg, SchemaConfiguration configuration) throws ValidationException {
            if (arg instanceof Map<?, ?> castArg) {
                return validateAndBox(castArg, configuration);
            }
            throw new ValidationException("Invalid input type="+getClass(arg)+". It can't be validated by this schema");
        }
    }

}
