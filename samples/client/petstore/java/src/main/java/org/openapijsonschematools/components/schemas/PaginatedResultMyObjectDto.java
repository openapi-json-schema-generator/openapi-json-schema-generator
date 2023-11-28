package org.openapijsonschematools.components.schemas;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Set;
import org.openapijsonschematools.configurations.SchemaConfiguration;
import org.openapijsonschematools.exceptions.ValidationException;
import org.openapijsonschematools.schemas.AnyTypeJsonSchema;
import org.openapijsonschematools.schemas.IntJsonSchema;
import org.openapijsonschematools.schemas.NotAnyTypeJsonSchema;
import org.openapijsonschematools.schemas.validation.AdditionalPropertiesValidator;
import org.openapijsonschematools.schemas.validation.FrozenList;
import org.openapijsonschematools.schemas.validation.FrozenMap;
import org.openapijsonschematools.schemas.validation.ItemsValidator;
import org.openapijsonschematools.schemas.validation.JsonSchema;
import org.openapijsonschematools.schemas.validation.KeywordEntry;
import org.openapijsonschematools.schemas.validation.KeywordValidator;
import org.openapijsonschematools.schemas.validation.PropertiesValidator;
import org.openapijsonschematools.schemas.validation.PropertyEntry;
import org.openapijsonschematools.schemas.validation.RequiredValidator;
import org.openapijsonschematools.schemas.validation.TypeValidator;

public class PaginatedResultMyObjectDto {
    // nest classes so all schemas and input/output classes can be public
    
    
    public static class AdditionalProperties extends NotAnyTypeJsonSchema {}
        // NotAnyTypeSchema
    
    
    public static class Count extends IntJsonSchema {}
    
    
    public static class ResultsList extends FrozenList<MyObjectDto.MyObjectDtoMap> {
        ResultsList(FrozenList<MyObjectDto.MyObjectDtoMap> m) {
            super(m);
        }
        public static ResultsList of(List<Map<String, String>> arg, SchemaConfiguration configuration) throws ValidationException {
            return Results.validate(arg, configuration);
        }
    }
    
    
    public static class Results extends JsonSchema {
        public static final LinkedHashMap<String, KeywordValidator> keywordToValidator = new LinkedHashMap<>(Map.ofEntries(
            new KeywordEntry("type", new TypeValidator(Set.of(FrozenList.class))),
            new KeywordEntry("items", new ItemsValidator(MyObjectDto.MyObjectDto1.class))
            
        ));
        protected static ResultsList getListOutputInstance(FrozenList<MyObjectDto.MyObjectDtoMap> arg) {
            return new ResultsList(arg);
        }
        public static ResultsList validate(List<Map<String, String>> arg, SchemaConfiguration configuration) throws ValidationException {
            return JsonSchema.validate(Results.class, arg, configuration);
        }
    }    
    
    public static class PaginatedResultMyObjectDtoMap extends FrozenMap<String, Object> {
        PaginatedResultMyObjectDtoMap(FrozenMap<String, Object> m) {
            super(m);
        }
        public static final Set<String> requiredKeys = Set.of(
            "count",
            "results"
        );
        public static final Set<String> optionalKeys = Set.of();
        public static PaginatedResultMyObjectDtoMap of(Map<String, Object> arg, SchemaConfiguration configuration) throws ValidationException {
            return PaginatedResultMyObjectDto1.validate(arg, configuration);
        }
        
        public long count() {
            return (long) get("count");
        }
        
        public ResultsList results() {
            return (ResultsList) get("results");
        }
    }    
    
    public static class PaginatedResultMyObjectDto1 extends JsonSchema {
        /*
        NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
        Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
    
        Do not edit the class manually.
        */
        public static final LinkedHashMap<String, KeywordValidator> keywordToValidator = new LinkedHashMap<>(Map.ofEntries(
            new KeywordEntry("type", new TypeValidator(Set.of(FrozenMap.class))),
            new KeywordEntry("properties", new PropertiesValidator(Map.ofEntries(
                new PropertyEntry("count", Count.class),
                new PropertyEntry("results", Results.class)
            ))),
            
            new KeywordEntry("required", new RequiredValidator(Set.of(
                "count",
                "results"
            ))),
            
            new KeywordEntry("additionalProperties", new AdditionalPropertiesValidator(AdditionalProperties.class))
        ));
        protected static PaginatedResultMyObjectDtoMap getMapOutputInstance(FrozenMap<String, Object> arg) {
            return new PaginatedResultMyObjectDtoMap(arg);
        }
        public static PaginatedResultMyObjectDtoMap validate(Map<String, Object> arg, SchemaConfiguration configuration) throws ValidationException {
            return JsonSchema.validate(PaginatedResultMyObjectDto1.class, arg, configuration);
        }
    }
}
