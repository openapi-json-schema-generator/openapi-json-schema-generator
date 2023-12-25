# MyObjectDto
org.openapijsonschematools.client.components.schemas.MyObjectDto.java
public class MyObjectDto

A class that contains necessary nested
- schema classes (which validate payloads), extends JsonSchema
- classes to store validated map payloads, extends FrozenMap
- classes to build inputs for map payloads

## Nested Class Summary
| Modifier and Type | Class and Description |
| ----------------- | ---------------------- |
| static class | [MyObjectDto.MyObjectDto1](#myobjectdto1)<br> schema class |
| static class | [MyObjectDto.MyObjectDtoMapInput](#myobjectdtomapinput)<br> builder for Map payloads |
| static class | [MyObjectDto.MyObjectDtoMap](#myobjectdtomap)<br> output class for Map payloads |
| static class | [MyObjectDto.Id](#id)<br> schema class |
| static class | [MyObjectDto.AdditionalProperties](#additionalproperties)<br> schema class |

## MyObjectDto1
public static class MyObjectDto1<br>
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
MyObjectDto.MyObjectDtoMap validatedPayload =
    MyObjectDto.MyObjectDto1.validate(
    MapMaker.makeMap(
        new AbstractMap.SimpleEntry<>(
            "id",
            "046b6c7f-0b8a-43b9-b35d-6489e6daee91"
        )
    ),
    configuration
);
```

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Set<Class<?>> | &nbsp;&nbsp;&nbsp;&nbsp;type = Set.of(Map.class)<br/> |
| Map<String, Class<? extends JsonSchema>> | &nbsp;&nbsp;&nbsp;&nbsp;properties = Map.ofEntries(<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;new PropertyEntry("id", [Id.class](#id)))<br>&nbsp;&nbsp;&nbsp;&nbsp;)<br> |
| Class<? extends JsonSchema> | &nbsp;&nbsp;&nbsp;&nbsp;additionalProperties = [AdditionalProperties.class](#additionalproperties)<br> |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| [MyObjectDtoMap](#myobjectdtomap) | validate([Map<?, ?>](#myobjectdtomapinput) arg, SchemaConfiguration configuration) |
| @Nullable Object | validate(@Nullable Object arg, SchemaConfiguration configuration) |
## MyObjectDtoMapInput
public class MyObjectDtoMapInput<br>
builder for `Map<String, String>`

A class that builds the Map input type

## Input Map Keys
| Key | Type |  Description | Notes |
| --- | ---- | ------------ | ----- |
| **id** | String |  | [optional] value must be a uuid |

## MyObjectDtoMap
public static class MyObjectDtoMap<br>
extends FrozenMap<String, String>

A class to store validated Map payloads

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| static [MyObjectDtoMap](#myobjectdtomap) | of([Map<String, String>](#myobjectdtomapinput) arg, SchemaConfiguration configuration) |
| String | id()<br>[optional] value must be a uuid |

## Id
public static class Id<br>
extends UuidJsonSchema

A schema class that validates payloads

| Methods Inherited from class org.openapijsonschematools.client.schemas.UuidJsonSchema |
| ------------------------------------------------------------------ |
| validate                                                           |

## AdditionalProperties
public static class AdditionalProperties<br>
extends NotAnyTypeJsonSchema

A schema class that validates payloads

| Methods Inherited from class org.openapijsonschematools.client.schemas.NotAnyTypeJsonSchema |
| ------------------------------------------------------------------ |
| validate                                                           |

[[Back to top]](#top) [[Back to Component Schemas]](../../../README.md#Component-Schemas) [[Back to README]](../../../README.md)
