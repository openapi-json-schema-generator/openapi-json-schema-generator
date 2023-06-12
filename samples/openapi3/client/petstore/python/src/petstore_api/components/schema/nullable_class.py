# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *

DictInput10 = typing.Mapping[str, schemas.INPUT_TYPES_ALL_INCL_SCHEMA]


class AdditionalProperties4(
    schemas.NoneBase,
    schemas.DictBase,
    schemas.Schema[schemas.T],
    schemas.NoneFrozenDictMixin
):


    @dataclasses.dataclass(frozen=True)
    class Schema_(metaclass=schemas.SingletonMeta):
        types: typing.FrozenSet[typing.Type] = frozenset({
            schemas.NoneClass,
            frozendict.frozendict,
        })


    def __new__(
        cls,
        arg: typing.Union[
            None,
            DictInput10,
            AdditionalProperties4[frozendict.frozendict],
        ],
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None
    ) -> AdditionalProperties4[
        typing.Union[
            schemas.NoneClass,
            frozendict.frozendict
        ]
    ]:
        inst = super().__new__(
            cls,
            arg,
            configuration_=configuration_,
        )
        inst = typing.cast(
            AdditionalProperties4[
                typing.Union[
                    schemas.NoneClass,
                    frozendict.frozendict
                ]
            ],
            inst
        )
        return inst



class IntegerProp(
    schemas.NoneBase,
    schemas.IntBase,
    schemas.Schema[schemas.T],
    schemas.NoneDecimalMixin
):


    @dataclasses.dataclass(frozen=True)
    class Schema_(metaclass=schemas.SingletonMeta):
        types: typing.FrozenSet[typing.Type] = frozenset({
            schemas.NoneClass,
            decimal.Decimal,
        })
        format: str = 'int'


    def __new__(
        cls,
        arg: typing.Union[
            None,
            decimal.Decimal,
            int
        ],
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None
    ) -> IntegerProp[
        typing.Union[
            schemas.NoneClass,
            decimal.Decimal
        ]
    ]:
        inst = super().__new__(
            cls,
            arg,
            configuration_=configuration_,
        )
        inst = typing.cast(
            IntegerProp[
                typing.Union[
                    schemas.NoneClass,
                    decimal.Decimal
                ]
            ],
            inst
        )
        return inst



class NumberProp(
    schemas.NoneBase,
    schemas.NumberBase,
    schemas.Schema[schemas.T],
    schemas.NoneDecimalMixin
):


    @dataclasses.dataclass(frozen=True)
    class Schema_(metaclass=schemas.SingletonMeta):
        types: typing.FrozenSet[typing.Type] = frozenset({
            schemas.NoneClass,
            decimal.Decimal,
        })


    def __new__(
        cls,
        arg: typing.Union[
            None,
            decimal.Decimal,
            int,
            float
        ],
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None
    ) -> NumberProp[
        typing.Union[
            schemas.NoneClass,
            decimal.Decimal
        ]
    ]:
        inst = super().__new__(
            cls,
            arg,
            configuration_=configuration_,
        )
        inst = typing.cast(
            NumberProp[
                typing.Union[
                    schemas.NoneClass,
                    decimal.Decimal
                ]
            ],
            inst
        )
        return inst



class BooleanProp(
    schemas.NoneBase,
    schemas.BoolBase,
    schemas.Schema[schemas.T],
    schemas.NoneBoolMixin
):


    @dataclasses.dataclass(frozen=True)
    class Schema_(metaclass=schemas.SingletonMeta):
        types: typing.FrozenSet[typing.Type] = frozenset({
            schemas.NoneClass,
            schemas.BoolClass,
        })


    def __new__(
        cls,
        arg: typing.Union[
            None,
            bool
        ],
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None
    ) -> BooleanProp[
        typing.Union[
            schemas.NoneClass,
            schemas.BoolClass
        ]
    ]:
        inst = super().__new__(
            cls,
            arg,
            configuration_=configuration_,
        )
        inst = typing.cast(
            BooleanProp[
                typing.Union[
                    schemas.NoneClass,
                    schemas.BoolClass
                ]
            ],
            inst
        )
        return inst



