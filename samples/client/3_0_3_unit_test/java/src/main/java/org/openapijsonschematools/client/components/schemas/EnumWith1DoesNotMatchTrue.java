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
import org.openapijsonschematools.client.exceptions.InvalidTypeException;
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

public class EnumWith1DoesNotMatchTrue {
    // nest classes so all schemas and input/output classes can be public
    
    public enum IntegerEnumWith1DoesNotMatchTrueEnums implements IntegerValueMethod {
        POSITIVE_1(1);
        private final int value;
    
        IntegerEnumWith1DoesNotMatchTrueEnums(int value) {
            this.value = value;
        }
        public int value() {
            return this.value;
        }
    }
    
    public enum LongEnumWith1DoesNotMatchTrueEnums implements LongValueMethod {
        POSITIVE_1(1L);
        private final long value;
    
        LongEnumWith1DoesNotMatchTrueEnums(long value) {
            this.value = value;
        }
        public long value() {
            return this.value;
        }
    }
    
    public enum FloatEnumWith1DoesNotMatchTrueEnums implements FloatValueMethod {
        POSITIVE_1(1.0f);
        private final float value;
    
        FloatEnumWith1DoesNotMatchTrueEnums(float value) {
            this.value = value;
        }
        public float value() {
            return this.value;
        }
    }
    
    public enum DoubleEnumWith1DoesNotMatchTrueEnums implements DoubleValueMethod {
        POSITIVE_1(1.0d);
        private final double value;
    
        DoubleEnumWith1DoesNotMatchTrueEnums(double value) {
            this.value = value;
        }
        public double value() {
            return this.value;
        }
    }
    
    
    public sealed interface EnumWith1DoesNotMatchTrue1Boxed permits EnumWith1DoesNotMatchTrue1BoxedNumber {
        @Nullable Object getData();
    }
    
    public record EnumWith1DoesNotMatchTrue1BoxedNumber(Number data) implements EnumWith1DoesNotMatchTrue1Boxed {
        @Override
        public @Nullable Object getData() {
            return data;
        }
    }
    
    
    
    public static class EnumWith1DoesNotMatchTrue1 extends JsonSchema<EnumWith1DoesNotMatchTrue1Boxed> implements IntegerEnumValidator<IntegerEnumWith1DoesNotMatchTrueEnums>, LongEnumValidator<LongEnumWith1DoesNotMatchTrueEnums>, FloatEnumValidator<FloatEnumWith1DoesNotMatchTrueEnums>, DoubleEnumValidator<DoubleEnumWith1DoesNotMatchTrueEnums>, NumberSchemaValidator<EnumWith1DoesNotMatchTrue1BoxedNumber> {
        /*
        NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
        Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
    
        Do not edit the class manually.
        */
        private static @Nullable EnumWith1DoesNotMatchTrue1 instance = null;
    
        protected EnumWith1DoesNotMatchTrue1() {
            super(new JsonSchemaInfo()
                .type(Set.of(
                    Integer.class,
                    Long.class,
                    Float.class,
                    Double.class
                ))
                .enumValues(SetMaker.makeSet(
                    new BigDecimal("1")
                ))
            );
        }
    
        public static EnumWith1DoesNotMatchTrue1 getInstance() {
            if (instance == null) {
                instance = new EnumWith1DoesNotMatchTrue1();
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
            PathToSchemasMap pathToSchemasMap = getPathToSchemas(this, castArg, validationMetadata, pathSet);
            return castArg;
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
        public int validate(IntegerEnumWith1DoesNotMatchTrueEnums arg,SchemaConfiguration configuration) throws ValidationException {
            return (int) validate((Number) arg.value(), configuration);
        }
        
        @Override
        public long validate(LongEnumWith1DoesNotMatchTrueEnums arg,SchemaConfiguration configuration) throws ValidationException {
            return (long) validate((Number) arg.value(), configuration);
        }
        
        @Override
        public float validate(FloatEnumWith1DoesNotMatchTrueEnums arg,SchemaConfiguration configuration) throws ValidationException {
            return (float) validate((Number) arg.value(), configuration);
        }
        
        @Override
        public double validate(DoubleEnumWith1DoesNotMatchTrueEnums arg,SchemaConfiguration configuration) throws ValidationException {
            return (double) validate((Number) arg.value(), configuration);
        }
        
        @Override
        public @Nullable Object validate(@Nullable Object arg, SchemaConfiguration configuration) throws ValidationException, InvalidTypeException {
            if (arg instanceof Number) {
                return validate((Number) arg, configuration);
            }
            throw new InvalidTypeException("Invalid input type="+getClass(arg)+". It can't be validated by this schema");
        }        
        @Override
        public @Nullable Object getNewInstance(@Nullable Object arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) throws InvalidTypeException {
            if (arg instanceof Number) {
                return getNewInstance((Number) arg, pathToItem, pathToSchemas);
            }
            throw new InvalidTypeException("Invalid input type="+getClass(arg)+". It can't be instantiated by this schema");
        }
        @Override
        public EnumWith1DoesNotMatchTrue1BoxedNumber validateAndBox(Number arg, SchemaConfiguration configuration) throws ValidationException, InvalidTypeException {
            return new EnumWith1DoesNotMatchTrue1BoxedNumber(validate(arg, configuration));
        }
        @Override
        public EnumWith1DoesNotMatchTrue1Boxed validateAndBox(@Nullable Object arg, SchemaConfiguration configuration) throws ValidationException, InvalidTypeException {
            if (arg instanceof Number castArg) {
                return validateAndBox(castArg, configuration);
            }
            throw new InvalidTypeException("Invalid input type="+getClass(arg)+". It can't be validated by this schema");
        }
    }
}
