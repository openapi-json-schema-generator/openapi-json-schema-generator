package org.openapijsonschematools.client.components.schemas;
import java.time.LocalDate;
import java.time.ZonedDateTime;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.LinkedHashMap;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Map;
import java.util.Objects;
import java.util.Set;
import java.util.UUID;
import org.openapijsonschematools.client.configurations.JsonSchemaKeywordFlags;
import org.openapijsonschematools.client.configurations.SchemaConfiguration;
import org.openapijsonschematools.client.exceptions.InvalidTypeException;
import org.openapijsonschematools.client.exceptions.ValidationException;
import org.openapijsonschematools.client.schemas.AnyTypeJsonSchema;
import org.openapijsonschematools.client.schemas.BooleanJsonSchema;
import org.openapijsonschematools.client.schemas.validation.AdditionalPropertiesValidator;
import org.openapijsonschematools.client.schemas.validation.AllOfValidator;
import org.openapijsonschematools.client.schemas.validation.FrozenList;
import org.openapijsonschematools.client.schemas.validation.FrozenMap;
import org.openapijsonschematools.client.schemas.validation.JsonSchema;
import org.openapijsonschematools.client.schemas.validation.KeywordEntry;
import org.openapijsonschematools.client.schemas.validation.PathToSchemasMap;
import org.openapijsonschematools.client.schemas.validation.PropertiesValidator;
import org.openapijsonschematools.client.schemas.validation.PropertyEntry;
import org.openapijsonschematools.client.schemas.validation.SchemaBooleanValidator;
import org.openapijsonschematools.client.schemas.validation.SchemaListValidator;
import org.openapijsonschematools.client.schemas.validation.SchemaMapValidator;
import org.openapijsonschematools.client.schemas.validation.SchemaNullValidator;
import org.openapijsonschematools.client.schemas.validation.SchemaNumberValidator;
import org.openapijsonschematools.client.schemas.validation.SchemaStringValidator;
import org.openapijsonschematools.client.schemas.validation.ValidationMetadata;

public class AdditionalpropertiesShouldNotLookInApplicators {
    // nest classes so all schemas and input/output classes can be public
    
    
    public static class AdditionalProperties extends BooleanJsonSchema {}
    
    
    public static class Foo extends AnyTypeJsonSchema {}
    
    
    public static class Schema0Map extends FrozenMap<Object> {
        Schema0Map(FrozenMap<Object> m) {
            super(m);
        }
        public static final Set<String> requiredKeys = Set.of();
        public static final Set<String> optionalKeys = Set.of(
            "foo"
        );
        public static Schema0Map of(Map<String, Object> arg, SchemaConfiguration configuration) throws ValidationException {
            return Schema0.getInstance().validate(arg, configuration);
        }
        
        public Object foo() {
            String key = "foo";
            throwIfKeyNotPresent(key);
            return get(key);
        }
        
        public Object getAdditionalProperty(String name) {
            throwIfKeyKnown(name, requiredKeys, optionalKeys);
            throwIfKeyNotPresent(name);
            return get(name);
        }
    }
    public static class Schema0MapInput {
        // Map<String, Object> because addProps is unset
    }
    
    
    public static class Schema0 extends JsonSchema implements SchemaNullValidator, SchemaBooleanValidator, SchemaNumberValidator, SchemaStringValidator, SchemaListValidator<Object, Object, FrozenList<Object>>, SchemaMapValidator<Object, Object, Schema0Map> {
        private static Schema0 instance;
        protected Schema0() {
            super(new LinkedHashMap<>(Map.ofEntries(
                new KeywordEntry("properties", new PropertiesValidator(Map.ofEntries(
                    new PropertyEntry("foo", Foo.class)
                )))
            )));
        }
    
        public static Schema0 getInstance() {
            if (instance == null) {
                instance = new Schema0();
            }
            return instance;
        }
        @Override
        public Void castToAllowedTypes(Void arg, List<Object> pathToItem, Set<List<Object>> pathSet) {
            return castToAllowedVoidTypes(arg, pathToItem, pathSet);
        }
        
