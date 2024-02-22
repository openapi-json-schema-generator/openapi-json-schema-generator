# BooleanTypeMatchesBooleans
org.openapijsonschematools.client.components.schemas.BooleanTypeMatchesBooleans.java
public class BooleanTypeMatchesBooleans<br>

A class that contains necessary nested
- schema classes (which validate payloads), extends JsonSchema
- sealed interfaces which store validated payloads, java version of a sum type
- boxed classes which store validated payloads, sealed permits class implementations

## Nested Class Summary
| Modifier and Type | Class and Description |
| ----------------- | ---------------------- |
| sealed interface | [BooleanTypeMatchesBooleans.BooleanTypeMatchesBooleans1Boxed](#booleantypematchesbooleans1boxed)<br> sealed interface for validated payloads |
| record | [BooleanTypeMatchesBooleans.BooleanTypeMatchesBooleans1BoxedBoolean](#booleantypematchesbooleans1boxedboolean)<br> boxed class to store validated boolean payloads |
| static class | [BooleanTypeMatchesBooleans.BooleanTypeMatchesBooleans1](#booleantypematchesbooleans1)<br> schema class |

## BooleanTypeMatchesBooleans1Boxed
public sealed interface BooleanTypeMatchesBooleans1Boxed<br>
permits<br>
[BooleanTypeMatchesBooleans1BoxedBoolean](#booleantypematchesbooleans1boxedboolean)

sealed interface that stores validated payloads using boxed classes

## BooleanTypeMatchesBooleans1BoxedBoolean
public record BooleanTypeMatchesBooleans1BoxedBoolean<br>
implements [BooleanTypeMatchesBooleans1Boxed](#booleantypematchesbooleans1boxed)

record that stores validated boolean payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| BooleanTypeMatchesBooleans1BoxedBoolean(boolean data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| boolean | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## BooleanTypeMatchesBooleans1
public static class BooleanTypeMatchesBooleans1<br>
extends BooleanJsonSchema.BooleanJsonSchema1

A schema class that validates payloads

| Methods Inherited from class org.openapijsonschematools.client.schemas.BooleanJsonSchema.BooleanJsonSchema1 |
| ------------------------------------------------------------------ |
| validate                                                           |
| validateAndBox                                                     |

[[Back to top]](#top) [[Back to Component Schemas]](../../../README.md#Component-Schemas) [[Back to README]](../../../README.md)
