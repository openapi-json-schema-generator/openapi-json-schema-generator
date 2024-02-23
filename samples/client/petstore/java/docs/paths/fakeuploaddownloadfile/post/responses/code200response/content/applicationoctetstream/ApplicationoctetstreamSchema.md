# ApplicationoctetstreamSchema
public class ApplicationoctetstreamSchema<br>

A class that contains necessary nested
- schema classes (which validate payloads), extends JsonSchema
- sealed interfaces which store validated payloads, java version of a sum type
- boxed classes which store validated payloads, sealed permits class implementations

## Nested Class Summary
| Modifier and Type | Class and Description |
| ----------------- | ---------------------- |
| sealed interface | [ApplicationoctetstreamSchema.ApplicationoctetstreamSchema1Boxed](#applicationoctetstreamschema1boxed)<br> sealed interface for validated payloads |
| static class | [ApplicationoctetstreamSchema.ApplicationoctetstreamSchema1](#applicationoctetstreamschema1)<br> schema class |

## ApplicationoctetstreamSchema1Boxed
public sealed interface ApplicationoctetstreamSchema1Boxed<br>
permits<br>

sealed interface that stores validated payloads using boxed classes

## ApplicationoctetstreamSchema1
public static class ApplicationoctetstreamSchema1<br>
extends JsonSchema

A schema class that validates payloads

## Description
file to download
