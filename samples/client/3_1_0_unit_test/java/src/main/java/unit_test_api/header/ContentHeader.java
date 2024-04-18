package unit_test_api.header;

import org.checkerframework.checker.nullness.qual.Nullable;
import unit_test_api.configurations.SchemaConfiguration;
import unit_test_api.contenttype.ContentTypeDetector;
import unit_test_api.contenttype.ContentTypeSerializer;
import unit_test_api.contenttype.ContentTypeDeserializer;
import unit_test_api.exceptions.NotImplementedException;
import unit_test_api.exceptions.ValidationException;
import unit_test_api.mediatype.MediaType;
import unit_test_api.parameter.ParameterStyle;

import java.net.http.HttpHeaders;
import java.util.List;
import java.util.Map;
import java.util.AbstractMap;
import java.util.function.BiPredicate;

public class ContentHeader extends HeaderBase implements Header {
    public final AbstractMap.SimpleEntry<String, MediaType<?, ?>> content;

    public ContentHeader(boolean required, @Nullable Boolean allowReserved, @Nullable Boolean explode, AbstractMap.SimpleEntry<String, MediaType<?, ?>> content) {
        super(required, ParameterStyle.SIMPLE, explode, allowReserved);
        this.content = content;
    }

    private static HttpHeaders toHeaders(String name, String value) {
        Map<String, List<String>> map = Map.of(name, List.of(value));
        BiPredicate<String, String> headerFilter = (key, val) -> true;
        return HttpHeaders.of(map, headerFilter);
    }

    @Override
    public HttpHeaders serialize(@Nullable Object inData, String name, boolean validate, SchemaConfiguration configuration) throws NotImplementedException, ValidationException {
        var castInData = validate ? content.getValue().schema().validate(inData, configuration) : inData ;
        String contentType = content.getKey();
        if (ContentTypeDetector.contentTypeIsJson(contentType)) {
            var value = ContentTypeSerializer.toJson(castInData);
            return toHeaders(name, value);
        } else {
            throw new NotImplementedException("Serialization of "+contentType+" has not yet been implemented");
        }
    }

    @Override
    public @Nullable Object deserialize(List<String> inData, boolean validate, SchemaConfiguration configuration) throws NotImplementedException, ValidationException {
        String inDataJoined = String.join(",", inData); // unsure if this is needed
        @Nullable Object deserializedJson = ContentTypeDeserializer.fromJson(inDataJoined);
        if (validate) {
            String contentType = content.getKey();
            if (ContentTypeDetector.contentTypeIsJson(contentType)) {
                return content.getValue().schema().validate(deserializedJson, configuration);
            } else {
                throw new NotImplementedException("Header deserialization of "+contentType+" has not yet been implemented");
            }
        }
        return deserializedJson;
    }
}