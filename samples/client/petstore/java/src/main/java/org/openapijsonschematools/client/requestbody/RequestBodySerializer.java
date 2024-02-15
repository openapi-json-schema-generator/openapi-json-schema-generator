package org.openapijsonschematools.client.requestbody;

import org.openapijsonschematools.client.mediatype.MediaType;

import java.net.http.HttpRequest;
import org.checkerframework.checker.nullness.qual.Nullable;

import java.util.Map;

public abstract class RequestBodySerializer<T> {
    /*
    * Describes a single request body
    * content: content_type to MediaType schema info
    * each implementing class must implement RequestBody makeForApplicationJson(SealedOutput)
    * each the returned RequestBody must have a protected constructor to insure that
    * it is created by makeForApplicationJson
    * or make one enum for each content type, then implement make(SpecificContentType, SealedOutput)
    * requires one enum per contentType
    * abstract T make(String contentType, @Nullable Object body)
    * logic: MediaType<?> get(ContentTypeEnum contentType)
    * .makeRequestBody(SealedOutput)
    */
    public final Map<String, MediaType<?>> content;
    public final boolean required;

    public RequestBodySerializer(Map<String, MediaType<?>> content, boolean required) {
        this.content = content;
        this.required = required;
    }

    protected SerializedRequestBody serialize(String contentType, @Nullable Object body) {
        // todo add implementation here
        return new SerializedRequestBody(
            contentType,
            new HttpRequest.BodyPublishers.ofString("blah")
        );
    }

    public abstract SerializedRequestBody serialize(T requestBody);
}