# EnumWithTrueDoesNotMatch1
org.openapijsonschematools.client.components.schemas.EnumWithTrueDoesNotMatch1.java
public class EnumWithTrueDoesNotMatch1

A class that contains necessary nested schema classes, and classes to store validated list and map payloads

## Nested Class Summary
| Modifier and Type | Class and Description |
| ----------------- | ---------------------- |
| static class | [EnumWithTrueDoesNotMatch1.EnumWithTrueDoesNotMatch11](#enumwithtruedoesnotmatch11)<br> schema class |

## EnumWithTrueDoesNotMatch11
public static class EnumWithTrueDoesNotMatch11<br>
extends JsonSchema

A schema class that validates payloads

### Code Sample
```
import org.openapijsonschematools.client.configurations.JsonSchemaKeywordFlags;
import org.openapijsonschematools.client.configurations.SchemaConfiguration;
import org.openapijsonschematools.client.exceptions.ValidationException;
import org.openapijsonschematools.client.schemas.MapMaker;
import org.openapijsonschematools.client.schemas.validation.FrozenList;
import org.openapijsonschematools.client.schemas.validation.FrozenMap;

import java.util.Arrays;
import java.util.List;
import java.util.AbstractMap;

static final SchemaConfiguration configuration = new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone());

// boolean validation
boolean validatedPayload = EnumWithTrueDoesNotMatch1.EnumWithTrueDoesNotMatch11.validate(
    true,
    configuration
);
```

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| static LinkedHashMap<String, KeywordValidator> |keywordToValidator<br/>new LinkedHashMap<>(Map.ofEntries(<br/>&nbsp;&nbsp;&nbsp;&nbsp;new KeywordEntry("type", new TypeValidator(Set.of(Boolean.class))),<br/>&nbsp;&nbsp;&nbsp;&nbsp;new KeywordEntry("enum", new EnumValidator(Set.of(<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;true)))<br>)); |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| static boolean | validate(boolean arg, SchemaConfiguration configuration) |

[[Back to top]](#top) [[Back to Component Schemas]](../../../README.md#Component-Schemas) [[Back to README]](../../../README.md)
