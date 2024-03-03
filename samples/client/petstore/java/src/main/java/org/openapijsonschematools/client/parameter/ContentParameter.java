package org.openapijsonschematools.client.header;

import org.checkerframework.checker.nullness.qual.Nullable;
import org.openapijsonschematools.client.configurations.SchemaConfiguration;
import org.openapijsonschematools.client.contenttype.ContentTypeDetector;
import org.openapijsonschematools.client.contenttype.ContentTypeSerializer;
import org.openapijsonschematools.client.contenttype.ContentTypeDeserializer;
import org.openapijsonschematools.client.mediatype.MediaType;

import java.util.Map;

public class ContentParameter extends HeaderBase implements Parameter {
    public final String name;
    public final ParameterInType inType;
    public final Map<String, MediaType<?, ?>> content;

    public ContentHeader(String name, ParameterInType inType, boolean required, @Nullable ParameterStyle style, @Nullable Boolean allowReserved, @Nullable Boolean explode, Map<String, MediaType<?, ?>> content) {
        super(required, style, explode, allowReserved);
        this.name = name;
        this.inType = inType;
        this.content = content;
    }

    @Override
    public Map<String, String> serialize(@Nullable Object inData, boolean validate, SchemaConfiguration configuration) {
        for (Map.Entry<String, MediaType<?, ?>> entry: content.entrySet()) {
            var castInData = validate ? entry.getValue().schema().validate(inData, configuration) : inData ;
            String contentType = entry.getKey();
            if (ContentTypeDetector.contentTypeIsJson(contentType)) {
                var value = ContentTypeSerializer.toJson(castInData);
                return Map.of(name, value);
            } else {
                throw new RuntimeException("Serialization of "+contentType+" has not yet been implemented");
            }
        }
        throw new RuntimeException("Invalid value for content, it was empty and must have 1 key value pair");
    }
}