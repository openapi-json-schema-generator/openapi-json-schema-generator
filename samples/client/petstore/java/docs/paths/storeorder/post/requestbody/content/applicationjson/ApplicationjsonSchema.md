# ApplicationjsonSchema
public class ApplicationjsonSchema<br>
extends [Order1](../../../../../../components/schemas/Order.md#order)

A class that contains necessary nested
- schema classes (which validate payloads), extends JsonSchema
- sealed interfaces which store validated payloads, java version of a sum type
- boxed classes which store validated payloads, sealed permits class implementations

## Nested Class Summary
| Modifier and Type | Class and Description |
| ----------------- | ---------------------- |
| static class | [ApplicationjsonSchema.ApplicationjsonSchema1](#applicationjsonschema1)<br> schema class |

## ApplicationjsonSchema1
public static class ApplicationjsonSchema1<br>
extends [Order.Order1](../../../../../../components/schemas/Order.md#order1)

A schema class that validates payloads
