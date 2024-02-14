/*
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
*/

package org.openapijsonschematools.client.components.requestbodies;

import org.openapijsonschematools.client.requestbody.RequestBodySerializer;
import org.openapijsonschematools.client.requestbody.RequestBody;
import org.openapijsonschematools.client.mediatype.MediaType;
import org.openapijsonschematools.client.paths.fakeinlinecomposition.post.requestbody.content.applicationjson.ApplicationjsonSchema;
import org.openapijsonschematools.client.paths.fakeinlinecomposition.post.requestbody.content.multipartformdata.MultipartformdataSchema;

import java.util.AbstractMap;
import java.util.Map;

public class RequestBody extends RequestBodySerializer {

    public static class ApplicationjsonMediaType extends MediaType<ApplicationjsonSchema.ApplicationjsonSchema1> {
        public ApplicationjsonMediaType() {
            super(ApplicationjsonSchema.ApplicationjsonSchema1.getInstance());
        }
    }

    public static class MultipartformdataMediaType extends MediaType<MultipartformdataSchema.MultipartformdataSchema1> {
        public MultipartformdataMediaType() {
            super(MultipartformdataSchema.MultipartformdataSchema1.getInstance());
        }
    }

    public RequestBody() {
        super(
            Map.ofEntries(
                new AbstractMap.SimpleEntry<>("application/json", new ApplicationjsonMediaType()),
                new AbstractMap.SimpleEntry<>("multipart/form-data", new MultipartformdataMediaType())
            ),
            false
        );
    }

    public static abstract sealed class RequestBodyRequestBody permits RequestBodyApplicationjsonRequestBody, RequestBodyMultipartformdataRequestBody {}
    public static final class RequestBodyApplicationjsonRequestBody extends RequestBodyRequestBody implements RequestBody<ApplicationjsonSchema.ApplicationjsonSchema1Boxed> {
        public final String contentType;
        public final ApplicationjsonSchema.ApplicationjsonSchema1Boxed body;
        public RequestBodyApplicationjsonRequestBody(ApplicationjsonSchema.ApplicationjsonSchema1Boxed body) {
            contentType = "application/json";
            body = body;
        }
    }
    public static final class RequestBodyMultipartformdataRequestBody extends RequestBodyRequestBody implements RequestBody<MultipartformdataSchema.MultipartformdataSchema1Boxed> {
        public final String contentType;
        public final MultipartformdataSchema.MultipartformdataSchema1Boxed body;
        public RequestBodyMultipartformdataRequestBody(MultipartformdataSchema.MultipartformdataSchema1Boxed body) {
            contentType = "multipart/form-data";
            body = body;
        }
    }
}
