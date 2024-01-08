# Schema1
public class Schema1

A class that contains necessary nested
- schema classes (which validate payloads), extends JsonSchema
- classes to store validated map payloads, extends FrozenMap
- classes to build inputs for map payloads

## Nested Class Summary
| Modifier and Type | Class and Description |
| ----------------- | ---------------------- |
| static class | [Schema1.Schema11](#schema11)<br> schema class |
| static class | [Schema1.SchemaMapBuilder1](#schemamapbuilder1)<br> builder for Map payloads |
| static class | [Schema1.SchemaMap1](#schemamap1)<br> output class for Map payloads |
| static class | [Schema1.SomeProp1](#someprop1)<br> schema class |
| static class | [Schema1.Schema01](#schema01)<br> schema class |

## Schema11
public static class Schema11<br>
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
Schema1.SchemaMap1 validatedPayload =
    Schema1.Schema11.validate(
    new Schema1.SchemaMapBuilder1()
    .build(),
    configuration
);
```

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Set<Class<?>> | type = Set.of(Map.class) |
| Map<String, Class<? extends JsonSchema>> | properties = Map.ofEntries(<br>&nbsp;&nbsp;&nbsp;&nbsp;new PropertyEntry("someProp", [SomeProp1.class](#someprop1)))<br>)<br> |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| [SchemaMap1](#schemamap1) | validate([Map&lt;?, ?&gt;](#schemamapbuilder1) arg, SchemaConfiguration configuration) |
| @Nullable Object | validate(@Nullable Object arg, SchemaConfiguration configuration) |
## SchemaMapBuilder1
public class SchemaMapBuilder1<br>
builder for `Map<String, @Nullable Object>`

A class that builds the Map input type

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| SchemaMapBuilder1()<br>Creates a builder that contains an empty map |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| Map<String, @Nullable Object> | build()<br>Returns map input that should be used with Schema.validate |
| [SchemaMapBuilder1](#schemamapbuilder1) | someProp(Void value) |
| [SchemaMapBuilder1](#schemamapbuilder1) | someProp(boolean value) |
| [SchemaMapBuilder1](#schemamapbuilder1) | someProp(String value) |
| [SchemaMapBuilder1](#schemamapbuilder1) | someProp(int value) |
| [SchemaMapBuilder1](#schemamapbuilder1) | someProp(float value) |
| [SchemaMapBuilder1](#schemamapbuilder1) | someProp(long value) |
| [SchemaMapBuilder1](#schemamapbuilder1) | someProp(double value) |
| [SchemaMapBuilder1](#schemamapbuilder1) | someProp(List<?> value) |
| [SchemaMapBuilder1](#schemamapbuilder1) | someProp(Map<String, ?> value) |
| [SchemaMapBuilder1](#schemamapbuilder1) | additionalProperty(String key, Void value) |
| [SchemaMapBuilder1](#schemamapbuilder1) | additionalProperty(String key, boolean value) |
| [SchemaMapBuilder1](#schemamapbuilder1) | additionalProperty(String key, String value) |
| [SchemaMapBuilder1](#schemamapbuilder1) | additionalProperty(String key, int value) |
| [SchemaMapBuilder1](#schemamapbuilder1) | additionalProperty(String key, float value) |
| [SchemaMapBuilder1](#schemamapbuilder1) | additionalProperty(String key, long value) |
| [SchemaMapBuilder1](#schemamapbuilder1) | additionalProperty(String key, double value) |
| [SchemaMapBuilder1](#schemamapbuilder1) | additionalProperty(String key, List<?> value) |
| [SchemaMapBuilder1](#schemamapbuilder1) | additionalProperty(String key, Map<String, ?> value) |

## SchemaMap1
public static class SchemaMap1<br>
extends FrozenMap<String, @Nullable Object>

A class to store validated Map payloads

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| static [SchemaMap1](#schemamap1) | of([Map<String, ? extends @Nullable Object>](#schemamapbuilder1) arg, SchemaConfiguration configuration) |
| @Nullable Object | someProp()<br>[optional] |
| @Nullable Object | getAdditionalProperty(String name)<br>provides type safety for additional properties |

## SomeProp1
public static class SomeProp1<br>
extends JsonSchema

A schema class that validates payloads

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| List<Class<? extends JsonSchema>> | allOf = List.of(<br>&nbsp;&nbsp;&nbsp;&nbsp;[Schema01.class](#schema01)<br>;)<br> |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| String | validate(String arg, SchemaConfiguration configuration) |
| Void | validate(Void arg, SchemaConfiguration configuration) |
| int | validate(int arg, SchemaConfiguration configuration) |
| long | validate(long arg, SchemaConfiguration configuration) |
| float | validate(float arg, SchemaConfiguration configuration) |
| double | validate(double arg, SchemaConfiguration configuration) |
| boolean | validate(boolean arg, SchemaConfiguration configuration) |
| FrozenMap<String, @Nullable Object> | validate(Map&lt;?, ?&gt; arg, SchemaConfiguration configuration) |
| FrozenList<@Nullable Object> | validate(List<?> arg, SchemaConfiguration configuration) |
| @Nullable Object | validate(@Nullable Object arg, SchemaConfiguration configuration) |
## Schema01
public static class Schema01<br>
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
String validatedPayload = Schema1.Schema01.validate(
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
| @Nullable Object | validate(@Nullable Object arg, SchemaConfiguration configuration) |