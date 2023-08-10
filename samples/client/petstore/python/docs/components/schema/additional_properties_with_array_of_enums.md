# AdditionalPropertiesWithArrayOfEnums
petstore_api.components.schema.additional_properties_with_array_of_enums
```
type: schemas.Schema
```

## validate method
Input Type | Return Type | Notes
------------ | ------------- | -------------
[AdditionalPropertiesWithArrayOfEnumsDictInput](#additionalpropertieswitharrayofenumsdictinput), [AdditionalPropertiesWithArrayOfEnumsDict](#additionalpropertieswitharrayofenumsdict) | [AdditionalPropertiesWithArrayOfEnumsDict](#additionalpropertieswitharrayofenumsdict) |

## AdditionalPropertiesWithArrayOfEnumsDictInput
```
type: typing.Mapping[
    str,
    typing.Union[
        AdditionalPropertiesTupleInput,
        AdditionalPropertiesTuple
    ],
]
```
Key | Type |  Description | Notes
------------ | ------------- | ------------- | -------------
**any_string_name** | [AdditionalPropertiesTupleInput](#additionalpropertiestupleinput), [AdditionalPropertiesTuple](#additionalpropertiestuple) | any string name can be used but the value must be the correct type | [optional]

## AdditionalPropertiesWithArrayOfEnumsDict
```
base class: schemas.immutabledict[str, typing.Tuple[schemas.OUTPUT_BASE_TYPES]]

```
### &lowbar;&lowbar;new&lowbar;&lowbar; method
Keyword Argument | Type | Description | Notes
---------------- | ---- | ----------- | -----
**kwargs** | [AdditionalPropertiesTupleInput](#additionalpropertiestupleinput), [AdditionalPropertiesTuple](#additionalpropertiestuple) | any string name can be used but the value must be the correct type | [optional] typed value is accessed with the get_additional_property_ method

### methods
Method | Input Type | Return Type | Notes
------ | ---------- | ----------- | ------
from_dict_ | [AdditionalPropertiesWithArrayOfEnumsDictInput](#additionalpropertieswitharrayofenumsdictinput), [AdditionalPropertiesWithArrayOfEnumsDict](#additionalpropertieswitharrayofenumsdict) | [AdditionalPropertiesWithArrayOfEnumsDict](#additionalpropertieswitharrayofenumsdict) | a constructor
get_additional_property_ | str | [AdditionalPropertiesTuple](#additionalpropertiestuple), schemas.Unset | provides type safety for additional properties

# AdditionalProperties
```
type: schemas.Schema
```

## validate method
Input Type | Return Type | Notes
------------ | ------------- | -------------
[AdditionalPropertiesTupleInput](#additionalpropertiestupleinput), [AdditionalPropertiesTuple](#additionalpropertiestuple) | [AdditionalPropertiesTuple](#additionalpropertiestuple) |

## AdditionalPropertiesTupleInput
```
type: typing.Union[
    typing.List[
        typing.Literal[
            "_abc",
            "-efg",
            "(xyz)",
            "COUNT_1M",
            "COUNT_50M"
        ],
    ],
    typing.Tuple[
        typing.Literal[
            "_abc",
            "-efg",
            "(xyz)",
            "COUNT_1M",
            "COUNT_50M"
        ],
        ...
    ]
]
```
List/Tuple Item Type | Description | Notes
-------------------- | ------------- | -------------
typing.Literal["_abc", "-efg", "(xyz)", "COUNT_1M", "COUNT_50M"] |  |

## AdditionalPropertiesTuple
```
base class: typing.Tuple[
    typing.Literal["_abc", "-efg", "(xyz)", "COUNT_1M", "COUNT_50M"],
    ...
]
```
### &lowbar;&lowbar;new&lowbar;&lowbar; method
Argument | Type
-------- | ------
arg      | [AdditionalPropertiesTupleInput](#additionalpropertiestupleinput), [AdditionalPropertiesTuple](#additionalpropertiestuple)
configuration | typing.Optional[schema_configuration.SchemaConfiguration] = None

### methods
Method | Input Type | Return Type | Notes
------ | ---------- | ----------- | ------
&lowbar;&lowbar;getitem&lowbar;&lowbar; | int | typing.Literal["_abc", "-efg", "(xyz)", "COUNT_1M", "COUNT_50M"] | This method is used under the hood when instance[0] is called

[[Back to top]](#top) [[Back to Component Schemas]](../../../README.md#Component-Schemas) [[Back to README]](../../../README.md)
