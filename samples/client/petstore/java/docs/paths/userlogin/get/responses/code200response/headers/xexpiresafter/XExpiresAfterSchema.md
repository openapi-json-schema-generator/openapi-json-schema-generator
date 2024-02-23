# XExpiresAfterSchema
public class XExpiresAfterSchema<br>

A class that contains necessary nested
- schema classes (which validate payloads), extends JsonSchema
- sealed interfaces which store validated payloads, java version of a sum type
- boxed classes which store validated payloads, sealed permits class implementations

## Nested Class Summary
| Modifier and Type | Class and Description |
| ----------------- | ---------------------- |
| sealed interface | [XExpiresAfterSchema.XExpiresAfterSchema1Boxed](#xexpiresafterschema1boxed)<br> sealed interface for validated payloads |
| record | [XExpiresAfterSchema.XExpiresAfterSchema1BoxedString](#xexpiresafterschema1boxedstring)<br> boxed class to store validated String payloads |
| static class | [XExpiresAfterSchema.XExpiresAfterSchema1](#xexpiresafterschema1)<br> schema class |

## XExpiresAfterSchema1Boxed
public sealed interface XExpiresAfterSchema1Boxed<br>
permits<br>
[XExpiresAfterSchema1BoxedString](#xexpiresafterschema1boxedstring)

sealed interface that stores validated payloads using boxed classes

## XExpiresAfterSchema1BoxedString
public record XExpiresAfterSchema1BoxedString<br>
implements [XExpiresAfterSchema1Boxed](#xexpiresafterschema1boxed)

record that stores validated String payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| XExpiresAfterSchema1BoxedString(String data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| String | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## XExpiresAfterSchema1
public static class XExpiresAfterSchema1<br>
extends DateTimeJsonSchema.DateTimeJsonSchema1

A schema class that validates payloads

| Methods Inherited from class org.openapijsonschematools.client.schemas.DateTimeJsonSchema.DateTimeJsonSchema1 |
| ------------------------------------------------------------------ |
| validate                                                           |
| validateAndBox                                                     |
