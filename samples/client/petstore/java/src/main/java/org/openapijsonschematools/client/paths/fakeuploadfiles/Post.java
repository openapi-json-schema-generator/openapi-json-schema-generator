package org.openapijsonschematools.client.paths.fakeuploadfiles;

import org.checkerframework.checker.nullness.qual.Nullable;
import org.openapijsonschematools.client.paths.fakeuploadfiles.post.RequestBody;
import org.openapijsonschematools.client.RootServerInfo;
import org.openapijsonschematools.client.paths.fakeuploadfiles.post.Responses;

public class Post {
    public static class PostCallData {
        public @Nullable RequestBody.SealedRequestBody requestBody;
        public @Nullable RootServerInfo.ServerIndex serverIndex;
    }
}
