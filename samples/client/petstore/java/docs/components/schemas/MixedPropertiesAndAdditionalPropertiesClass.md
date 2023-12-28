# MixedPropertiesAndAdditionalPropertiesClass
org.openapijsonschematools.client.components.schemas.MixedPropertiesAndAdditionalPropertiesClass.java
public class MixedPropertiesAndAdditionalPropertiesClass

A class that contains necessary nested
- schema classes (which validate payloads), extends JsonSchema
- classes to store validated map payloads, extends FrozenMap
- classes to build inputs for map payloads

## Nested Class Summary
| Modifier and Type | Class and Description |
| ----------------- | ---------------------- |
| static class | [MixedPropertiesAndAdditionalPropertiesClass.MixedPropertiesAndAdditionalPropertiesClass1](#mixedpropertiesandadditionalpropertiesclass1)<br> schema class |
| static class | [MixedPropertiesAndAdditionalPropertiesClass.MixedPropertiesAndAdditionalPropertiesClassMapBuilder](#mixedpropertiesandadditionalpropertiesclassmapbuilder)<br> builder for Map payloads |
| static class | [MixedPropertiesAndAdditionalPropertiesClass.MixedPropertiesAndAdditionalPropertiesClassMap](#mixedpropertiesandadditionalpropertiesclassmap)<br> output class for Map payloads |
| static class | [MixedPropertiesAndAdditionalPropertiesClass.MapSchema](#mapschema)<br> schema class |
| static class | [MixedPropertiesAndAdditionalPropertiesClass.MapMapBuilder](#mapmapbuilder)<br> builder for Map payloads |
| static class | [MixedPropertiesAndAdditionalPropertiesClass.MapMap](#mapmap)<br> output class for Map payloads |
| static class | [MixedPropertiesAndAdditionalPropertiesClass.DateTime](#datetime)<br> schema class |
| static class | [MixedPropertiesAndAdditionalPropertiesClass.UuidSchema](#uuidschema)<br> schema class |

## MixedPropertiesAndAdditionalPropertiesClass1
public static class MixedPropertiesAndAdditionalPropertiesClass1<br>
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
MixedPropertiesAndAdditionalPropertiesClass.MixedPropertiesAndAdditionalPropertiesClassMap validatedPayload =
    MixedPropertiesAndAdditionalPropertiesClass.MixedPropertiesAndAdditionalPropertiesClass1.validate(
    MapMaker.makeMap(
        new AbstractMap.SimpleEntry<String, Object>(
            "uuid",
            "046b6c7f-0b8a-43b9-b35d-6489e6daee91"
        ),
        new AbstractMap.SimpleEntry<String, Object>(
            "dateTime",
            "1970-01-01T00:00:00.00Z"
        ),
        new AbstractMap.SimpleEntry<String, Object>(
            "map",
            MapMaker.makeMap(
            )
        )
    ),
    configuration
);
```

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Set<Class<?>> | type = Set.of(Map.class) |
| Map<String, Class<? extends JsonSchema>> | properties = Map.ofEntries(<br>&nbsp;&nbsp;&nbsp;&nbsp;new PropertyEntry("uuid", [UuidSchema.class](#uuidschema))),<br>&nbsp;&nbsp;&nbsp;&nbsp;new PropertyEntry("dateTime", [DateTime.class](#datetime))),<br>&nbsp;&nbsp;&nbsp;&nbsp;new PropertyEntry("map", [MapSchema.class](#mapschema)))<br>)<br> |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| [MixedPropertiesAndAdditionalPropertiesClassMap](#mixedpropertiesandadditionalpropertiesclassmap) | validate([Map<?, ?>](#mixedpropertiesandadditionalpropertiesclassmapbuilder) arg, SchemaConfiguration configuration) |
| @Nullable Object | validate(@Nullable Object arg, SchemaConfiguration configuration) |
## MixedPropertiesAndAdditionalPropertiesClassMapBuilder
public class MixedPropertiesAndAdditionalPropertiesClassMapBuilder<br>
builder for `Map<String, ? extends @Nullable Object>`

A class that builds the Map input type

## Input Map Keys
| Key | Type |  Description | Notes |
| --- | ---- | ------------ | ----- |
| **uuid** | String |  | [optional] value must be a uuid |
| **dateTime** | String |  | [optional] value must conform to RFC-3339 date-time |
| **map** | Map<String, Map<String, ? extends @Nullable Object>> |  | [optional] |
| **anyStringName** | Object | any string name can be used but the value must be the correct type | [optional] |

## MixedPropertiesAndAdditionalPropertiesClassMap
public static class MixedPropertiesAndAdditionalPropertiesClassMap<br>
extends FrozenMap<String, @Nullable Object>

A class to store validated Map payloads

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| static [MixedPropertiesAndAdditionalPropertiesClassMap](#mixedpropertiesandadditionalpropertiesclassmap) | of([Map<String, ? extends @Nullable Object>](#mixedpropertiesandadditionalpropertiesclassmapbuilder) arg, SchemaConfiguration configuration) |
| String | dateTime()<br>[optional] value must conform to RFC-3339 date-time |
| @Nullable Object | get(String key)<br>This schema has invalid Java names so this method must be used when you access instance["uuid"], instance["map"],  |
| Object | getAdditionalProperty(String name)<br>provides type safety for additional properties |

## MapSchema
public static class MapSchema<br>
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
MixedPropertiesAndAdditionalPropertiesClass.MapMap validatedPayload =
    MixedPropertiesAndAdditionalPropertiesClass.MapSchema.validate(
    MapMaker.makeMap(
    ),
    configuration
);
```

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Set<Class<?>> | type = Set.of(Map.class) |
| Class<? extends JsonSchema> | additionalProperties = [Animal.Animal1.class](../../components/schemas/Animal.md#animal1) |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| [MapMap](#mapmap) | validate([Map<?, ?>](#mapmapbuilder) arg, SchemaConfiguration configuration) |
| @Nullable Object | validate(@Nullable Object arg, SchemaConfiguration configuration) |
## MapMapBuilder
public class MapMapBuilder<br>
builder for `Map<String, Map<String, ? extends @Nullable Object>>`

A class that builds the Map input type

## Input Map Keys
| Key | Type |  Description | Notes |
| --- | ---- | ------------ | ----- |
| **anyStringName** | Map<String, ? extends @Nullable Object> | any string name can be used but the value must be the correct type | [optional] |

## MapMap
public static class MapMap<br>
extends FrozenMap<String, Animal.AnimalMap>

A class to store validated Map payloads

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| static [MapMap](#mapmap) | of([Map<String, Map<String, ? extends @Nullable Object>>](#mapmapbuilder) arg, SchemaConfiguration configuration) |
| [Animal.AnimalMap](../../components/schemas/Animal.md#animalmap) | getAdditionalProperty(String name)<br>provides type safety for additional properties |

## DateTime
public static class DateTime<br>
extends DateTimeJsonSchema

A schema class that validates payloads

| Methods Inherited from class org.openapijsonschematools.client.schemas.DateTimeJsonSchema |
| ------------------------------------------------------------------ |
| validate                                                           |

## UuidSchema
public static class UuidSchema<br>
extends UuidJsonSchema

A schema class that validates payloads

| Methods Inherited from class org.openapijsonschematools.client.schemas.UuidJsonSchema |
| ------------------------------------------------------------------ |
| validate                                                           |

[[Back to top]](#top) [[Back to Component Schemas]](../../../README.md#Component-Schemas) [[Back to README]](../../../README.md)
