# Mammal
org.openapijsonschematools.client.components.schemas.Mammal.java
public class Mammal<br>

A class that contains necessary nested
- schema classes (which validate payloads), extends JsonSchema
- sealed interfaces which store validated payloads, java version of a sum type
- boxed classes which store validated payloads, sealed permits class implementations

## Nested Class Summary
| Modifier and Type | Class and Description |
| ----------------- | ---------------------- |
| sealed interface | [Mammal.Mammal1Boxed](#mammal1boxed)<br> sealed interface for validated payloads |
| record | [Mammal.Mammal1BoxedVoid](#mammal1boxedvoid)<br> boxed class to store validated null payloads |
| record | [Mammal.Mammal1BoxedBoolean](#mammal1boxedboolean)<br> boxed class to store validated boolean payloads |
| record | [Mammal.Mammal1BoxedNumber](#mammal1boxednumber)<br> boxed class to store validated Number payloads |
| record | [Mammal.Mammal1BoxedString](#mammal1boxedstring)<br> boxed class to store validated String payloads |
| record | [Mammal.Mammal1BoxedList](#mammal1boxedlist)<br> boxed class to store validated List payloads |
| record | [Mammal.Mammal1BoxedMap](#mammal1boxedmap)<br> boxed class to store validated Map payloads |
| static class | [Mammal.Mammal1](#mammal1)<br> schema class |

## Mammal1Boxed
public sealed interface Mammal1Boxed<br>
permits<br>
[Mammal1BoxedVoid](#mammal1boxedvoid),
[Mammal1BoxedBoolean](#mammal1boxedboolean),
[Mammal1BoxedNumber](#mammal1boxednumber),
[Mammal1BoxedString](#mammal1boxedstring),
[Mammal1BoxedList](#mammal1boxedlist),
[Mammal1BoxedMap](#mammal1boxedmap)

sealed interface that stores validated payloads using boxed classes

## Mammal1BoxedVoid
public record Mammal1BoxedVoid<br>
implements [Mammal1Boxed](#mammal1boxed)

record that stores validated null payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| Mammal1BoxedVoid(Void data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| Void | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## Mammal1BoxedBoolean
public record Mammal1BoxedBoolean<br>
implements [Mammal1Boxed](#mammal1boxed)

record that stores validated boolean payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| Mammal1BoxedBoolean(boolean data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| boolean | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## Mammal1BoxedNumber
public record Mammal1BoxedNumber<br>
implements [Mammal1Boxed](#mammal1boxed)

record that stores validated Number payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| Mammal1BoxedNumber(Number data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| Number | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## Mammal1BoxedString
public record Mammal1BoxedString<br>
implements [Mammal1Boxed](#mammal1boxed)

record that stores validated String payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| Mammal1BoxedString(String data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| String | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## Mammal1BoxedList
public record Mammal1BoxedList<br>
implements [Mammal1Boxed](#mammal1boxed)

record that stores validated List payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| Mammal1BoxedList(FrozenList<@Nullable Object> data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| FrozenList<@Nullable Object> | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## Mammal1BoxedMap
public record Mammal1BoxedMap<br>
implements [Mammal1Boxed](#mammal1boxed)

record that stores validated Map payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| Mammal1BoxedMap(FrozenMap<@Nullable Object> data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| FrozenMap<@Nullable Object> | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## Mammal1
public static class Mammal1<br>
extends JsonSchema

A schema class that validates payloads

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| List<Class<? extends JsonSchema>> | oneOf = List.of(<br>&nbsp;&nbsp;&nbsp;&nbsp;[Whale.Whale1.class](../../components/schemas/Whale.md#whale1),<br>&nbsp;&nbsp;&nbsp;&nbsp;[Zebra.Zebra1.class](../../components/schemas/Zebra.md#zebra1),<br>&nbsp;&nbsp;&nbsp;&nbsp;[Pig.Pig1.class](../../components/schemas/Pig.md#pig1)<br>))<br> |

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
| FrozenMap<@Nullable Object> | validate(Map&lt;?, ?&gt; arg, SchemaConfiguration configuration) |
| FrozenList<@Nullable Object> | validate(List<?> arg, SchemaConfiguration configuration) |
| [Mammal1BoxedString](#mammal1boxedstring) | validateAndBox(String arg, SchemaConfiguration configuration) |
| [Mammal1BoxedVoid](#mammal1boxedvoid) | validateAndBox(Void arg, SchemaConfiguration configuration) |
| [Mammal1BoxedNumber](#mammal1boxednumber) | validateAndBox(Number arg, SchemaConfiguration configuration) |
| [Mammal1BoxedBoolean](#mammal1boxedboolean) | validateAndBox(boolean arg, SchemaConfiguration configuration) |
| [Mammal1BoxedMap](#mammal1boxedmap) | validateAndBox(Map&lt;?, ?&gt; arg, SchemaConfiguration configuration) |
| [Mammal1BoxedList](#mammal1boxedlist) | validateAndBox(List<?> arg, SchemaConfiguration configuration) |
| [Mammal1Boxed](#mammal1boxed) | validateAndBox(@Nullable Object arg, SchemaConfiguration configuration) |
| @Nullable Object | validate(@Nullable Object arg, SchemaConfiguration configuration) |

[[Back to top]](#top) [[Back to Component Schemas]](../../../README.md#Component-Schemas) [[Back to README]](../../../README.md)
