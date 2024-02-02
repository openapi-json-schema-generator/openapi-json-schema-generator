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
import org.openapijsonschematools.client.exceptions.InvalidAdditionalPropertyException;
import org.openapijsonschematools.client.exceptions.InvalidTypeException;
import org.openapijsonschematools.client.exceptions.UnsetPropertyException;
import org.openapijsonschematools.client.exceptions.ValidationException;
import org.openapijsonschematools.client.schemas.BooleanJsonSchema;
import org.openapijsonschematools.client.schemas.GenericBuilder;
import org.openapijsonschematools.client.schemas.SetMaker;
import org.openapijsonschematools.client.schemas.UnsetAddPropsSetter;
import org.openapijsonschematools.client.schemas.validation.FrozenMap;
import org.openapijsonschematools.client.schemas.validation.JsonSchema;
import org.openapijsonschematools.client.schemas.validation.JsonSchemaInfo;
import org.openapijsonschematools.client.schemas.validation.MapSchemaValidator;
import org.openapijsonschematools.client.schemas.validation.PathToSchemasMap;
import org.openapijsonschematools.client.schemas.validation.PropertyEntry;
import org.openapijsonschematools.client.schemas.validation.StringEnumValidator;
import org.openapijsonschematools.client.schemas.validation.StringSchemaValidator;
import org.openapijsonschematools.client.schemas.validation.StringValueMethod;
import org.openapijsonschematools.client.schemas.validation.ValidationMetadata;

public class Whale {
    // nest classes so all schemas and input/output classes can be public
    
    
    public static class HasBaleen extends BooleanJsonSchema {
        private static @Nullable HasBaleen instance = null;
        public static HasBaleen getInstance() {
            if (instance == null) {
                instance = new HasBaleen();
            }
            return instance;
        }
    }
    
    
    public static class HasTeeth extends BooleanJsonSchema {
        private static @Nullable HasTeeth instance = null;
        public static HasTeeth getInstance() {
            if (instance == null) {
                instance = new HasTeeth();
            }
            return instance;
        }
    }
    
    public enum StringClassNameEnums implements StringValueMethod {
        WHALE("whale");
        private final String value;
    
        StringClassNameEnums(String value) {
            this.value = value;
        }
        public String value() {
            return this.value;
        }
    }
    
    
    public static class ClassName extends JsonSchema implements StringSchemaValidator, StringEnumValidator<StringClassNameEnums> {
        private static @Nullable ClassName instance = null;
    
        protected ClassName() {
            super(new JsonSchemaInfo()
                .type(Set.of(
                    String.class
                ))
                .enumValues(SetMaker.makeSet(
                    "whale"
                ))
            );
        }
    
        public static ClassName getInstance() {
            if (instance == null) {
                instance = new ClassName();
            }
            return instance;
        }
        
        @Override
        public String validate(String arg, SchemaConfiguration configuration) throws ValidationException {
            Set<List<Object>> pathSet = new HashSet<>();
            List<Object> pathToItem = List.of("args[0");
            String castArg = castToAllowedTypes(arg, pathToItem, pathSet);
            SchemaConfiguration usedConfiguration = Objects.requireNonNullElseGet(configuration, () -> new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone()));
            ValidationMetadata validationMetadata = new ValidationMetadata(pathToItem, usedConfiguration, new PathToSchemasMap(), new LinkedHashSet<>());
            getPathToSchemas(this, castArg, validationMetadata, pathSet);
            return castArg;
        }
        
        @Override
        public String validate(StringClassNameEnums arg,SchemaConfiguration configuration) throws ValidationException {
            return validate(arg.value(), configuration);
        }
        
