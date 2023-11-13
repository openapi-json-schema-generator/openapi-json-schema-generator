package org.openapijsonschematools.components.schemas;
import org.openapijsonschematools.configurations.SchemaConfiguration;
import org.openapijsonschematools.schemas.Schema;
import org.openapijsonschematools.schemas.AnyTypeSchema;

import java.util.LinkedHashSet;
public class ObjectWithAllOfWithReqTestPropFromUnsetAddProp {
    // nest classes so all schemas and input/output classes can be public
    
    
    public record Name(LinkedHashSet<Class<?>> type) implements Schema {
        public static Name withDefaults() {
            LinkedHashSet<Class<?>> type = new LinkedHashSet<>();
            type.add(String.class);
            return new Name(type);
        }
    }}
