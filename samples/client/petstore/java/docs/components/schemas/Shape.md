# Shape
org.openapijsonschematools.client.components.schemas.Shape.java
public class Shape<br>

A class that contains necessary nested
- schema classes (which validate payloads), extends JsonSchema
- sealed interfaces which store validated payloads, java version of a sum type
- boxed classes which store validated payloads, sealed permits class implementations

## Nested Class Summary
| Modifier and Type | Class and Description |
| ----------------- | ---------------------- |
| sealed interface | [Shape.Shape1Boxed](#shape1boxed)<br> sealed interface for validated payloads |
| record | [Shape.Shape1BoxedVoid](#shape1boxedvoid)<br> boxed class to store validated null payloads |
| record | [Shape.Shape1BoxedBoolean](#shape1boxedboolean)<br> boxed class to store validated boolean payloads |
| record | [Shape.Shape1BoxedNumber](#shape1boxednumber)<br> boxed class to store validated Number payloads |
| record | [Shape.Shape1BoxedString](#shape1boxedstring)<br> boxed class to store validated String payloads |
| record | [Shape.Shape1BoxedList](#shape1boxedlist)<br> boxed class to store validated List payloads |
| record | [Shape.Shape1BoxedMap](#shape1boxedmap)<br> boxed class to store validated Map payloads |
| static class | [Shape.Shape1](#shape1)<br> schema class |

## Shape1Boxed
public sealed interface Shape1Boxed<br>
permits<br>
[Shape1BoxedVoid](#shape1boxedvoid),
[Shape1BoxedBoolean](#shape1boxedboolean),
[Shape1BoxedNumber](#shape1boxednumber),
[Shape1BoxedString](#shape1boxedstring),
[Shape1BoxedList](#shape1boxedlist),
[Shape1BoxedMap](#shape1boxedmap)

sealed interface that stores validated payloads using boxed classes

## Shape1BoxedVoid
public record Shape1BoxedVoid<br>
implements [Shape1Boxed](#shape1boxed)

record that stores validated null payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| Shape1BoxedVoid(Void data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| Void | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## Shape1BoxedBoolean
public record Shape1BoxedBoolean<br>
implements [Shape1Boxed](#shape1boxed)

record that stores validated boolean payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| Shape1BoxedBoolean(boolean data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| boolean | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## Shape1BoxedNumber
public record Shape1BoxedNumber<br>
implements [Shape1Boxed](#shape1boxed)

record that stores validated Number payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| Shape1BoxedNumber(Number data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| Number | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## Shape1BoxedString
public record Shape1BoxedString<br>
implements [Shape1Boxed](#shape1boxed)

record that stores validated String payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| Shape1BoxedString(String data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| String | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## Shape1BoxedList
public record Shape1BoxedList<br>
implements [Shape1Boxed](#shape1boxed)

record that stores validated List payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| Shape1BoxedList(FrozenList<@Nullable Object> data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| FrozenList<@Nullable Object> | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## Shape1BoxedMap
public record Shape1BoxedMap<br>
implements [Shape1Boxed](#shape1boxed)

record that stores validated Map payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| Shape1BoxedMap(FrozenMap<@Nullable Object> data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| FrozenMap<@Nullable Object> | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## Shape1
public static class Shape1<br>
extends JsonSchema

A schema class that validates payloads

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| List<Class<? extends JsonSchema>> | oneOf = List.of(<br>&nbsp;&nbsp;&nbsp;&nbsp;[Triangle.Triangle1.class](../../components/schemas/Triangle.md#triangle1),<br>&nbsp;&nbsp;&nbsp;&nbsp;[Quadrilateral.Quadrilateral1.class](../../components/schemas/Quadrilateral.md#quadrilateral1)<br>))<br> |

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
| [Shape1BoxedString](#shape1boxedstring) | validateAndBox(String arg, SchemaConfiguration configuration) |
| [Shape1BoxedVoid](#shape1boxedvoid) | validateAndBox(Void arg, SchemaConfiguration configuration) |
| [Shape1BoxedNumber](#shape1boxednumber) | validateAndBox(Number arg, SchemaConfiguration configuration) |
| [Shape1BoxedBoolean](#shape1boxedboolean) | validateAndBox(boolean arg, SchemaConfiguration configuration) |
| [Shape1BoxedMap](#shape1boxedmap) | validateAndBox(Map&lt;?, ?&gt; arg, SchemaConfiguration configuration) |
| [Shape1BoxedList](#shape1boxedlist) | validateAndBox(List<?> arg, SchemaConfiguration configuration) |
| [Shape1Boxed](#shape1boxed) | validateAndBox(@Nullable Object arg, SchemaConfiguration configuration) |
| @Nullable Object | validate(@Nullable Object arg, SchemaConfiguration configuration) |

[[Back to top]](#top) [[Back to Component Schemas]](../../../README.md#Component-Schemas) [[Back to README]](../../../README.md)
