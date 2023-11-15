package org.openapijsonschematools.paths.storeorderorderid.get.responses.response200.content.applicationxml;

public class Schema {
    // $refed class
    
    
    public record Schema2() implements JsonSchema {
        public static Order.Order2 withDefaults() {
            return Order.Order2.withDefaults();
        }
    
        public static <T extends FrozenMap> T validate(Map<String, Object> arg, SchemaConfiguration configuration) {
            return JsonSchema.validate(Order.Order2.class, arg, configuration);
        }
    }
}
