# ApplicationxwwwformurlencodedSchema
public class ApplicationxwwwformurlencodedSchema<br>

A class that contains necessary nested
- schema classes (which validate payloads), extends JsonSchema
- abstract sealed classes which store validated payloads, java version of a sum type
- boxed classes which store validated payloads, sealed permits class implementations
- classes to store validated map payloads, extends FrozenMap
- classes to build inputs for map payloads

## Nested Class Summary
| Modifier and Type | Class and Description |
| ----------------- | ---------------------- |
| static class | [ApplicationxwwwformurlencodedSchema.ApplicationxwwwformurlencodedSchema1Boxed](#applicationxwwwformurlencodedschema1boxed)<br> abstract sealed validated payload class |
| static class | [ApplicationxwwwformurlencodedSchema.ApplicationxwwwformurlencodedSchema1BoxedMap](#applicationxwwwformurlencodedschema1boxedmap)<br> boxed class to store validated Map payloads |
| static class | [ApplicationxwwwformurlencodedSchema.ApplicationxwwwformurlencodedSchema1](#applicationxwwwformurlencodedschema1)<br> schema class |
| static class | [ApplicationxwwwformurlencodedSchema.ApplicationxwwwformurlencodedSchemaMapBuilder](#applicationxwwwformurlencodedschemamapbuilder)<br> builder for Map payloads |
| static class | [ApplicationxwwwformurlencodedSchema.ApplicationxwwwformurlencodedSchemaMap](#applicationxwwwformurlencodedschemamap)<br> output class for Map payloads |
| static class | [ApplicationxwwwformurlencodedSchema.ApplicationxwwwformurlencodedStatusBoxed](#applicationxwwwformurlencodedstatusboxed)<br> abstract sealed validated payload class |
| static class | [ApplicationxwwwformurlencodedSchema.ApplicationxwwwformurlencodedStatusBoxedString](#applicationxwwwformurlencodedstatusboxedstring)<br> boxed class to store validated String payloads |
| static class | [ApplicationxwwwformurlencodedSchema.ApplicationxwwwformurlencodedStatus](#applicationxwwwformurlencodedstatus)<br> schema class |
| static class | [ApplicationxwwwformurlencodedSchema.ApplicationxwwwformurlencodedNameBoxed](#applicationxwwwformurlencodednameboxed)<br> abstract sealed validated payload class |
| static class | [ApplicationxwwwformurlencodedSchema.ApplicationxwwwformurlencodedNameBoxedString](#applicationxwwwformurlencodednameboxedstring)<br> boxed class to store validated String payloads |
| static class | [ApplicationxwwwformurlencodedSchema.ApplicationxwwwformurlencodedName](#applicationxwwwformurlencodedname)<br> schema class |

## ApplicationxwwwformurlencodedSchema1Boxed
public static abstract sealed class ApplicationxwwwformurlencodedSchema1Boxed<br>
permits<br>
[ApplicationxwwwformurlencodedSchema1BoxedMap](#applicationxwwwformurlencodedschema1boxedmap)

abstract sealed class that stores validated payloads using boxed classes

## ApplicationxwwwformurlencodedSchema1BoxedMap
public static final class ApplicationxwwwformurlencodedSchema1BoxedMap<br>
extends [ApplicationxwwwformurlencodedSchema1Boxed](#applicationxwwwformurlencodedschema1boxed)

a boxed class to store validated Map payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| ApplicationxwwwformurlencodedSchema1BoxedMap([ApplicationxwwwformurlencodedSchemaMap](#applicationxwwwformurlencodedschemamap) data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| [ApplicationxwwwformurlencodedSchemaMap](#applicationxwwwformurlencodedschemamap) | data<br>validated payload |

## ApplicationxwwwformurlencodedSchema1
public static class ApplicationxwwwformurlencodedSchema1<br>
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
ApplicationxwwwformurlencodedSchema.ApplicationxwwwformurlencodedSchemaMap validatedPayload =
    ApplicationxwwwformurlencodedSchema.ApplicationxwwwformurlencodedSchema1.validate(
    new ApplicationxwwwformurlencodedSchema.ApplicationxwwwformurlencodedSchemaMapBuilder()
        .name("a")

        .status("a")

    .build(),
    configuration
);
```

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Set<Class<?>> | type = Set.of(Map.class) |
| Map<String, Class<? extends JsonSchema>> | properties = Map.ofEntries(<br>&nbsp;&nbsp;&nbsp;&nbsp;new PropertyEntry("name", [ApplicationxwwwformurlencodedName.class](#applicationxwwwformurlencodedname))),<br>&nbsp;&nbsp;&nbsp;&nbsp;new PropertyEntry("status", [ApplicationxwwwformurlencodedStatus.class](#applicationxwwwformurlencodedstatus)))<br>)<br> |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| [ApplicationxwwwformurlencodedSchemaMap](#applicationxwwwformurlencodedschemamap) | validate([Map&lt;?, ?&gt;](#applicationxwwwformurlencodedschemamapbuilder) arg, SchemaConfiguration configuration) |
| [ApplicationxwwwformurlencodedSchema1BoxedMap](#applicationxwwwformurlencodedschema1boxedmap) | validateAndBox([Map&lt;?, ?&gt;](#applicationxwwwformurlencodedschemamapbuilder) arg, SchemaConfiguration configuration) |
| @Nullable Object | validate(@Nullable Object arg, SchemaConfiguration configuration) |
## ApplicationxwwwformurlencodedSchemaMapBuilder
public class ApplicationxwwwformurlencodedSchemaMapBuilder<br>
builder for `Map<String, @Nullable Object>`

A class that builds the Map input type

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| ApplicationxwwwformurlencodedSchemaMapBuilder()<br>Creates a builder that contains an empty map |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| Map<String, @Nullable Object> | build()<br>Returns map input that should be used with Schema.validate |
| [ApplicationxwwwformurlencodedSchemaMapBuilder](#applicationxwwwformurlencodedschemamapbuilder) | name(String value) |
| [ApplicationxwwwformurlencodedSchemaMapBuilder](#applicationxwwwformurlencodedschemamapbuilder) | status(String value) |
| [ApplicationxwwwformurlencodedSchemaMapBuilder](#applicationxwwwformurlencodedschemamapbuilder) | additionalProperty(String key, Void value) |
| [ApplicationxwwwformurlencodedSchemaMapBuilder](#applicationxwwwformurlencodedschemamapbuilder) | additionalProperty(String key, boolean value) |
| [ApplicationxwwwformurlencodedSchemaMapBuilder](#applicationxwwwformurlencodedschemamapbuilder) | additionalProperty(String key, String value) |
| [ApplicationxwwwformurlencodedSchemaMapBuilder](#applicationxwwwformurlencodedschemamapbuilder) | additionalProperty(String key, int value) |
| [ApplicationxwwwformurlencodedSchemaMapBuilder](#applicationxwwwformurlencodedschemamapbuilder) | additionalProperty(String key, float value) |
| [ApplicationxwwwformurlencodedSchemaMapBuilder](#applicationxwwwformurlencodedschemamapbuilder) | additionalProperty(String key, long value) |
| [ApplicationxwwwformurlencodedSchemaMapBuilder](#applicationxwwwformurlencodedschemamapbuilder) | additionalProperty(String key, double value) |
| [ApplicationxwwwformurlencodedSchemaMapBuilder](#applicationxwwwformurlencodedschemamapbuilder) | additionalProperty(String key, List<?> value) |
| [ApplicationxwwwformurlencodedSchemaMapBuilder](#applicationxwwwformurlencodedschemamapbuilder) | additionalProperty(String key, Map<String, ?> value) |

## ApplicationxwwwformurlencodedSchemaMap
public static class ApplicationxwwwformurlencodedSchemaMap<br>
extends FrozenMap<String, @Nullable Object>

A class to store validated Map payloads

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| static [ApplicationxwwwformurlencodedSchemaMap](#applicationxwwwformurlencodedschemamap) | of([Map<String, ? extends @Nullable Object>](#applicationxwwwformurlencodedschemamapbuilder) arg, SchemaConfiguration configuration) |
| String | name()<br>[optional] |
| String | status()<br>[optional] |
| @Nullable Object | getAdditionalProperty(String name)<br>provides type safety for additional properties |

## ApplicationxwwwformurlencodedStatusBoxed
public static abstract sealed class ApplicationxwwwformurlencodedStatusBoxed<br>
permits<br>
[ApplicationxwwwformurlencodedStatusBoxedString](#applicationxwwwformurlencodedstatusboxedstring)

abstract sealed class that stores validated payloads using boxed classes

## ApplicationxwwwformurlencodedStatusBoxedString
public static final class ApplicationxwwwformurlencodedStatusBoxedString<br>
extends [ApplicationxwwwformurlencodedStatusBoxed](#applicationxwwwformurlencodedstatusboxed)

a boxed class to store validated String payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| ApplicationxwwwformurlencodedStatusBoxedString(String data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| String | data<br>validated payload |

## ApplicationxwwwformurlencodedStatus
public static class ApplicationxwwwformurlencodedStatus<br>
extends StringJsonSchema.StringJsonSchema1

A schema class that validates payloads

## Description
Updated status of the pet

| Methods Inherited from class org.openapijsonschematools.client.schemas.StringJsonSchema.StringJsonSchema1 |
| ------------------------------------------------------------------ |
| validate                                                           |
| validateAndBox                                                     |

## ApplicationxwwwformurlencodedNameBoxed
public static abstract sealed class ApplicationxwwwformurlencodedNameBoxed<br>
permits<br>
[ApplicationxwwwformurlencodedNameBoxedString](#applicationxwwwformurlencodednameboxedstring)

abstract sealed class that stores validated payloads using boxed classes

## ApplicationxwwwformurlencodedNameBoxedString
public static final class ApplicationxwwwformurlencodedNameBoxedString<br>
extends [ApplicationxwwwformurlencodedNameBoxed](#applicationxwwwformurlencodednameboxed)

a boxed class to store validated String payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| ApplicationxwwwformurlencodedNameBoxedString(String data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| String | data<br>validated payload |

## ApplicationxwwwformurlencodedName
public static class ApplicationxwwwformurlencodedName<br>
extends StringJsonSchema.StringJsonSchema1

A schema class that validates payloads

## Description
Updated name of the pet

| Methods Inherited from class org.openapijsonschematools.client.schemas.StringJsonSchema.StringJsonSchema1 |
| ------------------------------------------------------------------ |
| validate                                                           |
| validateAndBox                                                     |
