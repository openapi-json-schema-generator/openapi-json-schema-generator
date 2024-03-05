package org.openapijsonschematools.client.parameter;

import org.checkerframework.checker.nullness.qual.Nullable;
import org.junit.Assert;
import org.junit.Test;
import org.openapijsonschematools.client.configurations.JsonSchemaKeywordFlags;
import org.openapijsonschematools.client.configurations.SchemaConfiguration;
import org.openapijsonschematools.client.exceptions.InvalidTypeException;
import org.openapijsonschematools.client.schemas.AnyTypeJsonSchema;

import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Set;

public class SchemaQueryParameterTest {
    public record ParamTestCase(@Nullable Object payload, Map<String, String> expectedSerialization, @Nullable Boolean explode) {
        public ParamTestCase(@Nullable Object payload,  Map<String, String> expectedSerialization) {
            this(payload, expectedSerialization, null);
        }
    }

    public static class QueryParameterNoStyle extends SchemaQueryParameter {
        public QueryParameterNoStyle(@Nullable Boolean explode) {
            super("color", ParameterInType.QUERY, true, null, explode, null, AnyTypeJsonSchema.AnyTypeJsonSchema1.getInstance());
        }
    }

    @Test
    public void testQueryParameterNoStyleSerialization() {
        var mapPayload = new LinkedHashMap<String, Integer>();
        mapPayload.put("R", 100);
        mapPayload.put("G", 200);
        mapPayload.put("B", 150);
        var testCases = List.of(
                new ParamTestCase(
                        null,
                        Map.of("color", "")
                ),
                new ParamTestCase(
                        1,
                        Map.of("color", "?color=1")
                ),
                new ParamTestCase(
                        3.14,
                        Map.of("color","?color=3.14")
                ),
                new ParamTestCase(
                        "blue",
                        Map.of("color", "?color=blue")
                ),
                new ParamTestCase(
                        "hello world",
                        Map.of("color", "?color=hello%20world")
                ),
                new ParamTestCase(
                        "",
                        Map.of("color", "?color=")
                ),
                new ParamTestCase(
                        List.of(),
                        Map.of("color", "")
                ),
                new ParamTestCase(
                        List.of("blue", "black", "brown"),
                        Map.of("color", "?color=blue&color=black&color=brown")
                ),
                new ParamTestCase(
                        List.of("blue", "black", "brown"),
                        Map.of("color", "?color=blue&color=black&color=brown"),
                    true
                ),
                new ParamTestCase(
                        Map.of(),
                        Map.of("color", "")
                ),
                new ParamTestCase(
                        mapPayload,
                        Map.of("color", "?R=100&G=200&B=150")
                ),
                new ParamTestCase(
                        mapPayload,
                        Map.of("color", "?R=100&G=200&B=150"),
                        true
                )
        );
        SchemaConfiguration configuration = new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone());
        for (ParamTestCase testCase: testCases) {
            var parameter = new QueryParameterNoStyle(testCase.explode);
            var iterator = parameter.getPrefixSeparatorIterator();
            var serialization = parameter.serialize(testCase.payload, false, configuration, iterator);
            Assert.assertEquals(testCase.expectedSerialization, serialization);
        }
        var parameter = new QueryParameterNoStyle(false);
        var iterator = parameter.getPrefixSeparatorIterator();
        for (boolean value: Set.of(true, false)) {
            Assert.assertThrows(
                    InvalidTypeException.class,
                    () -> parameter.serialize(value, false, configuration, iterator)
            );
        }
    }

    public static class QueryParameterSpaceDelimited extends SchemaQueryParameter {
        public QueryParameterSpaceDelimited(@Nullable Boolean explode) {
            super("color", ParameterInType.QUERY, true, ParameterStyle.SPACE_DELIMITED, explode, null, AnyTypeJsonSchema.AnyTypeJsonSchema1.getInstance());
        }
    }

    @Test
    public void testQueryParameterSpaceDelimitedSerialization() {
        var mapPayload = new LinkedHashMap<String, Integer>();
        mapPayload.put("R", 100);
        mapPayload.put("G", 200);
        mapPayload.put("B", 150);
        var testCases = List.of(
                new ParamTestCase(
                        List.of(),
                        Map.of("color", "")
                ),
                new ParamTestCase(
                        List.of("blue", "black", "brown"),
                        Map.of("color", "blue%20black%20brown")
                ),
                new ParamTestCase(
                        List.of("blue", "black", "brown"),
                        Map.of("color", "blue%20black%20brown"),
                        true
                ),
                new ParamTestCase(
                        Map.of(),
                        Map.of("color", "")
                ),
                new ParamTestCase(
                        mapPayload,
                        Map.of("color", "R%20100%20G%20200%20B%20150")
                ),
                new ParamTestCase(
                        mapPayload,
                        Map.of("color", "R=100%20G=200%20B=150"),
                        true
                )
        );
        SchemaConfiguration configuration = new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone());
        for (ParamTestCase testCase: testCases) {
            var parameter = new QueryParameterSpaceDelimited(testCase.explode);
            var iterator = parameter.getPrefixSeparatorIterator();
            var serialization = parameter.serialize(testCase.payload, false, configuration, iterator);
            Assert.assertEquals(testCase.expectedSerialization, serialization);
        }
    }

    public static class QueryParameterPipeDelimited extends SchemaQueryParameter {
        public QueryParameterPipeDelimited(@Nullable Boolean explode) {
            super("color", ParameterInType.QUERY, true, ParameterStyle.PIPE_DELIMITED, explode, null, AnyTypeJsonSchema.AnyTypeJsonSchema1.getInstance());
        }
    }

    @Test
    public void testQueryParameterPipeDelimitedSerialization() {
        var mapPayload = new LinkedHashMap<String, Integer>();
        mapPayload.put("R", 100);
        mapPayload.put("G", 200);
        mapPayload.put("B", 150);
        var testCases = List.of(
                new ParamTestCase(
                        List.of(),
                        Map.of("color", "")
                ),
                new ParamTestCase(
                        List.of("blue", "black", "brown"),
                        Map.of("color", "blue|black|brown")
                ),
                new ParamTestCase(
                        List.of("blue", "black", "brown"),
                        Map.of("color", "blue|black|brown"),
                        true
                ),
                new ParamTestCase(
                        Map.of(),
                        Map.of("color", "")
                ),
                new ParamTestCase(
                        mapPayload,
                        Map.of("color", "R|100|G|200|B|150")
                ),
                new ParamTestCase(
                        mapPayload,
                        Map.of("color", "R=100|G=200|B=150"),
                        true
                )
        );
        SchemaConfiguration configuration = new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone());
        for (ParamTestCase testCase: testCases) {
            var parameter = new QueryParameterPipeDelimited(testCase.explode);
            var iterator = parameter.getPrefixSeparatorIterator();
            var serialization = parameter.serialize(testCase.payload, false, configuration, iterator);
            Assert.assertEquals(testCase.expectedSerialization, serialization);
        }
    }
}
