# HostnameFormat
org.openapijsonschematools.client.components.schemas.HostnameFormat.java
class HostnameFormat<br>

A class that contains necessary nested
- schema classes (which validate payloads), extends JsonSchema
- sealed interfaces which store validated payloads, Kotlin version of a sum type
- boxed classes which store validated payloads, sealed permits class implementations

## Nested Class Summary
| Modifier and Type | Class and Description |
| ----------------- | ---------------------- |
| sealed interface | [HostnameFormat.HostnameFormat1Boxed](#hostnameformat1boxed)<br> sealed interface for validated payloads |
| data class | [HostnameFormat.HostnameFormat1BoxedVoid](#hostnameformat1boxedvoid)<br> boxed class to store validated null payloads |
| data class | [HostnameFormat.HostnameFormat1BoxedBoolean](#hostnameformat1boxedboolean)<br> boxed class to store validated boolean payloads |
| data class | [HostnameFormat.HostnameFormat1BoxedNumber](#hostnameformat1boxednumber)<br> boxed class to store validated Number payloads |
| data class | [HostnameFormat.HostnameFormat1BoxedString](#hostnameformat1boxedstring)<br> boxed class to store validated String payloads |
| data class | [HostnameFormat.HostnameFormat1BoxedList](#hostnameformat1boxedlist)<br> boxed class to store validated List payloads |
| data class | [HostnameFormat.HostnameFormat1BoxedMap](#hostnameformat1boxedmap)<br> boxed class to store validated Map payloads |
| class | [HostnameFormat.HostnameFormat1](#hostnameformat1)<br> schema class |

## HostnameFormat1Boxed
sealed interface HostnameFormat1Boxed<br>
permits<br>
[HostnameFormat1BoxedVoid](#hostnameformat1boxedvoid),
[HostnameFormat1BoxedBoolean](#hostnameformat1boxedboolean),
[HostnameFormat1BoxedNumber](#hostnameformat1boxednumber),
[HostnameFormat1BoxedString](#hostnameformat1boxedstring),
[HostnameFormat1BoxedList](#hostnameformat1boxedlist),
[HostnameFormat1BoxedMap](#hostnameformat1boxedmap)

sealed interface that stores validated payloads using boxed classes

## HostnameFormat1BoxedVoid
data class HostnameFormat1BoxedVoid<br>
implements [HostnameFormat1Boxed](#hostnameformat1boxed)

data class that stores validated null payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| HostnameFormat1BoxedVoid(Nothing? data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| Nothing? | data()<br>validated payload |
| Any? | getData()<br>validated payload |

## HostnameFormat1BoxedBoolean
data class HostnameFormat1BoxedBoolean<br>
implements [HostnameFormat1Boxed](#hostnameformat1boxed)

data class that stores validated boolean payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| HostnameFormat1BoxedBoolean(boolean data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| boolean | data()<br>validated payload |
| Any? | getData()<br>validated payload |

## HostnameFormat1BoxedNumber
data class HostnameFormat1BoxedNumber<br>
implements [HostnameFormat1Boxed](#hostnameformat1boxed)

data class that stores validated Number payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| HostnameFormat1BoxedNumber(Number data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| Number | data()<br>validated payload |
| Any? | getData()<br>validated payload |

## HostnameFormat1BoxedString
data class HostnameFormat1BoxedString<br>
implements [HostnameFormat1Boxed](#hostnameformat1boxed)

data class that stores validated String payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| HostnameFormat1BoxedString(String data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| String | data()<br>validated payload |
| Any? | getData()<br>validated payload |

## HostnameFormat1BoxedList
data class HostnameFormat1BoxedList<br>
implements [HostnameFormat1Boxed](#hostnameformat1boxed)

data class that stores validated List payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| HostnameFormat1BoxedList(FrozenList<Any?> data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| FrozenList<Any?> | data()<br>validated payload |
| Any? | getData()<br>validated payload |

## HostnameFormat1BoxedMap
data class HostnameFormat1BoxedMap<br>
implements [HostnameFormat1Boxed](#hostnameformat1boxed)

data class that stores validated Map payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| HostnameFormat1BoxedMap(FrozenMap<Any?> data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| FrozenMap<Any?> | data()<br>validated payload |
| Any? | getData()<br>validated payload |

## HostnameFormat1
class HostnameFormat1<br>
extends JsonSchema

A schema class that validates payloads

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| String | type = "hostname"; |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| String | validate(arg: String, configuration: SchemaConfiguration) |
| Nothing? | validate(arg: Nothing?, configuration: SchemaConfiguration) |
| Int | validate(arg: Int, configuration: SchemaConfiguration) |
| Long | validate(arg: Long, configuration: SchemaConfiguration) |
| Float | validate(arg: Float, configuration: SchemaConfiguration) |
| Double | validate(arg: Double, configuration: SchemaConfiguration) |
| Number | validate(arg: Number, configuration: SchemaConfiguration) |
| Boolean | validate(arg: Boolean, configuration: SchemaConfiguration) |
| FrozenMap<Any?> | validate(arg: Map&lt;*, *&gt;, configuration: SchemaConfiguration) |
| FrozenList<Any?> | validate(arg: List<*>, configuration: SchemaConfiguration) |
| [HostnameFormat1BoxedString](#hostnameformat1boxedstring) | validateAndBox(String, configuration: SchemaConfiguration) |
| [HostnameFormat1BoxedVoid](#hostnameformat1boxedvoid) | validateAndBox(Nothing?, configuration: SchemaConfiguration) |
| [HostnameFormat1BoxedNumber](#hostnameformat1boxednumber) | validateAndBox(Number, configuration: SchemaConfiguration) |
| [HostnameFormat1BoxedBoolean](#hostnameformat1boxedboolean) | validateAndBox(Boolean, configuration: SchemaConfiguration) |
| [HostnameFormat1BoxedMap](#hostnameformat1boxedmap) | validateAndBox(Map&lt;*, *&gt;, configuration: SchemaConfiguration) |
| [HostnameFormat1BoxedList](#hostnameformat1boxedlist) | validateAndBox(List<*>, configuration: SchemaConfiguration) |
| [HostnameFormat1Boxed](#hostnameformat1boxed) | validateAndBox(Any?, configuration: SchemaConfiguration) |
| Any? | validate(arg: Any?, configuration: SchemaConfiguration) |

[[Back to top]](#top) [[Back to Component Schemas]](../../../README.md#Component-Schemas) [[Back to README]](../../../README.md)
