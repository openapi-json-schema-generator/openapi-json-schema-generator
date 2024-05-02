package org.openapijsonschematools.client.paths.fakerefsarraymodel.post;

import org.openapijsonschematools.client.paths.fakerefsarraymodel.post.responses.FakerefsarraymodelPostCode200Response;
import org.openapijsonschematools.client.exceptions.ApiException;
import org.openapijsonschematools.client.exceptions.NotImplementedException;
import org.openapijsonschematools.client.exceptions.ValidationException;
import org.openapijsonschematools.client.response.ApiResponse;
import org.openapijsonschematools.client.response.ResponsesDeserializer;
import org.openapijsonschematools.client.configurations.SchemaConfiguration;
import org.checkerframework.checker.nullness.qual.Nullable;

import java.net.http.HttpResponse;
import java.util.Map;
import java.util.AbstractMap;

public class FakerefsarraymodelPostResponses {
    public sealed interface EndpointResponse permits EndpointFakerefsarraymodelPostCode200Response {}

    public record EndpointFakerefsarraymodelPostCode200Response(
        HttpResponse<byte[]> response,
        FakerefsarraymodelPostCode200Response.SealedResponseBody body,
        Nothing? headers
    ) implements EndpointResponse, ApiResponse<FakerefsarraymodelPostCode200Response.SealedResponseBody, Nothing?>{
    }

    public sealed interface StatusCodeResponseDeserializer permits StatusFakerefsarraymodelPostCode200ResponseDeserializer {}

    public static final class StatusFakerefsarraymodelPostCode200ResponseDeserializer extends FakerefsarraymodelPostCode200Response.FakerefsarraymodelPostCode200Response1 implements StatusCodeResponseDeserializer {
    }

    public static final class FakerefsarraymodelPostResponses1 implements ResponsesDeserializer<EndpointResponse> {
        private final Map<String, StatusCodeResponseDeserializer> statusCodeToResponseDeserializer;
        public FakerefsarraymodelPostResponses1() {
            this.statusCodeToResponseDeserializer = Map.ofEntries(
                new AbstractMap.SimpleEntry<>("200", new StatusFakerefsarraymodelPostCode200ResponseDeserializer())
            );
        }

        public EndpointResponse deserialize(HttpResponse<byte[]> response, SchemaConfiguration configuration) throws ValidationException, NotImplementedException, ApiException {
            String statusCode = String.valueOf(response.statusCode());
            @Nullable StatusCodeResponseDeserializer statusCodeDeserializer = statusCodeToResponseDeserializer.get(statusCode);
            if (statusCodeDeserializer == null) {
                throw new ApiException(
                    "Invalid response statusCode="+statusCode+" has no response defined in the openapi document",
                    response
                );
            }
            StatusFakerefsarraymodelPostCode200ResponseDeserializer castDeserializer = (StatusFakerefsarraymodelPostCode200ResponseDeserializer) statusCodeDeserializer;
            var deserializedResponse = castDeserializer.deserialize(response, configuration);
            return new EndpointFakerefsarraymodelPostCode200Response(response, deserializedResponse.body(), deserializedResponse.headers());
        }
    }
}
