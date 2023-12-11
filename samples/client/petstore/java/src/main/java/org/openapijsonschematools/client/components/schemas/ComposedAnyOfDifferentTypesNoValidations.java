package org.openapijsonschematools.client.components.schemas;
import java.time.LocalDate;
import java.time.ZonedDateTime;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.UUID;
import org.openapijsonschematools.client.configurations.SchemaConfiguration;
import org.openapijsonschematools.client.exceptions.ValidationException;
import org.openapijsonschematools.client.schemas.AnyTypeJsonSchema;
import org.openapijsonschematools.client.schemas.BooleanJsonSchema;
import org.openapijsonschematools.client.schemas.DateJsonSchema;
import org.openapijsonschematools.client.schemas.DateTimeJsonSchema;
import org.openapijsonschematools.client.schemas.DoubleJsonSchema;
import org.openapijsonschematools.client.schemas.FloatJsonSchema;
import org.openapijsonschematools.client.schemas.Int32JsonSchema;
import org.openapijsonschematools.client.schemas.Int64JsonSchema;
import org.openapijsonschematools.client.schemas.IntJsonSchema;
import org.openapijsonschematools.client.schemas.MapJsonSchema;
import org.openapijsonschematools.client.schemas.NullJsonSchema;
import org.openapijsonschematools.client.schemas.NumberJsonSchema;
import org.openapijsonschematools.client.schemas.StringJsonSchema;
import org.openapijsonschematools.client.schemas.validation.AnyOfValidator;
import org.openapijsonschematools.client.schemas.validation.FrozenList;
import org.openapijsonschematools.client.schemas.validation.FrozenMap;
import org.openapijsonschematools.client.schemas.validation.ItemsValidator;
import org.openapijsonschematools.client.schemas.validation.JsonSchema;
import org.openapijsonschematools.client.schemas.validation.JsonSchemaFactory;
import org.openapijsonschematools.client.schemas.validation.KeywordEntry;
import org.openapijsonschematools.client.schemas.validation.KeywordValidator;
import org.openapijsonschematools.client.schemas.validation.NonCollectionJsonSchema;
import org.openapijsonschematools.client.schemas.validation.TypeValidator;

public class ComposedAnyOfDifferentTypesNoValidations {
    // nest classes so all schemas and input/output classes can be public
    
    
    public static class Schema0 extends MapJsonSchema {}
    
    
    public static class Schema1 extends DateJsonSchema {}
    
    
    public static class Schema2 extends DateTimeJsonSchema {}
    
    
    public static class Schema3 extends StringJsonSchema {
        // BinarySchema
    }
    
    
    public static class Schema4 extends StringJsonSchema {}
    
    
    public static class Schema5 extends StringJsonSchema {}
    
    
    public static class Schema6 extends MapJsonSchema {}
    
    
    public static class Schema7 extends BooleanJsonSchema {}
    
    
    public static class Schema8 extends NullJsonSchema {}
    
    
    public static class Items extends AnyTypeJsonSchema {}
    
    
    public static class Schema9List extends FrozenList<Object> {
        Schema9List(FrozenList<Object> m) {
            super(m);
        }
        public static Schema9List of(List<Object> arg, SchemaConfiguration configuration) throws ValidationException {
            return JsonSchemaFactory.getInstance(Schema9.class).validate(arg, configuration);
        }
    }
    
    public class Schema9ListInput {
        // class to build List<Object>
    }
    
    
    public static class Schema9 extends JsonSchema<Object, Object, FrozenMap<String, Object>, Object, Object, Schema9List> {
        public Schema9() {
            super(new LinkedHashMap<>(Map.ofEntries(
                new KeywordEntry("type", new TypeValidator(Set.of(FrozenList.class))),
                new KeywordEntry("items", new ItemsValidator(Items.class))
            )));
        }
        
        @Override
        protected Schema9List getListOutputInstance(FrozenList<Object> arg) {
            return new Schema9List(arg);
        }
        public Schema9List validate(List<Object> arg, SchemaConfiguration configuration) throws ValidationException {
            return validateList(arg, configuration);
        }
    }    
    
    public static class Schema10 extends NumberJsonSchema {}
    
    
    public static class Schema11 extends FloatJsonSchema {}
    
    
    public static class Schema12 extends DoubleJsonSchema {}
    
    
    public static class Schema13 extends IntJsonSchema {}
    
    
    public static class Schema14 extends Int32JsonSchema {}
    
    
    public static class Schema15 extends Int64JsonSchema {}
    
    
    public static class ComposedAnyOfDifferentTypesNoValidations1 extends NonCollectionJsonSchema {
        /*
        NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
        Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
    
        Do not edit the class manually.
        */
        public ComposedAnyOfDifferentTypesNoValidations1() {
            super(new LinkedHashMap<>(Map.ofEntries(
                new KeywordEntry("anyOf", new AnyOfValidator(List.of(
                    Schema0.class,
                    Schema1.class,
                    Schema2.class,
                    Schema3.class,
                    Schema4.class,
                    Schema5.class,
                    Schema6.class,
                    Schema7.class,
                    Schema8.class,
                    Schema9.class,
                    Schema10.class,
                    Schema11.class,
                    Schema12.class,
                    Schema13.class,
                    Schema14.class,
                    Schema15.class
                )))
            )));
        }
        public Void validate(Void arg, SchemaConfiguration configuration) throws ValidationException {
            return validateVoid(arg, configuration);
        }
        
        public boolean validate(boolean arg, SchemaConfiguration configuration) throws ValidationException {
            return validateBoolean(arg, configuration);
        }
        
        public int validate(int arg, SchemaConfiguration configuration) throws ValidationException {
            return validateInt(arg, configuration);
        }
        
        public long validate(long arg, SchemaConfiguration configuration) throws ValidationException {
            return validateLong(arg, configuration);
        }
        
        public float validate(float arg, SchemaConfiguration configuration) throws ValidationException {
            return validateFloat(arg, configuration);
        }
        
        public double validate(double arg, SchemaConfiguration configuration) throws ValidationException {
            return validateDouble(arg, configuration);
        }
        
        public String validate(String arg, SchemaConfiguration configuration) throws ValidationException {
            return validateString(arg, configuration);
        }
        
        public String validate(ZonedDateTime arg, SchemaConfiguration configuration) throws ValidationException {
            return validateZonedDateTime(arg, configuration);
        }
        
        public String validate(LocalDate arg, SchemaConfiguration configuration) throws ValidationException {
            return validateLocalDate(arg, configuration);
        }
        
        public String validate(UUID arg, SchemaConfiguration configuration) throws ValidationException {
            return validateUUID(arg, configuration);
        }
        
        public FrozenMap<String, Object> validate(Map<String, Object> arg, SchemaConfiguration configuration) throws ValidationException {
            return validateMap(arg, configuration);
        }
        
        public FrozenList<Object> validate(List<Object> arg, SchemaConfiguration configuration) throws ValidationException {
            return validateList(arg, configuration);
        }
    }}
