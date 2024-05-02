package org.openapijsonschematools.client.paths.commonparamsubdir.post;

import org.openapijsonschematools.client.paths.commonparamsubdir.post.responses.CommonparamsubdirPostCode200Response;
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

public class CommonparamsubdirPostResponses {
    public sealed interface EndpointResponse permits EndpointCommonparamsubdirPostCode200Response {}

    public record EndpointCommonparamsubdirPostCode200Response(
        HttpResponse<byte[]> response,
        Nothing? body,
        Nothing? headers
    ) implements EndpointResponse, ApiResponse<Nothing?, Nothing?>{
    }

    public sealed interface StatusCodeResponseDeserializer permits StatusCommonparamsubdirPostCode200ResponseDeserializer {}

    public static final class StatusCommonparamsubdirPostCode200ResponseDeserializer extends CommonparamsubdirPostCode200Response.CommonparamsubdirPostCode200Response1 implements StatusCodeResponseDeserializer {
    }

    public static final class CommonparamsubdirPostResponses1 implements ResponsesDeserializer<EndpointResponse> {
        private final Map<String, StatusCodeResponseDeserializer> statusCodeToResponseDeserializer;
        public CommonparamsubdirPostResponses1() {
            this.statusCodeToResponseDeserializer = Map.ofEntries(
                new AbstractMap.SimpleEntry<>("200", new StatusCommonparamsubdirPostCode200ResponseDeserializer())
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
            StatusCommonparamsubdirPostCode200ResponseDeserializer castDeserializer = (StatusCommonparamsubdirPostCode200ResponseDeserializer) statusCodeDeserializer;
            var deserializedResponse = castDeserializer.deserialize(response, configuration);
            return new EndpointCommonparamsubdirPostCode200Response(response, deserializedResponse.body(), deserializedResponse.headers());
        }
    }
}
