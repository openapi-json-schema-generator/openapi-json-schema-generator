package org.openapijsonschematools.client.paths.fakebodywithqueryparams;

import org.checkerframework.checker.nullness.qual.Nullable;
import org.openapijsonschematools.client.RootServerInfo;
import org.openapijsonschematools.client.paths.fakebodywithqueryparams.put.FakebodywithqueryparamsPutRequestBody;
import org.openapijsonschematools.client.paths.fakebodywithqueryparams.put.FakebodywithqueryparamsPutQueryParameters;
import org.openapijsonschematools.client.paths.fakebodywithqueryparams.put.Parameters;
import org.openapijsonschematools.client.paths.fakebodywithqueryparams.put.FakebodywithqueryparamsPutResponses;
import org.openapijsonschematools.client.apiclient.ApiClient;
import org.openapijsonschematools.client.configurations.ApiConfiguration;
import org.openapijsonschematools.client.configurations.SchemaConfiguration;
import org.openapijsonschematools.client.exceptions.ValidationException;
import org.openapijsonschematools.client.exceptions.NotImplementedException;
import org.openapijsonschematools.client.exceptions.ApiException;
import org.openapijsonschematools.client.restclient.RestClient;
import org.openapijsonschematools.client.requestbody.SerializedRequestBody;
import org.openapijsonschematools.client.paths.Fakebodywithqueryparams;

import java.io.IOException;
import java.util.ArrayList;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.time.Duration;
import java.util.List;
import java.util.Map;

public class FakebodywithqueryparamsPut {
    private static class PutProvider {
        private static final String method = "put";

        public static FakebodywithqueryparamsPutResponses.EndpointResponse put(
            PutRequest request,
            ApiConfiguration apiConfiguration,
            SchemaConfiguration schemaConfiguration,
            HttpClient client
        ) throws IOException, InterruptedException, ValidationException, NotImplementedException, ApiException {
            Map<String, List<String>> headers = apiConfiguration.getDefaultHeaders();

            SerializedRequestBody serializedRequestBody = new FakebodywithqueryparamsPutRequestBody.FakebodywithqueryparamsPutRequestBody1().serialize(
                request.requestBody
            );
            var contentTypeHeaderValues = headers.getOrDefault("Content-Type", new ArrayList<>());
            contentTypeHeaderValues.add(serializedRequestBody.contentType);
            HttpRequest.BodyPublisher bodyPublisher = serializedRequestBody.bodyPublisher;

            var querySerializer = new Parameters.QueryParametersSerializer();
            @Nullable Map<String, String> queryMap = querySerializer.getQueryMap(request.queryParameters);
            String host = apiConfiguration.getServer(request.serverIndex).url();

            String url = host + Fakebodywithqueryparams.path;
            if (queryMap != null) {
                url = url + querySerializer.serialize(queryMap);
            }
            var httpRequest = RestClient.getRequest(
                url,
                method,
                bodyPublisher,
                headers,
                request.timeout
            );
            var response = RestClient.getResponse(httpRequest, client);
            var responsesDeserializer = new FakebodywithqueryparamsPutResponses.FakebodywithqueryparamsPutResponses1();
            return responsesDeserializer.deserialize(response, schemaConfiguration);
        }
    }

    public interface PutOperation {
        ApiConfiguration getApiConfiguration();
        SchemaConfiguration getSchemaConfiguration();
        HttpClient getClient();
        default FakebodywithqueryparamsPutResponses.EndpointResponse put(PutRequest request) throws IOException, InterruptedException, ValidationException, NotImplementedException, ApiException {
            return PutProvider.put(request, getApiConfiguration(), getSchemaConfiguration(), getClient());
        }
    }

    public interface BodyWithQueryParamsOperation {
        ApiConfiguration getApiConfiguration();
        SchemaConfiguration getSchemaConfiguration();
        HttpClient getClient();
        default FakebodywithqueryparamsPutResponses.EndpointResponse bodyWithQueryParams(PutRequest request) throws IOException, InterruptedException, ValidationException, NotImplementedException, ApiException {
            return PutProvider.put(request, getApiConfiguration(), getSchemaConfiguration(), getClient());
        }
    }

    public static class Put extends ApiClient implements PutOperation {
        public Put(ApiConfiguration apiConfiguration, SchemaConfiguration schemaConfiguration) {
            super(apiConfiguration, schemaConfiguration);
        }
    }

    public static class PutRequest {
        public FakebodywithqueryparamsPutRequestBody.SealedRequestBody requestBody;
        public FakebodywithqueryparamsPutQueryParameters.QueryParametersMap queryParameters;
        public RootServerInfo.@Nullable ServerIndex serverIndex;
        public @Nullable Duration timeout;

