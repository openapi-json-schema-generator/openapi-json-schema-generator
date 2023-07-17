# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]



@dataclasses.dataclass(frozen=True)
class AdditionalProperties4(
    schemas.Schema[schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES], typing.Tuple[schemas.OUTPUT_BASE_TYPES, ...]],
):
    types: typing.FrozenSet[typing.Type] = frozenset({
        type(None),
        schemas.immutabledict,
    })

    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: None,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> None: ...
    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: typing.Mapping[str, schemas.INPUT_TYPES_ALL],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> schemas.immutabledict[str, schemas.INPUT_TYPES_ALL]: ...
    @classmethod
    def validate(
        cls,
        arg,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ):
        return super().validate_base(
            arg,
            configuration=configuration,
        )



@dataclasses.dataclass(frozen=True)
class IntegerProp(
    schemas.Schema[schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES], typing.Tuple[schemas.OUTPUT_BASE_TYPES, ...]],
):
    types: typing.FrozenSet[typing.Type] = frozenset({
        type(None),
        int,
    })
    format: str = 'int'

    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: None,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> None: ...
    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: int,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> int: ...
    @classmethod
    def validate(
        cls,
        arg,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ):
        return super().validate_base(
            arg,
            configuration=configuration,
        )



@dataclasses.dataclass(frozen=True)
class NumberProp(
    schemas.Schema[schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES], typing.Tuple[schemas.OUTPUT_BASE_TYPES, ...]],
):
    types: typing.FrozenSet[typing.Type] = frozenset({
        type(None),
        float,
        int,
    })

    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: None,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> None: ...
    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: typing.Union[int, float],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing.Union[int, float]: ...
    @classmethod
    def validate(
        cls,
        arg,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ):
        return super().validate_base(
            arg,
            configuration=configuration,
        )



@dataclasses.dataclass(frozen=True)
class BooleanProp(
    schemas.Schema[schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES], typing.Tuple[schemas.OUTPUT_BASE_TYPES, ...]],
):
    types: typing.FrozenSet[typing.Type] = frozenset({
        type(None),
        schemas.Bool,
    })

    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: None,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> None: ...
    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: bool,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> bool: ...
    @classmethod
    def validate(
        cls,
        arg,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ):
        return super().validate_base(
            arg,
            configuration=configuration,
        )



@dataclasses.dataclass(frozen=True)
class StringProp(
    schemas.Schema[schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES], typing.Tuple[schemas.OUTPUT_BASE_TYPES, ...]],
):
    types: typing.FrozenSet[typing.Type] = frozenset({
        type(None),
        str,
    })

    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: None,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> None: ...
    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: str,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> str: ...
    @classmethod
    def validate(
        cls,
        arg,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ):
        return super().validate_base(
            arg,
            configuration=configuration,
        )



@dataclasses.dataclass(frozen=True)
class DateProp(
    schemas.Schema[schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES], typing.Tuple[schemas.OUTPUT_BASE_TYPES, ...]],
):
    types: typing.FrozenSet[typing.Type] = frozenset({
        type(None),
        str,
    })
    format: str = 'date'

    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: None,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> None: ...
    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: str,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> str: ...
    @classmethod
    def validate(
        cls,
        arg,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ):
        return super().validate_base(
            arg,
            configuration=configuration,
        )



@dataclasses.dataclass(frozen=True)
class DatetimeProp(
    schemas.Schema[schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES], typing.Tuple[schemas.OUTPUT_BASE_TYPES, ...]],
):
    types: typing.FrozenSet[typing.Type] = frozenset({
        type(None),
        str,
    })
    format: str = 'date-time'

    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: None,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> None: ...
    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: str,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> str: ...
    @classmethod
    def validate(
        cls,
        arg,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ):
        return super().validate_base(
            arg,
            configuration=configuration,
        )

Items: typing_extensions.TypeAlias = schemas.DictSchema