        @Override
        public @Nullable Object validate(@Nullable Object arg, SchemaConfiguration configuration) throws ValidationException, InvalidTypeException {
            if (arg instanceof String) {
                return validate((String) arg, configuration);
            }
            throw new InvalidTypeException("Invalid input type="+getClass(arg)+". It can't be validated by this schema");
        }        
        @Override
        public @Nullable Object getNewInstance(@Nullable Object arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) throws InvalidTypeException {
            if (arg instanceof String) {
                return getNewInstance((String) arg, pathToItem, pathToSchemas);
            }
            throw new InvalidTypeException("Invalid input type="+getClass(arg)+". It can't be instantiated by this schema");
        }
    }    
    
    public static class WhaleMap extends FrozenMap<@Nullable Object> {
        protected WhaleMap(FrozenMap<@Nullable Object> m) {
            super(m);
        }
        public static final Set<String> requiredKeys = Set.of(
            "className"
        );
        public static final Set<String> optionalKeys = Set.of(
            "hasBaleen",
            "hasTeeth"
        );
        public static WhaleMap of(Map<String, ? extends @Nullable Object> arg, SchemaConfiguration configuration) throws ValidationException {
            return Whale1.getInstance().validate(arg, configuration);
        }
        
        public String className() {
                        @Nullable Object value = get("className");
            if (!(value instanceof String)) {
                throw new InvalidTypeException("Invalid value stored for className");
            }
            return (String) value;
        }
        
        public boolean hasBaleen() throws UnsetPropertyException {
            String key = "hasBaleen";
            throwIfKeyNotPresent(key);
            @Nullable Object value = get(key);
            if (!(value instanceof Boolean)) {
                throw new InvalidTypeException("Invalid value stored for hasBaleen");
            }
            return (boolean) value;
        }
        
        public boolean hasTeeth() throws UnsetPropertyException {
            String key = "hasTeeth";
            throwIfKeyNotPresent(key);
            @Nullable Object value = get(key);
            if (!(value instanceof Boolean)) {
                throw new InvalidTypeException("Invalid value stored for hasTeeth");
            }
            return (boolean) value;
        }
        
        public @Nullable Object getAdditionalProperty(String name) throws UnsetPropertyException, InvalidAdditionalPropertyException {
            throwIfKeyKnown(name, requiredKeys, optionalKeys);
            throwIfKeyNotPresent(name);
            return get(name);
        }
    }
    
    public interface SetterForClassName <T> {
        Map<String, @Nullable Object> getInstance();
        T getBuilderAfterClassName(Map<String, @Nullable Object> instance);
        
        default T className(String value) {
            var instance = getInstance();
            instance.put("className", value);
            return getBuilderAfterClassName(instance);
        }
        
        default T className(StringClassNameEnums value) {
            var instance = getInstance();
            instance.put("className", value.value());
            return getBuilderAfterClassName(instance);
        }
    }
    
    public interface SetterForHasBaleen <T> {
        Map<String, @Nullable Object> getInstance();
        T getBuilderAfterHasBaleen(Map<String, @Nullable Object> instance);
        
        default T hasBaleen(boolean value) {
            var instance = getInstance();
            instance.put("hasBaleen", value);
            return getBuilderAfterHasBaleen(instance);
        }
    }
    
    public interface SetterForHasTeeth <T> {
        Map<String, @Nullable Object> getInstance();
        T getBuilderAfterHasTeeth(Map<String, @Nullable Object> instance);
        
        default T hasTeeth(boolean value) {
            var instance = getInstance();
            instance.put("hasTeeth", value);
            return getBuilderAfterHasTeeth(instance);
        }
    }
    
    public static class WhaleMap0Builder extends UnsetAddPropsSetter<WhaleMap0Builder> implements GenericBuilder<Map<String, @Nullable Object>>, SetterForHasBaleen<WhaleMap0Builder>, SetterForHasTeeth<WhaleMap0Builder> {
        private final Map<String, @Nullable Object> instance;
        private static final Set<String> knownKeys = Set.of(
            "className",
            "hasBaleen",
            "hasTeeth"
        );
        public Set<String> getKnownKeys() {
            return knownKeys;
        }
        public WhaleMap0Builder(Map<String, @Nullable Object> instance) {
            this.instance = instance;
        }
        public Map<String, @Nullable Object> build() {
            return instance;
        }
        public Map<String, @Nullable Object> getInstance() {
            return instance;
        }
        public WhaleMap0Builder getBuilderAfterHasBaleen(Map<String, @Nullable Object> instance) {
            return this;
        }
        public WhaleMap0Builder getBuilderAfterHasTeeth(Map<String, @Nullable Object> instance) {
            return this;
        }
        public WhaleMap0Builder getBuilderAfterAdditionalProperty(Map<String, @Nullable Object> instance) {
            return this;
        }
    }
    
    public static class WhaleMapBuilder implements SetterForClassName<WhaleMap0Builder> {
        private final Map<String, @Nullable Object> instance;
        public WhaleMapBuilder() {
            this.instance = new LinkedHashMap<>();
        }
        public Map<String, @Nullable Object> getInstance() {
            return instance;
        }
        public WhaleMap0Builder getBuilderAfterClassName(Map<String, @Nullable Object> instance) {
            return new WhaleMap0Builder(instance);
        }
    }
    
    
    public static class Whale1 extends JsonSchema implements MapSchemaValidator<WhaleMap> {
        /*
        NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
        Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
    
        Do not edit the class manually.
        */
        private static @Nullable Whale1 instance = null;
    
        protected Whale1() {
            super(new JsonSchemaInfo()
                .type(Set.of(Map.class))
                .properties(Map.ofEntries(
                    new PropertyEntry("hasBaleen", HasBaleen.class),
                    new PropertyEntry("hasTeeth", HasTeeth.class),
                    new PropertyEntry("className", ClassName.class)
                ))
                .required(Set.of(
                    "className"
                ))
            );
        }
    
        public static Whale1 getInstance() {
            if (instance == null) {
                instance = new Whale1();
            }
            return instance;
        }
        
        public WhaleMap getNewInstance(Map<?, ?> arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) {
            LinkedHashMap<String, @Nullable Object> properties = new LinkedHashMap<>();
            for(Map.Entry<?, ?> entry: arg.entrySet()) {
                @Nullable Object entryKey = entry.getKey();
                if (!(entryKey instanceof String)) {
                    throw new InvalidTypeException("Invalid non-string key value");
                }
                String propertyName = (String) entryKey;
                List<Object> propertyPathToItem = new ArrayList<>(pathToItem);
                propertyPathToItem.add(propertyName);
                Object value = entry.getValue();
                LinkedHashMap<JsonSchema, Void> schemas = pathToSchemas.get(propertyPathToItem);
                if (schemas == null) {
                    throw new InvalidTypeException("Validation result is invalid, schemas must exist for a pathToItem");
                }
                JsonSchema propertySchema = schemas.entrySet().iterator().next().getKey();
                @Nullable Object propertyInstance = propertySchema.getNewInstance(value, propertyPathToItem, pathToSchemas);
                properties.put(propertyName, propertyInstance);
            }
            FrozenMap<@Nullable Object> castProperties = new FrozenMap<>(properties);
            return new WhaleMap(castProperties);
        }
        
        public WhaleMap validate(Map<?, ?> arg, SchemaConfiguration configuration) throws ValidationException, InvalidTypeException {
            Set<List<Object>> pathSet = new HashSet<>();
            List<Object> pathToItem = List.of("args[0");
            Map<?, ?> castArg = castToAllowedTypes(arg, pathToItem, pathSet);
            SchemaConfiguration usedConfiguration = Objects.requireNonNullElseGet(configuration, () -> new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone()));
            ValidationMetadata validationMetadata = new ValidationMetadata(pathToItem, usedConfiguration, new PathToSchemasMap(), new LinkedHashSet<>());
            PathToSchemasMap pathToSchemasMap = getPathToSchemas(this, castArg, validationMetadata, pathSet);
            return getNewInstance(castArg, validationMetadata.pathToItem(), pathToSchemasMap);
        }
        
        
        @Override
        public @Nullable Object validate(@Nullable Object arg, SchemaConfiguration configuration) throws ValidationException, InvalidTypeException {
            if (arg instanceof Map) {
                return validate((Map<?, ?>) arg, configuration);
            }
            throw new InvalidTypeException("Invalid input type="+getClass(arg)+". It can't be validated by this schema");
        }        
        @Override
        public @Nullable Object getNewInstance(@Nullable Object arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) throws InvalidTypeException {
            if (arg instanceof Map) {
                return getNewInstance((Map<?, ?>) arg, pathToItem, pathToSchemas);
            }
            throw new InvalidTypeException("Invalid input type="+getClass(arg)+". It can't be instantiated by this schema");
        }
    }

}
