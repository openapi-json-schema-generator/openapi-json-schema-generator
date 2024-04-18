package org.openapijsonschematools.client.components.schemas;
import org.checkerframework.checker.nullness.qual.Nullable;
import org.openapijsonschematools.client.schemas.StringJsonSchema;

public class String extends StringJsonSchema {
    // nest classes so all schemas and input/output classes can be public
    
    
    public static class String1 extends StringJsonSchema.StringJsonSchema1 {
        private static @Nullable String1 instance = null;
        public static String1 getInstance() {
            if (instance == null) {
                instance = new String1();
            }
            return instance;
        }
    }

}
