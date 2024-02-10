# Schema0
public class Schema0

A class that contains necessary nested
- schema classes (which validate payloads), extends JsonSchema
- abstract sealed classes which store validated payloads, java version of a sum type
- boxed classes which store validated payloads, sealed permits class implementations

## Nested Class Summary
| Modifier and Type | Class and Description |
| ----------------- | ---------------------- |
| static class | [Schema0.Schema01Boxed](#schema01boxed)<br> abstract sealed validated payload class |
| static class | [Schema0.Schema01BoxedVoid](#schema01boxedvoid)<br> boxed class to store validated null payloads |
| static class | [Schema0.Schema01BoxedBoolean](#schema01boxedboolean)<br> boxed class to store validated boolean payloads |
| static class | [Schema0.Schema01BoxedNumber](#schema01boxednumber)<br> boxed class to store validated Number payloads |
| static class | [Schema0.Schema01BoxedString](#schema01boxedstring)<br> boxed class to store validated String payloads |
| static class | [Schema0.Schema01BoxedList](#schema01boxedlist)<br> boxed class to store validated List payloads |
| static class | [Schema0.Schema01BoxedMap](#schema01boxedmap)<br> boxed class to store validated Map payloads |
| static class | [Schema0.Schema01](#schema01)<br> schema class |
| static class | [Schema0.Schema00Boxed](#schema00boxed)<br> abstract sealed validated payload class |
| static class | [Schema0.Schema00BoxedString](#schema00boxedstring)<br> boxed class to store validated String payloads |
| static class | [Schema0.Schema00](#schema00)<br> schema class |

## Schema01Boxed
public static abstract sealed class Schema01Boxed<br>
permits<br>
[Schema01BoxedVoid](#schema01boxedvoid),
[Schema01BoxedBoolean](#schema01boxedboolean),
[Schema01BoxedNumber](#schema01boxednumber),
[Schema01BoxedString](#schema01boxedstring),
[Schema01BoxedList](#schema01boxedlist),
[Schema01BoxedMap](#schema01boxedmap)

abstract sealed class that stores validated payloads using boxed classes

## Schema01BoxedVoid
public static final class Schema01BoxedVoid<br>
extends [Schema01Boxed](#schema01boxed)

a boxed class to store validated null payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| Schema01BoxedVoid(Void data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Void | data<br>validated payload |

## Schema01BoxedBoolean
public static final class Schema01BoxedBoolean<br>
extends [Schema01Boxed](#schema01boxed)

a boxed class to store validated boolean payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| Schema01BoxedBoolean(boolean data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| boolean | data<br>validated payload |

## Schema01BoxedNumber
public static final class Schema01BoxedNumber<br>
extends [Schema01Boxed](#schema01boxed)

a boxed class to store validated Number payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| Schema01BoxedNumber(Number data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Number | data<br>validated payload |

## Schema01BoxedString
public static final class Schema01BoxedString<br>
extends [Schema01Boxed](#schema01boxed)

a boxed class to store validated String payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| Schema01BoxedString(String data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| String | data<br>validated payload |

## Schema01BoxedList
public static final class Schema01BoxedList<br>
extends [Schema01Boxed](#schema01boxed)

a boxed class to store validated List payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| Schema01BoxedList(FrozenList<@Nullable Object> data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| FrozenList<@Nullable Object> | data<br>validated payload |

## Schema01BoxedMap
public static final class Schema01BoxedMap<br>
extends [Schema01Boxed](#schema01boxed)

a boxed class to store validated Map payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| Schema01BoxedMap(FrozenMap<@Nullable Object> data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| FrozenMap<@Nullable Object> | data<br>validated payload |

## Schema01
public static class Schema01<br>
extends JsonSchema

A schema class that validates payloads

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| List<Class<? extends JsonSchema>> | allOf = List.of(<br>&nbsp;&nbsp;&nbsp;&nbsp;[Schema00.class](#schema00)<br>;)<br> |

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
| [Schema01BoxedString](#schema01boxedstring) | validateAndBox(String arg, SchemaConfiguration configuration) |
| [Schema01BoxedVoid](#schema01boxedvoid) | validateAndBox(Void arg, SchemaConfiguration configuration) |
| [Schema01BoxedNumber](#schema01boxednumber) | validateAndBox(Number arg, SchemaConfiguration configuration) |
| [Schema01BoxedBoolean](#schema01boxedboolean) | validateAndBox(boolean arg, SchemaConfiguration configuration) |
| [Schema01BoxedMap](#schema01boxedmap) | validateAndBox(Map&lt;?, ?&gt; arg, SchemaConfiguration configuration) |
| [Schema01BoxedList](#schema01boxedlist) | validateAndBox(List<?> arg, SchemaConfiguration configuration) |
| @Nullable Object | validate(@Nullable Object arg, SchemaConfiguration configuration) |
## Schema00Boxed
public static abstract sealed class Schema00Boxed<br>
permits<br>
[Schema00BoxedString](#schema00boxedstring)

abstract sealed class that stores validated payloads using boxed classes

## Schema00BoxedString
public static final class Schema00BoxedString<br>
extends [Schema00Boxed](#schema00boxed)

a boxed class to store validated String payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| Schema00BoxedString(String data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| String | data<br>validated payload |

## Schema00
public static class Schema00<br>
extends JsonSchema

A schema class that validates payloads

### Code Sample
```
import org.openapijsonschematools.client.configurations.JsonSchemaKeywordFlags;
import org.openapijsonschematools.client.configurations.SchemaConfiguration;
import org.openapijsonschematools.client.exceptions.ValidationException;
import org.openapijsonschematools.client.schemas.validation.MapUtils;
import org.openapijsonschematools.client.schemas.validation.FrozenList;
import org.openapijsonschematools.client.schemas.validation.FrozenMap;

import java.util.Arrays;
import java.util.List;
import java.util.AbstractMap;

static final SchemaConfiguration configuration = new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone());

// String validation
String validatedPayload = Schema0.Schema00.validate(
    "a",
    configuration
);
```

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Set<Class<?>> | type = Set.of(<br/>&nbsp;&nbsp;&nbsp;&nbsp;String.class<br/>)<br/> |
| Integer | minLength = 1 |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| String | validate(String arg, SchemaConfiguration configuration) |
| [Schema00BoxedString](#schema00boxedstring) | validateAndBox(String arg, SchemaConfiguration configuration) |
| @Nullable Object | validate(@Nullable Object arg, SchemaConfiguration configuration) |