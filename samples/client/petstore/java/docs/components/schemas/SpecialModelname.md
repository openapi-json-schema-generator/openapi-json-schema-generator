# SpecialModelname
org.openapijsonschematools.client.components.schemas.SpecialModelname.java
public class SpecialModelname

A class that contains necessary nested
- schema classes (which validate payloads), extends JsonSchema
- classes to store validated map payloads, extends FrozenMap
- classes to build inputs for map payloads

## Nested Class Summary
| Modifier and Type | Class and Description |
| ----------------- | ---------------------- |
| static class | [SpecialModelname.SpecialModelname1](#specialmodelname1)<br> schema class |
| static class | [SpecialModelname.SpecialModelnameMapBuilder](#specialmodelnamemapbuilder)<br> builder for Map payloads |
| static class | [SpecialModelname.SpecialModelnameMap](#specialmodelnamemap)<br> output class for Map payloads |
| static class | [SpecialModelname.A](#a)<br> schema class |

## SpecialModelname1
public static class SpecialModelname1<br>
extends JsonSchema

A schema class that validates payloads

## Description
model with an invalid class name for python

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
SpecialModelname.SpecialModelnameMap validatedPayload =
    SpecialModelname.SpecialModelname1.validate(
    new SpecialModelname.SpecialModelnameMapBuilder()
        .a("a")

    .build(),
    configuration
);
```

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Set<Class<?>> | type = Set.of(Map.class) |
| Map<String, Class<? extends JsonSchema>> | properties = Map.ofEntries(<br>&nbsp;&nbsp;&nbsp;&nbsp;new PropertyEntry("a", [A.class](#a)))<br>)<br> |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| [SpecialModelnameMap](#specialmodelnamemap) | validate([Map&lt;?, ?&gt;](#specialmodelnamemapbuilder) arg, SchemaConfiguration configuration) |
| @Nullable Object | validate(@Nullable Object arg, SchemaConfiguration configuration) |
## SpecialModelnameMapBuilder
public class SpecialModelnameMapBuilder<br>
builder for `Map<String, @Nullable Object>`

A class that builds the Map input type

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| SpecialModelnameMapBuilder()<br>Creates a builder that contains an empty map |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| Map<String, @Nullable Object> | build()<br>Returns map input that should be used with Schema.validate |
| [SpecialModelnameMapBuilder](#specialmodelnamemapbuilder) | a(String value) |
| [SpecialModelnameMapBuilder](#specialmodelnamemapbuilder) | additionalProperty(String key, Void value) |
| [SpecialModelnameMapBuilder](#specialmodelnamemapbuilder) | additionalProperty(String key, boolean value) |
| [SpecialModelnameMapBuilder](#specialmodelnamemapbuilder) | additionalProperty(String key, String value) |
| [SpecialModelnameMapBuilder](#specialmodelnamemapbuilder) | additionalProperty(String key, int value) |
| [SpecialModelnameMapBuilder](#specialmodelnamemapbuilder) | additionalProperty(String key, float value) |
| [SpecialModelnameMapBuilder](#specialmodelnamemapbuilder) | additionalProperty(String key, long value) |
| [SpecialModelnameMapBuilder](#specialmodelnamemapbuilder) | additionalProperty(String key, double value) |
| [SpecialModelnameMapBuilder](#specialmodelnamemapbuilder) | additionalProperty(String key, List<?> value) |
| [SpecialModelnameMapBuilder](#specialmodelnamemapbuilder) | additionalProperty(String key, Map<String, ?> value) |

## SpecialModelnameMap
public static class SpecialModelnameMap<br>
extends FrozenMap<String, @Nullable Object>

A class to store validated Map payloads

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| static [SpecialModelnameMap](#specialmodelnamemap) | of([Map<String, ? extends @Nullable Object>](#specialmodelnamemapbuilder) arg, SchemaConfiguration configuration) |
| String | a()<br>[optional] |
| @Nullable Object | getAdditionalProperty(String name)<br>provides type safety for additional properties |

## A
public static class A<br>
extends StringJsonSchema

A schema class that validates payloads

| Methods Inherited from class org.openapijsonschematools.client.schemas.StringJsonSchema |
| ------------------------------------------------------------------ |
| validate                                                           |

[[Back to top]](#top) [[Back to Component Schemas]](../../../README.md#Component-Schemas) [[Back to README]](../../../README.md)
