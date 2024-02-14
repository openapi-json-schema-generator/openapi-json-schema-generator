package org.openapijsonschematools.client.components.parameters.pathusername;
import org.checkerframework.checker.nullness.qual.Nullable;
import org.openapijsonschematools.client.schemas.StringJsonSchema;

public class Schema extends StringJsonSchema {
    // nest classes so all schemas and input/output classes can be public
    
    
    public static class Schema1 extends StringJsonSchema.StringJsonSchema1 {
        private static @Nullable Schema1 instance = null;
        public static Schema1 getInstance() {
            if (instance == null) {
                instance = new Schema1();
            }
            return instance;
        }
    }

}
