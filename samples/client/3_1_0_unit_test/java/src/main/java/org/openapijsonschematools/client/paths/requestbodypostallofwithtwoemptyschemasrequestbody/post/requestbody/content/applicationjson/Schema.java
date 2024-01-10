package org.openapijsonschematools.client.paths.requestbodypostallofwithtwoemptyschemasrequestbody.post.requestbody.content.applicationjson;

import org.checkerframework.checker.nullness.qual.Nullable;
import org.openapijsonschematools.client.components.schemas.AllofWithTwoEmptySchemas;

public class Schema2 extends AllofWithTwoEmptySchemas {
    // $refed class
    
    
    public static class Schema3 extends AllofWithTwoEmptySchemas1 {
        private static @Nullable Schema3 instance = null;
        public static Schema3 getInstance() {
            if (instance == null) {
                instance = new Schema3();
            }
            return instance;
        }
    }
}
