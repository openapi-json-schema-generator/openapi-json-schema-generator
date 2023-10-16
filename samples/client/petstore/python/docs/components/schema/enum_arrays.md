# EnumArrays
petstore_api.components.schema.enum_arrays
```
type: schemas.Schema
```

## validate method
Input Type | Return Type | Notes
------------ | ------------- | -------------
[EnumArraysDictInput](#enumarraysdictinput), [EnumArraysDict](#enumarraysdict) | [EnumArraysDict](#enumarraysdict) |

## EnumArraysDictInput
```
type: typing.Mapping[str, schemas.INPUT_TYPES_ALL]
```
Key | Type |  Description | Notes
------------ | ------------- | ------------- | -------------
**just_symbol** | typing.Literal[">=", "$"] |  | [optional] must be one of [">=", "$"]
**array_enum** | [ArrayEnumTupleInput](#arrayenumtupleinput), [ArrayEnumTuple](#arrayenumtuple) |  | [optional]
**any_string_name** | dict, schemas.immutabledict, list, tuple, decimal.Decimal, float, int, str, datetime.date, datetime.datetime, uuid.UUID, bool, None, bytes, io.FileIO, io.BufferedReader, schemas.FileIO | any string name can be used but the value must be the correct type | [optional]

## EnumArraysDict
```
base class: schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES]

```
### &lowbar;&lowbar;new&lowbar;&lowbar; method
Keyword Argument | Type | Description | Notes
---------------- | ---- | ----------- | -----
**just_symbol** | typing.Literal[">=", "$"], schemas.Unset |  | [optional] must be one of [">=", "$"]
**array_enum** | [ArrayEnumTupleInput](#arrayenumtupleinput), [ArrayEnumTuple](#arrayenumtuple), schemas.Unset |  | [optional]
**kwargs** | schemas.immutabledict, tuple, float, int, str, bool, None, bytes, schemas.FileIO | any string name can be used but the value must be the correct type | [optional] typed value is accessed with the get_additional_property_ method

### properties
Property | Type | Description | Notes
-------- | ---- | ----------- | -----
**just_symbol** | typing.Literal[">=", "$"], schemas.Unset |  | [optional] must be one of [">=", "$"]
**array_enum** | [ArrayEnumTuple](#arrayenumtuple), schemas.Unset |  | [optional]

### methods
Method | Input Type | Return Type | Notes
------ | ---------- | ----------- | ------
from_dict_ | [EnumArraysDictInput](#enumarraysdictinput), [EnumArraysDict](#enumarraysdict) | [EnumArraysDict](#enumarraysdict) | a constructor
get_additional_property_ | str | schemas.immutabledict, tuple, float, int, str, bool, None, bytes, schemas.FileIO, schemas.Unset | provides type safety for additional properties

# ArrayEnum
```
type: schemas.Schema
```

## validate method
Input Type | Return Type | Notes
------------ | ------------- | -------------
[ArrayEnumTupleInput](#arrayenumtupleinput), [ArrayEnumTuple](#arrayenumtuple) | [ArrayEnumTuple](#arrayenumtuple) |

## ArrayEnumTupleInput
```
type: typing.Union[
    typing.List[
        typing.Literal[
            "fish",
            "crab"
        ],
    ],
    typing.Tuple[
        typing.Literal[
            "fish",
            "crab"
        ],
        ...
    ]
]
```
List/Tuple Item Type | Description | Notes
-------------------- | ------------- | -------------
typing.Literal["fish", "crab"] |  | must be one of ["fish", "crab"]

## ArrayEnumTuple
```
base class: typing.Tuple[
    typing.Literal["fish", "crab"],
    ...
]
```
### &lowbar;&lowbar;new&lowbar;&lowbar; method
Argument | Type
-------- | ------
arg      | [ArrayEnumTupleInput](#arrayenumtupleinput), [ArrayEnumTuple](#arrayenumtuple)
configuration | typing.Optional[schema_configuration.SchemaConfiguration] = None

### methods
Method | Input Type | Return Type | Notes
------ | ---------- | ----------- | ------
&lowbar;&lowbar;getitem&lowbar;&lowbar; | int | typing.Literal["fish", "crab"] | must be one of ["fish", "crab"] This method is used under the hood when instance[0] is called

[[Back to top]](#top) [[Back to Component Schemas]](../../../README.md#Component-Schemas) [[Back to README]](../../../README.md)
