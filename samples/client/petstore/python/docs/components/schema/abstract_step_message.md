# AbstractStepMessage
petstore_api.components.schema.abstract_step_message
```
type: schemas.Schema
```

## Description
Abstract Step

## validate method
Input Type | Return Type | Notes
------------ | ------------- | -------------
[AbstractStepMessageDictInput](#abstractstepmessagedictinput), [AbstractStepMessageDict](#abstractstepmessagedict) | [AbstractStepMessageDict](#abstractstepmessagedict) |

## AbstractStepMessageDictInput
```
type: typing.Mapping[str, schemas.INPUT_TYPES_ALL]
```
Key | Type |  Description | Notes
------------ | ------------- | ------------- | -------------
**description** | dict, schemas.immutabledict, str, datetime.date, datetime.datetime, uuid.UUID, int, float, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader |  |
**discriminator** | str |  |
**sequenceNumber** | dict, schemas.immutabledict, str, datetime.date, datetime.datetime, uuid.UUID, int, float, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader |  |
**any_string_name** | dict, schemas.immutabledict, list, tuple, decimal.Decimal, float, int, str, datetime.date, datetime.datetime, uuid.UUID, bool, None, bytes, io.FileIO, io.BufferedReader, schemas.FileIO | any string name can be used but the value must be the correct type | [optional]

## AbstractStepMessageDict
```
base class: schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES]

```
### &lowbar;&lowbar;new&lowbar;&lowbar; method
Keyword Argument | Type | Description | Notes
---------------- | ---- | ----------- | -----
**description** | dict, schemas.immutabledict, str, datetime.date, datetime.datetime, uuid.UUID, int, float, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader |  |
**discriminator** | str |  |
**sequenceNumber** | dict, schemas.immutabledict, str, datetime.date, datetime.datetime, uuid.UUID, int, float, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader |  |
**kwargs** | schemas.immutabledict, tuple, float, int, str, bool, None, bytes, schemas.FileIO | any string name can be used but the value must be the correct type Abstract Step | [optional] typed value is accessed with the get_additional_property_ method

### properties
Property | Type | Description | Notes
-------- | ---- | ----------- | -----
**description** | schemas.immutabledict, str, float, int, bool, None, tuple, bytes, io.FileIO |  |
**discriminator** | str |  |
**sequenceNumber** | schemas.immutabledict, str, float, int, bool, None, tuple, bytes, io.FileIO |  |

### methods
Method | Input Type | Return Type | Notes
------ | ---------- | ----------- | ------
from_dict_ | [AbstractStepMessageDictInput](#abstractstepmessagedictinput), [AbstractStepMessageDict](#abstractstepmessagedict) | [AbstractStepMessageDict](#abstractstepmessagedict) | a constructor
get_additional_property_ | str | schemas.immutabledict, tuple, float, int, str, bool, None, bytes, schemas.FileIO, schemas.Unset }} | provides type safety for additional properties

## Composed Schemas (allOf/anyOf/oneOf/not)
## anyOf
Schema Class | Input Type | Return Type
------------ | ---------- | -----------
[**AbstractStepMessage**](#top) | [AbstractStepMessageDictInput](#abstractstepmessagedictinput), [AbstractStepMessageDict](#abstractstepmessagedict) | [AbstractStepMessageDict](#abstractstepmessagedict)

[[Back to top]](#top) [[Back to Component Schemas]](../../../README.md#Component-Schemas) [[Back to README]](../../../README.md)
