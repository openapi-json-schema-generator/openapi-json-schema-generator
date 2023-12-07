# ArrayOfArrayOfNumberOnly
org.openapijsonschematools.client.components.schemas.ArrayOfArrayOfNumberOnly.java
public class ArrayOfArrayOfNumberOnly

A class that contains necessary nested
- schema classes (which validate payloads), extends JsonSchema
- classes to store validated list payloads, extends FrozenList
- classes to store validated map payloads, extends FrozenMap
- classes to build inputs for list payloads

## Nested Class Summary
| Modifier and Type | Class and Description |
| ----------------- | ---------------------- |
| static class | [ArrayOfArrayOfNumberOnly.ArrayOfArrayOfNumberOnly1](#arrayofarrayofnumberonly1)<br> schema class |
| static class | [ArrayOfArrayOfNumberOnly.ArrayOfArrayOfNumberOnlyMap](#arrayofarrayofnumberonlymap)<br> output class for Map payloads |
| static class | [ArrayOfArrayOfNumberOnly.ArrayArrayNumber](#arrayarraynumber)<br> schema class |
| static class | [ArrayOfArrayOfNumberOnly.ArrayArrayNumberListInput](#arrayarraynumberlistinput)<br> builder for List payloads |
| static class | [ArrayOfArrayOfNumberOnly.ArrayArrayNumberList](#arrayarraynumberlist)<br> output class for List payloads |
| static class | [ArrayOfArrayOfNumberOnly.Items](#items)<br> schema class |
| static class | [ArrayOfArrayOfNumberOnly.ItemsListInput](#itemslistinput)<br> builder for List payloads |
| static class | [ArrayOfArrayOfNumberOnly.ItemsList](#itemslist)<br> output class for List payloads |
| static class | [ArrayOfArrayOfNumberOnly.Items1](#items1)<br> schema class |

## ArrayOfArrayOfNumberOnly1
public static class ArrayOfArrayOfNumberOnly1<br>
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
ArrayOfArrayOfNumberOnly.ArrayOfArrayOfNumberOnlyMap validatedPayload =
    ArrayOfArrayOfNumberOnly.ArrayOfArrayOfNumberOnly1.validate(
    MapMaker.makeMap(
        new AbstractMap.SimpleEntry<>(
            "ArrayArrayNumber",
            Arrays.asList(
                Arrays.asList(
                    1
                )
            )
        )
    ),
    configuration
);
```

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| static LinkedHashMap<String, KeywordValidator> |keywordToValidator<br/>new LinkedHashMap<>(Map.ofEntries(<br/>&nbsp;&nbsp;&nbsp;&nbsp;new KeywordEntry("type", new TypeValidator(Set.of(FrozenMap.class))),<br/>&nbsp;&nbsp;&nbsp;&nbsp;new KeywordEntry("properties", new PropertiesValidator(Map.ofEntries(<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;new PropertyEntry("ArrayArrayNumber", [ArrayArrayNumber.class](#arrayarraynumber)))<br>&nbsp;&nbsp;&nbsp;&nbsp;)))<br>)); |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| static [ArrayOfArrayOfNumberOnlyMap](#arrayofarrayofnumberonlymap) | validate(Map<String, Object> arg, SchemaConfiguration configuration) |

## ArrayOfArrayOfNumberOnlyMap
public static class ArrayOfArrayOfNumberOnlyMap<br>
extends FrozenMap<String, Object>

A class to store validated Map payloads

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| static [ArrayOfArrayOfNumberOnlyMap](#arrayofarrayofnumberonlymap) | of(Map<String, Object> arg, SchemaConfiguration configuration) |
| [ArrayArrayNumberList](#arrayarraynumberlist) | ArrayArrayNumber()<br>[optional] |
| Object | getAdditionalProperty(String name)<br>provides type safety for additional properties |

## Input Map Keys
```
type: Map<String, Object>
```
| Key | Type |  Description | Notes |
| --- | ---- | ------------ | ----- |
| **ArrayArrayNumber** | List<List<Number>> |  | [optional] |
| **anyStringName** | Object | any string name can be used but the value must be the correct type | [optional] |

## ArrayArrayNumber
public static class ArrayArrayNumber<br>
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
ArrayOfArrayOfNumberOnly.ArrayArrayNumberList validatedPayload =
    ArrayOfArrayOfNumberOnly.ArrayArrayNumber.validate(
    Arrays.asList(
        Arrays.asList(
            1
        )
    ),
    configuration
);
```

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| static LinkedHashMap<String, KeywordValidator> |keywordToValidator<br/>new LinkedHashMap<>(Map.ofEntries(<br/>&nbsp;&nbsp;&nbsp;&nbsp;new KeywordEntry("type", new TypeValidator(Set.of(FrozenList.class))),<br/>&nbsp;&nbsp;&nbsp;&nbsp;new KeywordEntry("items", new ItemsValidator([Items.class](#items)))<br>)); |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| static [ArrayArrayNumberList](#arrayarraynumberlist) | validate([List<List<Number>>](#arrayarraynumberlistinput) arg, SchemaConfiguration configuration) |

## ArrayArrayNumberListInput
public class ArrayArrayNumberListInput<br>
builder for `List<List<Number>>`

A class that builds the List input type

## Input List Items
List Item Type | Description | Notes
-------------------- | ------------- | -------------
List<Number> |  |

## ArrayArrayNumberList
public class ArrayArrayNumberList<br>
extends `FrozenList<ItemsList>`

A class to store validated List payloads

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| static [ArrayArrayNumberList](#arrayarraynumberlist) | of([List<List<Number>>](#arrayarraynumberlistinput) arg, SchemaConfiguration configuration) |

## Items
public static class Items<br>
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
ArrayOfArrayOfNumberOnly.ItemsList validatedPayload =
    ArrayOfArrayOfNumberOnly.Items.validate(
    Arrays.asList(
        1
    ),
    configuration
);
```

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| static LinkedHashMap<String, KeywordValidator> |keywordToValidator<br/>new LinkedHashMap<>(Map.ofEntries(<br/>&nbsp;&nbsp;&nbsp;&nbsp;new KeywordEntry("type", new TypeValidator(Set.of(FrozenList.class))),<br/>&nbsp;&nbsp;&nbsp;&nbsp;new KeywordEntry("items", new ItemsValidator([Items1.class](#items1)))<br>)); |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| static [ItemsList](#itemslist) | validate([List<Number>](#itemslistinput) arg, SchemaConfiguration configuration) |

## ItemsListInput
public class ItemsListInput<br>
builder for `List<Number>`

A class that builds the List input type

## Input List Items
List Item Type | Description | Notes
-------------------- | ------------- | -------------
Number |  |

## ItemsList
public class ItemsList<br>
extends `FrozenList<Number>`

A class to store validated List payloads

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| static [ItemsList](#itemslist) | of([List<Number>](#itemslistinput) arg, SchemaConfiguration configuration) |

## Items1
public static class Items1<br>
extends NumberJsonSchema

A schema class that validates payloads

| Methods Inherited from class org.openapijsonschematools.client.schemas.NumberJsonSchema |
| ------------------------------------------------------------------ |
| validate                                                           |

[[Back to top]](#top) [[Back to Component Schemas]](../../../README.md#Component-Schemas) [[Back to README]](../../../README.md)
