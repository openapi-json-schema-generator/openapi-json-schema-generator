petstore_api.components.schema.enum_test
# Schema EnumTest

## Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict | frozendict.frozendict |  |

## Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**enum_string_required** | str | str |  | must be one of ["UPPER", "lower", ""]
**enum_string** | str | str |  | [optional] must be one of ["UPPER", "lower", ""]
**enum_integer** | decimal.Decimal, int | decimal.Decimal |  | [optional] must be one of [1, -1] value must be a 32 bit integer
**enum_number** | decimal.Decimal, int, float | decimal.Decimal |  | [optional] must be one of [1.1, -1.2] value must be a 64 bit float
**stringEnum** | [**StringEnum**](string_enum.md), None, str | [**StringEnum**](string_enum.md) |  | [optional]
**IntegerEnum** | [**IntegerEnum**](integer_enum.md), decimal.Decimal, int | [**IntegerEnum**](integer_enum.md) |  | [optional]
**StringEnumWithDefaultValue** | [**StringEnumWithDefaultValue**](string_enum_with_default_value.md), str | [**StringEnumWithDefaultValue**](string_enum_with_default_value.md) |  | [optional]
**IntegerEnumWithDefaultValue** | [**IntegerEnumWithDefaultValue**](integer_enum_with_default_value.md), decimal.Decimal, int | [**IntegerEnumWithDefaultValue**](integer_enum_with_default_value.md) |  | [optional]
**IntegerEnumOneValue** | [**IntegerEnumOneValue**](integer_enum_one_value.md), decimal.Decimal, int | [**IntegerEnumOneValue**](integer_enum_one_value.md) |  | [optional]
**any_string_name** | dict, frozendict.frozendict, list, tuple, decimal.Decimal, float, int, str, datetime.date, datetime.datetime, uuid.UUID, bool, None, bytes, io.FileIO, io.BufferedReader, schemas.Schema | frozendict.frozendict, tuple, decimal.Decimal, str, bytes, BoolClass, NoneClass, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to top]](#top) [[Back to Component Schemas]](../../../README.md#Component-Schemas) [[Back to README]](../../../README.md)
