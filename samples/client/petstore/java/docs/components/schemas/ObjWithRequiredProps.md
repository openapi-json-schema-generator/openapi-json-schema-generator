# ObjWithRequiredProps
org.openapijsonschematools.client.components.schemas.ObjWithRequiredProps.java
public class ObjWithRequiredProps

A class that contains necessary nested
- schema classes (which validate payloads), extends JsonSchema
- classes to store validated list payloads, extends FrozenList
- classes to store validated map payloads, extends FrozenMap
- classes to build inputs for list payloads
- classes to build inputs for map payloads

## Nested Class Summary
| Modifier and Type | Class and Description |
| ----------------- | ---------------------- |
| static class | [ObjWithRequiredProps.ObjWithRequiredProps1](#objwithrequiredprops1)<br> schema class |
| static class | [ObjWithRequiredProps.ObjWithRequiredPropsMapInput](#objwithrequiredpropsmapinput)<br> builder for Map payloads |
| static class | [ObjWithRequiredProps.ObjWithRequiredPropsMap](#objwithrequiredpropsmap)<br> output class for Map payloads |
| static class | [ObjWithRequiredProps.A](#a)<br> schema class |

## ObjWithRequiredProps1
public static class ObjWithRequiredProps1<br>
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
ObjWithRequiredProps.ObjWithRequiredPropsMap validatedPayload =
    ObjWithRequiredProps.ObjWithRequiredProps1.validate(
    MapMaker.makeMap(
        new AbstractMap.SimpleEntry<>(
            "a",
            "a"
        )
    ),
    configuration
);
```

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Set<Class<?>> | &nbsp;&nbsp;&nbsp;&nbsp;type = Set.of(Map.class)<br/> |
| Map<String, Class<? extends JsonSchema>> | &nbsp;&nbsp;&nbsp;&nbsp;properties = Map.ofEntries(<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;new PropertyEntry("a", [A.class](#a)))<br>&nbsp;&nbsp;&nbsp;&nbsp;)<br> |
| Set<String> | &nbsp;&nbsp;&nbsp;&nbsp;required = Set.of(<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"a"<br>&nbsp;&nbsp;&nbsp;&nbsp;)<br> |
| List<Class<? extends JsonSchema>> | &nbsp;&nbsp;&nbsp;&nbsp;allOf = List.of(<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ObjWithRequiredPropsBase.ObjWithRequiredPropsBase1.class](../../components/schemas/ObjWithRequiredPropsBase.md#objwithrequiredpropsbase1)<br>&nbsp;&nbsp;&nbsp;&nbsp;)<br> |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| static [ObjWithRequiredPropsMap](#objwithrequiredpropsmap) | validate([Map<String, Object>](#objwithrequiredpropsmapinput) arg, SchemaConfiguration configuration) |

## ObjWithRequiredPropsMapInput
public class ObjWithRequiredPropsMapInput<br>
builder for `Map<String, Object>`

A class that builds the Map input type

## Input Map Keys
| Key | Type |  Description | Notes |
| --- | ---- | ------------ | ----- |
| **a** | String |  | |
| **anyStringName** | Object | any string name can be used but the value must be the correct type | [optional] |

## ObjWithRequiredPropsMap
public static class ObjWithRequiredPropsMap<br>
extends FrozenMap<String, Object>

A class to store validated Map payloads

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| static [ObjWithRequiredPropsMap](#objwithrequiredpropsmap) | of([Map<String, Object>](#objwithrequiredpropsmapinput) arg, SchemaConfiguration configuration) |
| String | a()<br> |
| Object | getAdditionalProperty(String name)<br>provides type safety for additional properties |

## A
public static class A<br>
extends StringJsonSchema

A schema class that validates payloads

| Methods Inherited from class org.openapijsonschematools.client.schemas.StringJsonSchema |
| ------------------------------------------------------------------ |
| validate                                                           |

[[Back to top]](#top) [[Back to Component Schemas]](../../../README.md#Component-Schemas) [[Back to README]](../../../README.md)