        @Override
        public Void getNewInstance(Void arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) {
            return arg;
        }
        
        @Override
        public Void validate(Void arg, SchemaConfiguration configuration) throws ValidationException, InvalidTypeException {
            Set<List<Object>> pathSet = new HashSet<>();
            List<Object> pathToItem = new ArrayList<>();
            pathToItem.add("args[0]");
            Void castArg = castToAllowedTypes(arg, pathToItem, pathSet);
            SchemaConfiguration usedConfiguration = Objects.requireNonNullElseGet(configuration, () -> new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone()));
            PathToSchemasMap validatedPathToSchemas = new PathToSchemasMap();
            ValidationMetadata validationMetadata = new ValidationMetadata(pathToItem, usedConfiguration, validatedPathToSchemas, new LinkedHashSet<>());
            PathToSchemasMap pathToSchemasMap = getPathToSchemas(this, castArg, validationMetadata, pathSet);
            return getNewInstance(castArg, validationMetadata.pathToItem(), pathToSchemasMap);
        }
        
        @Override
        public boolean castToAllowedTypes(boolean arg, List<Object> pathToItem, Set<List<Object>> pathSet) {
            return castToAllowedBooleanTypes(arg, pathToItem, pathSet);
        }
        
        @Override
        public boolean getNewInstance(boolean arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) {
            return arg;
        }
        