class StringProp(
    schemas.NoneBase,
    schemas.StrBase,
    schemas.Schema[schemas.T],
    schemas.NoneStrMixin
):


    @dataclasses.dataclass(frozen=True)
    class Schema_(metaclass=schemas.SingletonMeta):
        types: typing.FrozenSet[typing.Type] = frozenset({
            schemas.NoneClass,
            str,
        })


    def __new__(
        cls,
        arg: typing.Union[
            None,
            str
        ],
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None
    ) -> StringProp[
        typing.Union[
            schemas.NoneClass,
            str
        ]
    ]:
        inst = super().__new__(
            cls,
            arg,
            configuration_=configuration_,
        )
        inst = typing.cast(
            StringProp[
                typing.Union[
                    schemas.NoneClass,
                    str
                ]
            ],
            inst
        )
        return inst



class DateProp(
    schemas.NoneBase,
    schemas.DateBase,
    schemas.StrBase,
    schemas.Schema[schemas.T],
    schemas.NoneStrMixin
):


    @dataclasses.dataclass(frozen=True)
    class Schema_(metaclass=schemas.SingletonMeta):
        types: typing.FrozenSet[typing.Type] = frozenset({
            schemas.NoneClass,
            str,
        })
        format: str = 'date'


    def __new__(
        cls,
        arg: typing.Union[
            None,
            str,
            datetime.date
        ],
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None
    ) -> DateProp[
        typing.Union[
            schemas.NoneClass,
            str
        ]
    ]:
        inst = super().__new__(
            cls,
            arg,
            configuration_=configuration_,
        )
        inst = typing.cast(
            DateProp[
                typing.Union[
                    schemas.NoneClass,
                    str
                ]
            ],
            inst
        )
        return inst



class DatetimeProp(
    schemas.NoneBase,
    schemas.DateTimeBase,
    schemas.StrBase,
    schemas.Schema[schemas.T],
    schemas.NoneStrMixin
):


    @dataclasses.dataclass(frozen=True)
    class Schema_(metaclass=schemas.SingletonMeta):
        types: typing.FrozenSet[typing.Type] = frozenset({
            schemas.NoneClass,
            str,
        })
        format: str = 'date-time'


    def __new__(
        cls,
        arg: typing.Union[
            None,
            str,
            datetime.datetime
        ],
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None
    ) -> DatetimeProp[
        typing.Union[
            schemas.NoneClass,
            str
        ]
    ]:
        inst = super().__new__(
            cls,
            arg,
            configuration_=configuration_,
        )
        inst = typing.cast(
            DatetimeProp[
                typing.Union[
                    schemas.NoneClass,
                    str
                ]
            ],
            inst
        )
        return inst

DictInput = typing.Mapping[str, schemas.INPUT_TYPES_ALL_INCL_SCHEMA]
Items: typing_extensions.TypeAlias = schemas.DictSchema[U]


class ArrayNullableProp(
    schemas.NoneBase,
    schemas.ListBase,
    schemas.Schema[schemas.T],
    schemas.NoneTupleMixin
):


    @dataclasses.dataclass(frozen=True)
    class Schema_(metaclass=schemas.SingletonMeta):
        types: typing.FrozenSet[typing.Type] = frozenset({
            schemas.NoneClass,
            tuple,
        })
        items: typing.Type[Items] = dataclasses.field(default_factory=lambda: Items) # type: ignore


    def __new__(
        cls,
        arg: typing.Union[
            None,
            list,
            tuple
        ],
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None
    ) -> ArrayNullableProp[
        typing.Union[
            schemas.NoneClass,
            tuple
        ]
    ]:
        inst = super().__new__(
            cls,
            arg,
            configuration_=configuration_,
        )
        inst = typing.cast(
            ArrayNullableProp[
                typing.Union[
                    schemas.NoneClass,
                    tuple
                ]
            ],
            inst
        )
        return inst

DictInput2 = typing.Mapping[str, schemas.INPUT_TYPES_ALL_INCL_SCHEMA]


