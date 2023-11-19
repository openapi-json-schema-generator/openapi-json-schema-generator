package org.openapijsonschematools.components.schemas;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Set;
import org.openapijsonschematools.configurations.SchemaConfiguration;
import org.openapijsonschematools.schemas.AnyTypeJsonSchema;
import org.openapijsonschematools.schemas.FrozenList;
import org.openapijsonschematools.schemas.JsonSchema;

public class ArrayHoldingAnyType {
    // nest classes so all schemas and input/output classes can be public
    
    
    public class Items extends AnyTypeJsonSchema {}
    
    
    public static class ArrayHoldingAnyTypeTuple extends FrozenList<Object> {
        ArrayHoldingAnyTypeTuple(FrozenList<Object> m) {
            super(m);
        }
    }    
    
    public class ArrayHoldingAnyType1 implements JsonSchema {
        /*
        NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
        Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
    
        Do not edit the class manually.
        */
        static final LinkedHashSet<Class<?>> type = new LinkedHashSet<>(Set.of(
            FrozenList.class
        ));
        static final Class<?> items = Items.class;
        public static <U extends FrozenList> U validate(List<Object> arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(ArrayHoldingAnyType1.class, arg, configuration);
        }
    }}
