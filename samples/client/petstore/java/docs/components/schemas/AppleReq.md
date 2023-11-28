# AppleReq
org.openapijsonschematools.components.schemas.AppleReq.java
public class AppleReq

A class that contains necessary nested schema classes, and classes to store validated list and map payloads

## Nested Class Summary
| Modifier and Type | Class and Description |
| ----------------- | ---------------------- |
| static class | [AppleReq.AppleReq1](#applereq1)<br> schema class |
| static class | [AppleReq.AppleReqMap](#applereqmap)<br> output class for Map payloads |
| static class | [AppleReq.Mealy](#mealy)<br> schema class |
| static class | [AppleReq.Cultivar](#cultivar)<br> schema class |
| static class | [AppleReq.AdditionalProperties](#additionalproperties)<br> schema class |

## AppleReq1
public static class AppleReq1<br>
extends JsonSchema

A schema class that validates payloads
### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| static LinkedHashMap<String, KeywordValidator> |keywordToValidator<br/>new LinkedHashMap<>(Map.ofEntries(<br/>&nbsp;&nbsp;&nbsp;&nbsp;new KeywordEntry("type", new TypeValidator(Set.of(FrozenMap.class))),<br/>&nbsp;&nbsp;&nbsp;&nbsp;new KeywordEntry("properties", new PropertiesValidator(Map.ofEntries(<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;new PropertyEntry("cultivar", [Cultivar.class](#cultivar))),<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;new PropertyEntry("mealy", [Mealy.class](#mealy)))<br>&nbsp;&nbsp;&nbsp;&nbsp;))),<br>&nbsp;&nbsp;&nbsp;&nbsp;new KeywordEntry("required", new RequiredValidator(Set.of(<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"cultivar"<br>&nbsp;&nbsp;&nbsp;&nbsp;))),<br>&nbsp;&nbsp;&nbsp;&nbsp;new KeywordEntry("additionalProperties", new AdditionalPropertiesValidator([AdditionalProperties.class](#additionalproperties)))<br>)); |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| static [AppleReqMap](#applereqmap) | validate(Map<String, Object> arg, SchemaConfiguration configuration) |

## AppleReqMap
public static class AppleReqMap<br>
extends FrozenMap<String, Object>

A class to store validated Map payloads

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| static [AppleReqMap](#applereqmap) | of(Map<String, Object> arg, SchemaConfiguration configuration) |
| String | cultivar()<br> |
| boolean | mealy()<br>[optional] |

## Input Map Keys
```
type: Map<String, Object>
```
| Key | Type |  Description | Notes |
| --- | ---- | ------------ | ----- |
| **cultivar** | String |  | |
| **mealy** | boolean |  | [optional] |

## Mealy
public static class Mealy<br>
extends BooleanJsonSchema

A schema class that validates payloads

| Methods Inherited from class org.openapijsonschematools.schemas.BooleanJsonSchema |
| ------------------------------------------------------------------ |
| validate                                                           |

## Cultivar
public static class Cultivar<br>
extends StringJsonSchema

A schema class that validates payloads

| Methods Inherited from class org.openapijsonschematools.schemas.StringJsonSchema |
| ------------------------------------------------------------------ |
| validate                                                           |

## AdditionalProperties
public static class AdditionalProperties<br>
extends NotAnyTypeJsonSchema

A schema class that validates payloads

| Methods Inherited from class org.openapijsonschematools.schemas.NotAnyTypeJsonSchema |
| ------------------------------------------------------------------ |
| validate                                                           |

[[Back to top]](#top) [[Back to Component Schemas]](../../../README.md#Component-Schemas) [[Back to README]](../../../README.md)
