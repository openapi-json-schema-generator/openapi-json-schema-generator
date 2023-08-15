# ObjectWithDecimalProperties
petstore_api.components.schema.object_with_decimal_properties
```
type: schemas.Schema
```

## validate method
Input Type | Return Type | Notes
------------ | ------------- | -------------
[ObjectWithDecimalPropertiesDictInput](#objectwithdecimalpropertiesdictinput), [ObjectWithDecimalPropertiesDict](#objectwithdecimalpropertiesdict) | [ObjectWithDecimalPropertiesDict](#objectwithdecimalpropertiesdict) |

## ObjectWithDecimalPropertiesDictInput
```
type: typing.Mapping[str, schemas.INPUT_TYPES_ALL]
```
Key | Type |  Description | Notes
------------ | ------------- | ------------- | -------------
**length** | str |  | [optional]
**width** | str |  | [optional] value must be int or float numeric
**cost** | [money.MoneyDictInput](../../components/schema/money.md#moneydictinput), [money.MoneyDict](../../components/schema/money.md#moneydict) |  | [optional]
**any_string_name** | dict, schemas.immutabledict, list, tuple, decimal.Decimal, float, int, str, datetime.date, datetime.datetime, uuid.UUID, bool, None, bytes, io.FileIO, io.BufferedReader, schemas.FileIO | any string name can be used but the value must be the correct type | [optional]

## ObjectWithDecimalPropertiesDict
```
base class: schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES]
```
### &lowbar;&lowbar;new&lowbar;&lowbar; method
Keyword Argument | Type | Description | Notes
---------------- | ---- | ----------- | -----
**length** | str, schemas.Unset |  | [optional]
**width** | str, schemas.Unset |  | [optional] value must be int or float numeric
**cost** | [money.MoneyDictInput](../../components/schema/money.md#moneydictinput), [money.MoneyDict](../../components/schema/money.md#moneydict), schemas.Unset |  | [optional]
**kwargs** | schemas.immutabledict, tuple, float, int, str, bool, None, bytes, schemas.FileIO | any string name can be used but the value must be the correct type | [optional] typed value is accessed with the get_additional_property_ method

### properties
Property | Type | Description | Notes
-------- | ---- | ----------- | -----
**length** | str, schemas.Unset |  | [optional]
**width** | str, schemas.Unset |  | [optional] value must be int or float numeric
**cost** | [money.MoneyDict](../../components/schema/money.md#moneydict), schemas.Unset |  | [optional]

### methods
Method | Input Type | Return Type | Notes
------ | ---------- | ----------- | ------
from_dict_ | [ObjectWithDecimalPropertiesDictInput](#objectwithdecimalpropertiesdictinput), [ObjectWithDecimalPropertiesDict](#objectwithdecimalpropertiesdict) | [ObjectWithDecimalPropertiesDict](#objectwithdecimalpropertiesdict) | a constructor
get_additional_property_ | str | schemas.immutabledict, tuple, float, int, str, bool, None, bytes, schemas.FileIO, schemas.Unset }} | provides type safety for additional properties

[[Back to top]](#top) [[Back to Component Schemas]](../../../README.md#Component-Schemas) [[Back to README]](../../../README.md)
