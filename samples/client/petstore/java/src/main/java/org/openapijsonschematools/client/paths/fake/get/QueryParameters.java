package org.openapijsonschematools.client.paths.fake.get;
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
import org.openapijsonschematools.client.exceptions.InvalidTypeException;
import org.openapijsonschematools.client.exceptions.UnsetPropertyException;
import org.openapijsonschematools.client.exceptions.ValidationException;
import org.openapijsonschematools.client.paths.fake.get.parameters.parameter2.Schema2;
import org.openapijsonschematools.client.paths.fake.get.parameters.parameter3.Schema3;
import org.openapijsonschematools.client.paths.fake.get.parameters.parameter4.Schema4;
import org.openapijsonschematools.client.paths.fake.get.parameters.parameter5.Schema5;
import org.openapijsonschematools.client.schemas.AnyTypeJsonSchema;
import org.openapijsonschematools.client.schemas.GenericBuilder;
import org.openapijsonschematools.client.schemas.NotAnyTypeJsonSchema;
import org.openapijsonschematools.client.schemas.validation.FrozenMap;
import org.openapijsonschematools.client.schemas.validation.JsonSchema;
import org.openapijsonschematools.client.schemas.validation.JsonSchemaInfo;
import org.openapijsonschematools.client.schemas.validation.MapSchemaValidator;
import org.openapijsonschematools.client.schemas.validation.MapUtils;
import org.openapijsonschematools.client.schemas.validation.PathToSchemasMap;
import org.openapijsonschematools.client.schemas.validation.PropertyEntry;
import org.openapijsonschematools.client.schemas.validation.ValidationMetadata;

public class QueryParameters {
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
    
    
    public static class QueryParametersMap extends FrozenMap<@Nullable Object> {
        protected QueryParametersMap(FrozenMap<@Nullable Object> m) {
            super(m);
        }
        public static final Set<String> requiredKeys = Set.of();
        public static final Set<String> optionalKeys = Set.of(
            "enum_query_double",
            "enum_query_string",
            "enum_query_integer",
            "enum_query_string_array"
        );
        public static QueryParametersMap of(Map<String, ? extends @Nullable Object> arg, SchemaConfiguration configuration) throws ValidationException {
            return QueryParameters1.getInstance().validate(arg, configuration);
        }
        
        public Number enum_query_double() throws UnsetPropertyException {
            String key = "enum_query_double";
            throwIfKeyNotPresent(key);
            @Nullable Object value = get(key);
            if (!(value instanceof Number)) {
                throw new InvalidTypeException("Invalid value stored for enum_query_double");
            }
            return (Number) value;
        }
        
        public String enum_query_string() throws UnsetPropertyException {
            String key = "enum_query_string";
            throwIfKeyNotPresent(key);
            @Nullable Object value = get(key);
            if (!(value instanceof String)) {
                throw new InvalidTypeException("Invalid value stored for enum_query_string");
            }
            return (String) value;
        }
        
        public Number enum_query_integer() throws UnsetPropertyException {
            String key = "enum_query_integer";
            throwIfKeyNotPresent(key);
            @Nullable Object value = get(key);
            if (!(value instanceof Number)) {
                throw new InvalidTypeException("Invalid value stored for enum_query_integer");
            }
            return (Number) value;
        }
        
        public Schema2.SchemaList2 enum_query_string_array() throws UnsetPropertyException {
            String key = "enum_query_string_array";
            throwIfKeyNotPresent(key);
            @Nullable Object value = get(key);
            if (!(value instanceof Schema2.SchemaList2)) {
                throw new InvalidTypeException("Invalid value stored for enum_query_string_array");
            }
            return (Schema2.SchemaList2) value;
        }
    }
    
    public interface SetterForEnumQueryDouble <T> {
        Map<String, @Nullable Object> getInstance();
        T getBuilderAfterEnumQueryDouble(Map<String, @Nullable Object> instance);
        
        default T enum_query_double(int value) {
            var instance = getInstance();
            instance.put("enum_query_double", value);
            return getBuilderAfterEnumQueryDouble(instance);
        }
        
        default T enum_query_double(float value) {
            var instance = getInstance();
            instance.put("enum_query_double", value);
            return getBuilderAfterEnumQueryDouble(instance);
        }
        
        default T enum_query_double(long value) {
            var instance = getInstance();
            instance.put("enum_query_double", value);
            return getBuilderAfterEnumQueryDouble(instance);
        }
        
        default T enum_query_double(double value) {
            var instance = getInstance();
            instance.put("enum_query_double", value);
            return getBuilderAfterEnumQueryDouble(instance);
        }
        
        default T enum_query_double(Schema5.DoubleSchemaEnums5 value) {
            var instance = getInstance();
            instance.put("enum_query_double", value.value());
            return getBuilderAfterEnumQueryDouble(instance);
        }
        
        default T enum_query_double(Schema5.FloatSchemaEnums5 value) {
            var instance = getInstance();
            instance.put("enum_query_double", value.value());
            return getBuilderAfterEnumQueryDouble(instance);
        }
    }
    
    public interface SetterForEnumQueryString <T> {
        Map<String, @Nullable Object> getInstance();
        T getBuilderAfterEnumQueryString(Map<String, @Nullable Object> instance);
        
        default T enum_query_string(String value) {
            var instance = getInstance();
            instance.put("enum_query_string", value);
            return getBuilderAfterEnumQueryString(instance);
        }
        
