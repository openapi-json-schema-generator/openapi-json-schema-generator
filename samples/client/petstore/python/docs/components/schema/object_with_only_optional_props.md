# ObjectWithOnlyOptionalProps
petstore_api.components.schema.object_with_only_optional_props
```
type: schemas.Schema
```

## validate method
Input Type | Return Type | Notes
------------ | ------------- | -------------
[ObjectWithOnlyOptionalPropsDictInput](#objectwithonlyoptionalpropsdictinput), [ObjectWithOnlyOptionalPropsDict](#objectwithonlyoptionalpropsdict) | [ObjectWithOnlyOptionalPropsDict](#objectwithonlyoptionalpropsdict) |

## ObjectWithOnlyOptionalPropsDictInput
```
type: typing.TypedDict
```
Key | Type |  Description | Notes
------------ | ------------- | ------------- | -------------
**a** | str |  | [optional]
**b** | float, int |  | [optional]

## ObjectWithOnlyOptionalPropsDict
```
base class: schemas.immutabledict[str, typing.Union[
    typing.Union[int, float],
    str,
]]

```
### &lowbar;&lowbar;new&lowbar;&lowbar; method
Keyword Argument | Type | Description | Notes
---------------- | ---- | ----------- | -----
**a** | str, schemas.Unset |  | [optional]
**b** | float, int, schemas.Unset |  | [optional]

### properties
Property | Type | Description | Notes
-------- | ---- | ----------- | -----
**a** | str, schemas.Unset |  | [optional]
**b** | float, int, schemas.Unset |  | [optional]

### methods
Method | Input Type | Return Type | Notes
------ | ---------- | ----------- | ------
from_dict_ | [ObjectWithOnlyOptionalPropsDictInput](#objectwithonlyoptionalpropsdictinput), [ObjectWithOnlyOptionalPropsDict](#objectwithonlyoptionalpropsdict) | [ObjectWithOnlyOptionalPropsDict](#objectwithonlyoptionalpropsdict) | a constructor

[[Back to top]](#top) [[Back to Component Schemas]](../../../README.md#Component-Schemas) [[Back to README]](../../../README.md)
