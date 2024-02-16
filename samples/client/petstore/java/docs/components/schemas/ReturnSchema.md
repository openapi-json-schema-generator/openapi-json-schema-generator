# ReturnSchema
org.openapijsonschematools.client.components.schemas.ReturnSchema.java
public class ReturnSchema<br>

A class that contains necessary nested
- schema classes (which validate payloads), extends JsonSchema
- abstract sealed classes which store validated payloads, java version of a sum type
- boxed classes which store validated payloads, sealed permits class implementations
- classes to store validated map payloads, extends FrozenMap
- classes to build inputs for map payloads

## Nested Class Summary
| Modifier and Type | Class and Description |
| ----------------- | ---------------------- |
| static class | [ReturnSchema.ReturnSchema1Boxed](#returnschema1boxed)<br> abstract sealed validated payload class |
| static class | [ReturnSchema.ReturnSchema1BoxedVoid](#returnschema1boxedvoid)<br> boxed class to store validated null payloads |
| static class | [ReturnSchema.ReturnSchema1BoxedBoolean](#returnschema1boxedboolean)<br> boxed class to store validated boolean payloads |
| static class | [ReturnSchema.ReturnSchema1BoxedNumber](#returnschema1boxednumber)<br> boxed class to store validated Number payloads |
| static class | [ReturnSchema.ReturnSchema1BoxedString](#returnschema1boxedstring)<br> boxed class to store validated String payloads |
| static class | [ReturnSchema.ReturnSchema1BoxedList](#returnschema1boxedlist)<br> boxed class to store validated List payloads |
| static class | [ReturnSchema.ReturnSchema1BoxedMap](#returnschema1boxedmap)<br> boxed class to store validated Map payloads |
| static class | [ReturnSchema.ReturnSchema1](#returnschema1)<br> schema class |
| static class | [ReturnSchema.ReturnMapBuilder1](#returnmapbuilder1)<br> builder for Map payloads |
| static class | [ReturnSchema.ReturnMap](#returnmap)<br> output class for Map payloads |
| static class | [ReturnSchema.ReturnSchema2Boxed](#returnschema2boxed)<br> abstract sealed validated payload class |
| static class | [ReturnSchema.ReturnSchema2BoxedNumber](#returnschema2boxednumber)<br> boxed class to store validated Number payloads |
| static class | [ReturnSchema.ReturnSchema2](#returnschema2)<br> schema class |

## ReturnSchema1Boxed
public static abstract sealed class ReturnSchema1Boxed<br>
permits<br>
[ReturnSchema1BoxedVoid](#returnschema1boxedvoid),
[ReturnSchema1BoxedBoolean](#returnschema1boxedboolean),
[ReturnSchema1BoxedNumber](#returnschema1boxednumber),
[ReturnSchema1BoxedString](#returnschema1boxedstring),
[ReturnSchema1BoxedList](#returnschema1boxedlist),
[ReturnSchema1BoxedMap](#returnschema1boxedmap)

abstract sealed class that stores validated payloads using boxed classes

## ReturnSchema1BoxedVoid
public static final class ReturnSchema1BoxedVoid<br>
extends [ReturnSchema1Boxed](#returnschema1boxed)

a boxed class to store validated null payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| ReturnSchema1BoxedVoid(Void data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Void | data<br>validated payload |

## ReturnSchema1BoxedBoolean
public static final class ReturnSchema1BoxedBoolean<br>
extends [ReturnSchema1Boxed](#returnschema1boxed)

a boxed class to store validated boolean payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| ReturnSchema1BoxedBoolean(boolean data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| boolean | data<br>validated payload |

## ReturnSchema1BoxedNumber
public static final class ReturnSchema1BoxedNumber<br>
extends [ReturnSchema1Boxed](#returnschema1boxed)

a boxed class to store validated Number payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| ReturnSchema1BoxedNumber(Number data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Number | data<br>validated payload |

## ReturnSchema1BoxedString
public static final class ReturnSchema1BoxedString<br>
extends [ReturnSchema1Boxed](#returnschema1boxed)

a boxed class to store validated String payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| ReturnSchema1BoxedString(String data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| String | data<br>validated payload |

## ReturnSchema1BoxedList
public static final class ReturnSchema1BoxedList<br>
extends [ReturnSchema1Boxed](#returnschema1boxed)

a boxed class to store validated List payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| ReturnSchema1BoxedList(FrozenList<@Nullable Object> data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| FrozenList<@Nullable Object> | data<br>validated payload |

## ReturnSchema1BoxedMap
public static final class ReturnSchema1BoxedMap<br>
extends [ReturnSchema1Boxed](#returnschema1boxed)

a boxed class to store validated Map payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| ReturnSchema1BoxedMap([ReturnMap](#returnmap) data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| [ReturnMap](#returnmap) | data<br>validated payload |

## ReturnSchema1
public static class ReturnSchema1<br>
extends JsonSchema

A schema class that validates payloads

## Description
Model for testing reserved words

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Map<String, Class<? extends JsonSchema>> | properties = Map.ofEntries(<br>&nbsp;&nbsp;&nbsp;&nbsp;new PropertyEntry("return", [ReturnSchema2.class](#returnschema2)))<br>)<br> |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| String | validate(String arg, SchemaConfiguration configuration) |
| Void | validate(Void arg, SchemaConfiguration configuration) |
| int | validate(int arg, SchemaConfiguration configuration) |
| long | validate(long arg, SchemaConfiguration configuration) |
| float | validate(float arg, SchemaConfiguration configuration) |
| double | validate(double arg, SchemaConfiguration configuration) |
| Number | validate(Number arg, SchemaConfiguration configuration) |
| boolean | validate(boolean arg, SchemaConfiguration configuration) |
| [ReturnMap](#returnmap) | validate([Map&lt;?, ?&gt;](#returnmapbuilder1) arg, SchemaConfiguration configuration) |
| FrozenList<@Nullable Object> | validate(List<?> arg, SchemaConfiguration configuration) |
| [ReturnSchema1BoxedString](#returnschema1boxedstring) | validateAndBox(String arg, SchemaConfiguration configuration) |
| [ReturnSchema1BoxedVoid](#returnschema1boxedvoid) | validateAndBox(Void arg, SchemaConfiguration configuration) |
| [ReturnSchema1BoxedNumber](#returnschema1boxednumber) | validateAndBox(Number arg, SchemaConfiguration configuration) |
| [ReturnSchema1BoxedBoolean](#returnschema1boxedboolean) | validateAndBox(boolean arg, SchemaConfiguration configuration) |
| [ReturnSchema1BoxedMap](#returnschema1boxedmap) | validateAndBox([Map&lt;?, ?&gt;](#returnmapbuilder1) arg, SchemaConfiguration configuration) |
| [ReturnSchema1BoxedList](#returnschema1boxedlist) | validateAndBox(List<?> arg, SchemaConfiguration configuration) |
| @Nullable Object | validate(@Nullable Object arg, SchemaConfiguration configuration) |
## ReturnMapBuilder1
public class ReturnMapBuilder1<br>
builder for `Map<String, @Nullable Object>`

A class that builds the Map input type

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| ReturnMapBuilder1()<br>Creates a builder that contains an empty map |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| Map<String, @Nullable Object> | build()<br>Returns map input that should be used with Schema.validate |
| [ReturnMapBuilder1](#returnmapbuilder1) | setReturn(int value) |
| [ReturnMapBuilder1](#returnmapbuilder1) | setReturn(float value) |
| [ReturnMapBuilder1](#returnmapbuilder1) | additionalProperty(String key, Void value) |
| [ReturnMapBuilder1](#returnmapbuilder1) | additionalProperty(String key, boolean value) |
| [ReturnMapBuilder1](#returnmapbuilder1) | additionalProperty(String key, String value) |
| [ReturnMapBuilder1](#returnmapbuilder1) | additionalProperty(String key, int value) |
| [ReturnMapBuilder1](#returnmapbuilder1) | additionalProperty(String key, float value) |
| [ReturnMapBuilder1](#returnmapbuilder1) | additionalProperty(String key, long value) |
| [ReturnMapBuilder1](#returnmapbuilder1) | additionalProperty(String key, double value) |
| [ReturnMapBuilder1](#returnmapbuilder1) | additionalProperty(String key, List<?> value) |
| [ReturnMapBuilder1](#returnmapbuilder1) | additionalProperty(String key, Map<String, ?> value) |

## ReturnMap
public static class ReturnMap<br>
extends FrozenMap<String, @Nullable Object>

A class to store validated Map payloads

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| static [ReturnMap](#returnmap) | of([Map<String, ? extends @Nullable Object>](#returnmapbuilder1) arg, SchemaConfiguration configuration) |
| @Nullable Object | get(String key)<br>This schema has invalid Java names so this method must be used when you access instance["return"],  |
| @Nullable Object | getAdditionalProperty(String name)<br>provides type safety for additional properties |

## ReturnSchema2Boxed
public static abstract sealed class ReturnSchema2Boxed<br>
permits<br>
[ReturnSchema2BoxedNumber](#returnschema2boxednumber)

abstract sealed class that stores validated payloads using boxed classes

## ReturnSchema2BoxedNumber
public static final class ReturnSchema2BoxedNumber<br>
extends [ReturnSchema2Boxed](#returnschema2boxed)

a boxed class to store validated Number payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| ReturnSchema2BoxedNumber(Number data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Number | data<br>validated payload |

## ReturnSchema2
public static class ReturnSchema2<br>
extends Int32JsonSchema.Int32JsonSchema1

A schema class that validates payloads

## Description
this is a reserved python keyword

| Methods Inherited from class org.openapijsonschematools.client.schemas.Int32JsonSchema.Int32JsonSchema1 |
| ------------------------------------------------------------------ |
| validate                                                           |
| validateAndBox                                                     |

[[Back to top]](#top) [[Back to Component Schemas]](../../../README.md#Component-Schemas) [[Back to README]](../../../README.md)
