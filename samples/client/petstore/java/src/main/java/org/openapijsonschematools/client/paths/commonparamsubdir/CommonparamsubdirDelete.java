package org.openapijsonschematools.client.paths.commonparamsubdir;

import org.checkerframework.checker.nullness.qual.Nullable;
import org.openapijsonschematools.client.paths.commonparamsubdir.delete.CommonparamsubdirDeleteHeaderParameters;
import org.openapijsonschematools.client.RootServerInfo;
import org.openapijsonschematools.client.paths.commonparamsubdir.delete.CommonparamsubdirDeletePathParameters;
import org.openapijsonschematools.client.paths.commonparamsubdir.delete.Parameters;
import org.openapijsonschematools.client.paths.commonparamsubdir.delete.CommonparamsubdirDeleteResponses;
import org.openapijsonschematools.client.apiclient.ApiClient;
import org.openapijsonschematools.client.configurations.ApiConfiguration;
import org.openapijsonschematools.client.configurations.SchemaConfiguration;
import org.openapijsonschematools.client.exceptions.ValidationException;
import org.openapijsonschematools.client.exceptions.NotImplementedException;
import org.openapijsonschematools.client.exceptions.ApiException;
import org.openapijsonschematools.client.restclient.RestClient;
import org.openapijsonschematools.client.paths.Commonparamsubdir;

import java.io.IOException;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.time.Duration;
import java.util.List;
import java.util.Map;

public class CommonparamsubdirDelete {
    private static class DeleteProvider {
        private static final String method = "delete";

        public static CommonparamsubdirDeleteResponses.EndpointResponse delete(
            DeleteRequest request,
            ApiConfiguration apiConfiguration,
            SchemaConfiguration schemaConfiguration,
            HttpClient client
        ) throws IOException, InterruptedException, ValidationException, NotImplementedException, ApiException {
            Map<String, List<String>> headers = apiConfiguration.getDefaultHeaders();
            HttpRequest.BodyPublisher bodyPublisher = HttpRequest.BodyPublishers.noBody();

            if (request.headerParameters != null) {
                var headersSerializer = new Parameters.HeaderParametersSerializer();
                Map<String, List<String>> serializedHeaders = headersSerializer.serialize(request.headerParameters);
                headers.putAll(serializedHeaders);
            }

            var pathSerializer = new Parameters.PathParametersSerializer();
            String updatedPath = pathSerializer.serialize(request.pathParameters, Commonparamsubdir.path);
            // TODO set this to a map if there is a query security scheme
            @Nullable Map<String, String> queryMap = null;
            String host = apiConfiguration.getServer(request.serverIndex).url();

            String url = host + updatedPath;
            var httpRequest = RestClient.getRequest(
                url,
                method,
                bodyPublisher,
                headers,
                request.timeout
            );
            var response = RestClient.getResponse(httpRequest, client);
            var responsesDeserializer = new CommonparamsubdirDeleteResponses.CommonparamsubdirDeleteResponses1();
            return responsesDeserializer.deserialize(response, schemaConfiguration);
        }
    }

    public interface DeleteOperation {
        ApiConfiguration getApiConfiguration();
        SchemaConfiguration getSchemaConfiguration();
        HttpClient getClient();
        default CommonparamsubdirDeleteResponses.EndpointResponse delete(DeleteRequest request) throws IOException, InterruptedException, ValidationException, NotImplementedException, ApiException {
            return DeleteProvider.delete(request, getApiConfiguration(), getSchemaConfiguration(), getClient());
        }
    }

    public interface DeleteCommonParamOperation {
        ApiConfiguration getApiConfiguration();
        SchemaConfiguration getSchemaConfiguration();
        HttpClient getClient();
        default CommonparamsubdirDeleteResponses.EndpointResponse deleteCommonParam(DeleteRequest request) throws IOException, InterruptedException, ValidationException, NotImplementedException, ApiException {
            return DeleteProvider.delete(request, getApiConfiguration(), getSchemaConfiguration(), getClient());
        }
    }

    public static class Delete extends ApiClient implements DeleteOperation {
        public Delete(ApiConfiguration apiConfiguration, SchemaConfiguration schemaConfiguration) {
            super(apiConfiguration, schemaConfiguration);
        }
    }

    public static class DeleteRequest {
        public CommonparamsubdirDeletePathParameters.CommonparamsubdirDeletePathParametersMap pathParameters;
        public CommonparamsubdirDeleteHeaderParameters.@Nullable CommonparamsubdirDeleteHeaderParametersMap headerParameters;
        public RootServerInfo.@Nullable ServerIndex serverIndex;
        public @Nullable Duration timeout;

        public DeleteRequest(
            CommonparamsubdirDeletePathParameters.CommonparamsubdirDeletePathParametersMap pathParameters,
            CommonparamsubdirDeleteHeaderParameters.@Nullable CommonparamsubdirDeleteHeaderParametersMap headerParameters,
            RootServerInfo.@Nullable ServerIndex serverIndex,
            @Nullable Duration timeout
        ) {
            this.pathParameters = pathParameters;
            this.headerParameters = headerParameters;
            this.serverIndex = serverIndex;
            this.timeout = timeout;
        }
    }

    public static class DeleteNullableRequest {
        public CommonparamsubdirDeletePathParameters.@Nullable CommonparamsubdirDeletePathParametersMap pathParameters;
        public CommonparamsubdirDeleteHeaderParameters.@Nullable CommonparamsubdirDeleteHeaderParametersMap headerParameters;
        public RootServerInfo.@Nullable ServerIndex serverIndex;
        public @Nullable Duration timeout;
    }

    public interface SetterForHeaderParameters <T> {
        DeleteNullableRequest getInstance();
        T getBuilderAfterHeaderParameters(DeleteNullableRequest instance);
        default T headerParameters(CommonparamsubdirDeleteHeaderParameters.CommonparamsubdirDeleteHeaderParametersMap headerParameters) {
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

    public interface SetterForTimeout <T> {
        DeleteNullableRequest getInstance();
        T getBuilderAfterTimeout(DeleteNullableRequest instance);
        default T timeout(Duration timeout) {
            var instance = getInstance();
            instance.timeout = timeout;
            return getBuilderAfterTimeout(instance);
        }
    }

    public interface SetterForPathParameters <T> {
        DeleteNullableRequest getInstance();
        T getBuilderAfterPathParameters(DeleteNullableRequest instance);
        default T pathParameters(CommonparamsubdirDeletePathParameters.CommonparamsubdirDeletePathParametersMap pathParameters) {
            var instance = getInstance();
            instance.pathParameters = pathParameters;
            return getBuilderAfterPathParameters(instance);
        }
    }

    public static class Delete0RequestBuilder implements SetterForHeaderParameters<Delete0RequestBuilder>, SetterForServerIndex<Delete0RequestBuilder>, SetterForTimeout<Delete0RequestBuilder> {
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
                instance.serverIndex,
                instance.timeout
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

        public Delete0RequestBuilder getBuilderAfterTimeout(DeleteNullableRequest instance) {
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