class ArrayNullablePropTuple(
    typing.Tuple[
        schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES],
        ...
    ]
):

    def __new__(cls, arg: ArrayNullablePropTupleInput, configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None):
        return ArrayNullableProp.validate(arg, configuration=configuration)
ArrayNullablePropTupleInput = typing.Union[
    typing.List[
        typing.Union[
            dict,
            schemas.immutabledict
        ],
    ],
    typing.Tuple[
        typing.Union[
            dict,
            schemas.immutabledict
        ],
        ...
    ]
]


@dataclasses.dataclass(frozen=True)
class ArrayNullableProp(
    schemas.Schema[schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES], ArrayNullablePropTuple],
):
    types: typing.FrozenSet[typing.Type] = frozenset({
        type(None),
        tuple,
    })
    items: typing.Type[Items] = dataclasses.field(default_factory=lambda: Items) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            tuple: ArrayNullablePropTuple,
        }
    )

    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: None,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> None: ...
    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: typing.Union[
            ArrayNullablePropTupleInput,
            ArrayNullablePropTuple,
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> ArrayNullablePropTuple: ...
    @classmethod
    def validate(
        cls,
        arg,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ):
        return super().validate_base(
            arg,
            configuration=configuration,
        )



@dataclasses.dataclass(frozen=True)
class Items2(
    schemas.Schema[schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES], typing.Tuple[schemas.OUTPUT_BASE_TYPES, ...]],
):
    types: typing.FrozenSet[typing.Type] = frozenset({
        type(None),
        schemas.immutabledict,
    })

    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: None,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> None: ...
    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: typing.Mapping[str, schemas.INPUT_TYPES_ALL],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> schemas.immutabledict[str, schemas.INPUT_TYPES_ALL]: ...
    @classmethod
    def validate(
        cls,
        arg,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ):
        return super().validate_base(
            arg,
            configuration=configuration,
        )



class ArrayAndItemsNullablePropTuple(
    typing.Tuple[
        typing.Union[
            None,
            schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES],
        ],
        ...
    ]
):

    def __new__(cls, arg: ArrayAndItemsNullablePropTupleInput, configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None):
        return ArrayAndItemsNullableProp.validate(arg, configuration=configuration)
ArrayAndItemsNullablePropTupleInput = typing.Union[
    typing.List[
        typing.Union[
            None,
            dict,
            schemas.immutabledict
        ],
    ],
    typing.Tuple[
        typing.Union[
            None,
            dict,
            schemas.immutabledict
        ],
        ...
    ]
]


@dataclasses.dataclass(frozen=True)
class ArrayAndItemsNullableProp(
    schemas.Schema[schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES], ArrayAndItemsNullablePropTuple],
):
    types: typing.FrozenSet[typing.Type] = frozenset({
        type(None),
        tuple,
    })
    items: typing.Type[Items2] = dataclasses.field(default_factory=lambda: Items2) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            tuple: ArrayAndItemsNullablePropTuple,
        }
    )

    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: None,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> None: ...
    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: typing.Union[
            ArrayAndItemsNullablePropTupleInput,
            ArrayAndItemsNullablePropTuple,
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> ArrayAndItemsNullablePropTuple: ...
    @classmethod
    def validate(
        cls,
        arg,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ):
        return super().validate_base(
            arg,
            configuration=configuration,
        )



@dataclasses.dataclass(frozen=True)
class Items3(
    schemas.Schema[schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES], typing.Tuple[schemas.OUTPUT_BASE_TYPES, ...]],
):
    types: typing.FrozenSet[typing.Type] = frozenset({
        type(None),
        schemas.immutabledict,
    })

    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: None,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> None: ...
    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: typing.Mapping[str, schemas.INPUT_TYPES_ALL],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> schemas.immutabledict[str, schemas.INPUT_TYPES_ALL]: ...
    @classmethod
    def validate(
        cls,
        arg,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ):
        return super().validate_base(
            arg,
            configuration=configuration,
        )



