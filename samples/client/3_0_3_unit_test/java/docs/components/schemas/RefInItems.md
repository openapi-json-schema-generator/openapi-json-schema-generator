# RefInItems
org.openapijsonschematools.client.components.schemas.RefInItems.java
public class RefInItems

A class that contains necessary nested
- schema classes (which validate payloads), extends JsonSchema
- abstract sealed classes which store validated payloads, java version of a sum type
- boxed classes which store validated payloads, sealed permits class implementations
- classes to store validated list payloads, extends FrozenList
- classes to build inputs for list payloads

## Nested Class Summary
| Modifier and Type | Class and Description |
| ----------------- | ---------------------- |
| static class | [RefInItems.RefInItems1Boxed](#refinitems1boxed)<br> abstract sealed validated payload class |
| static class | [RefInItems.RefInItems1BoxedList](#refinitems1boxedlist)<br> boxed class to store validated List payloads |
| static class | [RefInItems.RefInItems1](#refinitems1)<br> schema class |
| static class | [RefInItems.RefInItemsListBuilder](#refinitemslistbuilder)<br> builder for List payloads |
| static class | [RefInItems.RefInItemsList](#refinitemslist)<br> output class for List payloads |

## RefInItems1Boxed
public static abstract sealed class RefInItems1Boxed<br>
permits<br>
[RefInItems1BoxedList](#refinitems1boxedlist)

abstract sealed class that stores validated payloads using boxed classes

## RefInItems1BoxedList
public static final class RefInItems1BoxedList<br>
extends [RefInItems1Boxed](#refinitems1boxed)

a boxed class to store validated List payloads, sealed permits class implementation

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| RefInItems1BoxedList([RefInItemsList](#refinitemslist) data)<br>Creates an instance, private visibility |

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| [RefInItemsList](#refinitemslist) | data<br>validated payload |

## RefInItems1
public static class RefInItems1<br>
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
RefInItems.RefInItemsList validatedPayload =
    RefInItems.RefInItems1.validate(
    new RefInItems.RefInItemsListBuilder()
    .build(),
    configuration
);
```

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Set<Class<?>> | type = Set.of(List.class) |
| Class<? extends JsonSchema> | items = [PropertyNamedRefThatIsNotAReference.PropertyNamedRefThatIsNotAReference1.class](../../components/schemas/PropertyNamedRefThatIsNotAReference.md#propertynamedrefthatisnotareference1) |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| [RefInItemsList](#refinitemslist) | validate([List<?>](#refinitemslistbuilder) arg, SchemaConfiguration configuration) |
| [RefInItems1BoxedList](#refinitems1boxedlist) | validateAndBox([List<?>](#refinitemslistbuilder) arg, SchemaConfiguration configuration) |
| @Nullable Object | validate(@Nullable Object arg, SchemaConfiguration configuration) |
## RefInItemsListBuilder
public class RefInItemsListBuilder<br>
builder for `List<@Nullable Object>`

A class that builds the List input type

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| RefInItemsListBuilder()<br>Creates an empty list |
| RefInItemsListBuilder(List<@Nullable Object> items)<br>Stores the items in a list |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| RefInItemsListBuilder | add(Void item) |
| RefInItemsListBuilder | add(boolean item) |
| RefInItemsListBuilder | add(String item) |
| RefInItemsListBuilder | add(int item) |
| RefInItemsListBuilder | add(float item) |
| RefInItemsListBuilder | add(long item) |
| RefInItemsListBuilder | add(double item) |
| RefInItemsListBuilder | add(List<?> item) |
| RefInItemsListBuilder | add(Map<String, ?> item) |
| List<@Nullable Object> | build()<br>Returns list input that should be used with Schema.validate |

## RefInItemsList
public class RefInItemsList<br>
extends `FrozenList<@Nullable Object>`

A class to store validated List payloads

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| static [RefInItemsList](#refinitemslist) | of([List<? extends @Nullable Object>](#refinitemslistbuilder) arg, SchemaConfiguration configuration) |

[[Back to top]](#top) [[Back to Component Schemas]](../../../README.md#Component-Schemas) [[Back to README]](../../../README.md)
