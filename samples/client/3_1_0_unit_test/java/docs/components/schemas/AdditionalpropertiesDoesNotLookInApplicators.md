# AdditionalpropertiesDoesNotLookInApplicators
org.openapijsonschematools.client.components.schemas.AdditionalpropertiesDoesNotLookInApplicators.java
public class AdditionalpropertiesDoesNotLookInApplicators

A class that contains necessary nested
- schema classes (which validate payloads), extends JsonSchema
- classes to store validated map payloads, extends FrozenMap
- classes to build inputs for map payloads

## Nested Class Summary
| Modifier and Type | Class and Description |
| ----------------- | ---------------------- |
| static class | [AdditionalpropertiesDoesNotLookInApplicators.AdditionalpropertiesDoesNotLookInApplicators1](#additionalpropertiesdoesnotlookinapplicators1)<br> schema class |
| static class | [AdditionalpropertiesDoesNotLookInApplicators.AdditionalpropertiesDoesNotLookInApplicatorsMapBuilder](#additionalpropertiesdoesnotlookinapplicatorsmapbuilder)<br> builder for Map payloads |
| static class | [AdditionalpropertiesDoesNotLookInApplicators.AdditionalpropertiesDoesNotLookInApplicatorsMap](#additionalpropertiesdoesnotlookinapplicatorsmap)<br> output class for Map payloads |
| static class | [AdditionalpropertiesDoesNotLookInApplicators.Schema0](#schema0)<br> schema class |
| static class | [AdditionalpropertiesDoesNotLookInApplicators.Schema0MapBuilder](#schema0mapbuilder)<br> builder for Map payloads |
| static class | [AdditionalpropertiesDoesNotLookInApplicators.Schema0Map](#schema0map)<br> output class for Map payloads |
| static class | [AdditionalpropertiesDoesNotLookInApplicators.Foo](#foo)<br> schema class |
| static class | [AdditionalpropertiesDoesNotLookInApplicators.AdditionalProperties](#additionalproperties)<br> schema class |

## AdditionalpropertiesDoesNotLookInApplicators1
public static class AdditionalpropertiesDoesNotLookInApplicators1<br>
extends JsonSchema

A schema class that validates payloads

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Class<? extends JsonSchema> | additionalProperties = [AdditionalProperties.class](#additionalproperties) |
| List<Class<? extends JsonSchema>> | allOf = List.of(<br>&nbsp;&nbsp;&nbsp;&nbsp;[Schema0.class](#schema0)<br>;)<br> |

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
| [AdditionalpropertiesDoesNotLookInApplicatorsMap](#additionalpropertiesdoesnotlookinapplicatorsmap) | validate([Map&lt;?, ?&gt;](#additionalpropertiesdoesnotlookinapplicatorsmapbuilder) arg, SchemaConfiguration configuration) |
| FrozenList<@Nullable Object> | validate(List<?> arg, SchemaConfiguration configuration) |
| @Nullable Object | validate(@Nullable Object arg, SchemaConfiguration configuration) |
## AdditionalpropertiesDoesNotLookInApplicatorsMapBuilder
public class AdditionalpropertiesDoesNotLookInApplicatorsMapBuilder<br>
builder for `Map<String, Boolean>`

A class that builds the Map input type

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| AdditionalpropertiesDoesNotLookInApplicatorsMapBuilder()<br>Creates a builder that contains an empty map |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| Map<String, Boolean> | build()<br>Returns map input that should be used with Schema.validate |
| [AdditionalpropertiesDoesNotLookInApplicatorsMapBuilder](#additionalpropertiesdoesnotlookinapplicatorsmapbuilder) | additionalProperty(String key, boolean value) |

## AdditionalpropertiesDoesNotLookInApplicatorsMap
public static class AdditionalpropertiesDoesNotLookInApplicatorsMap<br>
extends FrozenMap<String, Boolean>

A class to store validated Map payloads

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| static [AdditionalpropertiesDoesNotLookInApplicatorsMap](#additionalpropertiesdoesnotlookinapplicatorsmap) | of([Map<String, Boolean>](#additionalpropertiesdoesnotlookinapplicatorsmapbuilder) arg, SchemaConfiguration configuration) |
| boolean | getAdditionalProperty(String name)<br>provides type safety for additional properties |

## Schema0
public static class Schema0<br>
extends JsonSchema

A schema class that validates payloads

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Map<String, Class<? extends JsonSchema>> | properties = Map.ofEntries(<br>&nbsp;&nbsp;&nbsp;&nbsp;new PropertyEntry("foo", [Foo.class](#foo)))<br>)<br> |

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
| [Schema0Map](#schema0map) | validate([Map&lt;?, ?&gt;](#schema0mapbuilder) arg, SchemaConfiguration configuration) |
| FrozenList<@Nullable Object> | validate(List<?> arg, SchemaConfiguration configuration) |
| @Nullable Object | validate(@Nullable Object arg, SchemaConfiguration configuration) |
## Schema0MapBuilder
public class Schema0MapBuilder<br>
builder for `Map<String, @Nullable Object>`

A class that builds the Map input type

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| Schema0MapBuilder()<br>Creates a builder that contains an empty map |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| Map<String, @Nullable Object> | build()<br>Returns map input that should be used with Schema.validate |
| [Schema0MapBuilder](#schema0mapbuilder) | foo(Void value) |
| [Schema0MapBuilder](#schema0mapbuilder) | foo(boolean value) |
| [Schema0MapBuilder](#schema0mapbuilder) | foo(String value) |
| [Schema0MapBuilder](#schema0mapbuilder) | foo(int value) |
| [Schema0MapBuilder](#schema0mapbuilder) | foo(float value) |
| [Schema0MapBuilder](#schema0mapbuilder) | foo(long value) |
| [Schema0MapBuilder](#schema0mapbuilder) | foo(double value) |
| [Schema0MapBuilder](#schema0mapbuilder) | foo(List<?> value) |
| [Schema0MapBuilder](#schema0mapbuilder) | foo(Map<String, ?> value) |
| [Schema0MapBuilder](#schema0mapbuilder) | additionalProperty(String key, Void value) |
| [Schema0MapBuilder](#schema0mapbuilder) | additionalProperty(String key, boolean value) |
| [Schema0MapBuilder](#schema0mapbuilder) | additionalProperty(String key, String value) |
| [Schema0MapBuilder](#schema0mapbuilder) | additionalProperty(String key, int value) |
| [Schema0MapBuilder](#schema0mapbuilder) | additionalProperty(String key, float value) |
| [Schema0MapBuilder](#schema0mapbuilder) | additionalProperty(String key, long value) |
| [Schema0MapBuilder](#schema0mapbuilder) | additionalProperty(String key, double value) |
| [Schema0MapBuilder](#schema0mapbuilder) | additionalProperty(String key, List<?> value) |
| [Schema0MapBuilder](#schema0mapbuilder) | additionalProperty(String key, Map<String, ?> value) |

## Schema0Map
public static class Schema0Map<br>
extends FrozenMap<String, @Nullable Object>

A class to store validated Map payloads

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| static [Schema0Map](#schema0map) | of([Map<String, ? extends @Nullable Object>](#schema0mapbuilder) arg, SchemaConfiguration configuration) |
| @Nullable Object | foo()<br>[optional] |
| @Nullable Object | getAdditionalProperty(String name)<br>provides type safety for additional properties |

## Foo
public static class Foo<br>
extends AnyTypeJsonSchema

A schema class that validates payloads

| Methods Inherited from class org.openapijsonschematools.client.schemas.AnyTypeJsonSchema |
| ------------------------------------------------------------------ |
| validate                                                           |

## AdditionalProperties
public static class AdditionalProperties<br>
extends BooleanJsonSchema

A schema class that validates payloads

| Methods Inherited from class org.openapijsonschematools.client.schemas.BooleanJsonSchema |
| ------------------------------------------------------------------ |
| validate                                                           |

[[Back to top]](#top) [[Back to Component Schemas]](../../../README.md#Component-Schemas) [[Back to README]](../../../README.md)
