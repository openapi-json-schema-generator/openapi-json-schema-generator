# Schema14
public class Schema14<br>

A class that contains necessary nested
- schema classes (which validate payloads), extends JsonSchema
- sealed interfaces which store validated payloads, java version of a sum type
- boxed classes which store validated payloads, sealed permits class implementations

## Nested Class Summary
| Modifier and Type | Class and Description |
| ----------------- | ---------------------- |
| sealed interface | [Schema14.Schema141Boxed](#schema141boxed)<br> sealed interface for validated payloads |
| record | [Schema14.Schema141BoxedString](#schema141boxedstring)<br> boxed class to store validated String payloads |
| static class | [Schema14.Schema141](#schema141)<br> schema class |

## Schema141Boxed
public sealed interface Schema141Boxed<br>
permits<br>
[Schema141BoxedString](#schema141boxedstring)

sealed interface that stores validated payloads using boxed classes

## Schema141BoxedString
public record Schema141BoxedString<br>
implements [Schema141Boxed](#schema141boxed)

record that stores validated String payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| Schema141BoxedString(String data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| String | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## Schema141
public static class Schema141<br>
extends StringJsonSchema.StringJsonSchema1

A schema class that validates payloads

| Methods Inherited from class org.openapijsonschematools.client.schemas.StringJsonSchema.StringJsonSchema1 |
| ------------------------------------------------------------------ |
| validate                                                           |
| validateAndBox                                                     |
