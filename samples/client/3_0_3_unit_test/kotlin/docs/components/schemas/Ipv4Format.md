# Ipv4Format
org.openapijsonschematools.client.components.schemas.Ipv4Format.java
class Ipv4Format<br>

A class that contains necessary nested
- schema classes (which validate payloads), extends JsonSchema
- sealed interfaces which store validated payloads, Kotlin version of a sum type
- boxed classes which store validated payloads, sealed permits class implementations

## Nested Class Summary
| Modifier and Type | Class and Description |
| ----------------- | ---------------------- |
| sealed interface | [Ipv4Format.Ipv4Format1Boxed](#ipv4format1boxed)<br> sealed interface for validated payloads |
| record | [Ipv4Format.Ipv4Format1BoxedVoid](#ipv4format1boxedvoid)<br> boxed class to store validated null payloads |
| record | [Ipv4Format.Ipv4Format1BoxedBoolean](#ipv4format1boxedboolean)<br> boxed class to store validated boolean payloads |
| record | [Ipv4Format.Ipv4Format1BoxedNumber](#ipv4format1boxednumber)<br> boxed class to store validated Number payloads |
| record | [Ipv4Format.Ipv4Format1BoxedString](#ipv4format1boxedstring)<br> boxed class to store validated String payloads |
| record | [Ipv4Format.Ipv4Format1BoxedList](#ipv4format1boxedlist)<br> boxed class to store validated List payloads |
| record | [Ipv4Format.Ipv4Format1BoxedMap](#ipv4format1boxedmap)<br> boxed class to store validated Map payloads |
| static class | [Ipv4Format.Ipv4Format1](#ipv4format1)<br> schema class |

## Ipv4Format1Boxed
sealed interface Ipv4Format1Boxed<br>
permits<br>
[Ipv4Format1BoxedVoid](#ipv4format1boxedvoid),
[Ipv4Format1BoxedBoolean](#ipv4format1boxedboolean),
[Ipv4Format1BoxedNumber](#ipv4format1boxednumber),
[Ipv4Format1BoxedString](#ipv4format1boxedstring),
[Ipv4Format1BoxedList](#ipv4format1boxedlist),
[Ipv4Format1BoxedMap](#ipv4format1boxedmap)

sealed interface that stores validated payloads using boxed classes

## Ipv4Format1BoxedVoid
data class Ipv4Format1BoxedVoid<br>
implements [Ipv4Format1Boxed](#ipv4format1boxed)

data class that stores validated null payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| Ipv4Format1BoxedVoid(Nothing? data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| Nothing? | data()<br>validated payload |
| Any? | getData()<br>validated payload |

## Ipv4Format1BoxedBoolean
data class Ipv4Format1BoxedBoolean<br>
implements [Ipv4Format1Boxed](#ipv4format1boxed)

record that stores validated boolean payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| Ipv4Format1BoxedBoolean(boolean data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| boolean | data()<br>validated payload |
| Any? | getData()<br>validated payload |

## Ipv4Format1BoxedNumber
data class Ipv4Format1BoxedNumber<br>
implements [Ipv4Format1Boxed](#ipv4format1boxed)

data class that stores validated Number payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| Ipv4Format1BoxedNumber(Number data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| Number | data()<br>validated payload |
| Any? | getData()<br>validated payload |

## Ipv4Format1BoxedString
data class Ipv4Format1BoxedString<br>
implements [Ipv4Format1Boxed](#ipv4format1boxed)

data class that stores validated String payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| Ipv4Format1BoxedString(String data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| String | data()<br>validated payload |
| Any? | getData()<br>validated payload |

## Ipv4Format1BoxedList
data class Ipv4Format1BoxedList<br>
implements [Ipv4Format1Boxed](#ipv4format1boxed)

data class that stores validated List payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| Ipv4Format1BoxedList(FrozenList<Any?> data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| FrozenList<Any?> | data()<br>validated payload |
| Any? | getData()<br>validated payload |

## Ipv4Format1BoxedMap
data class Ipv4Format1BoxedMap<br>
implements [Ipv4Format1Boxed](#ipv4format1boxed)

data class that stores validated Map payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| Ipv4Format1BoxedMap(FrozenMap<Any?> data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| FrozenMap<Any?> | data()<br>validated payload |
| Any? | getData()<br>validated payload |

## Ipv4Format1
class Ipv4Format1<br>
extends JsonSchema

A schema class that validates payloads

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| String | type = "ipv4"; |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| String | validate(arg: String, configuration: SchemaConfiguration) |
| Nothing? | validate(arg: Nothing?, configuration: SchemaConfiguration) |
| int | validate(arg: int, configuration: SchemaConfiguration) |
| long | validate(arg: long, configuration: SchemaConfiguration) |
| float | validate(arg: float, configuration: SchemaConfiguration) |
| double | validate(arg: double, configuration: SchemaConfiguration) |
| Number | validate(arg: Number, configuration: SchemaConfiguration) |
| boolean | validate(arg: boolean, configuration: SchemaConfiguration) |
| FrozenMap<Any?> | validate(arg: Map&lt;?, ?&gt;, configuration: SchemaConfiguration) |
| FrozenList<Any?> | validate(arg: List<*>, configuration: SchemaConfiguration) |
| [Ipv4Format1BoxedString](#ipv4format1boxedstring) | validateAndBox(String, configuration: SchemaConfiguration) |
| [Ipv4Format1BoxedVoid](#ipv4format1boxedvoid) | validateAndBox(Nothing?, configuration: SchemaConfiguration) |
| [Ipv4Format1BoxedNumber](#ipv4format1boxednumber) | validateAndBox(Number, configuration: SchemaConfiguration) |
| [Ipv4Format1BoxedBoolean](#ipv4format1boxedboolean) | validateAndBox(boolean, configuration: SchemaConfiguration) |
| [Ipv4Format1BoxedMap](#ipv4format1boxedmap) | validateAndBox(Map&lt;?, ?&gt;, configuration: SchemaConfiguration) |
| [Ipv4Format1BoxedList](#ipv4format1boxedlist) | validateAndBox(List<*>, configuration: SchemaConfiguration) |
| [Ipv4Format1Boxed](#ipv4format1boxed) | validateAndBox(Any?, configuration: SchemaConfiguration) |
| Any? | validate(arg: Any?, configuration: SchemaConfiguration) |

[[Back to top]](#top) [[Back to Component Schemas]](../../../README.md#Component-Schemas) [[Back to README]](../../../README.md)