        @Override
        public boolean validate(boolean arg, SchemaConfiguration configuration) throws ValidationException, InvalidTypeException {
            Set<List<Object>> pathSet = new HashSet<>();
            List<Object> pathToItem = new ArrayList<>();
            pathToItem.add("args[0]");
            boolean castArg = castToAllowedTypes(arg, pathToItem, pathSet);
            SchemaConfiguration usedConfiguration = Objects.requireNonNullElseGet(configuration, () -> new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone()));
            PathToSchemasMap validatedPathToSchemas = new PathToSchemasMap();
            ValidationMetadata validationMetadata = new ValidationMetadata(pathToItem, usedConfiguration, validatedPathToSchemas, new LinkedHashSet<>());
            PathToSchemasMap pathToSchemasMap = getPathToSchemas(this, castArg, validationMetadata, pathSet);
            return getNewInstance(castArg, validationMetadata.pathToItem(), pathToSchemasMap);
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
        public Number validate(Number arg, SchemaConfiguration configuration) throws ValidationException, InvalidTypeException {
            Set<List<Object>> pathSet = new HashSet<>();
            List<Object> pathToItem = new ArrayList<>();
            pathToItem.add("args[0]");
            Number castArg = castToAllowedTypes(arg, pathToItem, pathSet);
            SchemaConfiguration usedConfiguration = Objects.requireNonNullElseGet(configuration, () -> new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone()));
            PathToSchemasMap validatedPathToSchemas = new PathToSchemasMap();
            ValidationMetadata validationMetadata = new ValidationMetadata(pathToItem, usedConfiguration, validatedPathToSchemas, new LinkedHashSet<>());
            PathToSchemasMap pathToSchemasMap = getPathToSchemas(this, castArg, validationMetadata, pathSet);
            return getNewInstance(castArg, validationMetadata.pathToItem(), pathToSchemasMap);
        }
        
        public int validate(int arg, SchemaConfiguration configuration) {
            return (int) validate((Number) arg, configuration);
        }
        
        public long validate(long arg, SchemaConfiguration configuration) {
            return (long) validate((Number) arg, configuration);
        }
        
        public float validate(float arg, SchemaConfiguration configuration) {
            return (float) validate((Number) arg, configuration);
        }
        
        public double validate(double arg, SchemaConfiguration configuration) {
            return (double) validate((Number) arg, configuration);
        }
        
        @Override
        public String castToAllowedTypes(String arg, List<Object> pathToItem, Set<List<Object>> pathSet) {
            return castToAllowedStringTypes(arg, pathToItem, pathSet);
        }
        
        @Override
        public String getNewInstance(String arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) {
            return arg;
        }
        
        @Override
        public String validate(String arg, SchemaConfiguration configuration) throws ValidationException, InvalidTypeException {
            Set<List<Object>> pathSet = new HashSet<>();
            List<Object> pathToItem = new ArrayList<>();
            pathToItem.add("args[0]");
            String castArg = castToAllowedTypes(arg, pathToItem, pathSet);
            SchemaConfiguration usedConfiguration = Objects.requireNonNullElseGet(configuration, () -> new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone()));
            PathToSchemasMap validatedPathToSchemas = new PathToSchemasMap();
            ValidationMetadata validationMetadata = new ValidationMetadata(pathToItem, usedConfiguration, validatedPathToSchemas, new LinkedHashSet<>());
            PathToSchemasMap pathToSchemasMap = getPathToSchemas(this, castArg, validationMetadata, pathSet);
            return getNewInstance(castArg, validationMetadata.pathToItem(), pathToSchemasMap);
        }
        
        public String validate(LocalDate arg, SchemaConfiguration configuration) throws ValidationException {
            return validate(arg.toString(), configuration);
        }
        
        public String validate(ZonedDateTime arg, SchemaConfiguration configuration) throws ValidationException {
            return validate(arg.toString(), configuration);
        }
        
        public String validate(UUID arg, SchemaConfiguration configuration) throws ValidationException {
            return validate(arg.toString(), configuration);
        }
        
        @Override
        public FrozenList<Object> castToAllowedTypes(List<Object> arg, List<Object> pathToItem, Set<List<Object>> pathSet) {
            return castToAllowedListTypes(arg, pathToItem, pathSet);
        }
        
        @Override
        public FrozenList<Object> getNewInstance(FrozenList<Object> arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) {
            return arg;
        }
        
        @Override
        public FrozenList<Object> validate(List<Object> arg, SchemaConfiguration configuration) throws ValidationException, InvalidTypeException {
            Set<List<Object>> pathSet = new HashSet<>();
            List<Object> pathToItem = new ArrayList<>();
            pathToItem.add("args[0]");
            FrozenList<Object> castArg = castToAllowedTypes(arg, pathToItem, pathSet);
            SchemaConfiguration usedConfiguration = Objects.requireNonNullElseGet(configuration, () -> new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone()));
            PathToSchemasMap validatedPathToSchemas = new PathToSchemasMap();
            ValidationMetadata validationMetadata = new ValidationMetadata(pathToItem, usedConfiguration, validatedPathToSchemas, new LinkedHashSet<>());
            PathToSchemasMap pathToSchemasMap = getPathToSchemas(this, castArg, validationMetadata, pathSet);
            return getNewInstance(castArg, validationMetadata.pathToItem(), pathToSchemasMap);
        }
        
        @Override
        public FrozenMap<Object> castToAllowedTypes(Map<String, Object> arg, List<Object> pathToItem, Set<List<Object>> pathSet) {
            pathSet.add(pathToItem);
            LinkedHashMap<String, Object> argFixed = new LinkedHashMap<>();
            for (Map.Entry<String, Object> entry: arg.entrySet()) {
                String key = entry.getKey();
                                Object val = entry.getValue();
                List<Object> newPathToItem = new ArrayList<>(pathToItem);
                newPathToItem.add(key);
                                Object fixedVal = (Object) castToAllowedObjectTypes(val, newPathToItem, pathSet);
                argFixed.put(key, fixedVal);
            }
            return new FrozenMap<>(argFixed);
        }
        
        @Override
        public Schema0Map getNewInstance(FrozenMap<Object> arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) {
            LinkedHashMap<String, Object> properties = new LinkedHashMap<>();
            for(Map.Entry<String, Object> entry: arg.entrySet()) {
                String propertyName = entry.getKey();
                List<Object> propertyPathToItem = new ArrayList<>(pathToItem);
                propertyPathToItem.add(propertyName);
                                Object value = entry.getValue();
                JsonSchema propertySchema = pathToSchemas.get(propertyPathToItem).entrySet().iterator().next().getKey();
                                Object castValue = (Object) propertySchema.getNewInstance(value, propertyPathToItem, pathToSchemas);
                properties.put(propertyName, castValue);
            }
            FrozenMap<Object> castProperties = new FrozenMap<>(properties);
            return new Schema0Map(castProperties);
        }
        
        @Override
        public Schema0Map validate(Map<String, Object> arg, SchemaConfiguration configuration) throws ValidationException, InvalidTypeException {
            Set<List<Object>> pathSet = new HashSet<>();
            List<Object> pathToItem = new ArrayList<>();
            pathToItem.add("args[0]");
            FrozenMap<Object> castArg = castToAllowedTypes(arg, pathToItem, pathSet);
            SchemaConfiguration usedConfiguration = Objects.requireNonNullElseGet(configuration, () -> new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone()));
            PathToSchemasMap validatedPathToSchemas = new PathToSchemasMap();
            ValidationMetadata validationMetadata = new ValidationMetadata(pathToItem, usedConfiguration, validatedPathToSchemas, new LinkedHashSet<>());
            PathToSchemasMap pathToSchemasMap = getPathToSchemas(this, castArg, validationMetadata, pathSet);
            return getNewInstance(castArg, validationMetadata.pathToItem(), pathToSchemasMap);
        }
        
        @Override
        public Object getNewInstance(Object arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) {
            if (arg == null) {
                return getNewInstance((Void) null, pathToItem, pathToSchemas);
            } else if (arg instanceof Boolean) {
                boolean boolArg = (Boolean) arg;
                return getNewInstance(boolArg, pathToItem, pathToSchemas);
            } else if (arg instanceof Number) {
                return getNewInstance((Number) arg, pathToItem, pathToSchemas);
            } else if (arg instanceof String) {
                return getNewInstance((String) arg, pathToItem, pathToSchemas);
            } else if (arg instanceof FrozenList) {
                @SuppressWarnings("unchecked") FrozenList<Object> castArg = (FrozenList<Object>) arg;
                return getNewInstance(castArg, pathToItem, pathToSchemas);
            } else if (arg instanceof FrozenMap) {
                @SuppressWarnings("unchecked") FrozenMap<Object> castArg = (FrozenMap<Object>) arg;
                return getNewInstance(castArg, pathToItem, pathToSchemas);
            }
            throw new InvalidTypeException("Invalid input type="+arg.getClass()+". It can't be instantiated by this schema");
        }
    }    
    
    public static class AdditionalpropertiesShouldNotLookInApplicatorsMap extends FrozenMap<Boolean> {
        AdditionalpropertiesShouldNotLookInApplicatorsMap(FrozenMap<Boolean> m) {
            super(m);
        }
        public static final Set<String> requiredKeys = Set.of();
        public static final Set<String> optionalKeys = Set.of();
        public static AdditionalpropertiesShouldNotLookInApplicatorsMap of(Map<String, Boolean> arg, SchemaConfiguration configuration) throws ValidationException {
            return AdditionalpropertiesShouldNotLookInApplicators1.getInstance().validate(arg, configuration);
        }
        
        public boolean getAdditionalProperty(String name) {
            throwIfKeyNotPresent(name);
            return get(name);
        }
    }
    public static class AdditionalpropertiesShouldNotLookInApplicatorsMapInput {
        // Map<String, additionalProperties>
    }
    
    
    public static class AdditionalpropertiesShouldNotLookInApplicators1 extends JsonSchema implements SchemaNullValidator, SchemaBooleanValidator, SchemaNumberValidator, SchemaStringValidator, SchemaListValidator<Object, Object, FrozenList<Object>>, SchemaMapValidator<Boolean, Boolean, AdditionalpropertiesShouldNotLookInApplicatorsMap> {
        /*
        NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
        Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
    
        Do not edit the class manually.
        */
        private static AdditionalpropertiesShouldNotLookInApplicators1 instance;
        protected AdditionalpropertiesShouldNotLookInApplicators1() {
            super(new LinkedHashMap<>(Map.ofEntries(
                new KeywordEntry("additionalProperties", new AdditionalPropertiesValidator(AdditionalProperties.class)),
                new KeywordEntry("allOf", new AllOfValidator(List.of(
                    Schema0.class
                )))
            )));
        }
    
        public static AdditionalpropertiesShouldNotLookInApplicators1 getInstance() {
            if (instance == null) {
                instance = new AdditionalpropertiesShouldNotLookInApplicators1();
            }
            return instance;
        }
        @Override
        public Void castToAllowedTypes(Void arg, List<Object> pathToItem, Set<List<Object>> pathSet) {
            return castToAllowedVoidTypes(arg, pathToItem, pathSet);
        }
        
        @Override
        public Void getNewInstance(Void arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) {
            return arg;
        }
        
        @Override
        public Void validate(Void arg, SchemaConfiguration configuration) throws ValidationException, InvalidTypeException {
            Set<List<Object>> pathSet = new HashSet<>();
            List<Object> pathToItem = new ArrayList<>();
            pathToItem.add("args[0]");
            Void castArg = castToAllowedTypes(arg, pathToItem, pathSet);
            SchemaConfiguration usedConfiguration = Objects.requireNonNullElseGet(configuration, () -> new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone()));
            PathToSchemasMap validatedPathToSchemas = new PathToSchemasMap();
            ValidationMetadata validationMetadata = new ValidationMetadata(pathToItem, usedConfiguration, validatedPathToSchemas, new LinkedHashSet<>());
            PathToSchemasMap pathToSchemasMap = getPathToSchemas(this, castArg, validationMetadata, pathSet);
            return getNewInstance(castArg, validationMetadata.pathToItem(), pathToSchemasMap);
        }
        
        @Override
        public boolean castToAllowedTypes(boolean arg, List<Object> pathToItem, Set<List<Object>> pathSet) {
            return castToAllowedBooleanTypes(arg, pathToItem, pathSet);
        }
        
        @Override
        public boolean getNewInstance(boolean arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) {
            return arg;
        }
        
        @Override
        public boolean validate(boolean arg, SchemaConfiguration configuration) throws ValidationException, InvalidTypeException {
            Set<List<Object>> pathSet = new HashSet<>();
            List<Object> pathToItem = new ArrayList<>();
            pathToItem.add("args[0]");
            boolean castArg = castToAllowedTypes(arg, pathToItem, pathSet);
            SchemaConfiguration usedConfiguration = Objects.requireNonNullElseGet(configuration, () -> new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone()));
            PathToSchemasMap validatedPathToSchemas = new PathToSchemasMap();
            ValidationMetadata validationMetadata = new ValidationMetadata(pathToItem, usedConfiguration, validatedPathToSchemas, new LinkedHashSet<>());
            PathToSchemasMap pathToSchemasMap = getPathToSchemas(this, castArg, validationMetadata, pathSet);
            return getNewInstance(castArg, validationMetadata.pathToItem(), pathToSchemasMap);
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
        public Number validate(Number arg, SchemaConfiguration configuration) throws ValidationException, InvalidTypeException {
            Set<List<Object>> pathSet = new HashSet<>();
            List<Object> pathToItem = new ArrayList<>();
            pathToItem.add("args[0]");
            Number castArg = castToAllowedTypes(arg, pathToItem, pathSet);
            SchemaConfiguration usedConfiguration = Objects.requireNonNullElseGet(configuration, () -> new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone()));
            PathToSchemasMap validatedPathToSchemas = new PathToSchemasMap();
            ValidationMetadata validationMetadata = new ValidationMetadata(pathToItem, usedConfiguration, validatedPathToSchemas, new LinkedHashSet<>());
            PathToSchemasMap pathToSchemasMap = getPathToSchemas(this, castArg, validationMetadata, pathSet);
            return getNewInstance(castArg, validationMetadata.pathToItem(), pathToSchemasMap);
        }
        
        public int validate(int arg, SchemaConfiguration configuration) {
            return (int) validate((Number) arg, configuration);
        }
        
        public long validate(long arg, SchemaConfiguration configuration) {
            return (long) validate((Number) arg, configuration);
        }
        
        public float validate(float arg, SchemaConfiguration configuration) {
            return (float) validate((Number) arg, configuration);
        }
        
        public double validate(double arg, SchemaConfiguration configuration) {
            return (double) validate((Number) arg, configuration);
        }
        
        @Override
        public String castToAllowedTypes(String arg, List<Object> pathToItem, Set<List<Object>> pathSet) {
            return castToAllowedStringTypes(arg, pathToItem, pathSet);
        }
        
        @Override
        public String getNewInstance(String arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) {
            return arg;
        }
        
        @Override
        public String validate(String arg, SchemaConfiguration configuration) throws ValidationException, InvalidTypeException {
            Set<List<Object>> pathSet = new HashSet<>();
            List<Object> pathToItem = new ArrayList<>();
            pathToItem.add("args[0]");
            String castArg = castToAllowedTypes(arg, pathToItem, pathSet);
            SchemaConfiguration usedConfiguration = Objects.requireNonNullElseGet(configuration, () -> new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone()));
            PathToSchemasMap validatedPathToSchemas = new PathToSchemasMap();
            ValidationMetadata validationMetadata = new ValidationMetadata(pathToItem, usedConfiguration, validatedPathToSchemas, new LinkedHashSet<>());
            PathToSchemasMap pathToSchemasMap = getPathToSchemas(this, castArg, validationMetadata, pathSet);
            return getNewInstance(castArg, validationMetadata.pathToItem(), pathToSchemasMap);
        }
        
        public String validate(LocalDate arg, SchemaConfiguration configuration) throws ValidationException {
            return validate(arg.toString(), configuration);
        }
        
        public String validate(ZonedDateTime arg, SchemaConfiguration configuration) throws ValidationException {
            return validate(arg.toString(), configuration);
        }
        
        public String validate(UUID arg, SchemaConfiguration configuration) throws ValidationException {
            return validate(arg.toString(), configuration);
        }
        
        @Override
        public FrozenList<Object> castToAllowedTypes(List<Object> arg, List<Object> pathToItem, Set<List<Object>> pathSet) {
            return castToAllowedListTypes(arg, pathToItem, pathSet);
        }
        
        @Override
        public FrozenList<Object> getNewInstance(FrozenList<Object> arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) {
            return arg;
        }
        
        @Override
        public FrozenList<Object> validate(List<Object> arg, SchemaConfiguration configuration) throws ValidationException, InvalidTypeException {
            Set<List<Object>> pathSet = new HashSet<>();
            List<Object> pathToItem = new ArrayList<>();
            pathToItem.add("args[0]");
            FrozenList<Object> castArg = castToAllowedTypes(arg, pathToItem, pathSet);
            SchemaConfiguration usedConfiguration = Objects.requireNonNullElseGet(configuration, () -> new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone()));
            PathToSchemasMap validatedPathToSchemas = new PathToSchemasMap();
            ValidationMetadata validationMetadata = new ValidationMetadata(pathToItem, usedConfiguration, validatedPathToSchemas, new LinkedHashSet<>());
            PathToSchemasMap pathToSchemasMap = getPathToSchemas(this, castArg, validationMetadata, pathSet);
            return getNewInstance(castArg, validationMetadata.pathToItem(), pathToSchemasMap);
        }
        
        @Override
        public FrozenMap<Boolean> castToAllowedTypes(Map<String, Boolean> arg, List<Object> pathToItem, Set<List<Object>> pathSet) {
            pathSet.add(pathToItem);
            LinkedHashMap<String, Boolean> argFixed = new LinkedHashMap<>();
            for (Map.Entry<String, Boolean> entry: arg.entrySet()) {
                String key = entry.getKey();
                                Boolean val = entry.getValue();
                List<Object> newPathToItem = new ArrayList<>(pathToItem);
                newPathToItem.add(key);
                                Boolean fixedVal = (Boolean) castToAllowedObjectTypes(val, newPathToItem, pathSet);
                argFixed.put(key, fixedVal);
            }
            return new FrozenMap<>(argFixed);
        }
        
        @Override
        public AdditionalpropertiesShouldNotLookInApplicatorsMap getNewInstance(FrozenMap<Boolean> arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) {
            LinkedHashMap<String, Boolean> properties = new LinkedHashMap<>();
            for(Map.Entry<String, Boolean> entry: arg.entrySet()) {
                String propertyName = entry.getKey();
                List<Object> propertyPathToItem = new ArrayList<>(pathToItem);
                propertyPathToItem.add(propertyName);
                                Boolean value = entry.getValue();
                JsonSchema propertySchema = pathToSchemas.get(propertyPathToItem).entrySet().iterator().next().getKey();
                                Boolean castValue = (Boolean) propertySchema.getNewInstance(value, propertyPathToItem, pathToSchemas);
                properties.put(propertyName, castValue);
            }
            FrozenMap<Boolean> castProperties = new FrozenMap<>(properties);
            return new AdditionalpropertiesShouldNotLookInApplicatorsMap(castProperties);
        }
        
        @Override
        public AdditionalpropertiesShouldNotLookInApplicatorsMap validate(Map<String, Boolean> arg, SchemaConfiguration configuration) throws ValidationException, InvalidTypeException {
            Set<List<Object>> pathSet = new HashSet<>();
            List<Object> pathToItem = new ArrayList<>();
            pathToItem.add("args[0]");
            FrozenMap<Boolean> castArg = castToAllowedTypes(arg, pathToItem, pathSet);
            SchemaConfiguration usedConfiguration = Objects.requireNonNullElseGet(configuration, () -> new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone()));
            PathToSchemasMap validatedPathToSchemas = new PathToSchemasMap();
            ValidationMetadata validationMetadata = new ValidationMetadata(pathToItem, usedConfiguration, validatedPathToSchemas, new LinkedHashSet<>());
            PathToSchemasMap pathToSchemasMap = getPathToSchemas(this, castArg, validationMetadata, pathSet);
            return getNewInstance(castArg, validationMetadata.pathToItem(), pathToSchemasMap);
        }
        
        @Override
        public Object getNewInstance(Object arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) {
            if (arg == null) {
                return getNewInstance((Void) null, pathToItem, pathToSchemas);
            } else if (arg instanceof Boolean) {
                boolean boolArg = (Boolean) arg;
                return getNewInstance(boolArg, pathToItem, pathToSchemas);
            } else if (arg instanceof Number) {
                return getNewInstance((Number) arg, pathToItem, pathToSchemas);
            } else if (arg instanceof String) {
                return getNewInstance((String) arg, pathToItem, pathToSchemas);
            } else if (arg instanceof FrozenList) {
                @SuppressWarnings("unchecked") FrozenList<Object> castArg = (FrozenList<Object>) arg;
                return getNewInstance(castArg, pathToItem, pathToSchemas);
            } else if (arg instanceof FrozenMap) {
                @SuppressWarnings("unchecked") FrozenMap<Object> castArg = (FrozenMap<Object>) arg;
                return getNewInstance(castArg, pathToItem, pathToSchemas);
            }
            throw new InvalidTypeException("Invalid input type="+arg.getClass()+". It can't be instantiated by this schema");
        }
    }
}
