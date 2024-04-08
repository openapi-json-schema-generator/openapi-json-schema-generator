# ArrayOfNumberOnly
org.openapijsonschematools.client.components.schemas.ArrayOfNumberOnly.java
public class ArrayOfNumberOnly<br>

A class that contains necessary nested
- schema classes (which validate payloads), extends JsonSchema
- sealed interfaces which store validated payloads, java version of a sum type
- boxed classes which store validated payloads, sealed permits class implementations
- classes to store validated list payloads, extends FrozenList
- classes to build inputs for list payloads
- classes to store validated map payloads, extends FrozenMap
- classes to build inputs for map payloads

## Nested Class Summary
| Modifier and Type | Class and Description |
| ----------------- | ---------------------- |
| sealed interface | [ArrayOfNumberOnly.ArrayOfNumberOnly1Boxed](#arrayofnumberonly1boxed)<br> sealed interface for validated payloads |
| record | [ArrayOfNumberOnly.ArrayOfNumberOnly1BoxedMap](#arrayofnumberonly1boxedmap)<br> boxed class to store validated Map payloads |
| static class | [ArrayOfNumberOnly.ArrayOfNumberOnly1](#arrayofnumberonly1)<br> schema class |
| static class | [ArrayOfNumberOnly.ArrayOfNumberOnlyMapBuilder](#arrayofnumberonlymapbuilder)<br> builder for Map payloads |
| static class | [ArrayOfNumberOnly.ArrayOfNumberOnlyMap](#arrayofnumberonlymap)<br> output class for Map payloads |
| sealed interface | [ArrayOfNumberOnly.ArrayNumberBoxed](#arraynumberboxed)<br> sealed interface for validated payloads |
| record | [ArrayOfNumberOnly.ArrayNumberBoxedList](#arraynumberboxedlist)<br> boxed class to store validated List payloads |
| static class | [ArrayOfNumberOnly.ArrayNumber](#arraynumber)<br> schema class |
| static class | [ArrayOfNumberOnly.ArrayNumberListBuilder](#arraynumberlistbuilder)<br> builder for List payloads |
| static class | [ArrayOfNumberOnly.ArrayNumberList](#arraynumberlist)<br> output class for List payloads |
| sealed interface | [ArrayOfNumberOnly.ItemsBoxed](#itemsboxed)<br> sealed interface for validated payloads |
| record | [ArrayOfNumberOnly.ItemsBoxedNumber](#itemsboxednumber)<br> boxed class to store validated Number payloads |
| static class | [ArrayOfNumberOnly.Items](#items)<br> schema class |

## ArrayOfNumberOnly1Boxed
public sealed interface ArrayOfNumberOnly1Boxed<br>
permits<br>
[ArrayOfNumberOnly1BoxedMap](#arrayofnumberonly1boxedmap)

sealed interface that stores validated payloads using boxed classes

## ArrayOfNumberOnly1BoxedMap
public record ArrayOfNumberOnly1BoxedMap<br>
implements [ArrayOfNumberOnly1Boxed](#arrayofnumberonly1boxed)

record that stores validated Map payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| ArrayOfNumberOnly1BoxedMap([ArrayOfNumberOnlyMap](#arrayofnumberonlymap) data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| [ArrayOfNumberOnlyMap](#arrayofnumberonlymap) | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## ArrayOfNumberOnly1
public static class ArrayOfNumberOnly1<br>
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
import org.openapijsonschematools.client.components.schemas.ArrayOfNumberOnly;

import java.util.Arrays;
import java.util.List;
import java.util.AbstractMap;

static final SchemaConfiguration configuration = new SchemaConfiguration(new JsonSchemaKeywordFlags.Builder().build());

// Map validation
ArrayOfNumberOnly.ArrayOfNumberOnlyMap validatedPayload =
    ArrayOfNumberOnly.ArrayOfNumberOnly1.validate(
    new ArrayOfNumberOnly.ArrayOfNumberOnlyMapBuilder()
        .ArrayNumber(
            Arrays.asList(
                1
            )
        )
    .build(),
    configuration
);
```

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Set<Class<?>> | type = Set.of(Map.class) |
| Map<String, Class<? extends JsonSchema>> | properties = Map.ofEntries(<br>&nbsp;&nbsp;&nbsp;&nbsp;new PropertyEntry("ArrayNumber", [ArrayNumber.class](#arraynumber)))<br>)<br> |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| [ArrayOfNumberOnlyMap](#arrayofnumberonlymap) | validate([Map&lt;?, ?&gt;](#arrayofnumberonlymapbuilder) arg, SchemaConfiguration configuration) |
| [ArrayOfNumberOnly1BoxedMap](#arrayofnumberonly1boxedmap) | validateAndBox([Map&lt;?, ?&gt;](#arrayofnumberonlymapbuilder) arg, SchemaConfiguration configuration) |
| [ArrayOfNumberOnly1Boxed](#arrayofnumberonly1boxed) | validateAndBox(@Nullable Object arg, SchemaConfiguration configuration) |
| @Nullable Object | validate(@Nullable Object arg, SchemaConfiguration configuration) |

## ArrayOfNumberOnlyMapBuilder
public class ArrayOfNumberOnlyMapBuilder<br>
builder for `Map<String, @Nullable Object>`

A class that builds the Map input type

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| ArrayOfNumberOnlyMapBuilder()<br>Creates a builder that contains an empty map |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| Map<String, @Nullable Object> | build()<br>Returns map input that should be used with Schema.validate |
| [ArrayOfNumberOnlyMapBuilder](#arrayofnumberonlymapbuilder) | ArrayNumber(List<Number> value) |
| [ArrayOfNumberOnlyMapBuilder](#arrayofnumberonlymapbuilder) | additionalProperty(String key, Void value) |
| [ArrayOfNumberOnlyMapBuilder](#arrayofnumberonlymapbuilder) | additionalProperty(String key, boolean value) |
| [ArrayOfNumberOnlyMapBuilder](#arrayofnumberonlymapbuilder) | additionalProperty(String key, String value) |
| [ArrayOfNumberOnlyMapBuilder](#arrayofnumberonlymapbuilder) | additionalProperty(String key, int value) |
| [ArrayOfNumberOnlyMapBuilder](#arrayofnumberonlymapbuilder) | additionalProperty(String key, float value) |
| [ArrayOfNumberOnlyMapBuilder](#arrayofnumberonlymapbuilder) | additionalProperty(String key, long value) |
| [ArrayOfNumberOnlyMapBuilder](#arrayofnumberonlymapbuilder) | additionalProperty(String key, double value) |
| [ArrayOfNumberOnlyMapBuilder](#arrayofnumberonlymapbuilder) | additionalProperty(String key, List<?> value) |
| [ArrayOfNumberOnlyMapBuilder](#arrayofnumberonlymapbuilder) | additionalProperty(String key, Map<String, ?> value) |

## ArrayOfNumberOnlyMap
public static class ArrayOfNumberOnlyMap<br>
extends FrozenMap<String, @Nullable Object>

A class to store validated Map payloads

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| static [ArrayOfNumberOnlyMap](#arrayofnumberonlymap) | of([Map<String, ? extends @Nullable Object>](#arrayofnumberonlymapbuilder) arg, SchemaConfiguration configuration) |
| [ArrayNumberList](#arraynumberlist) | ArrayNumber()<br>[optional] |
| @Nullable Object | getAdditionalProperty(String name)<br>provides type safety for additional properties |

## ArrayNumberBoxed
public sealed interface ArrayNumberBoxed<br>
permits<br>
[ArrayNumberBoxedList](#arraynumberboxedlist)

sealed interface that stores validated payloads using boxed classes

## ArrayNumberBoxedList
public record ArrayNumberBoxedList<br>
implements [ArrayNumberBoxed](#arraynumberboxed)

record that stores validated List payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| ArrayNumberBoxedList([ArrayNumberList](#arraynumberlist) data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| [ArrayNumberList](#arraynumberlist) | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## ArrayNumber
public static class ArrayNumber<br>
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
import org.openapijsonschematools.client.components.schemas.ArrayOfNumberOnly;

import java.util.Arrays;
import java.util.List;
import java.util.AbstractMap;

static final SchemaConfiguration configuration = new SchemaConfiguration(new JsonSchemaKeywordFlags.Builder().build());

// List validation
ArrayOfNumberOnly.ArrayNumberList validatedPayload =
    ArrayOfNumberOnly.ArrayNumber.validate(
    new ArrayOfNumberOnly.ArrayNumberListBuilder()
        .add(1)

    .build(),
    configuration
);
```

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Set<Class<?>> | type = Set.of(List.class) |
| Class<? extends JsonSchema> | items = [Items.class](#items) |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| [ArrayNumberList](#arraynumberlist) | validate([List<?>](#arraynumberlistbuilder) arg, SchemaConfiguration configuration) |
| [ArrayNumberBoxedList](#arraynumberboxedlist) | validateAndBox([List<?>](#arraynumberlistbuilder) arg, SchemaConfiguration configuration) |
| [ArrayNumberBoxed](#arraynumberboxed) | validateAndBox(@Nullable Object arg, SchemaConfiguration configuration) |
| @Nullable Object | validate(@Nullable Object arg, SchemaConfiguration configuration) |

## ArrayNumberListBuilder
public class ArrayNumberListBuilder<br>
builder for `List<Number>`

A class that builds the List input type

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| ArrayNumberListBuilder()<br>Creates an empty list |
| ArrayNumberListBuilder(List<Number> items)<br>Stores the items in a list |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| ArrayNumberListBuilder | add(int item) |
| ArrayNumberListBuilder | add(float item) |
| ArrayNumberListBuilder | add(long item) |
| ArrayNumberListBuilder | add(double item) |
| List<Number> | build()<br>Returns list input that should be used with Schema.validate |

## ArrayNumberList
public class ArrayNumberList<br>
extends `FrozenList<Number>`

A class to store validated List payloads

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| static [ArrayNumberList](#arraynumberlist) | of([List<Number>](#arraynumberlistbuilder) arg, SchemaConfiguration configuration) |

## ItemsBoxed
public sealed interface ItemsBoxed<br>
permits<br>
[ItemsBoxedNumber](#itemsboxednumber)

sealed interface that stores validated payloads using boxed classes

## ItemsBoxedNumber
public record ItemsBoxedNumber<br>
implements [ItemsBoxed](#itemsboxed)

record that stores validated Number payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| ItemsBoxedNumber(Number data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| Number | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## Items
public static class Items<br>
extends NumberJsonSchema.NumberJsonSchema1

A schema class that validates payloads

| Methods Inherited from class org.openapijsonschematools.client.schemas.NumberJsonSchema.NumberJsonSchema1 |
| ------------------------------------------------------------------ |
| validate                                                           |
| validateAndBox                                                     |

[[Back to top]](#top) [[Back to Component Schemas]](../../../README.md#Component-Schemas) [[Back to README]](../../../README.md)
