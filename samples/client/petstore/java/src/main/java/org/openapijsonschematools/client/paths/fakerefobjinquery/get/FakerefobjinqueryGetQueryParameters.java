package org.openapijsonschematools.client.paths.fakerefobjinquery.get;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.LinkedHashMap;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Map;
import java.util.Objects;
import java.util.Set;
import org.checkerframework.checker.nullness.qual.Nullable;
import org.openapijsonschematools.client.components.schemas.Foo;
import org.openapijsonschematools.client.configurations.JsonSchemaKeywordFlags;
import org.openapijsonschematools.client.configurations.SchemaConfiguration;
import org.openapijsonschematools.client.exceptions.UnsetPropertyException;
import org.openapijsonschematools.client.exceptions.ValidationException;
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

public class FakerefobjinqueryGetQueryParameters {
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
    
    
    public static class QueryParametersMap extends FrozenMap<Foo.FooMap> {
        protected QueryParametersMap(FrozenMap<Foo.FooMap> m) {
            super(m);
        }
        public static final Set<String> requiredKeys = Set.of();
        public static final Set<String> optionalKeys = Set.of(
            "mapBean"
        );
        public static QueryParametersMap of(Map<String, Map<String, ? extends @Nullable Object>> arg, SchemaConfiguration configuration) throws ValidationException {
            return FakerefobjinqueryGetQueryParameters1.getInstance().validate(arg, configuration);
        }
        
        public Foo.FooMap mapBean() throws UnsetPropertyException {
            return getOrThrow("mapBean");
        }
    }
    
    public interface SetterForMapBean <T> {
        Map<String, Map<String, @Nullable Object>> getInstance();
        T getBuilderAfterMapBean(Map<String, Map<String, @Nullable Object>> instance);
        
        default T mapBean(Map<String, @Nullable Object> value) {
            var instance = getInstance();
            instance.put("mapBean", value);
            return getBuilderAfterMapBean(instance);
        }
    }
    
    public static class QueryParametersMapBuilder implements GenericBuilder<Map<String, Map<String, @Nullable Object>>>, SetterForMapBean<QueryParametersMapBuilder> {
        private final Map<String, Map<String, @Nullable Object>> instance;
        private static final Set<String> knownKeys = Set.of(
            "mapBean"
        );
        public Set<String> getKnownKeys() {
            return knownKeys;
        }
        public QueryParametersMapBuilder() {
            this.instance = new LinkedHashMap<>();
        }
        public Map<String, Map<String, @Nullable Object>> build() {
            return instance;
        }
        public Map<String, Map<String, @Nullable Object>> getInstance() {
            return instance;
        }
        public QueryParametersMapBuilder getBuilderAfterMapBean(Map<String, Map<String, @Nullable Object>> instance) {
            return this;
        }
    }
    
    
    public sealed interface FakerefobjinqueryGetQueryParameters1Boxed permits FakerefobjinqueryGetQueryParameters1BoxedMap {
        @Nullable Object getData();
    }
    
    public record FakerefobjinqueryGetQueryParameters1BoxedMap(QueryParametersMap data) implements FakerefobjinqueryGetQueryParameters1Boxed {
        @Override
        public @Nullable Object getData() {
            return data;
        }
    }
    
    
    public static class FakerefobjinqueryGetQueryParameters1 extends JsonSchema<FakerefobjinqueryGetQueryParameters1Boxed> implements MapSchemaValidator<QueryParametersMap, FakerefobjinqueryGetQueryParameters1BoxedMap> {
        private static @Nullable FakerefobjinqueryGetQueryParameters1 instance = null;
    
        protected FakerefobjinqueryGetQueryParameters1() {
            super(new JsonSchemaInfo()
                .type(Set.of(Map.class))
                .properties(Map.ofEntries(
                    new PropertyEntry("mapBean", Foo.Foo1.class)
                ))
                .additionalProperties(AdditionalProperties.class)
            );
        }
    
        public static FakerefobjinqueryGetQueryParameters1 getInstance() {
            if (instance == null) {
                instance = new FakerefobjinqueryGetQueryParameters1();
            }
            return instance;
        }
        
        public QueryParametersMap getNewInstance(Map<?, ?> arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) {
            LinkedHashMap<String, Foo.FooMap> properties = new LinkedHashMap<>();
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
                if (!(propertyInstance instanceof Foo.FooMap)) {
                    throw new RuntimeException("Invalid instantiated value");
                }
                properties.put(propertyName, (Foo.FooMap) propertyInstance);
            }
            FrozenMap<Foo.FooMap> castProperties = new FrozenMap<>(properties);
            return new QueryParametersMap(castProperties);
        }
        
        public QueryParametersMap validate(Map<?, ?> arg, SchemaConfiguration configuration) throws ValidationException {
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
        public FakerefobjinqueryGetQueryParameters1BoxedMap validateAndBox(Map<?, ?> arg, SchemaConfiguration configuration) throws ValidationException {
            return new FakerefobjinqueryGetQueryParameters1BoxedMap(validate(arg, configuration));
        }
        @Override
        public FakerefobjinqueryGetQueryParameters1Boxed validateAndBox(@Nullable Object arg, SchemaConfiguration configuration) throws ValidationException {
            if (arg instanceof Map<?, ?> castArg) {
                return validateAndBox(castArg, configuration);
            }
            throw new ValidationException("Invalid input type="+getClass(arg)+". It can't be validated by this schema");
        }
    }

}
