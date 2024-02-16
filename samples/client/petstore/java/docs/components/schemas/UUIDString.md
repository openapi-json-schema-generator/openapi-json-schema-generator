# UUIDString
org.openapijsonschematools.client.components.schemas.UUIDString.java
public class UUIDString<br>

A class that contains necessary nested
- schema classes (which validate payloads), extends JsonSchema
- abstract sealed classes which store validated payloads, java version of a sum type
- boxed classes which store validated payloads, sealed permits class implementations

## Nested Class Summary
| Modifier and Type | Class and Description |
| ----------------- | ---------------------- |
| static class | [UUIDString.UUIDString1Boxed](#uuidstring1boxed)<br> abstract sealed validated payload class |
| static class | [UUIDString.UUIDString1BoxedString](#uuidstring1boxedstring)<br> boxed class to store validated String payloads |
| static class | [UUIDString.UUIDString1](#uuidstring1)<br> schema class |

## UUIDString1Boxed
public static abstract sealed class UUIDString1Boxed<br>
permits<br>
[UUIDString1BoxedString](#uuidstring1boxedstring)

abstract sealed class that stores validated payloads using boxed classes

## UUIDString1BoxedString
public static final class UUIDString1BoxedString<br>
extends [UUIDString1Boxed](#uuidstring1boxed)

a boxed class to store validated String payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| UUIDString1BoxedString(String data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| String | data<br>validated payload |

## UUIDString1
public static class UUIDString1<br>
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

import java.util.Arrays;
import java.util.List;
import java.util.AbstractMap;

static final SchemaConfiguration configuration = new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone());

// String validation
String validatedPayload = UUIDString.UUIDString1.validate(
    "046b6c7f-0b8a-43b9-b35d-6489e6daee91",
    configuration
);
```

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Set<Class<?>> | type = Set.of(<br/>&nbsp;&nbsp;&nbsp;&nbsp;String.class<br/>)<br/> |
| String | type = "uuid"; |
| Integer | minLength = 1 |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| String | validate(String arg, SchemaConfiguration configuration) |
| [UUIDString1BoxedString](#uuidstring1boxedstring) | validateAndBox(String arg, SchemaConfiguration configuration) |
| @Nullable Object | validate(@Nullable Object arg, SchemaConfiguration configuration) |
[[Back to top]](#top) [[Back to Component Schemas]](../../../README.md#Component-Schemas) [[Back to README]](../../../README.md)