class Items2(
    schemas.NoneBase,
    schemas.DictBase,
    schemas.Schema[schemas.T],
    schemas.NoneFrozenDictMixin
):


    @dataclasses.dataclass(frozen=True)
    class Schema_(metaclass=schemas.SingletonMeta):
        types: typing.FrozenSet[typing.Type] = frozenset({
            schemas.NoneClass,
            frozendict.frozendict,
        })


    def __new__(
        cls,
        arg: typing.Union[
            None,
            DictInput2,
            Items2[frozendict.frozendict],
        ],
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None
    ) -> Items2[
        typing.Union[
            schemas.NoneClass,
            frozendict.frozendict
        ]
    ]:
        inst = super().__new__(
            cls,
            arg,
            configuration_=configuration_,
        )
        inst = typing.cast(
            Items2[
                typing.Union[
                    schemas.NoneClass,
                    frozendict.frozendict
                ]
            ],
            inst
        )
        return inst



class ArrayAndItemsNullableProp(
    schemas.NoneBase,
    schemas.ListBase,
    schemas.Schema[schemas.T],
    schemas.NoneTupleMixin
):


    @dataclasses.dataclass(frozen=True)
    class Schema_(metaclass=schemas.SingletonMeta):
        types: typing.FrozenSet[typing.Type] = frozenset({
            schemas.NoneClass,
            tuple,
        })
        items: typing.Type[Items2] = dataclasses.field(default_factory=lambda: Items2) # type: ignore


    def __new__(
        cls,
        arg: typing.Union[
            None,
            list,
            tuple
        ],
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None
    ) -> ArrayAndItemsNullableProp[
        typing.Union[
            schemas.NoneClass,
            tuple
        ]
    ]:
        inst = super().__new__(
            cls,
            arg,
            configuration_=configuration_,
        )
        inst = typing.cast(
            ArrayAndItemsNullableProp[
                typing.Union[
                    schemas.NoneClass,
                    tuple
                ]
            ],
            inst
        )
        return inst

DictInput3 = typing.Mapping[str, schemas.INPUT_TYPES_ALL_INCL_SCHEMA]


class Items3(
    schemas.NoneBase,
    schemas.DictBase,
    schemas.Schema[schemas.T],
    schemas.NoneFrozenDictMixin
):


    @dataclasses.dataclass(frozen=True)
    class Schema_(metaclass=schemas.SingletonMeta):
        types: typing.FrozenSet[typing.Type] = frozenset({
            schemas.NoneClass,
            frozendict.frozendict,
        })


    def __new__(
        cls,
        arg: typing.Union[
            None,
            DictInput3,
            Items3[frozendict.frozendict],
        ],
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None
    ) -> Items3[
        typing.Union[
            schemas.NoneClass,
            frozendict.frozendict
        ]
    ]:
        inst = super().__new__(
            cls,
            arg,
            configuration_=configuration_,
        )
        inst = typing.cast(
            Items3[
                typing.Union[
                    schemas.NoneClass,
                    frozendict.frozendict
                ]
            ],
            inst
        )
        return inst



class ArrayItemsNullable(
    schemas.ListSchema[schemas.T]
):


    @dataclasses.dataclass(frozen=True)
    class Schema_(metaclass=schemas.SingletonMeta):
        types: typing.FrozenSet[typing.Type] = frozenset({tuple})
        items: typing.Type[Items3] = dataclasses.field(default_factory=lambda: Items3) # type: ignore

    def __new__(
        cls,
        arg: typing.Sequence[
            typing.Union[
                Items3[typing.Union[
                    schemas.NoneClass,
                    frozendict.frozendict
                ]],
                None,
                dict,
                frozendict.frozendict
            ]
        ],
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None
    ) -> ArrayItemsNullable[tuple]:
        inst = super().__new__(
            cls,
            arg,
            configuration_=configuration_,
        )
        inst = typing.cast(
            ArrayItemsNullable[tuple],
            inst
        )
        return inst

    def __getitem__(self, name: int) -> Items3[typing.Union[
        schemas.NoneClass,
        frozendict.frozendict
    ]]:
        return super().__getitem__(name)

