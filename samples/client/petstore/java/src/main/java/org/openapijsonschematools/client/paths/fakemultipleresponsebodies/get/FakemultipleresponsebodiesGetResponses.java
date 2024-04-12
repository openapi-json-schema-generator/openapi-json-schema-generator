package org.openapijsonschematools.client.paths.fakemultipleresponsebodies.get;

import org.openapijsonschematools.client.paths.fakemultipleresponsebodies.get.responses.FakemultipleresponsebodiesGetCode200Response;
import org.openapijsonschematools.client.paths.fakemultipleresponsebodies.get.responses.FakemultipleresponsebodiesGetCode202Response;
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

public class FakemultipleresponsebodiesGetResponses {
    public sealed interface EndpointResponse permits EndpointFakemultipleresponsebodiesGetCode200Response, EndpointFakemultipleresponsebodiesGetCode202Response {}

    public record EndpointFakemultipleresponsebodiesGetCode200Response(
        HttpResponse<byte[]> response,
        FakemultipleresponsebodiesGetCode200Response.SealedResponseBody body,
        Void headers
    ) implements EndpointResponse, ApiResponse<FakemultipleresponsebodiesGetCode200Response.SealedResponseBody, Void>{
    }

    public record EndpointFakemultipleresponsebodiesGetCode202Response(
        HttpResponse<byte[]> response,
        FakemultipleresponsebodiesGetCode202Response.SealedResponseBody body,
        Void headers
    ) implements EndpointResponse, ApiResponse<FakemultipleresponsebodiesGetCode202Response.SealedResponseBody, Void>{
    }

    public sealed interface StatusCodeResponseDeserializer permits StatusFakemultipleresponsebodiesGetCode200ResponseDeserializer, StatusFakemultipleresponsebodiesGetCode202ResponseDeserializer {}

    public static final class StatusFakemultipleresponsebodiesGetCode200ResponseDeserializer extends FakemultipleresponsebodiesGetCode200Response.FakemultipleresponsebodiesGetCode200Response1 implements StatusCodeResponseDeserializer {
    }
    public static final class StatusFakemultipleresponsebodiesGetCode202ResponseDeserializer extends FakemultipleresponsebodiesGetCode202Response.FakemultipleresponsebodiesGetCode202Response1 implements StatusCodeResponseDeserializer {
    }

    public static final class FakemultipleresponsebodiesGetResponses1 implements ResponsesDeserializer<EndpointResponse> {
        private final Map<String, StatusCodeResponseDeserializer> statusCodeToResponseDeserializer;
        public FakemultipleresponsebodiesGetResponses1() {
            this.statusCodeToResponseDeserializer = Map.ofEntries(
                new AbstractMap.SimpleEntry<>("200", new StatusFakemultipleresponsebodiesGetCode200ResponseDeserializer()),
                new AbstractMap.SimpleEntry<>("202", new StatusFakemultipleresponsebodiesGetCode202ResponseDeserializer())
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
            if (statusCodeDeserializer instanceof StatusFakemultipleresponsebodiesGetCode200ResponseDeserializer castDeserializer) {
                var deserializedResponse = castDeserializer.deserialize(response, configuration);
                return new EndpointFakemultipleresponsebodiesGetCode200Response(response, deserializedResponse.body(), deserializedResponse.headers());
            } else {
                StatusFakemultipleresponsebodiesGetCode202ResponseDeserializer castDeserializer = (StatusFakemultipleresponsebodiesGetCode202ResponseDeserializer) statusCodeDeserializer;
                var deserializedResponse = castDeserializer.deserialize(response, configuration);
                return new EndpointFakemultipleresponsebodiesGetCode202Response(response, deserializedResponse.body(), deserializedResponse.headers());
            }
        }
    }
}
