# Schema
org.openapijsonschematools.client.paths.petpetid.post.requestbody.content.applicationxwwwformurlencoded.Schema.java
public class Schema

A class that contains necessary nested schema classes, and classes to store validated list and map payloads

## Nested Class Summary
| Modifier and Type | Class and Description |
| ----------------- | ---------------------- |
| static class | [Schema.Schema1](#schema1)<br> schema class |
| static class | [Schema.SchemaMap](#schemamap)<br> output class for Map payloads |
| static class | [Schema.Status](#status)<br> schema class |
| static class | [Schema.Name](#name)<br> schema class |

## Schema1
public static class Schema1<br>
extends JsonSchema

A schema class that validates payloads
### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| static LinkedHashMap<String, KeywordValidator> |keywordToValidator<br/>new LinkedHashMap<>(Map.ofEntries(<br/>&nbsp;&nbsp;&nbsp;&nbsp;new KeywordEntry("type", new TypeValidator(Set.of(FrozenMap.class))),<br/>&nbsp;&nbsp;&nbsp;&nbsp;new KeywordEntry("properties", new PropertiesValidator(Map.ofEntries(<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;new PropertyEntry("name", [Name.class](#name))),<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;new PropertyEntry("status", [Status.class](#status)))<br>&nbsp;&nbsp;&nbsp;&nbsp;)))<br>)); |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| static [SchemaMap](#schemamap) | validate(Map<String, Object> arg, SchemaConfiguration configuration) |

## SchemaMap
public static class SchemaMap<br>
extends FrozenMap<String, Object>

A class to store validated Map payloads

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| static [SchemaMap](#schemamap) | of(Map<String, Object> arg, SchemaConfiguration configuration) |
| String | name()<br>[optional] |
| String | status()<br>[optional] |
| Object | getAdditionalProperty(String name)<br>provides type safety for additional properties |

## Input Map Keys
```
type: Map<String, Object>
```
| Key | Type |  Description | Notes |
| --- | ---- | ------------ | ----- |
| **name** | String | Updated name of the pet | [optional] |
| **status** | String | Updated status of the pet | [optional] |
| **anyStringName** | Object | any string name can be used but the value must be the correct type | [optional] |

## Status
public static class Status<br>
extends StringJsonSchema

A schema class that validates payloads

## Description
Updated status of the pet

| Methods Inherited from class org.openapijsonschematools.client.schemas.StringJsonSchema |
| ------------------------------------------------------------------ |
| validate                                                           |

## Name
public static class Name<br>
extends StringJsonSchema

A schema class that validates payloads

## Description
Updated name of the pet

| Methods Inherited from class org.openapijsonschematools.client.schemas.StringJsonSchema |
| ------------------------------------------------------------------ |
| validate                                                           |
