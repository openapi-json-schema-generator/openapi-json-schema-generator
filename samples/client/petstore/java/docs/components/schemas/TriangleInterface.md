# TriangleInterface
org.openapijsonschematools.client.components.schemas.TriangleInterface.java
public class TriangleInterface

A class that contains necessary nested
- schema classes (which validate payloads), extends JsonSchema
- classes to store validated map payloads, extends FrozenMap
- classes to build inputs for map payloads
- enum classes

## Nested Class Summary
| Modifier and Type | Class and Description |
| ----------------- | ---------------------- |
| static class | [TriangleInterface.TriangleInterface1](#triangleinterface1)<br> schema class |
| static class | [TriangleInterface.TriangleInterfaceMapBuilder](#triangleinterfacemapbuilder)<br> builder for Map payloads |
| static class | [TriangleInterface.TriangleInterfaceMap](#triangleinterfacemap)<br> output class for Map payloads |
| static class | [TriangleInterface.TriangleType](#triangletype)<br> schema class |
| static class | [TriangleInterface.ShapeType](#shapetype)<br> schema class |
| enum | [TriangleInterface.StringShapeTypeEnums](#stringshapetypeenums)<br>String enum |

## TriangleInterface1
public static class TriangleInterface1<br>
extends JsonSchema

A schema class that validates payloads

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Map<String, Class<? extends JsonSchema>> | properties = Map.ofEntries(<br>&nbsp;&nbsp;&nbsp;&nbsp;new PropertyEntry("shapeType", [ShapeType.class](#shapetype))),<br>&nbsp;&nbsp;&nbsp;&nbsp;new PropertyEntry("triangleType", [TriangleType.class](#triangletype)))<br>)<br> |
| Set<String> | required = Set.of(<br>&nbsp;&nbsp;&nbsp;&nbsp;"shapeType",<br>&nbsp;&nbsp;&nbsp;&nbsp;"triangleType"<br>)<br> |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| String | validate(String arg, SchemaConfiguration configuration) |
| Void | validate(Void arg, SchemaConfiguration configuration) |
| int | validate(int arg, SchemaConfiguration configuration) |
| long | validate(long arg, SchemaConfiguration configuration) |
| float | validate(float arg, SchemaConfiguration configuration) |
| double | validate(double arg, SchemaConfiguration configuration) |
| boolean | validate(boolean arg, SchemaConfiguration configuration) |
| [TriangleInterfaceMap](#triangleinterfacemap) | validate([Map&lt;?, ?&gt;](#triangleinterfacemapbuilder) arg, SchemaConfiguration configuration) |
| FrozenList<@Nullable Object> | validate(List<?> arg, SchemaConfiguration configuration) |
| @Nullable Object | validate(@Nullable Object arg, SchemaConfiguration configuration) |
## TriangleInterfaceMap00Builder
public class TriangleInterfaceMap00Builder<br>
builder for `Map<String, @Nullable Object>`

A class that builds the Map input type

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| TriangleInterfaceMap00Builder(Map<String, @Nullable Object> instance)<br>Creates a builder that contains the passed instance |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| Map<String, @Nullable Object> | build()<br>Returns map input that should be used with Schema.validate |
| [TriangleInterfaceMap00Builder](#triangleinterfacemap00builder) | additionalProperty(String key, Void value) |
| [TriangleInterfaceMap00Builder](#triangleinterfacemap00builder) | additionalProperty(String key, boolean value) |
| [TriangleInterfaceMap00Builder](#triangleinterfacemap00builder) | additionalProperty(String key, String value) |
| [TriangleInterfaceMap00Builder](#triangleinterfacemap00builder) | additionalProperty(String key, int value) |
| [TriangleInterfaceMap00Builder](#triangleinterfacemap00builder) | additionalProperty(String key, float value) |
| [TriangleInterfaceMap00Builder](#triangleinterfacemap00builder) | additionalProperty(String key, long value) |
| [TriangleInterfaceMap00Builder](#triangleinterfacemap00builder) | additionalProperty(String key, double value) |
| [TriangleInterfaceMap00Builder](#triangleinterfacemap00builder) | additionalProperty(String key, List<?> value) |
| [TriangleInterfaceMap00Builder](#triangleinterfacemap00builder) | additionalProperty(String key, Map<String, ?> value) |

## TriangleInterfaceMap01Builder
public class TriangleInterfaceMap01Builder<br>
builder for `Map<String, @Nullable Object>`

A class that builds the Map input type

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| TriangleInterfaceMap01Builder(Map<String, @Nullable Object> instance)<br>Creates a builder that contains the passed instance |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| [TriangleInterfaceMap00Builder](#triangleinterfacemap00builder) | triangleType(String value) |

## TriangleInterfaceMap10Builder
public class TriangleInterfaceMap10Builder<br>
builder for `Map<String, @Nullable Object>`

A class that builds the Map input type

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| TriangleInterfaceMap10Builder(Map<String, @Nullable Object> instance)<br>Creates a builder that contains the passed instance |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| [TriangleInterfaceMap00Builder](#triangleinterfacemap00builder) | shapeType(String value) |
| [TriangleInterfaceMap00Builder](#triangleinterfacemap00builder) | shapeType([StringShapeTypeEnums](#stringshapetypeenums) value) |

## TriangleInterfaceMapBuilder
public class TriangleInterfaceMapBuilder<br>
builder for `Map<String, @Nullable Object>`

A class that builds the Map input type

### Constructor Summary
| Constructor and Description |
| --------------------------- |
| TriangleInterfaceMapBuilder()<br>Creates a builder that contains an empty map |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| [TriangleInterfaceMap01Builder](#triangleinterfacemap01builder) | shapeType(String value) |
| [TriangleInterfaceMap01Builder](#triangleinterfacemap01builder) | shapeType([StringShapeTypeEnums](#stringshapetypeenums) value) |
| [TriangleInterfaceMap10Builder](#triangleinterfacemap10builder) | triangleType(String value) |

## TriangleInterfaceMap
public static class TriangleInterfaceMap<br>
extends FrozenMap<String, @Nullable Object>

A class to store validated Map payloads

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| static [TriangleInterfaceMap](#triangleinterfacemap) | of([Map<String, ? extends @Nullable Object>](#triangleinterfacemapbuilder) arg, SchemaConfiguration configuration) |
| String | shapeType()<br> must be one of ["Triangle"] |
| String | triangleType()<br> |
| @Nullable Object | getAdditionalProperty(String name)<br>provides type safety for additional properties |

## TriangleType
public static class TriangleType<br>
extends StringJsonSchema

A schema class that validates payloads

| Methods Inherited from class org.openapijsonschematools.client.schemas.StringJsonSchema |
| ------------------------------------------------------------------ |
| validate                                                           |

## ShapeType
public static class ShapeType<br>
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

// String validation
String validatedPayload = TriangleInterface.ShapeType.validate(
    "Triangle",
    configuration
);
```

### Field Summary
| Modifier and Type | Field and Description |
| ----------------- | ---------------------- |
| Set<Class<?>> | type = Set.of(<br/>&nbsp;&nbsp;&nbsp;&nbsp;String.class<br/>)<br/> |
| Set<Object> | enumValues = SetMaker.makeSet(<br>&nbsp;&nbsp;&nbsp;&nbsp;"Triangle"<br>)<br> |

### Method Summary
| Modifier and Type | Method and Description |
| ----------------- | ---------------------- |
| String | validate(String arg, SchemaConfiguration configuration) |
| String | validate([StringShapeTypeEnums](#stringshapetypeenums) arg, SchemaConfiguration configuration) |
| @Nullable Object | validate(@Nullable Object arg, SchemaConfiguration configuration) |
## StringShapeTypeEnums
public enum StringShapeTypeEnums<br>
extends `Enum<StringShapeTypeEnums>`

A class that stores String enum values

### Enum Constant Summary
| Enum Constant | Description |
| ------------- | ----------- |
| TRIANGLE | value = "Triangle" |

[[Back to top]](#top) [[Back to Component Schemas]](../../../README.md#Component-Schemas) [[Back to README]](../../../README.md)
