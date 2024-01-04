# HasOnlyReadOnly
org.openapijsonschematools.client.components.schemas.HasOnlyReadOnly.java
public class HasOnlyReadOnly

A class that contains necessary nested
- schema classes (which validate payloads), extends JsonSchema
- classes to store validated map payloads, extends FrozenMap
- classes to build inputs for map payloads

## Nested Class Summary
| Modifier and Type | Class and Description |
| ----------------- | ---------------------- |
| static class | [HasOnlyReadOnly.HasOnlyReadOnly1](#hasonlyreadonly1)<br> schema class |
| static class | [HasOnlyReadOnly.HasOnlyReadOnlyMapBuilder](#hasonlyreadonlymapbuilder)<br> builder for Map payloads |
| static class | [HasOnlyReadOnly.HasOnlyReadOnlyMap](#hasonlyreadonlymap)<br> output class for Map payloads |
| static class | [HasOnlyReadOnly.Foo](#foo)<br> schema class |
| static class | [HasOnlyReadOnly.Bar](#bar)<br> schema class |

## HasOnlyReadOnly1
public static class HasOnlyReadOnly1<br>
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
HasOnlyReadOnly.HasOnlyReadOnlyMap validatedPayload =
    HasOnlyReadOnly.HasOnlyReadOnly1.validate(
    new HasOnlyReadOnly.HasOnlyReadOnlyMapBuilder()
        .bar("a")

        .foo("a")

    .build(),
    configuration
);
```

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Set<Class<?>> | type = Set.of(Map.class) |
| Map<String, Class<? extends JsonSchema>> | properties = Map.ofEntries(<br>&nbsp;&nbsp;&nbsp;&nbsp;new PropertyEntry("bar", [Bar.class](#bar))),<br>&nbsp;&nbsp;&nbsp;&nbsp;new PropertyEntry("foo", [Foo.class](#foo)))<br>)<br> |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| [HasOnlyReadOnlyMap](#hasonlyreadonlymap) | validate([Map&lt;?, ?&gt;](#hasonlyreadonlymapbuilder) arg, SchemaConfiguration configuration) |
| @Nullable Object | validate(@Nullable Object arg, SchemaConfiguration configuration) |
## HasOnlyReadOnlyMapBuilder
public class HasOnlyReadOnlyMapBuilder<br>
builder for `Map<String, @Nullable Object>`

A class that builds the Map input type

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| HasOnlyReadOnlyMapBuilder()<br>Creates a builder that contains an empty map |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| Map<String, @Nullable Object> | build()<br>Returns map input that should be used with Schema.validate |
| [HasOnlyReadOnlyMapBuilder](#hasonlyreadonlymapbuilder) | bar(String value) |
| [HasOnlyReadOnlyMapBuilder](#hasonlyreadonlymapbuilder) | foo(String value) |
| [HasOnlyReadOnlyMapBuilder](#hasonlyreadonlymapbuilder) | additionalProperty(String key, Void value) |
| [HasOnlyReadOnlyMapBuilder](#hasonlyreadonlymapbuilder) | additionalProperty(String key, boolean value) |
| [HasOnlyReadOnlyMapBuilder](#hasonlyreadonlymapbuilder) | additionalProperty(String key, String value) |
| [HasOnlyReadOnlyMapBuilder](#hasonlyreadonlymapbuilder) | additionalProperty(String key, int value) |
| [HasOnlyReadOnlyMapBuilder](#hasonlyreadonlymapbuilder) | additionalProperty(String key, float value) |
| [HasOnlyReadOnlyMapBuilder](#hasonlyreadonlymapbuilder) | additionalProperty(String key, long value) |
| [HasOnlyReadOnlyMapBuilder](#hasonlyreadonlymapbuilder) | additionalProperty(String key, double value) |
| [HasOnlyReadOnlyMapBuilder](#hasonlyreadonlymapbuilder) | additionalProperty(String key, List<?> value) |
| [HasOnlyReadOnlyMapBuilder](#hasonlyreadonlymapbuilder) | additionalProperty(String key, Map<String, ?> value) |

## HasOnlyReadOnlyMap
public static class HasOnlyReadOnlyMap<br>
extends FrozenMap<String, @Nullable Object>

A class to store validated Map payloads

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| static [HasOnlyReadOnlyMap](#hasonlyreadonlymap) | of([Map<String, ? extends @Nullable Object>](#hasonlyreadonlymapbuilder) arg, SchemaConfiguration configuration) |
| String | bar()<br>[optional] |
| String | foo()<br>[optional] |
| @Nullable Object | getAdditionalProperty(String name)<br>provides type safety for additional properties |

## Foo
public static class Foo<br>
extends StringJsonSchema

A schema class that validates payloads

| Methods Inherited from class org.openapijsonschematools.client.schemas.StringJsonSchema |
| ------------------------------------------------------------------ |
| validate                                                           |

## Bar
public static class Bar<br>
extends StringJsonSchema

A schema class that validates payloads

| Methods Inherited from class org.openapijsonschematools.client.schemas.StringJsonSchema |
| ------------------------------------------------------------------ |
| validate                                                           |

[[Back to top]](#top) [[Back to Component Schemas]](../../../README.md#Component-Schemas) [[Back to README]](../../../README.md)
