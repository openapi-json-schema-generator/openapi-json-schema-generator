# SelfReferencingObjectModel
org.openapijsonschematools.components.schemas.SelfReferencingObjectModel.java
public class SelfReferencingObjectModel

A class that contains necessary nested schema classes, and classes to store validated list and map payloads

## Nested Class Summary
| Modifier and Type | Class and Description |
| ----------------- | ---------------------- |
| static class | [SelfReferencingObjectModel.SelfReferencingObjectModel1](#selfreferencingobjectmodel1)<br> schema class |
| static class | [SelfReferencingObjectModel.SelfReferencingObjectModelMap](#selfreferencingobjectmodelmap)<br> output class for Map payloads |

## SelfReferencingObjectModel1
public static class SelfReferencingObjectModel1<br>
extends JsonSchema

A schema class that validates payloads
### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| static LinkedHashMap<String, KeywordValidator> |keywordToValidator<br/>new LinkedHashMap<>(Map.ofEntries(<br/>&nbsp;&nbsp;&nbsp;&nbsp;new KeywordEntry("type", new TypeValidator(Set.of(FrozenMap.class))),<br/>&nbsp;&nbsp;&nbsp;&nbsp;new KeywordEntry("properties", new PropertiesValidator(Map.ofEntries(<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;new PropertyEntry("selfRef", [SelfReferencingObjectModel1.class](#selfreferencingobjectmodel1)))<br>&nbsp;&nbsp;&nbsp;&nbsp;))),<br>&nbsp;&nbsp;&nbsp;&nbsp;new KeywordEntry("additionalProperties", new AdditionalPropertiesValidator([SelfReferencingObjectModel1.class](#selfreferencingobjectmodel1)))<br>)); |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| static [SelfReferencingObjectModelMap](#selfreferencingobjectmodelmap) | validate(Map<String, Object> arg, SchemaConfiguration configuration) |

## SelfReferencingObjectModelMap
public static class SelfReferencingObjectModelMap<br>
extends FrozenMap<String, Object>

A class to store validated Map payloads

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| static [SelfReferencingObjectModelMap](#selfreferencingobjectmodelmap) | of(Map<String, Object> arg, SchemaConfiguration configuration) |
| [SelfReferencingObjectModelMap](#selfreferencingobjectmodelmap) | selfRef()<br>[optional] |
| [SelfReferencingObjectModelMap](#selfreferencingobjectmodelmap) | getAdditionalProperty(String name)<br>provides type safety for additional properties |

## Input Map Keys
```
type: Map<String, Object>
```
| Key | Type |  Description | Notes |
| --- | ---- | ------------ | ----- |
| **selfRef** | Map<String, Object> |  | [optional] |
| **anyStringName** | Map<String, Object> | any string name can be used but the value must be the correct type | [optional] |

[[Back to top]](#top) [[Back to Component Schemas]](../../../README.md#Component-Schemas) [[Back to README]](../../../README.md)
