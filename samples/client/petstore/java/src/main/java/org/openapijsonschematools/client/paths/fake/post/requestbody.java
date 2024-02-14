/*
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
*/

package org.openapijsonschematools.client.components.requestbodies;

import org.openapijsonschematools.client.requestbody.RequestBodySerializer;
import org.openapijsonschematools.client.requestbody.RequestBody;
import org.openapijsonschematools.client.mediatype.MediaType;
import org.openapijsonschematools.client.paths.fake.post.requestbody.content.applicationxwwwformurlencoded.ApplicationxwwwformurlencodedSchema;

import java.util.AbstractMap;
import java.util.Map;

public class RequestBody extends RequestBodySerializer {

    public static class ApplicationxwwwformurlencodedMediaType extends MediaType<ApplicationxwwwformurlencodedSchema.ApplicationxwwwformurlencodedSchema1> {
        public ApplicationxwwwformurlencodedMediaType() {
            super(ApplicationxwwwformurlencodedSchema.ApplicationxwwwformurlencodedSchema1.getInstance());
        }
    }

    public RequestBody() {
        super(
            Map.ofEntries(
                new AbstractMap.SimpleEntry<>("application/x-www-form-urlencoded", new ApplicationxwwwformurlencodedMediaType())
            ),
            false
        );
    }

    public static abstract sealed class RequestBodyRequestBody permits RequestBodyApplicationxwwwformurlencodedRequestBody {}
    public static final class RequestBodyApplicationxwwwformurlencodedRequestBody extends RequestBodyRequestBody implements RequestBody<ApplicationxwwwformurlencodedSchema.ApplicationxwwwformurlencodedSchema1Boxed> {
        private final String contentType;
        private final ApplicationxwwwformurlencodedSchema.ApplicationxwwwformurlencodedSchema1Boxed body;
        public RequestBodyApplicationxwwwformurlencodedRequestBody(ApplicationxwwwformurlencodedSchema.ApplicationxwwwformurlencodedSchema1Boxed body) {
            contentType = "application/x-www-form-urlencoded";
            this.body = body;
        }
        @Override
        public String contentType() {
            return contentType;
        }

        @Override
        public ApplicationxwwwformurlencodedSchema.ApplicationxwwwformurlencodedSchema1Boxed body() {
            return body;
        }
    }
}
