# AnyTypeAndFormat
org.openapijsonschematools.client.components.schemas.AnyTypeAndFormat.java
public class AnyTypeAndFormat<br>

A class that contains necessary nested
- schema classes (which validate payloads), extends JsonSchema
- abstract sealed classes which store validated payloads, java version of a sum type
- boxed classes which store validated payloads, sealed permits class implementations
- classes to store validated map payloads, extends FrozenMap
- classes to build inputs for map payloads

## Nested Class Summary
| Modifier and Type | Class and Description |
| ----------------- | ---------------------- |
| static class | [AnyTypeAndFormat.AnyTypeAndFormat1Boxed](#anytypeandformat1boxed)<br> abstract sealed validated payload class |
| static class | [AnyTypeAndFormat.AnyTypeAndFormat1BoxedMap](#anytypeandformat1boxedmap)<br> boxed class to store validated Map payloads |
| static class | [AnyTypeAndFormat.AnyTypeAndFormat1](#anytypeandformat1)<br> schema class |
| static class | [AnyTypeAndFormat.AnyTypeAndFormatMapBuilder](#anytypeandformatmapbuilder)<br> builder for Map payloads |
| static class | [AnyTypeAndFormat.AnyTypeAndFormatMap](#anytypeandformatmap)<br> output class for Map payloads |
| static class | [AnyTypeAndFormat.FloatSchemaBoxed](#floatschemaboxed)<br> abstract sealed validated payload class |
| static class | [AnyTypeAndFormat.FloatSchemaBoxedVoid](#floatschemaboxedvoid)<br> boxed class to store validated null payloads |
| static class | [AnyTypeAndFormat.FloatSchemaBoxedBoolean](#floatschemaboxedboolean)<br> boxed class to store validated boolean payloads |
| static class | [AnyTypeAndFormat.FloatSchemaBoxedNumber](#floatschemaboxednumber)<br> boxed class to store validated Number payloads |
| static class | [AnyTypeAndFormat.FloatSchemaBoxedString](#floatschemaboxedstring)<br> boxed class to store validated String payloads |
| static class | [AnyTypeAndFormat.FloatSchemaBoxedList](#floatschemaboxedlist)<br> boxed class to store validated List payloads |
| static class | [AnyTypeAndFormat.FloatSchemaBoxedMap](#floatschemaboxedmap)<br> boxed class to store validated Map payloads |
| static class | [AnyTypeAndFormat.FloatSchema](#floatschema)<br> schema class |
| static class | [AnyTypeAndFormat.DoubleSchemaBoxed](#doubleschemaboxed)<br> abstract sealed validated payload class |
| static class | [AnyTypeAndFormat.DoubleSchemaBoxedVoid](#doubleschemaboxedvoid)<br> boxed class to store validated null payloads |
| static class | [AnyTypeAndFormat.DoubleSchemaBoxedBoolean](#doubleschemaboxedboolean)<br> boxed class to store validated boolean payloads |
| static class | [AnyTypeAndFormat.DoubleSchemaBoxedNumber](#doubleschemaboxednumber)<br> boxed class to store validated Number payloads |
| static class | [AnyTypeAndFormat.DoubleSchemaBoxedString](#doubleschemaboxedstring)<br> boxed class to store validated String payloads |
| static class | [AnyTypeAndFormat.DoubleSchemaBoxedList](#doubleschemaboxedlist)<br> boxed class to store validated List payloads |
| static class | [AnyTypeAndFormat.DoubleSchemaBoxedMap](#doubleschemaboxedmap)<br> boxed class to store validated Map payloads |
| static class | [AnyTypeAndFormat.DoubleSchema](#doubleschema)<br> schema class |
| static class | [AnyTypeAndFormat.Int64Boxed](#int64boxed)<br> abstract sealed validated payload class |
| static class | [AnyTypeAndFormat.Int64BoxedVoid](#int64boxedvoid)<br> boxed class to store validated null payloads |
| static class | [AnyTypeAndFormat.Int64BoxedBoolean](#int64boxedboolean)<br> boxed class to store validated boolean payloads |
| static class | [AnyTypeAndFormat.Int64BoxedNumber](#int64boxednumber)<br> boxed class to store validated Number payloads |
| static class | [AnyTypeAndFormat.Int64BoxedString](#int64boxedstring)<br> boxed class to store validated String payloads |
| static class | [AnyTypeAndFormat.Int64BoxedList](#int64boxedlist)<br> boxed class to store validated List payloads |
| static class | [AnyTypeAndFormat.Int64BoxedMap](#int64boxedmap)<br> boxed class to store validated Map payloads |
| static class | [AnyTypeAndFormat.Int64](#int64)<br> schema class |
| static class | [AnyTypeAndFormat.Int32Boxed](#int32boxed)<br> abstract sealed validated payload class |
| static class | [AnyTypeAndFormat.Int32BoxedVoid](#int32boxedvoid)<br> boxed class to store validated null payloads |
| static class | [AnyTypeAndFormat.Int32BoxedBoolean](#int32boxedboolean)<br> boxed class to store validated boolean payloads |
| static class | [AnyTypeAndFormat.Int32BoxedNumber](#int32boxednumber)<br> boxed class to store validated Number payloads |
| static class | [AnyTypeAndFormat.Int32BoxedString](#int32boxedstring)<br> boxed class to store validated String payloads |
| static class | [AnyTypeAndFormat.Int32BoxedList](#int32boxedlist)<br> boxed class to store validated List payloads |
| static class | [AnyTypeAndFormat.Int32BoxedMap](#int32boxedmap)<br> boxed class to store validated Map payloads |
| static class | [AnyTypeAndFormat.Int32](#int32)<br> schema class |
| static class | [AnyTypeAndFormat.BinaryBoxed](#binaryboxed)<br> abstract sealed validated payload class |
| static class | [AnyTypeAndFormat.BinaryBoxedVoid](#binaryboxedvoid)<br> boxed class to store validated null payloads |
| static class | [AnyTypeAndFormat.BinaryBoxedBoolean](#binaryboxedboolean)<br> boxed class to store validated boolean payloads |
| static class | [AnyTypeAndFormat.BinaryBoxedNumber](#binaryboxednumber)<br> boxed class to store validated Number payloads |
| static class | [AnyTypeAndFormat.BinaryBoxedString](#binaryboxedstring)<br> boxed class to store validated String payloads |
| static class | [AnyTypeAndFormat.BinaryBoxedList](#binaryboxedlist)<br> boxed class to store validated List payloads |
| static class | [AnyTypeAndFormat.BinaryBoxedMap](#binaryboxedmap)<br> boxed class to store validated Map payloads |
| static class | [AnyTypeAndFormat.Binary](#binary)<br> schema class |
| static class | [AnyTypeAndFormat.NumberSchemaBoxed](#numberschemaboxed)<br> abstract sealed validated payload class |
| static class | [AnyTypeAndFormat.NumberSchemaBoxedVoid](#numberschemaboxedvoid)<br> boxed class to store validated null payloads |
| static class | [AnyTypeAndFormat.NumberSchemaBoxedBoolean](#numberschemaboxedboolean)<br> boxed class to store validated boolean payloads |
| static class | [AnyTypeAndFormat.NumberSchemaBoxedNumber](#numberschemaboxednumber)<br> boxed class to store validated Number payloads |
| static class | [AnyTypeAndFormat.NumberSchemaBoxedString](#numberschemaboxedstring)<br> boxed class to store validated String payloads |
| static class | [AnyTypeAndFormat.NumberSchemaBoxedList](#numberschemaboxedlist)<br> boxed class to store validated List payloads |
| static class | [AnyTypeAndFormat.NumberSchemaBoxedMap](#numberschemaboxedmap)<br> boxed class to store validated Map payloads |
| static class | [AnyTypeAndFormat.NumberSchema](#numberschema)<br> schema class |
| static class | [AnyTypeAndFormat.DatetimeBoxed](#datetimeboxed)<br> abstract sealed validated payload class |
| static class | [AnyTypeAndFormat.DatetimeBoxedVoid](#datetimeboxedvoid)<br> boxed class to store validated null payloads |
| static class | [AnyTypeAndFormat.DatetimeBoxedBoolean](#datetimeboxedboolean)<br> boxed class to store validated boolean payloads |
| static class | [AnyTypeAndFormat.DatetimeBoxedNumber](#datetimeboxednumber)<br> boxed class to store validated Number payloads |
| static class | [AnyTypeAndFormat.DatetimeBoxedString](#datetimeboxedstring)<br> boxed class to store validated String payloads |
| static class | [AnyTypeAndFormat.DatetimeBoxedList](#datetimeboxedlist)<br> boxed class to store validated List payloads |
| static class | [AnyTypeAndFormat.DatetimeBoxedMap](#datetimeboxedmap)<br> boxed class to store validated Map payloads |
| static class | [AnyTypeAndFormat.Datetime](#datetime)<br> schema class |
| static class | [AnyTypeAndFormat.DateBoxed](#dateboxed)<br> abstract sealed validated payload class |
| static class | [AnyTypeAndFormat.DateBoxedVoid](#dateboxedvoid)<br> boxed class to store validated null payloads |
| static class | [AnyTypeAndFormat.DateBoxedBoolean](#dateboxedboolean)<br> boxed class to store validated boolean payloads |
| static class | [AnyTypeAndFormat.DateBoxedNumber](#dateboxednumber)<br> boxed class to store validated Number payloads |
| static class | [AnyTypeAndFormat.DateBoxedString](#dateboxedstring)<br> boxed class to store validated String payloads |
| static class | [AnyTypeAndFormat.DateBoxedList](#dateboxedlist)<br> boxed class to store validated List payloads |
| static class | [AnyTypeAndFormat.DateBoxedMap](#dateboxedmap)<br> boxed class to store validated Map payloads |
| static class | [AnyTypeAndFormat.Date](#date)<br> schema class |
| static class | [AnyTypeAndFormat.UuidSchemaBoxed](#uuidschemaboxed)<br> abstract sealed validated payload class |
| static class | [AnyTypeAndFormat.UuidSchemaBoxedVoid](#uuidschemaboxedvoid)<br> boxed class to store validated null payloads |
| static class | [AnyTypeAndFormat.UuidSchemaBoxedBoolean](#uuidschemaboxedboolean)<br> boxed class to store validated boolean payloads |
| static class | [AnyTypeAndFormat.UuidSchemaBoxedNumber](#uuidschemaboxednumber)<br> boxed class to store validated Number payloads |
| static class | [AnyTypeAndFormat.UuidSchemaBoxedString](#uuidschemaboxedstring)<br> boxed class to store validated String payloads |
| static class | [AnyTypeAndFormat.UuidSchemaBoxedList](#uuidschemaboxedlist)<br> boxed class to store validated List payloads |
| static class | [AnyTypeAndFormat.UuidSchemaBoxedMap](#uuidschemaboxedmap)<br> boxed class to store validated Map payloads |
| static class | [AnyTypeAndFormat.UuidSchema](#uuidschema)<br> schema class |

## AnyTypeAndFormat1Boxed
public static abstract sealed class AnyTypeAndFormat1Boxed<br>
permits<br>
[AnyTypeAndFormat1BoxedMap](#anytypeandformat1boxedmap)

abstract sealed class that stores validated payloads using boxed classes

## AnyTypeAndFormat1BoxedMap
public static final class AnyTypeAndFormat1BoxedMap<br>
extends [AnyTypeAndFormat1Boxed](#anytypeandformat1boxed)

a boxed class to store validated Map payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| AnyTypeAndFormat1BoxedMap([AnyTypeAndFormatMap](#anytypeandformatmap) data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| [AnyTypeAndFormatMap](#anytypeandformatmap) | data<br>validated payload |

## AnyTypeAndFormat1
public static class AnyTypeAndFormat1<br>
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
AnyTypeAndFormat.AnyTypeAndFormatMap validatedPayload =
    AnyTypeAndFormat.AnyTypeAndFormat1.validate(
    new AnyTypeAndFormat.AnyTypeAndFormatMapBuilder()
    .build(),
    configuration
);
```

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Set<Class<?>> | type = Set.of(Map.class) |
| Map<String, Class<? extends JsonSchema>> | properties = Map.ofEntries(<br>&nbsp;&nbsp;&nbsp;&nbsp;new PropertyEntry("uuid", [UuidSchema.class](#uuidschema))),<br>&nbsp;&nbsp;&nbsp;&nbsp;new PropertyEntry("date", [Date.class](#date))),<br>&nbsp;&nbsp;&nbsp;&nbsp;new PropertyEntry("date-time", [Datetime.class](#datetime))),<br>&nbsp;&nbsp;&nbsp;&nbsp;new PropertyEntry("number", [NumberSchema.class](#numberschema))),<br>&nbsp;&nbsp;&nbsp;&nbsp;new PropertyEntry("binary", [Binary.class](#binary))),<br>&nbsp;&nbsp;&nbsp;&nbsp;new PropertyEntry("int32", [Int32.class](#int32))),<br>&nbsp;&nbsp;&nbsp;&nbsp;new PropertyEntry("int64", [Int64.class](#int64))),<br>&nbsp;&nbsp;&nbsp;&nbsp;new PropertyEntry("double", [DoubleSchema.class](#doubleschema))),<br>&nbsp;&nbsp;&nbsp;&nbsp;new PropertyEntry("float", [FloatSchema.class](#floatschema)))<br>)<br> |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| [AnyTypeAndFormatMap](#anytypeandformatmap) | validate([Map&lt;?, ?&gt;](#anytypeandformatmapbuilder) arg, SchemaConfiguration configuration) |
| [AnyTypeAndFormat1BoxedMap](#anytypeandformat1boxedmap) | validateAndBox([Map&lt;?, ?&gt;](#anytypeandformatmapbuilder) arg, SchemaConfiguration configuration) |
| @Nullable Object | validate(@Nullable Object arg, SchemaConfiguration configuration) |
## AnyTypeAndFormatMapBuilder
public class AnyTypeAndFormatMapBuilder<br>
builder for `Map<String, @Nullable Object>`

A class that builds the Map input type

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| AnyTypeAndFormatMapBuilder()<br>Creates a builder that contains an empty map |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| Map<String, @Nullable Object> | build()<br>Returns map input that should be used with Schema.validate |
| [AnyTypeAndFormatMapBuilder](#anytypeandformatmapbuilder) | setUuid(Void value) |
| [AnyTypeAndFormatMapBuilder](#anytypeandformatmapbuilder) | setUuid(boolean value) |
| [AnyTypeAndFormatMapBuilder](#anytypeandformatmapbuilder) | setUuid(String value) |
| [AnyTypeAndFormatMapBuilder](#anytypeandformatmapbuilder) | setUuid(int value) |
| [AnyTypeAndFormatMapBuilder](#anytypeandformatmapbuilder) | setUuid(float value) |
| [AnyTypeAndFormatMapBuilder](#anytypeandformatmapbuilder) | setUuid(long value) |
| [AnyTypeAndFormatMapBuilder](#anytypeandformatmapbuilder) | setUuid(double value) |
| [AnyTypeAndFormatMapBuilder](#anytypeandformatmapbuilder) | setUuid(List<?> value) |
| [AnyTypeAndFormatMapBuilder](#anytypeandformatmapbuilder) | setUuid(Map<String, ?> value) |
| [AnyTypeAndFormatMapBuilder](#anytypeandformatmapbuilder) | date(Void value) |
| [AnyTypeAndFormatMapBuilder](#anytypeandformatmapbuilder) | date(boolean value) |
| [AnyTypeAndFormatMapBuilder](#anytypeandformatmapbuilder) | date(String value) |
| [AnyTypeAndFormatMapBuilder](#anytypeandformatmapbuilder) | date(int value) |
| [AnyTypeAndFormatMapBuilder](#anytypeandformatmapbuilder) | date(float value) |
| [AnyTypeAndFormatMapBuilder](#anytypeandformatmapbuilder) | date(long value) |
| [AnyTypeAndFormatMapBuilder](#anytypeandformatmapbuilder) | date(double value) |
| [AnyTypeAndFormatMapBuilder](#anytypeandformatmapbuilder) | date(List<?> value) |
| [AnyTypeAndFormatMapBuilder](#anytypeandformatmapbuilder) | date(Map<String, ?> value) |
| [AnyTypeAndFormatMapBuilder](#anytypeandformatmapbuilder) | setDateHyphenMinusTime(Void value) |
| [AnyTypeAndFormatMapBuilder](#anytypeandformatmapbuilder) | setDateHyphenMinusTime(boolean value) |
| [AnyTypeAndFormatMapBuilder](#anytypeandformatmapbuilder) | setDateHyphenMinusTime(String value) |
| [AnyTypeAndFormatMapBuilder](#anytypeandformatmapbuilder) | setDateHyphenMinusTime(int value) |
| [AnyTypeAndFormatMapBuilder](#anytypeandformatmapbuilder) | setDateHyphenMinusTime(float value) |
| [AnyTypeAndFormatMapBuilder](#anytypeandformatmapbuilder) | setDateHyphenMinusTime(long value) |
| [AnyTypeAndFormatMapBuilder](#anytypeandformatmapbuilder) | setDateHyphenMinusTime(double value) |
| [AnyTypeAndFormatMapBuilder](#anytypeandformatmapbuilder) | setDateHyphenMinusTime(List<?> value) |
| [AnyTypeAndFormatMapBuilder](#anytypeandformatmapbuilder) | setDateHyphenMinusTime(Map<String, ?> value) |
| [AnyTypeAndFormatMapBuilder](#anytypeandformatmapbuilder) | setNumber(Void value) |
| [AnyTypeAndFormatMapBuilder](#anytypeandformatmapbuilder) | setNumber(boolean value) |
| [AnyTypeAndFormatMapBuilder](#anytypeandformatmapbuilder) | setNumber(String value) |
| [AnyTypeAndFormatMapBuilder](#anytypeandformatmapbuilder) | setNumber(int value) |
| [AnyTypeAndFormatMapBuilder](#anytypeandformatmapbuilder) | setNumber(float value) |
| [AnyTypeAndFormatMapBuilder](#anytypeandformatmapbuilder) | setNumber(long value) |
| [AnyTypeAndFormatMapBuilder](#anytypeandformatmapbuilder) | setNumber(double value) |
| [AnyTypeAndFormatMapBuilder](#anytypeandformatmapbuilder) | setNumber(List<?> value) |
| [AnyTypeAndFormatMapBuilder](#anytypeandformatmapbuilder) | setNumber(Map<String, ?> value) |
| [AnyTypeAndFormatMapBuilder](#anytypeandformatmapbuilder) | binary(Void value) |
| [AnyTypeAndFormatMapBuilder](#anytypeandformatmapbuilder) | binary(boolean value) |
| [AnyTypeAndFormatMapBuilder](#anytypeandformatmapbuilder) | binary(String value) |
| [AnyTypeAndFormatMapBuilder](#anytypeandformatmapbuilder) | binary(int value) |
| [AnyTypeAndFormatMapBuilder](#anytypeandformatmapbuilder) | binary(float value) |
| [AnyTypeAndFormatMapBuilder](#anytypeandformatmapbuilder) | binary(long value) |
| [AnyTypeAndFormatMapBuilder](#anytypeandformatmapbuilder) | binary(double value) |
| [AnyTypeAndFormatMapBuilder](#anytypeandformatmapbuilder) | binary(List<?> value) |
| [AnyTypeAndFormatMapBuilder](#anytypeandformatmapbuilder) | binary(Map<String, ?> value) |
| [AnyTypeAndFormatMapBuilder](#anytypeandformatmapbuilder) | int32(Void value) |
| [AnyTypeAndFormatMapBuilder](#anytypeandformatmapbuilder) | int32(boolean value) |
| [AnyTypeAndFormatMapBuilder](#anytypeandformatmapbuilder) | int32(String value) |
| [AnyTypeAndFormatMapBuilder](#anytypeandformatmapbuilder) | int32(int value) |
| [AnyTypeAndFormatMapBuilder](#anytypeandformatmapbuilder) | int32(float value) |
| [AnyTypeAndFormatMapBuilder](#anytypeandformatmapbuilder) | int32(long value) |
| [AnyTypeAndFormatMapBuilder](#anytypeandformatmapbuilder) | int32(double value) |
| [AnyTypeAndFormatMapBuilder](#anytypeandformatmapbuilder) | int32(List<?> value) |
| [AnyTypeAndFormatMapBuilder](#anytypeandformatmapbuilder) | int32(Map<String, ?> value) |
| [AnyTypeAndFormatMapBuilder](#anytypeandformatmapbuilder) | int64(Void value) |
| [AnyTypeAndFormatMapBuilder](#anytypeandformatmapbuilder) | int64(boolean value) |
| [AnyTypeAndFormatMapBuilder](#anytypeandformatmapbuilder) | int64(String value) |
| [AnyTypeAndFormatMapBuilder](#anytypeandformatmapbuilder) | int64(int value) |
| [AnyTypeAndFormatMapBuilder](#anytypeandformatmapbuilder) | int64(float value) |
| [AnyTypeAndFormatMapBuilder](#anytypeandformatmapbuilder) | int64(long value) |
| [AnyTypeAndFormatMapBuilder](#anytypeandformatmapbuilder) | int64(double value) |
| [AnyTypeAndFormatMapBuilder](#anytypeandformatmapbuilder) | int64(List<?> value) |
| [AnyTypeAndFormatMapBuilder](#anytypeandformatmapbuilder) | int64(Map<String, ?> value) |
| [AnyTypeAndFormatMapBuilder](#anytypeandformatmapbuilder) | setDouble(Void value) |
| [AnyTypeAndFormatMapBuilder](#anytypeandformatmapbuilder) | setDouble(boolean value) |
| [AnyTypeAndFormatMapBuilder](#anytypeandformatmapbuilder) | setDouble(String value) |
| [AnyTypeAndFormatMapBuilder](#anytypeandformatmapbuilder) | setDouble(int value) |
| [AnyTypeAndFormatMapBuilder](#anytypeandformatmapbuilder) | setDouble(float value) |
| [AnyTypeAndFormatMapBuilder](#anytypeandformatmapbuilder) | setDouble(long value) |
| [AnyTypeAndFormatMapBuilder](#anytypeandformatmapbuilder) | setDouble(double value) |
| [AnyTypeAndFormatMapBuilder](#anytypeandformatmapbuilder) | setDouble(List<?> value) |
| [AnyTypeAndFormatMapBuilder](#anytypeandformatmapbuilder) | setDouble(Map<String, ?> value) |
| [AnyTypeAndFormatMapBuilder](#anytypeandformatmapbuilder) | setFloat(Void value) |
| [AnyTypeAndFormatMapBuilder](#anytypeandformatmapbuilder) | setFloat(boolean value) |
| [AnyTypeAndFormatMapBuilder](#anytypeandformatmapbuilder) | setFloat(String value) |
| [AnyTypeAndFormatMapBuilder](#anytypeandformatmapbuilder) | setFloat(int value) |
| [AnyTypeAndFormatMapBuilder](#anytypeandformatmapbuilder) | setFloat(float value) |
| [AnyTypeAndFormatMapBuilder](#anytypeandformatmapbuilder) | setFloat(long value) |
| [AnyTypeAndFormatMapBuilder](#anytypeandformatmapbuilder) | setFloat(double value) |
| [AnyTypeAndFormatMapBuilder](#anytypeandformatmapbuilder) | setFloat(List<?> value) |
| [AnyTypeAndFormatMapBuilder](#anytypeandformatmapbuilder) | setFloat(Map<String, ?> value) |
| [AnyTypeAndFormatMapBuilder](#anytypeandformatmapbuilder) | additionalProperty(String key, Void value) |
| [AnyTypeAndFormatMapBuilder](#anytypeandformatmapbuilder) | additionalProperty(String key, boolean value) |
| [AnyTypeAndFormatMapBuilder](#anytypeandformatmapbuilder) | additionalProperty(String key, String value) |
| [AnyTypeAndFormatMapBuilder](#anytypeandformatmapbuilder) | additionalProperty(String key, int value) |
| [AnyTypeAndFormatMapBuilder](#anytypeandformatmapbuilder) | additionalProperty(String key, float value) |
| [AnyTypeAndFormatMapBuilder](#anytypeandformatmapbuilder) | additionalProperty(String key, long value) |
| [AnyTypeAndFormatMapBuilder](#anytypeandformatmapbuilder) | additionalProperty(String key, double value) |
| [AnyTypeAndFormatMapBuilder](#anytypeandformatmapbuilder) | additionalProperty(String key, List<?> value) |
| [AnyTypeAndFormatMapBuilder](#anytypeandformatmapbuilder) | additionalProperty(String key, Map<String, ?> value) |

## AnyTypeAndFormatMap
public static class AnyTypeAndFormatMap<br>
extends FrozenMap<String, @Nullable Object>

A class to store validated Map payloads

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| static [AnyTypeAndFormatMap](#anytypeandformatmap) | of([Map<String, ? extends @Nullable Object>](#anytypeandformatmapbuilder) arg, SchemaConfiguration configuration) |
| @Nullable Object | date()<br>[optional] value must conform to RFC-3339 full-date YYYY-MM-DD |
| @Nullable Object | binary()<br>[optional] |
| @Nullable Object | int32()<br>[optional] value must be a 32 bit integer |
| @Nullable Object | int64()<br>[optional] value must be a 64 bit integer |
| @Nullable Object | get(String key)<br>This schema has invalid Java names so this method must be used when you access instance["uuid"], instance["date-time"], instance["number"], instance["double"], instance["float"],  |
| @Nullable Object | getAdditionalProperty(String name)<br>provides type safety for additional properties |

## FloatSchemaBoxed
public static abstract sealed class FloatSchemaBoxed<br>
permits<br>
[FloatSchemaBoxedVoid](#floatschemaboxedvoid),
[FloatSchemaBoxedBoolean](#floatschemaboxedboolean),
[FloatSchemaBoxedNumber](#floatschemaboxednumber),
[FloatSchemaBoxedString](#floatschemaboxedstring),
[FloatSchemaBoxedList](#floatschemaboxedlist),
[FloatSchemaBoxedMap](#floatschemaboxedmap)

abstract sealed class that stores validated payloads using boxed classes

## FloatSchemaBoxedVoid
public static final class FloatSchemaBoxedVoid<br>
extends [FloatSchemaBoxed](#floatschemaboxed)

a boxed class to store validated null payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| FloatSchemaBoxedVoid(Void data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Void | data<br>validated payload |

## FloatSchemaBoxedBoolean
public static final class FloatSchemaBoxedBoolean<br>
extends [FloatSchemaBoxed](#floatschemaboxed)

a boxed class to store validated boolean payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| FloatSchemaBoxedBoolean(boolean data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| boolean | data<br>validated payload |

## FloatSchemaBoxedNumber
public static final class FloatSchemaBoxedNumber<br>
extends [FloatSchemaBoxed](#floatschemaboxed)

a boxed class to store validated Number payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| FloatSchemaBoxedNumber(Number data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Number | data<br>validated payload |

## FloatSchemaBoxedString
public static final class FloatSchemaBoxedString<br>
extends [FloatSchemaBoxed](#floatschemaboxed)

a boxed class to store validated String payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| FloatSchemaBoxedString(String data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| String | data<br>validated payload |

## FloatSchemaBoxedList
public static final class FloatSchemaBoxedList<br>
extends [FloatSchemaBoxed](#floatschemaboxed)

a boxed class to store validated List payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| FloatSchemaBoxedList(FrozenList<@Nullable Object> data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| FrozenList<@Nullable Object> | data<br>validated payload |

## FloatSchemaBoxedMap
public static final class FloatSchemaBoxedMap<br>
extends [FloatSchemaBoxed](#floatschemaboxed)

a boxed class to store validated Map payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| FloatSchemaBoxedMap(FrozenMap<@Nullable Object> data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| FrozenMap<@Nullable Object> | data<br>validated payload |

## FloatSchema
public static class FloatSchema<br>
extends JsonSchema

A schema class that validates payloads

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| String | type = "float"; |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| String | validate(String arg, SchemaConfiguration configuration) |
| Void | validate(Void arg, SchemaConfiguration configuration) |
| int | validate(int arg, SchemaConfiguration configuration) |
| long | validate(long arg, SchemaConfiguration configuration) |
| float | validate(float arg, SchemaConfiguration configuration) |
| double | validate(double arg, SchemaConfiguration configuration) |
| Number | validate(Number arg, SchemaConfiguration configuration) |
| boolean | validate(boolean arg, SchemaConfiguration configuration) |
| FrozenMap<@Nullable Object> | validate(Map&lt;?, ?&gt; arg, SchemaConfiguration configuration) |
| FrozenList<@Nullable Object> | validate(List<?> arg, SchemaConfiguration configuration) |
| [FloatSchemaBoxedString](#floatschemaboxedstring) | validateAndBox(String arg, SchemaConfiguration configuration) |
| [FloatSchemaBoxedVoid](#floatschemaboxedvoid) | validateAndBox(Void arg, SchemaConfiguration configuration) |
| [FloatSchemaBoxedNumber](#floatschemaboxednumber) | validateAndBox(Number arg, SchemaConfiguration configuration) |
| [FloatSchemaBoxedBoolean](#floatschemaboxedboolean) | validateAndBox(boolean arg, SchemaConfiguration configuration) |
| [FloatSchemaBoxedMap](#floatschemaboxedmap) | validateAndBox(Map&lt;?, ?&gt; arg, SchemaConfiguration configuration) |
| [FloatSchemaBoxedList](#floatschemaboxedlist) | validateAndBox(List<?> arg, SchemaConfiguration configuration) |
| @Nullable Object | validate(@Nullable Object arg, SchemaConfiguration configuration) |
## DoubleSchemaBoxed
public static abstract sealed class DoubleSchemaBoxed<br>
permits<br>
[DoubleSchemaBoxedVoid](#doubleschemaboxedvoid),
[DoubleSchemaBoxedBoolean](#doubleschemaboxedboolean),
[DoubleSchemaBoxedNumber](#doubleschemaboxednumber),
[DoubleSchemaBoxedString](#doubleschemaboxedstring),
[DoubleSchemaBoxedList](#doubleschemaboxedlist),
[DoubleSchemaBoxedMap](#doubleschemaboxedmap)

abstract sealed class that stores validated payloads using boxed classes

## DoubleSchemaBoxedVoid
public static final class DoubleSchemaBoxedVoid<br>
extends [DoubleSchemaBoxed](#doubleschemaboxed)

a boxed class to store validated null payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| DoubleSchemaBoxedVoid(Void data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Void | data<br>validated payload |

## DoubleSchemaBoxedBoolean
public static final class DoubleSchemaBoxedBoolean<br>
extends [DoubleSchemaBoxed](#doubleschemaboxed)

a boxed class to store validated boolean payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| DoubleSchemaBoxedBoolean(boolean data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| boolean | data<br>validated payload |

## DoubleSchemaBoxedNumber
public static final class DoubleSchemaBoxedNumber<br>
extends [DoubleSchemaBoxed](#doubleschemaboxed)

a boxed class to store validated Number payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| DoubleSchemaBoxedNumber(Number data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Number | data<br>validated payload |

## DoubleSchemaBoxedString
public static final class DoubleSchemaBoxedString<br>
extends [DoubleSchemaBoxed](#doubleschemaboxed)

a boxed class to store validated String payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| DoubleSchemaBoxedString(String data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| String | data<br>validated payload |

## DoubleSchemaBoxedList
public static final class DoubleSchemaBoxedList<br>
extends [DoubleSchemaBoxed](#doubleschemaboxed)

a boxed class to store validated List payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| DoubleSchemaBoxedList(FrozenList<@Nullable Object> data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| FrozenList<@Nullable Object> | data<br>validated payload |

## DoubleSchemaBoxedMap
public static final class DoubleSchemaBoxedMap<br>
extends [DoubleSchemaBoxed](#doubleschemaboxed)

a boxed class to store validated Map payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| DoubleSchemaBoxedMap(FrozenMap<@Nullable Object> data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| FrozenMap<@Nullable Object> | data<br>validated payload |

## DoubleSchema
public static class DoubleSchema<br>
extends JsonSchema

A schema class that validates payloads

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| String | type = "double"; |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| String | validate(String arg, SchemaConfiguration configuration) |
| Void | validate(Void arg, SchemaConfiguration configuration) |
| int | validate(int arg, SchemaConfiguration configuration) |
| long | validate(long arg, SchemaConfiguration configuration) |
| float | validate(float arg, SchemaConfiguration configuration) |
| double | validate(double arg, SchemaConfiguration configuration) |
| Number | validate(Number arg, SchemaConfiguration configuration) |
| boolean | validate(boolean arg, SchemaConfiguration configuration) |
| FrozenMap<@Nullable Object> | validate(Map&lt;?, ?&gt; arg, SchemaConfiguration configuration) |
| FrozenList<@Nullable Object> | validate(List<?> arg, SchemaConfiguration configuration) |
| [DoubleSchemaBoxedString](#doubleschemaboxedstring) | validateAndBox(String arg, SchemaConfiguration configuration) |
| [DoubleSchemaBoxedVoid](#doubleschemaboxedvoid) | validateAndBox(Void arg, SchemaConfiguration configuration) |
| [DoubleSchemaBoxedNumber](#doubleschemaboxednumber) | validateAndBox(Number arg, SchemaConfiguration configuration) |
| [DoubleSchemaBoxedBoolean](#doubleschemaboxedboolean) | validateAndBox(boolean arg, SchemaConfiguration configuration) |
| [DoubleSchemaBoxedMap](#doubleschemaboxedmap) | validateAndBox(Map&lt;?, ?&gt; arg, SchemaConfiguration configuration) |
| [DoubleSchemaBoxedList](#doubleschemaboxedlist) | validateAndBox(List<?> arg, SchemaConfiguration configuration) |
| @Nullable Object | validate(@Nullable Object arg, SchemaConfiguration configuration) |
## Int64Boxed
public static abstract sealed class Int64Boxed<br>
permits<br>
[Int64BoxedVoid](#int64boxedvoid),
[Int64BoxedBoolean](#int64boxedboolean),
[Int64BoxedNumber](#int64boxednumber),
[Int64BoxedString](#int64boxedstring),
[Int64BoxedList](#int64boxedlist),
[Int64BoxedMap](#int64boxedmap)

abstract sealed class that stores validated payloads using boxed classes

## Int64BoxedVoid
public static final class Int64BoxedVoid<br>
extends [Int64Boxed](#int64boxed)

a boxed class to store validated null payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| Int64BoxedVoid(Void data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Void | data<br>validated payload |

## Int64BoxedBoolean
public static final class Int64BoxedBoolean<br>
extends [Int64Boxed](#int64boxed)

a boxed class to store validated boolean payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| Int64BoxedBoolean(boolean data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| boolean | data<br>validated payload |

## Int64BoxedNumber
public static final class Int64BoxedNumber<br>
extends [Int64Boxed](#int64boxed)

a boxed class to store validated Number payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| Int64BoxedNumber(Number data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Number | data<br>validated payload |

## Int64BoxedString
public static final class Int64BoxedString<br>
extends [Int64Boxed](#int64boxed)

a boxed class to store validated String payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| Int64BoxedString(String data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| String | data<br>validated payload |

## Int64BoxedList
public static final class Int64BoxedList<br>
extends [Int64Boxed](#int64boxed)

a boxed class to store validated List payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| Int64BoxedList(FrozenList<@Nullable Object> data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| FrozenList<@Nullable Object> | data<br>validated payload |

## Int64BoxedMap
public static final class Int64BoxedMap<br>
extends [Int64Boxed](#int64boxed)

a boxed class to store validated Map payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| Int64BoxedMap(FrozenMap<@Nullable Object> data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| FrozenMap<@Nullable Object> | data<br>validated payload |

## Int64
public static class Int64<br>
extends JsonSchema

A schema class that validates payloads

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| String | type = "int64"; |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| String | validate(String arg, SchemaConfiguration configuration) |
| Void | validate(Void arg, SchemaConfiguration configuration) |
| int | validate(int arg, SchemaConfiguration configuration) |
| long | validate(long arg, SchemaConfiguration configuration) |
| float | validate(float arg, SchemaConfiguration configuration) |
| double | validate(double arg, SchemaConfiguration configuration) |
| Number | validate(Number arg, SchemaConfiguration configuration) |
| boolean | validate(boolean arg, SchemaConfiguration configuration) |
| FrozenMap<@Nullable Object> | validate(Map&lt;?, ?&gt; arg, SchemaConfiguration configuration) |
| FrozenList<@Nullable Object> | validate(List<?> arg, SchemaConfiguration configuration) |
| [Int64BoxedString](#int64boxedstring) | validateAndBox(String arg, SchemaConfiguration configuration) |
| [Int64BoxedVoid](#int64boxedvoid) | validateAndBox(Void arg, SchemaConfiguration configuration) |
| [Int64BoxedNumber](#int64boxednumber) | validateAndBox(Number arg, SchemaConfiguration configuration) |
| [Int64BoxedBoolean](#int64boxedboolean) | validateAndBox(boolean arg, SchemaConfiguration configuration) |
| [Int64BoxedMap](#int64boxedmap) | validateAndBox(Map&lt;?, ?&gt; arg, SchemaConfiguration configuration) |
| [Int64BoxedList](#int64boxedlist) | validateAndBox(List<?> arg, SchemaConfiguration configuration) |
| @Nullable Object | validate(@Nullable Object arg, SchemaConfiguration configuration) |
## Int32Boxed
public static abstract sealed class Int32Boxed<br>
permits<br>
[Int32BoxedVoid](#int32boxedvoid),
[Int32BoxedBoolean](#int32boxedboolean),
[Int32BoxedNumber](#int32boxednumber),
[Int32BoxedString](#int32boxedstring),
[Int32BoxedList](#int32boxedlist),
[Int32BoxedMap](#int32boxedmap)

abstract sealed class that stores validated payloads using boxed classes

## Int32BoxedVoid
public static final class Int32BoxedVoid<br>
extends [Int32Boxed](#int32boxed)

a boxed class to store validated null payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| Int32BoxedVoid(Void data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Void | data<br>validated payload |

## Int32BoxedBoolean
public static final class Int32BoxedBoolean<br>
extends [Int32Boxed](#int32boxed)

a boxed class to store validated boolean payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| Int32BoxedBoolean(boolean data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| boolean | data<br>validated payload |

## Int32BoxedNumber
public static final class Int32BoxedNumber<br>
extends [Int32Boxed](#int32boxed)

a boxed class to store validated Number payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| Int32BoxedNumber(Number data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Number | data<br>validated payload |

## Int32BoxedString
public static final class Int32BoxedString<br>
extends [Int32Boxed](#int32boxed)

a boxed class to store validated String payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| Int32BoxedString(String data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| String | data<br>validated payload |

## Int32BoxedList
public static final class Int32BoxedList<br>
extends [Int32Boxed](#int32boxed)

a boxed class to store validated List payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| Int32BoxedList(FrozenList<@Nullable Object> data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| FrozenList<@Nullable Object> | data<br>validated payload |

## Int32BoxedMap
public static final class Int32BoxedMap<br>
extends [Int32Boxed](#int32boxed)

a boxed class to store validated Map payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| Int32BoxedMap(FrozenMap<@Nullable Object> data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| FrozenMap<@Nullable Object> | data<br>validated payload |

## Int32
public static class Int32<br>
extends JsonSchema

A schema class that validates payloads

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| String | type = "int32"; |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| String | validate(String arg, SchemaConfiguration configuration) |
| Void | validate(Void arg, SchemaConfiguration configuration) |
| int | validate(int arg, SchemaConfiguration configuration) |
| long | validate(long arg, SchemaConfiguration configuration) |
| float | validate(float arg, SchemaConfiguration configuration) |
| double | validate(double arg, SchemaConfiguration configuration) |
| Number | validate(Number arg, SchemaConfiguration configuration) |
| boolean | validate(boolean arg, SchemaConfiguration configuration) |
| FrozenMap<@Nullable Object> | validate(Map&lt;?, ?&gt; arg, SchemaConfiguration configuration) |
| FrozenList<@Nullable Object> | validate(List<?> arg, SchemaConfiguration configuration) |
| [Int32BoxedString](#int32boxedstring) | validateAndBox(String arg, SchemaConfiguration configuration) |
| [Int32BoxedVoid](#int32boxedvoid) | validateAndBox(Void arg, SchemaConfiguration configuration) |
| [Int32BoxedNumber](#int32boxednumber) | validateAndBox(Number arg, SchemaConfiguration configuration) |
| [Int32BoxedBoolean](#int32boxedboolean) | validateAndBox(boolean arg, SchemaConfiguration configuration) |
| [Int32BoxedMap](#int32boxedmap) | validateAndBox(Map&lt;?, ?&gt; arg, SchemaConfiguration configuration) |
| [Int32BoxedList](#int32boxedlist) | validateAndBox(List<?> arg, SchemaConfiguration configuration) |
| @Nullable Object | validate(@Nullable Object arg, SchemaConfiguration configuration) |
## BinaryBoxed
public static abstract sealed class BinaryBoxed<br>
permits<br>
[BinaryBoxedVoid](#binaryboxedvoid),
[BinaryBoxedBoolean](#binaryboxedboolean),
[BinaryBoxedNumber](#binaryboxednumber),
[BinaryBoxedString](#binaryboxedstring),
[BinaryBoxedList](#binaryboxedlist),
[BinaryBoxedMap](#binaryboxedmap)

abstract sealed class that stores validated payloads using boxed classes

## BinaryBoxedVoid
public static final class BinaryBoxedVoid<br>
extends [BinaryBoxed](#binaryboxed)

a boxed class to store validated null payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| BinaryBoxedVoid(Void data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Void | data<br>validated payload |

## BinaryBoxedBoolean
public static final class BinaryBoxedBoolean<br>
extends [BinaryBoxed](#binaryboxed)

a boxed class to store validated boolean payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| BinaryBoxedBoolean(boolean data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| boolean | data<br>validated payload |

## BinaryBoxedNumber
public static final class BinaryBoxedNumber<br>
extends [BinaryBoxed](#binaryboxed)

a boxed class to store validated Number payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| BinaryBoxedNumber(Number data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Number | data<br>validated payload |

## BinaryBoxedString
public static final class BinaryBoxedString<br>
extends [BinaryBoxed](#binaryboxed)

a boxed class to store validated String payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| BinaryBoxedString(String data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| String | data<br>validated payload |

## BinaryBoxedList
public static final class BinaryBoxedList<br>
extends [BinaryBoxed](#binaryboxed)

a boxed class to store validated List payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| BinaryBoxedList(FrozenList<@Nullable Object> data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| FrozenList<@Nullable Object> | data<br>validated payload |

## BinaryBoxedMap
public static final class BinaryBoxedMap<br>
extends [BinaryBoxed](#binaryboxed)

a boxed class to store validated Map payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| BinaryBoxedMap(FrozenMap<@Nullable Object> data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| FrozenMap<@Nullable Object> | data<br>validated payload |

## Binary
public static class Binary<br>
extends JsonSchema

A schema class that validates payloads

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| String | type = "binary"; |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| String | validate(String arg, SchemaConfiguration configuration) |
| Void | validate(Void arg, SchemaConfiguration configuration) |
| int | validate(int arg, SchemaConfiguration configuration) |
| long | validate(long arg, SchemaConfiguration configuration) |
| float | validate(float arg, SchemaConfiguration configuration) |
| double | validate(double arg, SchemaConfiguration configuration) |
| Number | validate(Number arg, SchemaConfiguration configuration) |
| boolean | validate(boolean arg, SchemaConfiguration configuration) |
| FrozenMap<@Nullable Object> | validate(Map&lt;?, ?&gt; arg, SchemaConfiguration configuration) |
| FrozenList<@Nullable Object> | validate(List<?> arg, SchemaConfiguration configuration) |
| [BinaryBoxedString](#binaryboxedstring) | validateAndBox(String arg, SchemaConfiguration configuration) |
| [BinaryBoxedVoid](#binaryboxedvoid) | validateAndBox(Void arg, SchemaConfiguration configuration) |
| [BinaryBoxedNumber](#binaryboxednumber) | validateAndBox(Number arg, SchemaConfiguration configuration) |
| [BinaryBoxedBoolean](#binaryboxedboolean) | validateAndBox(boolean arg, SchemaConfiguration configuration) |
| [BinaryBoxedMap](#binaryboxedmap) | validateAndBox(Map&lt;?, ?&gt; arg, SchemaConfiguration configuration) |
| [BinaryBoxedList](#binaryboxedlist) | validateAndBox(List<?> arg, SchemaConfiguration configuration) |
| @Nullable Object | validate(@Nullable Object arg, SchemaConfiguration configuration) |
## NumberSchemaBoxed
public static abstract sealed class NumberSchemaBoxed<br>
permits<br>
[NumberSchemaBoxedVoid](#numberschemaboxedvoid),
[NumberSchemaBoxedBoolean](#numberschemaboxedboolean),
[NumberSchemaBoxedNumber](#numberschemaboxednumber),
[NumberSchemaBoxedString](#numberschemaboxedstring),
[NumberSchemaBoxedList](#numberschemaboxedlist),
[NumberSchemaBoxedMap](#numberschemaboxedmap)

abstract sealed class that stores validated payloads using boxed classes

## NumberSchemaBoxedVoid
public static final class NumberSchemaBoxedVoid<br>
extends [NumberSchemaBoxed](#numberschemaboxed)

a boxed class to store validated null payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| NumberSchemaBoxedVoid(Void data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Void | data<br>validated payload |

## NumberSchemaBoxedBoolean
public static final class NumberSchemaBoxedBoolean<br>
extends [NumberSchemaBoxed](#numberschemaboxed)

a boxed class to store validated boolean payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| NumberSchemaBoxedBoolean(boolean data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| boolean | data<br>validated payload |

## NumberSchemaBoxedNumber
public static final class NumberSchemaBoxedNumber<br>
extends [NumberSchemaBoxed](#numberschemaboxed)

a boxed class to store validated Number payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| NumberSchemaBoxedNumber(Number data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Number | data<br>validated payload |

## NumberSchemaBoxedString
public static final class NumberSchemaBoxedString<br>
extends [NumberSchemaBoxed](#numberschemaboxed)

a boxed class to store validated String payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| NumberSchemaBoxedString(String data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| String | data<br>validated payload |

## NumberSchemaBoxedList
public static final class NumberSchemaBoxedList<br>
extends [NumberSchemaBoxed](#numberschemaboxed)

a boxed class to store validated List payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| NumberSchemaBoxedList(FrozenList<@Nullable Object> data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| FrozenList<@Nullable Object> | data<br>validated payload |

## NumberSchemaBoxedMap
public static final class NumberSchemaBoxedMap<br>
extends [NumberSchemaBoxed](#numberschemaboxed)

a boxed class to store validated Map payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| NumberSchemaBoxedMap(FrozenMap<@Nullable Object> data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| FrozenMap<@Nullable Object> | data<br>validated payload |

## NumberSchema
public static class NumberSchema<br>
extends JsonSchema

A schema class that validates payloads

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| String | type = "number"; |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| String | validate(String arg, SchemaConfiguration configuration) |
| Void | validate(Void arg, SchemaConfiguration configuration) |
| int | validate(int arg, SchemaConfiguration configuration) |
| long | validate(long arg, SchemaConfiguration configuration) |
| float | validate(float arg, SchemaConfiguration configuration) |
| double | validate(double arg, SchemaConfiguration configuration) |
| Number | validate(Number arg, SchemaConfiguration configuration) |
| boolean | validate(boolean arg, SchemaConfiguration configuration) |
| FrozenMap<@Nullable Object> | validate(Map&lt;?, ?&gt; arg, SchemaConfiguration configuration) |
| FrozenList<@Nullable Object> | validate(List<?> arg, SchemaConfiguration configuration) |
| [NumberSchemaBoxedString](#numberschemaboxedstring) | validateAndBox(String arg, SchemaConfiguration configuration) |
| [NumberSchemaBoxedVoid](#numberschemaboxedvoid) | validateAndBox(Void arg, SchemaConfiguration configuration) |
| [NumberSchemaBoxedNumber](#numberschemaboxednumber) | validateAndBox(Number arg, SchemaConfiguration configuration) |
| [NumberSchemaBoxedBoolean](#numberschemaboxedboolean) | validateAndBox(boolean arg, SchemaConfiguration configuration) |
| [NumberSchemaBoxedMap](#numberschemaboxedmap) | validateAndBox(Map&lt;?, ?&gt; arg, SchemaConfiguration configuration) |
| [NumberSchemaBoxedList](#numberschemaboxedlist) | validateAndBox(List<?> arg, SchemaConfiguration configuration) |
| @Nullable Object | validate(@Nullable Object arg, SchemaConfiguration configuration) |
## DatetimeBoxed
public static abstract sealed class DatetimeBoxed<br>
permits<br>
[DatetimeBoxedVoid](#datetimeboxedvoid),
[DatetimeBoxedBoolean](#datetimeboxedboolean),
[DatetimeBoxedNumber](#datetimeboxednumber),
[DatetimeBoxedString](#datetimeboxedstring),
[DatetimeBoxedList](#datetimeboxedlist),
[DatetimeBoxedMap](#datetimeboxedmap)

abstract sealed class that stores validated payloads using boxed classes

## DatetimeBoxedVoid
public static final class DatetimeBoxedVoid<br>
extends [DatetimeBoxed](#datetimeboxed)

a boxed class to store validated null payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| DatetimeBoxedVoid(Void data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Void | data<br>validated payload |

## DatetimeBoxedBoolean
public static final class DatetimeBoxedBoolean<br>
extends [DatetimeBoxed](#datetimeboxed)

a boxed class to store validated boolean payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| DatetimeBoxedBoolean(boolean data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| boolean | data<br>validated payload |

## DatetimeBoxedNumber
public static final class DatetimeBoxedNumber<br>
extends [DatetimeBoxed](#datetimeboxed)

a boxed class to store validated Number payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| DatetimeBoxedNumber(Number data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Number | data<br>validated payload |

## DatetimeBoxedString
public static final class DatetimeBoxedString<br>
extends [DatetimeBoxed](#datetimeboxed)

a boxed class to store validated String payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| DatetimeBoxedString(String data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| String | data<br>validated payload |

## DatetimeBoxedList
public static final class DatetimeBoxedList<br>
extends [DatetimeBoxed](#datetimeboxed)

a boxed class to store validated List payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| DatetimeBoxedList(FrozenList<@Nullable Object> data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| FrozenList<@Nullable Object> | data<br>validated payload |

## DatetimeBoxedMap
public static final class DatetimeBoxedMap<br>
extends [DatetimeBoxed](#datetimeboxed)

a boxed class to store validated Map payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| DatetimeBoxedMap(FrozenMap<@Nullable Object> data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| FrozenMap<@Nullable Object> | data<br>validated payload |

## Datetime
public static class Datetime<br>
extends JsonSchema

A schema class that validates payloads

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| String | type = "date-time"; |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| String | validate(String arg, SchemaConfiguration configuration) |
| Void | validate(Void arg, SchemaConfiguration configuration) |
| int | validate(int arg, SchemaConfiguration configuration) |
| long | validate(long arg, SchemaConfiguration configuration) |
| float | validate(float arg, SchemaConfiguration configuration) |
| double | validate(double arg, SchemaConfiguration configuration) |
| Number | validate(Number arg, SchemaConfiguration configuration) |
| boolean | validate(boolean arg, SchemaConfiguration configuration) |
| FrozenMap<@Nullable Object> | validate(Map&lt;?, ?&gt; arg, SchemaConfiguration configuration) |
| FrozenList<@Nullable Object> | validate(List<?> arg, SchemaConfiguration configuration) |
| [DatetimeBoxedString](#datetimeboxedstring) | validateAndBox(String arg, SchemaConfiguration configuration) |
| [DatetimeBoxedVoid](#datetimeboxedvoid) | validateAndBox(Void arg, SchemaConfiguration configuration) |
| [DatetimeBoxedNumber](#datetimeboxednumber) | validateAndBox(Number arg, SchemaConfiguration configuration) |
| [DatetimeBoxedBoolean](#datetimeboxedboolean) | validateAndBox(boolean arg, SchemaConfiguration configuration) |
| [DatetimeBoxedMap](#datetimeboxedmap) | validateAndBox(Map&lt;?, ?&gt; arg, SchemaConfiguration configuration) |
| [DatetimeBoxedList](#datetimeboxedlist) | validateAndBox(List<?> arg, SchemaConfiguration configuration) |
| @Nullable Object | validate(@Nullable Object arg, SchemaConfiguration configuration) |
## DateBoxed
public static abstract sealed class DateBoxed<br>
permits<br>
[DateBoxedVoid](#dateboxedvoid),
[DateBoxedBoolean](#dateboxedboolean),
[DateBoxedNumber](#dateboxednumber),
[DateBoxedString](#dateboxedstring),
[DateBoxedList](#dateboxedlist),
[DateBoxedMap](#dateboxedmap)

abstract sealed class that stores validated payloads using boxed classes

## DateBoxedVoid
public static final class DateBoxedVoid<br>
extends [DateBoxed](#dateboxed)

a boxed class to store validated null payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| DateBoxedVoid(Void data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Void | data<br>validated payload |

## DateBoxedBoolean
public static final class DateBoxedBoolean<br>
extends [DateBoxed](#dateboxed)

a boxed class to store validated boolean payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| DateBoxedBoolean(boolean data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| boolean | data<br>validated payload |

## DateBoxedNumber
public static final class DateBoxedNumber<br>
extends [DateBoxed](#dateboxed)

a boxed class to store validated Number payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| DateBoxedNumber(Number data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Number | data<br>validated payload |

## DateBoxedString
public static final class DateBoxedString<br>
extends [DateBoxed](#dateboxed)

a boxed class to store validated String payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| DateBoxedString(String data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| String | data<br>validated payload |

## DateBoxedList
public static final class DateBoxedList<br>
extends [DateBoxed](#dateboxed)

a boxed class to store validated List payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| DateBoxedList(FrozenList<@Nullable Object> data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| FrozenList<@Nullable Object> | data<br>validated payload |

## DateBoxedMap
public static final class DateBoxedMap<br>
extends [DateBoxed](#dateboxed)

a boxed class to store validated Map payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| DateBoxedMap(FrozenMap<@Nullable Object> data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| FrozenMap<@Nullable Object> | data<br>validated payload |

## Date
public static class Date<br>
extends JsonSchema

A schema class that validates payloads

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| String | type = "date"; |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| String | validate(String arg, SchemaConfiguration configuration) |
| Void | validate(Void arg, SchemaConfiguration configuration) |
| int | validate(int arg, SchemaConfiguration configuration) |
| long | validate(long arg, SchemaConfiguration configuration) |
| float | validate(float arg, SchemaConfiguration configuration) |
| double | validate(double arg, SchemaConfiguration configuration) |
| Number | validate(Number arg, SchemaConfiguration configuration) |
| boolean | validate(boolean arg, SchemaConfiguration configuration) |
| FrozenMap<@Nullable Object> | validate(Map&lt;?, ?&gt; arg, SchemaConfiguration configuration) |
| FrozenList<@Nullable Object> | validate(List<?> arg, SchemaConfiguration configuration) |
| [DateBoxedString](#dateboxedstring) | validateAndBox(String arg, SchemaConfiguration configuration) |
| [DateBoxedVoid](#dateboxedvoid) | validateAndBox(Void arg, SchemaConfiguration configuration) |
| [DateBoxedNumber](#dateboxednumber) | validateAndBox(Number arg, SchemaConfiguration configuration) |
| [DateBoxedBoolean](#dateboxedboolean) | validateAndBox(boolean arg, SchemaConfiguration configuration) |
| [DateBoxedMap](#dateboxedmap) | validateAndBox(Map&lt;?, ?&gt; arg, SchemaConfiguration configuration) |
| [DateBoxedList](#dateboxedlist) | validateAndBox(List<?> arg, SchemaConfiguration configuration) |
| @Nullable Object | validate(@Nullable Object arg, SchemaConfiguration configuration) |
## UuidSchemaBoxed
public static abstract sealed class UuidSchemaBoxed<br>
permits<br>
[UuidSchemaBoxedVoid](#uuidschemaboxedvoid),
[UuidSchemaBoxedBoolean](#uuidschemaboxedboolean),
[UuidSchemaBoxedNumber](#uuidschemaboxednumber),
[UuidSchemaBoxedString](#uuidschemaboxedstring),
[UuidSchemaBoxedList](#uuidschemaboxedlist),
[UuidSchemaBoxedMap](#uuidschemaboxedmap)

abstract sealed class that stores validated payloads using boxed classes

## UuidSchemaBoxedVoid
public static final class UuidSchemaBoxedVoid<br>
extends [UuidSchemaBoxed](#uuidschemaboxed)

a boxed class to store validated null payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| UuidSchemaBoxedVoid(Void data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Void | data<br>validated payload |

## UuidSchemaBoxedBoolean
public static final class UuidSchemaBoxedBoolean<br>
extends [UuidSchemaBoxed](#uuidschemaboxed)

a boxed class to store validated boolean payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| UuidSchemaBoxedBoolean(boolean data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| boolean | data<br>validated payload |

## UuidSchemaBoxedNumber
public static final class UuidSchemaBoxedNumber<br>
extends [UuidSchemaBoxed](#uuidschemaboxed)

a boxed class to store validated Number payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| UuidSchemaBoxedNumber(Number data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Number | data<br>validated payload |

## UuidSchemaBoxedString
public static final class UuidSchemaBoxedString<br>
extends [UuidSchemaBoxed](#uuidschemaboxed)

a boxed class to store validated String payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| UuidSchemaBoxedString(String data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| String | data<br>validated payload |

## UuidSchemaBoxedList
public static final class UuidSchemaBoxedList<br>
extends [UuidSchemaBoxed](#uuidschemaboxed)

a boxed class to store validated List payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| UuidSchemaBoxedList(FrozenList<@Nullable Object> data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| FrozenList<@Nullable Object> | data<br>validated payload |

## UuidSchemaBoxedMap
public static final class UuidSchemaBoxedMap<br>
extends [UuidSchemaBoxed](#uuidschemaboxed)

a boxed class to store validated Map payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| UuidSchemaBoxedMap(FrozenMap<@Nullable Object> data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| FrozenMap<@Nullable Object> | data<br>validated payload |

## UuidSchema
public static class UuidSchema<br>
extends JsonSchema

A schema class that validates payloads

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| String | type = "uuid"; |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| String | validate(String arg, SchemaConfiguration configuration) |
| Void | validate(Void arg, SchemaConfiguration configuration) |
| int | validate(int arg, SchemaConfiguration configuration) |
| long | validate(long arg, SchemaConfiguration configuration) |
| float | validate(float arg, SchemaConfiguration configuration) |
| double | validate(double arg, SchemaConfiguration configuration) |
| Number | validate(Number arg, SchemaConfiguration configuration) |
| boolean | validate(boolean arg, SchemaConfiguration configuration) |
| FrozenMap<@Nullable Object> | validate(Map&lt;?, ?&gt; arg, SchemaConfiguration configuration) |
| FrozenList<@Nullable Object> | validate(List<?> arg, SchemaConfiguration configuration) |
| [UuidSchemaBoxedString](#uuidschemaboxedstring) | validateAndBox(String arg, SchemaConfiguration configuration) |
| [UuidSchemaBoxedVoid](#uuidschemaboxedvoid) | validateAndBox(Void arg, SchemaConfiguration configuration) |
| [UuidSchemaBoxedNumber](#uuidschemaboxednumber) | validateAndBox(Number arg, SchemaConfiguration configuration) |
| [UuidSchemaBoxedBoolean](#uuidschemaboxedboolean) | validateAndBox(boolean arg, SchemaConfiguration configuration) |
| [UuidSchemaBoxedMap](#uuidschemaboxedmap) | validateAndBox(Map&lt;?, ?&gt; arg, SchemaConfiguration configuration) |
| [UuidSchemaBoxedList](#uuidschemaboxedlist) | validateAndBox(List<?> arg, SchemaConfiguration configuration) |
| @Nullable Object | validate(@Nullable Object arg, SchemaConfiguration configuration) |
[[Back to top]](#top) [[Back to Component Schemas]](../../../README.md#Component-Schemas) [[Back to README]](../../../README.md)
