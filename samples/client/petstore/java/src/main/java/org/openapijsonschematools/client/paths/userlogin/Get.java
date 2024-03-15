package org.openapijsonschematools.client.paths.userlogin;

import org.checkerframework.checker.nullness.qual.Nullable;
import org.openapijsonschematools.client.RootServerInfo;
import org.openapijsonschematools.client.paths.userlogin.get.QueryParameters;
import org.openapijsonschematools.client.paths.userlogin.get.Parameters;
import org.openapijsonschematools.client.paths.userlogin.get.Responses;

public class Get {
    public static class GetCallData {
        public @Nullable RootServerInfo.ServerIndex serverIndex;
        public @Nullable QueryParameters.QueryParameters1 queryParameters;
    }
}
