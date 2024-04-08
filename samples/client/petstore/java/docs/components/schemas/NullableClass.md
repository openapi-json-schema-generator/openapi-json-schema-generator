# NullableClass
org.openapijsonschematools.client.components.schemas.NullableClass.java
public class NullableClass<br>

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
| sealed interface | [NullableClass.NullableClass1Boxed](#nullableclass1boxed)<br> sealed interface for validated payloads |
| record | [NullableClass.NullableClass1BoxedMap](#nullableclass1boxedmap)<br> boxed class to store validated Map payloads |
| static class | [NullableClass.NullableClass1](#nullableclass1)<br> schema class |
| static class | [NullableClass.NullableClassMapBuilder](#nullableclassmapbuilder)<br> builder for Map payloads |
| static class | [NullableClass.NullableClassMap](#nullableclassmap)<br> output class for Map payloads |
| sealed interface | [NullableClass.ObjectItemsNullableBoxed](#objectitemsnullableboxed)<br> sealed interface for validated payloads |
| record | [NullableClass.ObjectItemsNullableBoxedMap](#objectitemsnullableboxedmap)<br> boxed class to store validated Map payloads |
| static class | [NullableClass.ObjectItemsNullable](#objectitemsnullable)<br> schema class |
| static class | [NullableClass.ObjectItemsNullableMapBuilder](#objectitemsnullablemapbuilder)<br> builder for Map payloads |
| static class | [NullableClass.ObjectItemsNullableMap](#objectitemsnullablemap)<br> output class for Map payloads |
| sealed interface | [NullableClass.AdditionalProperties2Boxed](#additionalproperties2boxed)<br> sealed interface for validated payloads |
| record | [NullableClass.AdditionalProperties2BoxedVoid](#additionalproperties2boxedvoid)<br> boxed class to store validated null payloads |
| record | [NullableClass.AdditionalProperties2BoxedMap](#additionalproperties2boxedmap)<br> boxed class to store validated Map payloads |
| static class | [NullableClass.AdditionalProperties2](#additionalproperties2)<br> schema class |
| sealed interface | [NullableClass.ObjectAndItemsNullablePropBoxed](#objectanditemsnullablepropboxed)<br> sealed interface for validated payloads |
| record | [NullableClass.ObjectAndItemsNullablePropBoxedVoid](#objectanditemsnullablepropboxedvoid)<br> boxed class to store validated null payloads |
| record | [NullableClass.ObjectAndItemsNullablePropBoxedMap](#objectanditemsnullablepropboxedmap)<br> boxed class to store validated Map payloads |
| static class | [NullableClass.ObjectAndItemsNullableProp](#objectanditemsnullableprop)<br> schema class |
| static class | [NullableClass.ObjectAndItemsNullablePropMapBuilder](#objectanditemsnullablepropmapbuilder)<br> builder for Map payloads |
| static class | [NullableClass.ObjectAndItemsNullablePropMap](#objectanditemsnullablepropmap)<br> output class for Map payloads |
| sealed interface | [NullableClass.AdditionalProperties1Boxed](#additionalproperties1boxed)<br> sealed interface for validated payloads |
| record | [NullableClass.AdditionalProperties1BoxedVoid](#additionalproperties1boxedvoid)<br> boxed class to store validated null payloads |
| record | [NullableClass.AdditionalProperties1BoxedMap](#additionalproperties1boxedmap)<br> boxed class to store validated Map payloads |
| static class | [NullableClass.AdditionalProperties1](#additionalproperties1)<br> schema class |
| sealed interface | [NullableClass.ObjectNullablePropBoxed](#objectnullablepropboxed)<br> sealed interface for validated payloads |
| record | [NullableClass.ObjectNullablePropBoxedVoid](#objectnullablepropboxedvoid)<br> boxed class to store validated null payloads |
| record | [NullableClass.ObjectNullablePropBoxedMap](#objectnullablepropboxedmap)<br> boxed class to store validated Map payloads |
| static class | [NullableClass.ObjectNullableProp](#objectnullableprop)<br> schema class |
| static class | [NullableClass.ObjectNullablePropMapBuilder](#objectnullablepropmapbuilder)<br> builder for Map payloads |
| static class | [NullableClass.ObjectNullablePropMap](#objectnullablepropmap)<br> output class for Map payloads |
| sealed interface | [NullableClass.AdditionalPropertiesBoxed](#additionalpropertiesboxed)<br> sealed interface for validated payloads |
| record | [NullableClass.AdditionalPropertiesBoxedMap](#additionalpropertiesboxedmap)<br> boxed class to store validated Map payloads |
| static class | [NullableClass.AdditionalProperties](#additionalproperties)<br> schema class |
| sealed interface | [NullableClass.ArrayItemsNullableBoxed](#arrayitemsnullableboxed)<br> sealed interface for validated payloads |
| record | [NullableClass.ArrayItemsNullableBoxedList](#arrayitemsnullableboxedlist)<br> boxed class to store validated List payloads |
| static class | [NullableClass.ArrayItemsNullable](#arrayitemsnullable)<br> schema class |
| static class | [NullableClass.ArrayItemsNullableListBuilder](#arrayitemsnullablelistbuilder)<br> builder for List payloads |
| static class | [NullableClass.ArrayItemsNullableList](#arrayitemsnullablelist)<br> output class for List payloads |
| sealed interface | [NullableClass.Items2Boxed](#items2boxed)<br> sealed interface for validated payloads |
| record | [NullableClass.Items2BoxedVoid](#items2boxedvoid)<br> boxed class to store validated null payloads |
| record | [NullableClass.Items2BoxedMap](#items2boxedmap)<br> boxed class to store validated Map payloads |
| static class | [NullableClass.Items2](#items2)<br> schema class |
| sealed interface | [NullableClass.ArrayAndItemsNullablePropBoxed](#arrayanditemsnullablepropboxed)<br> sealed interface for validated payloads |
| record | [NullableClass.ArrayAndItemsNullablePropBoxedVoid](#arrayanditemsnullablepropboxedvoid)<br> boxed class to store validated null payloads |
| record | [NullableClass.ArrayAndItemsNullablePropBoxedList](#arrayanditemsnullablepropboxedlist)<br> boxed class to store validated List payloads |
| static class | [NullableClass.ArrayAndItemsNullableProp](#arrayanditemsnullableprop)<br> schema class |
| static class | [NullableClass.ArrayAndItemsNullablePropListBuilder](#arrayanditemsnullableproplistbuilder)<br> builder for List payloads |
| static class | [NullableClass.ArrayAndItemsNullablePropList](#arrayanditemsnullableproplist)<br> output class for List payloads |
| sealed interface | [NullableClass.Items1Boxed](#items1boxed)<br> sealed interface for validated payloads |
| record | [NullableClass.Items1BoxedVoid](#items1boxedvoid)<br> boxed class to store validated null payloads |
| record | [NullableClass.Items1BoxedMap](#items1boxedmap)<br> boxed class to store validated Map payloads |
| static class | [NullableClass.Items1](#items1)<br> schema class |
| sealed interface | [NullableClass.ArrayNullablePropBoxed](#arraynullablepropboxed)<br> sealed interface for validated payloads |
| record | [NullableClass.ArrayNullablePropBoxedVoid](#arraynullablepropboxedvoid)<br> boxed class to store validated null payloads |
| record | [NullableClass.ArrayNullablePropBoxedList](#arraynullablepropboxedlist)<br> boxed class to store validated List payloads |
| static class | [NullableClass.ArrayNullableProp](#arraynullableprop)<br> schema class |
| static class | [NullableClass.ArrayNullablePropListBuilder](#arraynullableproplistbuilder)<br> builder for List payloads |
| static class | [NullableClass.ArrayNullablePropList](#arraynullableproplist)<br> output class for List payloads |
| sealed interface | [NullableClass.ItemsBoxed](#itemsboxed)<br> sealed interface for validated payloads |
| record | [NullableClass.ItemsBoxedMap](#itemsboxedmap)<br> boxed class to store validated Map payloads |
| static class | [NullableClass.Items](#items)<br> schema class |
| sealed interface | [NullableClass.DatetimePropBoxed](#datetimepropboxed)<br> sealed interface for validated payloads |
| record | [NullableClass.DatetimePropBoxedVoid](#datetimepropboxedvoid)<br> boxed class to store validated null payloads |
| record | [NullableClass.DatetimePropBoxedString](#datetimepropboxedstring)<br> boxed class to store validated String payloads |
| static class | [NullableClass.DatetimeProp](#datetimeprop)<br> schema class |
| sealed interface | [NullableClass.DatePropBoxed](#datepropboxed)<br> sealed interface for validated payloads |
| record | [NullableClass.DatePropBoxedVoid](#datepropboxedvoid)<br> boxed class to store validated null payloads |
| record | [NullableClass.DatePropBoxedString](#datepropboxedstring)<br> boxed class to store validated String payloads |
| static class | [NullableClass.DateProp](#dateprop)<br> schema class |
| sealed interface | [NullableClass.StringPropBoxed](#stringpropboxed)<br> sealed interface for validated payloads |
| record | [NullableClass.StringPropBoxedVoid](#stringpropboxedvoid)<br> boxed class to store validated null payloads |
| record | [NullableClass.StringPropBoxedString](#stringpropboxedstring)<br> boxed class to store validated String payloads |
| static class | [NullableClass.StringProp](#stringprop)<br> schema class |
| sealed interface | [NullableClass.BooleanPropBoxed](#booleanpropboxed)<br> sealed interface for validated payloads |
| record | [NullableClass.BooleanPropBoxedVoid](#booleanpropboxedvoid)<br> boxed class to store validated null payloads |
| record | [NullableClass.BooleanPropBoxedBoolean](#booleanpropboxedboolean)<br> boxed class to store validated boolean payloads |
| static class | [NullableClass.BooleanProp](#booleanprop)<br> schema class |
| sealed interface | [NullableClass.NumberPropBoxed](#numberpropboxed)<br> sealed interface for validated payloads |
| record | [NullableClass.NumberPropBoxedVoid](#numberpropboxedvoid)<br> boxed class to store validated null payloads |
| record | [NullableClass.NumberPropBoxedNumber](#numberpropboxednumber)<br> boxed class to store validated Number payloads |
| static class | [NullableClass.NumberProp](#numberprop)<br> schema class |
| sealed interface | [NullableClass.IntegerPropBoxed](#integerpropboxed)<br> sealed interface for validated payloads |
| record | [NullableClass.IntegerPropBoxedVoid](#integerpropboxedvoid)<br> boxed class to store validated null payloads |
| record | [NullableClass.IntegerPropBoxedNumber](#integerpropboxednumber)<br> boxed class to store validated Number payloads |
| static class | [NullableClass.IntegerProp](#integerprop)<br> schema class |
| sealed interface | [NullableClass.AdditionalProperties3Boxed](#additionalproperties3boxed)<br> sealed interface for validated payloads |
| record | [NullableClass.AdditionalProperties3BoxedVoid](#additionalproperties3boxedvoid)<br> boxed class to store validated null payloads |
| record | [NullableClass.AdditionalProperties3BoxedMap](#additionalproperties3boxedmap)<br> boxed class to store validated Map payloads |
| static class | [NullableClass.AdditionalProperties3](#additionalproperties3)<br> schema class |

## NullableClass1Boxed
public sealed interface NullableClass1Boxed<br>
permits<br>
[NullableClass1BoxedMap](#nullableclass1boxedmap)

sealed interface that stores validated payloads using boxed classes

## NullableClass1BoxedMap
public record NullableClass1BoxedMap<br>
implements [NullableClass1Boxed](#nullableclass1boxed)

record that stores validated Map payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| NullableClass1BoxedMap([NullableClassMap](#nullableclassmap) data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| [NullableClassMap](#nullableclassmap) | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## NullableClass1
public static class NullableClass1<br>
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
import org.openapijsonschematools.client.components.schemas.NullableClass;

import java.util.Arrays;
import java.util.List;
import java.util.AbstractMap;

static final SchemaConfiguration configuration = new SchemaConfiguration(new JsonSchemaKeywordFlags.Builder().build());

// Map validation
NullableClass.NullableClassMap validatedPayload =
    NullableClass.NullableClass1.validate(
    new NullableClass.NullableClassMapBuilder()
        .integer_prop(null)

        .number_prop(null)

        .boolean_prop(null)

        .string_prop(null)

        .date_prop(null)

        .datetime_prop(null)

        .array_nullable_prop(null)

        .array_and_items_nullable_prop(null)

        .array_items_nullable(
            Arrays.asList(
                null
            )
        )
        .object_nullable_prop(null)

        .object_and_items_nullable_prop(null)

        .object_items_nullable(
            MapUtils.makeMap(
                new AbstractMap.SimpleEntry<String, Void>(
                    "someAdditionalProperty",
                    null
                )
            )
        )
        .additionalProperty("someAdditionalProperty", null)

    .build(),
    configuration
);
```

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Set<Class<?>> | type = Set.of(Map.class) |
| Map<String, Class<? extends JsonSchema>> | properties = Map.ofEntries(<br>&nbsp;&nbsp;&nbsp;&nbsp;new PropertyEntry("integer_prop", [IntegerProp.class](#integerprop))),<br>&nbsp;&nbsp;&nbsp;&nbsp;new PropertyEntry("number_prop", [NumberProp.class](#numberprop))),<br>&nbsp;&nbsp;&nbsp;&nbsp;new PropertyEntry("boolean_prop", [BooleanProp.class](#booleanprop))),<br>&nbsp;&nbsp;&nbsp;&nbsp;new PropertyEntry("string_prop", [StringProp.class](#stringprop))),<br>&nbsp;&nbsp;&nbsp;&nbsp;new PropertyEntry("date_prop", [DateProp.class](#dateprop))),<br>&nbsp;&nbsp;&nbsp;&nbsp;new PropertyEntry("datetime_prop", [DatetimeProp.class](#datetimeprop))),<br>&nbsp;&nbsp;&nbsp;&nbsp;new PropertyEntry("array_nullable_prop", [ArrayNullableProp.class](#arraynullableprop))),<br>&nbsp;&nbsp;&nbsp;&nbsp;new PropertyEntry("array_and_items_nullable_prop", [ArrayAndItemsNullableProp.class](#arrayanditemsnullableprop))),<br>&nbsp;&nbsp;&nbsp;&nbsp;new PropertyEntry("array_items_nullable", [ArrayItemsNullable.class](#arrayitemsnullable))),<br>&nbsp;&nbsp;&nbsp;&nbsp;new PropertyEntry("object_nullable_prop", [ObjectNullableProp.class](#objectnullableprop))),<br>&nbsp;&nbsp;&nbsp;&nbsp;new PropertyEntry("object_and_items_nullable_prop", [ObjectAndItemsNullableProp.class](#objectanditemsnullableprop))),<br>&nbsp;&nbsp;&nbsp;&nbsp;new PropertyEntry("object_items_nullable", [ObjectItemsNullable.class](#objectitemsnullable)))<br>)<br> |
| Class<? extends JsonSchema> | additionalProperties = [AdditionalProperties3.class](#additionalproperties3) |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| [NullableClassMap](#nullableclassmap) | validate([Map&lt;?, ?&gt;](#nullableclassmapbuilder) arg, SchemaConfiguration configuration) |
| [NullableClass1BoxedMap](#nullableclass1boxedmap) | validateAndBox([Map&lt;?, ?&gt;](#nullableclassmapbuilder) arg, SchemaConfiguration configuration) |
| [NullableClass1Boxed](#nullableclass1boxed) | validateAndBox(@Nullable Object arg, SchemaConfiguration configuration) |
| @Nullable Object | validate(@Nullable Object arg, SchemaConfiguration configuration) |

## NullableClassMapBuilder
public class NullableClassMapBuilder<br>
builder for `Map<String, @Nullable Object>`

A class that builds the Map input type

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| NullableClassMapBuilder()<br>Creates a builder that contains an empty map |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| Map<String, @Nullable Object> | build()<br>Returns map input that should be used with Schema.validate |
| [NullableClassMapBuilder](#nullableclassmapbuilder) | integer_prop(Void value) |
| [NullableClassMapBuilder](#nullableclassmapbuilder) | integer_prop(int value) |
| [NullableClassMapBuilder](#nullableclassmapbuilder) | integer_prop(float value) |
| [NullableClassMapBuilder](#nullableclassmapbuilder) | integer_prop(long value) |
| [NullableClassMapBuilder](#nullableclassmapbuilder) | integer_prop(double value) |
| [NullableClassMapBuilder](#nullableclassmapbuilder) | number_prop(Void value) |
| [NullableClassMapBuilder](#nullableclassmapbuilder) | number_prop(int value) |
| [NullableClassMapBuilder](#nullableclassmapbuilder) | number_prop(float value) |
| [NullableClassMapBuilder](#nullableclassmapbuilder) | number_prop(long value) |
| [NullableClassMapBuilder](#nullableclassmapbuilder) | number_prop(double value) |
| [NullableClassMapBuilder](#nullableclassmapbuilder) | boolean_prop(Void value) |
| [NullableClassMapBuilder](#nullableclassmapbuilder) | boolean_prop(boolean value) |
| [NullableClassMapBuilder](#nullableclassmapbuilder) | string_prop(Void value) |
| [NullableClassMapBuilder](#nullableclassmapbuilder) | string_prop(String value) |
| [NullableClassMapBuilder](#nullableclassmapbuilder) | date_prop(Void value) |
| [NullableClassMapBuilder](#nullableclassmapbuilder) | date_prop(String value) |
| [NullableClassMapBuilder](#nullableclassmapbuilder) | datetime_prop(Void value) |
| [NullableClassMapBuilder](#nullableclassmapbuilder) | datetime_prop(String value) |
| [NullableClassMapBuilder](#nullableclassmapbuilder) | array_nullable_prop(Void value) |
| [NullableClassMapBuilder](#nullableclassmapbuilder) | array_nullable_prop(List<Map<String, @Nullable Object>> value) |
| [NullableClassMapBuilder](#nullableclassmapbuilder) | array_and_items_nullable_prop(Void value) |
| [NullableClassMapBuilder](#nullableclassmapbuilder) | array_and_items_nullable_prop(List<@Nullable Map<String, @Nullable Object>> value) |
| [NullableClassMapBuilder](#nullableclassmapbuilder) | array_items_nullable(List<@Nullable Map<String, @Nullable Object>> value) |
| [NullableClassMapBuilder](#nullableclassmapbuilder) | object_nullable_prop(Void value) |
| [NullableClassMapBuilder](#nullableclassmapbuilder) | object_nullable_prop(Map<String, Map<String, @Nullable Object>> value) |
| [NullableClassMapBuilder](#nullableclassmapbuilder) | object_and_items_nullable_prop(Void value) |
| [NullableClassMapBuilder](#nullableclassmapbuilder) | object_and_items_nullable_prop(Map<String, @Nullable Map<String, @Nullable Object>> value) |
| [NullableClassMapBuilder](#nullableclassmapbuilder) | object_items_nullable(Map<String, @Nullable Map<String, @Nullable Object>> value) |
| [NullableClassMapBuilder](#nullableclassmapbuilder) | additionalProperty(String key, Void value) |
| [NullableClassMapBuilder](#nullableclassmapbuilder) | additionalProperty(String key, Map<String, @Nullable Object> value) |

## NullableClassMap
public static class NullableClassMap<br>
extends FrozenMap<String, @Nullable Object>

A class to store validated Map payloads

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| static [NullableClassMap](#nullableclassmap) | of([Map<String, ? extends @Nullable Object>](#nullableclassmapbuilder) arg, SchemaConfiguration configuration) |
| @Nullable Number | integer_prop()<br>[optional] |
| @Nullable Number | number_prop()<br>[optional] |
| @Nullable Boolean | boolean_prop()<br>[optional] |
| @Nullable String | string_prop()<br>[optional] |
| @Nullable String | date_prop()<br>[optional] value must conform to RFC-3339 full-date YYYY-MM-DD |
| @Nullable String | datetime_prop()<br>[optional] value must conform to RFC-3339 date-time |
| [ArrayNullablePropList](#arraynullableproplist) | array_nullable_prop()<br>[optional] |
| [ArrayAndItemsNullablePropList](#arrayanditemsnullableproplist) | array_and_items_nullable_prop()<br>[optional] |
| [ArrayItemsNullableList](#arrayitemsnullablelist) | array_items_nullable()<br>[optional] |
| [ObjectNullablePropMap](#objectnullablepropmap) | object_nullable_prop()<br>[optional] |
| [ObjectAndItemsNullablePropMap](#objectanditemsnullablepropmap) | object_and_items_nullable_prop()<br>[optional] |
| [ObjectItemsNullableMap](#objectitemsnullablemap) | object_items_nullable()<br>[optional] |
| @Nullable FrozenMap<?> | getAdditionalProperty(String name)<br>provides type safety for additional properties |

## ObjectItemsNullableBoxed
public sealed interface ObjectItemsNullableBoxed<br>
permits<br>
[ObjectItemsNullableBoxedMap](#objectitemsnullableboxedmap)

sealed interface that stores validated payloads using boxed classes

## ObjectItemsNullableBoxedMap
public record ObjectItemsNullableBoxedMap<br>
implements [ObjectItemsNullableBoxed](#objectitemsnullableboxed)

record that stores validated Map payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| ObjectItemsNullableBoxedMap([ObjectItemsNullableMap](#objectitemsnullablemap) data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| [ObjectItemsNullableMap](#objectitemsnullablemap) | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## ObjectItemsNullable
public static class ObjectItemsNullable<br>
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
import org.openapijsonschematools.client.components.schemas.NullableClass;

import java.util.Arrays;
import java.util.List;
import java.util.AbstractMap;

static final SchemaConfiguration configuration = new SchemaConfiguration(new JsonSchemaKeywordFlags.Builder().build());

// Map validation
NullableClass.ObjectItemsNullableMap validatedPayload =
    NullableClass.ObjectItemsNullable.validate(
    new NullableClass.ObjectItemsNullableMapBuilder()
        .additionalProperty("someAdditionalProperty", null)

    .build(),
    configuration
);
```

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Set<Class<?>> | type = Set.of(Map.class) |
| Class<? extends JsonSchema> | additionalProperties = [AdditionalProperties2.class](#additionalproperties2) |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| [ObjectItemsNullableMap](#objectitemsnullablemap) | validate([Map&lt;?, ?&gt;](#objectitemsnullablemapbuilder) arg, SchemaConfiguration configuration) |
| [ObjectItemsNullableBoxedMap](#objectitemsnullableboxedmap) | validateAndBox([Map&lt;?, ?&gt;](#objectitemsnullablemapbuilder) arg, SchemaConfiguration configuration) |
| [ObjectItemsNullableBoxed](#objectitemsnullableboxed) | validateAndBox(@Nullable Object arg, SchemaConfiguration configuration) |
| @Nullable Object | validate(@Nullable Object arg, SchemaConfiguration configuration) |

## ObjectItemsNullableMapBuilder
public class ObjectItemsNullableMapBuilder<br>
builder for `Map<String, @Nullable Map<String, @Nullable Object>>`

A class that builds the Map input type

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| ObjectItemsNullableMapBuilder()<br>Creates a builder that contains an empty map |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| Map<String, @Nullable Map<String, @Nullable Object>> | build()<br>Returns map input that should be used with Schema.validate |
| [ObjectItemsNullableMapBuilder](#objectitemsnullablemapbuilder) | additionalProperty(String key, Void value) |
| [ObjectItemsNullableMapBuilder](#objectitemsnullablemapbuilder) | additionalProperty(String key, Map<String, @Nullable Object> value) |

## ObjectItemsNullableMap
public static class ObjectItemsNullableMap<br>
extends FrozenMap<String, @Nullable FrozenMap<?>>

A class to store validated Map payloads

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| static [ObjectItemsNullableMap](#objectitemsnullablemap) | of([Map<String, ? extends @Nullable Map<String, ? extends @Nullable Object>>](#objectitemsnullablemapbuilder) arg, SchemaConfiguration configuration) |
| @Nullable FrozenMap<?> | getAdditionalProperty(String name)<br>provides type safety for additional properties |

## AdditionalProperties2Boxed
public sealed interface AdditionalProperties2Boxed<br>
permits<br>
[AdditionalProperties2BoxedVoid](#additionalproperties2boxedvoid),
[AdditionalProperties2BoxedMap](#additionalproperties2boxedmap)

sealed interface that stores validated payloads using boxed classes

## AdditionalProperties2BoxedVoid
public record AdditionalProperties2BoxedVoid<br>
implements [AdditionalProperties2Boxed](#additionalproperties2boxed)

record that stores validated null payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| AdditionalProperties2BoxedVoid(Void data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| Void | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## AdditionalProperties2BoxedMap
public record AdditionalProperties2BoxedMap<br>
implements [AdditionalProperties2Boxed](#additionalproperties2boxed)

record that stores validated Map payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| AdditionalProperties2BoxedMap(FrozenMap<@Nullable Object> data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| FrozenMap<@Nullable Object> | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## AdditionalProperties2
public static class AdditionalProperties2<br>
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
import org.openapijsonschematools.client.components.schemas.NullableClass;

import java.util.Arrays;
import java.util.List;
import java.util.AbstractMap;

static final SchemaConfiguration configuration = new SchemaConfiguration(new JsonSchemaKeywordFlags.Builder().build());

// null validation
Void validatedPayload = NullableClass.AdditionalProperties2.validate(
    (Void) null,
    configuration
);
```

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Set<Class<?>> | type = Set.of(<br/>&nbsp;&nbsp;&nbsp;&nbsp;Void.class,<br/>&nbsp;&nbsp;&nbsp;&nbsp;Map.class<br/>)<br/> |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| Void | validate(Void arg, SchemaConfiguration configuration) |
| [AdditionalProperties2BoxedVoid](#additionalproperties2boxedvoid) | validateAndBox(Void arg, SchemaConfiguration configuration) |
| FrozenMap<String, @Nullable Object> | validate(Map&lt;?, ?&gt; arg, SchemaConfiguration configuration) |
| [AdditionalProperties2BoxedMap](#additionalproperties2boxedmap) | validateAndBox(Map&lt;?, ?&gt; arg, SchemaConfiguration configuration) |
| [AdditionalProperties2Boxed](#additionalproperties2boxed) | validateAndBox(@Nullable Object arg, SchemaConfiguration configuration) |
| @Nullable Object | validate(@Nullable Object arg, SchemaConfiguration configuration) |

## ObjectAndItemsNullablePropBoxed
public sealed interface ObjectAndItemsNullablePropBoxed<br>
permits<br>
[ObjectAndItemsNullablePropBoxedVoid](#objectanditemsnullablepropboxedvoid),
[ObjectAndItemsNullablePropBoxedMap](#objectanditemsnullablepropboxedmap)

sealed interface that stores validated payloads using boxed classes

## ObjectAndItemsNullablePropBoxedVoid
public record ObjectAndItemsNullablePropBoxedVoid<br>
implements [ObjectAndItemsNullablePropBoxed](#objectanditemsnullablepropboxed)

record that stores validated null payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| ObjectAndItemsNullablePropBoxedVoid(Void data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| Void | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## ObjectAndItemsNullablePropBoxedMap
public record ObjectAndItemsNullablePropBoxedMap<br>
implements [ObjectAndItemsNullablePropBoxed](#objectanditemsnullablepropboxed)

record that stores validated Map payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| ObjectAndItemsNullablePropBoxedMap([ObjectAndItemsNullablePropMap](#objectanditemsnullablepropmap) data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| [ObjectAndItemsNullablePropMap](#objectanditemsnullablepropmap) | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## ObjectAndItemsNullableProp
public static class ObjectAndItemsNullableProp<br>
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
import org.openapijsonschematools.client.components.schemas.NullableClass;

import java.util.Arrays;
import java.util.List;
import java.util.AbstractMap;

static final SchemaConfiguration configuration = new SchemaConfiguration(new JsonSchemaKeywordFlags.Builder().build());

// null validation
Void validatedPayload = NullableClass.ObjectAndItemsNullableProp.validate(
    (Void) null,
    configuration
);

// Map validation
NullableClass.ObjectAndItemsNullablePropMap validatedPayload =
    NullableClass.ObjectAndItemsNullableProp.validate(
    new NullableClass.ObjectAndItemsNullablePropMapBuilder()
        .additionalProperty("someAdditionalProperty", null)

    .build(),
    configuration
);
```

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Set<Class<?>> | type = Set.of(<br/>&nbsp;&nbsp;&nbsp;&nbsp;Void.class,<br/>&nbsp;&nbsp;&nbsp;&nbsp;Map.class<br/>)<br/> |
| Class<? extends JsonSchema> | additionalProperties = [AdditionalProperties1.class](#additionalproperties1) |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| Void | validate(Void arg, SchemaConfiguration configuration) |
| [ObjectAndItemsNullablePropBoxedVoid](#objectanditemsnullablepropboxedvoid) | validateAndBox(Void arg, SchemaConfiguration configuration) |
| [ObjectAndItemsNullablePropMap](#objectanditemsnullablepropmap) | validate([Map&lt;?, ?&gt;](#objectanditemsnullablepropmapbuilder) arg, SchemaConfiguration configuration) |
| [ObjectAndItemsNullablePropBoxedMap](#objectanditemsnullablepropboxedmap) | validateAndBox([Map&lt;?, ?&gt;](#objectanditemsnullablepropmapbuilder) arg, SchemaConfiguration configuration) |
| [ObjectAndItemsNullablePropBoxed](#objectanditemsnullablepropboxed) | validateAndBox(@Nullable Object arg, SchemaConfiguration configuration) |
| @Nullable Object | validate(@Nullable Object arg, SchemaConfiguration configuration) |

## ObjectAndItemsNullablePropMapBuilder
public class ObjectAndItemsNullablePropMapBuilder<br>
builder for `Map<String, @Nullable Map<String, @Nullable Object>>`

A class that builds the Map input type

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| ObjectAndItemsNullablePropMapBuilder()<br>Creates a builder that contains an empty map |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| Map<String, @Nullable Map<String, @Nullable Object>> | build()<br>Returns map input that should be used with Schema.validate |
| [ObjectAndItemsNullablePropMapBuilder](#objectanditemsnullablepropmapbuilder) | additionalProperty(String key, Void value) |
| [ObjectAndItemsNullablePropMapBuilder](#objectanditemsnullablepropmapbuilder) | additionalProperty(String key, Map<String, @Nullable Object> value) |

## ObjectAndItemsNullablePropMap
public static class ObjectAndItemsNullablePropMap<br>
extends FrozenMap<String, @Nullable FrozenMap<?>>

A class to store validated Map payloads

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| static [ObjectAndItemsNullablePropMap](#objectanditemsnullablepropmap) | of([Map<String, ? extends @Nullable Map<String, ? extends @Nullable Object>>](#objectanditemsnullablepropmapbuilder) arg, SchemaConfiguration configuration) |
| @Nullable FrozenMap<?> | getAdditionalProperty(String name)<br>provides type safety for additional properties |

## AdditionalProperties1Boxed
public sealed interface AdditionalProperties1Boxed<br>
permits<br>
[AdditionalProperties1BoxedVoid](#additionalproperties1boxedvoid),
[AdditionalProperties1BoxedMap](#additionalproperties1boxedmap)

sealed interface that stores validated payloads using boxed classes

## AdditionalProperties1BoxedVoid
public record AdditionalProperties1BoxedVoid<br>
implements [AdditionalProperties1Boxed](#additionalproperties1boxed)

record that stores validated null payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| AdditionalProperties1BoxedVoid(Void data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| Void | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## AdditionalProperties1BoxedMap
public record AdditionalProperties1BoxedMap<br>
implements [AdditionalProperties1Boxed](#additionalproperties1boxed)

record that stores validated Map payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| AdditionalProperties1BoxedMap(FrozenMap<@Nullable Object> data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| FrozenMap<@Nullable Object> | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## AdditionalProperties1
public static class AdditionalProperties1<br>
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
import org.openapijsonschematools.client.components.schemas.NullableClass;

import java.util.Arrays;
import java.util.List;
import java.util.AbstractMap;

static final SchemaConfiguration configuration = new SchemaConfiguration(new JsonSchemaKeywordFlags.Builder().build());

// null validation
Void validatedPayload = NullableClass.AdditionalProperties1.validate(
    (Void) null,
    configuration
);
```

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Set<Class<?>> | type = Set.of(<br/>&nbsp;&nbsp;&nbsp;&nbsp;Void.class,<br/>&nbsp;&nbsp;&nbsp;&nbsp;Map.class<br/>)<br/> |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| Void | validate(Void arg, SchemaConfiguration configuration) |
| [AdditionalProperties1BoxedVoid](#additionalproperties1boxedvoid) | validateAndBox(Void arg, SchemaConfiguration configuration) |
| FrozenMap<String, @Nullable Object> | validate(Map&lt;?, ?&gt; arg, SchemaConfiguration configuration) |
| [AdditionalProperties1BoxedMap](#additionalproperties1boxedmap) | validateAndBox(Map&lt;?, ?&gt; arg, SchemaConfiguration configuration) |
| [AdditionalProperties1Boxed](#additionalproperties1boxed) | validateAndBox(@Nullable Object arg, SchemaConfiguration configuration) |
| @Nullable Object | validate(@Nullable Object arg, SchemaConfiguration configuration) |

## ObjectNullablePropBoxed
public sealed interface ObjectNullablePropBoxed<br>
permits<br>
[ObjectNullablePropBoxedVoid](#objectnullablepropboxedvoid),
[ObjectNullablePropBoxedMap](#objectnullablepropboxedmap)

sealed interface that stores validated payloads using boxed classes

## ObjectNullablePropBoxedVoid
public record ObjectNullablePropBoxedVoid<br>
implements [ObjectNullablePropBoxed](#objectnullablepropboxed)

record that stores validated null payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| ObjectNullablePropBoxedVoid(Void data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| Void | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## ObjectNullablePropBoxedMap
public record ObjectNullablePropBoxedMap<br>
implements [ObjectNullablePropBoxed](#objectnullablepropboxed)

record that stores validated Map payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| ObjectNullablePropBoxedMap([ObjectNullablePropMap](#objectnullablepropmap) data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| [ObjectNullablePropMap](#objectnullablepropmap) | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## ObjectNullableProp
public static class ObjectNullableProp<br>
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
import org.openapijsonschematools.client.components.schemas.NullableClass;

import java.util.Arrays;
import java.util.List;
import java.util.AbstractMap;

static final SchemaConfiguration configuration = new SchemaConfiguration(new JsonSchemaKeywordFlags.Builder().build());

// null validation
Void validatedPayload = NullableClass.ObjectNullableProp.validate(
    (Void) null,
    configuration
);

// Map validation
NullableClass.ObjectNullablePropMap validatedPayload =
    NullableClass.ObjectNullableProp.validate(
    new NullableClass.ObjectNullablePropMapBuilder()
    .build(),
    configuration
);
```

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Set<Class<?>> | type = Set.of(<br/>&nbsp;&nbsp;&nbsp;&nbsp;Void.class,<br/>&nbsp;&nbsp;&nbsp;&nbsp;Map.class<br/>)<br/> |
| Class<? extends JsonSchema> | additionalProperties = [AdditionalProperties.class](#additionalproperties) |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| Void | validate(Void arg, SchemaConfiguration configuration) |
| [ObjectNullablePropBoxedVoid](#objectnullablepropboxedvoid) | validateAndBox(Void arg, SchemaConfiguration configuration) |
| [ObjectNullablePropMap](#objectnullablepropmap) | validate([Map&lt;?, ?&gt;](#objectnullablepropmapbuilder) arg, SchemaConfiguration configuration) |
| [ObjectNullablePropBoxedMap](#objectnullablepropboxedmap) | validateAndBox([Map&lt;?, ?&gt;](#objectnullablepropmapbuilder) arg, SchemaConfiguration configuration) |
| [ObjectNullablePropBoxed](#objectnullablepropboxed) | validateAndBox(@Nullable Object arg, SchemaConfiguration configuration) |
| @Nullable Object | validate(@Nullable Object arg, SchemaConfiguration configuration) |

## ObjectNullablePropMapBuilder
public class ObjectNullablePropMapBuilder<br>
builder for `Map<String, Map<String, @Nullable Object>>`

A class that builds the Map input type

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| ObjectNullablePropMapBuilder()<br>Creates a builder that contains an empty map |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| Map<String, Map<String, @Nullable Object>> | build()<br>Returns map input that should be used with Schema.validate |
| [ObjectNullablePropMapBuilder](#objectnullablepropmapbuilder) | additionalProperty(String key, Map<String, @Nullable Object> value) |

## ObjectNullablePropMap
public static class ObjectNullablePropMap<br>
extends FrozenMap<String, FrozenMap<?>>

A class to store validated Map payloads

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| static [ObjectNullablePropMap](#objectnullablepropmap) | of([Map<String, Map<String, ? extends @Nullable Object>>](#objectnullablepropmapbuilder) arg, SchemaConfiguration configuration) |
| FrozenMap<?> | getAdditionalProperty(String name)<br>provides type safety for additional properties |

## AdditionalPropertiesBoxed
public sealed interface AdditionalPropertiesBoxed<br>
permits<br>
[AdditionalPropertiesBoxedMap](#additionalpropertiesboxedmap)

sealed interface that stores validated payloads using boxed classes

## AdditionalPropertiesBoxedMap
public record AdditionalPropertiesBoxedMap<br>
implements [AdditionalPropertiesBoxed](#additionalpropertiesboxed)

record that stores validated Map payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| AdditionalPropertiesBoxedMap(FrozenMap<@Nullable Object> data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| FrozenMap<@Nullable Object> | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## AdditionalProperties
public static class AdditionalProperties<br>
extends MapJsonSchema.MapJsonSchema1

A schema class that validates payloads

| Methods Inherited from class org.openapijsonschematools.client.schemas.MapJsonSchema.MapJsonSchema1 |
| ------------------------------------------------------------------ |
| validate                                                           |
| validateAndBox                                                     |

## ArrayItemsNullableBoxed
public sealed interface ArrayItemsNullableBoxed<br>
permits<br>
[ArrayItemsNullableBoxedList](#arrayitemsnullableboxedlist)

sealed interface that stores validated payloads using boxed classes

## ArrayItemsNullableBoxedList
public record ArrayItemsNullableBoxedList<br>
implements [ArrayItemsNullableBoxed](#arrayitemsnullableboxed)

record that stores validated List payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| ArrayItemsNullableBoxedList([ArrayItemsNullableList](#arrayitemsnullablelist) data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| [ArrayItemsNullableList](#arrayitemsnullablelist) | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## ArrayItemsNullable
public static class ArrayItemsNullable<br>
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
import org.openapijsonschematools.client.components.schemas.NullableClass;

import java.util.Arrays;
import java.util.List;
import java.util.AbstractMap;

static final SchemaConfiguration configuration = new SchemaConfiguration(new JsonSchemaKeywordFlags.Builder().build());

// List validation
NullableClass.ArrayItemsNullableList validatedPayload =
    NullableClass.ArrayItemsNullable.validate(
    new NullableClass.ArrayItemsNullableListBuilder()
        .add((Void) null)

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
| [ArrayItemsNullableList](#arrayitemsnullablelist) | validate([List<?>](#arrayitemsnullablelistbuilder) arg, SchemaConfiguration configuration) |
| [ArrayItemsNullableBoxedList](#arrayitemsnullableboxedlist) | validateAndBox([List<?>](#arrayitemsnullablelistbuilder) arg, SchemaConfiguration configuration) |
| [ArrayItemsNullableBoxed](#arrayitemsnullableboxed) | validateAndBox(@Nullable Object arg, SchemaConfiguration configuration) |
| @Nullable Object | validate(@Nullable Object arg, SchemaConfiguration configuration) |

## ArrayItemsNullableListBuilder
public class ArrayItemsNullableListBuilder<br>
builder for `List<@Nullable Map<String, @Nullable Object>>`

A class that builds the List input type

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| ArrayItemsNullableListBuilder()<br>Creates an empty list |
| ArrayItemsNullableListBuilder(List<@Nullable Map<String, @Nullable Object>> items)<br>Stores the items in a list |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| ArrayItemsNullableListBuilder | add(Void item) |
| ArrayItemsNullableListBuilder | add(Map<String, @Nullable Object> item) |
| List<@Nullable Map<String, @Nullable Object>> | build()<br>Returns list input that should be used with Schema.validate |

## ArrayItemsNullableList
public class ArrayItemsNullableList<br>
extends `FrozenList<@Nullable FrozenMap<?>>`

A class to store validated List payloads

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| static [ArrayItemsNullableList](#arrayitemsnullablelist) | of([List<? extends @Nullable Map<String, ? extends @Nullable Object>>](#arrayitemsnullablelistbuilder) arg, SchemaConfiguration configuration) |

## Items2Boxed
public sealed interface Items2Boxed<br>
permits<br>
[Items2BoxedVoid](#items2boxedvoid),
[Items2BoxedMap](#items2boxedmap)

sealed interface that stores validated payloads using boxed classes

## Items2BoxedVoid
public record Items2BoxedVoid<br>
implements [Items2Boxed](#items2boxed)

record that stores validated null payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| Items2BoxedVoid(Void data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| Void | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## Items2BoxedMap
public record Items2BoxedMap<br>
implements [Items2Boxed](#items2boxed)

record that stores validated Map payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| Items2BoxedMap(FrozenMap<@Nullable Object> data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| FrozenMap<@Nullable Object> | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## Items2
public static class Items2<br>
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
import org.openapijsonschematools.client.components.schemas.NullableClass;

import java.util.Arrays;
import java.util.List;
import java.util.AbstractMap;

static final SchemaConfiguration configuration = new SchemaConfiguration(new JsonSchemaKeywordFlags.Builder().build());

// null validation
Void validatedPayload = NullableClass.Items2.validate(
    (Void) null,
    configuration
);
```

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Set<Class<?>> | type = Set.of(<br/>&nbsp;&nbsp;&nbsp;&nbsp;Void.class,<br/>&nbsp;&nbsp;&nbsp;&nbsp;Map.class<br/>)<br/> |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| Void | validate(Void arg, SchemaConfiguration configuration) |
| [Items2BoxedVoid](#items2boxedvoid) | validateAndBox(Void arg, SchemaConfiguration configuration) |
| FrozenMap<String, @Nullable Object> | validate(Map&lt;?, ?&gt; arg, SchemaConfiguration configuration) |
| [Items2BoxedMap](#items2boxedmap) | validateAndBox(Map&lt;?, ?&gt; arg, SchemaConfiguration configuration) |
| [Items2Boxed](#items2boxed) | validateAndBox(@Nullable Object arg, SchemaConfiguration configuration) |
| @Nullable Object | validate(@Nullable Object arg, SchemaConfiguration configuration) |

## ArrayAndItemsNullablePropBoxed
public sealed interface ArrayAndItemsNullablePropBoxed<br>
permits<br>
[ArrayAndItemsNullablePropBoxedVoid](#arrayanditemsnullablepropboxedvoid),
[ArrayAndItemsNullablePropBoxedList](#arrayanditemsnullablepropboxedlist)

sealed interface that stores validated payloads using boxed classes

## ArrayAndItemsNullablePropBoxedVoid
public record ArrayAndItemsNullablePropBoxedVoid<br>
implements [ArrayAndItemsNullablePropBoxed](#arrayanditemsnullablepropboxed)

record that stores validated null payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| ArrayAndItemsNullablePropBoxedVoid(Void data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| Void | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## ArrayAndItemsNullablePropBoxedList
public record ArrayAndItemsNullablePropBoxedList<br>
implements [ArrayAndItemsNullablePropBoxed](#arrayanditemsnullablepropboxed)

record that stores validated List payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| ArrayAndItemsNullablePropBoxedList([ArrayAndItemsNullablePropList](#arrayanditemsnullableproplist) data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| [ArrayAndItemsNullablePropList](#arrayanditemsnullableproplist) | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## ArrayAndItemsNullableProp
public static class ArrayAndItemsNullableProp<br>
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
import org.openapijsonschematools.client.components.schemas.NullableClass;

import java.util.Arrays;
import java.util.List;
import java.util.AbstractMap;

static final SchemaConfiguration configuration = new SchemaConfiguration(new JsonSchemaKeywordFlags.Builder().build());

// null validation
Void validatedPayload = NullableClass.ArrayAndItemsNullableProp.validate(
    (Void) null,
    configuration
);

// List validation
NullableClass.ArrayAndItemsNullablePropList validatedPayload =
    NullableClass.ArrayAndItemsNullableProp.validate(
    new NullableClass.ArrayAndItemsNullablePropListBuilder()
        .add((Void) null)

    .build(),
    configuration
);
```

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Set<Class<?>> | type = Set.of(<br/>&nbsp;&nbsp;&nbsp;&nbsp;Void.class,<br/>&nbsp;&nbsp;&nbsp;&nbsp;List.class<br/>)<br/> |
| Class<? extends JsonSchema> | items = [Items1.class](#items1) |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| Void | validate(Void arg, SchemaConfiguration configuration) |
| [ArrayAndItemsNullablePropBoxedVoid](#arrayanditemsnullablepropboxedvoid) | validateAndBox(Void arg, SchemaConfiguration configuration) |
| [ArrayAndItemsNullablePropList](#arrayanditemsnullableproplist) | validate([List<?>](#arrayanditemsnullableproplistbuilder) arg, SchemaConfiguration configuration) |
| [ArrayAndItemsNullablePropBoxedList](#arrayanditemsnullablepropboxedlist) | validateAndBox([List<?>](#arrayanditemsnullableproplistbuilder) arg, SchemaConfiguration configuration) |
| [ArrayAndItemsNullablePropBoxed](#arrayanditemsnullablepropboxed) | validateAndBox(@Nullable Object arg, SchemaConfiguration configuration) |
| @Nullable Object | validate(@Nullable Object arg, SchemaConfiguration configuration) |

## ArrayAndItemsNullablePropListBuilder
public class ArrayAndItemsNullablePropListBuilder<br>
builder for `List<@Nullable Map<String, @Nullable Object>>`

A class that builds the List input type

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| ArrayAndItemsNullablePropListBuilder()<br>Creates an empty list |
| ArrayAndItemsNullablePropListBuilder(List<@Nullable Map<String, @Nullable Object>> items)<br>Stores the items in a list |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| ArrayAndItemsNullablePropListBuilder | add(Void item) |
| ArrayAndItemsNullablePropListBuilder | add(Map<String, @Nullable Object> item) |
| List<@Nullable Map<String, @Nullable Object>> | build()<br>Returns list input that should be used with Schema.validate |

## ArrayAndItemsNullablePropList
public class ArrayAndItemsNullablePropList<br>
extends `FrozenList<@Nullable FrozenMap<?>>`

A class to store validated List payloads

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| static [ArrayAndItemsNullablePropList](#arrayanditemsnullableproplist) | of([List<? extends @Nullable Map<String, ? extends @Nullable Object>>](#arrayanditemsnullableproplistbuilder) arg, SchemaConfiguration configuration) |

## Items1Boxed
public sealed interface Items1Boxed<br>
permits<br>
[Items1BoxedVoid](#items1boxedvoid),
[Items1BoxedMap](#items1boxedmap)

sealed interface that stores validated payloads using boxed classes

## Items1BoxedVoid
public record Items1BoxedVoid<br>
implements [Items1Boxed](#items1boxed)

record that stores validated null payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| Items1BoxedVoid(Void data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| Void | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## Items1BoxedMap
public record Items1BoxedMap<br>
implements [Items1Boxed](#items1boxed)

record that stores validated Map payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| Items1BoxedMap(FrozenMap<@Nullable Object> data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| FrozenMap<@Nullable Object> | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## Items1
public static class Items1<br>
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
import org.openapijsonschematools.client.components.schemas.NullableClass;

import java.util.Arrays;
import java.util.List;
import java.util.AbstractMap;

static final SchemaConfiguration configuration = new SchemaConfiguration(new JsonSchemaKeywordFlags.Builder().build());

// null validation
Void validatedPayload = NullableClass.Items1.validate(
    (Void) null,
    configuration
);
```

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Set<Class<?>> | type = Set.of(<br/>&nbsp;&nbsp;&nbsp;&nbsp;Void.class,<br/>&nbsp;&nbsp;&nbsp;&nbsp;Map.class<br/>)<br/> |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| Void | validate(Void arg, SchemaConfiguration configuration) |
| [Items1BoxedVoid](#items1boxedvoid) | validateAndBox(Void arg, SchemaConfiguration configuration) |
| FrozenMap<String, @Nullable Object> | validate(Map&lt;?, ?&gt; arg, SchemaConfiguration configuration) |
| [Items1BoxedMap](#items1boxedmap) | validateAndBox(Map&lt;?, ?&gt; arg, SchemaConfiguration configuration) |
| [Items1Boxed](#items1boxed) | validateAndBox(@Nullable Object arg, SchemaConfiguration configuration) |
| @Nullable Object | validate(@Nullable Object arg, SchemaConfiguration configuration) |

## ArrayNullablePropBoxed
public sealed interface ArrayNullablePropBoxed<br>
permits<br>
[ArrayNullablePropBoxedVoid](#arraynullablepropboxedvoid),
[ArrayNullablePropBoxedList](#arraynullablepropboxedlist)

sealed interface that stores validated payloads using boxed classes

## ArrayNullablePropBoxedVoid
public record ArrayNullablePropBoxedVoid<br>
implements [ArrayNullablePropBoxed](#arraynullablepropboxed)

record that stores validated null payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| ArrayNullablePropBoxedVoid(Void data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| Void | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## ArrayNullablePropBoxedList
public record ArrayNullablePropBoxedList<br>
implements [ArrayNullablePropBoxed](#arraynullablepropboxed)

record that stores validated List payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| ArrayNullablePropBoxedList([ArrayNullablePropList](#arraynullableproplist) data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| [ArrayNullablePropList](#arraynullableproplist) | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## ArrayNullableProp
public static class ArrayNullableProp<br>
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
import org.openapijsonschematools.client.components.schemas.NullableClass;

import java.util.Arrays;
import java.util.List;
import java.util.AbstractMap;

static final SchemaConfiguration configuration = new SchemaConfiguration(new JsonSchemaKeywordFlags.Builder().build());

// null validation
Void validatedPayload = NullableClass.ArrayNullableProp.validate(
    (Void) null,
    configuration
);

// List validation
NullableClass.ArrayNullablePropList validatedPayload =
    NullableClass.ArrayNullableProp.validate(
    new NullableClass.ArrayNullablePropListBuilder()
    .build(),
    configuration
);
```

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Set<Class<?>> | type = Set.of(<br/>&nbsp;&nbsp;&nbsp;&nbsp;Void.class,<br/>&nbsp;&nbsp;&nbsp;&nbsp;List.class<br/>)<br/> |
| Class<? extends JsonSchema> | items = [Items.class](#items) |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| Void | validate(Void arg, SchemaConfiguration configuration) |
| [ArrayNullablePropBoxedVoid](#arraynullablepropboxedvoid) | validateAndBox(Void arg, SchemaConfiguration configuration) |
| [ArrayNullablePropList](#arraynullableproplist) | validate([List<?>](#arraynullableproplistbuilder) arg, SchemaConfiguration configuration) |
| [ArrayNullablePropBoxedList](#arraynullablepropboxedlist) | validateAndBox([List<?>](#arraynullableproplistbuilder) arg, SchemaConfiguration configuration) |
| [ArrayNullablePropBoxed](#arraynullablepropboxed) | validateAndBox(@Nullable Object arg, SchemaConfiguration configuration) |
| @Nullable Object | validate(@Nullable Object arg, SchemaConfiguration configuration) |

## ArrayNullablePropListBuilder
public class ArrayNullablePropListBuilder<br>
builder for `List<Map<String, @Nullable Object>>`

A class that builds the List input type

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| ArrayNullablePropListBuilder()<br>Creates an empty list |
| ArrayNullablePropListBuilder(List<Map<String, @Nullable Object>> items)<br>Stores the items in a list |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| ArrayNullablePropListBuilder | add(Map<String, @Nullable Object> item) |
| List<Map<String, @Nullable Object>> | build()<br>Returns list input that should be used with Schema.validate |

## ArrayNullablePropList
public class ArrayNullablePropList<br>
extends `FrozenList<FrozenMap<?>>`

A class to store validated List payloads

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| static [ArrayNullablePropList](#arraynullableproplist) | of([List<Map<String, ? extends @Nullable Object>>](#arraynullableproplistbuilder) arg, SchemaConfiguration configuration) |

## ItemsBoxed
public sealed interface ItemsBoxed<br>
permits<br>
[ItemsBoxedMap](#itemsboxedmap)

sealed interface that stores validated payloads using boxed classes

## ItemsBoxedMap
public record ItemsBoxedMap<br>
implements [ItemsBoxed](#itemsboxed)

record that stores validated Map payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| ItemsBoxedMap(FrozenMap<@Nullable Object> data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| FrozenMap<@Nullable Object> | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## Items
public static class Items<br>
extends MapJsonSchema.MapJsonSchema1

A schema class that validates payloads

| Methods Inherited from class org.openapijsonschematools.client.schemas.MapJsonSchema.MapJsonSchema1 |
| ------------------------------------------------------------------ |
| validate                                                           |
| validateAndBox                                                     |

## DatetimePropBoxed
public sealed interface DatetimePropBoxed<br>
permits<br>
[DatetimePropBoxedVoid](#datetimepropboxedvoid),
[DatetimePropBoxedString](#datetimepropboxedstring)

sealed interface that stores validated payloads using boxed classes

## DatetimePropBoxedVoid
public record DatetimePropBoxedVoid<br>
implements [DatetimePropBoxed](#datetimepropboxed)

record that stores validated null payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| DatetimePropBoxedVoid(Void data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| Void | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## DatetimePropBoxedString
public record DatetimePropBoxedString<br>
implements [DatetimePropBoxed](#datetimepropboxed)

record that stores validated String payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| DatetimePropBoxedString(String data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| String | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## DatetimeProp
public static class DatetimeProp<br>
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
import org.openapijsonschematools.client.components.schemas.NullableClass;

import java.util.Arrays;
import java.util.List;
import java.util.AbstractMap;

static final SchemaConfiguration configuration = new SchemaConfiguration(new JsonSchemaKeywordFlags.Builder().build());

// null validation
Void validatedPayload = NullableClass.DatetimeProp.validate(
    (Void) null,
    configuration
);

// String validation
String validatedPayload = NullableClass.DatetimeProp.validate(
    "1970-01-01T00:00:00.00Z",
    configuration
);
```

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Set<Class<?>> | type = Set.of(<br/>&nbsp;&nbsp;&nbsp;&nbsp;Void.class,<br/>&nbsp;&nbsp;&nbsp;&nbsp;String.class<br/>)<br/> |
| String | type = "date-time"; |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| Void | validate(Void arg, SchemaConfiguration configuration) |
| [DatetimePropBoxedVoid](#datetimepropboxedvoid) | validateAndBox(Void arg, SchemaConfiguration configuration) |
| String | validate(String arg, SchemaConfiguration configuration) |
| [DatetimePropBoxedString](#datetimepropboxedstring) | validateAndBox(String arg, SchemaConfiguration configuration) |
| [DatetimePropBoxed](#datetimepropboxed) | validateAndBox(@Nullable Object arg, SchemaConfiguration configuration) |
| @Nullable Object | validate(@Nullable Object arg, SchemaConfiguration configuration) |

## DatePropBoxed
public sealed interface DatePropBoxed<br>
permits<br>
[DatePropBoxedVoid](#datepropboxedvoid),
[DatePropBoxedString](#datepropboxedstring)

sealed interface that stores validated payloads using boxed classes

## DatePropBoxedVoid
public record DatePropBoxedVoid<br>
implements [DatePropBoxed](#datepropboxed)

record that stores validated null payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| DatePropBoxedVoid(Void data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| Void | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## DatePropBoxedString
public record DatePropBoxedString<br>
implements [DatePropBoxed](#datepropboxed)

record that stores validated String payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| DatePropBoxedString(String data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| String | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## DateProp
public static class DateProp<br>
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
import org.openapijsonschematools.client.components.schemas.NullableClass;

import java.util.Arrays;
import java.util.List;
import java.util.AbstractMap;

static final SchemaConfiguration configuration = new SchemaConfiguration(new JsonSchemaKeywordFlags.Builder().build());

// null validation
Void validatedPayload = NullableClass.DateProp.validate(
    (Void) null,
    configuration
);

// String validation
String validatedPayload = NullableClass.DateProp.validate(
    "2020-12-13",
    configuration
);
```

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Set<Class<?>> | type = Set.of(<br/>&nbsp;&nbsp;&nbsp;&nbsp;Void.class,<br/>&nbsp;&nbsp;&nbsp;&nbsp;String.class<br/>)<br/> |
| String | type = "date"; |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| Void | validate(Void arg, SchemaConfiguration configuration) |
| [DatePropBoxedVoid](#datepropboxedvoid) | validateAndBox(Void arg, SchemaConfiguration configuration) |
| String | validate(String arg, SchemaConfiguration configuration) |
| [DatePropBoxedString](#datepropboxedstring) | validateAndBox(String arg, SchemaConfiguration configuration) |
| [DatePropBoxed](#datepropboxed) | validateAndBox(@Nullable Object arg, SchemaConfiguration configuration) |
| @Nullable Object | validate(@Nullable Object arg, SchemaConfiguration configuration) |

## StringPropBoxed
public sealed interface StringPropBoxed<br>
permits<br>
[StringPropBoxedVoid](#stringpropboxedvoid),
[StringPropBoxedString](#stringpropboxedstring)

sealed interface that stores validated payloads using boxed classes

## StringPropBoxedVoid
public record StringPropBoxedVoid<br>
implements [StringPropBoxed](#stringpropboxed)

record that stores validated null payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| StringPropBoxedVoid(Void data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| Void | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## StringPropBoxedString
public record StringPropBoxedString<br>
implements [StringPropBoxed](#stringpropboxed)

record that stores validated String payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| StringPropBoxedString(String data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| String | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## StringProp
public static class StringProp<br>
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
import org.openapijsonschematools.client.components.schemas.NullableClass;

import java.util.Arrays;
import java.util.List;
import java.util.AbstractMap;

static final SchemaConfiguration configuration = new SchemaConfiguration(new JsonSchemaKeywordFlags.Builder().build());

// null validation
Void validatedPayload = NullableClass.StringProp.validate(
    (Void) null,
    configuration
);

// String validation
String validatedPayload = NullableClass.StringProp.validate(
    "a",
    configuration
);
```

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Set<Class<?>> | type = Set.of(<br/>&nbsp;&nbsp;&nbsp;&nbsp;Void.class,<br/>&nbsp;&nbsp;&nbsp;&nbsp;String.class<br/>)<br/> |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| Void | validate(Void arg, SchemaConfiguration configuration) |
| [StringPropBoxedVoid](#stringpropboxedvoid) | validateAndBox(Void arg, SchemaConfiguration configuration) |
| String | validate(String arg, SchemaConfiguration configuration) |
| [StringPropBoxedString](#stringpropboxedstring) | validateAndBox(String arg, SchemaConfiguration configuration) |
| [StringPropBoxed](#stringpropboxed) | validateAndBox(@Nullable Object arg, SchemaConfiguration configuration) |
| @Nullable Object | validate(@Nullable Object arg, SchemaConfiguration configuration) |

## BooleanPropBoxed
public sealed interface BooleanPropBoxed<br>
permits<br>
[BooleanPropBoxedVoid](#booleanpropboxedvoid),
[BooleanPropBoxedBoolean](#booleanpropboxedboolean)

sealed interface that stores validated payloads using boxed classes

## BooleanPropBoxedVoid
public record BooleanPropBoxedVoid<br>
implements [BooleanPropBoxed](#booleanpropboxed)

record that stores validated null payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| BooleanPropBoxedVoid(Void data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| Void | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## BooleanPropBoxedBoolean
public record BooleanPropBoxedBoolean<br>
implements [BooleanPropBoxed](#booleanpropboxed)

record that stores validated boolean payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| BooleanPropBoxedBoolean(boolean data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| boolean | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## BooleanProp
public static class BooleanProp<br>
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
import org.openapijsonschematools.client.components.schemas.NullableClass;

import java.util.Arrays;
import java.util.List;
import java.util.AbstractMap;

static final SchemaConfiguration configuration = new SchemaConfiguration(new JsonSchemaKeywordFlags.Builder().build());

// null validation
Void validatedPayload = NullableClass.BooleanProp.validate(
    (Void) null,
    configuration
);

// boolean validation
boolean validatedPayload = NullableClass.BooleanProp.validate(
    true,
    configuration
);
```

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Set<Class<?>> | type = Set.of(<br/>&nbsp;&nbsp;&nbsp;&nbsp;Void.class,<br/>&nbsp;&nbsp;&nbsp;&nbsp;Boolean.class<br/>)<br/> |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| Void | validate(Void arg, SchemaConfiguration configuration) |
| [BooleanPropBoxedVoid](#booleanpropboxedvoid) | validateAndBox(Void arg, SchemaConfiguration configuration) |
| boolean | validate(boolean arg, SchemaConfiguration configuration) |
| [BooleanPropBoxedBoolean](#booleanpropboxedboolean) | validateAndBox(boolean arg, SchemaConfiguration configuration) |
| [BooleanPropBoxed](#booleanpropboxed) | validateAndBox(@Nullable Object arg, SchemaConfiguration configuration) |
| @Nullable Object | validate(@Nullable Object arg, SchemaConfiguration configuration) |

## NumberPropBoxed
public sealed interface NumberPropBoxed<br>
permits<br>
[NumberPropBoxedVoid](#numberpropboxedvoid),
[NumberPropBoxedNumber](#numberpropboxednumber)

sealed interface that stores validated payloads using boxed classes

## NumberPropBoxedVoid
public record NumberPropBoxedVoid<br>
implements [NumberPropBoxed](#numberpropboxed)

record that stores validated null payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| NumberPropBoxedVoid(Void data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| Void | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## NumberPropBoxedNumber
public record NumberPropBoxedNumber<br>
implements [NumberPropBoxed](#numberpropboxed)

record that stores validated Number payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| NumberPropBoxedNumber(Number data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| Number | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## NumberProp
public static class NumberProp<br>
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
import org.openapijsonschematools.client.components.schemas.NullableClass;

import java.util.Arrays;
import java.util.List;
import java.util.AbstractMap;

static final SchemaConfiguration configuration = new SchemaConfiguration(new JsonSchemaKeywordFlags.Builder().build());

// null validation
Void validatedPayload = NullableClass.NumberProp.validate(
    (Void) null,
    configuration
);

// int validation
int validatedPayload = NullableClass.NumberProp.validate(
    1,
    configuration
);
```

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Set<Class<?>> | type = Set.of(<br/>&nbsp;&nbsp;&nbsp;&nbsp;Void.class,<br/>&nbsp;&nbsp;&nbsp;&nbsp;Integer.class,<br/>&nbsp;&nbsp;&nbsp;&nbsp;Long.class,<br/>&nbsp;&nbsp;&nbsp;&nbsp;Float.class,<br/>&nbsp;&nbsp;&nbsp;&nbsp;Double.class<br/>)<br/> |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| Void | validate(Void arg, SchemaConfiguration configuration) |
| [NumberPropBoxedVoid](#numberpropboxedvoid) | validateAndBox(Void arg, SchemaConfiguration configuration) |
| Number | validate(Number arg, SchemaConfiguration configuration) |
| [NumberPropBoxedNumber](#numberpropboxednumber) | validateAndBox(Number arg, SchemaConfiguration configuration) |
| [NumberPropBoxed](#numberpropboxed) | validateAndBox(@Nullable Object arg, SchemaConfiguration configuration) |
| @Nullable Object | validate(@Nullable Object arg, SchemaConfiguration configuration) |

## IntegerPropBoxed
public sealed interface IntegerPropBoxed<br>
permits<br>
[IntegerPropBoxedVoid](#integerpropboxedvoid),
[IntegerPropBoxedNumber](#integerpropboxednumber)

sealed interface that stores validated payloads using boxed classes

## IntegerPropBoxedVoid
public record IntegerPropBoxedVoid<br>
implements [IntegerPropBoxed](#integerpropboxed)

record that stores validated null payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| IntegerPropBoxedVoid(Void data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| Void | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## IntegerPropBoxedNumber
public record IntegerPropBoxedNumber<br>
implements [IntegerPropBoxed](#integerpropboxed)

record that stores validated Number payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| IntegerPropBoxedNumber(Number data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| Number | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## IntegerProp
public static class IntegerProp<br>
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
import org.openapijsonschematools.client.components.schemas.NullableClass;

import java.util.Arrays;
import java.util.List;
import java.util.AbstractMap;

static final SchemaConfiguration configuration = new SchemaConfiguration(new JsonSchemaKeywordFlags.Builder().build());

// null validation
Void validatedPayload = NullableClass.IntegerProp.validate(
    (Void) null,
    configuration
);

// int validation
int validatedPayload = NullableClass.IntegerProp.validate(
    1L,
    configuration
);
```

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Set<Class<?>> | type = Set.of(<br/>&nbsp;&nbsp;&nbsp;&nbsp;Void.class,<br/>&nbsp;&nbsp;&nbsp;&nbsp;Integer.class,<br/>&nbsp;&nbsp;&nbsp;&nbsp;Long.class,<br/>&nbsp;&nbsp;&nbsp;&nbsp;Float.class,<br/>&nbsp;&nbsp;&nbsp;&nbsp;Double.class<br/>)<br/> |
| String | type = "int"; |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| Void | validate(Void arg, SchemaConfiguration configuration) |
| [IntegerPropBoxedVoid](#integerpropboxedvoid) | validateAndBox(Void arg, SchemaConfiguration configuration) |
| long | validate(long arg, SchemaConfiguration configuration) |
| [IntegerPropBoxedNumber](#integerpropboxednumber) | validateAndBox(Number arg, SchemaConfiguration configuration) |
| [IntegerPropBoxed](#integerpropboxed) | validateAndBox(@Nullable Object arg, SchemaConfiguration configuration) |
| @Nullable Object | validate(@Nullable Object arg, SchemaConfiguration configuration) |

## AdditionalProperties3Boxed
public sealed interface AdditionalProperties3Boxed<br>
permits<br>
[AdditionalProperties3BoxedVoid](#additionalproperties3boxedvoid),
[AdditionalProperties3BoxedMap](#additionalproperties3boxedmap)

sealed interface that stores validated payloads using boxed classes

## AdditionalProperties3BoxedVoid
public record AdditionalProperties3BoxedVoid<br>
implements [AdditionalProperties3Boxed](#additionalproperties3boxed)

record that stores validated null payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| AdditionalProperties3BoxedVoid(Void data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| Void | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## AdditionalProperties3BoxedMap
public record AdditionalProperties3BoxedMap<br>
implements [AdditionalProperties3Boxed](#additionalproperties3boxed)

record that stores validated Map payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| AdditionalProperties3BoxedMap(FrozenMap<@Nullable Object> data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| FrozenMap<@Nullable Object> | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## AdditionalProperties3
public static class AdditionalProperties3<br>
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
import org.openapijsonschematools.client.components.schemas.NullableClass;

import java.util.Arrays;
import java.util.List;
import java.util.AbstractMap;

static final SchemaConfiguration configuration = new SchemaConfiguration(new JsonSchemaKeywordFlags.Builder().build());

// null validation
Void validatedPayload = NullableClass.AdditionalProperties3.validate(
    (Void) null,
    configuration
);
```

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Set<Class<?>> | type = Set.of(<br/>&nbsp;&nbsp;&nbsp;&nbsp;Void.class,<br/>&nbsp;&nbsp;&nbsp;&nbsp;Map.class<br/>)<br/> |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| Void | validate(Void arg, SchemaConfiguration configuration) |
| [AdditionalProperties3BoxedVoid](#additionalproperties3boxedvoid) | validateAndBox(Void arg, SchemaConfiguration configuration) |
| FrozenMap<String, @Nullable Object> | validate(Map&lt;?, ?&gt; arg, SchemaConfiguration configuration) |
| [AdditionalProperties3BoxedMap](#additionalproperties3boxedmap) | validateAndBox(Map&lt;?, ?&gt; arg, SchemaConfiguration configuration) |
| [AdditionalProperties3Boxed](#additionalproperties3boxed) | validateAndBox(@Nullable Object arg, SchemaConfiguration configuration) |
| @Nullable Object | validate(@Nullable Object arg, SchemaConfiguration configuration) |

[[Back to top]](#top) [[Back to Component Schemas]](../../../README.md#Component-Schemas) [[Back to README]](../../../README.md)
