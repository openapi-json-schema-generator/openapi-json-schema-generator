package unit_test_api.schemas;

import unit_test_api.configurations.JsonSchemaKeywordFlags;
import unit_test_api.configurations.SchemaConfiguration;
import unit_test_api.exceptions.ValidationException;
import unit_test_api.schemas.validation.JsonSchema;
import unit_test_api.schemas.validation.JsonSchemaInfo;
import unit_test_api.schemas.validation.PathToSchemasMap;
import unit_test_api.schemas.validation.NumberSchemaValidator;
import unit_test_api.schemas.validation.ValidationMetadata;
import org.checkerframework.checker.nullness.qual.Nullable;

import java.util.HashSet;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Objects;
import java.util.Set;

public class FloatJsonSchema {
    public sealed interface FloatJsonSchema1Boxed permits FloatJsonSchema1BoxedNumber {
        @Nullable Object getData();
    }
    public record FloatJsonSchema1BoxedNumber(Number data) implements FloatJsonSchema1Boxed {
        @Override
        public @Nullable Object getData() {
            return data;
        }
    }

    public static class FloatJsonSchema1 extends JsonSchema<FloatJsonSchema1Boxed> implements NumberSchemaValidator<FloatJsonSchema1BoxedNumber> {
        private static @Nullable FloatJsonSchema1 instance = null;

        protected FloatJsonSchema1() {
            super(new JsonSchemaInfo()
                    .type(Set.of(Float.class))
                    .format("float")
            );
        }

        public static FloatJsonSchema1 getInstance() {
            if (instance == null) {
                instance = new FloatJsonSchema1();
            }
            return instance;
        }

        @Override
        public Number validate(Number arg, SchemaConfiguration configuration) throws ValidationException {
            Set<List<Object>> pathSet = new HashSet<>();
            List<Object> pathToItem = List.of("args[0");
            Number castArg = castToAllowedTypes(arg, pathToItem, pathSet);
            SchemaConfiguration usedConfiguration = Objects.requireNonNullElseGet(configuration, () -> new SchemaConfiguration(new JsonSchemaKeywordFlags.Builder().build()));
            ValidationMetadata validationMetadata = new ValidationMetadata(pathToItem, usedConfiguration, new PathToSchemasMap(), new LinkedHashSet<>());
            PathToSchemasMap pathToSchemasMap = getPathToSchemas(this, castArg, validationMetadata, pathSet);
            return getNewInstance(castArg, validationMetadata.pathToItem(), pathToSchemasMap);
        }

        public float validate(float arg, SchemaConfiguration configuration) throws ValidationException {
            return (float) validate((Number) arg, configuration);
        }

        @Override
        public @Nullable Object getNewInstance(@Nullable Object arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) {
            if (arg instanceof Number) {
                return getNewInstance((Number) arg, pathToItem, pathToSchemas);
            }
            throw new RuntimeException("Invalid input type="+getClass(arg)+". It can't be instantiated by this schema");
        }

        @Override
        public @Nullable Object validate(@Nullable Object arg, SchemaConfiguration configuration) throws ValidationException {
            if (arg instanceof Number) {
                return validate((Number) arg, configuration);
            }
            throw new ValidationException("Invalid input type="+getClass(arg)+". It can't be validated by this schema");
        }

        @Override
        public FloatJsonSchema1BoxedNumber validateAndBox(Number arg, SchemaConfiguration configuration) throws ValidationException {
            return new FloatJsonSchema1BoxedNumber(validate(arg, configuration));
        }

        @Override
        public FloatJsonSchema1Boxed validateAndBox(@Nullable Object arg, SchemaConfiguration configuration) throws ValidationException {
            if (arg instanceof Number castArg) {
                return validateAndBox(castArg, configuration);
            }
            throw new ValidationException("Invalid input type="+getClass(arg)+". It can't be validated by this schema");
        }
    }
}
