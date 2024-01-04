# Schema3
org.openapijsonschematools.client.paths.faketestqueryparamters.put.parameters.parameter3.Schema3.java
public class Schema3

A class that contains necessary nested
- schema classes (which validate payloads), extends JsonSchema
- classes to store validated list payloads, extends FrozenList
- classes to build inputs for list payloads

## Nested Class Summary
| Modifier and Type | Class and Description |
| ----------------- | ---------------------- |
| static class | [Schema3.Schema31](#schema31)<br> schema class |
| static class | [Schema3.SchemaListBuilder3](#schemalistbuilder3)<br> builder for List payloads |
| static class | [Schema3.SchemaList3](#schemalist3)<br> output class for List payloads |
| static class | [Schema3.Items3](#items3)<br> schema class |

## Schema31
public static class Schema31<br>
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

// List validation
Schema3.SchemaList3 validatedPayload =
    Schema3.Schema31.validate(
    new Schema3.SchemaListBuilder3()
        .add("a")

    .build(),
    configuration
);
```

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Set<Class<?>> | type = Set.of(List.class) |
| Class<? extends JsonSchema> | items = [Items3.class](#items3) |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| [SchemaList3](#schemalist3) | validate([List<?>](#schemalistbuilder3) arg, SchemaConfiguration configuration) |
| @Nullable Object | validate(@Nullable Object arg, SchemaConfiguration configuration) |
## SchemaListBuilder3
public class SchemaListBuilder3<br>
builder for `List<String>`

A class that builds the List input type

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| SchemaListBuilder3()<br>Creates an empty list |
| SchemaListBuilder3(List<String> items)<br>Stores the items in a list |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| SchemaListBuilder3 | add(String item) |
| List<String> | build()<br>Returns list input that should be used with Schema.validate |

## SchemaList3
public class SchemaList3<br>
extends `FrozenList<String>`

A class to store validated List payloads

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| static [SchemaList3](#schemalist3) | of([List<String>](#schemalistbuilder3) arg, SchemaConfiguration configuration) |

## Items3
public static class Items3<br>
extends StringJsonSchema

A schema class that validates payloads

| Methods Inherited from class org.openapijsonschematools.client.schemas.StringJsonSchema |
| ------------------------------------------------------------------ |
| validate                                                           |
