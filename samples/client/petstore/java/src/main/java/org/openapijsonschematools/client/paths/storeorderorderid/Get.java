package org.openapijsonschematools.client.paths.storeorderorderid;

import org.checkerframework.checker.nullness.qual.Nullable;
import org.openapijsonschematools.client.RootServerInfo;
import org.openapijsonschematools.client.paths.storeorderorderid.get.PathParameters;
import org.openapijsonschematools.client.paths.storeorderorderid.get.Parameters;
import org.openapijsonschematools.client.paths.storeorderorderid.get.Responses;
import org.openapijsonschematools.client.configurations.ApiConfiguration;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;

public class Get {

    public static class Get1 {
        private final ApiConfiguration apiConfiguration;

        public Get1(ApiConfiguration apiConfiguration) {
            this.apiConfiguration = apiConfiguration;
        }

        public Responses.EndpointResponse get(GetRequest request) {
            Map<String, List<String>> headers = apiConfiguration.getDefaultHeaders();
            // todo serialize all parameter types
        }
    }

    public static class GetRequest {
        public PathParameters.PathParametersMap pathParameters;
        public RootServerInfo.@Nullable ServerIndex serverIndex;

        public GetRequest(
            PathParameters.PathParametersMap pathParameters,
            RootServerInfo.@Nullable ServerIndex serverIndex
        ) {
            this.pathParameters = pathParameters;
            this.serverIndex = serverIndex;
        }
    }

    public static class GetNullableRequest {
        public PathParameters.@Nullable PathParametersMap pathParameters;
        public RootServerInfo.@Nullable ServerIndex serverIndex;
    }

    public interface SetterForServerIndex <T> {
        GetNullableRequest getInstance();
        T getBuilderAfterServerIndex(GetNullableRequest instance);
        default T serverIndex(RootServerInfo.ServerIndex serverIndex) {
            var instance = getInstance();
            instance.serverIndex = serverIndex;
            return getBuilderAfterServerIndex(instance);
        }
    }

    public interface SetterForPathParameters <T> {
        GetNullableRequest getInstance();
        T getBuilderAfterPathParameters(GetNullableRequest instance);
        default T pathParameters(PathParameters.PathParametersMap pathParameters) {
            var instance = getInstance();
            instance.pathParameters = pathParameters;
            return getBuilderAfterPathParameters(instance);
        }
    }

    public static class Get0RequestBuilder implements SetterForServerIndex<Get0RequestBuilder> {
        private final GetNullableRequest instance;

        public Get0RequestBuilder(GetNullableRequest instance) {
            this.instance = instance;
        }

        public GetRequest build() {
            var pathParameters = instance.pathParameters;
            if (pathParameters == null) {
                throw new RuntimeException("invalid null value for required parameter");
            }
            return new GetRequest(
                pathParameters,
                instance.serverIndex
            );
        }

        public GetNullableRequest getInstance() {
            return instance;
        }

        public Get0RequestBuilder getBuilderAfterServerIndex(GetNullableRequest instance) {
            return this;
        }
    }
    public static class GetRequestBuilder implements SetterForPathParameters<Get0RequestBuilder> {
        private final GetNullableRequest instance;

        public GetRequestBuilder() {
            this.instance = new GetNullableRequest();
        }

        public GetNullableRequest getInstance() {
            return instance;
        }

        public Get0RequestBuilder getBuilderAfterPathParameters(GetNullableRequest instance) {
            return new Get0RequestBuilder(instance);
        }
    }
}
