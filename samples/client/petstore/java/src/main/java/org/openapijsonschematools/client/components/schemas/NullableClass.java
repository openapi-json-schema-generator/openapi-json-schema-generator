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
import org.openapijsonschematools.client.configurations.JsonSchemaKeywordFlags;
import org.openapijsonschematools.client.configurations.SchemaConfiguration;
import org.openapijsonschematools.client.exceptions.InvalidTypeException;
import org.openapijsonschematools.client.exceptions.ValidationException;
import org.openapijsonschematools.client.schemas.MapJsonSchema;
import org.openapijsonschematools.client.schemas.validation.AdditionalPropertiesValidator;
import org.openapijsonschematools.client.schemas.validation.FrozenList;
import org.openapijsonschematools.client.schemas.validation.FrozenMap;
import org.openapijsonschematools.client.schemas.validation.JsonSchema;
import org.openapijsonschematools.client.schemas.validation.JsonSchemaInfo;
import org.openapijsonschematools.client.schemas.validation.PathToSchemasMap;
import org.openapijsonschematools.client.schemas.validation.PropertyEntry;
import org.openapijsonschematools.client.schemas.validation.SchemaBooleanValidator;
import org.openapijsonschematools.client.schemas.validation.SchemaListValidator;
import org.openapijsonschematools.client.schemas.validation.SchemaMapValidator;
import org.openapijsonschematools.client.schemas.validation.SchemaNullValidator;
import org.openapijsonschematools.client.schemas.validation.SchemaNumberValidator;
import org.openapijsonschematools.client.schemas.validation.SchemaStringValidator;
import org.openapijsonschematools.client.schemas.validation.ValidationMetadata;

public class NullableClass {
    // nest classes so all schemas and input/output classes can be public
    
    
    public static class AdditionalProperties3 extends JsonSchema implements SchemaNullValidator, SchemaMapValidator<Object, Object, FrozenMap<Object>> {
        private static AdditionalProperties3 instance;
    
        protected AdditionalProperties3() {
            super(new JsonSchemaInfo()
                .type(Set.of(
                    Void.class,
                    FrozenMap.class
                ))
            );
        }
    
        public static AdditionalProperties3 getInstance() {
            if (instance == null) {
                instance = new AdditionalProperties3();
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
        public Void validate(Void arg, SchemaConfiguration configuration) throws ValidationException {
            Set<List<Object>> pathSet = new HashSet<>();
            List<Object> pathToItem = List.of("args[0");
            Void castArg = castToAllowedTypes(arg, pathToItem, pathSet);
            SchemaConfiguration usedConfiguration = Objects.requireNonNullElseGet(configuration, () -> new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone()));
            ValidationMetadata validationMetadata = new ValidationMetadata(pathToItem, usedConfiguration, new PathToSchemasMap(), new LinkedHashSet<>());
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
        public FrozenMap<Object> getNewInstance(FrozenMap<Object> arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) {
            return arg;
        }
        
        @Override
        public FrozenMap<Object> validate(Map<String, Object> arg, SchemaConfiguration configuration) throws ValidationException, InvalidTypeException {
            Set<List<Object>> pathSet = new HashSet<>();
            List<Object> pathToItem = List.of("args[0");
            FrozenMap<Object> castArg = castToAllowedTypes(arg, pathToItem, pathSet);
            SchemaConfiguration usedConfiguration = Objects.requireNonNullElseGet(configuration, () -> new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone()));
            ValidationMetadata validationMetadata = new ValidationMetadata(pathToItem, usedConfiguration, new PathToSchemasMap(), new LinkedHashSet<>());
            PathToSchemasMap pathToSchemasMap = getPathToSchemas(this, castArg, validationMetadata, pathSet);
            return getNewInstance(castArg, validationMetadata.pathToItem(), pathToSchemasMap);
        }
        
        
        @Override
        public Object getNewInstance(Object arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) {
            if (arg == null) {
                return getNewInstance((Void) null, pathToItem, pathToSchemas);
            } else if (arg instanceof FrozenMap) {
                @SuppressWarnings("unchecked") FrozenMap<Object> castArg = (FrozenMap<Object>) arg;
                return getNewInstance(castArg, pathToItem, pathToSchemas);
            }
            throw new InvalidTypeException("Invalid input type="+arg.getClass()+". It can't be instantiated by this schema");
        }
    }    
    
    public static class IntegerProp extends JsonSchema implements SchemaNullValidator, SchemaNumberValidator {
        private static IntegerProp instance;
    
        protected IntegerProp() {
            super(new JsonSchemaInfo()
                .type(Set.of(
                    Void.class,
                    Integer.class,
                    Long.class,
                    Float.class,
                    Double.class
                ))
            );
        }
    
