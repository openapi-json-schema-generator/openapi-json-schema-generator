# ComposedOneOfDifferentTypes
petstore_api.components.schema.composed_one_of_different_types
```
type: schemas.Schema
```

## Description
this is a model that allows payloads of type object or number

## validate method
Input Type | Return Type | Notes
------------ | ------------- | -------------
dict, schemas.immutabledict, str, datetime.date, datetime.datetime, uuid.UUID, int, float, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader | schemas.immutabledict, str, float, int, bool, None, tuple, bytes, io.FileIO |

## Composed Schemas (allOf/anyOf/oneOf/not)
## oneOf
Schema Class | Input Type | Return Type
------------ | ---------- | -----------
[**number_with_validations.NumberWithValidations**](../../components/schema/number_with_validations.md) | float, int | float, int
[**animal.Animal**](../../components/schema/animal.md) | [animal.AnimalDictInput](../../components/schema/animal.md#animaldictinput), [animal.AnimalDict](../../components/schema/animal.md#animaldict) | [animal.AnimalDict](../../components/schema/animal.md#animaldict)
[_2](#_2) | None | None
[_3](#_3) | str, datetime.date | str
[_4](#_4) | dict, schemas.immutabledict | schemas.immutabledict
[_5](#_5) | [_5TupleInput](#_5tupleinput), [_5Tuple](#_5tuple) | [_5Tuple](#_5tuple)
[_6](#_6) | str, datetime.datetime | str

# _2
```
type: schemas.Schema
```

## validate method
Input Type | Return Type | Notes
------------ | ------------- | -------------
None | None |

# _3
```
type: schemas.Schema
```

## validate method
Input Type | Return Type | Notes
------------ | ------------- | -------------
str, datetime.date | str | value must conform to RFC-3339 full-date YYYY-MM-DD

# _4
```
type: schemas.Schema
```

## validate method
Input Type | Return Type | Notes
------------ | ------------- | -------------
dict, schemas.immutabledict | schemas.immutabledict |

# _5
```
type: schemas.Schema
```

## validate method
Input Type | Return Type | Notes
------------ | ------------- | -------------
[_5TupleInput](#_5tupleinput), [_5Tuple](#_5tuple) | [_5Tuple](#_5tuple) |

## _5TupleInput
```
type: typing.Union[
    typing.List[
        typing.Union[
            schemas.INPUT_TYPES_ALL,
            schemas.OUTPUT_BASE_TYPES
        ],
    ],
    typing.Tuple[
        typing.Union[
            schemas.INPUT_TYPES_ALL,
            schemas.OUTPUT_BASE_TYPES
        ],
        ...
    ]
]
```
List/Tuple Item Type | Description | Notes
-------------------- | ------------- | -------------
dict, schemas.immutabledict, str, datetime.date, datetime.datetime, uuid.UUID, int, float, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader |  |

## _5Tuple
```
base class: typing.Tuple[
    schemas.OUTPUT_BASE_TYPES,
    ...
]
```
### &lowbar;&lowbar;new&lowbar;&lowbar; method
Argument | Type
-------- | ------
arg      | [_5TupleInput](#_5tupleinput), [_5Tuple](#_5tuple)
configuration | typing.Optional[schema_configuration.SchemaConfiguration] = None

### methods
Method | Input Type | Return Type | Notes
------ | ---------- | ----------- | ------
&lowbar;&lowbar;getitem&lowbar;&lowbar; | int | schemas.immutabledict, str, float, int, bool, None, tuple, bytes, io.FileIO | This method is used under the hood when instance[0] is called

# _6
```
type: schemas.Schema
```

## validate method
Input Type | Return Type | Notes
------------ | ------------- | -------------
str, datetime.datetime | str | value must conform to RFC-3339 date-time

[[Back to top]](#top) [[Back to Component Schemas]](../../../README.md#Component-Schemas) [[Back to README]](../../../README.md)