DictInput4 = typing.Mapping[str, schemas.INPUT_TYPES_ALL_INCL_SCHEMA]
AdditionalProperties: typing_extensions.TypeAlias = schemas.DictSchema[U]
DictInput5 = typing.Mapping[
    str,
    typing.Union[
        AdditionalProperties[frozendict.frozendict],
        dict,
        frozendict.frozendict
    ],
]


class ObjectNullableProp(
    schemas.NoneBase,
    schemas.DictBase,
    schemas.Schema[schemas.T],
    schemas.NoneFrozenDictMixin
):


    @dataclasses.dataclass(frozen=True)
    class Schema_(metaclass=schemas.SingletonMeta):
        types: typing.FrozenSet[typing.Type] = frozenset({
            schemas.NoneClass,
            frozendict.frozendict,
        })
        additional_properties: typing.Type[AdditionalProperties] = dataclasses.field(default_factory=lambda: AdditionalProperties) # type: ignore

    
    def __getitem__(self, name: str) -> AdditionalProperties[frozendict.frozendict]:
        # dict_instance[name] accessor
        return super().__getitem__(name)

    def __new__(
        cls,
        arg: typing.Union[
            None,
            DictInput5,
            ObjectNullableProp[frozendict.frozendict],
        ],
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None
    ) -> ObjectNullableProp[
        typing.Union[
            schemas.NoneClass,
            frozendict.frozendict
        ]
    ]:
        inst = super().__new__(
            cls,
            arg,
            configuration_=configuration_,
        )
        inst = typing.cast(
            ObjectNullableProp[
                typing.Union[
                    schemas.NoneClass,
                    frozendict.frozendict
                ]
            ],
            inst
        )
        return inst

DictInput6 = typing.Mapping[str, schemas.INPUT_TYPES_ALL_INCL_SCHEMA]


class AdditionalProperties2(
    schemas.NoneBase,
    schemas.DictBase,
    schemas.Schema[schemas.T],
    schemas.NoneFrozenDictMixin
):


    @dataclasses.dataclass(frozen=True)
    class Schema_(metaclass=schemas.SingletonMeta):
        types: typing.FrozenSet[typing.Type] = frozenset({
            schemas.NoneClass,
            frozendict.frozendict,
        })


    def __new__(
        cls,
        arg: typing.Union[
            None,
            DictInput6,
            AdditionalProperties2[frozendict.frozendict],
        ],
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None
    ) -> AdditionalProperties2[
        typing.Union[
            schemas.NoneClass,
            frozendict.frozendict
        ]
    ]:
        inst = super().__new__(
            cls,
            arg,
            configuration_=configuration_,
        )
        inst = typing.cast(
            AdditionalProperties2[
                typing.Union[
                    schemas.NoneClass,
                    frozendict.frozendict
                ]
            ],
            inst
        )
        return inst

DictInput7 = typing.Mapping[
    str,
    typing.Union[
        AdditionalProperties2[typing.Union[
            schemas.NoneClass,
            frozendict.frozendict
        ]],
        None,
        dict,
        frozendict.frozendict
    ],
]


class ObjectAndItemsNullableProp(
    schemas.NoneBase,
    schemas.DictBase,
    schemas.Schema[schemas.T],
    schemas.NoneFrozenDictMixin
):


    @dataclasses.dataclass(frozen=True)
    class Schema_(metaclass=schemas.SingletonMeta):
        types: typing.FrozenSet[typing.Type] = frozenset({
            schemas.NoneClass,
            frozendict.frozendict,
        })
        additional_properties: typing.Type[AdditionalProperties2] = dataclasses.field(default_factory=lambda: AdditionalProperties2) # type: ignore

    
    def __getitem__(self, name: str) -> AdditionalProperties2[typing.Union[
        schemas.NoneClass,
        frozendict.frozendict
    ]]:
        # dict_instance[name] accessor
        return super().__getitem__(name)

    def __new__(
        cls,
        arg: typing.Union[
            None,
            DictInput7,
            ObjectAndItemsNullableProp[frozendict.frozendict],
        ],
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None
    ) -> ObjectAndItemsNullableProp[
        typing.Union[
            schemas.NoneClass,
            frozendict.frozendict
        ]
    ]:
        inst = super().__new__(
            cls,
            arg,
            configuration_=configuration_,
        )
        inst = typing.cast(
            ObjectAndItemsNullableProp[
                typing.Union[
                    schemas.NoneClass,
                    frozendict.frozendict
                ]
            ],
            inst
        )
        return inst