        public static IntegerProp getInstance() {
            if (instance == null) {
                instance = new IntegerProp();
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
        public Void validate(Void arg, SchemaConfiguration configuration) throws ValidationException {
            Set<List<Object>> pathSet = new HashSet<>();
            List<Object> pathToItem = List.of("args[0");
            Void castArg = castToAllowedTypes(arg, pathToItem, pathSet);
            SchemaConfiguration usedConfiguration = Objects.requireNonNullElseGet(configuration, () -> new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone()));
            ValidationMetadata validationMetadata = new ValidationMetadata(pathToItem, usedConfiguration, new PathToSchemasMap(), new LinkedHashSet<>());
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
        
        public float validate(float arg, SchemaConfiguration configuration) throws ValidationException {
            return (float) validate((Number) arg, configuration);
        }
        
        public long validate(long arg, SchemaConfiguration configuration) throws ValidationException {
            return (long) validate((Number) arg, configuration);
        }
        
        public double validate(double arg, SchemaConfiguration configuration) throws ValidationException {
            return (double) validate((Number) arg, configuration);
        }
        
        @Override
        public Object getNewInstance(Object arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) {
            if (arg == null) {
                return getNewInstance((Void) null, pathToItem, pathToSchemas);
            } else if (arg instanceof Number) {
                return getNewInstance((Number) arg, pathToItem, pathToSchemas);
            }
            throw new InvalidTypeException("Invalid input type="+arg.getClass()+". It can't be instantiated by this schema");
        }
    }    
    
    public static class NumberProp extends JsonSchema implements SchemaNullValidator, SchemaNumberValidator {
        private static NumberProp instance;
    
        protected NumberProp() {
            super(new JsonSchemaInfo()
                .type(Set.of(
                    Void.class,
                    Integer.class,
                    Long.class,
                    Float.class,
                    Double.class
                ))
            );
        }
    
        public static NumberProp getInstance() {
            if (instance == null) {
                instance = new NumberProp();
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
        public Void validate(Void arg, SchemaConfiguration configuration) throws ValidationException {
            Set<List<Object>> pathSet = new HashSet<>();
            List<Object> pathToItem = List.of("args[0");
            Void castArg = castToAllowedTypes(arg, pathToItem, pathSet);
            SchemaConfiguration usedConfiguration = Objects.requireNonNullElseGet(configuration, () -> new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone()));
            ValidationMetadata validationMetadata = new ValidationMetadata(pathToItem, usedConfiguration, new PathToSchemasMap(), new LinkedHashSet<>());
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
        
        @Override
        public Object getNewInstance(Object arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) {
            if (arg == null) {
                return getNewInstance((Void) null, pathToItem, pathToSchemas);
            } else if (arg instanceof Number) {
                return getNewInstance((Number) arg, pathToItem, pathToSchemas);
            }
            throw new InvalidTypeException("Invalid input type="+arg.getClass()+". It can't be instantiated by this schema");
        }
    }    
    
    public static class BooleanProp extends JsonSchema implements SchemaNullValidator, SchemaBooleanValidator {
        private static BooleanProp instance;
    
        protected BooleanProp() {
            super(new JsonSchemaInfo()
                .type(Set.of(
                    Void.class,
                    Boolean.class
                ))
            );
        }
    
        public static BooleanProp getInstance() {
            if (instance == null) {
                instance = new BooleanProp();
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
        public Void validate(Void arg, SchemaConfiguration configuration) throws ValidationException {
            Set<List<Object>> pathSet = new HashSet<>();
            List<Object> pathToItem = List.of("args[0");
            Void castArg = castToAllowedTypes(arg, pathToItem, pathSet);
            SchemaConfiguration usedConfiguration = Objects.requireNonNullElseGet(configuration, () -> new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone()));
            ValidationMetadata validationMetadata = new ValidationMetadata(pathToItem, usedConfiguration, new PathToSchemasMap(), new LinkedHashSet<>());
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
        public boolean validate(boolean arg, SchemaConfiguration configuration) throws ValidationException {
            Set<List<Object>> pathSet = new HashSet<>();
            List<Object> pathToItem = List.of("args[0");
            boolean castArg = castToAllowedTypes(arg, pathToItem, pathSet);
            SchemaConfiguration usedConfiguration = Objects.requireNonNullElseGet(configuration, () -> new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone()));
            ValidationMetadata validationMetadata = new ValidationMetadata(pathToItem, usedConfiguration, new PathToSchemasMap(), new LinkedHashSet<>());
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
            }
            throw new InvalidTypeException("Invalid input type="+arg.getClass()+". It can't be instantiated by this schema");
        }
    }    
    
    public static class StringProp extends JsonSchema implements SchemaNullValidator, SchemaStringValidator {
        private static StringProp instance;
    
        protected StringProp() {
            super(new JsonSchemaInfo()
                .type(Set.of(
                    Void.class,
                    String.class
                ))
            );
        }
    
        public static StringProp getInstance() {
            if (instance == null) {
                instance = new StringProp();
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
        public Void validate(Void arg, SchemaConfiguration configuration) throws ValidationException {
            Set<List<Object>> pathSet = new HashSet<>();
            List<Object> pathToItem = List.of("args[0");
            Void castArg = castToAllowedTypes(arg, pathToItem, pathSet);
            SchemaConfiguration usedConfiguration = Objects.requireNonNullElseGet(configuration, () -> new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone()));
            ValidationMetadata validationMetadata = new ValidationMetadata(pathToItem, usedConfiguration, new PathToSchemasMap(), new LinkedHashSet<>());
            PathToSchemasMap pathToSchemasMap = getPathToSchemas(this, castArg, validationMetadata, pathSet);
            return getNewInstance(castArg, validationMetadata.pathToItem(), pathToSchemasMap);
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
        public String validate(String arg, SchemaConfiguration configuration) throws ValidationException {
            Set<List<Object>> pathSet = new HashSet<>();
            List<Object> pathToItem = List.of("args[0");
            String castArg = castToAllowedTypes(arg, pathToItem, pathSet);
            SchemaConfiguration usedConfiguration = Objects.requireNonNullElseGet(configuration, () -> new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone()));
            ValidationMetadata validationMetadata = new ValidationMetadata(pathToItem, usedConfiguration, new PathToSchemasMap(), new LinkedHashSet<>());
            PathToSchemasMap pathToSchemasMap = getPathToSchemas(this, castArg, validationMetadata, pathSet);
            return getNewInstance(castArg, validationMetadata.pathToItem(), pathToSchemasMap);
        }
        
        @Override
        public Object getNewInstance(Object arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) {
            if (arg == null) {
                return getNewInstance((Void) null, pathToItem, pathToSchemas);
            } else if (arg instanceof String) {
                return getNewInstance((String) arg, pathToItem, pathToSchemas);
            }
            throw new InvalidTypeException("Invalid input type="+arg.getClass()+". It can't be instantiated by this schema");
        }
    }    
    
    public static class DateProp extends JsonSchema implements SchemaNullValidator, SchemaStringValidator {
        private static DateProp instance;
    
        protected DateProp() {
            super(new JsonSchemaInfo()
                .type(Set.of(
                    Void.class,
                    String.class
                ))
                .format("date")
            );
        }
    
        public static DateProp getInstance() {
            if (instance == null) {
                instance = new DateProp();
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
        public Void validate(Void arg, SchemaConfiguration configuration) throws ValidationException {
            Set<List<Object>> pathSet = new HashSet<>();
            List<Object> pathToItem = List.of("args[0");
            Void castArg = castToAllowedTypes(arg, pathToItem, pathSet);
            SchemaConfiguration usedConfiguration = Objects.requireNonNullElseGet(configuration, () -> new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone()));
            ValidationMetadata validationMetadata = new ValidationMetadata(pathToItem, usedConfiguration, new PathToSchemasMap(), new LinkedHashSet<>());
            PathToSchemasMap pathToSchemasMap = getPathToSchemas(this, castArg, validationMetadata, pathSet);
            return getNewInstance(castArg, validationMetadata.pathToItem(), pathToSchemasMap);
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
        public String validate(String arg, SchemaConfiguration configuration) throws ValidationException {
            Set<List<Object>> pathSet = new HashSet<>();
            List<Object> pathToItem = List.of("args[0");
            String castArg = castToAllowedTypes(arg, pathToItem, pathSet);
            SchemaConfiguration usedConfiguration = Objects.requireNonNullElseGet(configuration, () -> new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone()));
            ValidationMetadata validationMetadata = new ValidationMetadata(pathToItem, usedConfiguration, new PathToSchemasMap(), new LinkedHashSet<>());
            PathToSchemasMap pathToSchemasMap = getPathToSchemas(this, castArg, validationMetadata, pathSet);
            return getNewInstance(castArg, validationMetadata.pathToItem(), pathToSchemasMap);
        }
        
        @Override
        public Object getNewInstance(Object arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) {
            if (arg == null) {
                return getNewInstance((Void) null, pathToItem, pathToSchemas);
            } else if (arg instanceof String) {
                return getNewInstance((String) arg, pathToItem, pathToSchemas);
            }
            throw new InvalidTypeException("Invalid input type="+arg.getClass()+". It can't be instantiated by this schema");
        }
    }    
    
    public static class DatetimeProp extends JsonSchema implements SchemaNullValidator, SchemaStringValidator {
        private static DatetimeProp instance;
    
        protected DatetimeProp() {
            super(new JsonSchemaInfo()
                .type(Set.of(
                    Void.class,
                    String.class
                ))
                .format("date-time")
            );
        }
    
        public static DatetimeProp getInstance() {
            if (instance == null) {
                instance = new DatetimeProp();
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
        public Void validate(Void arg, SchemaConfiguration configuration) throws ValidationException {
            Set<List<Object>> pathSet = new HashSet<>();
            List<Object> pathToItem = List.of("args[0");
            Void castArg = castToAllowedTypes(arg, pathToItem, pathSet);
            SchemaConfiguration usedConfiguration = Objects.requireNonNullElseGet(configuration, () -> new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone()));
            ValidationMetadata validationMetadata = new ValidationMetadata(pathToItem, usedConfiguration, new PathToSchemasMap(), new LinkedHashSet<>());
            PathToSchemasMap pathToSchemasMap = getPathToSchemas(this, castArg, validationMetadata, pathSet);
            return getNewInstance(castArg, validationMetadata.pathToItem(), pathToSchemasMap);
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
        public String validate(String arg, SchemaConfiguration configuration) throws ValidationException {
            Set<List<Object>> pathSet = new HashSet<>();
            List<Object> pathToItem = List.of("args[0");
            String castArg = castToAllowedTypes(arg, pathToItem, pathSet);
            SchemaConfiguration usedConfiguration = Objects.requireNonNullElseGet(configuration, () -> new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone()));
            ValidationMetadata validationMetadata = new ValidationMetadata(pathToItem, usedConfiguration, new PathToSchemasMap(), new LinkedHashSet<>());
            PathToSchemasMap pathToSchemasMap = getPathToSchemas(this, castArg, validationMetadata, pathSet);
            return getNewInstance(castArg, validationMetadata.pathToItem(), pathToSchemasMap);
        }
        
        @Override
        public Object getNewInstance(Object arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) {
            if (arg == null) {
                return getNewInstance((Void) null, pathToItem, pathToSchemas);
            } else if (arg instanceof String) {
                return getNewInstance((String) arg, pathToItem, pathToSchemas);
            }
            throw new InvalidTypeException("Invalid input type="+arg.getClass()+". It can't be instantiated by this schema");
        }
    }    
    
    public static class Items extends MapJsonSchema {}
    
    
    public static class ArrayNullablePropList extends FrozenList<FrozenMap<Object>> {
        ArrayNullablePropList(FrozenList<FrozenMap<Object>> m) {
            super(m);
        }
        public static ArrayNullablePropList of(List<Map<String, Object>> arg, SchemaConfiguration configuration) throws ValidationException {
            return ArrayNullableProp.getInstance().validate(arg, configuration);
        }
    }
    
    public static class ArrayNullablePropListInput {
        // class to build List<Map<String, Object>>
    }
    
    
    public static class ArrayNullableProp extends JsonSchema implements SchemaNullValidator, SchemaListValidator<Map<String, Object>, FrozenMap<Object>, ArrayNullablePropList> {
        private static ArrayNullableProp instance;
    
        protected ArrayNullableProp() {
            super(new JsonSchemaInfo()
                .type(Set.of(
                    Void.class,
                    FrozenList.class
                ))
                .items(Items.class)
            );
        }
    
        public static ArrayNullableProp getInstance() {
            if (instance == null) {
                instance = new ArrayNullableProp();
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
        public Void validate(Void arg, SchemaConfiguration configuration) throws ValidationException {
            Set<List<Object>> pathSet = new HashSet<>();
            List<Object> pathToItem = List.of("args[0");
            Void castArg = castToAllowedTypes(arg, pathToItem, pathSet);
            SchemaConfiguration usedConfiguration = Objects.requireNonNullElseGet(configuration, () -> new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone()));
            ValidationMetadata validationMetadata = new ValidationMetadata(pathToItem, usedConfiguration, new PathToSchemasMap(), new LinkedHashSet<>());
            PathToSchemasMap pathToSchemasMap = getPathToSchemas(this, castArg, validationMetadata, pathSet);
            return getNewInstance(castArg, validationMetadata.pathToItem(), pathToSchemasMap);
        }
        
        @Override
        public FrozenList<FrozenMap<Object>> castToAllowedTypes(List<Map<String, Object>> arg, List<Object> pathToItem, Set<List<Object>> pathSet) {
            pathSet.add(pathToItem);
            List<FrozenMap<Object>> argFixed = new ArrayList<>();
            int i =0;
            for (Map<String, Object> item: arg) {
                List<Object> newPathToItem = new ArrayList<>(pathToItem);
                newPathToItem.add(i);
                                FrozenMap<Object> fixedVal = (FrozenMap<Object>) castToAllowedObjectTypes(item, newPathToItem, pathSet);
                argFixed.add(fixedVal);
                i += 1;
            }
            return new FrozenList<>(argFixed);
        }
        
        @Override
        public ArrayNullablePropList getNewInstance(FrozenList<FrozenMap<Object>> arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) {
            ArrayList<FrozenMap<Object>> items = new ArrayList<>();
            int i = 0;
            for (FrozenMap<Object> item: arg) {
                List<Object> itemPathToItem = new ArrayList<>(pathToItem);
                itemPathToItem.add(i);
                JsonSchema itemSchema = pathToSchemas.get(itemPathToItem).entrySet().iterator().next().getKey();
                                FrozenMap<Object> castItem = (FrozenMap<Object>) itemSchema.getNewInstance(item, itemPathToItem, pathToSchemas);
                items.add(castItem);
                i += 1;
            }
            FrozenList<FrozenMap<Object>> newInstanceItems = new FrozenList<>(items);
            return new ArrayNullablePropList(newInstanceItems);
        }
        
        @Override
        public ArrayNullablePropList validate(List<Map<String, Object>> arg, SchemaConfiguration configuration) throws ValidationException {
            Set<List<Object>> pathSet = new HashSet<>();
            List<Object> pathToItem = List.of("args[0");
            FrozenList<FrozenMap<Object>> castArg = castToAllowedTypes(arg, pathToItem, pathSet);
            SchemaConfiguration usedConfiguration = Objects.requireNonNullElseGet(configuration, () -> new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone()));
            ValidationMetadata validationMetadata = new ValidationMetadata(pathToItem, usedConfiguration, new PathToSchemasMap(), new LinkedHashSet<>());
            PathToSchemasMap pathToSchemasMap = getPathToSchemas(this, castArg, validationMetadata, pathSet);
            return getNewInstance(castArg, validationMetadata.pathToItem(), pathToSchemasMap);
        }
        
        @Override
        public Object getNewInstance(Object arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) {
            if (arg == null) {
                return getNewInstance((Void) null, pathToItem, pathToSchemas);
            } else if (arg instanceof FrozenList) {
                @SuppressWarnings("unchecked") FrozenList<FrozenMap<Object>> castArg = (FrozenList<FrozenMap<Object>>) arg;
                return getNewInstance(castArg, pathToItem, pathToSchemas);
            }
            throw new InvalidTypeException("Invalid input type="+arg.getClass()+". It can't be instantiated by this schema");
        }
    }    
    
    public static class Items1 extends JsonSchema implements SchemaNullValidator, SchemaMapValidator<Object, Object, FrozenMap<Object>> {
        private static Items1 instance;
    
        protected Items1() {
            super(new JsonSchemaInfo()
                .type(Set.of(
                    Void.class,
                    FrozenMap.class
                ))
            );
        }
    
        public static Items1 getInstance() {
            if (instance == null) {
                instance = new Items1();
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
        public Void validate(Void arg, SchemaConfiguration configuration) throws ValidationException {
            Set<List<Object>> pathSet = new HashSet<>();
            List<Object> pathToItem = List.of("args[0");
            Void castArg = castToAllowedTypes(arg, pathToItem, pathSet);
            SchemaConfiguration usedConfiguration = Objects.requireNonNullElseGet(configuration, () -> new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone()));
            ValidationMetadata validationMetadata = new ValidationMetadata(pathToItem, usedConfiguration, new PathToSchemasMap(), new LinkedHashSet<>());
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
        public FrozenMap<Object> getNewInstance(FrozenMap<Object> arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) {
            return arg;
        }
        
        @Override
        public FrozenMap<Object> validate(Map<String, Object> arg, SchemaConfiguration configuration) throws ValidationException, InvalidTypeException {
            Set<List<Object>> pathSet = new HashSet<>();
            List<Object> pathToItem = List.of("args[0");
            FrozenMap<Object> castArg = castToAllowedTypes(arg, pathToItem, pathSet);
            SchemaConfiguration usedConfiguration = Objects.requireNonNullElseGet(configuration, () -> new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone()));
            ValidationMetadata validationMetadata = new ValidationMetadata(pathToItem, usedConfiguration, new PathToSchemasMap(), new LinkedHashSet<>());
            PathToSchemasMap pathToSchemasMap = getPathToSchemas(this, castArg, validationMetadata, pathSet);
            return getNewInstance(castArg, validationMetadata.pathToItem(), pathToSchemasMap);
        }
        
        
        @Override
        public Object getNewInstance(Object arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) {
            if (arg == null) {
                return getNewInstance((Void) null, pathToItem, pathToSchemas);
            } else if (arg instanceof FrozenMap) {
                @SuppressWarnings("unchecked") FrozenMap<Object> castArg = (FrozenMap<Object>) arg;
                return getNewInstance(castArg, pathToItem, pathToSchemas);
            }
            throw new InvalidTypeException("Invalid input type="+arg.getClass()+". It can't be instantiated by this schema");
        }
    }    
    
    public static class ArrayAndItemsNullablePropList extends FrozenList<FrozenMap<Object>> {
        ArrayAndItemsNullablePropList(FrozenList<FrozenMap<Object>> m) {
            super(m);
        }
        public static ArrayAndItemsNullablePropList of(List<Map<String, Object>> arg, SchemaConfiguration configuration) throws ValidationException {
            return ArrayAndItemsNullableProp.getInstance().validate(arg, configuration);
        }
    }
    
    public static class ArrayAndItemsNullablePropListInput {
        // class to build List<Map<String, Object>>
    }
    
    
    public static class ArrayAndItemsNullableProp extends JsonSchema implements SchemaNullValidator, SchemaListValidator<Map<String, Object>, FrozenMap<Object>, ArrayAndItemsNullablePropList> {
        private static ArrayAndItemsNullableProp instance;
    
        protected ArrayAndItemsNullableProp() {
            super(new JsonSchemaInfo()
                .type(Set.of(
                    Void.class,
                    FrozenList.class
                ))
                .items(Items1.class)
            );
        }
    
        public static ArrayAndItemsNullableProp getInstance() {
            if (instance == null) {
                instance = new ArrayAndItemsNullableProp();
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
        public Void validate(Void arg, SchemaConfiguration configuration) throws ValidationException {
            Set<List<Object>> pathSet = new HashSet<>();
            List<Object> pathToItem = List.of("args[0");
            Void castArg = castToAllowedTypes(arg, pathToItem, pathSet);
            SchemaConfiguration usedConfiguration = Objects.requireNonNullElseGet(configuration, () -> new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone()));
            ValidationMetadata validationMetadata = new ValidationMetadata(pathToItem, usedConfiguration, new PathToSchemasMap(), new LinkedHashSet<>());
            PathToSchemasMap pathToSchemasMap = getPathToSchemas(this, castArg, validationMetadata, pathSet);
            return getNewInstance(castArg, validationMetadata.pathToItem(), pathToSchemasMap);
        }
        
        @Override
        public FrozenList<FrozenMap<Object>> castToAllowedTypes(List<Map<String, Object>> arg, List<Object> pathToItem, Set<List<Object>> pathSet) {
            pathSet.add(pathToItem);
            List<FrozenMap<Object>> argFixed = new ArrayList<>();
            int i =0;
            for (Map<String, Object> item: arg) {
                List<Object> newPathToItem = new ArrayList<>(pathToItem);
                newPathToItem.add(i);
                                FrozenMap<Object> fixedVal = (FrozenMap<Object>) castToAllowedObjectTypes(item, newPathToItem, pathSet);
                argFixed.add(fixedVal);
                i += 1;
            }
            return new FrozenList<>(argFixed);
        }
        
        @Override
        public ArrayAndItemsNullablePropList getNewInstance(FrozenList<FrozenMap<Object>> arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) {
            ArrayList<FrozenMap<Object>> items = new ArrayList<>();
            int i = 0;
            for (FrozenMap<Object> item: arg) {
                List<Object> itemPathToItem = new ArrayList<>(pathToItem);
                itemPathToItem.add(i);
                JsonSchema itemSchema = pathToSchemas.get(itemPathToItem).entrySet().iterator().next().getKey();
                                FrozenMap<Object> castItem = (FrozenMap<Object>) itemSchema.getNewInstance(item, itemPathToItem, pathToSchemas);
                items.add(castItem);
                i += 1;
            }
            FrozenList<FrozenMap<Object>> newInstanceItems = new FrozenList<>(items);
            return new ArrayAndItemsNullablePropList(newInstanceItems);
        }
        
        @Override
        public ArrayAndItemsNullablePropList validate(List<Map<String, Object>> arg, SchemaConfiguration configuration) throws ValidationException {
            Set<List<Object>> pathSet = new HashSet<>();
            List<Object> pathToItem = List.of("args[0");
            FrozenList<FrozenMap<Object>> castArg = castToAllowedTypes(arg, pathToItem, pathSet);
            SchemaConfiguration usedConfiguration = Objects.requireNonNullElseGet(configuration, () -> new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone()));
            ValidationMetadata validationMetadata = new ValidationMetadata(pathToItem, usedConfiguration, new PathToSchemasMap(), new LinkedHashSet<>());
            PathToSchemasMap pathToSchemasMap = getPathToSchemas(this, castArg, validationMetadata, pathSet);
            return getNewInstance(castArg, validationMetadata.pathToItem(), pathToSchemasMap);
        }
        
        @Override
        public Object getNewInstance(Object arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) {
            if (arg == null) {
                return getNewInstance((Void) null, pathToItem, pathToSchemas);
            } else if (arg instanceof FrozenList) {
                @SuppressWarnings("unchecked") FrozenList<FrozenMap<Object>> castArg = (FrozenList<FrozenMap<Object>>) arg;
                return getNewInstance(castArg, pathToItem, pathToSchemas);
            }
            throw new InvalidTypeException("Invalid input type="+arg.getClass()+". It can't be instantiated by this schema");
        }
    }    
    
    public static class Items2 extends JsonSchema implements SchemaNullValidator, SchemaMapValidator<Object, Object, FrozenMap<Object>> {
        private static Items2 instance;
    
        protected Items2() {
            super(new JsonSchemaInfo()
                .type(Set.of(
                    Void.class,
                    FrozenMap.class
                ))
            );
        }
    
        public static Items2 getInstance() {
            if (instance == null) {
                instance = new Items2();
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
        public Void validate(Void arg, SchemaConfiguration configuration) throws ValidationException {
            Set<List<Object>> pathSet = new HashSet<>();
            List<Object> pathToItem = List.of("args[0");
            Void castArg = castToAllowedTypes(arg, pathToItem, pathSet);
            SchemaConfiguration usedConfiguration = Objects.requireNonNullElseGet(configuration, () -> new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone()));
            ValidationMetadata validationMetadata = new ValidationMetadata(pathToItem, usedConfiguration, new PathToSchemasMap(), new LinkedHashSet<>());
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
        public FrozenMap<Object> getNewInstance(FrozenMap<Object> arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) {
            return arg;
        }
        
        @Override
        public FrozenMap<Object> validate(Map<String, Object> arg, SchemaConfiguration configuration) throws ValidationException, InvalidTypeException {
            Set<List<Object>> pathSet = new HashSet<>();
            List<Object> pathToItem = List.of("args[0");
            FrozenMap<Object> castArg = castToAllowedTypes(arg, pathToItem, pathSet);
            SchemaConfiguration usedConfiguration = Objects.requireNonNullElseGet(configuration, () -> new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone()));
            ValidationMetadata validationMetadata = new ValidationMetadata(pathToItem, usedConfiguration, new PathToSchemasMap(), new LinkedHashSet<>());
            PathToSchemasMap pathToSchemasMap = getPathToSchemas(this, castArg, validationMetadata, pathSet);
            return getNewInstance(castArg, validationMetadata.pathToItem(), pathToSchemasMap);
        }
        
        
        @Override
        public Object getNewInstance(Object arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) {
            if (arg == null) {
                return getNewInstance((Void) null, pathToItem, pathToSchemas);
            } else if (arg instanceof FrozenMap) {
                @SuppressWarnings("unchecked") FrozenMap<Object> castArg = (FrozenMap<Object>) arg;
                return getNewInstance(castArg, pathToItem, pathToSchemas);
            }
            throw new InvalidTypeException("Invalid input type="+arg.getClass()+". It can't be instantiated by this schema");
        }
    }    
    
    public static class ArrayItemsNullableList extends FrozenList<FrozenMap<Object>> {
        ArrayItemsNullableList(FrozenList<FrozenMap<Object>> m) {
            super(m);
        }
        public static ArrayItemsNullableList of(List<Map<String, Object>> arg, SchemaConfiguration configuration) throws ValidationException {
            return ArrayItemsNullable.getInstance().validate(arg, configuration);
        }
    }
    
    public static class ArrayItemsNullableListInput {
        // class to build List<Map<String, Object>>
    }
    
    
    public static class ArrayItemsNullable extends JsonSchema implements SchemaListValidator<Map<String, Object>, FrozenMap<Object>, ArrayItemsNullableList> {
        private static ArrayItemsNullable instance;
    
        protected ArrayItemsNullable() {
            super(new JsonSchemaInfo()
                .type(Set.of(FrozenList.class))
                .items(Items2.class)
            );
        }
    
        public static ArrayItemsNullable getInstance() {
            if (instance == null) {
                instance = new ArrayItemsNullable();
            }
            return instance;
        }
        
        @Override
        public FrozenList<FrozenMap<Object>> castToAllowedTypes(List<Map<String, Object>> arg, List<Object> pathToItem, Set<List<Object>> pathSet) {
            pathSet.add(pathToItem);
            List<FrozenMap<Object>> argFixed = new ArrayList<>();
            int i =0;
            for (Map<String, Object> item: arg) {
                List<Object> newPathToItem = new ArrayList<>(pathToItem);
                newPathToItem.add(i);
                                FrozenMap<Object> fixedVal = (FrozenMap<Object>) castToAllowedObjectTypes(item, newPathToItem, pathSet);
                argFixed.add(fixedVal);
                i += 1;
            }
            return new FrozenList<>(argFixed);
        }
        
        @Override
        public ArrayItemsNullableList getNewInstance(FrozenList<FrozenMap<Object>> arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) {
            ArrayList<FrozenMap<Object>> items = new ArrayList<>();
            int i = 0;
            for (FrozenMap<Object> item: arg) {
                List<Object> itemPathToItem = new ArrayList<>(pathToItem);
                itemPathToItem.add(i);
                JsonSchema itemSchema = pathToSchemas.get(itemPathToItem).entrySet().iterator().next().getKey();
                                FrozenMap<Object> castItem = (FrozenMap<Object>) itemSchema.getNewInstance(item, itemPathToItem, pathToSchemas);
                items.add(castItem);
                i += 1;
            }
            FrozenList<FrozenMap<Object>> newInstanceItems = new FrozenList<>(items);
            return new ArrayItemsNullableList(newInstanceItems);
        }
        
        @Override
        public ArrayItemsNullableList validate(List<Map<String, Object>> arg, SchemaConfiguration configuration) throws ValidationException {
            Set<List<Object>> pathSet = new HashSet<>();
            List<Object> pathToItem = List.of("args[0");
            FrozenList<FrozenMap<Object>> castArg = castToAllowedTypes(arg, pathToItem, pathSet);
            SchemaConfiguration usedConfiguration = Objects.requireNonNullElseGet(configuration, () -> new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone()));
            ValidationMetadata validationMetadata = new ValidationMetadata(pathToItem, usedConfiguration, new PathToSchemasMap(), new LinkedHashSet<>());
            PathToSchemasMap pathToSchemasMap = getPathToSchemas(this, castArg, validationMetadata, pathSet);
            return getNewInstance(castArg, validationMetadata.pathToItem(), pathToSchemasMap);
        }
        
        @Override
        public Object getNewInstance(Object arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) {
            if (arg instanceof FrozenList) {
                @SuppressWarnings("unchecked") FrozenList<FrozenMap<Object>> castArg = (FrozenList<FrozenMap<Object>>) arg;
                return getNewInstance(castArg, pathToItem, pathToSchemas);
            }
            throw new InvalidTypeException("Invalid input type="+arg.getClass()+". It can't be instantiated by this schema");
        }
    }    
    
    public static class AdditionalProperties extends MapJsonSchema {}
    
    
    public static class ObjectNullablePropMap extends FrozenMap<FrozenMap<Object>> {
        ObjectNullablePropMap(FrozenMap<FrozenMap<Object>> m) {
            super(m);
        }
        public static final Set<String> requiredKeys = Set.of();
        public static final Set<String> optionalKeys = Set.of();
        public static ObjectNullablePropMap of(Map<String, Map<String, Object>> arg, SchemaConfiguration configuration) throws ValidationException {
            return ObjectNullableProp.getInstance().validate(arg, configuration);
        }
        
        public FrozenMap<Object> getAdditionalProperty(String name) {
            throwIfKeyNotPresent(name);
            return get(name);
        }
    }
    public static class ObjectNullablePropMapInput {
        // Map<String, additionalProperties>
    }
    
    
    public static class ObjectNullableProp extends JsonSchema implements SchemaNullValidator, SchemaMapValidator<Map<String, Object>, FrozenMap<Object>, ObjectNullablePropMap> {
        private static ObjectNullableProp instance;
    
        protected ObjectNullableProp() {
            super(new JsonSchemaInfo()
                .type(Set.of(
                    Void.class,
                    FrozenMap.class
                ))
                .additionalProperties(AdditionalProperties.class)
            );
        }
    
        public static ObjectNullableProp getInstance() {
            if (instance == null) {
                instance = new ObjectNullableProp();
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
        public Void validate(Void arg, SchemaConfiguration configuration) throws ValidationException {
            Set<List<Object>> pathSet = new HashSet<>();
            List<Object> pathToItem = List.of("args[0");
            Void castArg = castToAllowedTypes(arg, pathToItem, pathSet);
            SchemaConfiguration usedConfiguration = Objects.requireNonNullElseGet(configuration, () -> new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone()));
            ValidationMetadata validationMetadata = new ValidationMetadata(pathToItem, usedConfiguration, new PathToSchemasMap(), new LinkedHashSet<>());
            PathToSchemasMap pathToSchemasMap = getPathToSchemas(this, castArg, validationMetadata, pathSet);
            return getNewInstance(castArg, validationMetadata.pathToItem(), pathToSchemasMap);
        }
        
        @Override
        public FrozenMap<FrozenMap<Object>> castToAllowedTypes(Map<String, Map<String, Object>> arg, List<Object> pathToItem, Set<List<Object>> pathSet) {
            pathSet.add(pathToItem);
            LinkedHashMap<String, FrozenMap<Object>> argFixed = new LinkedHashMap<>();
            for (Map.Entry<String, Map<String, Object>> entry: arg.entrySet()) {
                String key = entry.getKey();
                                Map<String, Object> val = entry.getValue();
                List<Object> newPathToItem = new ArrayList<>(pathToItem);
                newPathToItem.add(key);
                                FrozenMap<Object> fixedVal = (FrozenMap<Object>) castToAllowedObjectTypes(val, newPathToItem, pathSet);
                argFixed.put(key, fixedVal);
            }
            return new FrozenMap<>(argFixed);
        }
        
        public ObjectNullablePropMap getNewInstance(FrozenMap<FrozenMap<Object>> arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) {
            LinkedHashMap<String, FrozenMap<Object>> properties = new LinkedHashMap<>();
            for(Map.Entry<String, FrozenMap<Object>> entry: arg.entrySet()) {
                String propertyName = entry.getKey();
                List<Object> propertyPathToItem = new ArrayList<>(pathToItem);
                propertyPathToItem.add(propertyName);
                FrozenMap<Object> value = entry.getValue();
                JsonSchema propertySchema = pathToSchemas.get(propertyPathToItem).entrySet().iterator().next().getKey();
                FrozenMap<Object> castValue = (FrozenMap<Object>) propertySchema.getNewInstance(value, propertyPathToItem, pathToSchemas);
                properties.put(propertyName, castValue);
            }
            FrozenMap<FrozenMap<Object>> castProperties = new FrozenMap<>(properties);
            return new ObjectNullablePropMap(castProperties);
        }
        
        @Override
        public ObjectNullablePropMap validate(Map<String, Map<String, Object>> arg, SchemaConfiguration configuration) throws ValidationException, InvalidTypeException {
            Set<List<Object>> pathSet = new HashSet<>();
            List<Object> pathToItem = List.of("args[0");
            FrozenMap<FrozenMap<Object>> castArg = castToAllowedTypes(arg, pathToItem, pathSet);
            SchemaConfiguration usedConfiguration = Objects.requireNonNullElseGet(configuration, () -> new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone()));
            ValidationMetadata validationMetadata = new ValidationMetadata(pathToItem, usedConfiguration, new PathToSchemasMap(), new LinkedHashSet<>());
            PathToSchemasMap pathToSchemasMap = getPathToSchemas(this, castArg, validationMetadata, pathSet);
            return getNewInstance(castArg, validationMetadata.pathToItem(), pathToSchemasMap);
        }
        
        
        @Override
        public Object getNewInstance(Object arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) {
            if (arg == null) {
                return getNewInstance((Void) null, pathToItem, pathToSchemas);
            } else if (arg instanceof FrozenMap) {
                @SuppressWarnings("unchecked") FrozenMap<FrozenMap<Object>> castArg = (FrozenMap<FrozenMap<Object>>) arg;
                return getNewInstance(castArg, pathToItem, pathToSchemas);
            }
            throw new InvalidTypeException("Invalid input type="+arg.getClass()+". It can't be instantiated by this schema");
        }
    }    
    
    public static class AdditionalProperties1 extends JsonSchema implements SchemaNullValidator, SchemaMapValidator<Object, Object, FrozenMap<Object>> {
        private static AdditionalProperties1 instance;
    
        protected AdditionalProperties1() {
            super(new JsonSchemaInfo()
                .type(Set.of(
                    Void.class,
                    FrozenMap.class
                ))
            );
        }
    
        public static AdditionalProperties1 getInstance() {
            if (instance == null) {
                instance = new AdditionalProperties1();
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
        public Void validate(Void arg, SchemaConfiguration configuration) throws ValidationException {
            Set<List<Object>> pathSet = new HashSet<>();
            List<Object> pathToItem = List.of("args[0");
            Void castArg = castToAllowedTypes(arg, pathToItem, pathSet);
            SchemaConfiguration usedConfiguration = Objects.requireNonNullElseGet(configuration, () -> new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone()));
            ValidationMetadata validationMetadata = new ValidationMetadata(pathToItem, usedConfiguration, new PathToSchemasMap(), new LinkedHashSet<>());
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
        public FrozenMap<Object> getNewInstance(FrozenMap<Object> arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) {
            return arg;
        }
        
        @Override
        public FrozenMap<Object> validate(Map<String, Object> arg, SchemaConfiguration configuration) throws ValidationException, InvalidTypeException {
            Set<List<Object>> pathSet = new HashSet<>();
            List<Object> pathToItem = List.of("args[0");
            FrozenMap<Object> castArg = castToAllowedTypes(arg, pathToItem, pathSet);
            SchemaConfiguration usedConfiguration = Objects.requireNonNullElseGet(configuration, () -> new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone()));
            ValidationMetadata validationMetadata = new ValidationMetadata(pathToItem, usedConfiguration, new PathToSchemasMap(), new LinkedHashSet<>());
            PathToSchemasMap pathToSchemasMap = getPathToSchemas(this, castArg, validationMetadata, pathSet);
            return getNewInstance(castArg, validationMetadata.pathToItem(), pathToSchemasMap);
        }
        
        
        @Override
        public Object getNewInstance(Object arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) {
            if (arg == null) {
                return getNewInstance((Void) null, pathToItem, pathToSchemas);
            } else if (arg instanceof FrozenMap) {
                @SuppressWarnings("unchecked") FrozenMap<Object> castArg = (FrozenMap<Object>) arg;
                return getNewInstance(castArg, pathToItem, pathToSchemas);
            }
            throw new InvalidTypeException("Invalid input type="+arg.getClass()+". It can't be instantiated by this schema");
        }
    }    
    
    public static class ObjectAndItemsNullablePropMap extends FrozenMap<FrozenMap<Object>> {
        ObjectAndItemsNullablePropMap(FrozenMap<FrozenMap<Object>> m) {
            super(m);
        }
        public static final Set<String> requiredKeys = Set.of();
        public static final Set<String> optionalKeys = Set.of();
        public static ObjectAndItemsNullablePropMap of(Map<String, Map<String, Object>> arg, SchemaConfiguration configuration) throws ValidationException {
            return ObjectAndItemsNullableProp.getInstance().validate(arg, configuration);
        }
        
        public FrozenMap<Object> getAdditionalProperty(String name) {
            throwIfKeyNotPresent(name);
            return get(name);
        }
    }
    public static class ObjectAndItemsNullablePropMapInput {
        // Map<String, additionalProperties>
    }
    
    
    public static class ObjectAndItemsNullableProp extends JsonSchema implements SchemaNullValidator, SchemaMapValidator<Map<String, Object>, FrozenMap<Object>, ObjectAndItemsNullablePropMap> {
        private static ObjectAndItemsNullableProp instance;
    
        protected ObjectAndItemsNullableProp() {
            super(new JsonSchemaInfo()
                .type(Set.of(
                    Void.class,
                    FrozenMap.class
                ))
                .additionalProperties(AdditionalProperties1.class)
            );
        }
    
        public static ObjectAndItemsNullableProp getInstance() {
            if (instance == null) {
                instance = new ObjectAndItemsNullableProp();
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
        public Void validate(Void arg, SchemaConfiguration configuration) throws ValidationException {
            Set<List<Object>> pathSet = new HashSet<>();
            List<Object> pathToItem = List.of("args[0");
            Void castArg = castToAllowedTypes(arg, pathToItem, pathSet);
            SchemaConfiguration usedConfiguration = Objects.requireNonNullElseGet(configuration, () -> new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone()));
            ValidationMetadata validationMetadata = new ValidationMetadata(pathToItem, usedConfiguration, new PathToSchemasMap(), new LinkedHashSet<>());
            PathToSchemasMap pathToSchemasMap = getPathToSchemas(this, castArg, validationMetadata, pathSet);
            return getNewInstance(castArg, validationMetadata.pathToItem(), pathToSchemasMap);
        }
        
        @Override
        public FrozenMap<FrozenMap<Object>> castToAllowedTypes(Map<String, Map<String, Object>> arg, List<Object> pathToItem, Set<List<Object>> pathSet) {
            pathSet.add(pathToItem);
            LinkedHashMap<String, FrozenMap<Object>> argFixed = new LinkedHashMap<>();
            for (Map.Entry<String, Map<String, Object>> entry: arg.entrySet()) {
                String key = entry.getKey();
                                Map<String, Object> val = entry.getValue();
                List<Object> newPathToItem = new ArrayList<>(pathToItem);
                newPathToItem.add(key);
                                FrozenMap<Object> fixedVal = (FrozenMap<Object>) castToAllowedObjectTypes(val, newPathToItem, pathSet);
                argFixed.put(key, fixedVal);
            }
            return new FrozenMap<>(argFixed);
        }
        
        public ObjectAndItemsNullablePropMap getNewInstance(FrozenMap<FrozenMap<Object>> arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) {
            LinkedHashMap<String, FrozenMap<Object>> properties = new LinkedHashMap<>();
            for(Map.Entry<String, FrozenMap<Object>> entry: arg.entrySet()) {
                String propertyName = entry.getKey();
                List<Object> propertyPathToItem = new ArrayList<>(pathToItem);
                propertyPathToItem.add(propertyName);
                FrozenMap<Object> value = entry.getValue();
                JsonSchema propertySchema = pathToSchemas.get(propertyPathToItem).entrySet().iterator().next().getKey();
                FrozenMap<Object> castValue = (FrozenMap<Object>) propertySchema.getNewInstance(value, propertyPathToItem, pathToSchemas);
                properties.put(propertyName, castValue);
            }
            FrozenMap<FrozenMap<Object>> castProperties = new FrozenMap<>(properties);
            return new ObjectAndItemsNullablePropMap(castProperties);
        }
        
        @Override
        public ObjectAndItemsNullablePropMap validate(Map<String, Map<String, Object>> arg, SchemaConfiguration configuration) throws ValidationException, InvalidTypeException {
            Set<List<Object>> pathSet = new HashSet<>();
            List<Object> pathToItem = List.of("args[0");
            FrozenMap<FrozenMap<Object>> castArg = castToAllowedTypes(arg, pathToItem, pathSet);
            SchemaConfiguration usedConfiguration = Objects.requireNonNullElseGet(configuration, () -> new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone()));
            ValidationMetadata validationMetadata = new ValidationMetadata(pathToItem, usedConfiguration, new PathToSchemasMap(), new LinkedHashSet<>());
            PathToSchemasMap pathToSchemasMap = getPathToSchemas(this, castArg, validationMetadata, pathSet);
            return getNewInstance(castArg, validationMetadata.pathToItem(), pathToSchemasMap);
        }
        
        
        @Override
        public Object getNewInstance(Object arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) {
            if (arg == null) {
                return getNewInstance((Void) null, pathToItem, pathToSchemas);
            } else if (arg instanceof FrozenMap) {
                @SuppressWarnings("unchecked") FrozenMap<FrozenMap<Object>> castArg = (FrozenMap<FrozenMap<Object>>) arg;
                return getNewInstance(castArg, pathToItem, pathToSchemas);
            }
            throw new InvalidTypeException("Invalid input type="+arg.getClass()+". It can't be instantiated by this schema");
        }
    }    
    
    public static class AdditionalProperties2 extends JsonSchema implements SchemaNullValidator, SchemaMapValidator<Object, Object, FrozenMap<Object>> {
        private static AdditionalProperties2 instance;
    
        protected AdditionalProperties2() {
            super(new JsonSchemaInfo()
                .type(Set.of(
                    Void.class,
                    FrozenMap.class
                ))
            );
        }
    
        public static AdditionalProperties2 getInstance() {
            if (instance == null) {
                instance = new AdditionalProperties2();
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
        public Void validate(Void arg, SchemaConfiguration configuration) throws ValidationException {
            Set<List<Object>> pathSet = new HashSet<>();
            List<Object> pathToItem = List.of("args[0");
            Void castArg = castToAllowedTypes(arg, pathToItem, pathSet);
            SchemaConfiguration usedConfiguration = Objects.requireNonNullElseGet(configuration, () -> new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone()));
            ValidationMetadata validationMetadata = new ValidationMetadata(pathToItem, usedConfiguration, new PathToSchemasMap(), new LinkedHashSet<>());
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
        public FrozenMap<Object> getNewInstance(FrozenMap<Object> arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) {
            return arg;
        }
        
        @Override
        public FrozenMap<Object> validate(Map<String, Object> arg, SchemaConfiguration configuration) throws ValidationException, InvalidTypeException {
            Set<List<Object>> pathSet = new HashSet<>();
            List<Object> pathToItem = List.of("args[0");
            FrozenMap<Object> castArg = castToAllowedTypes(arg, pathToItem, pathSet);
            SchemaConfiguration usedConfiguration = Objects.requireNonNullElseGet(configuration, () -> new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone()));
            ValidationMetadata validationMetadata = new ValidationMetadata(pathToItem, usedConfiguration, new PathToSchemasMap(), new LinkedHashSet<>());
            PathToSchemasMap pathToSchemasMap = getPathToSchemas(this, castArg, validationMetadata, pathSet);
            return getNewInstance(castArg, validationMetadata.pathToItem(), pathToSchemasMap);
        }
        
        
        @Override
        public Object getNewInstance(Object arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) {
            if (arg == null) {
                return getNewInstance((Void) null, pathToItem, pathToSchemas);
            } else if (arg instanceof FrozenMap) {
                @SuppressWarnings("unchecked") FrozenMap<Object> castArg = (FrozenMap<Object>) arg;
                return getNewInstance(castArg, pathToItem, pathToSchemas);
            }
            throw new InvalidTypeException("Invalid input type="+arg.getClass()+". It can't be instantiated by this schema");
        }
    }    
    
    public static class ObjectItemsNullableMap extends FrozenMap<FrozenMap<Object>> {
        ObjectItemsNullableMap(FrozenMap<FrozenMap<Object>> m) {
            super(m);
        }
        public static final Set<String> requiredKeys = Set.of();
        public static final Set<String> optionalKeys = Set.of();
        public static ObjectItemsNullableMap of(Map<String, Map<String, Object>> arg, SchemaConfiguration configuration) throws ValidationException {
            return ObjectItemsNullable.getInstance().validate(arg, configuration);
        }
        
        public FrozenMap<Object> getAdditionalProperty(String name) {
            throwIfKeyNotPresent(name);
            return get(name);
        }
    }
    public static class ObjectItemsNullableMapInput {
        // Map<String, additionalProperties>
    }
    
    
    public static class ObjectItemsNullable extends JsonSchema implements SchemaMapValidator<Map<String, Object>, FrozenMap<Object>, ObjectItemsNullableMap> {
        private static ObjectItemsNullable instance;
    
        protected ObjectItemsNullable() {
            super(new JsonSchemaInfo()
                .type(Set.of(FrozenMap.class))
                .additionalProperties(AdditionalProperties2.class)
            );
        }
    
        public static ObjectItemsNullable getInstance() {
            if (instance == null) {
                instance = new ObjectItemsNullable();
            }
            return instance;
        }
        
        @Override
        public FrozenMap<FrozenMap<Object>> castToAllowedTypes(Map<String, Map<String, Object>> arg, List<Object> pathToItem, Set<List<Object>> pathSet) {
            pathSet.add(pathToItem);
            LinkedHashMap<String, FrozenMap<Object>> argFixed = new LinkedHashMap<>();
            for (Map.Entry<String, Map<String, Object>> entry: arg.entrySet()) {
                String key = entry.getKey();
                                Map<String, Object> val = entry.getValue();
                List<Object> newPathToItem = new ArrayList<>(pathToItem);
                newPathToItem.add(key);
                                FrozenMap<Object> fixedVal = (FrozenMap<Object>) castToAllowedObjectTypes(val, newPathToItem, pathSet);
                argFixed.put(key, fixedVal);
            }
            return new FrozenMap<>(argFixed);
        }
        
        public ObjectItemsNullableMap getNewInstance(FrozenMap<FrozenMap<Object>> arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) {
            LinkedHashMap<String, FrozenMap<Object>> properties = new LinkedHashMap<>();
            for(Map.Entry<String, FrozenMap<Object>> entry: arg.entrySet()) {
                String propertyName = entry.getKey();
                List<Object> propertyPathToItem = new ArrayList<>(pathToItem);
                propertyPathToItem.add(propertyName);
                FrozenMap<Object> value = entry.getValue();
                JsonSchema propertySchema = pathToSchemas.get(propertyPathToItem).entrySet().iterator().next().getKey();
                FrozenMap<Object> castValue = (FrozenMap<Object>) propertySchema.getNewInstance(value, propertyPathToItem, pathToSchemas);
                properties.put(propertyName, castValue);
            }
            FrozenMap<FrozenMap<Object>> castProperties = new FrozenMap<>(properties);
            return new ObjectItemsNullableMap(castProperties);
        }
        
        @Override
        public ObjectItemsNullableMap validate(Map<String, Map<String, Object>> arg, SchemaConfiguration configuration) throws ValidationException, InvalidTypeException {
            Set<List<Object>> pathSet = new HashSet<>();
            List<Object> pathToItem = List.of("args[0");
            FrozenMap<FrozenMap<Object>> castArg = castToAllowedTypes(arg, pathToItem, pathSet);
            SchemaConfiguration usedConfiguration = Objects.requireNonNullElseGet(configuration, () -> new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone()));
            ValidationMetadata validationMetadata = new ValidationMetadata(pathToItem, usedConfiguration, new PathToSchemasMap(), new LinkedHashSet<>());
            PathToSchemasMap pathToSchemasMap = getPathToSchemas(this, castArg, validationMetadata, pathSet);
            return getNewInstance(castArg, validationMetadata.pathToItem(), pathToSchemasMap);
        }
        
        
        @Override
        public Object getNewInstance(Object arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) {
            if (arg instanceof FrozenMap) {
                @SuppressWarnings("unchecked") FrozenMap<FrozenMap<Object>> castArg = (FrozenMap<FrozenMap<Object>>) arg;
                return getNewInstance(castArg, pathToItem, pathToSchemas);
            }
            throw new InvalidTypeException("Invalid input type="+arg.getClass()+". It can't be instantiated by this schema");
        }
    }
    
    
    public static class NullableClassMap extends FrozenMap<Object> {
        NullableClassMap(FrozenMap<Object> m) {
            super(m);
        }
        public static final Set<String> requiredKeys = Set.of();
        public static final Set<String> optionalKeys = Set.of(
            "integer_prop",
            "number_prop",
            "boolean_prop",
            "string_prop",
            "date_prop",
            "datetime_prop",
            "array_nullable_prop",
            "array_and_items_nullable_prop",
            "array_items_nullable",
            "object_nullable_prop",
            "object_and_items_nullable_prop",
            "object_items_nullable"
        );
        public static NullableClassMap of(Map<String, Object> arg, SchemaConfiguration configuration) throws ValidationException {
            return NullableClass1.getInstance().validate(arg, configuration);
        }
        
        public Long integer_prop() {
            String key = "integer_prop";
            throwIfKeyNotPresent(key);
            return (Long) get(key);
        }
        
        public Number number_prop() {
            String key = "number_prop";
            throwIfKeyNotPresent(key);
            return (Number) get(key);
        }
        
        public Boolean boolean_prop() {
            String key = "boolean_prop";
            throwIfKeyNotPresent(key);
            return (Boolean) get(key);
        }
        
        public String string_prop() {
            String key = "string_prop";
            throwIfKeyNotPresent(key);
            return (String) get(key);
        }
        
        public String date_prop() {
            String key = "date_prop";
            throwIfKeyNotPresent(key);
            return (String) get(key);
        }
        
        public String datetime_prop() {
            String key = "datetime_prop";
            throwIfKeyNotPresent(key);
            return (String) get(key);
        }
        
        public ArrayNullablePropList array_nullable_prop() {
            String key = "array_nullable_prop";
            throwIfKeyNotPresent(key);
            return (ArrayNullablePropList) get(key);
        }
        
        public ArrayAndItemsNullablePropList array_and_items_nullable_prop() {
            String key = "array_and_items_nullable_prop";
            throwIfKeyNotPresent(key);
            return (ArrayAndItemsNullablePropList) get(key);
        }
        
        public ArrayItemsNullableList array_items_nullable() {
            String key = "array_items_nullable";
            throwIfKeyNotPresent(key);
            return (ArrayItemsNullableList) get(key);
        }
        
        public ObjectNullablePropMap object_nullable_prop() {
            String key = "object_nullable_prop";
            throwIfKeyNotPresent(key);
            return (ObjectNullablePropMap) get(key);
        }
        
        public ObjectAndItemsNullablePropMap object_and_items_nullable_prop() {
            String key = "object_and_items_nullable_prop";
            throwIfKeyNotPresent(key);
            return (ObjectAndItemsNullablePropMap) get(key);
        }
        
        public ObjectItemsNullableMap object_items_nullable() {
            String key = "object_items_nullable";
            throwIfKeyNotPresent(key);
            return (ObjectItemsNullableMap) get(key);
        }
        
        public FrozenMap<Object> getAdditionalProperty(String name) {
            throwIfKeyNotPresent(name);
            return (FrozenMap<Object>) get(name);
        }
    }
    public static class NullableClassMapInput {
        // optionalProperties + additionalProperties
    }
    
    
    public static class NullableClass1 extends JsonSchema implements SchemaMapValidator<Object, Object, NullableClassMap> {
        /*
        NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
        Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
    
        Do not edit the class manually.
        */
        private static NullableClass1 instance;
    
        protected NullableClass1() {
            super(new JsonSchemaInfo()
                .type(Set.of(FrozenMap.class))
                .properties(Map.ofEntries(
                    new PropertyEntry("integer_prop", IntegerProp.class),
                    new PropertyEntry("number_prop", NumberProp.class),
                    new PropertyEntry("boolean_prop", BooleanProp.class),
                    new PropertyEntry("string_prop", StringProp.class),
                    new PropertyEntry("date_prop", DateProp.class),
                    new PropertyEntry("datetime_prop", DatetimeProp.class),
                    new PropertyEntry("array_nullable_prop", ArrayNullableProp.class),
                    new PropertyEntry("array_and_items_nullable_prop", ArrayAndItemsNullableProp.class),
                    new PropertyEntry("array_items_nullable", ArrayItemsNullable.class),
                    new PropertyEntry("object_nullable_prop", ObjectNullableProp.class),
                    new PropertyEntry("object_and_items_nullable_prop", ObjectAndItemsNullableProp.class),
                    new PropertyEntry("object_items_nullable", ObjectItemsNullable.class)
                ))
                .additionalProperties(AdditionalProperties3.class)
            );
        }
    
        public static NullableClass1 getInstance() {
            if (instance == null) {
                instance = new NullableClass1();
            }
            return instance;
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
        
        public NullableClassMap getNewInstance(FrozenMap<Object> arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) {
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
            return new NullableClassMap(castProperties);
        }
        
        @Override
        public NullableClassMap validate(Map<String, Object> arg, SchemaConfiguration configuration) throws ValidationException, InvalidTypeException {
            Set<List<Object>> pathSet = new HashSet<>();
            List<Object> pathToItem = List.of("args[0");
            FrozenMap<Object> castArg = castToAllowedTypes(arg, pathToItem, pathSet);
            SchemaConfiguration usedConfiguration = Objects.requireNonNullElseGet(configuration, () -> new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone()));
            ValidationMetadata validationMetadata = new ValidationMetadata(pathToItem, usedConfiguration, new PathToSchemasMap(), new LinkedHashSet<>());
            PathToSchemasMap pathToSchemasMap = getPathToSchemas(this, castArg, validationMetadata, pathSet);
            return getNewInstance(castArg, validationMetadata.pathToItem(), pathToSchemasMap);
        }
        
        
        @Override
        public Object getNewInstance(Object arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) {
            if (arg instanceof FrozenMap) {
                @SuppressWarnings("unchecked") FrozenMap<Object> castArg = (FrozenMap<Object>) arg;
                return getNewInstance(castArg, pathToItem, pathToSchemas);
            }
            throw new InvalidTypeException("Invalid input type="+arg.getClass()+". It can't be instantiated by this schema");
        }
    }

}
