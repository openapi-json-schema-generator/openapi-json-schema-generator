# PetpetidGetCode400Response

public class PetpetidGetCode400Response

A class that contains necessary nested response classes
- a class that extends ResponseDeserializer and is used to deserialize responses

## Nested Class Summary
| Modifier and Type | Class and Description |
| ----------------- | --------------------- |
| static class | [PetpetidGetCode400Response.PetpetidGetCode400Response1](#petpetidgetcode400response1)<br>class that deserializes responses |

## PetpetidGetCode400Response1
public static class PetpetidGetCode400Response1<br>
extends ResponseDeserializer<Void, Void, Void>

a class that deserializes responses

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| PetpetidGetCode400Response1()<br>Creates an instance |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | --------------------- |
| Map<String, Void> | content =  MapUtils.makeMap(<br>)<br>the contentType to schema info |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| ApiResponse<Void, Void> | deserialize(HttpResponse<byte[]> response, SchemaConfiguration configuration)<br>called by endpoint when deserialize responses |
