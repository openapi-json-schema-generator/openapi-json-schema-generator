package org.openapijsonschematools.client.paths.userusername;

import org.checkerframework.checker.nullness.qual.Nullable;
import org.openapijsonschematools.client.RootServerInfo;
import org.openapijsonschematools.client.paths.userusername.put.UserusernamePutRequestBody;
import org.openapijsonschematools.client.paths.userusername.put.UserusernamePutPathParameters;
import org.openapijsonschematools.client.paths.userusername.put.Parameters;
import org.openapijsonschematools.client.paths.userusername.put.UserusernamePutResponses;
import org.openapijsonschematools.client.apiclient.ApiClient;
import org.openapijsonschematools.client.configurations.ApiConfiguration;
import org.openapijsonschematools.client.configurations.SchemaConfiguration;
import org.openapijsonschematools.client.exceptions.ValidationException;
import org.openapijsonschematools.client.exceptions.NotImplementedException;
import org.openapijsonschematools.client.exceptions.ApiException;
import org.openapijsonschematools.client.restclient.RestClient;
import org.openapijsonschematools.client.requestbody.SerializedRequestBody;
import org.openapijsonschematools.client.paths.Userusername;

import java.io.IOException;
import java.util.ArrayList;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.time.Duration;
import java.util.List;
import java.util.Map;

public class UserusernamePut {
    private static class PutProvider {
        private static final String method = "put";

        public static Void put(
            PutRequest request,
            ApiConfiguration apiConfiguration,
            SchemaConfiguration schemaConfiguration,
            HttpClient client
        ) throws IOException, InterruptedException, ValidationException, NotImplementedException, ApiException {
            Map<String, List<String>> headers = apiConfiguration.getDefaultHeaders();

            SerializedRequestBody serializedRequestBody = new UserusernamePutRequestBody.UserusernamePutRequestBody1().serialize(
                request.requestBody
            );
            var contentTypeHeaderValues = headers.getOrDefault("Content-Type", new ArrayList<>());
            contentTypeHeaderValues.add(serializedRequestBody.contentType);
            HttpRequest.BodyPublisher bodyPublisher = serializedRequestBody.bodyPublisher;

            var pathSerializer = new Parameters.PathParametersSerializer();
            String updatedPath = pathSerializer.serialize(request.pathParameters, Userusername.path);
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
            return (Void) null;
        }
    }

    public interface PutOperation {
        ApiConfiguration getApiConfiguration();
        SchemaConfiguration getSchemaConfiguration();
        HttpClient getClient();
        default Void put(PutRequest request) throws IOException, InterruptedException, ValidationException, NotImplementedException, ApiException {
            return PutProvider.put(request, getApiConfiguration(), getSchemaConfiguration(), getClient());
        }
    }

    public interface UpdateUserOperation {
        ApiConfiguration getApiConfiguration();
        SchemaConfiguration getSchemaConfiguration();
        HttpClient getClient();
        default Void updateUser(PutRequest request) throws IOException, InterruptedException, ValidationException, NotImplementedException, ApiException {
            return PutProvider.put(request, getApiConfiguration(), getSchemaConfiguration(), getClient());
        }
    }

    public static class Put extends ApiClient implements PutOperation {
        public Put(ApiConfiguration apiConfiguration, SchemaConfiguration schemaConfiguration) {
            super(apiConfiguration, schemaConfiguration);
        }
    }

    public static class PutRequest {
        public UserusernamePutRequestBody.SealedRequestBody requestBody;
        public UserusernamePutPathParameters.UserusernamePutPathParametersMap pathParameters;
        public RootServerInfo.@Nullable ServerIndex serverIndex;
        public @Nullable Duration timeout;

        public PutRequest(
            UserusernamePutRequestBody.SealedRequestBody requestBody,
            UserusernamePutPathParameters.UserusernamePutPathParametersMap pathParameters,
            RootServerInfo.@Nullable ServerIndex serverIndex,
            @Nullable Duration timeout
        ) {
            this.requestBody = requestBody;
            this.pathParameters = pathParameters;
            this.serverIndex = serverIndex;
            this.timeout = timeout;
        }
    }

    public static class PutNullableRequest {
        public UserusernamePutRequestBody.@Nullable SealedRequestBody requestBody;
        public UserusernamePutPathParameters.@Nullable UserusernamePutPathParametersMap pathParameters;
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
        default T requestBody(UserusernamePutRequestBody.SealedRequestBody requestBody) {
            var instance = getInstance();
            instance.requestBody = requestBody;
            return getBuilderAfterRequestBody(instance);
        }
    }

    public interface SetterForPathParameters <T> {
        PutNullableRequest getInstance();
        T getBuilderAfterPathParameters(PutNullableRequest instance);
        default T pathParameters(UserusernamePutPathParameters.UserusernamePutPathParametersMap pathParameters) {
            var instance = getInstance();
            instance.pathParameters = pathParameters;
            return getBuilderAfterPathParameters(instance);
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
            var pathParameters = instance.pathParameters;
            if (pathParameters == null) {
                throw new RuntimeException("invalid null value for required parameter");
            }
            return new PutRequest(
                requestBody,
                pathParameters,
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
    public static class Put01RequestBuilder implements SetterForPathParameters<Put00RequestBuilder> {
        private final PutNullableRequest instance;

        public Put01RequestBuilder(PutNullableRequest instance) {
            this.instance = instance;
        }

        public PutNullableRequest getInstance() {
            return instance;
        }

        public Put00RequestBuilder getBuilderAfterPathParameters(PutNullableRequest instance) {
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
    public static class PutRequestBuilder implements SetterForRequestBody<Put01RequestBuilder>, SetterForPathParameters<Put10RequestBuilder> {
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

        public Put10RequestBuilder getBuilderAfterPathParameters(PutNullableRequest instance) {
            return new Put10RequestBuilder(instance);
        }
    }
}
