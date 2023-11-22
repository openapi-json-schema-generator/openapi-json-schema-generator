package org.openapijsonschematools.components.schemas;
import java.time.LocalDate;
import java.time.ZonedDateTime;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.UUID;
import org.openapijsonschematools.configurations.SchemaConfiguration;
import org.openapijsonschematools.schemas.AnyTypeJsonSchema;
import org.openapijsonschematools.schemas.BooleanJsonSchema;
import org.openapijsonschematools.schemas.DateJsonSchema;
import org.openapijsonschematools.schemas.DateTimeJsonSchema;
import org.openapijsonschematools.schemas.DoubleJsonSchema;
import org.openapijsonschematools.schemas.FloatJsonSchema;
import org.openapijsonschematools.schemas.Int32JsonSchema;
import org.openapijsonschematools.schemas.Int64JsonSchema;
import org.openapijsonschematools.schemas.IntJsonSchema;
import org.openapijsonschematools.schemas.MapJsonSchema;
import org.openapijsonschematools.schemas.NullJsonSchema;
import org.openapijsonschematools.schemas.NumberJsonSchema;
import org.openapijsonschematools.schemas.StringJsonSchema;
import org.openapijsonschematools.schemas.validation.FrozenList;
import org.openapijsonschematools.schemas.validation.FrozenMap;
import org.openapijsonschematools.schemas.validation.ItemsValidator;
import org.openapijsonschematools.schemas.validation.JsonSchema;
import org.openapijsonschematools.schemas.validation.KeywordEntry;
import org.openapijsonschematools.schemas.validation.KeywordValidator;
import org.openapijsonschematools.schemas.validation.TypeValidator;

public class ComposedAnyOfDifferentTypesNoValidations {
    // nest classes so all schemas and input/output classes can be public
    
    
    public class Schema0 extends MapJsonSchema {}
    
    
    public class Schema1 extends DateJsonSchema {}
    
    
    public class Schema2 extends DateTimeJsonSchema {}
    
    
    public class Schema3 extends JsonSchema {
        // BinarySchema
    }
    
    
    public class Schema4 extends StringJsonSchema {}
    
    
    public class Schema5 extends StringJsonSchema {}
    
    
    public class Schema6 extends MapJsonSchema {}
    
    
    public class Schema7 extends BooleanJsonSchema {}
    
    
    public class Schema8 extends NullJsonSchema {}
    
    
    public class Items extends AnyTypeJsonSchema {}
    
    
    public static class Schema9List extends FrozenList<Object> {

        Schema9List(FrozenList<Object> m) {

            super(m);
        }
    }    
    
    public class Schema9 extends JsonSchema {
        public static final LinkedHashMap<String, KeywordValidator> keywordToValidator = new LinkedHashMap<>(Map.ofEntries(
            new KeywordEntry("type", new TypeValidator(Set.of(FrozenList.class))),
            new KeywordEntry("items", new ItemsValidator(Items.class))
        ));
        protected static Schema9List getListOutputInstance(FrozenList<Object> arg) {

            return new Schema9List(arg);
        }
        public static Schema9List validate(List<Object> arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(Schema9.class, arg, configuration);
        }
    }    
    
    public class Schema10 extends NumberJsonSchema {}
    
    
    public class Schema11 extends FloatJsonSchema {}
    
    
    public class Schema12 extends DoubleJsonSchema {}
    
    
    public class Schema13 extends IntJsonSchema {}
    
    
    public class Schema14 extends Int32JsonSchema {}
    
    
    public class Schema15 extends Int64JsonSchema {}
    
    
    public class ComposedAnyOfDifferentTypesNoValidations1 extends JsonSchema {
        /*
        NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
        Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
    
        Do not edit the class manually.
        */
        public static Void validate(Void arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(ComposedAnyOfDifferentTypesNoValidations1.class, arg, configuration);
        }
        
        public static boolean validate(boolean arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(ComposedAnyOfDifferentTypesNoValidations1.class, arg, configuration);
        }
        
        public static int validate(int arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(ComposedAnyOfDifferentTypesNoValidations1.class, arg, configuration);
        }
        
        public static long validate(long arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(ComposedAnyOfDifferentTypesNoValidations1.class, arg, configuration);
        }
        
        public static float validate(float arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(ComposedAnyOfDifferentTypesNoValidations1.class, arg, configuration);
        }
        
        public static double validate(double arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(ComposedAnyOfDifferentTypesNoValidations1.class, arg, configuration);
        }
        
        public static String validate(String arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(ComposedAnyOfDifferentTypesNoValidations1.class, arg, configuration);
        }
        
        public static String validate(ZonedDateTime arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(ComposedAnyOfDifferentTypesNoValidations1.class, arg, configuration);
        }
        
        public static String validate(LocalDate arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(ComposedAnyOfDifferentTypesNoValidations1.class, arg, configuration);
        }
        
        public static String validate(UUID arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(ComposedAnyOfDifferentTypesNoValidations1.class, arg, configuration);
        }
        
        public static <T extends FrozenMap> T validate(Map<String, Object> arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(ComposedAnyOfDifferentTypesNoValidations1.class, arg, configuration);
        }
        
        public static <U extends FrozenList> U validate(List<Object> arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(ComposedAnyOfDifferentTypesNoValidations1.class, arg, configuration);
        }
    }}
