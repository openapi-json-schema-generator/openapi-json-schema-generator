# RefInAllof
org.openapijsonschematools.client.components.schemas.RefInAllof.java
public class RefInAllof<br>

A class that contains necessary nested
- schema classes (which validate payloads), extends JsonSchema
- sealed interfaces which store validated payloads, java version of a sum type
- boxed classes which store validated payloads, sealed permits class implementations

## Nested Class Summary
| Modifier and Type | Class and Description |
| ----------------- | ---------------------- |
| sealed interface | [RefInAllof.RefInAllof1Boxed](#refinallof1boxed)<br> sealed interface for validated payloads |
| record | [RefInAllof.RefInAllof1BoxedVoid](#refinallof1boxedvoid)<br> boxed class to store validated null payloads |
| record | [RefInAllof.RefInAllof1BoxedBoolean](#refinallof1boxedboolean)<br> boxed class to store validated boolean payloads |
| record | [RefInAllof.RefInAllof1BoxedNumber](#refinallof1boxednumber)<br> boxed class to store validated Number payloads |
| record | [RefInAllof.RefInAllof1BoxedString](#refinallof1boxedstring)<br> boxed class to store validated String payloads |
| record | [RefInAllof.RefInAllof1BoxedList](#refinallof1boxedlist)<br> boxed class to store validated List payloads |
| record | [RefInAllof.RefInAllof1BoxedMap](#refinallof1boxedmap)<br> boxed class to store validated Map payloads |
| static class | [RefInAllof.RefInAllof1](#refinallof1)<br> schema class |

## RefInAllof1Boxed
public sealed interface RefInAllof1Boxed<br>
permits<br>
[RefInAllof1BoxedVoid](#refinallof1boxedvoid),
[RefInAllof1BoxedBoolean](#refinallof1boxedboolean),
[RefInAllof1BoxedNumber](#refinallof1boxednumber),
[RefInAllof1BoxedString](#refinallof1boxedstring),
[RefInAllof1BoxedList](#refinallof1boxedlist),
[RefInAllof1BoxedMap](#refinallof1boxedmap)

sealed interface that stores validated payloads using boxed classes

## RefInAllof1BoxedVoid
public record RefInAllof1BoxedVoid<br>
implements [RefInAllof1Boxed](#refinallof1boxed)

record that stores validated null payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| RefInAllof1BoxedVoid(Void data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| Void | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## RefInAllof1BoxedBoolean
public record RefInAllof1BoxedBoolean<br>
implements [RefInAllof1Boxed](#refinallof1boxed)

record that stores validated boolean payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| RefInAllof1BoxedBoolean(boolean data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| boolean | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## RefInAllof1BoxedNumber
public record RefInAllof1BoxedNumber<br>
implements [RefInAllof1Boxed](#refinallof1boxed)

record that stores validated Number payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| RefInAllof1BoxedNumber(Number data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| Number | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## RefInAllof1BoxedString
public record RefInAllof1BoxedString<br>
implements [RefInAllof1Boxed](#refinallof1boxed)

record that stores validated String payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| RefInAllof1BoxedString(String data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| String | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## RefInAllof1BoxedList
public record RefInAllof1BoxedList<br>
implements [RefInAllof1Boxed](#refinallof1boxed)

record that stores validated List payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| RefInAllof1BoxedList(FrozenList<@Nullable Object> data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| FrozenList<@Nullable Object> | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## RefInAllof1BoxedMap
public record RefInAllof1BoxedMap<br>
implements [RefInAllof1Boxed](#refinallof1boxed)

record that stores validated Map payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| RefInAllof1BoxedMap(FrozenMap<@Nullable Object> data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| FrozenMap<@Nullable Object> | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## RefInAllof1
public static class RefInAllof1<br>
extends JsonSchema

A schema class that validates payloads

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| List<Class<? extends JsonSchema>> | allOf = List.of(<br>&nbsp;&nbsp;&nbsp;&nbsp;[PropertyNamedRefThatIsNotAReference.PropertyNamedRefThatIsNotAReference1.class](../../components/schemas/PropertyNamedRefThatIsNotAReference.md#propertynamedrefthatisnotareference1)<br>;)<br> |

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
| [RefInAllof1BoxedString](#refinallof1boxedstring) | validateAndBox(String arg, SchemaConfiguration configuration) |
| [RefInAllof1BoxedVoid](#refinallof1boxedvoid) | validateAndBox(Void arg, SchemaConfiguration configuration) |
| [RefInAllof1BoxedNumber](#refinallof1boxednumber) | validateAndBox(Number arg, SchemaConfiguration configuration) |
| [RefInAllof1BoxedBoolean](#refinallof1boxedboolean) | validateAndBox(boolean arg, SchemaConfiguration configuration) |
| [RefInAllof1BoxedMap](#refinallof1boxedmap) | validateAndBox(Map&lt;?, ?&gt; arg, SchemaConfiguration configuration) |
| [RefInAllof1BoxedList](#refinallof1boxedlist) | validateAndBox(List<?> arg, SchemaConfiguration configuration) |
| [RefInAllof1Boxed](#refinallof1boxed) | validateAndBox(@Nullable Object arg, SchemaConfiguration configuration) |
| @Nullable Object | validate(@Nullable Object arg, SchemaConfiguration configuration) |

[[Back to top]](#top) [[Back to Component Schemas]](../../../README.md#Component-Schemas) [[Back to README]](../../../README.md)