class ArrayItemsNullableTuple(
    typing.Tuple[
        typing.Union[
            None,
            schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES],
        ],
        ...
    ]
):

    def __new__(cls, arg: ArrayItemsNullableTupleInput, configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None):
        return ArrayItemsNullable.validate(arg, configuration=configuration)
ArrayItemsNullableTupleInput = typing.Union[
    typing.List[
        typing.Union[
            None,
            dict,
            schemas.immutabledict
        ],
    ],
    typing.Tuple[
        typing.Union[
            None,
            dict,
            schemas.immutabledict
        ],
        ...
    ]
]


@dataclasses.dataclass(frozen=True)
class ArrayItemsNullable(
    schemas.Schema[schemas.immutabledict, ArrayItemsNullableTuple]
):
    types: typing.FrozenSet[typing.Type] = frozenset({tuple})
    items: typing.Type[Items3] = dataclasses.field(default_factory=lambda: Items3) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            tuple: ArrayItemsNullableTuple
        }
    )

    @classmethod
    def validate(
        cls,
        arg: typing.Union[
            ArrayItemsNullableTupleInput,
            ArrayItemsNullableTuple,
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> ArrayItemsNullableTuple:
        return super().validate_base(
            arg,
            configuration=configuration,
        )
AdditionalProperties: typing_extensions.TypeAlias = schemas.DictSchema


class ObjectNullablePropDict(schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES]):
    __required_keys__: typing.FrozenSet[str] = frozenset({
    })
    __optional_keys__: typing.FrozenSet[str] = frozenset({
    })
    
    def get_additional_property_(self, name: str) -> schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES]:
        schemas.raise_if_key_known(name, self.__required_keys__, self.__optional_keys__)
        return typing.cast(
            schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES],
            self.__getitem__(name)
        )

    def __new__(cls, arg: ObjectNullablePropDictInput, configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None):
        return ObjectNullableProp.validate(arg, configuration=configuration)
ObjectNullablePropDictInput = typing.Mapping[
    str,
    typing.Union[
        dict,
        schemas.immutabledict
    ],
]


@dataclasses.dataclass(frozen=True)
class ObjectNullableProp(
    schemas.Schema[ObjectNullablePropDict, typing.Tuple[schemas.OUTPUT_BASE_TYPES, ...]],
):
    types: typing.FrozenSet[typing.Type] = frozenset({
        type(None),
        schemas.immutabledict,
    })
    additional_properties: typing.Type[AdditionalProperties] = dataclasses.field(default_factory=lambda: AdditionalProperties) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            schemas.immutabledict: ObjectNullablePropDict,
        }
    )

    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: None,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> None: ...
    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: typing.Union[
            ObjectNullablePropDictInput,
            ObjectNullablePropDict,
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> ObjectNullablePropDict: ...
    @classmethod
    def validate(
        cls,
        arg,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ):
        return super().validate_base(
            arg,
            configuration=configuration,
        )



@dataclasses.dataclass(frozen=True)
class AdditionalProperties2(
    schemas.Schema[schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES], typing.Tuple[schemas.OUTPUT_BASE_TYPES, ...]],
):
    types: typing.FrozenSet[typing.Type] = frozenset({
        type(None),
        schemas.immutabledict,
    })

    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: None,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> None: ...
    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: typing.Mapping[str, schemas.INPUT_TYPES_ALL],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> schemas.immutabledict[str, schemas.INPUT_TYPES_ALL]: ...
    @classmethod
    def validate(
        cls,
        arg,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ):
        return super().validate_base(
            arg,
            configuration=configuration,
        )



