/*
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
*/

package org.openapijsonschematools.client.paths.storeorder.post;

import org.openapijsonschematools.client.requestbody.RequestBodySerializer;
import org.openapijsonschematools.client.requestbody.GenericRequestBody;
import org.openapijsonschematools.client.mediatype.MediaType;
import org.openapijsonschematools.client.paths.storeorder.post.requestbody.content.applicationjson.ApplicationjsonSchema;
import org.openapijsonschematools.client.requestbody.SerializedRequestBody;

import java.util.AbstractMap;
import java.util.Map;

public class RequestBody {

    public static class ApplicationjsonMediaType extends MediaType<ApplicationjsonSchema.ApplicationjsonSchema1> {
        public ApplicationjsonMediaType() {
            super(ApplicationjsonSchema.ApplicationjsonSchema1.getInstance());
        }
    }

    public static class RequestBody1 extends RequestBodySerializer<SealedRequestBody> {
        public RequestBody1() {
            super(
                Map.ofEntries(
                    new AbstractMap.SimpleEntry<>("application/json", new ApplicationjsonMediaType())
                ),
                true
            );
        }

        public SerializedRequestBody serialize(SealedRequestBody requestBody) {
            ApplicationjsonRequestBody applicationJsonRequestBody = (ApplicationjsonRequestBody) requestBody;
            return serialize(applicationJsonRequestBody.contentType(), applicationJsonRequestBody.body().data);
        }
    }

    public static abstract sealed class SealedRequestBody permits ApplicationjsonRequestBody {}
    public static final class ApplicationjsonRequestBody extends SealedRequestBody implements GenericRequestBody<ApplicationjsonSchema.Order1Boxed> {
        private final String contentType;
        private final ApplicationjsonSchema.Order1Boxed body;
        public ApplicationjsonRequestBody(ApplicationjsonSchema.Order1Boxed body) {
            contentType = "application/json";
            this.body = body;
        }
        @Override
        public String contentType() {
            return contentType;
        }

        @Override
        public ApplicationjsonSchema.Order1Boxed body() {
            return body;
        }
    }
}