        public PutRequest(
            FakebodywithqueryparamsPutRequestBody.SealedRequestBody requestBody,
            FakebodywithqueryparamsPutQueryParameters.QueryParametersMap queryParameters,
            RootServerInfo.@Nullable ServerIndex serverIndex,
            @Nullable Duration timeout
        ) {
            this.requestBody = requestBody;
            this.queryParameters = queryParameters;
            this.serverIndex = serverIndex;
            this.timeout = timeout;
        }
    }

    public static class PutNullableRequest {
        public FakebodywithqueryparamsPutRequestBody.@Nullable SealedRequestBody requestBody;
        public FakebodywithqueryparamsPutQueryParameters.@Nullable QueryParametersMap queryParameters;
        public RootServerInfo.@Nullable ServerIndex serverIndex;
        public @Nullable Duration timeout;
    }

    public interface SetterForServerIndex <T> {
        PutNullableRequest getInstance();
        T getBuilderAfterServerIndex(PutNullableRequest instance);
        default T serverIndex(RootServerInfo.ServerIndex serverIndex) {
            var instance = getInstance();
            instance.serverIndex = serverIndex;
            return getBuilderAfterServerIndex(instance);
        }
    }

    public interface SetterForTimeout <T> {
        PutNullableRequest getInstance();
        T getBuilderAfterTimeout(PutNullableRequest instance);
        default T timeout(Duration timeout) {
            var instance = getInstance();
            instance.timeout = timeout;
            return getBuilderAfterTimeout(instance);
        }
    }

    public interface SetterForRequestBody <T> {
        PutNullableRequest getInstance();
        T getBuilderAfterRequestBody(PutNullableRequest instance);
        default T requestBody(FakebodywithqueryparamsPutRequestBody.SealedRequestBody requestBody) {
            var instance = getInstance();
            instance.requestBody = requestBody;
            return getBuilderAfterRequestBody(instance);
        }
    }

    public interface SetterForQueryParameters <T> {
        PutNullableRequest getInstance();
        T getBuilderAfterQueryParameters(PutNullableRequest instance);
        default T queryParameters(FakebodywithqueryparamsPutQueryParameters.QueryParametersMap queryParameters) {
            var instance = getInstance();
            instance.queryParameters = queryParameters;
            return getBuilderAfterQueryParameters(instance);
        }
    }

    public static class Put00RequestBuilder implements SetterForServerIndex<Put00RequestBuilder>, SetterForTimeout<Put00RequestBuilder> {
        private final PutNullableRequest instance;

        public Put00RequestBuilder(PutNullableRequest instance) {
            this.instance = instance;
        }

        public PutRequest build() {
            var requestBody = instance.requestBody;
            if (requestBody == null) {
                throw new RuntimeException("invalid null value for required parameter");
            }
            var queryParameters = instance.queryParameters;
            if (queryParameters == null) {
                throw new RuntimeException("invalid null value for required parameter");
            }
            return new PutRequest(
                requestBody,
                queryParameters,
                instance.serverIndex,
                instance.timeout
            );
        }

        public PutNullableRequest getInstance() {
            return instance;
        }

        public Put00RequestBuilder getBuilderAfterServerIndex(PutNullableRequest instance) {
            return this;
        }

        public Put00RequestBuilder getBuilderAfterTimeout(PutNullableRequest instance) {
            return this;
        }
    }
    public static class Put01RequestBuilder implements SetterForQueryParameters<Put00RequestBuilder> {
        private final PutNullableRequest instance;

        public Put01RequestBuilder(PutNullableRequest instance) {
            this.instance = instance;
        }

        public PutNullableRequest getInstance() {
            return instance;
        }

        public Put00RequestBuilder getBuilderAfterQueryParameters(PutNullableRequest instance) {
            return new Put00RequestBuilder(instance);
        }
    }
    public static class Put10RequestBuilder implements SetterForRequestBody<Put00RequestBuilder> {
        private final PutNullableRequest instance;

        public Put10RequestBuilder(PutNullableRequest instance) {
            this.instance = instance;
        }

        public PutNullableRequest getInstance() {
            return instance;
        }

        public Put00RequestBuilder getBuilderAfterRequestBody(PutNullableRequest instance) {
            return new Put00RequestBuilder(instance);
        }
    }
    public static class PutRequestBuilder implements SetterForRequestBody<Put01RequestBuilder>, SetterForQueryParameters<Put10RequestBuilder> {
        private final PutNullableRequest instance;

        public PutRequestBuilder() {
            this.instance = new PutNullableRequest();
        }

        public PutNullableRequest getInstance() {
            return instance;
        }

        public Put01RequestBuilder getBuilderAfterRequestBody(PutNullableRequest instance) {
            return new Put01RequestBuilder(instance);
        }

        public Put10RequestBuilder getBuilderAfterQueryParameters(PutNullableRequest instance) {
            return new Put10RequestBuilder(instance);
        }
    }
}
