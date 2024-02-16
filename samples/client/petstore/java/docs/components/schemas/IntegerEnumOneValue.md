# IntegerEnumOneValue
org.openapijsonschematools.client.components.schemas.IntegerEnumOneValue.java
public class IntegerEnumOneValue<br>

A class that contains necessary nested
- schema classes (which validate payloads), extends JsonSchema
- abstract sealed classes which store validated payloads, java version of a sum type
- boxed classes which store validated payloads, sealed permits class implementations
- enum classes

## Nested Class Summary
| Modifier and Type | Class and Description |
| ----------------- | ---------------------- |
| static class | [IntegerEnumOneValue.IntegerEnumOneValue1Boxed](#integerenumonevalue1boxed)<br> abstract sealed validated payload class |
| static class | [IntegerEnumOneValue.IntegerEnumOneValue1BoxedNumber](#integerenumonevalue1boxednumber)<br> boxed class to store validated Number payloads |
| static class | [IntegerEnumOneValue.IntegerEnumOneValue1](#integerenumonevalue1)<br> schema class |
| enum | [IntegerEnumOneValue.IntegerIntegerEnumOneValueEnums](#integerintegerenumonevalueenums)<br>Integer enum |
| enum | [IntegerEnumOneValue.LongIntegerEnumOneValueEnums](#longintegerenumonevalueenums)<br>Long enum |
| enum | [IntegerEnumOneValue.FloatIntegerEnumOneValueEnums](#floatintegerenumonevalueenums)<br>Float enum |
| enum | [IntegerEnumOneValue.DoubleIntegerEnumOneValueEnums](#doubleintegerenumonevalueenums)<br>Double enum |

## IntegerEnumOneValue1Boxed
public static abstract sealed class IntegerEnumOneValue1Boxed<br>
permits<br>
[IntegerEnumOneValue1BoxedNumber](#integerenumonevalue1boxednumber)

abstract sealed class that stores validated payloads using boxed classes

## IntegerEnumOneValue1BoxedNumber
public static final class IntegerEnumOneValue1BoxedNumber<br>
extends [IntegerEnumOneValue1Boxed](#integerenumonevalue1boxed)

a boxed class to store validated Number payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| IntegerEnumOneValue1BoxedNumber(Number data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Number | data<br>validated payload |

## IntegerEnumOneValue1
public static class IntegerEnumOneValue1<br>
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

// int validation
int validatedPayload = IntegerEnumOneValue.IntegerEnumOneValue1.validate(
    1L,
    configuration
);
```

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Set<Class<?>> | type = Set.of(<br/>&nbsp;&nbsp;&nbsp;&nbsp;Integer.class,<br/>&nbsp;&nbsp;&nbsp;&nbsp;Long.class,<br/>&nbsp;&nbsp;&nbsp;&nbsp;Float.class,<br/>&nbsp;&nbsp;&nbsp;&nbsp;Double.class<br/>)<br/> |
| String | type = "int"; |
| Set<Object> | enumValues = SetMaker.makeSet(<br>&nbsp;&nbsp;&nbsp;&nbsp;0<br>)<br> |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| long | validate(long arg, SchemaConfiguration configuration) |
| [IntegerEnumOneValue1BoxedNumber](#integerenumonevalue1boxednumber) | validateAndBox(Number arg, SchemaConfiguration configuration) |
| @Nullable Object | validate(@Nullable Object arg, SchemaConfiguration configuration) |
## IntegerIntegerEnumOneValueEnums
public enum IntegerIntegerEnumOneValueEnums<br>
extends `Enum<IntegerIntegerEnumOneValueEnums>`

A class that stores Integer enum values

### Enum Constant Summary
| Enum Constant | Description |
| ------------- | ----------- |
| POSITIVE_0 | value = 0 |

## LongIntegerEnumOneValueEnums
public enum LongIntegerEnumOneValueEnums<br>
extends `Enum<LongIntegerEnumOneValueEnums>`

A class that stores Long enum values

### Enum Constant Summary
| Enum Constant | Description |
| ------------- | ----------- |
| POSITIVE_0 | value = 0L |

## FloatIntegerEnumOneValueEnums
public enum FloatIntegerEnumOneValueEnums<br>
extends `Enum<FloatIntegerEnumOneValueEnums>`

A class that stores Float enum values

### Enum Constant Summary
| Enum Constant | Description |
| ------------- | ----------- |
| POSITIVE_0 | value = 0.0f |

## DoubleIntegerEnumOneValueEnums
public enum DoubleIntegerEnumOneValueEnums<br>
extends `Enum<DoubleIntegerEnumOneValueEnums>`

A class that stores Double enum values

### Enum Constant Summary
| Enum Constant | Description |
| ------------- | ----------- |
| POSITIVE_0 | value = 0.0d |

[[Back to top]](#top) [[Back to Component Schemas]](../../../README.md#Component-Schemas) [[Back to README]](../../../README.md)
