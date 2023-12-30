# ArrayHoldingAnyType
org.openapijsonschematools.client.components.schemas.ArrayHoldingAnyType.java
public class ArrayHoldingAnyType

A class that contains necessary nested
- schema classes (which validate payloads), extends JsonSchema
- classes to store validated list payloads, extends FrozenList
- classes to build inputs for list payloads

## Nested Class Summary
| Modifier and Type | Class and Description |
| ----------------- | ---------------------- |
| static class | [ArrayHoldingAnyType.ArrayHoldingAnyType1](#arrayholdinganytype1)<br> schema class |
| static class | [ArrayHoldingAnyType.ArrayHoldingAnyTypeListBuilder](#arrayholdinganytypelistbuilder)<br> builder for List payloads |
| static class | [ArrayHoldingAnyType.ArrayHoldingAnyTypeList](#arrayholdinganytypelist)<br> output class for List payloads |
| static class | [ArrayHoldingAnyType.Items](#items)<br> schema class |

## ArrayHoldingAnyType1
public static class ArrayHoldingAnyType1<br>
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

// List validation
ArrayHoldingAnyType.ArrayHoldingAnyTypeList validatedPayload =
    ArrayHoldingAnyType.ArrayHoldingAnyType1.validate(
    new ArrayHoldingAnyType.ArrayHoldingAnyTypeListBuilder(
        Arrays.asList(
        )
    ).build(),
    configuration
);
```

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Set<Class<?>> | type = Set.of(List.class) |
| Class<? extends JsonSchema> | items = [Items.class](#items) |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| [ArrayHoldingAnyTypeList](#arrayholdinganytypelist) | validate([List<?>](#arrayholdinganytypelistbuilder) arg, SchemaConfiguration configuration) |
| @Nullable Object | validate(@Nullable Object arg, SchemaConfiguration configuration) |
## ArrayHoldingAnyTypeListBuilder
public class ArrayHoldingAnyTypeListBuilder<br>
builder for `List<@Nullable Object>`

A class that builds the List input type

## Constructor Summary
| Constructor and Description |
| --------------------------- |
| ArrayHoldingAnyTypeListBuilder()<br>Creates an empty list |
| ArrayHoldingAnyTypeListBuilder(List<@Nullable Object> items)<br>Stores the items in a list |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| ArrayHoldingAnyTypeListBuilder | add(Void item) |
| ArrayHoldingAnyTypeListBuilder | add(boolean item) |
| ArrayHoldingAnyTypeListBuilder | add(String item) |
| ArrayHoldingAnyTypeListBuilder | add(int item) |
| ArrayHoldingAnyTypeListBuilder | add(float item) |
| ArrayHoldingAnyTypeListBuilder | add(long item) |
| ArrayHoldingAnyTypeListBuilder | add(double item) |
| ArrayHoldingAnyTypeListBuilder | add(List<?> item) |
| ArrayHoldingAnyTypeListBuilder | add(Map<String, ?> item) |
| List<@Nullable Object> | build()<br>Returns list input that should be used with Schema.validate |

## ArrayHoldingAnyTypeList
public class ArrayHoldingAnyTypeList<br>
extends `FrozenList<@Nullable Object>`

A class to store validated List payloads

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| static [ArrayHoldingAnyTypeList](#arrayholdinganytypelist) | of([List<? extends @Nullable Object>](#arrayholdinganytypelistbuilder) arg, SchemaConfiguration configuration) |

## Items
public static class Items<br>
extends AnyTypeJsonSchema

A schema class that validates payloads

## Description
any type can be stored here

| Methods Inherited from class org.openapijsonschematools.client.schemas.AnyTypeJsonSchema |
| ------------------------------------------------------------------ |
| validate                                                           |

[[Back to top]](#top) [[Back to Component Schemas]](../../../README.md#Component-Schemas) [[Back to README]](../../../README.md)
