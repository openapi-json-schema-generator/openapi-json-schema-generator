package org.openapijsonschematools.codegen.templating.mustache;

import static org.mockito.AdditionalAnswers.returnsFirstArg;
import static org.mockito.ArgumentMatchers.anyString;
import static org.mockito.Mockito.when;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Map;

import org.mockito.Mock;
import org.mockito.MockitoAnnotations;
import org.openapijsonschematools.codegen.generators.Generator;
import org.testng.annotations.BeforeMethod;
import org.testng.annotations.Test;

public class LowercaseLambdaTest extends LambdaTest {

    @Mock
    Generator generator;

    @BeforeMethod
    public void setup() {
        MockitoAnnotations.initMocks(this);
    }

    @Test
    public void lowercaseTest() {
        // Given
        Map<String, Object> ctx = context("lowercase", new LowercaseLambda());

        // When & Then
        test("input text", "{{#lowercase}}InPut Text{{/lowercase}}", ctx);
    }

    @Test
    public void lowercaseReservedWordTest() {
        // Given
        Map<String, Object> ctx = context("lowercase", new LowercaseLambda().generator(generator));

        when(generator.sanitizeName(anyString())).then(returnsFirstArg());
        when(generator.reservedWords()).thenReturn(new HashSet<String>(Arrays.asList("reserved")));
        when(generator.escapeReservedWord("reserved")).thenReturn("escaped-reserved");

        // When & Then
        test("escaped-reserved", "{{#lowercase}}rEservEd{{/lowercase}}", ctx);
    }

}
