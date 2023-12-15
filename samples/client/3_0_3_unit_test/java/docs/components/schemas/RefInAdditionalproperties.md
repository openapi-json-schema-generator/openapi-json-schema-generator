# RefInAdditionalproperties
org.openapijsonschematools.client.components.schemas.RefInAdditionalproperties.java
public class RefInAdditionalproperties

A class that contains necessary nested
- schema classes (which validate payloads), extends JsonSchema
- classes to store validated list payloads, extends FrozenList
- classes to store validated map payloads, extends FrozenMap
- classes to build inputs for list payloads
- classes to build inputs for map payloads

## Nested Class Summary
| Modifier and Type | Class and Description |
| ----------------- | ---------------------- |
| static class | [RefInAdditionalproperties.RefInAdditionalproperties1](#refinadditionalproperties1)<br> schema class |
| static class | [RefInAdditionalproperties.RefInAdditionalpropertiesMapInput](#refinadditionalpropertiesmapinput)<br> builder for Map payloads |
| static class | [RefInAdditionalproperties.RefInAdditionalpropertiesMap](#refinadditionalpropertiesmap)<br> output class for Map payloads |

## RefInAdditionalproperties1
public static class RefInAdditionalproperties1<br>
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
RefInAdditionalproperties.RefInAdditionalpropertiesMap validatedPayload =
    RefInAdditionalproperties.RefInAdditionalproperties1.validate(
    MapMaker.makeMap(
    ),
    configuration
);
```

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Set<Class<?>> | &nbsp;&nbsp;&nbsp;&nbsp;type = Set.of(FrozenMap.class)<br/> |
| Class<? extends JsonSchema> | &nbsp;&nbsp;&nbsp;&nbsp;additionalProperties = [PropertyNamedRefThatIsNotAReference.PropertyNamedRefThatIsNotAReference1.class](../../components/schemas/PropertyNamedRefThatIsNotAReference.md#propertynamedrefthatisnotareference1)<br> |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| static [RefInAdditionalpropertiesMap](#refinadditionalpropertiesmap) | validate([Map<String, Object>](#refinadditionalpropertiesmapinput) arg, SchemaConfiguration configuration) |

## RefInAdditionalpropertiesMapInput
public class RefInAdditionalpropertiesMapInput<br>
builder for `Map<String, Object>`

A class that builds the Map input type

## Input Map Keys
| Key | Type |  Description | Notes |
| --- | ---- | ------------ | ----- |
| **anyStringName** | Object | any string name can be used but the value must be the correct type | [optional] |

## RefInAdditionalpropertiesMap
public static class RefInAdditionalpropertiesMap<br>
extends FrozenMap<String, Object>

A class to store validated Map payloads

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| static [RefInAdditionalpropertiesMap](#refinadditionalpropertiesmap) | of([Map<String, Object>](#refinadditionalpropertiesmapinput) arg, SchemaConfiguration configuration) |
| Object | getAdditionalProperty(String name)<br>provides type safety for additional properties |

[[Back to top]](#top) [[Back to Component Schemas]](../../../README.md#Component-Schemas) [[Back to README]](../../../README.md)
