package org.openapijsonschematools.client.paths.fakejsonpatch;

import org.checkerframework.checker.nullness.qual.Nullable;
import org.openapijsonschematools.client.paths.fakejsonpatch.patch.FakejsonpatchPatchRequestBody;
import org.openapijsonschematools.client.RootServerInfo;
import org.openapijsonschematools.client.paths.fakejsonpatch.patch.FakejsonpatchPatchResponses;
import org.openapijsonschematools.client.apiclient.ApiClient;
import org.openapijsonschematools.client.configurations.ApiConfiguration;
import org.openapijsonschematools.client.configurations.SchemaConfiguration;
import org.openapijsonschematools.client.exceptions.ValidationException;
import org.openapijsonschematools.client.exceptions.NotImplementedException;
import org.openapijsonschematools.client.exceptions.ApiException;
import org.openapijsonschematools.client.restclient.RestClient;
import org.openapijsonschematools.client.requestbody.SerializedRequestBody;
import org.openapijsonschematools.client.paths.Fakejsonpatch;

import java.io.IOException;
import java.util.ArrayList;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.time.Duration;
import java.util.List;
import java.util.Map;

public class FakejsonpatchPatch {
    private static class PatchProvider {
        private static final String method = "patch";

        public static FakejsonpatchPatchResponses.EndpointResponse patch(
            PatchRequest request,
            ApiConfiguration apiConfiguration,
            SchemaConfiguration schemaConfiguration,
            HttpClient client
        ) throws IOException, InterruptedException, ValidationException, NotImplementedException, ApiException {
            Map<String, List<String>> headers = apiConfiguration.getDefaultHeaders();

            @Nullable SerializedRequestBody serializedRequestBody;
            HttpRequest.BodyPublisher bodyPublisher = HttpRequest.BodyPublishers.noBody();
            if (request.requestBody != null) {
                serializedRequestBody = new FakejsonpatchPatchRequestBody.FakejsonpatchPatchRequestBody1().serialize(
                    request.requestBody
                );
                var contentTypeHeaderValues = headers.getOrDefault("Content-Type", new ArrayList<>());
                contentTypeHeaderValues.add(serializedRequestBody.contentType);
                bodyPublisher = serializedRequestBody.bodyPublisher;
            }
            // TODO set this to a map if there is a query security scheme
            @Nullable Map<String, String> queryMap = null;
            String host = apiConfiguration.getServer(request.serverIndex).url();

            String url = host + Fakejsonpatch.path;
            var httpRequest = RestClient.getRequest(
                url,
                method,
                bodyPublisher,
                headers,
                request.timeout
            );
            var response = RestClient.getResponse(httpRequest, client);
            var responsesDeserializer = new FakejsonpatchPatchResponses.FakejsonpatchPatchResponses1();
            return responsesDeserializer.deserialize(response, schemaConfiguration);
        }
    }

    public interface PatchOperation {
        ApiConfiguration getApiConfiguration();
        SchemaConfiguration getSchemaConfiguration();
        HttpClient getClient();
        default FakejsonpatchPatchResponses.EndpointResponse patch(PatchRequest request) throws IOException, InterruptedException, ValidationException, NotImplementedException, ApiException {
            return PatchProvider.patch(request, getApiConfiguration(), getSchemaConfiguration(), getClient());
        }
    }

    public interface JsonPatchOperation {
        ApiConfiguration getApiConfiguration();
        SchemaConfiguration getSchemaConfiguration();
        HttpClient getClient();
        default FakejsonpatchPatchResponses.EndpointResponse jsonPatch(PatchRequest request) throws IOException, InterruptedException, ValidationException, NotImplementedException, ApiException {
            return PatchProvider.patch(request, getApiConfiguration(), getSchemaConfiguration(), getClient());
        }
    }

    public static class Patch extends ApiClient implements PatchOperation {
        public Patch(ApiConfiguration apiConfiguration, SchemaConfiguration schemaConfiguration) {
            super(apiConfiguration, schemaConfiguration);
        }
    }

    public static class PatchRequest {
        public FakejsonpatchPatchRequestBody.@Nullable SealedRequestBody requestBody;
        public RootServerInfo.@Nullable ServerIndex serverIndex;
        public @Nullable Duration timeout;
    }

    public interface SetterForRequestBody <T> {
        PatchRequest getInstance();
        T getBuilderAfterRequestBody(PatchRequest instance);
        default T requestBody(FakejsonpatchPatchRequestBody.SealedRequestBody requestBody) {
            var instance = getInstance();
            instance.requestBody = requestBody;
            return getBuilderAfterRequestBody(instance);
        }
    }

    public interface SetterForServerIndex <T> {
        PatchRequest getInstance();
        T getBuilderAfterServerIndex(PatchRequest instance);
        default T serverIndex(RootServerInfo.ServerIndex serverIndex) {
            var instance = getInstance();
            instance.serverIndex = serverIndex;
            return getBuilderAfterServerIndex(instance);
        }
    }

    public interface SetterForTimeout <T> {
        PatchRequest getInstance();
        T getBuilderAfterTimeout(PatchRequest instance);
        default T timeout(Duration timeout) {
            var instance = getInstance();
            instance.timeout = timeout;
            return getBuilderAfterTimeout(instance);
        }
    }

    public static class PatchRequestBuilder implements SetterForRequestBody<PatchRequestBuilder>, SetterForServerIndex<PatchRequestBuilder>, SetterForTimeout<PatchRequestBuilder> {
        private final PatchRequest instance;

        public PatchRequestBuilder() {
            this.instance = new PatchRequest();
        }

        public PatchRequest build() {
            return instance;
        }

        public PatchRequest getInstance() {
            return instance;
        }

        public PatchRequestBuilder getBuilderAfterRequestBody(PatchRequest instance) {
            return this;
        }

        public PatchRequestBuilder getBuilderAfterServerIndex(PatchRequest instance) {
            return this;
        }

        public PatchRequestBuilder getBuilderAfterTimeout(PatchRequest instance) {
            return this;
        }
    }
}
