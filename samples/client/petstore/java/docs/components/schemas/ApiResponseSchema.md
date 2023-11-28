# ApiResponseSchema
org.openapijsonschematools.components.schemas.ApiResponseSchema.java
public class ApiResponseSchema

A class that contains necessary nested schema classes, and classes to store validated list and map payloads

## Nested Class Summary
| Modifier and Type | Class and Description |
| ----------------- | ---------------------- |
| static class | [ApiResponseSchema.ApiResponseSchema1](#apiresponseschema1)<br> schema class |
| static class | [ApiResponseSchema.ApiResponseMap](#apiresponsemap)<br> output class for Map payloads |
| static class | [ApiResponseSchema.Message](#message)<br> schema class |
| static class | [ApiResponseSchema.Type](#type)<br> schema class |
| static class | [ApiResponseSchema.Code](#code)<br> schema class |

## ApiResponseSchema1
public static class ApiResponseSchema1<br>
extends JsonSchema

A schema class that validates payloads
### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| static LinkedHashMap<String, KeywordValidator> |keywordToValidator<br/>new LinkedHashMap<>(Map.ofEntries(<br/>&nbsp;&nbsp;&nbsp;&nbsp;new KeywordEntry("type", new TypeValidator(Set.of(FrozenMap.class))),<br/>&nbsp;&nbsp;&nbsp;&nbsp;new KeywordEntry("properties", new PropertiesValidator(Map.ofEntries(<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;new PropertyEntry("code", [Code.class](#code))),<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;new PropertyEntry("type", [Type.class](#type))),<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;new PropertyEntry("message", [Message.class](#message)))<br>&nbsp;&nbsp;&nbsp;&nbsp;)))<br>)); |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| static [ApiResponseMap](#apiresponsemap) | validate(Map<String, Object> arg, SchemaConfiguration configuration) |

## ApiResponseMap
public static class ApiResponseMap<br>
extends FrozenMap<String, Object>

A class to store validated Map payloads

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| static [ApiResponseMap](#apiresponsemap) | of(Map<String, Object> arg, SchemaConfiguration configuration) |
| int | code()<br>[optional] value must be a 32 bit integer |
| String | type()<br>[optional] |
| String | message()<br>[optional] |
| Object | getAdditionalProperty(String name)<br>provides type safety for additional properties |

## Input Map Keys
```
type: Map<String, Object>
```
| Key | Type |  Description | Notes |
| --- | ---- | ------------ | ----- |
| **code** | int |  | [optional] value must be a 32 bit integer |
| **type** | String |  | [optional] |
| **message** | String |  | [optional] |
| **anyStringName** | Object | any string name can be used but the value must be the correct type | [optional] |

## Message
public static class Message<br>
extends StringJsonSchema

A schema class that validates payloads

| Methods Inherited from class org.openapijsonschematools.schemas.StringJsonSchema |
| ------------------------------------------------------------------ |
| validate                                                           |

## Type
public static class Type<br>
extends StringJsonSchema

A schema class that validates payloads

| Methods Inherited from class org.openapijsonschematools.schemas.StringJsonSchema |
| ------------------------------------------------------------------ |
| validate                                                           |

## Code
public static class Code<br>
extends Int32JsonSchema

A schema class that validates payloads

[[Back to top]](#top) [[Back to Component Schemas]](../../../README.md#Component-Schemas) [[Back to README]](../../../README.md)
