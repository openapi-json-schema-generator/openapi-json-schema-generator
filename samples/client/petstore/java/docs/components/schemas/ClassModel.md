# ClassModel
org.openapijsonschematools.client.components.schemas.ClassModel.java
public class ClassModel

A class that contains necessary nested
- schema classes (which validate payloads), extends JsonSchema
- classes to store validated map payloads, extends FrozenMap
- classes to build inputs for map payloads

## Nested Class Summary
| Modifier and Type | Class and Description |
| ----------------- | ---------------------- |
| static class | [ClassModel.ClassModel1](#classmodel1)<br> schema class |
| static class | [ClassModel.ClassModelMapBuilder](#classmodelmapbuilder)<br> builder for Map payloads |
| static class | [ClassModel.ClassModelMap](#classmodelmap)<br> output class for Map payloads |
| static class | [ClassModel.ClassSchema](#classschema)<br> schema class |

## ClassModel1
public static class ClassModel1<br>
extends JsonSchema

A schema class that validates payloads

## Description
Model for testing model with &quot;_class&quot; property

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Map<String, Class<? extends JsonSchema>> | properties = Map.ofEntries(<br>&nbsp;&nbsp;&nbsp;&nbsp;new PropertyEntry("_class", [ClassSchema.class](#classschema)))<br>)<br> |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| String | validate(String arg, SchemaConfiguration configuration) |
| Void | validate(Void arg, SchemaConfiguration configuration) |
| int | validate(int arg, SchemaConfiguration configuration) |
| long | validate(long arg, SchemaConfiguration configuration) |
| float | validate(float arg, SchemaConfiguration configuration) |
| double | validate(double arg, SchemaConfiguration configuration) |
| boolean | validate(boolean arg, SchemaConfiguration configuration) |
| [ClassModelMap](#classmodelmap) | validate([Map<?, ?>](#classmodelmapbuilder) arg, SchemaConfiguration configuration) |
| FrozenList<@Nullable Object> | validate(List<?> arg, SchemaConfiguration configuration) |
| @Nullable Object | validate(@Nullable Object arg, SchemaConfiguration configuration) |
## ClassModelMapBuilder
public class ClassModelMapBuilder<br>
builder for `Map<String, ? extends @Nullable Object>`

A class that builds the Map input type

## Input Map Keys
| Key | Type |  Description | Notes |
| --- | ---- | ------------ | ----- |
| **_class** | String |  | [optional] |
| **anyStringName** | Object | any string name can be used but the value must be the correct type | [optional] |

## ClassModelMap
public static class ClassModelMap<br>
extends FrozenMap<String, @Nullable Object>

A class to store validated Map payloads

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| static [ClassModelMap](#classmodelmap) | of([Map<String, ? extends @Nullable Object>](#classmodelmapbuilder) arg, SchemaConfiguration configuration) |
| @Nullable Object | get(String key)<br>This schema has invalid Java names so this method must be used when you access instance["_class"],  |
| Object | getAdditionalProperty(String name)<br>provides type safety for additional properties |

## ClassSchema
public static class ClassSchema<br>
extends StringJsonSchema

A schema class that validates payloads

| Methods Inherited from class org.openapijsonschematools.client.schemas.StringJsonSchema |
| ------------------------------------------------------------------ |
| validate                                                           |

[[Back to top]](#top) [[Back to Component Schemas]](../../../README.md#Component-Schemas) [[Back to README]](../../../README.md)
