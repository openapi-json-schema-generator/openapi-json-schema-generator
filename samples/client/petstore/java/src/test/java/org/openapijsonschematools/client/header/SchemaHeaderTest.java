package org.openapijsonschematools.client.header;

import org.checkerframework.checker.nullness.qual.Nullable;
import org.junit.Assert;
import org.junit.Test;
import org.openapijsonschematools.client.configurations.JsonSchemaKeywordFlags;
import org.openapijsonschematools.client.configurations.SchemaConfiguration;
import org.openapijsonschematools.client.exceptions.InvalidTypeException;
import org.openapijsonschematools.client.schemas.AnyTypeJsonSchema;

import java.net.http.HttpHeaders;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.function.BiPredicate;

public class SchemaHeaderTest {
    public record ParamTestCase(@Nullable Object payload, Map<String, List<String>> expectedSerialization, @Nullable Boolean explode) {
        public ParamTestCase(@Nullable Object payload,  Map<String, List<String>> expectedSerialization) {
            this(payload, expectedSerialization, null);
        }
    }

    @Test
    public void testSerialization() {
        var mapPayload = new LinkedHashMap<String, Integer>();
        mapPayload.put("R", 100);
        mapPayload.put("G", 200);
        mapPayload.put("B", 150);
        var testCases = List.of(
                new ParamTestCase(
                        null,
                        Map.of("color", List.of(""))
                ),
                new ParamTestCase(
                        1,
                        Map.of("color", List.of("1"))
                ),
                new ParamTestCase(
                        3.14,
                        Map.of("color",List.of("3.14"))
                ),
                new ParamTestCase(
                        "blue",
                        Map.of("color", List.of("blue"))
                ),
                new ParamTestCase(
                        "hello world",
                        Map.of("color", List.of("hello world"))
                ),
                new ParamTestCase(
                        "",
                        Map.of("color", List.of(""))
                ),
                new ParamTestCase(
                        List.of(),
                        Map.of("color", List.of(""))
                ),
                new ParamTestCase(
                        List.of("blue", "black", "brown"),
                        Map.of("color", List.of("blue,black,brown"))
                ),
                new ParamTestCase(
                        List.of("blue", "black", "brown"),
                        Map.of("color", List.of("blue,black,brown")),
                    true
                ),
                new ParamTestCase(
                        Map.of(),
                        Map.of("color", List.of(""))
                ),
                new ParamTestCase(
                        mapPayload,
                        Map.of("color", List.of("R,100,G,200,B,150"))
                ),
                new ParamTestCase(
                        mapPayload,
                        Map.of("color", List.of("R=100,G=200,B=150")),
                        true
                )
        );
        SchemaConfiguration configuration = new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone());
        BiPredicate<String, String> headerFilter = (key, val) -> true;
        for (ParamTestCase testCase: testCases) {
            var header = new SchemaHeader(
                    true,
                    false,
                    testCase.explode,
                    AnyTypeJsonSchema.AnyTypeJsonSchema1.getInstance()
            );
            var serialization = header.serialize(testCase.payload, "color", true, configuration);
            Assert.assertEquals(HttpHeaders.of(testCase.expectedSerialization, headerFilter), serialization);
        }
        SchemaHeader boolHeader = new SchemaHeader(
                true,
                false,
                false,
                AnyTypeJsonSchema.AnyTypeJsonSchema1.getInstance()
        );
        for (boolean value: Set.of(true, false)) {
            Assert.assertThrows(
                    InvalidTypeException.class,
                    () -> boolHeader.serialize(value, "color", true, configuration)
            );
        }
    }
}
