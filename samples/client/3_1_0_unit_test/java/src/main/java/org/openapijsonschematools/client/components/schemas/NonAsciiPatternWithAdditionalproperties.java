package org.openapijsonschematools.client.components.schemas;
import java.util.AbstractMap;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.LinkedHashMap;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Map;
import java.util.Objects;
import java.util.Set;
import java.util.regex.Pattern;
import org.checkerframework.checker.nullness.qual.Nullable;
import org.openapijsonschematools.client.configurations.JsonSchemaKeywordFlags;
import org.openapijsonschematools.client.configurations.SchemaConfiguration;
import org.openapijsonschematools.client.exceptions.InvalidTypeException;
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
import org.openapijsonschematools.client.schemas.validation.ValidationMetadata;

public class NonAsciiPatternWithAdditionalproperties {
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
    
    
    public static class CircumflexAccentLatinSmallLetterAWithAcute extends AnyTypeJsonSchema.AnyTypeJsonSchema1 {
        private static @Nullable CircumflexAccentLatinSmallLetterAWithAcute instance = null;
        public static CircumflexAccentLatinSmallLetterAWithAcute getInstance() {
            if (instance == null) {
                instance = new CircumflexAccentLatinSmallLetterAWithAcute();
            }
            return instance;
        }
    }
    
    
    public static class NonAsciiPatternWithAdditionalpropertiesMap extends FrozenMap<@Nullable Object> {
        protected NonAsciiPatternWithAdditionalpropertiesMap(FrozenMap<@Nullable Object> m) {
            super(m);
        }
        public static final Set<String> requiredKeys = Set.of();
        public static final Set<String> optionalKeys = Set.of();
        // map with no key value pairs
        public static NonAsciiPatternWithAdditionalpropertiesMap of(Map<String, @Nullable Object> arg, SchemaConfiguration configuration) throws ValidationException {
            return NonAsciiPatternWithAdditionalproperties1.getInstance().validate(arg, configuration);
        }
    }
    
    public static class NonAsciiPatternWithAdditionalpropertiesMapBuilder implements GenericBuilder<Map<String, @Nullable Object>> {
        private final Map<String, @Nullable Object> instance;
        private static final Set<String> knownKeys = Set.of();
        public Set<String> getKnownKeys() {
            return knownKeys;
        }
        public NonAsciiPatternWithAdditionalpropertiesMapBuilder() {
            this.instance = new LinkedHashMap<>();
        }
        public Map<String, @Nullable Object> build() {
            return instance;
        }
    }
    
    
    public static abstract sealed class NonAsciiPatternWithAdditionalproperties1Boxed permits NonAsciiPatternWithAdditionalproperties1BoxedMap {}
    
    public static final class NonAsciiPatternWithAdditionalproperties1BoxedMap extends NonAsciiPatternWithAdditionalproperties1Boxed {
        public final NonAsciiPatternWithAdditionalpropertiesMap data;
        private NonAsciiPatternWithAdditionalproperties1BoxedMap(NonAsciiPatternWithAdditionalpropertiesMap data) {
            this.data = data;
        }
    }
    
    
    public static class NonAsciiPatternWithAdditionalproperties1 extends JsonSchema implements MapSchemaValidator<NonAsciiPatternWithAdditionalpropertiesMap, NonAsciiPatternWithAdditionalproperties1BoxedMap> {
        /*
        NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
        Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
    
        Do not edit the class manually.
        */
        private static @Nullable NonAsciiPatternWithAdditionalproperties1 instance = null;
    
        protected NonAsciiPatternWithAdditionalproperties1() {
            super(new JsonSchemaInfo()
                .type(Set.of(Map.class))
                .additionalProperties(AdditionalProperties.class)
                .patternProperties(Map.ofEntries(
                    new AbstractMap.SimpleEntry<>(Pattern.compile("^á"), CircumflexAccentLatinSmallLetterAWithAcute.class)
                ))
            );
        }
    
        public static NonAsciiPatternWithAdditionalproperties1 getInstance() {
            if (instance == null) {
                instance = new NonAsciiPatternWithAdditionalproperties1();
            }
            return instance;
        }
        
        public NonAsciiPatternWithAdditionalpropertiesMap getNewInstance(Map<?, ?> arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) {
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
            return new NonAsciiPatternWithAdditionalpropertiesMap(castProperties);
        }
        
        public NonAsciiPatternWithAdditionalpropertiesMap validate(Map<?, ?> arg, SchemaConfiguration configuration) throws ValidationException, InvalidTypeException {
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
        public NonAsciiPatternWithAdditionalproperties1BoxedMap validateAndBox(Map<?, ?> arg, SchemaConfiguration configuration) throws ValidationException, InvalidTypeException {
            return new NonAsciiPatternWithAdditionalproperties1BoxedMap(validate(arg, configuration));
        }
    }

}
