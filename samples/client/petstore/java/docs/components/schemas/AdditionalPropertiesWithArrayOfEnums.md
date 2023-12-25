# AdditionalPropertiesWithArrayOfEnums
org.openapijsonschematools.client.components.schemas.AdditionalPropertiesWithArrayOfEnums.java
public class AdditionalPropertiesWithArrayOfEnums

A class that contains necessary nested
- schema classes (which validate payloads), extends JsonSchema
- classes to store validated list payloads, extends FrozenList
- classes to build inputs for list payloads
- classes to store validated map payloads, extends FrozenMap
- classes to build inputs for map payloads

## Nested Class Summary
| Modifier and Type | Class and Description |
| ----------------- | ---------------------- |
| static class | [AdditionalPropertiesWithArrayOfEnums.AdditionalPropertiesWithArrayOfEnums1](#additionalpropertieswitharrayofenums1)<br> schema class |
| static class | [AdditionalPropertiesWithArrayOfEnums.AdditionalPropertiesWithArrayOfEnumsMapInput](#additionalpropertieswitharrayofenumsmapinput)<br> builder for Map payloads |
| static class | [AdditionalPropertiesWithArrayOfEnums.AdditionalPropertiesWithArrayOfEnumsMap](#additionalpropertieswitharrayofenumsmap)<br> output class for Map payloads |
| static class | [AdditionalPropertiesWithArrayOfEnums.AdditionalProperties](#additionalproperties)<br> schema class |
| static class | [AdditionalPropertiesWithArrayOfEnums.AdditionalPropertiesListInput](#additionalpropertieslistinput)<br> builder for List payloads |
| static class | [AdditionalPropertiesWithArrayOfEnums.AdditionalPropertiesList](#additionalpropertieslist)<br> output class for List payloads |

## AdditionalPropertiesWithArrayOfEnums1
public static class AdditionalPropertiesWithArrayOfEnums1<br>
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
AdditionalPropertiesWithArrayOfEnums.AdditionalPropertiesWithArrayOfEnumsMap validatedPayload =
    AdditionalPropertiesWithArrayOfEnums.AdditionalPropertiesWithArrayOfEnums1.validate(
    MapMaker.makeMap(
    ),
    configuration
);
```

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Set<Class<?>> | &nbsp;&nbsp;&nbsp;&nbsp;type = Set.of(Map.class)<br/> |
| Class<? extends JsonSchema> | &nbsp;&nbsp;&nbsp;&nbsp;additionalProperties = [AdditionalProperties.class](#additionalproperties)<br> |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| [AdditionalPropertiesWithArrayOfEnumsMap](#additionalpropertieswitharrayofenumsmap) | validate([Map<?, ?>](#additionalpropertieswitharrayofenumsmapinput) arg, SchemaConfiguration configuration) |
| @Nullable Object | validate(@Nullable Object arg, SchemaConfiguration configuration) |
## AdditionalPropertiesWithArrayOfEnumsMapInput
public class AdditionalPropertiesWithArrayOfEnumsMapInput<br>
builder for `Map<String, List<String>>`

A class that builds the Map input type

## Input Map Keys
| Key | Type |  Description | Notes |
| --- | ---- | ------------ | ----- |
| **anyStringName** | List<String> | any string name can be used but the value must be the correct type | [optional] |

## AdditionalPropertiesWithArrayOfEnumsMap
public static class AdditionalPropertiesWithArrayOfEnumsMap<br>
extends FrozenMap<String, AdditionalPropertiesList>

A class to store validated Map payloads

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| static [AdditionalPropertiesWithArrayOfEnumsMap](#additionalpropertieswitharrayofenumsmap) | of([Map<String, List<String>>](#additionalpropertieswitharrayofenumsmapinput) arg, SchemaConfiguration configuration) |
| [AdditionalPropertiesList](#additionalpropertieslist) | getAdditionalProperty(String name)<br>provides type safety for additional properties |

## AdditionalProperties
public static class AdditionalProperties<br>
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

// List validation
AdditionalPropertiesWithArrayOfEnums.AdditionalPropertiesList validatedPayload =
    AdditionalPropertiesWithArrayOfEnums.AdditionalProperties.validate(
    Arrays.asList(
        "_abc"
    ),
    configuration
);
```

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Set<Class<?>> | &nbsp;&nbsp;&nbsp;&nbsp;type = Set.of(List.class)<br/> |
| Class<? extends JsonSchema> | &nbsp;&nbsp;&nbsp;&nbsp;items = [EnumClass.EnumClass1.class](../../components/schemas/EnumClass.md#enumclass1)<br> |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| [AdditionalPropertiesList](#additionalpropertieslist) | validate([List<?>](#additionalpropertieslistinput) arg, SchemaConfiguration configuration) |
| @Nullable Object | validate(@Nullable Object arg, SchemaConfiguration configuration) |
## AdditionalPropertiesListInput
public class AdditionalPropertiesListInput<br>
builder for `List<String>`

A class that builds the List input type

## Input List Items
List Item Type | Description | Notes
-------------------- | ------------- | -------------
String |  |

## AdditionalPropertiesList
public class AdditionalPropertiesList<br>
extends `FrozenList<String>`

A class to store validated List payloads

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| static [AdditionalPropertiesList](#additionalpropertieslist) | of([List<String>](#additionalpropertieslistinput) arg, SchemaConfiguration configuration) |

[[Back to top]](#top) [[Back to Component Schemas]](../../../README.md#Component-Schemas) [[Back to README]](../../../README.md)
