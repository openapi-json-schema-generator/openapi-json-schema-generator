/*
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
*/

package org.openapijsonschematools.client.components.requestbodies;

import org.openapijsonschematools.client.requestbody.RequestBodySerializer;
import org.openapijsonschematools.client.mediatype.MediaType;
import org.openapijsonschematools.client.paths.fakeuploaddownloadfile.post.requestbody.content.applicationoctetstream.ApplicationoctetstreamSchema;

import java.util.AbstractMap;
import java.util.Map;

public class RequestBody extends RequestBodySerializer {

    public static class ApplicationoctetstreamMediaType extends MediaType<ApplicationoctetstreamSchema.ApplicationoctetstreamSchema1> {
        public ApplicationoctetstreamMediaType() {
            super(ApplicationoctetstreamSchema.ApplicationoctetstreamSchema1.getInstance());
        }
    }

    public RequestBody() {
        super(
            Map.ofEntries(
                new AbstractMap.SimpleEntry<>("application/octet-stream", new ApplicationoctetstreamMediaType())
            ),
            true
        );
    }
}
