<a name="top"></a>
## petstore_api.components.schema.object_with_decimal_properties
# ObjectWithDecimalProperties

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  |

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**length** | [**DecimalPayload**](decimal_payload.DecimalPayload.md) | [**DecimalPayload**](decimal_payload.DecimalPayload.md) |  | [optional]
**width** | str,  | str,  |  | [optional] value must be numeric and storable in decimal.Decimal
**cost** | [**Money**](money.Money.md) | [**Money**](money.Money.md) |  | [optional]
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to top]](#top) [[Back to Component Schemas]](../../../README.md#Component-Schemas) [[Back to README]](../../../README.md)