DictInput8 = typing.Mapping[str, schemas.INPUT_TYPES_ALL_INCL_SCHEMA]


class AdditionalProperties3(
    schemas.NoneBase,
    schemas.DictBase,
    schemas.Schema[schemas.T],
    schemas.NoneFrozenDictMixin
):


    @dataclasses.dataclass(frozen=True)
    class Schema_(metaclass=schemas.SingletonMeta):
        types: typing.FrozenSet[typing.Type] = frozenset({
            schemas.NoneClass,
            frozendict.frozendict,
        })


    def __new__(
        cls,
        arg: typing.Union[
            None,
            DictInput8,
            AdditionalProperties3[frozendict.frozendict],
        ],
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None
    ) -> AdditionalProperties3[
        typing.Union[
            schemas.NoneClass,
            frozendict.frozendict
        ]
    ]:
        inst = super().__new__(
            cls,
            arg,
            configuration_=configuration_,
        )
        inst = typing.cast(
            AdditionalProperties3[
                typing.Union[
                    schemas.NoneClass,
                    frozendict.frozendict
                ]
            ],
            inst
        )
        return inst

DictInput9 = typing.Mapping[
    str,
    typing.Union[
        AdditionalProperties3[typing.Union[
            schemas.NoneClass,
            frozendict.frozendict
        ]],
        None,
        dict,
        frozendict.frozendict
    ],
]


class ObjectItemsNullable(
    schemas.DictSchema[schemas.T]
):


    @dataclasses.dataclass(frozen=True)
    class Schema_(metaclass=schemas.SingletonMeta):
        types: typing.FrozenSet[typing.Type] = frozenset({frozendict.frozendict})
        additional_properties: typing.Type[AdditionalProperties3] = dataclasses.field(default_factory=lambda: AdditionalProperties3) # type: ignore
    
    def __getitem__(self, name: str) -> AdditionalProperties3[typing.Union[
        schemas.NoneClass,
        frozendict.frozendict
    ]]:
        # dict_instance[name] accessor
        return super().__getitem__(name)

    def __new__(
        cls,
        arg: typing.Union[
            DictInput9,
            ObjectItemsNullable[frozendict.frozendict],
        ],
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None
    ) -> ObjectItemsNullable[frozendict.frozendict]:
        inst = super().__new__(
            cls,
            arg,
            configuration_=configuration_,
        )
        inst = typing.cast(
            ObjectItemsNullable[frozendict.frozendict],
            inst
        )
        return inst

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
DictInput11 = typing.Mapping[
    str,
    typing.Union[
        typing.Union[
            IntegerProp[typing.Union[
                schemas.NoneClass,
                decimal.Decimal
            ]],
            None,
            decimal.Decimal,
            int
        ],
        typing.Union[
            NumberProp[typing.Union[
                schemas.NoneClass,
                decimal.Decimal
            ]],
            None,
            decimal.Decimal,
            int,
            float
        ],
        typing.Union[
            BooleanProp[typing.Union[
                schemas.NoneClass,
                schemas.BoolClass
            ]],
            None,
            bool
        ],
        typing.Union[
            StringProp[typing.Union[
                schemas.NoneClass,
                str
            ]],
            None,
            str
        ],
        typing.Union[
            DateProp[typing.Union[
                schemas.NoneClass,
                str
            ]],
            None,
            str,
            datetime.date
        ],
        typing.Union[
            DatetimeProp[typing.Union[
                schemas.NoneClass,
                str
            ]],
            None,
            str,
            datetime.datetime
        ],
        typing.Union[
            ArrayNullableProp[typing.Union[
                schemas.NoneClass,
                tuple
            ]],
            None,
            list,
            tuple
        ],
        typing.Union[
            ArrayAndItemsNullableProp[typing.Union[
                schemas.NoneClass,
                tuple
            ]],
            None,
            list,
            tuple
        ],
        typing.Union[
            ArrayItemsNullable[tuple],
            list,
            tuple
        ],
        typing.Union[
            ObjectNullableProp[typing.Union[
                schemas.NoneClass,
                frozendict.frozendict
            ]],
            None,
            dict,
            frozendict.frozendict
        ],
        typing.Union[
            ObjectAndItemsNullableProp[typing.Union[
                schemas.NoneClass,
                frozendict.frozendict
            ]],
            None,
            dict,
            frozendict.frozendict
        ],
        typing.Union[
            ObjectItemsNullable[frozendict.frozendict],
            dict,
            frozendict.frozendict
        ],
        typing.Union[
            AdditionalProperties4[typing.Union[
                schemas.NoneClass,
                frozendict.frozendict
            ]],
            None,
            dict,
            frozendict.frozendict
        ],
    ]
]


