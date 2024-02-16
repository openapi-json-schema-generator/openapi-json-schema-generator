# PathParamSchema0
public class PathParamSchema0<br>

A class that contains necessary nested
- schema classes (which validate payloads), extends JsonSchema
- abstract sealed classes which store validated payloads, java version of a sum type
- boxed classes which store validated payloads, sealed permits class implementations
- enum classes

## Nested Class Summary
| Modifier and Type | Class and Description |
| ----------------- | ---------------------- |
| static class | [PathParamSchema0.PathParamSchema01Boxed](#pathparamschema01boxed)<br> abstract sealed validated payload class |
| static class | [PathParamSchema0.PathParamSchema01BoxedString](#pathparamschema01boxedstring)<br> boxed class to store validated String payloads |
| static class | [PathParamSchema0.PathParamSchema01](#pathparamschema01)<br> schema class |
| enum | [PathParamSchema0.StringPathParamSchemaEnums0](#stringpathparamschemaenums0)<br>String enum |

## PathParamSchema01Boxed
public static abstract sealed class PathParamSchema01Boxed<br>
permits<br>
[PathParamSchema01BoxedString](#pathparamschema01boxedstring)

abstract sealed class that stores validated payloads using boxed classes

## PathParamSchema01BoxedString
public static final class PathParamSchema01BoxedString<br>
extends [PathParamSchema01Boxed](#pathparamschema01boxed)

a boxed class to store validated String payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| PathParamSchema01BoxedString(String data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| String | data<br>validated payload |

## PathParamSchema01
public static class PathParamSchema01<br>
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
String validatedPayload = PathParamSchema0.PathParamSchema01.validate(
    "a",
    configuration
);
```

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Set<Class<?>> | type = Set.of(<br/>&nbsp;&nbsp;&nbsp;&nbsp;String.class<br/>)<br/> |
| Set<Object> | enumValues = SetMaker.makeSet(<br>&nbsp;&nbsp;&nbsp;&nbsp;"a",<br>&nbsp;&nbsp;&nbsp;&nbsp;"b"<br>)<br> |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| String | validate(String arg, SchemaConfiguration configuration) |
| String | validate([StringPathParamSchemaEnums0](#stringpathparamschemaenums0) arg, SchemaConfiguration configuration) |
| [PathParamSchema01BoxedString](#pathparamschema01boxedstring) | validateAndBox(String arg, SchemaConfiguration configuration) |
| @Nullable Object | validate(@Nullable Object arg, SchemaConfiguration configuration) |
## StringPathParamSchemaEnums0
public enum StringPathParamSchemaEnums0<br>
extends `Enum<StringPathParamSchemaEnums0>`

A class that stores String enum values

### Enum Constant Summary
| Enum Constant | Description |
| ------------- | ----------- |
| A | value = "a" |
| B | value = "b" |
