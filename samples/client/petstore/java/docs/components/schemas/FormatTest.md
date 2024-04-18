# FormatTest
org.openapijsonschematools.client.components.schemas.FormatTest.java
public class FormatTest<br>

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
| sealed interface | [FormatTest.FormatTest1Boxed](#formattest1boxed)<br> sealed interface for validated payloads |
| record | [FormatTest.FormatTest1BoxedMap](#formattest1boxedmap)<br> boxed class to store validated Map payloads |
| static class | [FormatTest.FormatTest1](#formattest1)<br> schema class |
| static class | [FormatTest.FormatTestMapBuilder](#formattestmapbuilder)<br> builder for Map payloads |
| static class | [FormatTest.FormatTestMap](#formattestmap)<br> output class for Map payloads |
| sealed interface | [FormatTest.NonePropBoxed](#nonepropboxed)<br> sealed interface for validated payloads |
| record | [FormatTest.NonePropBoxedVoid](#nonepropboxedvoid)<br> boxed class to store validated null payloads |
| static class | [FormatTest.NoneProp](#noneprop)<br> schema class |
| sealed interface | [FormatTest.PatternWithDigitsAndDelimiterBoxed](#patternwithdigitsanddelimiterboxed)<br> sealed interface for validated payloads |
| record | [FormatTest.PatternWithDigitsAndDelimiterBoxedString](#patternwithdigitsanddelimiterboxedstring)<br> boxed class to store validated String payloads |
| static class | [FormatTest.PatternWithDigitsAndDelimiter](#patternwithdigitsanddelimiter)<br> schema class |
| sealed interface | [FormatTest.PatternWithDigitsBoxed](#patternwithdigitsboxed)<br> sealed interface for validated payloads |
| record | [FormatTest.PatternWithDigitsBoxedString](#patternwithdigitsboxedstring)<br> boxed class to store validated String payloads |
| static class | [FormatTest.PatternWithDigits](#patternwithdigits)<br> schema class |
| sealed interface | [FormatTest.PasswordBoxed](#passwordboxed)<br> sealed interface for validated payloads |
| record | [FormatTest.PasswordBoxedString](#passwordboxedstring)<br> boxed class to store validated String payloads |
| static class | [FormatTest.Password](#password)<br> schema class |
| sealed interface | [FormatTest.UuidNoExampleBoxed](#uuidnoexampleboxed)<br> sealed interface for validated payloads |
| record | [FormatTest.UuidNoExampleBoxedString](#uuidnoexampleboxedstring)<br> boxed class to store validated String payloads |
| static class | [FormatTest.UuidNoExample](#uuidnoexample)<br> schema class |
| sealed interface | [FormatTest.UuidSchemaBoxed](#uuidschemaboxed)<br> sealed interface for validated payloads |
| record | [FormatTest.UuidSchemaBoxedString](#uuidschemaboxedstring)<br> boxed class to store validated String payloads |
| static class | [FormatTest.UuidSchema](#uuidschema)<br> schema class |
| sealed interface | [FormatTest.DateTimeBoxed](#datetimeboxed)<br> sealed interface for validated payloads |
| record | [FormatTest.DateTimeBoxedString](#datetimeboxedstring)<br> boxed class to store validated String payloads |
| static class | [FormatTest.DateTime](#datetime)<br> schema class |
| sealed interface | [FormatTest.DateBoxed](#dateboxed)<br> sealed interface for validated payloads |
| record | [FormatTest.DateBoxedString](#dateboxedstring)<br> boxed class to store validated String payloads |
| static class | [FormatTest.Date](#date)<br> schema class |
| sealed interface | [FormatTest.BinaryBoxed](#binaryboxed)<br> sealed interface for validated payloads |
| static class | [FormatTest.Binary](#binary)<br> schema class |
| sealed interface | [FormatTest.ByteSchemaBoxed](#byteschemaboxed)<br> sealed interface for validated payloads |
| record | [FormatTest.ByteSchemaBoxedString](#byteschemaboxedstring)<br> boxed class to store validated String payloads |
| static class | [FormatTest.ByteSchema](#byteschema)<br> schema class |
| sealed interface | [FormatTest.StringSchemaBoxed](#stringschemaboxed)<br> sealed interface for validated payloads |
| record | [FormatTest.StringSchemaBoxedString](#stringschemaboxedstring)<br> boxed class to store validated String payloads |
| static class | [FormatTest.StringSchema](#stringschema)<br> schema class |
| sealed interface | [FormatTest.ArrayWithUniqueItemsBoxed](#arraywithuniqueitemsboxed)<br> sealed interface for validated payloads |
| record | [FormatTest.ArrayWithUniqueItemsBoxedList](#arraywithuniqueitemsboxedlist)<br> boxed class to store validated List payloads |
| static class | [FormatTest.ArrayWithUniqueItems](#arraywithuniqueitems)<br> schema class |
| static class | [FormatTest.ArrayWithUniqueItemsListBuilder](#arraywithuniqueitemslistbuilder)<br> builder for List payloads |
| static class | [FormatTest.ArrayWithUniqueItemsList](#arraywithuniqueitemslist)<br> output class for List payloads |
| sealed interface | [FormatTest.ItemsBoxed](#itemsboxed)<br> sealed interface for validated payloads |
| record | [FormatTest.ItemsBoxedNumber](#itemsboxednumber)<br> boxed class to store validated Number payloads |
| static class | [FormatTest.Items](#items)<br> schema class |
| sealed interface | [FormatTest.Float64Boxed](#float64boxed)<br> sealed interface for validated payloads |
| record | [FormatTest.Float64BoxedNumber](#float64boxednumber)<br> boxed class to store validated Number payloads |
| static class | [FormatTest.Float64](#float64)<br> schema class |
| sealed interface | [FormatTest.DoubleSchemaBoxed](#doubleschemaboxed)<br> sealed interface for validated payloads |
| record | [FormatTest.DoubleSchemaBoxedNumber](#doubleschemaboxednumber)<br> boxed class to store validated Number payloads |
| static class | [FormatTest.DoubleSchema](#doubleschema)<br> schema class |
| sealed interface | [FormatTest.Float32Boxed](#float32boxed)<br> sealed interface for validated payloads |
| record | [FormatTest.Float32BoxedNumber](#float32boxednumber)<br> boxed class to store validated Number payloads |
| static class | [FormatTest.Float32](#float32)<br> schema class |
| sealed interface | [FormatTest.FloatSchemaBoxed](#floatschemaboxed)<br> sealed interface for validated payloads |
| record | [FormatTest.FloatSchemaBoxedNumber](#floatschemaboxednumber)<br> boxed class to store validated Number payloads |
| static class | [FormatTest.FloatSchema](#floatschema)<br> schema class |
| sealed interface | [FormatTest.NumberSchemaBoxed](#numberschemaboxed)<br> sealed interface for validated payloads |
| record | [FormatTest.NumberSchemaBoxedNumber](#numberschemaboxednumber)<br> boxed class to store validated Number payloads |
| static class | [FormatTest.NumberSchema](#numberschema)<br> schema class |
| sealed interface | [FormatTest.Int64Boxed](#int64boxed)<br> sealed interface for validated payloads |
| record | [FormatTest.Int64BoxedNumber](#int64boxednumber)<br> boxed class to store validated Number payloads |
| static class | [FormatTest.Int64](#int64)<br> schema class |
| sealed interface | [FormatTest.Int32withValidationsBoxed](#int32withvalidationsboxed)<br> sealed interface for validated payloads |
| record | [FormatTest.Int32withValidationsBoxedNumber](#int32withvalidationsboxednumber)<br> boxed class to store validated Number payloads |
| static class | [FormatTest.Int32withValidations](#int32withvalidations)<br> schema class |
| sealed interface | [FormatTest.Int32Boxed](#int32boxed)<br> sealed interface for validated payloads |
| record | [FormatTest.Int32BoxedNumber](#int32boxednumber)<br> boxed class to store validated Number payloads |
| static class | [FormatTest.Int32](#int32)<br> schema class |
| sealed interface | [FormatTest.IntegerSchemaBoxed](#integerschemaboxed)<br> sealed interface for validated payloads |
| record | [FormatTest.IntegerSchemaBoxedNumber](#integerschemaboxednumber)<br> boxed class to store validated Number payloads |
| static class | [FormatTest.IntegerSchema](#integerschema)<br> schema class |

## FormatTest1Boxed
public sealed interface FormatTest1Boxed<br>
permits<br>
[FormatTest1BoxedMap](#formattest1boxedmap)

sealed interface that stores validated payloads using boxed classes

## FormatTest1BoxedMap
public record FormatTest1BoxedMap<br>
implements [FormatTest1Boxed](#formattest1boxed)

record that stores validated Map payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| FormatTest1BoxedMap([FormatTestMap](#formattestmap) data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| [FormatTestMap](#formattestmap) | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## FormatTest1
public static class FormatTest1<br>
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
import org.openapijsonschematools.client.components.schemas.FormatTest;

import java.util.Arrays;
import java.util.List;
import java.util.AbstractMap;

static final SchemaConfiguration configuration = new SchemaConfiguration(new JsonSchemaKeywordFlags.Builder().build());

// Map validation
FormatTest.FormatTestMap validatedPayload =
    FormatTest.FormatTest1.validate(
    new FormatTest.FormatTestMapBuilder()
        .setByte("a")

        .date("2020-12-13")

        .setNumber(1)

        .password("a")

        .setInteger(1)

        .int32(1)

        .int32withValidations(1)

        .int64(1L)

        .setFloat(3.14f)

        .float32(3.14f)

        .setDouble(3.14d)

        .float64(3.14d)

        .arrayWithUniqueItems(
            Arrays.asList(
                1
            )
        )
        .setString("A")

        .binary("a")

        .dateTime("1970-01-01T00:00:00.00Z")

        .setUuid("046b6c7f-0b8a-43b9-b35d-6489e6daee91")

        .uuidNoExample("046b6c7f-0b8a-43b9-b35d-6489e6daee91")

        .pattern_with_digits("0480728880")

        .pattern_with_digits_and_delimiter("IMage_88")

        .noneProp(null)

    .build(),
    configuration
);
```

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Set<Class<?>> | type = Set.of(Map.class) |
| Map<String, Class<? extends JsonSchema>> | properties = Map.ofEntries(<br>&nbsp;&nbsp;&nbsp;&nbsp;new PropertyEntry("integer", [IntegerSchema.class](#integerschema))),<br>&nbsp;&nbsp;&nbsp;&nbsp;new PropertyEntry("int32", [Int32.class](#int32))),<br>&nbsp;&nbsp;&nbsp;&nbsp;new PropertyEntry("int32withValidations", [Int32withValidations.class](#int32withvalidations))),<br>&nbsp;&nbsp;&nbsp;&nbsp;new PropertyEntry("int64", [Int64.class](#int64))),<br>&nbsp;&nbsp;&nbsp;&nbsp;new PropertyEntry("number", [NumberSchema.class](#numberschema))),<br>&nbsp;&nbsp;&nbsp;&nbsp;new PropertyEntry("float", [FloatSchema.class](#floatschema))),<br>&nbsp;&nbsp;&nbsp;&nbsp;new PropertyEntry("float32", [Float32.class](#float32))),<br>&nbsp;&nbsp;&nbsp;&nbsp;new PropertyEntry("double", [DoubleSchema.class](#doubleschema))),<br>&nbsp;&nbsp;&nbsp;&nbsp;new PropertyEntry("float64", [Float64.class](#float64))),<br>&nbsp;&nbsp;&nbsp;&nbsp;new PropertyEntry("arrayWithUniqueItems", [ArrayWithUniqueItems.class](#arraywithuniqueitems))),<br>&nbsp;&nbsp;&nbsp;&nbsp;new PropertyEntry("string", [StringSchema.class](#stringschema))),<br>&nbsp;&nbsp;&nbsp;&nbsp;new PropertyEntry("byte", [ByteSchema.class](#byteschema))),<br>&nbsp;&nbsp;&nbsp;&nbsp;new PropertyEntry("binary", [Binary.class](#binary))),<br>&nbsp;&nbsp;&nbsp;&nbsp;new PropertyEntry("date", [Date.class](#date))),<br>&nbsp;&nbsp;&nbsp;&nbsp;new PropertyEntry("dateTime", [DateTime.class](#datetime))),<br>&nbsp;&nbsp;&nbsp;&nbsp;new PropertyEntry("uuid", [UuidSchema.class](#uuidschema))),<br>&nbsp;&nbsp;&nbsp;&nbsp;new PropertyEntry("uuidNoExample", [UuidNoExample.class](#uuidnoexample))),<br>&nbsp;&nbsp;&nbsp;&nbsp;new PropertyEntry("password", [Password.class](#password))),<br>&nbsp;&nbsp;&nbsp;&nbsp;new PropertyEntry("pattern_with_digits", [PatternWithDigits.class](#patternwithdigits))),<br>&nbsp;&nbsp;&nbsp;&nbsp;new PropertyEntry("pattern_with_digits_and_delimiter", [PatternWithDigitsAndDelimiter.class](#patternwithdigitsanddelimiter))),<br>&nbsp;&nbsp;&nbsp;&nbsp;new PropertyEntry("noneProp", [NoneProp.class](#noneprop)))<br>)<br> |
| Set<String> | required = Set.of(<br>&nbsp;&nbsp;&nbsp;&nbsp;"byte",<br>&nbsp;&nbsp;&nbsp;&nbsp;"date",<br>&nbsp;&nbsp;&nbsp;&nbsp;"number",<br>&nbsp;&nbsp;&nbsp;&nbsp;"password"<br>)<br> |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| [FormatTestMap](#formattestmap) | validate([Map&lt;?, ?&gt;](#formattestmapbuilder) arg, SchemaConfiguration configuration) |
| [FormatTest1BoxedMap](#formattest1boxedmap) | validateAndBox([Map&lt;?, ?&gt;](#formattestmapbuilder) arg, SchemaConfiguration configuration) |
| [FormatTest1Boxed](#formattest1boxed) | validateAndBox(@Nullable Object arg, SchemaConfiguration configuration) |
| @Nullable Object | validate(@Nullable Object arg, SchemaConfiguration configuration) |

## FormatTestMap0000Builder
public class FormatTestMap0000Builder<br>
builder for `Map<String, @Nullable Object>`

A class that builds the Map input type

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| FormatTestMap0000Builder(Map<String, @Nullable Object> instance)<br>Creates a builder that contains the passed instance |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| Map<String, @Nullable Object> | build()<br>Returns map input that should be used with Schema.validate |
| [FormatTestMap0000Builder](#formattestmap0000builder) | setInteger(int value) |
| [FormatTestMap0000Builder](#formattestmap0000builder) | setInteger(float value) |
| [FormatTestMap0000Builder](#formattestmap0000builder) | setInteger(long value) |
| [FormatTestMap0000Builder](#formattestmap0000builder) | setInteger(double value) |
| [FormatTestMap0000Builder](#formattestmap0000builder) | int32(int value) |
| [FormatTestMap0000Builder](#formattestmap0000builder) | int32(float value) |
| [FormatTestMap0000Builder](#formattestmap0000builder) | int32withValidations(int value) |
| [FormatTestMap0000Builder](#formattestmap0000builder) | int32withValidations(float value) |
| [FormatTestMap0000Builder](#formattestmap0000builder) | int64(int value) |
| [FormatTestMap0000Builder](#formattestmap0000builder) | int64(float value) |
| [FormatTestMap0000Builder](#formattestmap0000builder) | int64(long value) |
| [FormatTestMap0000Builder](#formattestmap0000builder) | int64(double value) |
| [FormatTestMap0000Builder](#formattestmap0000builder) | setFloat(int value) |
| [FormatTestMap0000Builder](#formattestmap0000builder) | setFloat(float value) |
| [FormatTestMap0000Builder](#formattestmap0000builder) | setFloat(long value) |
| [FormatTestMap0000Builder](#formattestmap0000builder) | setFloat(double value) |
| [FormatTestMap0000Builder](#formattestmap0000builder) | float32(int value) |
| [FormatTestMap0000Builder](#formattestmap0000builder) | float32(float value) |
| [FormatTestMap0000Builder](#formattestmap0000builder) | float32(long value) |
| [FormatTestMap0000Builder](#formattestmap0000builder) | float32(double value) |
| [FormatTestMap0000Builder](#formattestmap0000builder) | setDouble(int value) |
| [FormatTestMap0000Builder](#formattestmap0000builder) | setDouble(float value) |
| [FormatTestMap0000Builder](#formattestmap0000builder) | setDouble(long value) |
| [FormatTestMap0000Builder](#formattestmap0000builder) | setDouble(double value) |
| [FormatTestMap0000Builder](#formattestmap0000builder) | float64(int value) |
| [FormatTestMap0000Builder](#formattestmap0000builder) | float64(float value) |
| [FormatTestMap0000Builder](#formattestmap0000builder) | float64(long value) |
| [FormatTestMap0000Builder](#formattestmap0000builder) | float64(double value) |
| [FormatTestMap0000Builder](#formattestmap0000builder) | arrayWithUniqueItems(List<Number> value) |
| [FormatTestMap0000Builder](#formattestmap0000builder) | setString(String value) |
| [FormatTestMap0000Builder](#formattestmap0000builder) | binary(String value) |
| [FormatTestMap0000Builder](#formattestmap0000builder) | dateTime(String value) |
| [FormatTestMap0000Builder](#formattestmap0000builder) | setUuid(String value) |
| [FormatTestMap0000Builder](#formattestmap0000builder) | uuidNoExample(String value) |
| [FormatTestMap0000Builder](#formattestmap0000builder) | pattern_with_digits(String value) |
| [FormatTestMap0000Builder](#formattestmap0000builder) | pattern_with_digits_and_delimiter(String value) |
| [FormatTestMap0000Builder](#formattestmap0000builder) | noneProp(Void value) |
| [FormatTestMap0000Builder](#formattestmap0000builder) | additionalProperty(String key, Void value) |
| [FormatTestMap0000Builder](#formattestmap0000builder) | additionalProperty(String key, boolean value) |
| [FormatTestMap0000Builder](#formattestmap0000builder) | additionalProperty(String key, String value) |
| [FormatTestMap0000Builder](#formattestmap0000builder) | additionalProperty(String key, int value) |
| [FormatTestMap0000Builder](#formattestmap0000builder) | additionalProperty(String key, float value) |
| [FormatTestMap0000Builder](#formattestmap0000builder) | additionalProperty(String key, long value) |
| [FormatTestMap0000Builder](#formattestmap0000builder) | additionalProperty(String key, double value) |
| [FormatTestMap0000Builder](#formattestmap0000builder) | additionalProperty(String key, List<?> value) |
| [FormatTestMap0000Builder](#formattestmap0000builder) | additionalProperty(String key, Map<String, ?> value) |

## FormatTestMap0001Builder
public class FormatTestMap0001Builder<br>
builder for `Map<String, @Nullable Object>`

A class that builds the Map input type

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| FormatTestMap0001Builder(Map<String, @Nullable Object> instance)<br>Creates a builder that contains the passed instance |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| [FormatTestMap0000Builder](#formattestmap0000builder) | password(String value) |

## FormatTestMap0010Builder
public class FormatTestMap0010Builder<br>
builder for `Map<String, @Nullable Object>`

A class that builds the Map input type

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| FormatTestMap0010Builder(Map<String, @Nullable Object> instance)<br>Creates a builder that contains the passed instance |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| [FormatTestMap0000Builder](#formattestmap0000builder) | setNumber(int value) |
| [FormatTestMap0000Builder](#formattestmap0000builder) | setNumber(float value) |
| [FormatTestMap0000Builder](#formattestmap0000builder) | setNumber(long value) |
| [FormatTestMap0000Builder](#formattestmap0000builder) | setNumber(double value) |

## FormatTestMap0011Builder
public class FormatTestMap0011Builder<br>
builder for `Map<String, @Nullable Object>`

A class that builds the Map input type

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| FormatTestMap0011Builder(Map<String, @Nullable Object> instance)<br>Creates a builder that contains the passed instance |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| [FormatTestMap0001Builder](#formattestmap0001builder) | setNumber(int value) |
| [FormatTestMap0001Builder](#formattestmap0001builder) | setNumber(float value) |
| [FormatTestMap0001Builder](#formattestmap0001builder) | setNumber(long value) |
| [FormatTestMap0001Builder](#formattestmap0001builder) | setNumber(double value) |
| [FormatTestMap0010Builder](#formattestmap0010builder) | password(String value) |

## FormatTestMap0100Builder
public class FormatTestMap0100Builder<br>
builder for `Map<String, @Nullable Object>`

A class that builds the Map input type

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| FormatTestMap0100Builder(Map<String, @Nullable Object> instance)<br>Creates a builder that contains the passed instance |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| [FormatTestMap0000Builder](#formattestmap0000builder) | date(String value) |

## FormatTestMap0101Builder
public class FormatTestMap0101Builder<br>
builder for `Map<String, @Nullable Object>`

A class that builds the Map input type

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| FormatTestMap0101Builder(Map<String, @Nullable Object> instance)<br>Creates a builder that contains the passed instance |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| [FormatTestMap0001Builder](#formattestmap0001builder) | date(String value) |
| [FormatTestMap0100Builder](#formattestmap0100builder) | password(String value) |

## FormatTestMap0110Builder
public class FormatTestMap0110Builder<br>
builder for `Map<String, @Nullable Object>`

A class that builds the Map input type

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| FormatTestMap0110Builder(Map<String, @Nullable Object> instance)<br>Creates a builder that contains the passed instance |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| [FormatTestMap0010Builder](#formattestmap0010builder) | date(String value) |
| [FormatTestMap0100Builder](#formattestmap0100builder) | setNumber(int value) |
| [FormatTestMap0100Builder](#formattestmap0100builder) | setNumber(float value) |
| [FormatTestMap0100Builder](#formattestmap0100builder) | setNumber(long value) |
| [FormatTestMap0100Builder](#formattestmap0100builder) | setNumber(double value) |

## FormatTestMap0111Builder
public class FormatTestMap0111Builder<br>
builder for `Map<String, @Nullable Object>`

A class that builds the Map input type

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| FormatTestMap0111Builder(Map<String, @Nullable Object> instance)<br>Creates a builder that contains the passed instance |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| [FormatTestMap0011Builder](#formattestmap0011builder) | date(String value) |
| [FormatTestMap0101Builder](#formattestmap0101builder) | setNumber(int value) |
| [FormatTestMap0101Builder](#formattestmap0101builder) | setNumber(float value) |
| [FormatTestMap0101Builder](#formattestmap0101builder) | setNumber(long value) |
| [FormatTestMap0101Builder](#formattestmap0101builder) | setNumber(double value) |
| [FormatTestMap0110Builder](#formattestmap0110builder) | password(String value) |

## FormatTestMap1000Builder
public class FormatTestMap1000Builder<br>
builder for `Map<String, @Nullable Object>`

A class that builds the Map input type

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| FormatTestMap1000Builder(Map<String, @Nullable Object> instance)<br>Creates a builder that contains the passed instance |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| [FormatTestMap0000Builder](#formattestmap0000builder) | setByte(String value) |

## FormatTestMap1001Builder
public class FormatTestMap1001Builder<br>
builder for `Map<String, @Nullable Object>`

A class that builds the Map input type

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| FormatTestMap1001Builder(Map<String, @Nullable Object> instance)<br>Creates a builder that contains the passed instance |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| [FormatTestMap0001Builder](#formattestmap0001builder) | setByte(String value) |
| [FormatTestMap1000Builder](#formattestmap1000builder) | password(String value) |

## FormatTestMap1010Builder
public class FormatTestMap1010Builder<br>
builder for `Map<String, @Nullable Object>`

A class that builds the Map input type

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| FormatTestMap1010Builder(Map<String, @Nullable Object> instance)<br>Creates a builder that contains the passed instance |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| [FormatTestMap0010Builder](#formattestmap0010builder) | setByte(String value) |
| [FormatTestMap1000Builder](#formattestmap1000builder) | setNumber(int value) |
| [FormatTestMap1000Builder](#formattestmap1000builder) | setNumber(float value) |
| [FormatTestMap1000Builder](#formattestmap1000builder) | setNumber(long value) |
| [FormatTestMap1000Builder](#formattestmap1000builder) | setNumber(double value) |

## FormatTestMap1011Builder
public class FormatTestMap1011Builder<br>
builder for `Map<String, @Nullable Object>`

A class that builds the Map input type

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| FormatTestMap1011Builder(Map<String, @Nullable Object> instance)<br>Creates a builder that contains the passed instance |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| [FormatTestMap0011Builder](#formattestmap0011builder) | setByte(String value) |
| [FormatTestMap1001Builder](#formattestmap1001builder) | setNumber(int value) |
| [FormatTestMap1001Builder](#formattestmap1001builder) | setNumber(float value) |
| [FormatTestMap1001Builder](#formattestmap1001builder) | setNumber(long value) |
| [FormatTestMap1001Builder](#formattestmap1001builder) | setNumber(double value) |
| [FormatTestMap1010Builder](#formattestmap1010builder) | password(String value) |

## FormatTestMap1100Builder
public class FormatTestMap1100Builder<br>
builder for `Map<String, @Nullable Object>`

A class that builds the Map input type

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| FormatTestMap1100Builder(Map<String, @Nullable Object> instance)<br>Creates a builder that contains the passed instance |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| [FormatTestMap0100Builder](#formattestmap0100builder) | setByte(String value) |
| [FormatTestMap1000Builder](#formattestmap1000builder) | date(String value) |

## FormatTestMap1101Builder
public class FormatTestMap1101Builder<br>
builder for `Map<String, @Nullable Object>`

A class that builds the Map input type

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| FormatTestMap1101Builder(Map<String, @Nullable Object> instance)<br>Creates a builder that contains the passed instance |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| [FormatTestMap0101Builder](#formattestmap0101builder) | setByte(String value) |
| [FormatTestMap1001Builder](#formattestmap1001builder) | date(String value) |
| [FormatTestMap1100Builder](#formattestmap1100builder) | password(String value) |

## FormatTestMap1110Builder
public class FormatTestMap1110Builder<br>
builder for `Map<String, @Nullable Object>`

A class that builds the Map input type

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| FormatTestMap1110Builder(Map<String, @Nullable Object> instance)<br>Creates a builder that contains the passed instance |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| [FormatTestMap0110Builder](#formattestmap0110builder) | setByte(String value) |
| [FormatTestMap1010Builder](#formattestmap1010builder) | date(String value) |
| [FormatTestMap1100Builder](#formattestmap1100builder) | setNumber(int value) |
| [FormatTestMap1100Builder](#formattestmap1100builder) | setNumber(float value) |
| [FormatTestMap1100Builder](#formattestmap1100builder) | setNumber(long value) |
| [FormatTestMap1100Builder](#formattestmap1100builder) | setNumber(double value) |

## FormatTestMapBuilder
public class FormatTestMapBuilder<br>
builder for `Map<String, @Nullable Object>`

A class that builds the Map input type

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| FormatTestMapBuilder()<br>Creates a builder that contains an empty map |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| [FormatTestMap0111Builder](#formattestmap0111builder) | setByte(String value) |
| [FormatTestMap1011Builder](#formattestmap1011builder) | date(String value) |
| [FormatTestMap1101Builder](#formattestmap1101builder) | setNumber(int value) |
| [FormatTestMap1101Builder](#formattestmap1101builder) | setNumber(float value) |
| [FormatTestMap1101Builder](#formattestmap1101builder) | setNumber(long value) |
| [FormatTestMap1101Builder](#formattestmap1101builder) | setNumber(double value) |
| [FormatTestMap1110Builder](#formattestmap1110builder) | password(String value) |

## FormatTestMap
public static class FormatTestMap<br>
extends FrozenMap<String, @Nullable Object>

A class to store validated Map payloads

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| static [FormatTestMap](#formattestmap) | of([Map<String, ? extends @Nullable Object>](#formattestmapbuilder) arg, SchemaConfiguration configuration) |
| String | date()<br> value must conform to RFC-3339 full-date YYYY-MM-DD |
| String | password()<br> |
| Number | int32()<br>[optional] value must be a 32 bit integer |
| Number | int32withValidations()<br>[optional] value must be a 32 bit integer |
| Number | int64()<br>[optional] value must be a 64 bit integer |
| Number | float32()<br>[optional] value must be a 32 bit float |
| Number | float64()<br>[optional] value must be a 64 bit float |
| [ArrayWithUniqueItemsList](#arraywithuniqueitemslist) | arrayWithUniqueItems()<br>[optional] |
| String | binary()<br>[optional] |
| String | dateTime()<br>[optional] value must conform to RFC-3339 date-time |
| String | uuidNoExample()<br>[optional] value must be a uuid |
| String | pattern_with_digits()<br>[optional] |
| String | pattern_with_digits_and_delimiter()<br>[optional] |
| Void | noneProp()<br>[optional] |
| @Nullable Object | get(String key)<br>This schema has invalid Java names so this method must be used when you access instance["byte"], instance["number"], instance["integer"], instance["float"], instance["double"], instance["string"], instance["uuid"],  |
| @Nullable Object | getAdditionalProperty(String name)<br>provides type safety for additional properties |

## NonePropBoxed
public sealed interface NonePropBoxed<br>
permits<br>
[NonePropBoxedVoid](#nonepropboxedvoid)

sealed interface that stores validated payloads using boxed classes

## NonePropBoxedVoid
public record NonePropBoxedVoid<br>
implements [NonePropBoxed](#nonepropboxed)

record that stores validated null payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| NonePropBoxedVoid(Void data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| Void | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## NoneProp
public static class NoneProp<br>
extends NullJsonSchema.NullJsonSchema1

A schema class that validates payloads

| Methods Inherited from class org.openapijsonschematools.client.schemas.NullJsonSchema.NullJsonSchema1 |
| ------------------------------------------------------------------ |
| validate                                                           |
| validateAndBox                                                     |

## PatternWithDigitsAndDelimiterBoxed
public sealed interface PatternWithDigitsAndDelimiterBoxed<br>
permits<br>
[PatternWithDigitsAndDelimiterBoxedString](#patternwithdigitsanddelimiterboxedstring)

sealed interface that stores validated payloads using boxed classes

## PatternWithDigitsAndDelimiterBoxedString
public record PatternWithDigitsAndDelimiterBoxedString<br>
implements [PatternWithDigitsAndDelimiterBoxed](#patternwithdigitsanddelimiterboxed)

record that stores validated String payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| PatternWithDigitsAndDelimiterBoxedString(String data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| String | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## PatternWithDigitsAndDelimiter
public static class PatternWithDigitsAndDelimiter<br>
extends JsonSchema

A schema class that validates payloads

## Description
A string starting with &#x27;image_&#x27; (case insensitive) and one to three digits following i.e. Image_01.

### Code Sample
```
import org.openapijsonschematools.client.configurations.JsonSchemaKeywordFlags;
import org.openapijsonschematools.client.configurations.SchemaConfiguration;
import org.openapijsonschematools.client.exceptions.ValidationException;
import org.openapijsonschematools.client.schemas.validation.MapUtils;
import org.openapijsonschematools.client.schemas.validation.FrozenList;
import org.openapijsonschematools.client.schemas.validation.FrozenMap;
import org.openapijsonschematools.client.components.schemas.FormatTest;

import java.util.Arrays;
import java.util.List;
import java.util.AbstractMap;

static final SchemaConfiguration configuration = new SchemaConfiguration(new JsonSchemaKeywordFlags.Builder().build());

// String validation
String validatedPayload = FormatTest.PatternWithDigitsAndDelimiter.validate(
    "IMage_88",
    configuration
);
```

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Set<Class<?>> | type = Set.of(<br/>&nbsp;&nbsp;&nbsp;&nbsp;String.class<br/>)<br/> |
| Pattern | pattern = Pattern.compile(<br>&nbsp;&nbsp;&nbsp;&nbsp;"^image_\\d{1,3}$",<br>&nbsp;&nbsp;&nbsp;&nbsp;Pattern.CASE_INSENSITIVE<br>)<br> |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| String | validate(String arg, SchemaConfiguration configuration) |
| [PatternWithDigitsAndDelimiterBoxedString](#patternwithdigitsanddelimiterboxedstring) | validateAndBox(String arg, SchemaConfiguration configuration) |
| [PatternWithDigitsAndDelimiterBoxed](#patternwithdigitsanddelimiterboxed) | validateAndBox(@Nullable Object arg, SchemaConfiguration configuration) |
| @Nullable Object | validate(@Nullable Object arg, SchemaConfiguration configuration) |

## PatternWithDigitsBoxed
public sealed interface PatternWithDigitsBoxed<br>
permits<br>
[PatternWithDigitsBoxedString](#patternwithdigitsboxedstring)

sealed interface that stores validated payloads using boxed classes

## PatternWithDigitsBoxedString
public record PatternWithDigitsBoxedString<br>
implements [PatternWithDigitsBoxed](#patternwithdigitsboxed)

record that stores validated String payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| PatternWithDigitsBoxedString(String data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| String | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## PatternWithDigits
public static class PatternWithDigits<br>
extends JsonSchema

A schema class that validates payloads

## Description
A string that is a 10 digit number. Can have leading zeros.

### Code Sample
```
import org.openapijsonschematools.client.configurations.JsonSchemaKeywordFlags;
import org.openapijsonschematools.client.configurations.SchemaConfiguration;
import org.openapijsonschematools.client.exceptions.ValidationException;
import org.openapijsonschematools.client.schemas.validation.MapUtils;
import org.openapijsonschematools.client.schemas.validation.FrozenList;
import org.openapijsonschematools.client.schemas.validation.FrozenMap;
import org.openapijsonschematools.client.components.schemas.FormatTest;

import java.util.Arrays;
import java.util.List;
import java.util.AbstractMap;

static final SchemaConfiguration configuration = new SchemaConfiguration(new JsonSchemaKeywordFlags.Builder().build());

// String validation
String validatedPayload = FormatTest.PatternWithDigits.validate(
    "0480728880",
    configuration
);
```

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Set<Class<?>> | type = Set.of(<br/>&nbsp;&nbsp;&nbsp;&nbsp;String.class<br/>)<br/> |
| Pattern | pattern = Pattern.compile(<br>&nbsp;&nbsp;&nbsp;&nbsp;"^\\d{10}$"<br>)<br> |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| String | validate(String arg, SchemaConfiguration configuration) |
| [PatternWithDigitsBoxedString](#patternwithdigitsboxedstring) | validateAndBox(String arg, SchemaConfiguration configuration) |
| [PatternWithDigitsBoxed](#patternwithdigitsboxed) | validateAndBox(@Nullable Object arg, SchemaConfiguration configuration) |
| @Nullable Object | validate(@Nullable Object arg, SchemaConfiguration configuration) |

## PasswordBoxed
public sealed interface PasswordBoxed<br>
permits<br>
[PasswordBoxedString](#passwordboxedstring)

sealed interface that stores validated payloads using boxed classes

## PasswordBoxedString
public record PasswordBoxedString<br>
implements [PasswordBoxed](#passwordboxed)

record that stores validated String payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| PasswordBoxedString(String data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| String | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## Password
public static class Password<br>
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
import org.openapijsonschematools.client.components.schemas.FormatTest;

import java.util.Arrays;
import java.util.List;
import java.util.AbstractMap;

static final SchemaConfiguration configuration = new SchemaConfiguration(new JsonSchemaKeywordFlags.Builder().build());

// String validation
String validatedPayload = FormatTest.Password.validate(
    "a",
    configuration
);
```

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Set<Class<?>> | type = Set.of(<br/>&nbsp;&nbsp;&nbsp;&nbsp;String.class<br/>)<br/> |
| String | type = "password"; |
| Integer | maxLength = 64 |
| Integer | minLength = 10 |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| String | validate(String arg, SchemaConfiguration configuration) |
| [PasswordBoxedString](#passwordboxedstring) | validateAndBox(String arg, SchemaConfiguration configuration) |
| [PasswordBoxed](#passwordboxed) | validateAndBox(@Nullable Object arg, SchemaConfiguration configuration) |
| @Nullable Object | validate(@Nullable Object arg, SchemaConfiguration configuration) |

## UuidNoExampleBoxed
public sealed interface UuidNoExampleBoxed<br>
permits<br>
[UuidNoExampleBoxedString](#uuidnoexampleboxedstring)

sealed interface that stores validated payloads using boxed classes

## UuidNoExampleBoxedString
public record UuidNoExampleBoxedString<br>
implements [UuidNoExampleBoxed](#uuidnoexampleboxed)

record that stores validated String payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| UuidNoExampleBoxedString(String data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| String | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## UuidNoExample
public static class UuidNoExample<br>
extends UuidJsonSchema.UuidJsonSchema1

A schema class that validates payloads

| Methods Inherited from class org.openapijsonschematools.client.schemas.UuidJsonSchema.UuidJsonSchema1 |
| ------------------------------------------------------------------ |
| validate                                                           |
| validateAndBox                                                     |

## UuidSchemaBoxed
public sealed interface UuidSchemaBoxed<br>
permits<br>
[UuidSchemaBoxedString](#uuidschemaboxedstring)

sealed interface that stores validated payloads using boxed classes

## UuidSchemaBoxedString
public record UuidSchemaBoxedString<br>
implements [UuidSchemaBoxed](#uuidschemaboxed)

record that stores validated String payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| UuidSchemaBoxedString(String data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| String | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## UuidSchema
public static class UuidSchema<br>
extends UuidJsonSchema.UuidJsonSchema1

A schema class that validates payloads

| Methods Inherited from class org.openapijsonschematools.client.schemas.UuidJsonSchema.UuidJsonSchema1 |
| ------------------------------------------------------------------ |
| validate                                                           |
| validateAndBox                                                     |

## DateTimeBoxed
public sealed interface DateTimeBoxed<br>
permits<br>
[DateTimeBoxedString](#datetimeboxedstring)

sealed interface that stores validated payloads using boxed classes

## DateTimeBoxedString
public record DateTimeBoxedString<br>
implements [DateTimeBoxed](#datetimeboxed)

record that stores validated String payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| DateTimeBoxedString(String data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| String | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## DateTime
public static class DateTime<br>
extends DateTimeJsonSchema.DateTimeJsonSchema1

A schema class that validates payloads

| Methods Inherited from class org.openapijsonschematools.client.schemas.DateTimeJsonSchema.DateTimeJsonSchema1 |
| ------------------------------------------------------------------ |
| validate                                                           |
| validateAndBox                                                     |

## DateBoxed
public sealed interface DateBoxed<br>
permits<br>
[DateBoxedString](#dateboxedstring)

sealed interface that stores validated payloads using boxed classes

## DateBoxedString
public record DateBoxedString<br>
implements [DateBoxed](#dateboxed)

record that stores validated String payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| DateBoxedString(String data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| String | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## Date
public static class Date<br>
extends DateJsonSchema.DateJsonSchema1

A schema class that validates payloads

| Methods Inherited from class org.openapijsonschematools.client.schemas.DateJsonSchema.DateJsonSchema1 |
| ------------------------------------------------------------------ |
| validate                                                           |
| validateAndBox                                                     |

## BinaryBoxed
public sealed interface BinaryBoxed<br>
permits<br>

sealed interface that stores validated payloads using boxed classes

## Binary
public static class Binary<br>
extends JsonSchema

A schema class that validates payloads

## ByteSchemaBoxed
public sealed interface ByteSchemaBoxed<br>
permits<br>
[ByteSchemaBoxedString](#byteschemaboxedstring)

sealed interface that stores validated payloads using boxed classes

## ByteSchemaBoxedString
public record ByteSchemaBoxedString<br>
implements [ByteSchemaBoxed](#byteschemaboxed)

record that stores validated String payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| ByteSchemaBoxedString(String data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| String | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## ByteSchema
public static class ByteSchema<br>
extends StringJsonSchema.StringJsonSchema1

A schema class that validates payloads

## StringSchemaBoxed
public sealed interface StringSchemaBoxed<br>
permits<br>
[StringSchemaBoxedString](#stringschemaboxedstring)

sealed interface that stores validated payloads using boxed classes

## StringSchemaBoxedString
public record StringSchemaBoxedString<br>
implements [StringSchemaBoxed](#stringschemaboxed)

record that stores validated String payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| StringSchemaBoxedString(String data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| String | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## StringSchema
public static class StringSchema<br>
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
import org.openapijsonschematools.client.components.schemas.FormatTest;

import java.util.Arrays;
import java.util.List;
import java.util.AbstractMap;

static final SchemaConfiguration configuration = new SchemaConfiguration(new JsonSchemaKeywordFlags.Builder().build());

// String validation
String validatedPayload = FormatTest.StringSchema.validate(
    "A",
    configuration
);
```

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Set<Class<?>> | type = Set.of(<br/>&nbsp;&nbsp;&nbsp;&nbsp;String.class<br/>)<br/> |
| Pattern | pattern = Pattern.compile(<br>&nbsp;&nbsp;&nbsp;&nbsp;"[a-z]",<br>&nbsp;&nbsp;&nbsp;&nbsp;Pattern.CASE_INSENSITIVE<br>)<br> |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| String | validate(String arg, SchemaConfiguration configuration) |
| [StringSchemaBoxedString](#stringschemaboxedstring) | validateAndBox(String arg, SchemaConfiguration configuration) |
| [StringSchemaBoxed](#stringschemaboxed) | validateAndBox(@Nullable Object arg, SchemaConfiguration configuration) |
| @Nullable Object | validate(@Nullable Object arg, SchemaConfiguration configuration) |

## ArrayWithUniqueItemsBoxed
public sealed interface ArrayWithUniqueItemsBoxed<br>
permits<br>
[ArrayWithUniqueItemsBoxedList](#arraywithuniqueitemsboxedlist)

sealed interface that stores validated payloads using boxed classes

## ArrayWithUniqueItemsBoxedList
public record ArrayWithUniqueItemsBoxedList<br>
implements [ArrayWithUniqueItemsBoxed](#arraywithuniqueitemsboxed)

record that stores validated List payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| ArrayWithUniqueItemsBoxedList([ArrayWithUniqueItemsList](#arraywithuniqueitemslist) data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| [ArrayWithUniqueItemsList](#arraywithuniqueitemslist) | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## ArrayWithUniqueItems
public static class ArrayWithUniqueItems<br>
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
import org.openapijsonschematools.client.components.schemas.FormatTest;

import java.util.Arrays;
import java.util.List;
import java.util.AbstractMap;

static final SchemaConfiguration configuration = new SchemaConfiguration(new JsonSchemaKeywordFlags.Builder().build());

// List validation
FormatTest.ArrayWithUniqueItemsList validatedPayload =
    FormatTest.ArrayWithUniqueItems.validate(
    new FormatTest.ArrayWithUniqueItemsListBuilder()
        .add(1)

    .build(),
    configuration
);
```

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Set<Class<?>> | type = Set.of(List.class) |
| Class<? extends JsonSchema> | items = [Items.class](#items) |
| Boolean | uniqueItems = true |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| [ArrayWithUniqueItemsList](#arraywithuniqueitemslist) | validate([List<?>](#arraywithuniqueitemslistbuilder) arg, SchemaConfiguration configuration) |
| [ArrayWithUniqueItemsBoxedList](#arraywithuniqueitemsboxedlist) | validateAndBox([List<?>](#arraywithuniqueitemslistbuilder) arg, SchemaConfiguration configuration) |
| [ArrayWithUniqueItemsBoxed](#arraywithuniqueitemsboxed) | validateAndBox(@Nullable Object arg, SchemaConfiguration configuration) |
| @Nullable Object | validate(@Nullable Object arg, SchemaConfiguration configuration) |

## ArrayWithUniqueItemsListBuilder
public class ArrayWithUniqueItemsListBuilder<br>
builder for `List<Number>`

A class that builds the List input type

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| ArrayWithUniqueItemsListBuilder()<br>Creates an empty list |
| ArrayWithUniqueItemsListBuilder(List<Number> items)<br>Stores the items in a list |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| ArrayWithUniqueItemsListBuilder | add(int item) |
| ArrayWithUniqueItemsListBuilder | add(float item) |
| ArrayWithUniqueItemsListBuilder | add(long item) |
| ArrayWithUniqueItemsListBuilder | add(double item) |
| List<Number> | build()<br>Returns list input that should be used with Schema.validate |

## ArrayWithUniqueItemsList
public class ArrayWithUniqueItemsList<br>
extends `FrozenList<Number>`

A class to store validated List payloads

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| static [ArrayWithUniqueItemsList](#arraywithuniqueitemslist) | of([List<Number>](#arraywithuniqueitemslistbuilder) arg, SchemaConfiguration configuration) |

## ItemsBoxed
public sealed interface ItemsBoxed<br>
permits<br>
[ItemsBoxedNumber](#itemsboxednumber)

sealed interface that stores validated payloads using boxed classes

## ItemsBoxedNumber
public record ItemsBoxedNumber<br>
implements [ItemsBoxed](#itemsboxed)

record that stores validated Number payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| ItemsBoxedNumber(Number data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| Number | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## Items
public static class Items<br>
extends NumberJsonSchema.NumberJsonSchema1

A schema class that validates payloads

| Methods Inherited from class org.openapijsonschematools.client.schemas.NumberJsonSchema.NumberJsonSchema1 |
| ------------------------------------------------------------------ |
| validate                                                           |
| validateAndBox                                                     |

## Float64Boxed
public sealed interface Float64Boxed<br>
permits<br>
[Float64BoxedNumber](#float64boxednumber)

sealed interface that stores validated payloads using boxed classes

## Float64BoxedNumber
public record Float64BoxedNumber<br>
implements [Float64Boxed](#float64boxed)

record that stores validated Number payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| Float64BoxedNumber(Number data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| Number | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## Float64
public static class Float64<br>
extends DoubleJsonSchema.DoubleJsonSchema1

A schema class that validates payloads

| Methods Inherited from class org.openapijsonschematools.client.schemas.DoubleJsonSchema.DoubleJsonSchema1 |
| ------------------------------------------------------------------ |
| validate                                                           |
| validateAndBox                                                     |

## DoubleSchemaBoxed
public sealed interface DoubleSchemaBoxed<br>
permits<br>
[DoubleSchemaBoxedNumber](#doubleschemaboxednumber)

sealed interface that stores validated payloads using boxed classes

## DoubleSchemaBoxedNumber
public record DoubleSchemaBoxedNumber<br>
implements [DoubleSchemaBoxed](#doubleschemaboxed)

record that stores validated Number payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| DoubleSchemaBoxedNumber(Number data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| Number | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## DoubleSchema
public static class DoubleSchema<br>
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
import org.openapijsonschematools.client.components.schemas.FormatTest;

import java.util.Arrays;
import java.util.List;
import java.util.AbstractMap;

static final SchemaConfiguration configuration = new SchemaConfiguration(new JsonSchemaKeywordFlags.Builder().build());

// double validation
double validatedPayload = FormatTest.DoubleSchema.validate(
    3.14d,
    configuration
);
```

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Set<Class<?>> | type = Set.of(<br/>&nbsp;&nbsp;&nbsp;&nbsp;Integer.class,<br/>&nbsp;&nbsp;&nbsp;&nbsp;Long.class,<br/>&nbsp;&nbsp;&nbsp;&nbsp;Float.class,<br/>&nbsp;&nbsp;&nbsp;&nbsp;Double.class<br/>)<br/> |
| String | type = "double"; |
| Number | maximum = 123.4 |
| Number | minimum = 67.8 |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| double | validate(double arg, SchemaConfiguration configuration) |
| [DoubleSchemaBoxedNumber](#doubleschemaboxednumber) | validateAndBox(Number arg, SchemaConfiguration configuration) |
| [DoubleSchemaBoxed](#doubleschemaboxed) | validateAndBox(@Nullable Object arg, SchemaConfiguration configuration) |
| @Nullable Object | validate(@Nullable Object arg, SchemaConfiguration configuration) |

## Float32Boxed
public sealed interface Float32Boxed<br>
permits<br>
[Float32BoxedNumber](#float32boxednumber)

sealed interface that stores validated payloads using boxed classes

## Float32BoxedNumber
public record Float32BoxedNumber<br>
implements [Float32Boxed](#float32boxed)

record that stores validated Number payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| Float32BoxedNumber(Number data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| Number | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## Float32
public static class Float32<br>
extends FloatJsonSchema.FloatJsonSchema1

A schema class that validates payloads

| Methods Inherited from class org.openapijsonschematools.client.schemas.FloatJsonSchema.FloatJsonSchema1 |
| ------------------------------------------------------------------ |
| validate                                                           |
| validateAndBox                                                     |

## FloatSchemaBoxed
public sealed interface FloatSchemaBoxed<br>
permits<br>
[FloatSchemaBoxedNumber](#floatschemaboxednumber)

sealed interface that stores validated payloads using boxed classes

## FloatSchemaBoxedNumber
public record FloatSchemaBoxedNumber<br>
implements [FloatSchemaBoxed](#floatschemaboxed)

record that stores validated Number payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| FloatSchemaBoxedNumber(Number data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| Number | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## FloatSchema
public static class FloatSchema<br>
extends JsonSchema

A schema class that validates payloads

## Description
this is a reserved python keyword

### Code Sample
```
import org.openapijsonschematools.client.configurations.JsonSchemaKeywordFlags;
import org.openapijsonschematools.client.configurations.SchemaConfiguration;
import org.openapijsonschematools.client.exceptions.ValidationException;
import org.openapijsonschematools.client.schemas.validation.MapUtils;
import org.openapijsonschematools.client.schemas.validation.FrozenList;
import org.openapijsonschematools.client.schemas.validation.FrozenMap;
import org.openapijsonschematools.client.components.schemas.FormatTest;

import java.util.Arrays;
import java.util.List;
import java.util.AbstractMap;

static final SchemaConfiguration configuration = new SchemaConfiguration(new JsonSchemaKeywordFlags.Builder().build());

// float validation
float validatedPayload = FormatTest.FloatSchema.validate(
    3.14f,
    configuration
);
```

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Set<Class<?>> | type = Set.of(<br/>&nbsp;&nbsp;&nbsp;&nbsp;Integer.class,<br/>&nbsp;&nbsp;&nbsp;&nbsp;Long.class,<br/>&nbsp;&nbsp;&nbsp;&nbsp;Float.class,<br/>&nbsp;&nbsp;&nbsp;&nbsp;Double.class<br/>)<br/> |
| String | type = "float"; |
| Number | maximum = 987.6 |
| Number | minimum = 54.3 |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| float | validate(float arg, SchemaConfiguration configuration) |
| [FloatSchemaBoxedNumber](#floatschemaboxednumber) | validateAndBox(Number arg, SchemaConfiguration configuration) |
| [FloatSchemaBoxed](#floatschemaboxed) | validateAndBox(@Nullable Object arg, SchemaConfiguration configuration) |
| @Nullable Object | validate(@Nullable Object arg, SchemaConfiguration configuration) |

## NumberSchemaBoxed
public sealed interface NumberSchemaBoxed<br>
permits<br>
[NumberSchemaBoxedNumber](#numberschemaboxednumber)

sealed interface that stores validated payloads using boxed classes

## NumberSchemaBoxedNumber
public record NumberSchemaBoxedNumber<br>
implements [NumberSchemaBoxed](#numberschemaboxed)

record that stores validated Number payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| NumberSchemaBoxedNumber(Number data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| Number | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## NumberSchema
public static class NumberSchema<br>
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
import org.openapijsonschematools.client.components.schemas.FormatTest;

import java.util.Arrays;
import java.util.List;
import java.util.AbstractMap;

static final SchemaConfiguration configuration = new SchemaConfiguration(new JsonSchemaKeywordFlags.Builder().build());

// int validation
int validatedPayload = FormatTest.NumberSchema.validate(
    1,
    configuration
);
```

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Set<Class<?>> | type = Set.of(<br/>&nbsp;&nbsp;&nbsp;&nbsp;Integer.class,<br/>&nbsp;&nbsp;&nbsp;&nbsp;Long.class,<br/>&nbsp;&nbsp;&nbsp;&nbsp;Float.class,<br/>&nbsp;&nbsp;&nbsp;&nbsp;Double.class<br/>)<br/> |
| Number | maximum = 543.2 |
| Number | minimum = 32.1 |
| BigDecimal | multipleOf = new BigDecimal("32.5") |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| Number | validate(Number arg, SchemaConfiguration configuration) |
| [NumberSchemaBoxedNumber](#numberschemaboxednumber) | validateAndBox(Number arg, SchemaConfiguration configuration) |
| [NumberSchemaBoxed](#numberschemaboxed) | validateAndBox(@Nullable Object arg, SchemaConfiguration configuration) |
| @Nullable Object | validate(@Nullable Object arg, SchemaConfiguration configuration) |

## Int64Boxed
public sealed interface Int64Boxed<br>
permits<br>
[Int64BoxedNumber](#int64boxednumber)

sealed interface that stores validated payloads using boxed classes

## Int64BoxedNumber
public record Int64BoxedNumber<br>
implements [Int64Boxed](#int64boxed)

record that stores validated Number payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| Int64BoxedNumber(Number data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| Number | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## Int64
public static class Int64<br>
extends Int64JsonSchema.Int64JsonSchema1

A schema class that validates payloads

| Methods Inherited from class org.openapijsonschematools.client.schemas.Int64JsonSchema.Int64JsonSchema1 |
| ------------------------------------------------------------------ |
| validate                                                           |
| validateAndBox                                                     |

## Int32withValidationsBoxed
public sealed interface Int32withValidationsBoxed<br>
permits<br>
[Int32withValidationsBoxedNumber](#int32withvalidationsboxednumber)

sealed interface that stores validated payloads using boxed classes

## Int32withValidationsBoxedNumber
public record Int32withValidationsBoxedNumber<br>
implements [Int32withValidationsBoxed](#int32withvalidationsboxed)

record that stores validated Number payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| Int32withValidationsBoxedNumber(Number data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| Number | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## Int32withValidations
public static class Int32withValidations<br>
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
import org.openapijsonschematools.client.components.schemas.FormatTest;

import java.util.Arrays;
import java.util.List;
import java.util.AbstractMap;

static final SchemaConfiguration configuration = new SchemaConfiguration(new JsonSchemaKeywordFlags.Builder().build());

// int validation
int validatedPayload = FormatTest.Int32withValidations.validate(
    1,
    configuration
);
```

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Set<Class<?>> | type = Set.of(<br/>&nbsp;&nbsp;&nbsp;&nbsp;Integer.class,<br/>&nbsp;&nbsp;&nbsp;&nbsp;Long.class,<br/>&nbsp;&nbsp;&nbsp;&nbsp;Float.class,<br/>&nbsp;&nbsp;&nbsp;&nbsp;Double.class<br/>)<br/> |
| String | type = "int32"; |
| Number | maximum = 200 |
| Number | minimum = 20 |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| int | validate(int arg, SchemaConfiguration configuration) |
| [Int32withValidationsBoxedNumber](#int32withvalidationsboxednumber) | validateAndBox(Number arg, SchemaConfiguration configuration) |
| [Int32withValidationsBoxed](#int32withvalidationsboxed) | validateAndBox(@Nullable Object arg, SchemaConfiguration configuration) |
| @Nullable Object | validate(@Nullable Object arg, SchemaConfiguration configuration) |

## Int32Boxed
public sealed interface Int32Boxed<br>
permits<br>
[Int32BoxedNumber](#int32boxednumber)

sealed interface that stores validated payloads using boxed classes

## Int32BoxedNumber
public record Int32BoxedNumber<br>
implements [Int32Boxed](#int32boxed)

record that stores validated Number payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| Int32BoxedNumber(Number data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| Number | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## Int32
public static class Int32<br>
extends Int32JsonSchema.Int32JsonSchema1

A schema class that validates payloads

| Methods Inherited from class org.openapijsonschematools.client.schemas.Int32JsonSchema.Int32JsonSchema1 |
| ------------------------------------------------------------------ |
| validate                                                           |
| validateAndBox                                                     |

## IntegerSchemaBoxed
public sealed interface IntegerSchemaBoxed<br>
permits<br>
[IntegerSchemaBoxedNumber](#integerschemaboxednumber)

sealed interface that stores validated payloads using boxed classes

## IntegerSchemaBoxedNumber
public record IntegerSchemaBoxedNumber<br>
implements [IntegerSchemaBoxed](#integerschemaboxed)

record that stores validated Number payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| IntegerSchemaBoxedNumber(Number data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| Number | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## IntegerSchema
public static class IntegerSchema<br>
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
import org.openapijsonschematools.client.components.schemas.FormatTest;

import java.util.Arrays;
import java.util.List;
import java.util.AbstractMap;

static final SchemaConfiguration configuration = new SchemaConfiguration(new JsonSchemaKeywordFlags.Builder().build());

// int validation
int validatedPayload = FormatTest.IntegerSchema.validate(
    1L,
    configuration
);
```

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Set<Class<?>> | type = Set.of(<br/>&nbsp;&nbsp;&nbsp;&nbsp;Integer.class,<br/>&nbsp;&nbsp;&nbsp;&nbsp;Long.class,<br/>&nbsp;&nbsp;&nbsp;&nbsp;Float.class,<br/>&nbsp;&nbsp;&nbsp;&nbsp;Double.class<br/>)<br/> |
| String | type = "int"; |
| Number | maximum = 100 |
| Number | minimum = 10 |
| BigDecimal | multipleOf = new BigDecimal("2") |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| long | validate(long arg, SchemaConfiguration configuration) |
| [IntegerSchemaBoxedNumber](#integerschemaboxednumber) | validateAndBox(Number arg, SchemaConfiguration configuration) |
| [IntegerSchemaBoxed](#integerschemaboxed) | validateAndBox(@Nullable Object arg, SchemaConfiguration configuration) |
| @Nullable Object | validate(@Nullable Object arg, SchemaConfiguration configuration) |

[[Back to top]](#top) [[Back to Component Schemas]](../../../README.md#Component-Schemas) [[Back to README]](../../../README.md)
