package org.openapijsonschematools.client.paths.fakerefsboolean.post.requestbody.content.applicationjson;

import org.checkerframework.checker.nullness.qual.Nullable;
import org.openapijsonschematools.client.components.schemas.BooleanSchema;

public class Schema extends BooleanSchema {
    // $refed class
    
    
    public static class Schema1 extends BooleanSchema1 {
        private static @Nullable Schema1 instance = null;
        public static Schema1 getInstance() {
            if (instance == null) {
                instance = new Schema1();
            }
            return instance;
        }
    }
}