class ObjectAndItemsNullablePropDict(schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES]):
    __required_keys__: typing.FrozenSet[str] = frozenset({
    })
    __optional_keys__: typing.FrozenSet[str] = frozenset({
    })
    
    def get_additional_property_(self, name: str) -> typing.Union[
        None,
        schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES],
    ]:
        schemas.raise_if_key_known(name, self.__required_keys__, self.__optional_keys__)
        return typing.cast(
            typing.Union[
                None,
                schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES],
            ],
            self.__getitem__(name)
        )

    def __new__(cls, arg: ObjectAndItemsNullablePropDictInput, configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None):
        return ObjectAndItemsNullableProp.validate(arg, configuration=configuration)
ObjectAndItemsNullablePropDictInput = typing.Mapping[
    str,
    typing.Union[
        None,
        dict,
        schemas.immutabledict
    ],
]


@dataclasses.dataclass(frozen=True)
class ObjectAndItemsNullableProp(
    schemas.Schema[ObjectAndItemsNullablePropDict, typing.Tuple[schemas.OUTPUT_BASE_TYPES, ...]],
):
    types: typing.FrozenSet[typing.Type] = frozenset({
        type(None),
        schemas.immutabledict,
    })
    additional_properties: typing.Type[AdditionalProperties2] = dataclasses.field(default_factory=lambda: AdditionalProperties2) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            schemas.immutabledict: ObjectAndItemsNullablePropDict,
        }
    )

    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: None,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> None: ...
    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: typing.Union[
            ObjectAndItemsNullablePropDictInput,
            ObjectAndItemsNullablePropDict,
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> ObjectAndItemsNullablePropDict: ...
    @classmethod
    def validate(
        cls,
        arg,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ):
        return super().validate_base(
            arg,
            configuration=configuration,
        )



@dataclasses.dataclass(frozen=True)
class AdditionalProperties3(
    schemas.Schema[schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES], typing.Tuple[schemas.OUTPUT_BASE_TYPES, ...]],
):
    types: typing.FrozenSet[typing.Type] = frozenset({
        type(None),
        schemas.immutabledict,
    })

    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: None,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> None: ...
    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: typing.Mapping[str, schemas.INPUT_TYPES_ALL],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> schemas.immutabledict[str, schemas.INPUT_TYPES_ALL]: ...
    @classmethod
    def validate(
        cls,
        arg,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ):
        return super().validate_base(
            arg,
            configuration=configuration,
        )



class ObjectItemsNullableDict(schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES]):
    __required_keys__: typing.FrozenSet[str] = frozenset({
    })
    __optional_keys__: typing.FrozenSet[str] = frozenset({
    })
    
    def get_additional_property_(self, name: str) -> typing.Union[
        None,
        schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES],
    ]:
        schemas.raise_if_key_known(name, self.__required_keys__, self.__optional_keys__)
        return typing.cast(
            typing.Union[
                None,
                schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES],
            ],
            self.__getitem__(name)
        )

    def __new__(cls, arg: ObjectItemsNullableDictInput, configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None):
        return ObjectItemsNullable.validate(arg, configuration=configuration)
ObjectItemsNullableDictInput = typing.Mapping[
    str,
    typing.Union[
        None,
        dict,
        schemas.immutabledict
    ],
]


