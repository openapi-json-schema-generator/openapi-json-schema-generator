package org.openapijsonschematools.client.components.schemas;
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
import org.openapijsonschematools.client.schemas.validation.BooleanEnumValidator;
import org.openapijsonschematools.client.schemas.validation.BooleanSchemaValidator;
import org.openapijsonschematools.client.schemas.validation.BooleanValueMethod;
import org.openapijsonschematools.client.schemas.validation.JsonSchema;
import org.openapijsonschematools.client.schemas.validation.JsonSchemaInfo;
import org.openapijsonschematools.client.schemas.validation.PathToSchemasMap;
import org.openapijsonschematools.client.schemas.validation.ValidationMetadata;

public class EnumWithTrueDoesNotMatch1 {
    // nest classes so all schemas and input/output classes can be public
    
    public enum BooleanEnumWithTrueDoesNotMatch1Enums implements BooleanValueMethod {
        TRUE(true);
        private final boolean value;
    
        BooleanEnumWithTrueDoesNotMatch1Enums(boolean value) {
            this.value = value;
        }
        public boolean value() {
            return this.value;
        }
    }
    
    
    public static abstract sealed class EnumWithTrueDoesNotMatch11Boxed permits EnumWithTrueDoesNotMatch11BoxedBoolean {}
    
    public static final class EnumWithTrueDoesNotMatch11BoxedBoolean extends EnumWithTrueDoesNotMatch11Boxed {
        public final boolean data;
        private EnumWithTrueDoesNotMatch11BoxedBoolean(boolean data) {
            this.data = data;
        }
    }
    
    
    
    public static class EnumWithTrueDoesNotMatch11 extends JsonSchema implements BooleanSchemaValidator<EnumWithTrueDoesNotMatch11BoxedBoolean>, BooleanEnumValidator<BooleanEnumWithTrueDoesNotMatch1Enums> {
        /*
        NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
        Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
    
        Do not edit the class manually.
        */
        private static @Nullable EnumWithTrueDoesNotMatch11 instance = null;
    
        protected EnumWithTrueDoesNotMatch11() {
            super(new JsonSchemaInfo()
                .type(Set.of(Boolean.class))
                .enumValues(SetMaker.makeSet(
                    true
                ))
            );
        }
    
        public static EnumWithTrueDoesNotMatch11 getInstance() {
            if (instance == null) {
                instance = new EnumWithTrueDoesNotMatch11();
            }
            return instance;
        }
        
        @Override
        public boolean validate(boolean arg, SchemaConfiguration configuration) throws ValidationException {
            Set<List<Object>> pathSet = new HashSet<>();
            List<Object> pathToItem = List.of("args[0");
            boolean castArg = castToAllowedTypes(arg, pathToItem, pathSet);
            SchemaConfiguration usedConfiguration = Objects.requireNonNullElseGet(configuration, () -> new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone()));
            ValidationMetadata validationMetadata = new ValidationMetadata(pathToItem, usedConfiguration, new PathToSchemasMap(), new LinkedHashSet<>());
            getPathToSchemas(this, castArg, validationMetadata, pathSet);
            return castArg;
        }
        
        @Override
        public boolean validate(BooleanEnumWithTrueDoesNotMatch1Enums arg,SchemaConfiguration configuration) throws ValidationException {
            return validate(arg.value(), configuration);
        }
        
        @Override
        public @Nullable Object validate(@Nullable Object arg, SchemaConfiguration configuration) throws ValidationException, InvalidTypeException {
            if (arg instanceof Boolean) {
                boolean boolArg = (Boolean) arg;
                return validate(boolArg, configuration);
            }
            throw new InvalidTypeException("Invalid input type="+getClass(arg)+". It can't be validated by this schema");
        }        
        @Override
        public @Nullable Object getNewInstance(@Nullable Object arg, List<Object> pathToItem, PathToSchemasMap pathToSchemas) throws InvalidTypeException {
            if (arg instanceof Boolean) {
                boolean boolArg = (Boolean) arg;
                return getNewInstance(boolArg, pathToItem, pathToSchemas);
            }
            throw new InvalidTypeException("Invalid input type="+getClass(arg)+". It can't be instantiated by this schema");
        }
        @Override
        public EnumWithTrueDoesNotMatch11BoxedBoolean validateAndBox(boolean arg, SchemaConfiguration configuration) throws ValidationException, InvalidTypeException {
            return new EnumWithTrueDoesNotMatch11BoxedBoolean(validate(arg, configuration));
        }
    }
}