class NullableClass(
    schemas.DictSchema[schemas.T]
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """


    @dataclasses.dataclass(frozen=True)
    class Schema_(metaclass=schemas.SingletonMeta):
        types: typing.FrozenSet[typing.Type] = frozenset({frozendict.frozendict})
        properties: Properties = dataclasses.field(default_factory=lambda: schemas.typed_dict_to_instance(Properties)) # type: ignore
        additional_properties: typing.Type[AdditionalProperties4] = dataclasses.field(default_factory=lambda: AdditionalProperties4) # type: ignore
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["integer_prop"]) -> IntegerProp[typing.Union[
        schemas.NoneClass,
        decimal.Decimal
    ]]: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["number_prop"]) -> NumberProp[typing.Union[
        schemas.NoneClass,
        decimal.Decimal
    ]]: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["boolean_prop"]) -> BooleanProp[typing.Union[
        schemas.NoneClass,
        schemas.BoolClass
    ]]: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["string_prop"]) -> StringProp[typing.Union[
        schemas.NoneClass,
        str
    ]]: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["date_prop"]) -> DateProp[typing.Union[
        schemas.NoneClass,
        str
    ]]: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["datetime_prop"]) -> DatetimeProp[typing.Union[
        schemas.NoneClass,
        str
    ]]: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["array_nullable_prop"]) -> ArrayNullableProp[typing.Union[
        schemas.NoneClass,
        tuple
    ]]: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["array_and_items_nullable_prop"]) -> ArrayAndItemsNullableProp[typing.Union[
        schemas.NoneClass,
        tuple
    ]]: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["array_items_nullable"]) -> ArrayItemsNullable[tuple]: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["object_nullable_prop"]) -> ObjectNullableProp[typing.Union[
        schemas.NoneClass,
        frozendict.frozendict
    ]]: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["object_and_items_nullable_prop"]) -> ObjectAndItemsNullableProp[typing.Union[
        schemas.NoneClass,
        frozendict.frozendict
    ]]: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["object_items_nullable"]) -> ObjectItemsNullable[frozendict.frozendict]: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> AdditionalProperties4[typing.Union[
        schemas.NoneClass,
        frozendict.frozendict
    ]]: ...
    
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal["integer_prop"],
            typing_extensions.Literal["number_prop"],
            typing_extensions.Literal["boolean_prop"],
            typing_extensions.Literal["string_prop"],
            typing_extensions.Literal["date_prop"],
            typing_extensions.Literal["datetime_prop"],
            typing_extensions.Literal["array_nullable_prop"],
            typing_extensions.Literal["array_and_items_nullable_prop"],
            typing_extensions.Literal["array_items_nullable"],
            typing_extensions.Literal["object_nullable_prop"],
            typing_extensions.Literal["object_and_items_nullable_prop"],
            typing_extensions.Literal["object_items_nullable"],
            str
        ]
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    def __new__(
        cls,
        arg: typing.Union[
            DictInput11,
            NullableClass[frozendict.frozendict],
        ],
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None
    ) -> NullableClass[frozendict.frozendict]:
        inst = super().__new__(
            cls,
            arg,
            configuration_=configuration_,
        )
        inst = typing.cast(
            NullableClass[frozendict.frozendict],
            inst
        )
        return inst

