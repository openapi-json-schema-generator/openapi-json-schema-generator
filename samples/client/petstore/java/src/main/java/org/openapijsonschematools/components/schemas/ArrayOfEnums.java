package org.openapijsonschematools.components.schemas;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Set;
import org.openapijsonschematools.configurations.SchemaConfiguration;
import org.openapijsonschematools.schemas.validation.FrozenList;
import org.openapijsonschematools.schemas.validation.JsonSchema;

public class ArrayOfEnums {
    // nest classes so all schemas and input/output classes can be public
    
    
    public static class ArrayOfEnumsTuple extends FrozenList<Object> {
        ArrayOfEnumsTuple(FrozenList<Object> m) {
            super(m);
        }
    }    
    
    public class ArrayOfEnums1 extends JsonSchema {
        /*
        NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
        Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
    
        Do not edit the class manually.
        */
        public static final LinkedHashSet<Class<?>> type = new LinkedHashSet<>(Set.of(
            FrozenList.class
        ));
        public static final Class<?> items = StringEnum.StringEnum1.class;
        protected static ArrayOfEnumsTuple getListOutputInstance(FrozenList<Object> arg) {
            return new ArrayOfEnumsTuple(arg);
        }
        public static <U extends FrozenList> U validate(List<Object> arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(ArrayOfEnums1.class, arg, configuration);
        }
    }}
