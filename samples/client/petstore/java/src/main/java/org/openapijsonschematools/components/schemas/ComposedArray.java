package org.openapijsonschematools.components.schemas;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Set;
import org.openapijsonschematools.configurations.SchemaConfiguration;
import org.openapijsonschematools.schemas.AnyTypeJsonSchema;
import org.openapijsonschematools.schemas.validation.FrozenList;
import org.openapijsonschematools.schemas.validation.JsonSchema;

public class ComposedArray {
    // nest classes so all schemas and input/output classes can be public
    
    
    public class Items extends AnyTypeJsonSchema {}
    
    
    public static class ComposedArrayTuple extends FrozenList<Object> {
        ComposedArrayTuple(FrozenList<Object> m) {
            super(m);
        }
    }    
    
    public class ComposedArray1 extends JsonSchema {
        /*
        NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
        Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
    
        Do not edit the class manually.
        */
        public static final LinkedHashSet<Class<?>> type = new LinkedHashSet<>(Set.of(
            FrozenList.class
        ));
        public static final Class<?> items = Items.class;
        protected static ComposedArrayTuple getListOutputInstance(FrozenList<Object> arg) {
            return new ComposedArrayTuple(arg);
        }
        public static <U extends FrozenList> U validate(List<Object> arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(ComposedArray1.class, arg, configuration);
        }
    }}