@dataclasses.dataclass(frozen=True)
class ObjectItemsNullable(
    schemas.Schema[ObjectItemsNullableDict, tuple]
):
    types: typing.FrozenSet[typing.Type] = frozenset({schemas.immutabledict})
    additional_properties: typing.Type[AdditionalProperties3] = dataclasses.field(default_factory=lambda: AdditionalProperties3) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            schemas.immutabledict: ObjectItemsNullableDict
        }
    )

    @classmethod
    def validate(
        cls,
        arg: typing.Union[
            ObjectItemsNullableDictInput,
            ObjectItemsNullableDict,
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> ObjectItemsNullableDict:
        return super().validate_base(
            arg,
            configuration=configuration,
        )

Properties = typing_extensions.TypedDict(
    'Properties',
    {
        "integer_prop": typing.Type[IntegerProp],
        "number_prop": typing.Type[NumberProp],
        "boolean_prop": typing.Type[BooleanProp],
        "string_prop": typing.Type[StringProp],
        "date_prop": typing.Type[DateProp],
        "datetime_prop": typing.Type[DatetimeProp],
        "array_nullable_prop": typing.Type[ArrayNullableProp],
        "array_and_items_nullable_prop": typing.Type[ArrayAndItemsNullableProp],
        "array_items_nullable": typing.Type[ArrayItemsNullable],
        "object_nullable_prop": typing.Type[ObjectNullableProp],
        "object_and_items_nullable_prop": typing.Type[ObjectAndItemsNullableProp],
        "object_items_nullable": typing.Type[ObjectItemsNullable],
    }
)


class NullableClassDict(schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES]):
    __required_keys__: typing.FrozenSet[str] = frozenset({
    })
    __optional_keys__: typing.FrozenSet[str] = frozenset({
        "integer_prop",
        "number_prop",
        "boolean_prop",
        "string_prop",
        "date_prop",
        "datetime_prop",
        "array_nullable_prop",
        "array_and_items_nullable_prop",
        "array_items_nullable",
        "object_nullable_prop",
        "object_and_items_nullable_prop",
        "object_items_nullable",
    })
    
    @typing.overload
    def get_property(self, name: typing_extensions.Literal["integer_prop"]) -> typing.Union[
        None,
        int,
    ]:
        ...
    
    @typing.overload
    def get_property(self, name: typing_extensions.Literal["number_prop"]) -> typing.Union[
        None,
        typing.Union[int, float],
    ]:
        ...
    
    @typing.overload
    def get_property(self, name: typing_extensions.Literal["boolean_prop"]) -> typing.Union[
        None,
        bool,
    ]:
        ...
    
    @typing.overload
    def get_property(self, name: typing_extensions.Literal["string_prop"]) -> typing.Union[
        None,
        str,
    ]:
        ...
    
    @typing.overload
    def get_property(self, name: typing_extensions.Literal["date_prop"]) -> typing.Union[
        None,
        str,
    ]:
        ...
    
    @typing.overload
    def get_property(self, name: typing_extensions.Literal["datetime_prop"]) -> typing.Union[
        None,
        str,
    ]:
        ...
    
    @typing.overload
    def get_property(self, name: typing_extensions.Literal["array_nullable_prop"]) -> typing.Union[
        None,
        ArrayNullablePropTuple,
    ]:
        ...
    
    @typing.overload
    def get_property(self, name: typing_extensions.Literal["array_and_items_nullable_prop"]) -> typing.Union[
        None,
        ArrayAndItemsNullablePropTuple,
    ]:
        ...
    
    @typing.overload
    def get_property(self, name: typing_extensions.Literal["array_items_nullable"]) -> ArrayItemsNullableTuple:
        ...
    
    @typing.overload
    def get_property(self, name: typing_extensions.Literal["object_nullable_prop"]) -> typing.Union[
        None,
        ObjectNullablePropDict,
    ]:
        ...
    
    @typing.overload
    def get_property(self, name: typing_extensions.Literal["object_and_items_nullable_prop"]) -> typing.Union[
        None,
        ObjectAndItemsNullablePropDict,
    ]:
        ...
    
    @typing.overload
    def get_property(self, name: typing_extensions.Literal["object_items_nullable"]) -> ObjectItemsNullableDict:
        ...
    
    def get_property(self, name):
        val = self.get(name, schemas.unset)
        if name == "integer_prop":
            return val if val is schemas.unset else typing.cast(
                typing.Union[
                    None,
                    int,
                ],
                val
            )
        elif name == "number_prop":
            return val if val is schemas.unset else typing.cast(
                typing.Union[
                    None,
                    typing.Union[int, float],
                ],
                val
            )
        elif name == "boolean_prop":
            return val if val is schemas.unset else typing.cast(
                typing.Union[
                    None,
                    bool,
                ],
                val
            )
        elif name == "string_prop":
            return val if val is schemas.unset else typing.cast(
                typing.Union[
                    None,
                    str,
                ],
                val
            )
        elif name == "date_prop":
            return val if val is schemas.unset else typing.cast(
                typing.Union[
                    None,
                    str,
                ],
                val
            )
        elif name == "datetime_prop":
            return val if val is schemas.unset else typing.cast(
                typing.Union[
                    None,
                    str,
                ],
                val
            )
        elif name == "array_nullable_prop":
            return val if val is schemas.unset else typing.cast(
                typing.Union[
                    None,
                    ArrayNullablePropTuple,
                ],
                val
            )
        elif name == "array_and_items_nullable_prop":
            return val if val is schemas.unset else typing.cast(
                typing.Union[
                    None,
                    ArrayAndItemsNullablePropTuple,
                ],
                val
            )
        elif name == "array_items_nullable":
            return val if val is schemas.unset else typing.cast(
                ArrayItemsNullableTuple,
                val
            )
        elif name == "object_nullable_prop":
            return val if val is schemas.unset else typing.cast(
                typing.Union[
                    None,
                    ObjectNullablePropDict,
                ],
                val
            )
        elif name == "object_and_items_nullable_prop":
            return val if val is schemas.unset else typing.cast(
                typing.Union[
                    None,
                    ObjectAndItemsNullablePropDict,
                ],
                val
            )
        elif name == "object_items_nullable":
            return val if val is schemas.unset else typing.cast(
                ObjectItemsNullableDict,
                val
            )
        raise ValueError(schemas.key_unknown_error_msg(name))
    
    def get_additional_property_(self, name: str) -> typing.Union[
        None,
        schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES],
    ]:
        schemas.raise_if_key_known(name, self.__required_keys__, self.__optional_keys__)
        return typing.cast(
            typing.Union[
                None,
                schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES],
            ],
            self.__getitem__(name)
        )

    def __new__(cls, arg: NullableClassDictInput, configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None):
        return NullableClass.validate(arg, configuration=configuration)
