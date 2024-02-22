# Tag
org.openapijsonschematools.client.components.schemas.Tag.java
public class Tag<br>

A class that contains necessary nested
- schema classes (which validate payloads), extends JsonSchema
- sealed interfaces which store validated payloads, java version of a sum type
- boxed classes which store validated payloads, sealed permits class implementations
- classes to store validated map payloads, extends FrozenMap
- classes to build inputs for map payloads

## Nested Class Summary
| Modifier and Type | Class and Description |
| ----------------- | ---------------------- |
| sealed interface | [Tag.Tag1Boxed](#tag1boxed)<br> sealed interface for validated payloads |
| record | [Tag.Tag1BoxedMap](#tag1boxedmap)<br> boxed class to store validated Map payloads |
| static class | [Tag.Tag1](#tag1)<br> schema class |
| static class | [Tag.TagMapBuilder](#tagmapbuilder)<br> builder for Map payloads |
| static class | [Tag.TagMap](#tagmap)<br> output class for Map payloads |
| sealed interface | [Tag.NameBoxed](#nameboxed)<br> sealed interface for validated payloads |
| record | [Tag.NameBoxedString](#nameboxedstring)<br> boxed class to store validated String payloads |
| static class | [Tag.Name](#name)<br> schema class |
| sealed interface | [Tag.IdBoxed](#idboxed)<br> sealed interface for validated payloads |
| record | [Tag.IdBoxedNumber](#idboxednumber)<br> boxed class to store validated Number payloads |
| static class | [Tag.Id](#id)<br> schema class |

## Tag1Boxed
public sealed interface Tag1Boxed<br>
permits<br>
[Tag1BoxedMap](#tag1boxedmap)

sealed interface that stores validated payloads using boxed classes

## Tag1BoxedMap
public record Tag1BoxedMap<br>
implements [Tag1Boxed](#tag1boxed)

record that stores validated Map payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| Tag1BoxedMap([TagMap](#tagmap) data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| [TagMap](#tagmap) | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## Tag1
public static class Tag1<br>
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
Tag.TagMap validatedPayload =
    Tag.Tag1.validate(
    new Tag.TagMapBuilder()
        .id(1L)

        .name("a")

    .build(),
    configuration
);
```

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Set<Class<?>> | type = Set.of(Map.class) |
| Map<String, Class<? extends JsonSchema>> | properties = Map.ofEntries(<br>&nbsp;&nbsp;&nbsp;&nbsp;new PropertyEntry("id", [Id.class](#id))),<br>&nbsp;&nbsp;&nbsp;&nbsp;new PropertyEntry("name", [Name.class](#name)))<br>)<br> |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| [TagMap](#tagmap) | validate([Map&lt;?, ?&gt;](#tagmapbuilder) arg, SchemaConfiguration configuration) |
| [Tag1BoxedMap](#tag1boxedmap) | validateAndBox([Map&lt;?, ?&gt;](#tagmapbuilder) arg, SchemaConfiguration configuration) |
| [Tag1Boxed](#tag1boxed) | validateAndBox(@Nullable Object arg, SchemaConfiguration configuration) |
| @Nullable Object | validate(@Nullable Object arg, SchemaConfiguration configuration) |

## TagMapBuilder
public class TagMapBuilder<br>
builder for `Map<String, @Nullable Object>`

A class that builds the Map input type

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| TagMapBuilder()<br>Creates a builder that contains an empty map |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| Map<String, @Nullable Object> | build()<br>Returns map input that should be used with Schema.validate |
| [TagMapBuilder](#tagmapbuilder) | id(int value) |
| [TagMapBuilder](#tagmapbuilder) | id(float value) |
| [TagMapBuilder](#tagmapbuilder) | id(long value) |
| [TagMapBuilder](#tagmapbuilder) | id(double value) |
| [TagMapBuilder](#tagmapbuilder) | name(String value) |
| [TagMapBuilder](#tagmapbuilder) | additionalProperty(String key, Void value) |
| [TagMapBuilder](#tagmapbuilder) | additionalProperty(String key, boolean value) |
| [TagMapBuilder](#tagmapbuilder) | additionalProperty(String key, String value) |
| [TagMapBuilder](#tagmapbuilder) | additionalProperty(String key, int value) |
| [TagMapBuilder](#tagmapbuilder) | additionalProperty(String key, float value) |
| [TagMapBuilder](#tagmapbuilder) | additionalProperty(String key, long value) |
| [TagMapBuilder](#tagmapbuilder) | additionalProperty(String key, double value) |
| [TagMapBuilder](#tagmapbuilder) | additionalProperty(String key, List<?> value) |
| [TagMapBuilder](#tagmapbuilder) | additionalProperty(String key, Map<String, ?> value) |

## TagMap
public static class TagMap<br>
extends FrozenMap<String, @Nullable Object>

A class to store validated Map payloads

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| static [TagMap](#tagmap) | of([Map<String, ? extends @Nullable Object>](#tagmapbuilder) arg, SchemaConfiguration configuration) |
| Number | id()<br>[optional] value must be a 64 bit integer |
| String | name()<br>[optional] |
| @Nullable Object | getAdditionalProperty(String name)<br>provides type safety for additional properties |

## NameBoxed
public sealed interface NameBoxed<br>
permits<br>
[NameBoxedString](#nameboxedstring)

sealed interface that stores validated payloads using boxed classes

## NameBoxedString
public record NameBoxedString<br>
implements [NameBoxed](#nameboxed)

record that stores validated String payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| NameBoxedString(String data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| String | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## Name
public static class Name<br>
extends StringJsonSchema.StringJsonSchema1

A schema class that validates payloads

| Methods Inherited from class org.openapijsonschematools.client.schemas.StringJsonSchema.StringJsonSchema1 |
| ------------------------------------------------------------------ |
| validate                                                           |
| validateAndBox                                                     |

## IdBoxed
public sealed interface IdBoxed<br>
permits<br>
[IdBoxedNumber](#idboxednumber)

sealed interface that stores validated payloads using boxed classes

## IdBoxedNumber
public record IdBoxedNumber<br>
implements [IdBoxed](#idboxed)

record that stores validated Number payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| IdBoxedNumber(Number data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| Number | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## Id
public static class Id<br>
extends Int64JsonSchema.Int64JsonSchema1

A schema class that validates payloads

| Methods Inherited from class org.openapijsonschematools.client.schemas.Int64JsonSchema.Int64JsonSchema1 |
| ------------------------------------------------------------------ |
| validate                                                           |
| validateAndBox                                                     |

[[Back to top]](#top) [[Back to Component Schemas]](../../../README.md#Component-Schemas) [[Back to README]](../../../README.md)
