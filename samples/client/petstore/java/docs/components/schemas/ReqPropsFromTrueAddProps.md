# ReqPropsFromTrueAddProps
org.openapijsonschematools.client.components.schemas.ReqPropsFromTrueAddProps.java
public class ReqPropsFromTrueAddProps

A class that contains necessary nested
- schema classes (which validate payloads), extends JsonSchema
- classes to store validated map payloads, extends FrozenMap
- classes to build inputs for map payloads

## Nested Class Summary
| Modifier and Type | Class and Description |
| ----------------- | ---------------------- |
| static class | [ReqPropsFromTrueAddProps.ReqPropsFromTrueAddProps1](#reqpropsfromtrueaddprops1)<br> schema class |
| static class | [ReqPropsFromTrueAddProps.ReqPropsFromTrueAddPropsMapBuilder](#reqpropsfromtrueaddpropsmapbuilder)<br> builder for Map payloads |
| static class | [ReqPropsFromTrueAddProps.ReqPropsFromTrueAddPropsMap](#reqpropsfromtrueaddpropsmap)<br> output class for Map payloads |
| static class | [ReqPropsFromTrueAddProps.AdditionalProperties](#additionalproperties)<br> schema class |

## ReqPropsFromTrueAddProps1
public static class ReqPropsFromTrueAddProps1<br>
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

// Map validation
ReqPropsFromTrueAddProps.ReqPropsFromTrueAddPropsMap validatedPayload =
    ReqPropsFromTrueAddProps.ReqPropsFromTrueAddProps1.validate(
    MapMaker.makeMap(
    ),
    configuration
);
```

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Set<Class<?>> | type = Set.of(Map.class) |
| Set<String> | required = Set.of(<br>&nbsp;&nbsp;&nbsp;&nbsp;"invalid-name",<br>&nbsp;&nbsp;&nbsp;&nbsp;"validName"<br>)<br> |
| Class<? extends JsonSchema> | additionalProperties = [AdditionalProperties.class](#additionalproperties) |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| [ReqPropsFromTrueAddPropsMap](#reqpropsfromtrueaddpropsmap) | validate([Map<?, ?>](#reqpropsfromtrueaddpropsmapbuilder) arg, SchemaConfiguration configuration) |
| @Nullable Object | validate(@Nullable Object arg, SchemaConfiguration configuration) |
## ReqPropsFromTrueAddPropsMapBuilder
public class ReqPropsFromTrueAddPropsMapBuilder<br>
builder for `Map<String, ? extends @Nullable Object>`

A class that builds the Map input type

## Input Map Keys
| Key | Type |  Description | Notes |
| --- | ---- | ------------ | ----- |
| **invalid-name** | ? extends @Nullable Object |  | |
| **validName** | ? extends @Nullable Object |  | |
| **anyStringName** | Object | any string name can be used but the value must be the correct type | [optional] |

## ReqPropsFromTrueAddPropsMap
public static class ReqPropsFromTrueAddPropsMap<br>
extends FrozenMap<String, @Nullable Object>

A class to store validated Map payloads

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| static [ReqPropsFromTrueAddPropsMap](#reqpropsfromtrueaddpropsmap) | of([Map<String, ? extends @Nullable Object>](#reqpropsfromtrueaddpropsmapbuilder) arg, SchemaConfiguration configuration) |
| @Nullable Object | validName()<br> |
| @Nullable Object | get(String key)<br>This schema has invalid Java names so this method must be used when you access instance["invalid-name"],  |
| Object | getAdditionalProperty(String name)<br>provides type safety for additional properties |

## AdditionalProperties
public static class AdditionalProperties<br>
extends AnyTypeJsonSchema

A schema class that validates payloads

| Methods Inherited from class org.openapijsonschematools.client.schemas.AnyTypeJsonSchema |
| ------------------------------------------------------------------ |
| validate                                                           |

[[Back to top]](#top) [[Back to Component Schemas]](../../../README.md#Component-Schemas) [[Back to README]](../../../README.md)
