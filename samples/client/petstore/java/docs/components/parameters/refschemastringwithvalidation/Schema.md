# Schema
public class Schema<br>
extends [StringWithValidation1](../../../components/schemas/StringWithValidation.md#stringwithvalidation)

A class that contains necessary nested
- schema classes (which validate payloads), extends JsonSchema
- abstract sealed classes which store validated payloads, java version of a sum type
- boxed classes which store validated payloads, sealed permits class implementations

## Nested Class Summary
| Modifier and Type | Class and Description |
| ----------------- | ---------------------- |
| static class | [Schema.Schema1](#schema1)<br> schema class |

## Schema1
public static class Schema1<br>
extends [StringWithValidation.StringWithValidation1](../../../components/schemas/StringWithValidation.md#stringwithvalidation1)

A schema class that validates payloads