NullableClassDictInput = typing.Mapping[
    str,
    typing.Union[
        typing.Union[
            None,
            int
        ],
        typing.Union[
            None,
            float,
            int
        ],
        typing.Union[
            None,
            bool
        ],
        typing.Union[
            None,
            str
        ],
        typing.Union[
            None,
            str,
            datetime.date
        ],
        typing.Union[
            None,
            str,
            datetime.datetime
        ],
        typing.Union[
            ArrayNullablePropTuple,
            None,
            list,
            tuple
        ],
        typing.Union[
            ArrayAndItemsNullablePropTuple,
            None,
            list,
            tuple
        ],
        typing.Union[
            ArrayItemsNullableTuple,
            list,
            tuple
        ],
        typing.Union[
            ObjectNullablePropDict,
            None,
            dict,
            schemas.immutabledict
        ],
        typing.Union[
            ObjectAndItemsNullablePropDict,
            None,
            dict,
            schemas.immutabledict
        ],
        typing.Union[
            ObjectItemsNullableDict,
            dict,
            schemas.immutabledict
        ],
        typing.Union[
            None,
            dict,
            schemas.immutabledict
        ],
    ]
]


@dataclasses.dataclass(frozen=True)
class NullableClass(
    schemas.Schema[NullableClassDict, tuple]
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """
    types: typing.FrozenSet[typing.Type] = frozenset({schemas.immutabledict})
    properties: Properties = dataclasses.field(default_factory=lambda: schemas.typed_dict_to_instance(Properties)) # type: ignore
    additional_properties: typing.Type[AdditionalProperties4] = dataclasses.field(default_factory=lambda: AdditionalProperties4) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            schemas.immutabledict: NullableClassDict
        }
    )

    @classmethod
    def validate(
        cls,
        arg: typing.Union[
            NullableClassDictInput,
            NullableClassDict,
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> NullableClassDict:
        return super().validate_base(
            arg,
            configuration=configuration,
        )

