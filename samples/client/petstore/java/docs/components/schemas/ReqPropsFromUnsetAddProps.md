# ReqPropsFromUnsetAddProps
org.openapijsonschematools.client.components.schemas.ReqPropsFromUnsetAddProps.java
public class ReqPropsFromUnsetAddProps

A class that contains necessary nested schema classes, and classes to store validated list and map payloads

## Nested Class Summary
| Modifier and Type | Class and Description |
| ----------------- | ---------------------- |
| static class | [ReqPropsFromUnsetAddProps.ReqPropsFromUnsetAddProps1](#reqpropsfromunsetaddprops1)<br> schema class |
| static class | [ReqPropsFromUnsetAddProps.ReqPropsFromUnsetAddPropsMap](#reqpropsfromunsetaddpropsmap)<br> output class for Map payloads |

## ReqPropsFromUnsetAddProps1
public static class ReqPropsFromUnsetAddProps1<br>
extends JsonSchema

A schema class that validates payloads
### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| static LinkedHashMap<String, KeywordValidator> |keywordToValidator<br/>new LinkedHashMap<>(Map.ofEntries(<br/>&nbsp;&nbsp;&nbsp;&nbsp;new KeywordEntry("type", new TypeValidator(Set.of(FrozenMap.class))),<br/>&nbsp;&nbsp;&nbsp;&nbsp;new KeywordEntry("required", new RequiredValidator(Set.of(<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"invalid-name",<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"validName"<br>&nbsp;&nbsp;&nbsp;&nbsp;)))<br>)); |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| static [ReqPropsFromUnsetAddPropsMap](#reqpropsfromunsetaddpropsmap) | validate(Map<String, Object> arg, SchemaConfiguration configuration) |

## ReqPropsFromUnsetAddPropsMap
public static class ReqPropsFromUnsetAddPropsMap<br>
extends FrozenMap<String, Object>

A class to store validated Map payloads

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| static [ReqPropsFromUnsetAddPropsMap](#reqpropsfromunsetaddpropsmap) | of(Map<String, Object> arg, SchemaConfiguration configuration) |
| Object | validName()<br> |
| Object | get(String key)<br>This schema has invalid Java names so this method must be used when you access instance["invalid-name"],  |
| Object | getAdditionalProperty(String name)<br>provides type safety for additional properties |

## Input Map Keys
```
type: Map<String, Object>
```
| Key | Type |  Description | Notes |
| --- | ---- | ------------ | ----- |
| **invalid-name** | Object |  | |
| **validName** | Object |  | |
| **anyStringName** | Object | any string name can be used but the value must be the correct type | [optional] |

[[Back to top]](#top) [[Back to Component Schemas]](../../../README.md#Component-Schemas) [[Back to README]](../../../README.md)
