# NullableClass
org.openapijsonschematools.client.components.schemas.NullableClass.java
public class NullableClass<br>

A class that contains necessary nested
- schema classes (which validate payloads), extends JsonSchema
- abstract sealed classes which store validated payloads, java version of a sum type
- boxed classes which store validated payloads, sealed permits class implementations
- classes to store validated list payloads, extends FrozenList
- classes to build inputs for list payloads
- classes to store validated map payloads, extends FrozenMap
- classes to build inputs for map payloads

## Nested Class Summary
| Modifier and Type | Class and Description |
| ----------------- | ---------------------- |
| static class | [NullableClass.NullableClass1Boxed](#nullableclass1boxed)<br> abstract sealed validated payload class |
| static class | [NullableClass.NullableClass1BoxedMap](#nullableclass1boxedmap)<br> boxed class to store validated Map payloads |
| static class | [NullableClass.NullableClass1](#nullableclass1)<br> schema class |
| static class | [NullableClass.NullableClassMapBuilder](#nullableclassmapbuilder)<br> builder for Map payloads |
| static class | [NullableClass.NullableClassMap](#nullableclassmap)<br> output class for Map payloads |
| static class | [NullableClass.ObjectItemsNullableBoxed](#objectitemsnullableboxed)<br> abstract sealed validated payload class |
| static class | [NullableClass.ObjectItemsNullableBoxedMap](#objectitemsnullableboxedmap)<br> boxed class to store validated Map payloads |
| static class | [NullableClass.ObjectItemsNullable](#objectitemsnullable)<br> schema class |
| static class | [NullableClass.ObjectItemsNullableMapBuilder](#objectitemsnullablemapbuilder)<br> builder for Map payloads |
| static class | [NullableClass.ObjectItemsNullableMap](#objectitemsnullablemap)<br> output class for Map payloads |
| static class | [NullableClass.AdditionalProperties2Boxed](#additionalproperties2boxed)<br> abstract sealed validated payload class |
| static class | [NullableClass.AdditionalProperties2BoxedVoid](#additionalproperties2boxedvoid)<br> boxed class to store validated null payloads |
| static class | [NullableClass.AdditionalProperties2BoxedMap](#additionalproperties2boxedmap)<br> boxed class to store validated Map payloads |
| static class | [NullableClass.AdditionalProperties2](#additionalproperties2)<br> schema class |
| static class | [NullableClass.ObjectAndItemsNullablePropBoxed](#objectanditemsnullablepropboxed)<br> abstract sealed validated payload class |
| static class | [NullableClass.ObjectAndItemsNullablePropBoxedVoid](#objectanditemsnullablepropboxedvoid)<br> boxed class to store validated null payloads |
| static class | [NullableClass.ObjectAndItemsNullablePropBoxedMap](#objectanditemsnullablepropboxedmap)<br> boxed class to store validated Map payloads |
| static class | [NullableClass.ObjectAndItemsNullableProp](#objectanditemsnullableprop)<br> schema class |
| static class | [NullableClass.ObjectAndItemsNullablePropMapBuilder](#objectanditemsnullablepropmapbuilder)<br> builder for Map payloads |
| static class | [NullableClass.ObjectAndItemsNullablePropMap](#objectanditemsnullablepropmap)<br> output class for Map payloads |
| static class | [NullableClass.AdditionalProperties1Boxed](#additionalproperties1boxed)<br> abstract sealed validated payload class |
| static class | [NullableClass.AdditionalProperties1BoxedVoid](#additionalproperties1boxedvoid)<br> boxed class to store validated null payloads |
| static class | [NullableClass.AdditionalProperties1BoxedMap](#additionalproperties1boxedmap)<br> boxed class to store validated Map payloads |
| static class | [NullableClass.AdditionalProperties1](#additionalproperties1)<br> schema class |
| static class | [NullableClass.ObjectNullablePropBoxed](#objectnullablepropboxed)<br> abstract sealed validated payload class |
| static class | [NullableClass.ObjectNullablePropBoxedVoid](#objectnullablepropboxedvoid)<br> boxed class to store validated null payloads |
| static class | [NullableClass.ObjectNullablePropBoxedMap](#objectnullablepropboxedmap)<br> boxed class to store validated Map payloads |
| static class | [NullableClass.ObjectNullableProp](#objectnullableprop)<br> schema class |
| static class | [NullableClass.ObjectNullablePropMapBuilder](#objectnullablepropmapbuilder)<br> builder for Map payloads |
| static class | [NullableClass.ObjectNullablePropMap](#objectnullablepropmap)<br> output class for Map payloads |
| static class | [NullableClass.AdditionalPropertiesBoxed](#additionalpropertiesboxed)<br> abstract sealed validated payload class |
| static class | [NullableClass.AdditionalPropertiesBoxedMap](#additionalpropertiesboxedmap)<br> boxed class to store validated Map payloads |
| static class | [NullableClass.AdditionalProperties](#additionalproperties)<br> schema class |
| static class | [NullableClass.ArrayItemsNullableBoxed](#arrayitemsnullableboxed)<br> abstract sealed validated payload class |
| static class | [NullableClass.ArrayItemsNullableBoxedList](#arrayitemsnullableboxedlist)<br> boxed class to store validated List payloads |
| static class | [NullableClass.ArrayItemsNullable](#arrayitemsnullable)<br> schema class |
| static class | [NullableClass.ArrayItemsNullableListBuilder](#arrayitemsnullablelistbuilder)<br> builder for List payloads |
| static class | [NullableClass.ArrayItemsNullableList](#arrayitemsnullablelist)<br> output class for List payloads |
| static class | [NullableClass.Items2Boxed](#items2boxed)<br> abstract sealed validated payload class |
| static class | [NullableClass.Items2BoxedVoid](#items2boxedvoid)<br> boxed class to store validated null payloads |
| static class | [NullableClass.Items2BoxedMap](#items2boxedmap)<br> boxed class to store validated Map payloads |
| static class | [NullableClass.Items2](#items2)<br> schema class |
| static class | [NullableClass.ArrayAndItemsNullablePropBoxed](#arrayanditemsnullablepropboxed)<br> abstract sealed validated payload class |
| static class | [NullableClass.ArrayAndItemsNullablePropBoxedVoid](#arrayanditemsnullablepropboxedvoid)<br> boxed class to store validated null payloads |
| static class | [NullableClass.ArrayAndItemsNullablePropBoxedList](#arrayanditemsnullablepropboxedlist)<br> boxed class to store validated List payloads |
| static class | [NullableClass.ArrayAndItemsNullableProp](#arrayanditemsnullableprop)<br> schema class |
| static class | [NullableClass.ArrayAndItemsNullablePropListBuilder](#arrayanditemsnullableproplistbuilder)<br> builder for List payloads |
| static class | [NullableClass.ArrayAndItemsNullablePropList](#arrayanditemsnullableproplist)<br> output class for List payloads |
| static class | [NullableClass.Items1Boxed](#items1boxed)<br> abstract sealed validated payload class |
| static class | [NullableClass.Items1BoxedVoid](#items1boxedvoid)<br> boxed class to store validated null payloads |
| static class | [NullableClass.Items1BoxedMap](#items1boxedmap)<br> boxed class to store validated Map payloads |
| static class | [NullableClass.Items1](#items1)<br> schema class |
| static class | [NullableClass.ArrayNullablePropBoxed](#arraynullablepropboxed)<br> abstract sealed validated payload class |
| static class | [NullableClass.ArrayNullablePropBoxedVoid](#arraynullablepropboxedvoid)<br> boxed class to store validated null payloads |
| static class | [NullableClass.ArrayNullablePropBoxedList](#arraynullablepropboxedlist)<br> boxed class to store validated List payloads |
| static class | [NullableClass.ArrayNullableProp](#arraynullableprop)<br> schema class |
| static class | [NullableClass.ArrayNullablePropListBuilder](#arraynullableproplistbuilder)<br> builder for List payloads |
| static class | [NullableClass.ArrayNullablePropList](#arraynullableproplist)<br> output class for List payloads |
| static class | [NullableClass.ItemsBoxed](#itemsboxed)<br> abstract sealed validated payload class |
| static class | [NullableClass.ItemsBoxedMap](#itemsboxedmap)<br> boxed class to store validated Map payloads |
| static class | [NullableClass.Items](#items)<br> schema class |
| static class | [NullableClass.DatetimePropBoxed](#datetimepropboxed)<br> abstract sealed validated payload class |
| static class | [NullableClass.DatetimePropBoxedVoid](#datetimepropboxedvoid)<br> boxed class to store validated null payloads |
| static class | [NullableClass.DatetimePropBoxedString](#datetimepropboxedstring)<br> boxed class to store validated String payloads |
| static class | [NullableClass.DatetimeProp](#datetimeprop)<br> schema class |
| static class | [NullableClass.DatePropBoxed](#datepropboxed)<br> abstract sealed validated payload class |
| static class | [NullableClass.DatePropBoxedVoid](#datepropboxedvoid)<br> boxed class to store validated null payloads |
| static class | [NullableClass.DatePropBoxedString](#datepropboxedstring)<br> boxed class to store validated String payloads |
| static class | [NullableClass.DateProp](#dateprop)<br> schema class |
| static class | [NullableClass.StringPropBoxed](#stringpropboxed)<br> abstract sealed validated payload class |
| static class | [NullableClass.StringPropBoxedVoid](#stringpropboxedvoid)<br> boxed class to store validated null payloads |
| static class | [NullableClass.StringPropBoxedString](#stringpropboxedstring)<br> boxed class to store validated String payloads |
| static class | [NullableClass.StringProp](#stringprop)<br> schema class |
| static class | [NullableClass.BooleanPropBoxed](#booleanpropboxed)<br> abstract sealed validated payload class |
| static class | [NullableClass.BooleanPropBoxedVoid](#booleanpropboxedvoid)<br> boxed class to store validated null payloads |
| static class | [NullableClass.BooleanPropBoxedBoolean](#booleanpropboxedboolean)<br> boxed class to store validated boolean payloads |
| static class | [NullableClass.BooleanProp](#booleanprop)<br> schema class |
| static class | [NullableClass.NumberPropBoxed](#numberpropboxed)<br> abstract sealed validated payload class |
| static class | [NullableClass.NumberPropBoxedVoid](#numberpropboxedvoid)<br> boxed class to store validated null payloads |
| static class | [NullableClass.NumberPropBoxedNumber](#numberpropboxednumber)<br> boxed class to store validated Number payloads |
| static class | [NullableClass.NumberProp](#numberprop)<br> schema class |
| static class | [NullableClass.IntegerPropBoxed](#integerpropboxed)<br> abstract sealed validated payload class |
| static class | [NullableClass.IntegerPropBoxedVoid](#integerpropboxedvoid)<br> boxed class to store validated null payloads |
| static class | [NullableClass.IntegerPropBoxedNumber](#integerpropboxednumber)<br> boxed class to store validated Number payloads |
| static class | [NullableClass.IntegerProp](#integerprop)<br> schema class |
| static class | [NullableClass.AdditionalProperties3Boxed](#additionalproperties3boxed)<br> abstract sealed validated payload class |
| static class | [NullableClass.AdditionalProperties3BoxedVoid](#additionalproperties3boxedvoid)<br> boxed class to store validated null payloads |
| static class | [NullableClass.AdditionalProperties3BoxedMap](#additionalproperties3boxedmap)<br> boxed class to store validated Map payloads |
| static class | [NullableClass.AdditionalProperties3](#additionalproperties3)<br> schema class |

## NullableClass1Boxed
public static abstract sealed class NullableClass1Boxed<br>
permits<br>
[NullableClass1BoxedMap](#nullableclass1boxedmap)

abstract sealed class that stores validated payloads using boxed classes

## NullableClass1BoxedMap
public static final class NullableClass1BoxedMap<br>
extends [NullableClass1Boxed](#nullableclass1boxed)

a boxed class to store validated Map payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| NullableClass1BoxedMap([NullableClassMap](#nullableclassmap) data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| [NullableClassMap](#nullableclassmap) | data<br>validated payload |

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

import java.util.Arrays;
import java.util.List;
import java.util.AbstractMap;

static final SchemaConfiguration configuration = new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone());

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
public static abstract sealed class ObjectItemsNullableBoxed<br>
permits<br>
[ObjectItemsNullableBoxedMap](#objectitemsnullableboxedmap)

abstract sealed class that stores validated payloads using boxed classes

## ObjectItemsNullableBoxedMap
public static final class ObjectItemsNullableBoxedMap<br>
extends [ObjectItemsNullableBoxed](#objectitemsnullableboxed)

a boxed class to store validated Map payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| ObjectItemsNullableBoxedMap([ObjectItemsNullableMap](#objectitemsnullablemap) data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| [ObjectItemsNullableMap](#objectitemsnullablemap) | data<br>validated payload |

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

import java.util.Arrays;
import java.util.List;
import java.util.AbstractMap;

static final SchemaConfiguration configuration = new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone());

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
public static abstract sealed class AdditionalProperties2Boxed<br>
permits<br>
[AdditionalProperties2BoxedVoid](#additionalproperties2boxedvoid),
[AdditionalProperties2BoxedMap](#additionalproperties2boxedmap)

abstract sealed class that stores validated payloads using boxed classes

## AdditionalProperties2BoxedVoid
public static final class AdditionalProperties2BoxedVoid<br>
extends [AdditionalProperties2Boxed](#additionalproperties2boxed)

a boxed class to store validated null payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| AdditionalProperties2BoxedVoid(Void data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Void | data<br>validated payload |

## AdditionalProperties2BoxedMap
public static final class AdditionalProperties2BoxedMap<br>
extends [AdditionalProperties2Boxed](#additionalproperties2boxed)

a boxed class to store validated Map payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| AdditionalProperties2BoxedMap(FrozenMap<@Nullable Object> data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| FrozenMap<@Nullable Object> | data<br>validated payload |

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

import java.util.Arrays;
import java.util.List;
import java.util.AbstractMap;

static final SchemaConfiguration configuration = new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone());

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
| @Nullable Object | validate(@Nullable Object arg, SchemaConfiguration configuration) |
## ObjectAndItemsNullablePropBoxed
public static abstract sealed class ObjectAndItemsNullablePropBoxed<br>
permits<br>
[ObjectAndItemsNullablePropBoxedVoid](#objectanditemsnullablepropboxedvoid),
[ObjectAndItemsNullablePropBoxedMap](#objectanditemsnullablepropboxedmap)

abstract sealed class that stores validated payloads using boxed classes

## ObjectAndItemsNullablePropBoxedVoid
public static final class ObjectAndItemsNullablePropBoxedVoid<br>
extends [ObjectAndItemsNullablePropBoxed](#objectanditemsnullablepropboxed)

a boxed class to store validated null payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| ObjectAndItemsNullablePropBoxedVoid(Void data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Void | data<br>validated payload |

## ObjectAndItemsNullablePropBoxedMap
public static final class ObjectAndItemsNullablePropBoxedMap<br>
extends [ObjectAndItemsNullablePropBoxed](#objectanditemsnullablepropboxed)

a boxed class to store validated Map payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| ObjectAndItemsNullablePropBoxedMap([ObjectAndItemsNullablePropMap](#objectanditemsnullablepropmap) data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| [ObjectAndItemsNullablePropMap](#objectanditemsnullablepropmap) | data<br>validated payload |

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

import java.util.Arrays;
import java.util.List;
import java.util.AbstractMap;

static final SchemaConfiguration configuration = new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone());

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
public static abstract sealed class AdditionalProperties1Boxed<br>
permits<br>
[AdditionalProperties1BoxedVoid](#additionalproperties1boxedvoid),
[AdditionalProperties1BoxedMap](#additionalproperties1boxedmap)

abstract sealed class that stores validated payloads using boxed classes

## AdditionalProperties1BoxedVoid
public static final class AdditionalProperties1BoxedVoid<br>
extends [AdditionalProperties1Boxed](#additionalproperties1boxed)

a boxed class to store validated null payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| AdditionalProperties1BoxedVoid(Void data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Void | data<br>validated payload |

## AdditionalProperties1BoxedMap
public static final class AdditionalProperties1BoxedMap<br>
extends [AdditionalProperties1Boxed](#additionalproperties1boxed)

a boxed class to store validated Map payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| AdditionalProperties1BoxedMap(FrozenMap<@Nullable Object> data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| FrozenMap<@Nullable Object> | data<br>validated payload |

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

import java.util.Arrays;
import java.util.List;
import java.util.AbstractMap;

static final SchemaConfiguration configuration = new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone());

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
| @Nullable Object | validate(@Nullable Object arg, SchemaConfiguration configuration) |
## ObjectNullablePropBoxed
public static abstract sealed class ObjectNullablePropBoxed<br>
permits<br>
[ObjectNullablePropBoxedVoid](#objectnullablepropboxedvoid),
[ObjectNullablePropBoxedMap](#objectnullablepropboxedmap)

abstract sealed class that stores validated payloads using boxed classes

## ObjectNullablePropBoxedVoid
public static final class ObjectNullablePropBoxedVoid<br>
extends [ObjectNullablePropBoxed](#objectnullablepropboxed)

a boxed class to store validated null payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| ObjectNullablePropBoxedVoid(Void data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Void | data<br>validated payload |

## ObjectNullablePropBoxedMap
public static final class ObjectNullablePropBoxedMap<br>
extends [ObjectNullablePropBoxed](#objectnullablepropboxed)

a boxed class to store validated Map payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| ObjectNullablePropBoxedMap([ObjectNullablePropMap](#objectnullablepropmap) data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| [ObjectNullablePropMap](#objectnullablepropmap) | data<br>validated payload |

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

import java.util.Arrays;
import java.util.List;
import java.util.AbstractMap;

static final SchemaConfiguration configuration = new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone());

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
public static abstract sealed class AdditionalPropertiesBoxed<br>
permits<br>
[AdditionalPropertiesBoxedMap](#additionalpropertiesboxedmap)

abstract sealed class that stores validated payloads using boxed classes

## AdditionalPropertiesBoxedMap
public static final class AdditionalPropertiesBoxedMap<br>
extends [AdditionalPropertiesBoxed](#additionalpropertiesboxed)

a boxed class to store validated Map payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| AdditionalPropertiesBoxedMap(FrozenMap<@Nullable Object> data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| FrozenMap<@Nullable Object> | data<br>validated payload |

## AdditionalProperties
public static class AdditionalProperties<br>
extends MapJsonSchema.MapJsonSchema1

A schema class that validates payloads

| Methods Inherited from class org.openapijsonschematools.client.schemas.MapJsonSchema.MapJsonSchema1 |
| ------------------------------------------------------------------ |
| validate                                                           |
| validateAndBox                                                     |

## ArrayItemsNullableBoxed
public static abstract sealed class ArrayItemsNullableBoxed<br>
permits<br>
[ArrayItemsNullableBoxedList](#arrayitemsnullableboxedlist)

abstract sealed class that stores validated payloads using boxed classes

## ArrayItemsNullableBoxedList
public static final class ArrayItemsNullableBoxedList<br>
extends [ArrayItemsNullableBoxed](#arrayitemsnullableboxed)

a boxed class to store validated List payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| ArrayItemsNullableBoxedList([ArrayItemsNullableList](#arrayitemsnullablelist) data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| [ArrayItemsNullableList](#arrayitemsnullablelist) | data<br>validated payload |

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

import java.util.Arrays;
import java.util.List;
import java.util.AbstractMap;

static final SchemaConfiguration configuration = new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone());

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
public static abstract sealed class Items2Boxed<br>
permits<br>
[Items2BoxedVoid](#items2boxedvoid),
[Items2BoxedMap](#items2boxedmap)

abstract sealed class that stores validated payloads using boxed classes

## Items2BoxedVoid
public static final class Items2BoxedVoid<br>
extends [Items2Boxed](#items2boxed)

a boxed class to store validated null payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| Items2BoxedVoid(Void data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Void | data<br>validated payload |

## Items2BoxedMap
public static final class Items2BoxedMap<br>
extends [Items2Boxed](#items2boxed)

a boxed class to store validated Map payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| Items2BoxedMap(FrozenMap<@Nullable Object> data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| FrozenMap<@Nullable Object> | data<br>validated payload |

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

import java.util.Arrays;
import java.util.List;
import java.util.AbstractMap;

static final SchemaConfiguration configuration = new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone());

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
| @Nullable Object | validate(@Nullable Object arg, SchemaConfiguration configuration) |
## ArrayAndItemsNullablePropBoxed
public static abstract sealed class ArrayAndItemsNullablePropBoxed<br>
permits<br>
[ArrayAndItemsNullablePropBoxedVoid](#arrayanditemsnullablepropboxedvoid),
[ArrayAndItemsNullablePropBoxedList](#arrayanditemsnullablepropboxedlist)

abstract sealed class that stores validated payloads using boxed classes

## ArrayAndItemsNullablePropBoxedVoid
public static final class ArrayAndItemsNullablePropBoxedVoid<br>
extends [ArrayAndItemsNullablePropBoxed](#arrayanditemsnullablepropboxed)

a boxed class to store validated null payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| ArrayAndItemsNullablePropBoxedVoid(Void data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Void | data<br>validated payload |

## ArrayAndItemsNullablePropBoxedList
public static final class ArrayAndItemsNullablePropBoxedList<br>
extends [ArrayAndItemsNullablePropBoxed](#arrayanditemsnullablepropboxed)

a boxed class to store validated List payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| ArrayAndItemsNullablePropBoxedList([ArrayAndItemsNullablePropList](#arrayanditemsnullableproplist) data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| [ArrayAndItemsNullablePropList](#arrayanditemsnullableproplist) | data<br>validated payload |

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

import java.util.Arrays;
import java.util.List;
import java.util.AbstractMap;

static final SchemaConfiguration configuration = new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone());

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
public static abstract sealed class Items1Boxed<br>
permits<br>
[Items1BoxedVoid](#items1boxedvoid),
[Items1BoxedMap](#items1boxedmap)

abstract sealed class that stores validated payloads using boxed classes

## Items1BoxedVoid
public static final class Items1BoxedVoid<br>
extends [Items1Boxed](#items1boxed)

a boxed class to store validated null payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| Items1BoxedVoid(Void data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Void | data<br>validated payload |

## Items1BoxedMap
public static final class Items1BoxedMap<br>
extends [Items1Boxed](#items1boxed)

a boxed class to store validated Map payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| Items1BoxedMap(FrozenMap<@Nullable Object> data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| FrozenMap<@Nullable Object> | data<br>validated payload |

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

import java.util.Arrays;
import java.util.List;
import java.util.AbstractMap;

static final SchemaConfiguration configuration = new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone());

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
| @Nullable Object | validate(@Nullable Object arg, SchemaConfiguration configuration) |
## ArrayNullablePropBoxed
public static abstract sealed class ArrayNullablePropBoxed<br>
permits<br>
[ArrayNullablePropBoxedVoid](#arraynullablepropboxedvoid),
[ArrayNullablePropBoxedList](#arraynullablepropboxedlist)

abstract sealed class that stores validated payloads using boxed classes

## ArrayNullablePropBoxedVoid
public static final class ArrayNullablePropBoxedVoid<br>
extends [ArrayNullablePropBoxed](#arraynullablepropboxed)

a boxed class to store validated null payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| ArrayNullablePropBoxedVoid(Void data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Void | data<br>validated payload |

## ArrayNullablePropBoxedList
public static final class ArrayNullablePropBoxedList<br>
extends [ArrayNullablePropBoxed](#arraynullablepropboxed)

a boxed class to store validated List payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| ArrayNullablePropBoxedList([ArrayNullablePropList](#arraynullableproplist) data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| [ArrayNullablePropList](#arraynullableproplist) | data<br>validated payload |

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

import java.util.Arrays;
import java.util.List;
import java.util.AbstractMap;

static final SchemaConfiguration configuration = new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone());

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
public static abstract sealed class ItemsBoxed<br>
permits<br>
[ItemsBoxedMap](#itemsboxedmap)

abstract sealed class that stores validated payloads using boxed classes

## ItemsBoxedMap
public static final class ItemsBoxedMap<br>
extends [ItemsBoxed](#itemsboxed)

a boxed class to store validated Map payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| ItemsBoxedMap(FrozenMap<@Nullable Object> data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| FrozenMap<@Nullable Object> | data<br>validated payload |

## Items
public static class Items<br>
extends MapJsonSchema.MapJsonSchema1

A schema class that validates payloads

| Methods Inherited from class org.openapijsonschematools.client.schemas.MapJsonSchema.MapJsonSchema1 |
| ------------------------------------------------------------------ |
| validate                                                           |
| validateAndBox                                                     |

## DatetimePropBoxed
public static abstract sealed class DatetimePropBoxed<br>
permits<br>
[DatetimePropBoxedVoid](#datetimepropboxedvoid),
[DatetimePropBoxedString](#datetimepropboxedstring)

abstract sealed class that stores validated payloads using boxed classes

## DatetimePropBoxedVoid
public static final class DatetimePropBoxedVoid<br>
extends [DatetimePropBoxed](#datetimepropboxed)

a boxed class to store validated null payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| DatetimePropBoxedVoid(Void data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Void | data<br>validated payload |

## DatetimePropBoxedString
public static final class DatetimePropBoxedString<br>
extends [DatetimePropBoxed](#datetimepropboxed)

a boxed class to store validated String payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| DatetimePropBoxedString(String data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| String | data<br>validated payload |

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

import java.util.Arrays;
import java.util.List;
import java.util.AbstractMap;

static final SchemaConfiguration configuration = new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone());

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
| @Nullable Object | validate(@Nullable Object arg, SchemaConfiguration configuration) |
## DatePropBoxed
public static abstract sealed class DatePropBoxed<br>
permits<br>
[DatePropBoxedVoid](#datepropboxedvoid),
[DatePropBoxedString](#datepropboxedstring)

abstract sealed class that stores validated payloads using boxed classes

## DatePropBoxedVoid
public static final class DatePropBoxedVoid<br>
extends [DatePropBoxed](#datepropboxed)

a boxed class to store validated null payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| DatePropBoxedVoid(Void data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Void | data<br>validated payload |

## DatePropBoxedString
public static final class DatePropBoxedString<br>
extends [DatePropBoxed](#datepropboxed)

a boxed class to store validated String payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| DatePropBoxedString(String data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| String | data<br>validated payload |

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

import java.util.Arrays;
import java.util.List;
import java.util.AbstractMap;

static final SchemaConfiguration configuration = new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone());

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
| @Nullable Object | validate(@Nullable Object arg, SchemaConfiguration configuration) |
## StringPropBoxed
public static abstract sealed class StringPropBoxed<br>
permits<br>
[StringPropBoxedVoid](#stringpropboxedvoid),
[StringPropBoxedString](#stringpropboxedstring)

abstract sealed class that stores validated payloads using boxed classes

## StringPropBoxedVoid
public static final class StringPropBoxedVoid<br>
extends [StringPropBoxed](#stringpropboxed)

a boxed class to store validated null payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| StringPropBoxedVoid(Void data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Void | data<br>validated payload |

## StringPropBoxedString
public static final class StringPropBoxedString<br>
extends [StringPropBoxed](#stringpropboxed)

a boxed class to store validated String payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| StringPropBoxedString(String data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| String | data<br>validated payload |

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

import java.util.Arrays;
import java.util.List;
import java.util.AbstractMap;

static final SchemaConfiguration configuration = new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone());

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
| @Nullable Object | validate(@Nullable Object arg, SchemaConfiguration configuration) |
## BooleanPropBoxed
public static abstract sealed class BooleanPropBoxed<br>
permits<br>
[BooleanPropBoxedVoid](#booleanpropboxedvoid),
[BooleanPropBoxedBoolean](#booleanpropboxedboolean)

abstract sealed class that stores validated payloads using boxed classes

## BooleanPropBoxedVoid
public static final class BooleanPropBoxedVoid<br>
extends [BooleanPropBoxed](#booleanpropboxed)

a boxed class to store validated null payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| BooleanPropBoxedVoid(Void data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Void | data<br>validated payload |

## BooleanPropBoxedBoolean
public static final class BooleanPropBoxedBoolean<br>
extends [BooleanPropBoxed](#booleanpropboxed)

a boxed class to store validated boolean payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| BooleanPropBoxedBoolean(boolean data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| boolean | data<br>validated payload |

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

import java.util.Arrays;
import java.util.List;
import java.util.AbstractMap;

static final SchemaConfiguration configuration = new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone());

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
| @Nullable Object | validate(@Nullable Object arg, SchemaConfiguration configuration) |
## NumberPropBoxed
public static abstract sealed class NumberPropBoxed<br>
permits<br>
[NumberPropBoxedVoid](#numberpropboxedvoid),
[NumberPropBoxedNumber](#numberpropboxednumber)

abstract sealed class that stores validated payloads using boxed classes

## NumberPropBoxedVoid
public static final class NumberPropBoxedVoid<br>
extends [NumberPropBoxed](#numberpropboxed)

a boxed class to store validated null payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| NumberPropBoxedVoid(Void data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Void | data<br>validated payload |

## NumberPropBoxedNumber
public static final class NumberPropBoxedNumber<br>
extends [NumberPropBoxed](#numberpropboxed)

a boxed class to store validated Number payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| NumberPropBoxedNumber(Number data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Number | data<br>validated payload |

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

import java.util.Arrays;
import java.util.List;
import java.util.AbstractMap;

static final SchemaConfiguration configuration = new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone());

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
| @Nullable Object | validate(@Nullable Object arg, SchemaConfiguration configuration) |
## IntegerPropBoxed
public static abstract sealed class IntegerPropBoxed<br>
permits<br>
[IntegerPropBoxedVoid](#integerpropboxedvoid),
[IntegerPropBoxedNumber](#integerpropboxednumber)

abstract sealed class that stores validated payloads using boxed classes

## IntegerPropBoxedVoid
public static final class IntegerPropBoxedVoid<br>
extends [IntegerPropBoxed](#integerpropboxed)

a boxed class to store validated null payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| IntegerPropBoxedVoid(Void data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Void | data<br>validated payload |

## IntegerPropBoxedNumber
public static final class IntegerPropBoxedNumber<br>
extends [IntegerPropBoxed](#integerpropboxed)

a boxed class to store validated Number payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| IntegerPropBoxedNumber(Number data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Number | data<br>validated payload |

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

import java.util.Arrays;
import java.util.List;
import java.util.AbstractMap;

static final SchemaConfiguration configuration = new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone());

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
| @Nullable Object | validate(@Nullable Object arg, SchemaConfiguration configuration) |
## AdditionalProperties3Boxed
public static abstract sealed class AdditionalProperties3Boxed<br>
permits<br>
[AdditionalProperties3BoxedVoid](#additionalproperties3boxedvoid),
[AdditionalProperties3BoxedMap](#additionalproperties3boxedmap)

abstract sealed class that stores validated payloads using boxed classes

## AdditionalProperties3BoxedVoid
public static final class AdditionalProperties3BoxedVoid<br>
extends [AdditionalProperties3Boxed](#additionalproperties3boxed)

a boxed class to store validated null payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| AdditionalProperties3BoxedVoid(Void data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Void | data<br>validated payload |

## AdditionalProperties3BoxedMap
public static final class AdditionalProperties3BoxedMap<br>
extends [AdditionalProperties3Boxed](#additionalproperties3boxed)

a boxed class to store validated Map payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| AdditionalProperties3BoxedMap(FrozenMap<@Nullable Object> data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| FrozenMap<@Nullable Object> | data<br>validated payload |

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

import java.util.Arrays;
import java.util.List;
import java.util.AbstractMap;

static final SchemaConfiguration configuration = new SchemaConfiguration(JsonSchemaKeywordFlags.ofNone());

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
| @Nullable Object | validate(@Nullable Object arg, SchemaConfiguration configuration) |
[[Back to top]](#top) [[Back to Component Schemas]](../../../README.md#Component-Schemas) [[Back to README]](../../../README.md)
