# AppleReq
petstore_api.components.schema.apple_req
```
type: schemas.Schema
```

## validate method
Input Type | Return Type | Notes
------------ | ------------- | -------------
[AppleReqDictInput](#applereqdictinput), [AppleReqDict](#applereqdict) | [AppleReqDict](#applereqdict) |

## AppleReqDictInput
```
type: typing.TypedDict
```
Key | Type |  Description | Notes
------------ | ------------- | ------------- | -------------
**cultivar** | str |  |
**mealy** | bool |  | [optional]

## AppleReqDict
```
base class: schemas.immutabledict[str, typing.Union[
    bool,
    str,
]]

```
### &lowbar;&lowbar;new&lowbar;&lowbar; method
Keyword Argument | Type | Description | Notes
---------------- | ---- | ----------- | -----
**cultivar** | str |  |
**mealy** | bool, schemas.Unset |  | [optional]

### properties
Property | Type | Description | Notes
-------- | ---- | ----------- | -----
**cultivar** | str |  |
**mealy** | bool, schemas.Unset |  | [optional]

### methods
Method | Input Type | Return Type | Notes
------ | ---------- | ----------- | ------
from_dict_ | [AppleReqDictInput](#applereqdictinput), [AppleReqDict](#applereqdict) | [AppleReqDict](#applereqdict) | a constructor

[[Back to top]](#top) [[Back to Component Schemas]](../../../README.md#Component-Schemas) [[Back to README]](../../../README.md)
