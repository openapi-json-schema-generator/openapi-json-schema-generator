package org.openapijsonschematools.client.header;

import org.checkerframework.checker.nullness.qual.Nullable;
import org.openapijsonschematools.client.configurations.SchemaConfiguration;
import org.openapijsonschematools.client.contenttype.ContentTypeDetector;
import org.openapijsonschematools.client.contenttype.ContentTypeSerializer;
import org.openapijsonschematools.client.mediatype.MediaType;
import org.openapijsonschematools.client.parameter.ParameterStyle;

import java.net.http.HttpHeaders;
import java.util.List;
import java.util.Map;
import java.util.function.BiPredicate;

public class ContentHeader extends HeaderBase implements Header {
    public final Map<String, MediaType<?, ?>> content;

    public ContentHeader(boolean required, @Nullable Boolean allowReserved, @Nullable Boolean explode, Map<String, MediaType<?, ?>> content) {
        super(required, ParameterStyle.SIMPLE, explode, allowReserved);
        this.content = content;
    }

    private static HttpHeaders toHeaders(String name, String value) {
        Map<String, List<String>> map = Map.of(name, List.of(value));
        BiPredicate<String, String> headerFilter = (key, val) -> true;
        return HttpHeaders.of(map, headerFilter);
    }

    @Override
    public HttpHeaders serialize(@Nullable Object inData, String name, boolean skipValidation, SchemaConfiguration configuration) {
        for (Map.Entry<String, MediaType<?, ?>> entry: content.entrySet()) {
            var castInData = skipValidation ? inData : entry.getValue().schema().validate(inData, configuration);
            String contentType = entry.getKey();
            if (ContentTypeDetector.contentTypeIsJson(contentType)) {
                var value = ContentTypeSerializer.toJson(castInData);
                return toHeaders(name, value);
            } else {
                throw new RuntimeException("Serialization of "+contentType+" has not yet been implemented");
            }
        }
        throw new RuntimeException("Invalid value for content, it was empty and must have 1 key value pair");
    }
}