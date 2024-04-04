package org.openapijsonschematools.client.components.parameters;

import org.openapijsonschematools.client.parameter.ParameterInType;
import org.openapijsonschematools.client.parameter.ContentParameter;
import org.openapijsonschematools.client.mediatype.MediaType;
import org.openapijsonschematools.client.components.parameters.componentrefschemastringwithvalidation.content.applicationjson.ApplicationjsonSchema;

import java.util.AbstractMap;

public class ComponentRefSchemaStringWithValidation {

    public record ApplicationjsonMediaType(ApplicationjsonSchema.ApplicationjsonSchema1 schema) implements MediaType<ApplicationjsonSchema.ApplicationjsonSchema1, Void> {
        public ApplicationjsonMediaType() {
            this(ApplicationjsonSchema.ApplicationjsonSchema1.getInstance());
        }
        @Override
        public Void encoding() {
            return null;
        }
    }

    public static class ComponentRefSchemaStringWithValidation1 extends ContentParameter {
        public ComponentRefSchemaStringWithValidation1() {
            super(
                "CRSstringWithValidation",
                ParameterInType.PATH,
                true,
                null,
                null,
                false,
                new AbstractMap.SimpleEntry<>("application/json", new ApplicationjsonMediaType())
            );
        }
    }
}
