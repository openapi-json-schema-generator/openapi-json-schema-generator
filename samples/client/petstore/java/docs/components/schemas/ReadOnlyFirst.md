# ReadOnlyFirst
org.openapijsonschematools.client.components.schemas.ReadOnlyFirst.java
public class ReadOnlyFirst<br>

A class that contains necessary nested
- schema classes (which validate payloads), extends JsonSchema
- sealed interfaces which store validated payloads, java version of a sum type
- boxed classes which store validated payloads, sealed permits class implementations
- classes to store validated map payloads, extends FrozenMap
- classes to build inputs for map payloads

## Nested Class Summary
| Modifier and Type | Class and Description |
| ----------------- | ---------------------- |
| sealed interface | [ReadOnlyFirst.ReadOnlyFirst1Boxed](#readonlyfirst1boxed)<br> sealed interface for validated payloads |
| record | [ReadOnlyFirst.ReadOnlyFirst1BoxedMap](#readonlyfirst1boxedmap)<br> boxed class to store validated Map payloads |
| static class | [ReadOnlyFirst.ReadOnlyFirst1](#readonlyfirst1)<br> schema class |
| static class | [ReadOnlyFirst.ReadOnlyFirstMapBuilder](#readonlyfirstmapbuilder)<br> builder for Map payloads |
| static class | [ReadOnlyFirst.ReadOnlyFirstMap](#readonlyfirstmap)<br> output class for Map payloads |
| sealed interface | [ReadOnlyFirst.BazBoxed](#bazboxed)<br> sealed interface for validated payloads |
| record | [ReadOnlyFirst.BazBoxedString](#bazboxedstring)<br> boxed class to store validated String payloads |
| static class | [ReadOnlyFirst.Baz](#baz)<br> schema class |
| sealed interface | [ReadOnlyFirst.BarBoxed](#barboxed)<br> sealed interface for validated payloads |
| record | [ReadOnlyFirst.BarBoxedString](#barboxedstring)<br> boxed class to store validated String payloads |
| static class | [ReadOnlyFirst.Bar](#bar)<br> schema class |

## ReadOnlyFirst1Boxed
public sealed interface ReadOnlyFirst1Boxed<br>
permits<br>
[ReadOnlyFirst1BoxedMap](#readonlyfirst1boxedmap)

sealed interface that stores validated payloads using boxed classes

## ReadOnlyFirst1BoxedMap
public record ReadOnlyFirst1BoxedMap<br>
implements [ReadOnlyFirst1Boxed](#readonlyfirst1boxed)

record that stores validated Map payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| ReadOnlyFirst1BoxedMap([ReadOnlyFirstMap](#readonlyfirstmap) data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| [ReadOnlyFirstMap](#readonlyfirstmap) | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## ReadOnlyFirst1
public static class ReadOnlyFirst1<br>
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

// Map validation
ReadOnlyFirst.ReadOnlyFirstMap validatedPayload =
    ReadOnlyFirst.ReadOnlyFirst1.validate(
    new ReadOnlyFirst.ReadOnlyFirstMapBuilder()
        .bar("a")

        .baz("a")

    .build(),
    configuration
);
```

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Set<Class<?>> | type = Set.of(Map.class) |
| Map<String, Class<? extends JsonSchema>> | properties = Map.ofEntries(<br>&nbsp;&nbsp;&nbsp;&nbsp;new PropertyEntry("bar", [Bar.class](#bar))),<br>&nbsp;&nbsp;&nbsp;&nbsp;new PropertyEntry("baz", [Baz.class](#baz)))<br>)<br> |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| [ReadOnlyFirstMap](#readonlyfirstmap) | validate([Map&lt;?, ?&gt;](#readonlyfirstmapbuilder) arg, SchemaConfiguration configuration) |
| [ReadOnlyFirst1BoxedMap](#readonlyfirst1boxedmap) | validateAndBox([Map&lt;?, ?&gt;](#readonlyfirstmapbuilder) arg, SchemaConfiguration configuration) |
| [ReadOnlyFirst1Boxed](#readonlyfirst1boxed) | validateAndBox(@Nullable Object arg, SchemaConfiguration configuration) |
| @Nullable Object | validate(@Nullable Object arg, SchemaConfiguration configuration) |

## ReadOnlyFirstMapBuilder
public class ReadOnlyFirstMapBuilder<br>
builder for `Map<String, @Nullable Object>`

A class that builds the Map input type

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| ReadOnlyFirstMapBuilder()<br>Creates a builder that contains an empty map |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| Map<String, @Nullable Object> | build()<br>Returns map input that should be used with Schema.validate |
| [ReadOnlyFirstMapBuilder](#readonlyfirstmapbuilder) | bar(String value) |
| [ReadOnlyFirstMapBuilder](#readonlyfirstmapbuilder) | baz(String value) |
| [ReadOnlyFirstMapBuilder](#readonlyfirstmapbuilder) | additionalProperty(String key, Void value) |
| [ReadOnlyFirstMapBuilder](#readonlyfirstmapbuilder) | additionalProperty(String key, boolean value) |
| [ReadOnlyFirstMapBuilder](#readonlyfirstmapbuilder) | additionalProperty(String key, String value) |
| [ReadOnlyFirstMapBuilder](#readonlyfirstmapbuilder) | additionalProperty(String key, int value) |
| [ReadOnlyFirstMapBuilder](#readonlyfirstmapbuilder) | additionalProperty(String key, float value) |
| [ReadOnlyFirstMapBuilder](#readonlyfirstmapbuilder) | additionalProperty(String key, long value) |
| [ReadOnlyFirstMapBuilder](#readonlyfirstmapbuilder) | additionalProperty(String key, double value) |
| [ReadOnlyFirstMapBuilder](#readonlyfirstmapbuilder) | additionalProperty(String key, List<?> value) |
| [ReadOnlyFirstMapBuilder](#readonlyfirstmapbuilder) | additionalProperty(String key, Map<String, ?> value) |

## ReadOnlyFirstMap
public static class ReadOnlyFirstMap<br>
extends FrozenMap<String, @Nullable Object>

A class to store validated Map payloads

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| static [ReadOnlyFirstMap](#readonlyfirstmap) | of([Map<String, ? extends @Nullable Object>](#readonlyfirstmapbuilder) arg, SchemaConfiguration configuration) |
| String | bar()<br>[optional] |
| String | baz()<br>[optional] |
| @Nullable Object | getAdditionalProperty(String name)<br>provides type safety for additional properties |

## BazBoxed
public sealed interface BazBoxed<br>
permits<br>
[BazBoxedString](#bazboxedstring)

sealed interface that stores validated payloads using boxed classes

## BazBoxedString
public record BazBoxedString<br>
implements [BazBoxed](#bazboxed)

record that stores validated String payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| BazBoxedString(String data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| String | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## Baz
public static class Baz<br>
extends StringJsonSchema.StringJsonSchema1

A schema class that validates payloads

| Methods Inherited from class org.openapijsonschematools.client.schemas.StringJsonSchema.StringJsonSchema1 |
| ------------------------------------------------------------------ |
| validate                                                           |
| validateAndBox                                                     |

## BarBoxed
public sealed interface BarBoxed<br>
permits<br>
[BarBoxedString](#barboxedstring)

sealed interface that stores validated payloads using boxed classes

## BarBoxedString
public record BarBoxedString<br>
implements [BarBoxed](#barboxed)

record that stores validated String payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| BarBoxedString(String data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| String | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## Bar
public static class Bar<br>
extends StringJsonSchema.StringJsonSchema1

A schema class that validates payloads

| Methods Inherited from class org.openapijsonschematools.client.schemas.StringJsonSchema.StringJsonSchema1 |
| ------------------------------------------------------------------ |
| validate                                                           |
| validateAndBox                                                     |

[[Back to top]](#top) [[Back to Component Schemas]](../../../README.md#Component-Schemas) [[Back to README]](../../../README.md)
