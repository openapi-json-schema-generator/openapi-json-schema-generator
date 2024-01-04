# ObjectPropertiesValidation
org.openapijsonschematools.client.components.schemas.ObjectPropertiesValidation.java
public class ObjectPropertiesValidation

A class that contains necessary nested
- schema classes (which validate payloads), extends JsonSchema
- classes to store validated map payloads, extends FrozenMap
- classes to build inputs for map payloads

## Nested Class Summary
| Modifier and Type | Class and Description |
| ----------------- | ---------------------- |
| static class | [ObjectPropertiesValidation.ObjectPropertiesValidation1](#objectpropertiesvalidation1)<br> schema class |
| static class | [ObjectPropertiesValidation.ObjectPropertiesValidationMapBuilder](#objectpropertiesvalidationmapbuilder)<br> builder for Map payloads |
| static class | [ObjectPropertiesValidation.ObjectPropertiesValidationMap](#objectpropertiesvalidationmap)<br> output class for Map payloads |
| static class | [ObjectPropertiesValidation.Bar](#bar)<br> schema class |
| static class | [ObjectPropertiesValidation.Foo](#foo)<br> schema class |

## ObjectPropertiesValidation1
public static class ObjectPropertiesValidation1<br>
extends JsonSchema

A schema class that validates payloads

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Map<String, Class<? extends JsonSchema>> | properties = Map.ofEntries(<br>&nbsp;&nbsp;&nbsp;&nbsp;new PropertyEntry("foo", [Foo.class](#foo))),<br>&nbsp;&nbsp;&nbsp;&nbsp;new PropertyEntry("bar", [Bar.class](#bar)))<br>)<br> |

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
| [ObjectPropertiesValidationMap](#objectpropertiesvalidationmap) | validate([Map&lt;?, ?&gt;](#objectpropertiesvalidationmapbuilder) arg, SchemaConfiguration configuration) |
| FrozenList<@Nullable Object> | validate(List<?> arg, SchemaConfiguration configuration) |
| @Nullable Object | validate(@Nullable Object arg, SchemaConfiguration configuration) |
## ObjectPropertiesValidationMapBuilder
public class ObjectPropertiesValidationMapBuilder<br>
builder for `Map<String, @Nullable Object>`

A class that builds the Map input type

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| ObjectPropertiesValidationMapBuilder()<br>Creates a builder that contains an empty map |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| Map<String, @Nullable Object> | build()<br>Returns map input that should be used with Schema.validate |
| [ObjectPropertiesValidationMapBuilder](#objectpropertiesvalidationmapbuilder) | foo(int value) |
| [ObjectPropertiesValidationMapBuilder](#objectpropertiesvalidationmapbuilder) | foo(float value) |
| [ObjectPropertiesValidationMapBuilder](#objectpropertiesvalidationmapbuilder) | foo(long value) |
| [ObjectPropertiesValidationMapBuilder](#objectpropertiesvalidationmapbuilder) | foo(double value) |
| [ObjectPropertiesValidationMapBuilder](#objectpropertiesvalidationmapbuilder) | bar(String value) |
| [ObjectPropertiesValidationMapBuilder](#objectpropertiesvalidationmapbuilder) | additionalProperty(String key, Void value) |
| [ObjectPropertiesValidationMapBuilder](#objectpropertiesvalidationmapbuilder) | additionalProperty(String key, boolean value) |
| [ObjectPropertiesValidationMapBuilder](#objectpropertiesvalidationmapbuilder) | additionalProperty(String key, String value) |
| [ObjectPropertiesValidationMapBuilder](#objectpropertiesvalidationmapbuilder) | additionalProperty(String key, int value) |
| [ObjectPropertiesValidationMapBuilder](#objectpropertiesvalidationmapbuilder) | additionalProperty(String key, float value) |
| [ObjectPropertiesValidationMapBuilder](#objectpropertiesvalidationmapbuilder) | additionalProperty(String key, long value) |
| [ObjectPropertiesValidationMapBuilder](#objectpropertiesvalidationmapbuilder) | additionalProperty(String key, double value) |
| [ObjectPropertiesValidationMapBuilder](#objectpropertiesvalidationmapbuilder) | additionalProperty(String key, List<?> value) |
| [ObjectPropertiesValidationMapBuilder](#objectpropertiesvalidationmapbuilder) | additionalProperty(String key, Map<String, ?> value) |

## ObjectPropertiesValidationMap
public static class ObjectPropertiesValidationMap<br>
extends FrozenMap<String, @Nullable Object>

A class to store validated Map payloads

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| static [ObjectPropertiesValidationMap](#objectpropertiesvalidationmap) | of([Map<String, ? extends @Nullable Object>](#objectpropertiesvalidationmapbuilder) arg, SchemaConfiguration configuration) |
| Number | foo()<br>[optional] |
| String | bar()<br>[optional] |
| @Nullable Object | getAdditionalProperty(String name)<br>provides type safety for additional properties |

## Bar
public static class Bar<br>
extends StringJsonSchema

A schema class that validates payloads

| Methods Inherited from class org.openapijsonschematools.client.schemas.StringJsonSchema |
| ------------------------------------------------------------------ |
| validate                                                           |

## Foo
public static class Foo<br>
extends IntJsonSchema

A schema class that validates payloads

| Methods Inherited from class org.openapijsonschematools.client.schemas.IntJsonSchema |
| ------------------------------------------------------------------ |
| validate                                                           |

[[Back to top]](#top) [[Back to Component Schemas]](../../../README.md#Component-Schemas) [[Back to README]](../../../README.md)
