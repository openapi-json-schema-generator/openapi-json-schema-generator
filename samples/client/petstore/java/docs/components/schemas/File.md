# File
org.openapijsonschematools.client.components.schemas.File.java
public class File

A class that contains necessary nested
- schema classes (which validate payloads), extends JsonSchema
- abstract sealed classes which store validated payloads, java version of a sum type
- boxed classes which store validated payloads, sealed permits class implementations
- classes to store validated map payloads, extends FrozenMap
- classes to build inputs for map payloads

## Nested Class Summary
| Modifier and Type | Class and Description |
| ----------------- | ---------------------- |
| static class | [File.File1Boxed](#file1boxed)<br> abstract sealed validated payload class |
| static class | [File.File1BoxedMap](#file1boxedmap)<br> boxed class to store validated Map payloads |
| static class | [File.File1](#file1)<br> schema class |
| static class | [File.FileMapBuilder](#filemapbuilder)<br> builder for Map payloads |
| static class | [File.FileMap](#filemap)<br> output class for Map payloads |
| static class | [File.SourceURIBoxed](#sourceuriboxed)<br> abstract sealed validated payload class |
| static class | [File.SourceURIBoxedString](#sourceuriboxedstring)<br> boxed class to store validated String payloads |
| static class | [File.SourceURI](#sourceuri)<br> schema class |

## File1Boxed
public static abstract sealed class File1Boxed<br>
permits<br>
[File1BoxedMap](#file1boxedmap)

abstract sealed class that stores validated payloads using boxed classes

## File1BoxedMap
public static final class File1BoxedMap<br>
extends [File1Boxed](#file1boxed)

a boxed class to store validated Map payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| File1BoxedMap([FileMap](#filemap) data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| [FileMap](#filemap) | data<br>validated payload |

## File1
public static class File1<br>
extends JsonSchema

A schema class that validates payloads

## Description
Must be named &#x60;File&#x60; for test.

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
File.FileMap validatedPayload =
    File.File1.validate(
    new File.FileMapBuilder()
        .sourceURI("a")

    .build(),
    configuration
);
```

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Set<Class<?>> | type = Set.of(Map.class) |
| Map<String, Class<? extends JsonSchema>> | properties = Map.ofEntries(<br>&nbsp;&nbsp;&nbsp;&nbsp;new PropertyEntry("sourceURI", [SourceURI.class](#sourceuri)))<br>)<br> |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| [FileMap](#filemap) | validate([Map&lt;?, ?&gt;](#filemapbuilder) arg, SchemaConfiguration configuration) |
| [File1BoxedMap](#file1boxedmap) | validateAndBox([Map&lt;?, ?&gt;](#filemapbuilder) arg, SchemaConfiguration configuration) |
| @Nullable Object | validate(@Nullable Object arg, SchemaConfiguration configuration) |
## FileMapBuilder
public class FileMapBuilder<br>
builder for `Map<String, @Nullable Object>`

A class that builds the Map input type

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| FileMapBuilder()<br>Creates a builder that contains an empty map |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| Map<String, @Nullable Object> | build()<br>Returns map input that should be used with Schema.validate |
| [FileMapBuilder](#filemapbuilder) | sourceURI(String value) |
| [FileMapBuilder](#filemapbuilder) | additionalProperty(String key, Void value) |
| [FileMapBuilder](#filemapbuilder) | additionalProperty(String key, boolean value) |
| [FileMapBuilder](#filemapbuilder) | additionalProperty(String key, String value) |
| [FileMapBuilder](#filemapbuilder) | additionalProperty(String key, int value) |
| [FileMapBuilder](#filemapbuilder) | additionalProperty(String key, float value) |
| [FileMapBuilder](#filemapbuilder) | additionalProperty(String key, long value) |
| [FileMapBuilder](#filemapbuilder) | additionalProperty(String key, double value) |
| [FileMapBuilder](#filemapbuilder) | additionalProperty(String key, List<?> value) |
| [FileMapBuilder](#filemapbuilder) | additionalProperty(String key, Map<String, ?> value) |

## FileMap
public static class FileMap<br>
extends FrozenMap<String, @Nullable Object>

A class to store validated Map payloads

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| static [FileMap](#filemap) | of([Map<String, ? extends @Nullable Object>](#filemapbuilder) arg, SchemaConfiguration configuration) |
| String | sourceURI()<br>[optional] |
| @Nullable Object | getAdditionalProperty(String name)<br>provides type safety for additional properties |

## SourceURIBoxed
public static abstract sealed class SourceURIBoxed<br>
permits<br>
[SourceURIBoxedString](#sourceuriboxedstring)

abstract sealed class that stores validated payloads using boxed classes

## SourceURIBoxedString
public static final class SourceURIBoxedString<br>
extends [SourceURIBoxed](#sourceuriboxed)

a boxed class to store validated String payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| SourceURIBoxedString(String data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| String | data<br>validated payload |

## SourceURI
public static class SourceURI<br>
extends StringJsonSchema.StringJsonSchema1

A schema class that validates payloads

## Description
Test capitalization

| Methods Inherited from class org.openapijsonschematools.client.schemas.StringJsonSchema.StringJsonSchema1 |
| ------------------------------------------------------------------ |
| validate                                                           |
| validateAndBox                                                     |

[[Back to top]](#top) [[Back to Component Schemas]](../../../README.md#Component-Schemas) [[Back to README]](../../../README.md)
