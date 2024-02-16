# Schema1
public class Schema1<br>

A class that contains necessary nested
- schema classes (which validate payloads), extends JsonSchema
- abstract sealed classes which store validated payloads, java version of a sum type
- boxed classes which store validated payloads, sealed permits class implementations

## Nested Class Summary
| Modifier and Type | Class and Description |
| ----------------- | ---------------------- |
| static class | [Schema1.Schema11Boxed](#schema11boxed)<br> abstract sealed validated payload class |
| static class | [Schema1.Schema11BoxedString](#schema11boxedstring)<br> boxed class to store validated String payloads |
| static class | [Schema1.Schema11](#schema11)<br> schema class |

## Schema11Boxed
public static abstract sealed class Schema11Boxed<br>
permits<br>
[Schema11BoxedString](#schema11boxedstring)

abstract sealed class that stores validated payloads using boxed classes

## Schema11BoxedString
public static final class Schema11BoxedString<br>
extends [Schema11Boxed](#schema11boxed)

a boxed class to store validated String payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| Schema11BoxedString(String data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| String | data<br>validated payload |

## Schema11
public static class Schema11<br>
extends StringJsonSchema.StringJsonSchema1

A schema class that validates payloads

| Methods Inherited from class org.openapijsonschematools.client.schemas.StringJsonSchema.StringJsonSchema1 |
| ------------------------------------------------------------------ |
| validate                                                           |
| validateAndBox                                                     |
