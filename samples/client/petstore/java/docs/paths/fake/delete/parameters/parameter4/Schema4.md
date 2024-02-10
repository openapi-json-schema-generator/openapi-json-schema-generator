# Schema4
public class Schema4

A class that contains necessary nested
- schema classes (which validate payloads), extends JsonSchema
- abstract sealed classes which store validated payloads, java version of a sum type
- boxed classes which store validated payloads, sealed permits class implementations
- enum classes

## Nested Class Summary
| Modifier and Type | Class and Description |
| ----------------- | ---------------------- |
| static class | [Schema4.Schema41Boxed](#schema41boxed)<br> abstract sealed validated payload class |
| static class | [Schema4.Schema41BoxedString](#schema41boxedstring)<br> boxed class to store validated String payloads |
| static class | [Schema4.Schema41](#schema41)<br> schema class |
| enum | [Schema4.StringSchemaEnums4](#stringschemaenums4)<br>String enum |

## Schema41Boxed
public static abstract sealed class Schema41Boxed<br>
permits<br>
[Schema41BoxedString](#schema41boxedstring)

abstract sealed class that stores validated payloads using boxed classes

## Schema41BoxedString
public static final class Schema41BoxedString<br>
extends [Schema41Boxed](#schema41boxed)

a boxed class to store validated String payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| Schema41BoxedString(String data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| String | data<br>validated payload |

## Schema41
public static class Schema41<br>
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

// String validation
String validatedPayload = Schema4.Schema41.validate(
    "true",
    configuration
);
```

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Set<Class<?>> | type = Set.of(<br/>&nbsp;&nbsp;&nbsp;&nbsp;String.class<br/>)<br/> |
| Set<Object> | enumValues = SetMaker.makeSet(<br>&nbsp;&nbsp;&nbsp;&nbsp;"true",<br>&nbsp;&nbsp;&nbsp;&nbsp;"false"<br>)<br> |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| String | validate(String arg, SchemaConfiguration configuration) |
| String | validate([StringSchemaEnums4](#stringschemaenums4) arg, SchemaConfiguration configuration) |
| [Schema41BoxedString](#schema41boxedstring) | validateAndBox(String arg, SchemaConfiguration configuration) |
| @Nullable Object | validate(@Nullable Object arg, SchemaConfiguration configuration) |
## StringSchemaEnums4
public enum StringSchemaEnums4<br>
extends `Enum<StringSchemaEnums4>`

A class that stores String enum values

### Enum Constant Summary
| Enum Constant | Description |
| ------------- | ----------- |
| TRUE | value = "true" |
| FALSE | value = "false" |
