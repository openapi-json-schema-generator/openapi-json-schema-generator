# Money
petstore_api.components.schema.money
```
type: schemas.Schema
```

## validate method
Input Type | Return Type | Notes
------------ | ------------- | -------------
[MoneyDictInput](#moneydictinput), [MoneyDict](#moneydict) | [MoneyDict](#moneydict) |

## MoneyDictInput
```
type: typing.TypedDict
```
Key | Type |  Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | str |  | value must be int or float numeric
**currency** | typing.Literal["eur", "usd"] |  |

## MoneyDict
```
base class: schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES]

```
### &lowbar;&lowbar;new&lowbar;&lowbar; method
Keyword Argument | Type | Description | Notes
---------------- | ---- | ----------- | -----
**amount** | str |  | value must be int or float numeric
**currency** | typing.Literal["eur", "usd"] |  |

### properties
Property | Type | Description | Notes
-------- | ---- | ----------- | -----
**amount** | str |  | value must be int or float numeric
**currency** | typing.Literal["eur", "usd"] |  |

### methods
Method | Input Type | Return Type | Notes
------ | ---------- | ----------- | ------
from_dict_ | [MoneyDictInput](#moneydictinput), [MoneyDict](#moneydict) | [MoneyDict](#moneydict) | a constructor

[[Back to top]](#top) [[Back to Component Schemas]](../../../README.md#Component-Schemas) [[Back to README]](../../../README.md)
