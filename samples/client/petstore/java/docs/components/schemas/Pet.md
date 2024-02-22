# Pet
org.openapijsonschematools.client.components.schemas.Pet.java
public class Pet<br>

A class that contains necessary nested
- schema classes (which validate payloads), extends JsonSchema
- sealed interfaces which store validated payloads, java version of a sum type
- boxed classes which store validated payloads, sealed permits class implementations
- classes to store validated list payloads, extends FrozenList
- classes to build inputs for list payloads
- classes to store validated map payloads, extends FrozenMap
- classes to build inputs for map payloads
- enum classes

## Nested Class Summary
| Modifier and Type | Class and Description |
| ----------------- | ---------------------- |
| sealed interface | [Pet.Pet1Boxed](#pet1boxed)<br> sealed interface for validated payloads |
| record | [Pet.Pet1BoxedMap](#pet1boxedmap)<br> boxed class to store validated Map payloads |
| static class | [Pet.Pet1](#pet1)<br> schema class |
| static class | [Pet.PetMapBuilder](#petmapbuilder)<br> builder for Map payloads |
| static class | [Pet.PetMap](#petmap)<br> output class for Map payloads |
| sealed interface | [Pet.TagsBoxed](#tagsboxed)<br> sealed interface for validated payloads |
| record | [Pet.TagsBoxedList](#tagsboxedlist)<br> boxed class to store validated List payloads |
| static class | [Pet.Tags](#tags)<br> schema class |
| static class | [Pet.TagsListBuilder](#tagslistbuilder)<br> builder for List payloads |
| static class | [Pet.TagsList](#tagslist)<br> output class for List payloads |
| sealed interface | [Pet.StatusBoxed](#statusboxed)<br> sealed interface for validated payloads |
| record | [Pet.StatusBoxedString](#statusboxedstring)<br> boxed class to store validated String payloads |
| static class | [Pet.Status](#status)<br> schema class |
| enum | [Pet.StringStatusEnums](#stringstatusenums)<br>String enum |
| sealed interface | [Pet.PhotoUrlsBoxed](#photourlsboxed)<br> sealed interface for validated payloads |
| record | [Pet.PhotoUrlsBoxedList](#photourlsboxedlist)<br> boxed class to store validated List payloads |
| static class | [Pet.PhotoUrls](#photourls)<br> schema class |
| static class | [Pet.PhotoUrlsListBuilder](#photourlslistbuilder)<br> builder for List payloads |
| static class | [Pet.PhotoUrlsList](#photourlslist)<br> output class for List payloads |
| sealed interface | [Pet.ItemsBoxed](#itemsboxed)<br> sealed interface for validated payloads |
| record | [Pet.ItemsBoxedString](#itemsboxedstring)<br> boxed class to store validated String payloads |
| static class | [Pet.Items](#items)<br> schema class |
| sealed interface | [Pet.NameBoxed](#nameboxed)<br> sealed interface for validated payloads |
| record | [Pet.NameBoxedString](#nameboxedstring)<br> boxed class to store validated String payloads |
| static class | [Pet.Name](#name)<br> schema class |
| sealed interface | [Pet.IdBoxed](#idboxed)<br> sealed interface for validated payloads |
| record | [Pet.IdBoxedNumber](#idboxednumber)<br> boxed class to store validated Number payloads |
| static class | [Pet.Id](#id)<br> schema class |

## Pet1Boxed
public sealed interface Pet1Boxed<br>
permits<br>
[Pet1BoxedMap](#pet1boxedmap)

sealed interface that stores validated payloads using boxed classes

## Pet1BoxedMap
public record Pet1BoxedMap<br>
implements [Pet1Boxed](#pet1boxed)

record that stores validated Map payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| Pet1BoxedMap([PetMap](#petmap) data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| [PetMap](#petmap) | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## Pet1
public static class Pet1<br>
extends JsonSchema

A schema class that validates payloads

## Description
Pet object that needs to be added to the store

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
Pet.PetMap validatedPayload =
    Pet.Pet1.validate(
    new Pet.PetMapBuilder()
        .name("a")

        .photoUrls(
            Arrays.asList(
                "a"
            )
        )
        .id(1L)

        .category(
            MapUtils.makeMap(
                new AbstractMap.SimpleEntry<String, Object>(
                    "name",
                    "a"
                ),
                new AbstractMap.SimpleEntry<String, Object>(
                    "id",
                    1L
                )
            )
        )
        .tags(
            Arrays.asList(
                MapUtils.makeMap(
                    new AbstractMap.SimpleEntry<String, String>(
                        "name",
                        "a"
                    )
                )
            )
        )
        .status("available")

    .build(),
    configuration
);
```

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Set<Class<?>> | type = Set.of(Map.class) |
| Map<String, Class<? extends JsonSchema>> | properties = Map.ofEntries(<br>&nbsp;&nbsp;&nbsp;&nbsp;new PropertyEntry("id", [Id.class](#id))),<br>&nbsp;&nbsp;&nbsp;&nbsp;new PropertyEntry("category", [Category.Category1.class](../../components/schemas/Category.md#category1)),<br>&nbsp;&nbsp;&nbsp;&nbsp;new PropertyEntry("name", [Name.class](#name))),<br>&nbsp;&nbsp;&nbsp;&nbsp;new PropertyEntry("photoUrls", [PhotoUrls.class](#photourls))),<br>&nbsp;&nbsp;&nbsp;&nbsp;new PropertyEntry("tags", [Tags.class](#tags))),<br>&nbsp;&nbsp;&nbsp;&nbsp;new PropertyEntry("status", [Status.class](#status)))<br>)<br> |
| Set<String> | required = Set.of(<br>&nbsp;&nbsp;&nbsp;&nbsp;"name",<br>&nbsp;&nbsp;&nbsp;&nbsp;"photoUrls"<br>)<br> |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| [PetMap](#petmap) | validate([Map&lt;?, ?&gt;](#petmapbuilder) arg, SchemaConfiguration configuration) |
| [Pet1BoxedMap](#pet1boxedmap) | validateAndBox([Map&lt;?, ?&gt;](#petmapbuilder) arg, SchemaConfiguration configuration) |
| [Pet1Boxed](#pet1boxed) | validateAndBox(@Nullable Object arg, SchemaConfiguration configuration) |
| @Nullable Object | validate(@Nullable Object arg, SchemaConfiguration configuration) |

## PetMap00Builder
public class PetMap00Builder<br>
builder for `Map<String, @Nullable Object>`

A class that builds the Map input type

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| PetMap00Builder(Map<String, @Nullable Object> instance)<br>Creates a builder that contains the passed instance |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| Map<String, @Nullable Object> | build()<br>Returns map input that should be used with Schema.validate |
| [PetMap00Builder](#petmap00builder) | id(int value) |
| [PetMap00Builder](#petmap00builder) | id(float value) |
| [PetMap00Builder](#petmap00builder) | id(long value) |
| [PetMap00Builder](#petmap00builder) | id(double value) |
| [PetMap00Builder](#petmap00builder) | category(Map<String, @Nullable Object> value) |
| [PetMap00Builder](#petmap00builder) | tags(List<Map<String, @Nullable Object>> value) |
| [PetMap00Builder](#petmap00builder) | status(String value) |
| [PetMap00Builder](#petmap00builder) | status([StringStatusEnums](#stringstatusenums) value) |
| [PetMap00Builder](#petmap00builder) | additionalProperty(String key, Void value) |
| [PetMap00Builder](#petmap00builder) | additionalProperty(String key, boolean value) |
| [PetMap00Builder](#petmap00builder) | additionalProperty(String key, String value) |
| [PetMap00Builder](#petmap00builder) | additionalProperty(String key, int value) |
| [PetMap00Builder](#petmap00builder) | additionalProperty(String key, float value) |
| [PetMap00Builder](#petmap00builder) | additionalProperty(String key, long value) |
| [PetMap00Builder](#petmap00builder) | additionalProperty(String key, double value) |
| [PetMap00Builder](#petmap00builder) | additionalProperty(String key, List<?> value) |
| [PetMap00Builder](#petmap00builder) | additionalProperty(String key, Map<String, ?> value) |

## PetMap01Builder
public class PetMap01Builder<br>
builder for `Map<String, @Nullable Object>`

A class that builds the Map input type

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| PetMap01Builder(Map<String, @Nullable Object> instance)<br>Creates a builder that contains the passed instance |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| [PetMap00Builder](#petmap00builder) | photoUrls(List<String> value) |

## PetMap10Builder
public class PetMap10Builder<br>
builder for `Map<String, @Nullable Object>`

A class that builds the Map input type

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| PetMap10Builder(Map<String, @Nullable Object> instance)<br>Creates a builder that contains the passed instance |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| [PetMap00Builder](#petmap00builder) | name(String value) |

## PetMapBuilder
public class PetMapBuilder<br>
builder for `Map<String, @Nullable Object>`

A class that builds the Map input type

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| PetMapBuilder()<br>Creates a builder that contains an empty map |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| [PetMap01Builder](#petmap01builder) | name(String value) |
| [PetMap10Builder](#petmap10builder) | photoUrls(List<String> value) |

## PetMap
public static class PetMap<br>
extends FrozenMap<String, @Nullable Object>

A class to store validated Map payloads

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| static [PetMap](#petmap) | of([Map<String, ? extends @Nullable Object>](#petmapbuilder) arg, SchemaConfiguration configuration) |
| String | name()<br> |
| [PhotoUrlsList](#photourlslist) | photoUrls()<br> |
| Number | id()<br>[optional] value must be a 64 bit integer |
| [Category.CategoryMap](../../components/schemas/Category.md#categorymap) | category()<br>[optional] |
| [TagsList](#tagslist) | tags()<br>[optional] |
| String | status()<br>[optional] must be one of ["available", "pending", "sold"] |
| @Nullable Object | getAdditionalProperty(String name)<br>provides type safety for additional properties |

## TagsBoxed
public sealed interface TagsBoxed<br>
permits<br>
[TagsBoxedList](#tagsboxedlist)

sealed interface that stores validated payloads using boxed classes

## TagsBoxedList
public record TagsBoxedList<br>
implements [TagsBoxed](#tagsboxed)

record that stores validated List payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| TagsBoxedList([TagsList](#tagslist) data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| [TagsList](#tagslist) | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## Tags
public static class Tags<br>
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

// List validation
Pet.TagsList validatedPayload =
    Pet.Tags.validate(
    new Pet.TagsListBuilder()
        .add(
            MapUtils.makeMap(
                new AbstractMap.SimpleEntry<String, Object>(
                    "id",
                    1L
                ),
                new AbstractMap.SimpleEntry<String, Object>(
                    "name",
                    "a"
                )
            )
        )
    .build(),
    configuration
);
```

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Set<Class<?>> | type = Set.of(List.class) |
| Class<? extends JsonSchema> | items = [Tag.Tag1.class](../../components/schemas/Tag.md#tag1) |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| [TagsList](#tagslist) | validate([List<?>](#tagslistbuilder) arg, SchemaConfiguration configuration) |
| [TagsBoxedList](#tagsboxedlist) | validateAndBox([List<?>](#tagslistbuilder) arg, SchemaConfiguration configuration) |
| [TagsBoxed](#tagsboxed) | validateAndBox(@Nullable Object arg, SchemaConfiguration configuration) |
| @Nullable Object | validate(@Nullable Object arg, SchemaConfiguration configuration) |

## TagsListBuilder
public class TagsListBuilder<br>
builder for `List<Map<String, @Nullable Object>>`

A class that builds the List input type

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| TagsListBuilder()<br>Creates an empty list |
| TagsListBuilder(List<Map<String, @Nullable Object>> items)<br>Stores the items in a list |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| TagsListBuilder | add(Map<String, @Nullable Object> item) |
| List<Map<String, @Nullable Object>> | build()<br>Returns list input that should be used with Schema.validate |

## TagsList
public class TagsList<br>
extends `FrozenList<Tag.TagMap>`

A class to store validated List payloads

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| static [TagsList](#tagslist) | of([List<Map<String, ? extends @Nullable Object>>](#tagslistbuilder) arg, SchemaConfiguration configuration) |

## StatusBoxed
public sealed interface StatusBoxed<br>
permits<br>
[StatusBoxedString](#statusboxedstring)

sealed interface that stores validated payloads using boxed classes

## StatusBoxedString
public record StatusBoxedString<br>
implements [StatusBoxed](#statusboxed)

record that stores validated String payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| StatusBoxedString(String data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| String | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## Status
public static class Status<br>
extends JsonSchema

A schema class that validates payloads

## Description
pet status in the store

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
String validatedPayload = Pet.Status.validate(
    "available",
    configuration
);
```

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Set<Class<?>> | type = Set.of(<br/>&nbsp;&nbsp;&nbsp;&nbsp;String.class<br/>)<br/> |
| Set<Object> | enumValues = SetMaker.makeSet(<br>&nbsp;&nbsp;&nbsp;&nbsp;"available",<br>&nbsp;&nbsp;&nbsp;&nbsp;"pending",<br>&nbsp;&nbsp;&nbsp;&nbsp;"sold"<br>)<br> |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| String | validate(String arg, SchemaConfiguration configuration) |
| String | validate([StringStatusEnums](#stringstatusenums) arg, SchemaConfiguration configuration) |
| [StatusBoxedString](#statusboxedstring) | validateAndBox(String arg, SchemaConfiguration configuration) |
| [StatusBoxed](#statusboxed) | validateAndBox(@Nullable Object arg, SchemaConfiguration configuration) |
| @Nullable Object | validate(@Nullable Object arg, SchemaConfiguration configuration) |

## StringStatusEnums
public enum StringStatusEnums<br>
extends `Enum<StringStatusEnums>`

A class that stores String enum values

### Enum Constant Summary
| Enum Constant | Description |
| ------------- | ----------- |
| AVAILABLE | value = "available" |
| PENDING | value = "pending" |
| SOLD | value = "sold" |

## PhotoUrlsBoxed
public sealed interface PhotoUrlsBoxed<br>
permits<br>
[PhotoUrlsBoxedList](#photourlsboxedlist)

sealed interface that stores validated payloads using boxed classes

## PhotoUrlsBoxedList
public record PhotoUrlsBoxedList<br>
implements [PhotoUrlsBoxed](#photourlsboxed)

record that stores validated List payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| PhotoUrlsBoxedList([PhotoUrlsList](#photourlslist) data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| [PhotoUrlsList](#photourlslist) | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## PhotoUrls
public static class PhotoUrls<br>
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

// List validation
Pet.PhotoUrlsList validatedPayload =
    Pet.PhotoUrls.validate(
    new Pet.PhotoUrlsListBuilder()
        .add("a")

    .build(),
    configuration
);
```

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Set<Class<?>> | type = Set.of(List.class) |
| Class<? extends JsonSchema> | items = [Items.class](#items) |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| [PhotoUrlsList](#photourlslist) | validate([List<?>](#photourlslistbuilder) arg, SchemaConfiguration configuration) |
| [PhotoUrlsBoxedList](#photourlsboxedlist) | validateAndBox([List<?>](#photourlslistbuilder) arg, SchemaConfiguration configuration) |
| [PhotoUrlsBoxed](#photourlsboxed) | validateAndBox(@Nullable Object arg, SchemaConfiguration configuration) |
| @Nullable Object | validate(@Nullable Object arg, SchemaConfiguration configuration) |

## PhotoUrlsListBuilder
public class PhotoUrlsListBuilder<br>
builder for `List<String>`

A class that builds the List input type

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| PhotoUrlsListBuilder()<br>Creates an empty list |
| PhotoUrlsListBuilder(List<String> items)<br>Stores the items in a list |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| PhotoUrlsListBuilder | add(String item) |
| List<String> | build()<br>Returns list input that should be used with Schema.validate |

## PhotoUrlsList
public class PhotoUrlsList<br>
extends `FrozenList<String>`

A class to store validated List payloads

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| static [PhotoUrlsList](#photourlslist) | of([List<String>](#photourlslistbuilder) arg, SchemaConfiguration configuration) |

## ItemsBoxed
public sealed interface ItemsBoxed<br>
permits<br>
[ItemsBoxedString](#itemsboxedstring)

sealed interface that stores validated payloads using boxed classes

## ItemsBoxedString
public record ItemsBoxedString<br>
implements [ItemsBoxed](#itemsboxed)

record that stores validated String payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| ItemsBoxedString(String data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| String | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## Items
public static class Items<br>
extends StringJsonSchema.StringJsonSchema1

A schema class that validates payloads

| Methods Inherited from class org.openapijsonschematools.client.schemas.StringJsonSchema.StringJsonSchema1 |
| ------------------------------------------------------------------ |
| validate                                                           |
| validateAndBox                                                     |

## NameBoxed
public sealed interface NameBoxed<br>
permits<br>
[NameBoxedString](#nameboxedstring)

sealed interface that stores validated payloads using boxed classes

## NameBoxedString
public record NameBoxedString<br>
implements [NameBoxed](#nameboxed)

record that stores validated String payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| NameBoxedString(String data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| String | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## Name
public static class Name<br>
extends StringJsonSchema.StringJsonSchema1

A schema class that validates payloads

| Methods Inherited from class org.openapijsonschematools.client.schemas.StringJsonSchema.StringJsonSchema1 |
| ------------------------------------------------------------------ |
| validate                                                           |
| validateAndBox                                                     |

## IdBoxed
public sealed interface IdBoxed<br>
permits<br>
[IdBoxedNumber](#idboxednumber)

sealed interface that stores validated payloads using boxed classes

## IdBoxedNumber
public record IdBoxedNumber<br>
implements [IdBoxed](#idboxed)

record that stores validated Number payloads, sealed permits implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| IdBoxedNumber(Number data)<br>Creates an instance, private visibility |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| Number | data()<br>validated payload |
| @Nullable Object | getData()<br>validated payload |

## Id
public static class Id<br>
extends Int64JsonSchema.Int64JsonSchema1

A schema class that validates payloads

| Methods Inherited from class org.openapijsonschematools.client.schemas.Int64JsonSchema.Int64JsonSchema1 |
| ------------------------------------------------------------------ |
| validate                                                           |
| validateAndBox                                                     |

[[Back to top]](#top) [[Back to Component Schemas]](../../../README.md#Component-Schemas) [[Back to README]](../../../README.md)
