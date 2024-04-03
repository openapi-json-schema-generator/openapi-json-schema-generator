package org.openapijsonschematools.client.paths.fakemultipleresponsebodies.get;

import org.openapijsonschematools.client.paths.fakemultipleresponsebodies.get.responses.Code200Response;
import org.openapijsonschematools.client.paths.fakemultipleresponsebodies.get.responses.Code202Response;
import org.openapijsonschematools.client.exceptions.ApiException;
import org.openapijsonschematools.client.exceptions.InvalidTypeException;
import org.openapijsonschematools.client.exceptions.NotImplementedException;
import org.openapijsonschematools.client.exceptions.ValidationException;
import org.openapijsonschematools.client.response.ApiResponse;
import org.openapijsonschematools.client.response.ResponsesDeserializer;
import org.openapijsonschematools.client.configurations.SchemaConfiguration;
import org.checkerframework.checker.nullness.qual.Nullable;

import java.net.http.HttpResponse;
import java.util.Map;
import java.util.AbstractMap;

public class Responses {
    public sealed interface EndpointResponse permits EndpointCode200Response, EndpointCode202Response {}

    public record EndpointCode200Response(
        HttpResponse<byte[]> response,
        Code200Response.SealedResponseBody body,
        Void headers
    ) implements EndpointResponse, ApiResponse<Code200Response.SealedResponseBody, Void>{
    }

    public record EndpointCode202Response(
        HttpResponse<byte[]> response,
        Code202Response.SealedResponseBody body,
        Void headers
    ) implements EndpointResponse, ApiResponse<Code202Response.SealedResponseBody, Void>{
    }

    public sealed interface StatusCodeResponseDeserializer permits StatusCode200ResponseDeserializer, StatusCode202ResponseDeserializer {}

    public static final class StatusCode200ResponseDeserializer extends Code200Response.Code200Response1 implements StatusCodeResponseDeserializer {
    }
    public static final class StatusCode202ResponseDeserializer extends Code202Response.Code202Response1 implements StatusCodeResponseDeserializer {
    }

    public static final class Responses1 implements ResponsesDeserializer<EndpointResponse> {
        private final Map<String, StatusCodeResponseDeserializer> statusCodeToResponseDeserializer;
        public Responses1() {
            this.statusCodeToResponseDeserializer = Map.ofEntries(
                new AbstractMap.SimpleEntry<>("200", new StatusCode200ResponseDeserializer()),
                new AbstractMap.SimpleEntry<>("202", new StatusCode202ResponseDeserializer())
            );
        }

        public EndpointResponse deserialize(HttpResponse<byte[]> response, SchemaConfiguration configuration) throws InvalidTypeException, ValidationException, NotImplementedException, ApiException {
            String statusCode = String.valueOf(response.statusCode());
            @Nullable StatusCodeResponseDeserializer statusCodeDeserializer = statusCodeToResponseDeserializer.get(statusCode);
            if (statusCodeDeserializer == null) {
                throw new ApiException(
                    "Invalid response statusCode="+statusCode+" has no response defined in the openapi document",
                    response
                );
            }
            if (statusCodeDeserializer instanceof StatusCode200ResponseDeserializer castDeserializer) {
                var deserializedResponse = castDeserializer.deserialize(response, configuration);
                return new EndpointCode200Response(response, deserializedResponse.body(), deserializedResponse.headers());
            } else {
                StatusCode202ResponseDeserializer castDeserializer = (StatusCode202ResponseDeserializer) statusCodeDeserializer;
                var deserializedResponse = castDeserializer.deserialize(response, configuration);
                return new EndpointCode202Response(response, deserializedResponse.body(), deserializedResponse.headers());
            }
        }
    }
}
