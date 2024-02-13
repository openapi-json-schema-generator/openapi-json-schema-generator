/*
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
*/

package org.openapijsonschematools.client.components.requestbodies;

import org.openapijsonschematools.client.requestbody.RequestBodySerializer;
import org.openapijsonschematools.client.mediatype.MediaType;
import org.openapijsonschematools.client.paths.fakeparametercollisions1ababselfab.post.requestbody.content.applicationjson.Schema;

import java.util.AbstractMap;
import java.util.Map;

public class RequestBody extends RequestBodySerializer {

    public static class ApplicationjsonMediaType extends MediaType<Schema.Schema1> {
        public ApplicationjsonMediaType() {
            super(Schema.Schema1.getInstance());
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
}
