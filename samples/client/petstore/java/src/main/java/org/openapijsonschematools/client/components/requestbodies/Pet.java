/*
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
*/

package org.openapijsonschematools.client.components.requestbodies;

import org.openapijsonschematools.client.requestbody.RequestBodySerializer;
import org.openapijsonschematools.client.requestbody.GenericRequestBody;
import org.openapijsonschematools.client.mediatype.MediaType;
import org.openapijsonschematools.client.components.requestbodies.pet.content.applicationjson.ApplicationjsonSchema;
import org.openapijsonschematools.client.components.requestbodies.pet.content.applicationxml.ApplicationxmlSchema;
import org.openapijsonschematools.client.requestbody.SerializedRequestBody;

import java.util.AbstractMap;
import java.util.Map;

public class Pet {

    public static class ApplicationjsonMediaType extends MediaType<ApplicationjsonSchema.ApplicationjsonSchema1> {
        public ApplicationjsonMediaType() {
            super(ApplicationjsonSchema.ApplicationjsonSchema1.getInstance());
        }
    }

    public static class ApplicationxmlMediaType extends MediaType<ApplicationxmlSchema.ApplicationxmlSchema1> {
        public ApplicationxmlMediaType() {
            super(ApplicationxmlSchema.ApplicationxmlSchema1.getInstance());
        }
    }

    public static class Pet1 extends RequestBodySerializer<SealedRequestBody> {
       public Pet1() {
            super(
                Map.ofEntries(
                    new AbstractMap.SimpleEntry<>("application/json", new ApplicationjsonMediaType()),
                    new AbstractMap.SimpleEntry<>("application/xml", new ApplicationxmlMediaType())
                ),
                true
            );
        }

        public SerializedRequestBody serialize(SealedRequestBody requestBody) {
            return null;
        }
    }

    public static abstract sealed class SealedRequestBody permits ApplicationjsonRequestBody, ApplicationxmlRequestBody {}
    public static final class ApplicationjsonRequestBody extends SealedRequestBody implements GenericRequestBody<ApplicationjsonSchema.Pet1Boxed> {
        private final String contentType;
        private final ApplicationjsonSchema.Pet1Boxed body;
        public ApplicationjsonRequestBody(ApplicationjsonSchema.Pet1Boxed body) {
            contentType = "application/json";
            this.body = body;
        }
        @Override
        public String contentType() {
            return contentType;
        }

        @Override
        public ApplicationjsonSchema.Pet1Boxed body() {
            return body;
        }
    }
    public static final class ApplicationxmlRequestBody extends SealedRequestBody implements GenericRequestBody<ApplicationxmlSchema.Pet1Boxed> {
        private final String contentType;
        private final ApplicationxmlSchema.Pet1Boxed body;
        public ApplicationxmlRequestBody(ApplicationxmlSchema.Pet1Boxed body) {
            contentType = "application/xml";
            this.body = body;
        }
        @Override
        public String contentType() {
            return contentType;
        }

        @Override
        public ApplicationxmlSchema.Pet1Boxed body() {
            return body;
        }
    }
}
