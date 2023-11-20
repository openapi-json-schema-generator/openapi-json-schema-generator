package org.openapijsonschematools.components.schemas;
import java.util.AbstractMap;
import java.util.LinkedHashMap;
import java.util.LinkedHashSet;
import java.util.Map;
import java.util.Set;
import org.openapijsonschematools.configurations.SchemaConfiguration;
import org.openapijsonschematools.schemas.BooleanJsonSchema;
import org.openapijsonschematools.schemas.DateTimeJsonSchema;
import org.openapijsonschematools.schemas.Int32JsonSchema;
import org.openapijsonschematools.schemas.Int64JsonSchema;
import org.openapijsonschematools.schemas.validation.FrozenMap;
import org.openapijsonschematools.schemas.validation.JsonSchema;

public class Order {
    // nest classes so all schemas and input/output classes can be public
    
    
    public class Id extends Int64JsonSchema {}
    
    
    public class PetId extends Int64JsonSchema {}
    
    
    public class Quantity extends Int32JsonSchema {}
    
    
    public class ShipDate extends DateTimeJsonSchema {}
    
    
    public class Status extends JsonSchema {
        public static final LinkedHashSet<Class<?>> type = new LinkedHashSet<>(Set.of(
            String.class
        ));
        public static String validate(String arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(Status.class, arg, configuration);
        }
    }    
    
    public class Complete extends BooleanJsonSchema {}
    
    
    public static class OrderMap extends FrozenMap<String, Object> {
        OrderMap(FrozenMap<? extends String, ?> m) {
            super(m);
        }
        public static OrderMap of(Map<String, Object> arg, SchemaConfiguration configuration) {
            return Order1.validate(arg, configuration);
        }
    }    
    
    public class Order1 extends JsonSchema {
        /*
        NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
        Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
    
        Do not edit the class manually.
        */
        public static final LinkedHashSet<Class<?>> type = new LinkedHashSet<>(Set.of(
            FrozenMap.class
        ));
        public static final LinkedHashMap<String, Class<?>> properties = new LinkedHashMap<>(Map.ofEntries(
            new AbstractMap.SimpleEntry<String, Class<?>>("id", Id.class),
            new AbstractMap.SimpleEntry<String, Class<?>>("petId", PetId.class),
            new AbstractMap.SimpleEntry<String, Class<?>>("quantity", Quantity.class),
            new AbstractMap.SimpleEntry<String, Class<?>>("shipDate", ShipDate.class),
            new AbstractMap.SimpleEntry<String, Class<?>>("status", Status.class),
            new AbstractMap.SimpleEntry<String, Class<?>>("complete", Complete.class)
        ));
        protected static OrderMap getMapOutputInstance(FrozenMap<? extends String, ?> arg) {
            return new OrderMap(arg);
        }
        public static <T extends FrozenMap> T validate(Map<String, Object> arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(Order1.class, arg, configuration);
        }
    }
}
