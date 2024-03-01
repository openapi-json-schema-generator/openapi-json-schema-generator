# Schema2
public class Schema2<br>

A class that contains necessary nested
- schema classes (which validate payloads), extends JsonSchema
- sealed interfaces which store validated payloads, java version of a sum type
- boxed classes which store validated payloads, sealed permits class implementations
- classes to store validated list payloads, extends FrozenList
- classes to build inputs for list payloads

## Nested Class Summary
| Modifier and Type | Class and Description |
| ----------------- | ---------------------- |
| sealed interface | [Schema2.Schema21Boxed](#schema21boxed)<br> sealed interface for validated payloads |
| record | [Schema2.Schema21BoxedList](#schema21boxedlist)<br> boxed class to store validated List payloads |
| static class | [Schema2.Schema21](#schema21)<br> schema class |
| static class | [Schema2.SchemaListBuilder2](#schemalistbuilder2)<br> builder for List payloads |
| static class | [Schema2.SchemaList2](#schemalist2)<br> output class for List payloads |
| sealed interface | [Schema2.Items2Boxed](#items2boxed)<br> sealed interface for validated payloads |
| record | [Schema2.Items2BoxedString](#items2boxedstring)<br> boxed class to store validated String payloads |
| static class | [Schema2.Items2](#items2)<br> schema class |

## Schema21Boxed
public sealed interface Schema21Boxed<br>
permits<br>
[Schema21BoxedList](#schema21boxedlist)

sealed interface that stores validated payloads using boxed classes

## Schema21BoxedList
public record Schema21BoxedList<br>
implements [Schema21Boxed](#schema21boxed)

record that stores validated List payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| Schema21BoxedList([SchemaList2](#schemalist2) data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| [SchemaList2](#schemalist2) | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## Schema21
public static class Schema21<br>
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
import org.openapijsonschematools.client.paths.faketestqueryparamters.put.parameters.parameter2.Schema2;

import java.util.Arrays;
import java.util.List;
import java.util.AbstractMap;

static final SchemaConfiguration configuration = new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone());

// List validation
Schema2.SchemaList2 validatedPayload =
    Schema2.Schema21.validate(
    new Schema2.SchemaListBuilder2()
        .add("a")

    .build(),
    configuration
);
```

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Set<Class<?>> | type = Set.of(List.class) |
| Class<? extends JsonSchema> | items = [Items2.class](#items2) |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| [SchemaList2](#schemalist2) | validate([List<?>](#schemalistbuilder2) arg, SchemaConfiguration configuration) |
| [Schema21BoxedList](#schema21boxedlist) | validateAndBox([List<?>](#schemalistbuilder2) arg, SchemaConfiguration configuration) |
| [Schema21Boxed](#schema21boxed) | validateAndBox(@Nullable Object arg, SchemaConfiguration configuration) |
| @Nullable Object | validate(@Nullable Object arg, SchemaConfiguration configuration) |

## SchemaListBuilder2
public class SchemaListBuilder2<br>
builder for `List<String>`

A class that builds the List input type

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| SchemaListBuilder2()<br>Creates an empty list |
| SchemaListBuilder2(List<String> items)<br>Stores the items in a list |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| SchemaListBuilder2 | add(String item) |
| List<String> | build()<br>Returns list input that should be used with Schema.validate |

## SchemaList2
public class SchemaList2<br>
extends `FrozenList<String>`

A class to store validated List payloads

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| static [SchemaList2](#schemalist2) | of([List<String>](#schemalistbuilder2) arg, SchemaConfiguration configuration) |

## Items2Boxed
public sealed interface Items2Boxed<br>
permits<br>
[Items2BoxedString](#items2boxedstring)

sealed interface that stores validated payloads using boxed classes

## Items2BoxedString
public record Items2BoxedString<br>
implements [Items2Boxed](#items2boxed)

record that stores validated String payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| Items2BoxedString(String data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| String | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## Items2
public static class Items2<br>
extends StringJsonSchema.StringJsonSchema1

A schema class that validates payloads

| Methods Inherited from class org.openapijsonschematools.client.schemas.StringJsonSchema.StringJsonSchema1 |
| ------------------------------------------------------------------ |
| validate                                                           |
| validateAndBox                                                     |
