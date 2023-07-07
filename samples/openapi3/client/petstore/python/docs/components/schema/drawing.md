petstore_api.components.schema.drawing
# Schema Drawing

## Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, schemas.immutabledict | schemas.immutabledict |  |

## Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**mainShape** | [**Shape**](shape.md), dict, schemas.immutabledict, str, datetime.date, datetime.datetime, uuid.UUID, int, float, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader | [**Shape**](shape.md) |  | [optional]
**shapeOrNull** | [**ShapeOrNull**](shape_or_null.md), dict, schemas.immutabledict, str, datetime.date, datetime.datetime, uuid.UUID, int, float, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader | [**ShapeOrNull**](shape_or_null.md) |  | [optional]
**nullableShape** | [**NullableShape**](nullable_shape.md), dict, schemas.immutabledict, str, datetime.date, datetime.datetime, uuid.UUID, int, float, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader | [**NullableShape**](nullable_shape.md) |  | [optional]
**shapes** | list, tuple | [properties.Shapes](#properties-shapes) |  | [optional]
**any_string_name** | [**Fruit**](fruit.md), dict, schemas.immutabledict, str, datetime.date, datetime.datetime, uuid.UUID, int, float, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader | [**Fruit**](fruit.md) | any string name can be used but the value must be the correct type | [optional]

# properties Shapes

## Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple | tuple |  |

## List Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Shape**](shape.md) | [**Shape**](shape.md) | [**Shape**](shape.md) |  |

[[Back to top]](#top) [[Back to Component Schemas]](../../../README.md#Component-Schemas) [[Back to README]](../../../README.md)
