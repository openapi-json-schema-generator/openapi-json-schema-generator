package org.openapijsonschematools.client.paths.fakerefsboolean.post.responses.code200response.content.applicationjson;

import org.checkerframework.checker.nullness.qual.Nullable;
import org.openapijsonschematools.client.components.schemas.BooleanSchema;

public class ApplicationjsonSchema extends BooleanSchema {
    // $refed class
    
    
    public static class ApplicationjsonSchema1 extends BooleanSchema1 {
        private static @Nullable ApplicationjsonSchema1 instance = null;
        public static ApplicationjsonSchema1 getInstance() {
            if (instance == null) {
                instance = new ApplicationjsonSchema1();
            }
            return instance;
        }
    }
}
