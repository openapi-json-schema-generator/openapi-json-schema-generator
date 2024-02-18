package org.openapijsonschematools.client.response;

import java.net.http.HttpResponse;

public class DeserializedApiResponse<SealedBodyOutputClass, HeaderOutputClass> implements ApiResponse<SealedBodyOutputClass, HeaderOutputClass> {
    private final HttpResponse<byte[]> response;
    private final SealedBodyOutputClass body;
    private final HeaderOutputClass headers;

    public DeserializedApiResponse(HttpResponse<byte[]> response, SealedBodyOutputClass body, HeaderOutputClass headers) {
        this.response = response;
        this.body = body;
        this.headers = headers;
    }

    @Override
    public HttpResponse<byte[]> response() {
        return response;
    }

    @Override
    public SealedBodyOutputClass body() {
        return body;
    }

    @Override
    public HeaderOutputClass headers() {
        return headers;
    }
}