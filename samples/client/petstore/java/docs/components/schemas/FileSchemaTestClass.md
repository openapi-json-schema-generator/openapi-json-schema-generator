# FileSchemaTestClass
org.openapijsonschematools.client.components.schemas.FileSchemaTestClass.java
public class FileSchemaTestClass<br>

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
| sealed interface | [FileSchemaTestClass.FileSchemaTestClass1Boxed](#fileschematestclass1boxed)<br> sealed interface for validated payloads |
| record | [FileSchemaTestClass.FileSchemaTestClass1BoxedMap](#fileschematestclass1boxedmap)<br> boxed class to store validated Map payloads |
| static class | [FileSchemaTestClass.FileSchemaTestClass1](#fileschematestclass1)<br> schema class |
| static class | [FileSchemaTestClass.FileSchemaTestClassMapBuilder](#fileschematestclassmapbuilder)<br> builder for Map payloads |
| static class | [FileSchemaTestClass.FileSchemaTestClassMap](#fileschematestclassmap)<br> output class for Map payloads |
| sealed interface | [FileSchemaTestClass.FilesBoxed](#filesboxed)<br> sealed interface for validated payloads |
| record | [FileSchemaTestClass.FilesBoxedList](#filesboxedlist)<br> boxed class to store validated List payloads |
| static class | [FileSchemaTestClass.Files](#files)<br> schema class |
| static class | [FileSchemaTestClass.FilesListBuilder](#fileslistbuilder)<br> builder for List payloads |
| static class | [FileSchemaTestClass.FilesList](#fileslist)<br> output class for List payloads |

## FileSchemaTestClass1Boxed
public sealed interface FileSchemaTestClass1Boxed<br>
permits<br>
[FileSchemaTestClass1BoxedMap](#fileschematestclass1boxedmap)

sealed interface that stores validated payloads using boxed classes

## FileSchemaTestClass1BoxedMap
public record FileSchemaTestClass1BoxedMap<br>
implements [FileSchemaTestClass1Boxed](#fileschematestclass1boxed)

record that stores validated Map payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| FileSchemaTestClass1BoxedMap([FileSchemaTestClassMap](#fileschematestclassmap) data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| [FileSchemaTestClassMap](#fileschematestclassmap) | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## FileSchemaTestClass1
public static class FileSchemaTestClass1<br>
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
import org.openapijsonschematools.client.components.schemas.FileSchemaTestClass;

import java.util.Arrays;
import java.util.List;
import java.util.AbstractMap;

static final SchemaConfiguration configuration = new SchemaConfiguration(new JsonSchemaKeywordFlags.Builder().build());

// Map validation
FileSchemaTestClass.FileSchemaTestClassMap validatedPayload =
    FileSchemaTestClass.FileSchemaTestClass1.validate(
    new FileSchemaTestClass.FileSchemaTestClassMapBuilder()
        .files(
            Arrays.asList(
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
| Map<String, Class<? extends JsonSchema>> | properties = Map.ofEntries(<br>&nbsp;&nbsp;&nbsp;&nbsp;new PropertyEntry("file", [File.File1.class](../../components/schemas/File.md#file1)),<br>&nbsp;&nbsp;&nbsp;&nbsp;new PropertyEntry("files", [Files.class](#files)))<br>)<br> |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| [FileSchemaTestClassMap](#fileschematestclassmap) | validate([Map&lt;?, ?&gt;](#fileschematestclassmapbuilder) arg, SchemaConfiguration configuration) |
| [FileSchemaTestClass1BoxedMap](#fileschematestclass1boxedmap) | validateAndBox([Map&lt;?, ?&gt;](#fileschematestclassmapbuilder) arg, SchemaConfiguration configuration) |
| [FileSchemaTestClass1Boxed](#fileschematestclass1boxed) | validateAndBox(@Nullable Object arg, SchemaConfiguration configuration) |
| @Nullable Object | validate(@Nullable Object arg, SchemaConfiguration configuration) |

## FileSchemaTestClassMapBuilder
public class FileSchemaTestClassMapBuilder<br>
builder for `Map<String, @Nullable Object>`

A class that builds the Map input type

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| FileSchemaTestClassMapBuilder()<br>Creates a builder that contains an empty map |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| Map<String, @Nullable Object> | build()<br>Returns map input that should be used with Schema.validate |
| [FileSchemaTestClassMapBuilder](#fileschematestclassmapbuilder) | file(Map<String, @Nullable Object> value) |
| [FileSchemaTestClassMapBuilder](#fileschematestclassmapbuilder) | files(List<Map<String, @Nullable Object>> value) |
| [FileSchemaTestClassMapBuilder](#fileschematestclassmapbuilder) | additionalProperty(String key, Void value) |
| [FileSchemaTestClassMapBuilder](#fileschematestclassmapbuilder) | additionalProperty(String key, boolean value) |
| [FileSchemaTestClassMapBuilder](#fileschematestclassmapbuilder) | additionalProperty(String key, String value) |
| [FileSchemaTestClassMapBuilder](#fileschematestclassmapbuilder) | additionalProperty(String key, int value) |
| [FileSchemaTestClassMapBuilder](#fileschematestclassmapbuilder) | additionalProperty(String key, float value) |
| [FileSchemaTestClassMapBuilder](#fileschematestclassmapbuilder) | additionalProperty(String key, long value) |
| [FileSchemaTestClassMapBuilder](#fileschematestclassmapbuilder) | additionalProperty(String key, double value) |
| [FileSchemaTestClassMapBuilder](#fileschematestclassmapbuilder) | additionalProperty(String key, List<?> value) |
| [FileSchemaTestClassMapBuilder](#fileschematestclassmapbuilder) | additionalProperty(String key, Map<String, ?> value) |

## FileSchemaTestClassMap
public static class FileSchemaTestClassMap<br>
extends FrozenMap<String, @Nullable Object>

A class to store validated Map payloads

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| static [FileSchemaTestClassMap](#fileschematestclassmap) | of([Map<String, ? extends @Nullable Object>](#fileschematestclassmapbuilder) arg, SchemaConfiguration configuration) |
| [File.FileMap](../../components/schemas/File.md#filemap) | file()<br>[optional] |
| [FilesList](#fileslist) | files()<br>[optional] |
| @Nullable Object | getAdditionalProperty(String name)<br>provides type safety for additional properties |

## FilesBoxed
public sealed interface FilesBoxed<br>
permits<br>
[FilesBoxedList](#filesboxedlist)

sealed interface that stores validated payloads using boxed classes

## FilesBoxedList
public record FilesBoxedList<br>
implements [FilesBoxed](#filesboxed)

record that stores validated List payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| FilesBoxedList([FilesList](#fileslist) data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| [FilesList](#fileslist) | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## Files
public static class Files<br>
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
import org.openapijsonschematools.client.components.schemas.FileSchemaTestClass;

import java.util.Arrays;
import java.util.List;
import java.util.AbstractMap;

static final SchemaConfiguration configuration = new SchemaConfiguration(new JsonSchemaKeywordFlags.Builder().build());

// List validation
FileSchemaTestClass.FilesList validatedPayload =
    FileSchemaTestClass.Files.validate(
    new FileSchemaTestClass.FilesListBuilder()
    .build(),
    configuration
);
```

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Set<Class<?>> | type = Set.of(List.class) |
| Class<? extends JsonSchema> | items = [File.File1.class](../../components/schemas/File.md#file1) |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| [FilesList](#fileslist) | validate([List<?>](#fileslistbuilder) arg, SchemaConfiguration configuration) |
| [FilesBoxedList](#filesboxedlist) | validateAndBox([List<?>](#fileslistbuilder) arg, SchemaConfiguration configuration) |
| [FilesBoxed](#filesboxed) | validateAndBox(@Nullable Object arg, SchemaConfiguration configuration) |
| @Nullable Object | validate(@Nullable Object arg, SchemaConfiguration configuration) |

## FilesListBuilder
public class FilesListBuilder<br>
builder for `List<Map<String, @Nullable Object>>`

A class that builds the List input type

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| FilesListBuilder()<br>Creates an empty list |
| FilesListBuilder(List<Map<String, @Nullable Object>> items)<br>Stores the items in a list |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| FilesListBuilder | add(Map<String, @Nullable Object> item) |
| List<Map<String, @Nullable Object>> | build()<br>Returns list input that should be used with Schema.validate |

## FilesList
public class FilesList<br>
extends `FrozenList<File.FileMap>`

A class to store validated List payloads

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| static [FilesList](#fileslist) | of([List<Map<String, ? extends @Nullable Object>>](#fileslistbuilder) arg, SchemaConfiguration configuration) |

[[Back to top]](#top) [[Back to Component Schemas]](../../../README.md#Component-Schemas) [[Back to README]](../../../README.md)
