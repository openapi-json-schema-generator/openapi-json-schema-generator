/*
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
*/

package org.openapijsonschematools.client.components.requestbodies;

import org.openapijsonschematools.client.requestbody.RequestBodySerializer;
import org.openapijsonschematools.client.requestbody.RequestBody;
import org.openapijsonschematools.client.mediatype.MediaType;
import org.openapijsonschematools.client.paths.fakerefscomposedoneofnumberwithvalidations.post.requestbody.content.applicationjson.ApplicationjsonSchema;

import java.util.AbstractMap;
import java.util.Map;

public class RequestBody extends RequestBodySerializer {

    public static class ApplicationjsonMediaType extends MediaType<ApplicationjsonSchema.ApplicationjsonSchema1> {
        public ApplicationjsonMediaType() {
            super(ApplicationjsonSchema.ApplicationjsonSchema1.getInstance());
        }
    }

    public RequestBody() {
        super(
            Map.ofEntries(
                new AbstractMap.SimpleEntry<>("application/json", new ApplicationjsonMediaType())
            ),
            false
        );
    }

    public static abstract sealed class RequestBodyRequestBody permits RequestBodyApplicationjsonRequestBody {}
    public static final class RequestBodyApplicationjsonRequestBody extends RequestBodyRequestBody implements RequestBody<ApplicationjsonSchema.ComposedOneOfDifferentTypes1Boxed> {
        private final String contentType;
        private final ApplicationjsonSchema.ComposedOneOfDifferentTypes1Boxed body;
        public RequestBodyApplicationjsonRequestBody(ApplicationjsonSchema.ComposedOneOfDifferentTypes1Boxed body) {
            contentType = "application/json";
            this.body = body;
        }
        @Override
        public String contentType() {
            return contentType;
        }

        @Override
        public ApplicationjsonSchema.ComposedOneOfDifferentTypes1Boxed body() {
            return body;
        }
    }
}
