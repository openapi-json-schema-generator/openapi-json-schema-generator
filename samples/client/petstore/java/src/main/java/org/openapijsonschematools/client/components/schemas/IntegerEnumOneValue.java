package org.openapijsonschematools.client.components.schemas;
import java.math.BigDecimal;
import java.util.HashSet;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Objects;
import java.util.Set;
import org.checkerframework.checker.nullness.qual.Nullable;
import org.openapijsonschematools.client.configurations.JsonSchemaKeywordFlags;
import org.openapijsonschematools.client.configurations.SchemaConfiguration;
import org.openapijsonschematools.client.exceptions.ValidationException;
import org.openapijsonschematools.client.schemas.SetMaker;
import org.openapijsonschematools.client.schemas.validation.DoubleEnumValidator;
import org.openapijsonschematools.client.schemas.validation.DoubleValueMethod;
import org.openapijsonschematools.client.schemas.validation.FloatEnumValidator;
import org.openapijsonschematools.client.schemas.validation.FloatValueMethod;
import org.openapijsonschematools.client.schemas.validation.IntegerEnumValidator;
import org.openapijsonschematools.client.schemas.validation.IntegerValueMethod;
import org.openapijsonschematools.client.schemas.validation.JsonSchema;
import org.openapijsonschematools.client.schemas.validation.JsonSchemaInfo;
import org.openapijsonschematools.client.schemas.validation.LongEnumValidator;
import org.openapijsonschematools.client.schemas.validation.LongValueMethod;
import org.openapijsonschematools.client.schemas.validation.NumberSchemaValidator;
import org.openapijsonschematools.client.schemas.validation.PathToSchemasMap;
import org.openapijsonschematools.client.schemas.validation.ValidationMetadata;

public class IntegerEnumOneValue {
    // nest classes so all schemas and input/output classes can be public
    
    public enum IntegerIntegerEnumOneValueEnums implements IntegerValueMethod {
        POSITIVE_0(0);
        private final int value;
    
        IntegerIntegerEnumOneValueEnums(int value) {
            this.value = value;
        }
        public int value() {
            return this.value;
        }
    }
    
    public enum LongIntegerEnumOneValueEnums implements LongValueMethod {
        POSITIVE_0(0L);
        private final long value;
    
        LongIntegerEnumOneValueEnums(long value) {
            this.value = value;
        }
        public long value() {
            return this.value;
        }
    }
    
    public enum FloatIntegerEnumOneValueEnums implements FloatValueMethod {
        POSITIVE_0(0.0f);
        private final float value;
    
        FloatIntegerEnumOneValueEnums(float value) {
            this.value = value;
        }
        public float value() {
            return this.value;
        }
    }
    
    public enum DoubleIntegerEnumOneValueEnums implements DoubleValueMethod {
        POSITIVE_0(0.0d);
        private final double value;
    
        DoubleIntegerEnumOneValueEnums(double value) {
            this.value = value;
        }
        public double value() {
            return this.value;
        }
    }
    
    
    public sealed interface IntegerEnumOneValue1Boxed permits IntegerEnumOneValue1BoxedNumber {
        @Nullable Object getData();
    }
    
    public record IntegerEnumOneValue1BoxedNumber(Number data) implements IntegerEnumOneValue1Boxed {
        @Override
        public @Nullable Object getData() {
            return data;
        }
    }
    
    
    
    public static class IntegerEnumOneValue1 extends JsonSchema<IntegerEnumOneValue1Boxed> implements IntegerEnumValidator<IntegerIntegerEnumOneValueEnums>, LongEnumValidator<LongIntegerEnumOneValueEnums>, FloatEnumValidator<FloatIntegerEnumOneValueEnums>, DoubleEnumValidator<DoubleIntegerEnumOneValueEnums>, NumberSchemaValidator<IntegerEnumOneValue1BoxedNumber> {
        /*
        NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
        Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
    
        Do not edit the class manually.
        */
        private static @Nullable IntegerEnumOneValue1 instance = null;
    
        protected IntegerEnumOneValue1() {
            super(new JsonSchemaInfo()
                .type(Set.of(
                    Integer.class,
                    Long.class,
                    Float.class,
                    Double.class
                ))
                .format("int")
                .enumValues(SetMaker.makeSet(
                    new BigDecimal("0")
                ))
            );
        }
    
        public static IntegerEnumOneValue1 getInstance() {
            if (instance == null) {
                instance = new IntegerEnumOneValue1();
            }
            return instance;
        }
        
        @Override
        public Number validate(Number arg, SchemaConfiguration configuration) throws ValidationException {
            Set<List<Object>> pathSet = new HashSet<>();
            List<Object> pathToItem = List.of("args[0");
            Number castArg = castToAllowedTypes(arg, pathToItem, pathSet);
            SchemaConfiguration usedConfiguration = Objects.requireNonNullElseGet(configuration, () -> new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone()));
            ValidationMetadata validationMetadata = new ValidationMetadata(pathToItem, usedConfiguration, new PathToSchemasMap(), new LinkedHashSet<>());
            getPathToSchemas(this, castArg, validationMetadata, pathSet);
            return castArg;
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
        public int validate(IntegerIntegerEnumOneValueEnums arg,SchemaConfiguration configuration) throws ValidationException {
            return (int) validate((Number) arg.value(), configuration);
        }
        
        @Override
        public long validate(LongIntegerEnumOneValueEnums arg,SchemaConfiguration configuration) throws ValidationException {
            return (long) validate((Number) arg.value(), configuration);
        }
        
        @Override
        public float validate(FloatIntegerEnumOneValueEnums arg,SchemaConfiguration configuration) throws ValidationException {
            return (float) validate((Number) arg.value(), configuration);
        }
        
        @Override
        public double validate(DoubleIntegerEnumOneValueEnums arg,SchemaConfiguration configuration) throws ValidationException {
            return (double) validate((Number) arg.value(), configuration);
        }
        
        @Override
        public @Nullable Object validate(@Nullable Object arg, SchemaConfiguration configuration) throws ValidationException {
            if (arg instanceof Number) {
                return validate((Number) arg, configuration);
            }
            throw new ValidationException("Invalid input type="+getClass(arg)+". It can't be validated by this schema");
        }        
        @Override
        public @Nullable Object getNewInstance(@Nullable Object arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) {
            if (arg instanceof Number) {
                return getNewInstance((Number) arg, pathToItem, pathToSchemas);
            }
            throw new RuntimeException("Invalid input type="+getClass(arg)+". It can't be instantiated by this schema");
        }
        @Override
        public IntegerEnumOneValue1BoxedNumber validateAndBox(Number arg, SchemaConfiguration configuration) throws ValidationException {
            return new IntegerEnumOneValue1BoxedNumber(validate(arg, configuration));
        }
        @Override
        public IntegerEnumOneValue1Boxed validateAndBox(@Nullable Object arg, SchemaConfiguration configuration) throws ValidationException {
            if (arg instanceof Number castArg) {
                return validateAndBox(castArg, configuration);
            }
            throw new ValidationException("Invalid input type="+getClass(arg)+". It can't be validated by this schema");
        }
    }
}
