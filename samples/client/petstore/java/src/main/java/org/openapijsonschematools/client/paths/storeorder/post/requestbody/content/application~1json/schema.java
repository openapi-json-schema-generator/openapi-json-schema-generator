package org.openapijsonschematools.client.paths.storeorder.post.requestbody.content.application~1json;

import org.checkerframework.checker.nullness.qual.Nullable;
import org.openapijsonschematools.client.components.schemas.Order;

public class Schema extends Order {
    // $refed class
    
    
    public static class Schema1 extends Order1 {
        private static @Nullable Schema1 instance = null;
        public static Schema1 getInstance() {
            if (instance == null) {
                instance = new Schema1();
            }
            return instance;
        }
    }
}
