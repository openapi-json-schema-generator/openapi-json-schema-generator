package org.openapijsonschematools.client.paths.commonparamsubdir;

import org.checkerframework.checker.nullness.qual.Nullable;
import org.openapijsonschematools.client.paths.commonparamsubdir.delete.HeaderParameters;
import org.openapijsonschematools.client.RootServerInfo;
import org.openapijsonschematools.client.paths.commonparamsubdir.delete.PathParameters;
import org.openapijsonschematools.client.paths.commonparamsubdir.delete.Parameters;
import org.openapijsonschematools.client.paths.commonparamsubdir.delete.Responses;
import org.openapijsonschematools.client.configurations.ApiConfiguration;
import org.openapijsonschematools.client.paths.CommonParamsubDir;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.HashMap;

public class Delete {

    public static class Delete1 extends CommonParamsubDir {
        private final ApiConfiguration apiConfiguration;

        public Delete1(ApiConfiguration apiConfiguration) {
            this.apiConfiguration = apiConfiguration;
        }

        public Responses.EndpointResponse delete(DeleteRequest request) {
            Map<String, List<String>> headers = apiConfiguration.getDefaultHeaders();

            if (request.headerParameters != null) {
                var headersSerializer = new Parameters.HeaderParametersSerializer();
                Map<String, List<String>> serializedHeaders = headersSerializer.serialize(request.headerParameters);
                headers.putAll(serializedHeaders);
            }

            var pathSerializer = new Parameters.PathParametersSerializer();
            String updatedPath = pathSerializer.serialize(request.pathParameters, path);
            String host = apiConfiguration.getServer(request.serverIndex).url();
        }
    }

    public static class DeleteRequest {
        public PathParameters.PathParametersMap pathParameters;
        public HeaderParameters.@Nullable HeaderParametersMap headerParameters;
        public RootServerInfo.@Nullable ServerIndex serverIndex;

        public DeleteRequest(
            PathParameters.PathParametersMap pathParameters,
            HeaderParameters.@Nullable HeaderParametersMap headerParameters,
            RootServerInfo.@Nullable ServerIndex serverIndex
        ) {
            this.pathParameters = pathParameters;
            this.headerParameters = headerParameters;
            this.serverIndex = serverIndex;
        }
    }

    public static class DeleteNullableRequest {
        public PathParameters.@Nullable PathParametersMap pathParameters;
        public HeaderParameters.@Nullable HeaderParametersMap headerParameters;
        public RootServerInfo.@Nullable ServerIndex serverIndex;
    }

    public interface SetterForHeaderParameters <T> {
        DeleteNullableRequest getInstance();
        T getBuilderAfterHeaderParameters(DeleteNullableRequest instance);
        default T headerParameters(HeaderParameters.HeaderParametersMap headerParameters) {
            var instance = getInstance();
            instance.headerParameters = headerParameters;
            return getBuilderAfterHeaderParameters(instance);
        }
    }

    public interface SetterForServerIndex <T> {
        DeleteNullableRequest getInstance();
        T getBuilderAfterServerIndex(DeleteNullableRequest instance);
        default T serverIndex(RootServerInfo.ServerIndex serverIndex) {
            var instance = getInstance();
            instance.serverIndex = serverIndex;
            return getBuilderAfterServerIndex(instance);
        }
    }

    public interface SetterForPathParameters <T> {
        DeleteNullableRequest getInstance();
        T getBuilderAfterPathParameters(DeleteNullableRequest instance);
        default T pathParameters(PathParameters.PathParametersMap pathParameters) {
            var instance = getInstance();
            instance.pathParameters = pathParameters;
            return getBuilderAfterPathParameters(instance);
        }
    }

    public static class Delete0RequestBuilder implements SetterForHeaderParameters<Delete0RequestBuilder>, SetterForServerIndex<Delete0RequestBuilder> {
        private final DeleteNullableRequest instance;

        public Delete0RequestBuilder(DeleteNullableRequest instance) {
            this.instance = instance;
        }

        public DeleteRequest build() {
            var pathParameters = instance.pathParameters;
            if (pathParameters == null) {
                throw new RuntimeException("invalid null value for required parameter");
            }
            return new DeleteRequest(
                pathParameters,
                instance.headerParameters,
                instance.serverIndex
            );
        }

        public DeleteNullableRequest getInstance() {
            return instance;
        }

        public Delete0RequestBuilder getBuilderAfterHeaderParameters(DeleteNullableRequest instance) {
            return this;
        }

        public Delete0RequestBuilder getBuilderAfterServerIndex(DeleteNullableRequest instance) {
            return this;
        }
    }
    public static class DeleteRequestBuilder implements SetterForPathParameters<Delete0RequestBuilder> {
        private final DeleteNullableRequest instance;

        public DeleteRequestBuilder() {
            this.instance = new DeleteNullableRequest();
        }

        public DeleteNullableRequest getInstance() {
            return instance;
        }

        public Delete0RequestBuilder getBuilderAfterPathParameters(DeleteNullableRequest instance) {
            return new Delete0RequestBuilder(instance);
        }
    }
}
