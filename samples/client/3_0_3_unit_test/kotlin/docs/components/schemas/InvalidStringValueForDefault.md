# InvalidStringValueForDefault
org.openapijsonschematools.client.components.schemas.InvalidStringValueForDefault.java
class InvalidStringValueForDefault<br>

A class that contains necessary nested
- schema classes (which validate payloads), extends JsonSchema
- sealed interfaces which store validated payloads, Kotlin version of a sum type
- boxed classes which store validated payloads, sealed permits class implementations
- classes to store validated map payloads, extends FrozenMap
- classes to build inputs for map payloads

## Nested Class Summary
| Modifier and Type | Class and Description |
| ----------------- | ---------------------- |
| sealed interface | [InvalidStringValueForDefault.InvalidStringValueForDefault1Boxed](#invalidstringvaluefordefault1boxed)<br> sealed interface for validated payloads |
| data class | [InvalidStringValueForDefault.InvalidStringValueForDefault1BoxedVoid](#invalidstringvaluefordefault1boxedvoid)<br> boxed class to store validated null payloads |
| data class | [InvalidStringValueForDefault.InvalidStringValueForDefault1BoxedBoolean](#invalidstringvaluefordefault1boxedboolean)<br> boxed class to store validated boolean payloads |
| data class | [InvalidStringValueForDefault.InvalidStringValueForDefault1BoxedNumber](#invalidstringvaluefordefault1boxednumber)<br> boxed class to store validated Number payloads |
| data class | [InvalidStringValueForDefault.InvalidStringValueForDefault1BoxedString](#invalidstringvaluefordefault1boxedstring)<br> boxed class to store validated String payloads |
| data class | [InvalidStringValueForDefault.InvalidStringValueForDefault1BoxedList](#invalidstringvaluefordefault1boxedlist)<br> boxed class to store validated List payloads |
| data class | [InvalidStringValueForDefault.InvalidStringValueForDefault1BoxedMap](#invalidstringvaluefordefault1boxedmap)<br> boxed class to store validated Map payloads |
| class | [InvalidStringValueForDefault.InvalidStringValueForDefault1](#invalidstringvaluefordefault1)<br> schema class |
| class | [InvalidStringValueForDefault.InvalidStringValueForDefaultMapBuilder](#invalidstringvaluefordefaultmapbuilder)<br> builder for Map payloads |
| class | [InvalidStringValueForDefault.InvalidStringValueForDefaultMap](#invalidstringvaluefordefaultmap)<br> output class for Map payloads |
| sealed interface | [InvalidStringValueForDefault.BarBoxed](#barboxed)<br> sealed interface for validated payloads |
| data class | [InvalidStringValueForDefault.BarBoxedString](#barboxedstring)<br> boxed class to store validated String payloads |
| class | [InvalidStringValueForDefault.Bar](#bar)<br> schema class |

## InvalidStringValueForDefault1Boxed
sealed interface InvalidStringValueForDefault1Boxed<br>
permits<br>
[InvalidStringValueForDefault1BoxedVoid](#invalidstringvaluefordefault1boxedvoid),
[InvalidStringValueForDefault1BoxedBoolean](#invalidstringvaluefordefault1boxedboolean),
[InvalidStringValueForDefault1BoxedNumber](#invalidstringvaluefordefault1boxednumber),
[InvalidStringValueForDefault1BoxedString](#invalidstringvaluefordefault1boxedstring),
[InvalidStringValueForDefault1BoxedList](#invalidstringvaluefordefault1boxedlist),
[InvalidStringValueForDefault1BoxedMap](#invalidstringvaluefordefault1boxedmap)

sealed interface that stores validated payloads using boxed classes

## InvalidStringValueForDefault1BoxedVoid
data class InvalidStringValueForDefault1BoxedVoid<br>
implements [InvalidStringValueForDefault1Boxed](#invalidstringvaluefordefault1boxed)

data class that stores validated null payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| InvalidStringValueForDefault1BoxedVoid(Nothing? data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| Nothing? | data()<br>validated payload |
| Any? | getData()<br>validated payload |

## InvalidStringValueForDefault1BoxedBoolean
data class InvalidStringValueForDefault1BoxedBoolean<br>
implements [InvalidStringValueForDefault1Boxed](#invalidstringvaluefordefault1boxed)

data class that stores validated boolean payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| InvalidStringValueForDefault1BoxedBoolean(boolean data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| boolean | data()<br>validated payload |
| Any? | getData()<br>validated payload |

## InvalidStringValueForDefault1BoxedNumber
data class InvalidStringValueForDefault1BoxedNumber<br>
implements [InvalidStringValueForDefault1Boxed](#invalidstringvaluefordefault1boxed)

data class that stores validated Number payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| InvalidStringValueForDefault1BoxedNumber(Number data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| Number | data()<br>validated payload |
| Any? | getData()<br>validated payload |

## InvalidStringValueForDefault1BoxedString
data class InvalidStringValueForDefault1BoxedString<br>
implements [InvalidStringValueForDefault1Boxed](#invalidstringvaluefordefault1boxed)

data class that stores validated String payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| InvalidStringValueForDefault1BoxedString(String data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| String | data()<br>validated payload |
| Any? | getData()<br>validated payload |

## InvalidStringValueForDefault1BoxedList
data class InvalidStringValueForDefault1BoxedList<br>
implements [InvalidStringValueForDefault1Boxed](#invalidstringvaluefordefault1boxed)

data class that stores validated List payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| InvalidStringValueForDefault1BoxedList(FrozenList<Any?> data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| FrozenList<Any?> | data()<br>validated payload |
| Any? | getData()<br>validated payload |

## InvalidStringValueForDefault1BoxedMap
data class InvalidStringValueForDefault1BoxedMap<br>
implements [InvalidStringValueForDefault1Boxed](#invalidstringvaluefordefault1boxed)

data class that stores validated Map payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| InvalidStringValueForDefault1BoxedMap([InvalidStringValueForDefaultMap](#invalidstringvaluefordefaultmap) data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| [InvalidStringValueForDefaultMap](#invalidstringvaluefordefaultmap) | data()<br>validated payload |
| Any? | getData()<br>validated payload |

## InvalidStringValueForDefault1
class InvalidStringValueForDefault1<br>
extends JsonSchema

A schema class that validates payloads

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Map<String, Class<? extends JsonSchema>> | properties = mapOf(<br>&nbsp;&nbsp;&nbsp;&nbsp;"bar" to [Bar::class.java](#bar))<br>)<br> |

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
| [InvalidStringValueForDefaultMap](#invalidstringvaluefordefaultmap) | validate(arg: [Map&lt;*, *&gt;](#invalidstringvaluefordefaultmapbuilder), configuration: SchemaConfiguration) |
| FrozenList<Any?> | validate(arg: List<*>, configuration: SchemaConfiguration) |
| [InvalidStringValueForDefault1BoxedString](#invalidstringvaluefordefault1boxedstring) | validateAndBox(String, configuration: SchemaConfiguration) |
| [InvalidStringValueForDefault1BoxedVoid](#invalidstringvaluefordefault1boxedvoid) | validateAndBox(Nothing?, configuration: SchemaConfiguration) |
| [InvalidStringValueForDefault1BoxedNumber](#invalidstringvaluefordefault1boxednumber) | validateAndBox(Number, configuration: SchemaConfiguration) |
| [InvalidStringValueForDefault1BoxedBoolean](#invalidstringvaluefordefault1boxedboolean) | validateAndBox(Boolean, configuration: SchemaConfiguration) |
| [InvalidStringValueForDefault1BoxedMap](#invalidstringvaluefordefault1boxedmap) | validateAndBox([Map&lt;*, *&gt;](#invalidstringvaluefordefaultmapbuilder), configuration: SchemaConfiguration) |
| [InvalidStringValueForDefault1BoxedList](#invalidstringvaluefordefault1boxedlist) | validateAndBox(List<*>, configuration: SchemaConfiguration) |
| [InvalidStringValueForDefault1Boxed](#invalidstringvaluefordefault1boxed) | validateAndBox(Any?, configuration: SchemaConfiguration) |
| Any? | validate(arg: Any?, configuration: SchemaConfiguration) |

## InvalidStringValueForDefaultMapBuilder
class InvalidStringValueForDefaultMapBuilder<br>
builder for `Map<String, Any?>`

A class that builds the Map input type

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| InvalidStringValueForDefaultMapBuilder()<br>Creates a builder that contains an empty map |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| Map<String, Any?> | build()<br>Returns map input that should be used with Schema.validate |
| [InvalidStringValueForDefaultMapBuilder](#invalidstringvaluefordefaultmapbuilder) | bar(value: String) |
| [InvalidStringValueForDefaultMapBuilder](#invalidstringvaluefordefaultmapbuilder) | additionalProperty(key: String, value: Nothing?) |
| [InvalidStringValueForDefaultMapBuilder](#invalidstringvaluefordefaultmapbuilder) | additionalProperty(key: String, value: Boolean) |
| [InvalidStringValueForDefaultMapBuilder](#invalidstringvaluefordefaultmapbuilder) | additionalProperty(key: String, value: String) |
| [InvalidStringValueForDefaultMapBuilder](#invalidstringvaluefordefaultmapbuilder) | additionalProperty(key: String, value: Int) |
| [InvalidStringValueForDefaultMapBuilder](#invalidstringvaluefordefaultmapbuilder) | additionalProperty(key: String, value: Float) |
| [InvalidStringValueForDefaultMapBuilder](#invalidstringvaluefordefaultmapbuilder) | additionalProperty(key: String, value: Long) |
| [InvalidStringValueForDefaultMapBuilder](#invalidstringvaluefordefaultmapbuilder) | additionalProperty(key: String, value: Double) |
| [InvalidStringValueForDefaultMapBuilder](#invalidstringvaluefordefaultmapbuilder) | additionalProperty(key: String, value: List<Any?>) |
| [InvalidStringValueForDefaultMapBuilder](#invalidstringvaluefordefaultmapbuilder) | additionalProperty(key: String, value: Map<String, Any?>) |

## InvalidStringValueForDefaultMap
class InvalidStringValueForDefaultMap<br>
extends FrozenMap<String, Any?>

A class to store validated Map payloads

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| static [InvalidStringValueForDefaultMap](#invalidstringvaluefordefaultmap) | of([Map<String, Any?>](#invalidstringvaluefordefaultmapbuilder) arg, SchemaConfiguration configuration) |
| String | bar()<br>[optional] if omitted the server will use the default value of bad |
| Any? | getAdditionalProperty(String name)<br>provides type safety for additional properties |

## BarBoxed
sealed interface BarBoxed<br>
permits<br>
[BarBoxedString](#barboxedstring)

sealed interface that stores validated payloads using boxed classes

## BarBoxedString
data class BarBoxedString<br>
implements [BarBoxed](#barboxed)

data class that stores validated String payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| BarBoxedString(String data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| String | data()<br>validated payload |
| Any? | getData()<br>validated payload |

## Bar
class Bar<br>
extends JsonSchema

A schema class that validates payloads

### Code Sample
```
import org.openapijsonschematools.client.configurations.JsonSchemaKeywordFlags
import org.openapijsonschematools.client.configurations.SchemaConfiguration
import org.openapijsonschematools.client.exceptions.ValidationException
import org.openapijsonschematools.client.schemas.validation.MapUtils
import org.openapijsonschematools.client.schemas.validation.FrozenList
import org.openapijsonschematools.client.schemas.validation.FrozenMap
import org.openapijsonschematools.client.components.schemas.InvalidStringValueForDefault

val configuration = SchemaConfiguration(JsonSchemaKeywordFlags.Builder().build())

// String validation
val validatedPayload: String = InvalidStringValueForDefault.Bar.validate(
    "a",
    configuration
)
```

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Set<Class<?>> | type = setOf(<br/>&nbsp;&nbsp;&nbsp;&nbsp;String::class.java<br/>)<br/> |
| Int | minLength = 4 |
| Any? | defaultValue = "bad" |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| String | validate(arg: String, configuration: SchemaConfiguration) |
| [BarBoxedString](#barboxedstring) | validateAndBox(String, configuration: SchemaConfiguration) |
| [BarBoxed](#barboxed) | validateAndBox(Any?, configuration: SchemaConfiguration) |
| Any? | validate(arg: Any?, configuration: SchemaConfiguration) |

[[Back to top]](#top) [[Back to Component Schemas]](../../../README.md#Component-Schemas) [[Back to README]](../../../README.md)
