# ReqPropsFromTrueAddProps
petstore_api.components.schema.req_props_from_true_add_props
```
type: schemas.Schema
```

## validate method
Input Type | Return Type | Notes
------------ | ------------- | -------------
[ReqPropsFromTrueAddPropsDictInput](#reqpropsfromtrueaddpropsdictinput), [ReqPropsFromTrueAddPropsDict](#reqpropsfromtrueaddpropsdict) | [ReqPropsFromTrueAddPropsDict](#reqpropsfromtrueaddpropsdict) |

## ReqPropsFromTrueAddPropsDictInput
```
type: typing.Mapping[str, schemas.INPUT_TYPES_ALL]
```
Key | Type |  Description | Notes
------------ | ------------- | ------------- | -------------
**invalid-name** | dict, schemas.immutabledict, str, datetime.date, datetime.datetime, uuid.UUID, int, float, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader |  |
**validName** | dict, schemas.immutabledict, str, datetime.date, datetime.datetime, uuid.UUID, int, float, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader |  |
**any_string_name** | dict, schemas.immutabledict, str, datetime.date, datetime.datetime, uuid.UUID, int, float, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader | any string name can be used but the value must be the correct type | [optional]

## ReqPropsFromTrueAddPropsDict
```
base class: schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES]

```
### &lowbar;&lowbar;new&lowbar;&lowbar; method
Keyword Argument | Type | Description | Notes
---------------- | ---- | ----------- | -----
**validName** | dict, schemas.immutabledict, str, datetime.date, datetime.datetime, uuid.UUID, int, float, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader |  |
**kwargs** | dict, schemas.immutabledict, str, datetime.date, datetime.datetime, uuid.UUID, int, float, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader | any string name can be used but the value must be the correct type | [optional] typed value is accessed with the get_additional_property_ method

### properties
Property | Type | Description | Notes
-------- | ---- | ----------- | -----
**validName** | schemas.immutabledict, str, float, int, bool, None, tuple, bytes, io.FileIO |  |

### methods
Method | Input Type | Return Type | Notes
------ | ---------- | ----------- | ------
from_dict_ | [ReqPropsFromTrueAddPropsDictInput](#reqpropsfromtrueaddpropsdictinput), [ReqPropsFromTrueAddPropsDict](#reqpropsfromtrueaddpropsdict) | [ReqPropsFromTrueAddPropsDict](#reqpropsfromtrueaddpropsdict) | a constructor
&lowbar;&lowbar;getitem&lowbar;&lowbar; | str | schemas.immutabledict, str, float, int, bool, None, tuple, bytes, io.FileIO | This model has invalid python names so this method is used under the hood when you access instance["invalid-name"], 
get_additional_property_ | str | schemas.immutabledict, str, float, int, bool, None, tuple, bytes, io.FileIO, schemas.Unset | provides type safety for additional properties

[[Back to top]](#top) [[Back to Component Schemas]](../../../README.md#Component-Schemas) [[Back to README]](../../../README.md)
