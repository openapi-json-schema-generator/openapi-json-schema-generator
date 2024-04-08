# Bar
org.openapijsonschematools.client.components.schemas.Bar.java
public class Bar<br>

A class that contains necessary nested
- schema classes (which validate payloads), extends JsonSchema
- sealed interfaces which store validated payloads, java version of a sum type
- boxed classes which store validated payloads, sealed permits class implementations

## Nested Class Summary
| Modifier and Type | Class and Description |
| ----------------- | ---------------------- |
| sealed interface | [Bar.Bar1Boxed](#bar1boxed)<br> sealed interface for validated payloads |
| record | [Bar.Bar1BoxedString](#bar1boxedstring)<br> boxed class to store validated String payloads |
| static class | [Bar.Bar1](#bar1)<br> schema class |

## Bar1Boxed
public sealed interface Bar1Boxed<br>
permits<br>
[Bar1BoxedString](#bar1boxedstring)

sealed interface that stores validated payloads using boxed classes

## Bar1BoxedString
public record Bar1BoxedString<br>
implements [Bar1Boxed](#bar1boxed)

record that stores validated String payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| Bar1BoxedString(String data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| String | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## Bar1
public static class Bar1<br>
extends JsonSchema

A schema class that validates payloads

### Code Sample
```
import org.openapijsonschematools.client.configurations.JsonSchemaKeywordFlags;
import org.openapijsonschematools.client.configurations.SchemaConfiguration;
import org.openapijsonschematools.client.exceptions.ValidationException;
import org.openapijsonschematools.client.schemas.validation.MapUtils;
import org.openapijsonschematools.client.schemas.validation.FrozenList;
import org.openapijsonschematools.client.schemas.validation.FrozenMap;
import org.openapijsonschematools.client.components.schemas.Bar;

import java.util.Arrays;
import java.util.List;
import java.util.AbstractMap;

static final SchemaConfiguration configuration = new SchemaConfiguration(new JsonSchemaKeywordFlags.Builder().build());

// String validation
String validatedPayload = Bar.Bar1.validate(
    "a",
    configuration
);
```

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Set<Class<?>> | type = Set.of(<br/>&nbsp;&nbsp;&nbsp;&nbsp;String.class<br/>)<br/> |
| @Nullable Object | defaultValue = "bar" |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| String | validate(String arg, SchemaConfiguration configuration) |
| [Bar1BoxedString](#bar1boxedstring) | validateAndBox(String arg, SchemaConfiguration configuration) |
| [Bar1Boxed](#bar1boxed) | validateAndBox(@Nullable Object arg, SchemaConfiguration configuration) |
| @Nullable Object | validate(@Nullable Object arg, SchemaConfiguration configuration) |

[[Back to top]](#top) [[Back to Component Schemas]](../../../README.md#Component-Schemas) [[Back to README]](../../../README.md)
