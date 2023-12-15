# HasOnlyReadOnly
org.openapijsonschematools.client.components.schemas.HasOnlyReadOnly.java
public class HasOnlyReadOnly

A class that contains necessary nested
- schema classes (which validate payloads), extends JsonSchema
- classes to store validated list payloads, extends FrozenList
- classes to store validated map payloads, extends FrozenMap
- classes to build inputs for list payloads
- classes to build inputs for map payloads

## Nested Class Summary
| Modifier and Type | Class and Description |
| ----------------- | ---------------------- |
| static class | [HasOnlyReadOnly.HasOnlyReadOnly1](#hasonlyreadonly1)<br> schema class |
| static class | [HasOnlyReadOnly.HasOnlyReadOnlyMapInput](#hasonlyreadonlymapinput)<br> builder for Map payloads |
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
import org.openapijsonschematools.client.schemas.MapMaker;
import org.openapijsonschematools.client.schemas.validation.FrozenList;
import org.openapijsonschematools.client.schemas.validation.FrozenMap;

import java.util.Arrays;
import java.util.List;
import java.util.AbstractMap;

static final SchemaConfiguration configuration = new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone());

// Map validation
HasOnlyReadOnly.HasOnlyReadOnlyMap validatedPayload =
    HasOnlyReadOnly.HasOnlyReadOnly1.validate(
    MapMaker.makeMap(
        new AbstractMap.SimpleEntry<>(
            "bar",
            "a"
        ),
        new AbstractMap.SimpleEntry<>(
            "foo",
            "a"
        )
    ),
    configuration
);
```

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Set<Class<?>> | &nbsp;&nbsp;&nbsp;&nbsp;type = Set.of(FrozenMap.class)<br/> |
| Map<String, Class<? extends JsonSchema>> | &nbsp;&nbsp;&nbsp;&nbsp;properties = Map.ofEntries(<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;new PropertyEntry("bar", [Bar.class](#bar))),<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;new PropertyEntry("foo", [Foo.class](#foo)))<br>&nbsp;&nbsp;&nbsp;&nbsp;)<br> |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| static [HasOnlyReadOnlyMap](#hasonlyreadonlymap) | validate([Map<String, Object>](#hasonlyreadonlymapinput) arg, SchemaConfiguration configuration) |

## HasOnlyReadOnlyMapInput
public class HasOnlyReadOnlyMapInput<br>
builder for `Map<String, Object>`

A class that builds the Map input type

## Input Map Keys
| Key | Type |  Description | Notes |
| --- | ---- | ------------ | ----- |
| **bar** | String |  | [optional] |
| **foo** | String |  | [optional] |
| **anyStringName** | Object | any string name can be used but the value must be the correct type | [optional] |

## HasOnlyReadOnlyMap
public static class HasOnlyReadOnlyMap<br>
extends FrozenMap<String, Object>

A class to store validated Map payloads

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| static [HasOnlyReadOnlyMap](#hasonlyreadonlymap) | of([Map<String, Object>](#hasonlyreadonlymapinput) arg, SchemaConfiguration configuration) |
| String | bar()<br>[optional] |
| String | foo()<br>[optional] |
| Object | getAdditionalProperty(String name)<br>provides type safety for additional properties |

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
