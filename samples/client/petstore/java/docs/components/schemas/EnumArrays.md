# EnumArrays
org.openapijsonschematools.client.components.schemas.EnumArrays.java
public class EnumArrays<br>

A class that contains necessary nested
- schema classes (which validate payloads), extends JsonSchema
- sealed interfaces which store validated payloads, java version of a sum type
- boxed classes which store validated payloads, sealed permits class implementations
- classes to store validated list payloads, extends FrozenList
- classes to build inputs for list payloads
- classes to store validated map payloads, extends FrozenMap
- classes to build inputs for map payloads
- enum classes

## Nested Class Summary
| Modifier and Type | Class and Description |
| ----------------- | ---------------------- |
| sealed interface | [EnumArrays.EnumArrays1Boxed](#enumarrays1boxed)<br> sealed interface for validated payloads |
| record | [EnumArrays.EnumArrays1BoxedMap](#enumarrays1boxedmap)<br> boxed class to store validated Map payloads |
| static class | [EnumArrays.EnumArrays1](#enumarrays1)<br> schema class |
| static class | [EnumArrays.EnumArraysMapBuilder](#enumarraysmapbuilder)<br> builder for Map payloads |
| static class | [EnumArrays.EnumArraysMap](#enumarraysmap)<br> output class for Map payloads |
| sealed interface | [EnumArrays.ArrayEnumBoxed](#arrayenumboxed)<br> sealed interface for validated payloads |
| record | [EnumArrays.ArrayEnumBoxedList](#arrayenumboxedlist)<br> boxed class to store validated List payloads |
| static class | [EnumArrays.ArrayEnum](#arrayenum)<br> schema class |
| static class | [EnumArrays.ArrayEnumListBuilder](#arrayenumlistbuilder)<br> builder for List payloads |
| static class | [EnumArrays.ArrayEnumList](#arrayenumlist)<br> output class for List payloads |
| sealed interface | [EnumArrays.ItemsBoxed](#itemsboxed)<br> sealed interface for validated payloads |
| record | [EnumArrays.ItemsBoxedString](#itemsboxedstring)<br> boxed class to store validated String payloads |
| static class | [EnumArrays.Items](#items)<br> schema class |
| enum | [EnumArrays.StringItemsEnums](#stringitemsenums)<br>String enum |
| sealed interface | [EnumArrays.JustSymbolBoxed](#justsymbolboxed)<br> sealed interface for validated payloads |
| record | [EnumArrays.JustSymbolBoxedString](#justsymbolboxedstring)<br> boxed class to store validated String payloads |
| static class | [EnumArrays.JustSymbol](#justsymbol)<br> schema class |
| enum | [EnumArrays.StringJustSymbolEnums](#stringjustsymbolenums)<br>String enum |

## EnumArrays1Boxed
public sealed interface EnumArrays1Boxed<br>
permits<br>
[EnumArrays1BoxedMap](#enumarrays1boxedmap)

sealed interface that stores validated payloads using boxed classes

## EnumArrays1BoxedMap
public record EnumArrays1BoxedMap<br>
implements [EnumArrays1Boxed](#enumarrays1boxed)

record that stores validated Map payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| EnumArrays1BoxedMap([EnumArraysMap](#enumarraysmap) data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| [EnumArraysMap](#enumarraysmap) | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## EnumArrays1
public static class EnumArrays1<br>
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
import org.openapijsonschematools.client.components.schemas.EnumArrays;

import java.util.Arrays;
import java.util.List;
import java.util.AbstractMap;

static final SchemaConfiguration configuration = new SchemaConfiguration(new JsonSchemaKeywordFlags.Builder().build());

// Map validation
EnumArrays.EnumArraysMap validatedPayload =
    EnumArrays.EnumArrays1.validate(
    new EnumArrays.EnumArraysMapBuilder()
        .just_symbol(">=")

        .array_enum(
            Arrays.asList(
                "fish"
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
| Map<String, Class<? extends JsonSchema>> | properties = Map.ofEntries(<br>&nbsp;&nbsp;&nbsp;&nbsp;new PropertyEntry("just_symbol", [JustSymbol.class](#justsymbol))),<br>&nbsp;&nbsp;&nbsp;&nbsp;new PropertyEntry("array_enum", [ArrayEnum.class](#arrayenum)))<br>)<br> |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| [EnumArraysMap](#enumarraysmap) | validate([Map&lt;?, ?&gt;](#enumarraysmapbuilder) arg, SchemaConfiguration configuration) |
| [EnumArrays1BoxedMap](#enumarrays1boxedmap) | validateAndBox([Map&lt;?, ?&gt;](#enumarraysmapbuilder) arg, SchemaConfiguration configuration) |
| [EnumArrays1Boxed](#enumarrays1boxed) | validateAndBox(@Nullable Object arg, SchemaConfiguration configuration) |
| @Nullable Object | validate(@Nullable Object arg, SchemaConfiguration configuration) |

## EnumArraysMapBuilder
public class EnumArraysMapBuilder<br>
builder for `Map<String, @Nullable Object>`

A class that builds the Map input type

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| EnumArraysMapBuilder()<br>Creates a builder that contains an empty map |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| Map<String, @Nullable Object> | build()<br>Returns map input that should be used with Schema.validate |
| [EnumArraysMapBuilder](#enumarraysmapbuilder) | just_symbol(String value) |
| [EnumArraysMapBuilder](#enumarraysmapbuilder) | just_symbol([StringJustSymbolEnums](#stringjustsymbolenums) value) |
| [EnumArraysMapBuilder](#enumarraysmapbuilder) | array_enum(List<String> value) |
| [EnumArraysMapBuilder](#enumarraysmapbuilder) | additionalProperty(String key, Void value) |
| [EnumArraysMapBuilder](#enumarraysmapbuilder) | additionalProperty(String key, boolean value) |
| [EnumArraysMapBuilder](#enumarraysmapbuilder) | additionalProperty(String key, String value) |
| [EnumArraysMapBuilder](#enumarraysmapbuilder) | additionalProperty(String key, int value) |
| [EnumArraysMapBuilder](#enumarraysmapbuilder) | additionalProperty(String key, float value) |
| [EnumArraysMapBuilder](#enumarraysmapbuilder) | additionalProperty(String key, long value) |
| [EnumArraysMapBuilder](#enumarraysmapbuilder) | additionalProperty(String key, double value) |
| [EnumArraysMapBuilder](#enumarraysmapbuilder) | additionalProperty(String key, List<?> value) |
| [EnumArraysMapBuilder](#enumarraysmapbuilder) | additionalProperty(String key, Map<String, ?> value) |

## EnumArraysMap
public static class EnumArraysMap<br>
extends FrozenMap<String, @Nullable Object>

A class to store validated Map payloads

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| static [EnumArraysMap](#enumarraysmap) | of([Map<String, ? extends @Nullable Object>](#enumarraysmapbuilder) arg, SchemaConfiguration configuration) |
| String | just_symbol()<br>[optional] must be one of [">=", "$"] |
| [ArrayEnumList](#arrayenumlist) | array_enum()<br>[optional] |
| @Nullable Object | getAdditionalProperty(String name)<br>provides type safety for additional properties |

## ArrayEnumBoxed
public sealed interface ArrayEnumBoxed<br>
permits<br>
[ArrayEnumBoxedList](#arrayenumboxedlist)

sealed interface that stores validated payloads using boxed classes

## ArrayEnumBoxedList
public record ArrayEnumBoxedList<br>
implements [ArrayEnumBoxed](#arrayenumboxed)

record that stores validated List payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| ArrayEnumBoxedList([ArrayEnumList](#arrayenumlist) data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| [ArrayEnumList](#arrayenumlist) | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## ArrayEnum
public static class ArrayEnum<br>
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
import org.openapijsonschematools.client.components.schemas.EnumArrays;

import java.util.Arrays;
import java.util.List;
import java.util.AbstractMap;

static final SchemaConfiguration configuration = new SchemaConfiguration(new JsonSchemaKeywordFlags.Builder().build());

// List validation
EnumArrays.ArrayEnumList validatedPayload =
    EnumArrays.ArrayEnum.validate(
    new EnumArrays.ArrayEnumListBuilder()
        .add("fish")

    .build(),
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
| [ArrayEnumList](#arrayenumlist) | validate([List<?>](#arrayenumlistbuilder) arg, SchemaConfiguration configuration) |
| [ArrayEnumBoxedList](#arrayenumboxedlist) | validateAndBox([List<?>](#arrayenumlistbuilder) arg, SchemaConfiguration configuration) |
| [ArrayEnumBoxed](#arrayenumboxed) | validateAndBox(@Nullable Object arg, SchemaConfiguration configuration) |
| @Nullable Object | validate(@Nullable Object arg, SchemaConfiguration configuration) |

## ArrayEnumListBuilder
public class ArrayEnumListBuilder<br>
builder for `List<String>`

A class that builds the List input type

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| ArrayEnumListBuilder()<br>Creates an empty list |
| ArrayEnumListBuilder(List<String> items)<br>Stores the items in a list |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| ArrayEnumListBuilder | add(String item) |
| ArrayEnumListBuilder | add([StringItemsEnums](#stringitemsenums) item) |
| List<String> | build()<br>Returns list input that should be used with Schema.validate |

## ArrayEnumList
public class ArrayEnumList<br>
extends `FrozenList<String>`

A class to store validated List payloads

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| static [ArrayEnumList](#arrayenumlist) | of([List<String>](#arrayenumlistbuilder) arg, SchemaConfiguration configuration) |

## ItemsBoxed
public sealed interface ItemsBoxed<br>
permits<br>
[ItemsBoxedString](#itemsboxedstring)

sealed interface that stores validated payloads using boxed classes

## ItemsBoxedString
public record ItemsBoxedString<br>
implements [ItemsBoxed](#itemsboxed)

record that stores validated String payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| ItemsBoxedString(String data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| String | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## Items
public static class Items<br>
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
import org.openapijsonschematools.client.components.schemas.EnumArrays;

import java.util.Arrays;
import java.util.List;
import java.util.AbstractMap;

static final SchemaConfiguration configuration = new SchemaConfiguration(new JsonSchemaKeywordFlags.Builder().build());

// String validation
String validatedPayload = EnumArrays.Items.validate(
    "fish",
    configuration
);
```

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Set<Class<?>> | type = Set.of(<br/>&nbsp;&nbsp;&nbsp;&nbsp;String.class<br/>)<br/> |
| Set<Object> | enumValues = SetMaker.makeSet(<br>&nbsp;&nbsp;&nbsp;&nbsp;"fish",<br>&nbsp;&nbsp;&nbsp;&nbsp;"crab"<br>)<br> |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| String | validate(String arg, SchemaConfiguration configuration) |
| String | validate([StringItemsEnums](#stringitemsenums) arg, SchemaConfiguration configuration) |
| [ItemsBoxedString](#itemsboxedstring) | validateAndBox(String arg, SchemaConfiguration configuration) |
| [ItemsBoxed](#itemsboxed) | validateAndBox(@Nullable Object arg, SchemaConfiguration configuration) |
| @Nullable Object | validate(@Nullable Object arg, SchemaConfiguration configuration) |

## StringItemsEnums
public enum StringItemsEnums<br>
extends `Enum<StringItemsEnums>`

A class that stores String enum values

### Enum Constant Summary
| Enum Constant | Description |
| ------------- | ----------- |
| FISH | value = "fish" |
| CRAB | value = "crab" |

## JustSymbolBoxed
public sealed interface JustSymbolBoxed<br>
permits<br>
[JustSymbolBoxedString](#justsymbolboxedstring)

sealed interface that stores validated payloads using boxed classes

## JustSymbolBoxedString
public record JustSymbolBoxedString<br>
implements [JustSymbolBoxed](#justsymbolboxed)

record that stores validated String payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| JustSymbolBoxedString(String data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| String | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## JustSymbol
public static class JustSymbol<br>
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
import org.openapijsonschematools.client.components.schemas.EnumArrays;

import java.util.Arrays;
import java.util.List;
import java.util.AbstractMap;

static final SchemaConfiguration configuration = new SchemaConfiguration(new JsonSchemaKeywordFlags.Builder().build());

// String validation
String validatedPayload = EnumArrays.JustSymbol.validate(
    ">=",
    configuration
);
```

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Set<Class<?>> | type = Set.of(<br/>&nbsp;&nbsp;&nbsp;&nbsp;String.class<br/>)<br/> |
| Set<Object> | enumValues = SetMaker.makeSet(<br>&nbsp;&nbsp;&nbsp;&nbsp;">=",<br>&nbsp;&nbsp;&nbsp;&nbsp;"$"<br>)<br> |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| String | validate(String arg, SchemaConfiguration configuration) |
| String | validate([StringJustSymbolEnums](#stringjustsymbolenums) arg, SchemaConfiguration configuration) |
| [JustSymbolBoxedString](#justsymbolboxedstring) | validateAndBox(String arg, SchemaConfiguration configuration) |
| [JustSymbolBoxed](#justsymbolboxed) | validateAndBox(@Nullable Object arg, SchemaConfiguration configuration) |
| @Nullable Object | validate(@Nullable Object arg, SchemaConfiguration configuration) |

## StringJustSymbolEnums
public enum StringJustSymbolEnums<br>
extends `Enum<StringJustSymbolEnums>`

A class that stores String enum values

### Enum Constant Summary
| Enum Constant | Description |
| ------------- | ----------- |
| GREATER_THAN_SIGN_EQUALS_SIGN | value = ">=" |
| DOLLAR_SIGN | value = "$" |

[[Back to top]](#top) [[Back to Component Schemas]](../../../README.md#Component-Schemas) [[Back to README]](../../../README.md)
