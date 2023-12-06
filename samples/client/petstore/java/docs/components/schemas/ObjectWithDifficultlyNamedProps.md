# ObjectWithDifficultlyNamedProps
org.openapijsonschematools.client.components.schemas.ObjectWithDifficultlyNamedProps.java
public class ObjectWithDifficultlyNamedProps

A class that contains necessary nested schema classes, and classes to store validated list and map payloads

## Nested Class Summary
| Modifier and Type | Class and Description |
| ----------------- | ---------------------- |
| static class | [ObjectWithDifficultlyNamedProps.ObjectWithDifficultlyNamedProps1](#objectwithdifficultlynamedprops1)<br> schema class |
| static class | [ObjectWithDifficultlyNamedProps.ObjectWithDifficultlyNamedPropsMap](#objectwithdifficultlynamedpropsmap)<br> output class for Map payloads |
| static class | [ObjectWithDifficultlyNamedProps.Schema123Number](#schema123number)<br> schema class |
| static class | [ObjectWithDifficultlyNamedProps.Schema123list](#schema123list)<br> schema class |
| static class | [ObjectWithDifficultlyNamedProps.Specialpropertyname](#specialpropertyname)<br> schema class |

## ObjectWithDifficultlyNamedProps1
public static class ObjectWithDifficultlyNamedProps1<br>
extends JsonSchema

A schema class that validates payloads

## Description
model with properties that have invalid names for python

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
ObjectWithDifficultlyNamedProps.ObjectWithDifficultlyNamedPropsMap validatedPayload =
    ObjectWithDifficultlyNamedProps.ObjectWithDifficultlyNamedProps1.validate(
    MapMaker.makeMap(
        new AbstractMap.SimpleEntry<>(
            "123-list",
            "a"
        ),
        new AbstractMap.SimpleEntry<>(
            "$special[property.name]",
            1L
        ),
        new AbstractMap.SimpleEntry<>(
            "123Number",
            1L
        )
    ),
    configuration
);
```

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| static LinkedHashMap<String, KeywordValidator> |keywordToValidator<br/>new LinkedHashMap<>(Map.ofEntries(<br/>&nbsp;&nbsp;&nbsp;&nbsp;new KeywordEntry("type", new TypeValidator(Set.of(FrozenMap.class))),<br/>&nbsp;&nbsp;&nbsp;&nbsp;new KeywordEntry("properties", new PropertiesValidator(Map.ofEntries(<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;new PropertyEntry("$special[property.name]", [Specialpropertyname.class](#specialpropertyname))),<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;new PropertyEntry("123-list", [Schema123list.class](#schema123list))),<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;new PropertyEntry("123Number", [Schema123Number.class](#schema123number)))<br>&nbsp;&nbsp;&nbsp;&nbsp;))),<br>&nbsp;&nbsp;&nbsp;&nbsp;new KeywordEntry("required", new RequiredValidator(Set.of(<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"123-list"<br>&nbsp;&nbsp;&nbsp;&nbsp;)))<br>)); |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| static [ObjectWithDifficultlyNamedPropsMap](#objectwithdifficultlynamedpropsmap) | validate(Map<String, Object> arg, SchemaConfiguration configuration) |

## ObjectWithDifficultlyNamedPropsMap
public static class ObjectWithDifficultlyNamedPropsMap<br>
extends FrozenMap<String, Object>

A class to store validated Map payloads

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| static [ObjectWithDifficultlyNamedPropsMap](#objectwithdifficultlynamedpropsmap) | of(Map<String, Object> arg, SchemaConfiguration configuration) |
| Object | get(String key)<br>This schema has invalid Java names so this method must be used when you access instance["123-list"], instance["$special[property.name]"], instance["123Number"],  |
| Object | getAdditionalProperty(String name)<br>provides type safety for additional properties |

## Input Map Keys
```
type: Map<String, Object>
```
| Key | Type |  Description | Notes |
| --- | ---- | ------------ | ----- |
| **123-list** | String |  | |
| **$special[property.name]** | long |  | [optional] value must be a 64 bit integer |
| **123Number** | long |  | [optional] |
| **anyStringName** | Object | any string name can be used but the value must be the correct type | [optional] |

## Schema123Number
public static class Schema123Number<br>
extends IntJsonSchema

A schema class that validates payloads

| Methods Inherited from class org.openapijsonschematools.client.schemas.IntJsonSchema |
| ------------------------------------------------------------------ |
| validate                                                           |

## Schema123list
public static class Schema123list<br>
extends StringJsonSchema

A schema class that validates payloads

| Methods Inherited from class org.openapijsonschematools.client.schemas.StringJsonSchema |
| ------------------------------------------------------------------ |
| validate                                                           |

## Specialpropertyname
public static class Specialpropertyname<br>
extends Int64JsonSchema

A schema class that validates payloads

| Methods Inherited from class org.openapijsonschematools.client.schemas.Int64JsonSchema |
| ------------------------------------------------------------------ |
| validate                                                           |

[[Back to top]](#top) [[Back to Component Schemas]](../../../README.md#Component-Schemas) [[Back to README]](../../../README.md)