        default T enum_query_string(Schema3.StringSchemaEnums3 value) {
            var instance = getInstance();
            instance.put("enum_query_string", value.value());
            return getBuilderAfterEnumQueryString(instance);
        }
    }
    
    public interface SetterForEnumQueryInteger <T> {
        Map<String, @Nullable Object> getInstance();
        T getBuilderAfterEnumQueryInteger(Map<String, @Nullable Object> instance);
        
        default T enum_query_integer(int value) {
            var instance = getInstance();
            instance.put("enum_query_integer", value);
            return getBuilderAfterEnumQueryInteger(instance);
        }
        
        default T enum_query_integer(float value) {
            var instance = getInstance();
            instance.put("enum_query_integer", value);
            return getBuilderAfterEnumQueryInteger(instance);
        }
        
        default T enum_query_integer(Schema4.IntegerSchemaEnums4 value) {
            var instance = getInstance();
            instance.put("enum_query_integer", value.value());
            return getBuilderAfterEnumQueryInteger(instance);
        }
        
        default T enum_query_integer(Schema4.LongSchemaEnums4 value) {
            var instance = getInstance();
            instance.put("enum_query_integer", value.value());
            return getBuilderAfterEnumQueryInteger(instance);
        }
        
        default T enum_query_integer(Schema4.FloatSchemaEnums4 value) {
            var instance = getInstance();
            instance.put("enum_query_integer", value.value());
            return getBuilderAfterEnumQueryInteger(instance);
        }
        
        default T enum_query_integer(Schema4.DoubleSchemaEnums4 value) {
            var instance = getInstance();
            instance.put("enum_query_integer", value.value());
            return getBuilderAfterEnumQueryInteger(instance);
        }
    }
    
    public interface SetterForEnumQueryStringArray <T> {
        Map<String, @Nullable Object> getInstance();
        T getBuilderAfterEnumQueryStringArray(Map<String, @Nullable Object> instance);
        
        default T enum_query_string_array(List<String> value) {
            var instance = getInstance();
            instance.put("enum_query_string_array", value);
            return getBuilderAfterEnumQueryStringArray(instance);
        }
    }
    
    public static class QueryParametersMapBuilder implements GenericBuilder<Map<String, @Nullable Object>>, SetterForEnumQueryDouble<QueryParametersMapBuilder>, SetterForEnumQueryString<QueryParametersMapBuilder>, SetterForEnumQueryInteger<QueryParametersMapBuilder>, SetterForEnumQueryStringArray<QueryParametersMapBuilder> {
        private final Map<String, @Nullable Object> instance;
        private static final Set<String> knownKeys = Set.of(
            "enum_query_double",
            "enum_query_string",
            "enum_query_integer",
            "enum_query_string_array"
        );
        public Set<String> getKnownKeys() {
            return knownKeys;
        }
        public QueryParametersMapBuilder() {
            this.instance = new LinkedHashMap<>();
        }
        public Map<String, @Nullable Object> build() {
            return instance;
        }
        public Map<String, @Nullable Object> getInstance() {
            return instance;
        }
        public QueryParametersMapBuilder getBuilderAfterEnumQueryDouble(Map<String, @Nullable Object> instance) {
            return this;
        }
        public QueryParametersMapBuilder getBuilderAfterEnumQueryString(Map<String, @Nullable Object> instance) {
            return this;
        }
        public QueryParametersMapBuilder getBuilderAfterEnumQueryInteger(Map<String, @Nullable Object> instance) {
            return this;
        }
        public QueryParametersMapBuilder getBuilderAfterEnumQueryStringArray(Map<String, @Nullable Object> instance) {
            return this;
        }
    }
    
    
    public static abstract sealed class QueryParameters1Boxed permits QueryParameters1BoxedMap {}
    
    public static final class QueryParameters1BoxedMap extends QueryParameters1Boxed {
        public final QueryParametersMap data;
        private QueryParameters1BoxedMap(QueryParametersMap data) {
            this.data = data;
        }
    }
    
    
    public static class QueryParameters1 extends JsonSchema implements MapSchemaValidator<QueryParametersMap, QueryParameters1BoxedMap> {
        private static @Nullable QueryParameters1 instance = null;
    
        protected QueryParameters1() {
            super(new JsonSchemaInfo()
                .type(Set.of(Map.class))
                .properties(Map.ofEntries(
                    new PropertyEntry("enum_query_double", Schema5.Schema51.class),
                    new PropertyEntry("enum_query_string", Schema3.Schema31.class),
                    new PropertyEntry("enum_query_integer", Schema4.Schema41.class),
                    new PropertyEntry("enum_query_string_array", Schema2.Schema21.class)
                ))
                .additionalProperties(AdditionalProperties.class)
            );
        }
    
        public static QueryParameters1 getInstance() {
            if (instance == null) {
                instance = new QueryParameters1();
            }
            return instance;
        }
        
        public QueryParametersMap getNewInstance(Map<?, ?> arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) {
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
            return new QueryParametersMap(castProperties);
        }
        
        public QueryParametersMap validate(Map<?, ?> arg, SchemaConfiguration configuration) throws ValidationException, InvalidTypeException {
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
        @Override
        public QueryParameters1BoxedMap validateAndBox(Map<?, ?> arg, SchemaConfiguration configuration) throws ValidationException, InvalidTypeException {
            return new QueryParameters1BoxedMap(validate(arg, configuration));
        }
    }

}
