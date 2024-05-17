# PatternpropertiesValidatesPropertiesMatchingARegex
org.openapijsonschematools.client.components.schemas.PatternpropertiesValidatesPropertiesMatchingARegex.java
class PatternpropertiesValidatesPropertiesMatchingARegex<br>

A class that contains necessary nested
- schema classes (which validate payloads), extends JsonSchema
- sealed interfaces which store validated payloads, Kotlin version of a sum type
- boxed classes which store validated payloads, sealed permits class implementations

## Nested Class Summary
| Modifier and Type | Class and Description |
| ----------------- | ---------------------- |
| sealed interface | [PatternpropertiesValidatesPropertiesMatchingARegex.PatternpropertiesValidatesPropertiesMatchingARegex1Boxed](#patternpropertiesvalidatespropertiesmatchingaregex1boxed)<br> sealed interface for validated payloads |
| record | [PatternpropertiesValidatesPropertiesMatchingARegex.PatternpropertiesValidatesPropertiesMatchingARegex1BoxedVoid](#patternpropertiesvalidatespropertiesmatchingaregex1boxedvoid)<br> boxed class to store validated null payloads |
| record | [PatternpropertiesValidatesPropertiesMatchingARegex.PatternpropertiesValidatesPropertiesMatchingARegex1BoxedBoolean](#patternpropertiesvalidatespropertiesmatchingaregex1boxedboolean)<br> boxed class to store validated boolean payloads |
| record | [PatternpropertiesValidatesPropertiesMatchingARegex.PatternpropertiesValidatesPropertiesMatchingARegex1BoxedNumber](#patternpropertiesvalidatespropertiesmatchingaregex1boxednumber)<br> boxed class to store validated Number payloads |
| record | [PatternpropertiesValidatesPropertiesMatchingARegex.PatternpropertiesValidatesPropertiesMatchingARegex1BoxedString](#patternpropertiesvalidatespropertiesmatchingaregex1boxedstring)<br> boxed class to store validated String payloads |
| record | [PatternpropertiesValidatesPropertiesMatchingARegex.PatternpropertiesValidatesPropertiesMatchingARegex1BoxedList](#patternpropertiesvalidatespropertiesmatchingaregex1boxedlist)<br> boxed class to store validated List payloads |
| record | [PatternpropertiesValidatesPropertiesMatchingARegex.PatternpropertiesValidatesPropertiesMatchingARegex1BoxedMap](#patternpropertiesvalidatespropertiesmatchingaregex1boxedmap)<br> boxed class to store validated Map payloads |
| static class | [PatternpropertiesValidatesPropertiesMatchingARegex.PatternpropertiesValidatesPropertiesMatchingARegex1](#patternpropertiesvalidatespropertiesmatchingaregex1)<br> schema class |
| sealed interface | [PatternpropertiesValidatesPropertiesMatchingARegex.FoBoxed](#foboxed)<br> sealed interface for validated payloads |
| record | [PatternpropertiesValidatesPropertiesMatchingARegex.FoBoxedNumber](#foboxednumber)<br> boxed class to store validated Number payloads |
| static class | [PatternpropertiesValidatesPropertiesMatchingARegex.Fo](#fo)<br> schema class |

## PatternpropertiesValidatesPropertiesMatchingARegex1Boxed
sealed interface PatternpropertiesValidatesPropertiesMatchingARegex1Boxed<br>
permits<br>
[PatternpropertiesValidatesPropertiesMatchingARegex1BoxedVoid](#patternpropertiesvalidatespropertiesmatchingaregex1boxedvoid),
[PatternpropertiesValidatesPropertiesMatchingARegex1BoxedBoolean](#patternpropertiesvalidatespropertiesmatchingaregex1boxedboolean),
[PatternpropertiesValidatesPropertiesMatchingARegex1BoxedNumber](#patternpropertiesvalidatespropertiesmatchingaregex1boxednumber),
[PatternpropertiesValidatesPropertiesMatchingARegex1BoxedString](#patternpropertiesvalidatespropertiesmatchingaregex1boxedstring),
[PatternpropertiesValidatesPropertiesMatchingARegex1BoxedList](#patternpropertiesvalidatespropertiesmatchingaregex1boxedlist),
[PatternpropertiesValidatesPropertiesMatchingARegex1BoxedMap](#patternpropertiesvalidatespropertiesmatchingaregex1boxedmap)

sealed interface that stores validated payloads using boxed classes

## PatternpropertiesValidatesPropertiesMatchingARegex1BoxedVoid
data class PatternpropertiesValidatesPropertiesMatchingARegex1BoxedVoid<br>
implements [PatternpropertiesValidatesPropertiesMatchingARegex1Boxed](#patternpropertiesvalidatespropertiesmatchingaregex1boxed)

data class that stores validated null payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| PatternpropertiesValidatesPropertiesMatchingARegex1BoxedVoid(Nothing? data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| Nothing? | data()<br>validated payload |
| Any? | getData()<br>validated payload |

## PatternpropertiesValidatesPropertiesMatchingARegex1BoxedBoolean
data class PatternpropertiesValidatesPropertiesMatchingARegex1BoxedBoolean<br>
implements [PatternpropertiesValidatesPropertiesMatchingARegex1Boxed](#patternpropertiesvalidatespropertiesmatchingaregex1boxed)

record that stores validated boolean payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| PatternpropertiesValidatesPropertiesMatchingARegex1BoxedBoolean(boolean data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| boolean | data()<br>validated payload |
| Any? | getData()<br>validated payload |

## PatternpropertiesValidatesPropertiesMatchingARegex1BoxedNumber
data class PatternpropertiesValidatesPropertiesMatchingARegex1BoxedNumber<br>
implements [PatternpropertiesValidatesPropertiesMatchingARegex1Boxed](#patternpropertiesvalidatespropertiesmatchingaregex1boxed)

data class that stores validated Number payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| PatternpropertiesValidatesPropertiesMatchingARegex1BoxedNumber(Number data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| Number | data()<br>validated payload |
| Any? | getData()<br>validated payload |

## PatternpropertiesValidatesPropertiesMatchingARegex1BoxedString
data class PatternpropertiesValidatesPropertiesMatchingARegex1BoxedString<br>
implements [PatternpropertiesValidatesPropertiesMatchingARegex1Boxed](#patternpropertiesvalidatespropertiesmatchingaregex1boxed)

data class that stores validated String payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| PatternpropertiesValidatesPropertiesMatchingARegex1BoxedString(String data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| String | data()<br>validated payload |
| Any? | getData()<br>validated payload |

## PatternpropertiesValidatesPropertiesMatchingARegex1BoxedList
data class PatternpropertiesValidatesPropertiesMatchingARegex1BoxedList<br>
implements [PatternpropertiesValidatesPropertiesMatchingARegex1Boxed](#patternpropertiesvalidatespropertiesmatchingaregex1boxed)

data class that stores validated List payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| PatternpropertiesValidatesPropertiesMatchingARegex1BoxedList(FrozenList<Any?> data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| FrozenList<Any?> | data()<br>validated payload |
| Any? | getData()<br>validated payload |

## PatternpropertiesValidatesPropertiesMatchingARegex1BoxedMap
data class PatternpropertiesValidatesPropertiesMatchingARegex1BoxedMap<br>
implements [PatternpropertiesValidatesPropertiesMatchingARegex1Boxed](#patternpropertiesvalidatespropertiesmatchingaregex1boxed)

data class that stores validated Map payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| PatternpropertiesValidatesPropertiesMatchingARegex1BoxedMap(FrozenMap<Any?> data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| FrozenMap<Any?> | data()<br>validated payload |
| Any? | getData()<br>validated payload |

## PatternpropertiesValidatesPropertiesMatchingARegex1
class PatternpropertiesValidatesPropertiesMatchingARegex1<br>
extends JsonSchema

A schema class that validates payloads

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Map<Pattern, Class<? extends JsonSchema>> | patternProperties = mapOf(<br>&nbsp;&nbsp;&nbsp;&nbsp;Pattern.compile("f.*o") to [Fo::class.java](#fo))<br>)<br> |

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
| [PatternpropertiesValidatesPropertiesMatchingARegex1BoxedString](#patternpropertiesvalidatespropertiesmatchingaregex1boxedstring) | validateAndBox(String, configuration: SchemaConfiguration) |
| [PatternpropertiesValidatesPropertiesMatchingARegex1BoxedVoid](#patternpropertiesvalidatespropertiesmatchingaregex1boxedvoid) | validateAndBox(Nothing?, configuration: SchemaConfiguration) |
| [PatternpropertiesValidatesPropertiesMatchingARegex1BoxedNumber](#patternpropertiesvalidatespropertiesmatchingaregex1boxednumber) | validateAndBox(Number, configuration: SchemaConfiguration) |
| [PatternpropertiesValidatesPropertiesMatchingARegex1BoxedBoolean](#patternpropertiesvalidatespropertiesmatchingaregex1boxedboolean) | validateAndBox(boolean, configuration: SchemaConfiguration) |
| [PatternpropertiesValidatesPropertiesMatchingARegex1BoxedMap](#patternpropertiesvalidatespropertiesmatchingaregex1boxedmap) | validateAndBox(Map&lt;?, ?&gt;, configuration: SchemaConfiguration) |
| [PatternpropertiesValidatesPropertiesMatchingARegex1BoxedList](#patternpropertiesvalidatespropertiesmatchingaregex1boxedlist) | validateAndBox(List<*>, configuration: SchemaConfiguration) |
| [PatternpropertiesValidatesPropertiesMatchingARegex1Boxed](#patternpropertiesvalidatespropertiesmatchingaregex1boxed) | validateAndBox(Any?, configuration: SchemaConfiguration) |
| Any? | validate(arg: Any?, configuration: SchemaConfiguration) |

## FoBoxed
sealed interface FoBoxed<br>
permits<br>
[FoBoxedNumber](#foboxednumber)

sealed interface that stores validated payloads using boxed classes

## FoBoxedNumber
data class FoBoxedNumber<br>
implements [FoBoxed](#foboxed)

data class that stores validated Number payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| FoBoxedNumber(Number data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| Number | data()<br>validated payload |
| Any? | getData()<br>validated payload |

## Fo
class Fo<br>
extends IntJsonSchema.IntJsonSchema1

A schema class that validates payloads

| Methods Inherited from class org.openapijsonschematools.client.schemas.IntJsonSchema.IntJsonSchema1 |
| ------------------------------------------------------------------ |
| validate                                                           |
| validateAndBox                                                     |

[[Back to top]](#top) [[Back to Component Schemas]](../../../README.md#Component-Schemas) [[Back to README]](../../../README.md)
