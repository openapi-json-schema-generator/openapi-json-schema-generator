package org.openapijsonschematools.client.paths.fakemultiplerequestbodycontenttypes.post;

import org.openapijsonschematools.client.exceptions.NotImplementedException;
import org.openapijsonschematools.client.requestbody.RequestBodySerializer;
import org.openapijsonschematools.client.requestbody.GenericRequestBody;
import org.openapijsonschematools.client.requestbody.SerializedRequestBody;
import org.openapijsonschematools.client.mediatype.MediaType;
import org.openapijsonschematools.client.paths.fakemultiplerequestbodycontenttypes.post.requestbody.content.applicationjson.ApplicationjsonSchema;
import org.openapijsonschematools.client.paths.fakemultiplerequestbodycontenttypes.post.requestbody.content.multipartformdata.MultipartformdataSchema;

import java.util.AbstractMap;
import java.util.Map;

public class FakemultiplerequestbodycontenttypesPostRequestBody {
    public sealed interface SealedMediaType permits ApplicationjsonMediaType, MultipartformdataMediaType {}

    public record ApplicationjsonMediaType(ApplicationjsonSchema.ApplicationjsonSchema1 schema) implements SealedMediaType, MediaType<ApplicationjsonSchema.ApplicationjsonSchema1, Void> {
        public ApplicationjsonMediaType() {
            this(ApplicationjsonSchema.ApplicationjsonSchema1.getInstance());
        }
        @Override
        public Void encoding() {
            return null;
        }
    }

    public record MultipartformdataMediaType(MultipartformdataSchema.MultipartformdataSchema1 schema) implements SealedMediaType, MediaType<MultipartformdataSchema.MultipartformdataSchema1, Void> {
        public MultipartformdataMediaType() {
            this(MultipartformdataSchema.MultipartformdataSchema1.getInstance());
        }
        @Override
        public Void encoding() {
            return null;
        }
    }

    public static class FakemultiplerequestbodycontenttypesPostRequestBody1 extends RequestBodySerializer<SealedRequestBody, SealedMediaType> {
        public FakemultiplerequestbodycontenttypesPostRequestBody1() {
            super(
                Map.ofEntries(
                    new AbstractMap.SimpleEntry<>("application/json", new ApplicationjsonMediaType()),
                    new AbstractMap.SimpleEntry<>("multipart/form-data", new MultipartformdataMediaType())
                ),
                false
            );
        }

        public SerializedRequestBody serialize(SealedRequestBody requestBody) throws NotImplementedException  {
            if (requestBody instanceof ApplicationjsonRequestBody requestBody0) {
                return serialize(requestBody0.contentType(), requestBody0.body().getData());
            } else  {
                MultipartformdataRequestBody requestBody1 = (MultipartformdataRequestBody) requestBody;
                return serialize(requestBody1.contentType(), requestBody1.body().getData());
            }
        }
    }

    public sealed interface SealedRequestBody permits ApplicationjsonRequestBody, MultipartformdataRequestBody {}
    public record ApplicationjsonRequestBody(ApplicationjsonSchema.ApplicationjsonSchema1Boxed body) implements SealedRequestBody, GenericRequestBody<ApplicationjsonSchema.ApplicationjsonSchema1Boxed> {
        @Override
        public String contentType() {
            return "application/json";
        }
    }
    public record MultipartformdataRequestBody(MultipartformdataSchema.MultipartformdataSchema1Boxed body) implements SealedRequestBody, GenericRequestBody<MultipartformdataSchema.MultipartformdataSchema1Boxed> {
        @Override
        public String contentType() {
            return "multipart/form-data";
        }
    }
}
