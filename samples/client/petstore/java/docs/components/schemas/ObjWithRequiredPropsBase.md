# ObjWithRequiredPropsBase
org.openapijsonschematools.client.components.schemas.ObjWithRequiredPropsBase.java
public class ObjWithRequiredPropsBase<br>

A class that contains necessary nested
- schema classes (which validate payloads), extends JsonSchema
- abstract sealed classes which store validated payloads, java version of a sum type
- boxed classes which store validated payloads, sealed permits class implementations
- classes to store validated map payloads, extends FrozenMap
- classes to build inputs for map payloads

## Nested Class Summary
| Modifier and Type | Class and Description |
| ----------------- | ---------------------- |
| static class | [ObjWithRequiredPropsBase.ObjWithRequiredPropsBase1Boxed](#objwithrequiredpropsbase1boxed)<br> abstract sealed validated payload class |
| static class | [ObjWithRequiredPropsBase.ObjWithRequiredPropsBase1BoxedMap](#objwithrequiredpropsbase1boxedmap)<br> boxed class to store validated Map payloads |
| static class | [ObjWithRequiredPropsBase.ObjWithRequiredPropsBase1](#objwithrequiredpropsbase1)<br> schema class |
| static class | [ObjWithRequiredPropsBase.ObjWithRequiredPropsBaseMapBuilder](#objwithrequiredpropsbasemapbuilder)<br> builder for Map payloads |
| static class | [ObjWithRequiredPropsBase.ObjWithRequiredPropsBaseMap](#objwithrequiredpropsbasemap)<br> output class for Map payloads |
| static class | [ObjWithRequiredPropsBase.BBoxed](#bboxed)<br> abstract sealed validated payload class |
| static class | [ObjWithRequiredPropsBase.BBoxedString](#bboxedstring)<br> boxed class to store validated String payloads |
| static class | [ObjWithRequiredPropsBase.B](#b)<br> schema class |

## ObjWithRequiredPropsBase1Boxed
public static abstract sealed class ObjWithRequiredPropsBase1Boxed<br>
permits<br>
[ObjWithRequiredPropsBase1BoxedMap](#objwithrequiredpropsbase1boxedmap)

abstract sealed class that stores validated payloads using boxed classes

## ObjWithRequiredPropsBase1BoxedMap
public static final class ObjWithRequiredPropsBase1BoxedMap<br>
extends [ObjWithRequiredPropsBase1Boxed](#objwithrequiredpropsbase1boxed)

a boxed class to store validated Map payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| ObjWithRequiredPropsBase1BoxedMap([ObjWithRequiredPropsBaseMap](#objwithrequiredpropsbasemap) data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| [ObjWithRequiredPropsBaseMap](#objwithrequiredpropsbasemap) | data<br>validated payload |

## ObjWithRequiredPropsBase1
public static class ObjWithRequiredPropsBase1<br>
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
ObjWithRequiredPropsBase.ObjWithRequiredPropsBaseMap validatedPayload =
    ObjWithRequiredPropsBase.ObjWithRequiredPropsBase1.validate(
    new ObjWithRequiredPropsBase.ObjWithRequiredPropsBaseMapBuilder()
        .b("a")

    .build(),
    configuration
);
```

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Set<Class<?>> | type = Set.of(Map.class) |
| Map<String, Class<? extends JsonSchema>> | properties = Map.ofEntries(<br>&nbsp;&nbsp;&nbsp;&nbsp;new PropertyEntry("b", [B.class](#b)))<br>)<br> |
| Set<String> | required = Set.of(<br>&nbsp;&nbsp;&nbsp;&nbsp;"b"<br>)<br> |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| [ObjWithRequiredPropsBaseMap](#objwithrequiredpropsbasemap) | validate([Map&lt;?, ?&gt;](#objwithrequiredpropsbasemapbuilder) arg, SchemaConfiguration configuration) |
| [ObjWithRequiredPropsBase1BoxedMap](#objwithrequiredpropsbase1boxedmap) | validateAndBox([Map&lt;?, ?&gt;](#objwithrequiredpropsbasemapbuilder) arg, SchemaConfiguration configuration) |
| @Nullable Object | validate(@Nullable Object arg, SchemaConfiguration configuration) |
## ObjWithRequiredPropsBaseMap0Builder
public class ObjWithRequiredPropsBaseMap0Builder<br>
builder for `Map<String, @Nullable Object>`

A class that builds the Map input type

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| ObjWithRequiredPropsBaseMap0Builder(Map<String, @Nullable Object> instance)<br>Creates a builder that contains the passed instance |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| Map<String, @Nullable Object> | build()<br>Returns map input that should be used with Schema.validate |
| [ObjWithRequiredPropsBaseMap0Builder](#objwithrequiredpropsbasemap0builder) | additionalProperty(String key, Void value) |
| [ObjWithRequiredPropsBaseMap0Builder](#objwithrequiredpropsbasemap0builder) | additionalProperty(String key, boolean value) |
| [ObjWithRequiredPropsBaseMap0Builder](#objwithrequiredpropsbasemap0builder) | additionalProperty(String key, String value) |
| [ObjWithRequiredPropsBaseMap0Builder](#objwithrequiredpropsbasemap0builder) | additionalProperty(String key, int value) |
| [ObjWithRequiredPropsBaseMap0Builder](#objwithrequiredpropsbasemap0builder) | additionalProperty(String key, float value) |
| [ObjWithRequiredPropsBaseMap0Builder](#objwithrequiredpropsbasemap0builder) | additionalProperty(String key, long value) |
| [ObjWithRequiredPropsBaseMap0Builder](#objwithrequiredpropsbasemap0builder) | additionalProperty(String key, double value) |
| [ObjWithRequiredPropsBaseMap0Builder](#objwithrequiredpropsbasemap0builder) | additionalProperty(String key, List<?> value) |
| [ObjWithRequiredPropsBaseMap0Builder](#objwithrequiredpropsbasemap0builder) | additionalProperty(String key, Map<String, ?> value) |

## ObjWithRequiredPropsBaseMapBuilder
public class ObjWithRequiredPropsBaseMapBuilder<br>
builder for `Map<String, @Nullable Object>`

A class that builds the Map input type

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| ObjWithRequiredPropsBaseMapBuilder()<br>Creates a builder that contains an empty map |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| [ObjWithRequiredPropsBaseMap0Builder](#objwithrequiredpropsbasemap0builder) | b(String value) |

## ObjWithRequiredPropsBaseMap
public static class ObjWithRequiredPropsBaseMap<br>
extends FrozenMap<String, @Nullable Object>

A class to store validated Map payloads

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| static [ObjWithRequiredPropsBaseMap](#objwithrequiredpropsbasemap) | of([Map<String, ? extends @Nullable Object>](#objwithrequiredpropsbasemapbuilder) arg, SchemaConfiguration configuration) |
| String | b()<br> |
| @Nullable Object | getAdditionalProperty(String name)<br>provides type safety for additional properties |

## BBoxed
public static abstract sealed class BBoxed<br>
permits<br>
[BBoxedString](#bboxedstring)

abstract sealed class that stores validated payloads using boxed classes

## BBoxedString
public static final class BBoxedString<br>
extends [BBoxed](#bboxed)

a boxed class to store validated String payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| BBoxedString(String data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| String | data<br>validated payload |

## B
public static class B<br>
extends StringJsonSchema.StringJsonSchema1

A schema class that validates payloads

| Methods Inherited from class org.openapijsonschematools.client.schemas.StringJsonSchema.StringJsonSchema1 |
| ------------------------------------------------------------------ |
| validate                                                           |
| validateAndBox                                                     |

[[Back to top]](#top) [[Back to Component Schemas]](../../../README.md#Component-Schemas) [[Back to README]](../../../README.md)
