# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *

_2: typing_extensions.TypeAlias = schemas.NoneSchema[U]
_3: typing_extensions.TypeAlias = schemas.DateSchema[U]
DictInput = typing.Mapping[str, schemas.INPUT_TYPES_ALL_INCL_SCHEMA]


class _4(
    schemas.DictSchema[schemas.T]
):


    @dataclasses.dataclass(frozen=True)
    class Schema_(metaclass=schemas.SingletonMeta):
        types: typing.FrozenSet[typing.Type] = frozenset({frozendict.frozendict})
        max_properties: int = 4
        min_properties: int = 4

    def __new__(
        cls,
        arg: typing.Union[
            DictInput,
            _4[frozendict.frozendict],
        ],
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None
    ) -> _4[frozendict.frozendict]:
        inst = super().__new__(
            cls,
            arg,
            configuration_=configuration_,
        )
        inst = typing.cast(
            _4[frozendict.frozendict],
            inst
        )
        return inst

DictInput2 = typing.Mapping[str, schemas.INPUT_TYPES_ALL_INCL_SCHEMA]
Items: typing_extensions.TypeAlias = schemas.AnyTypeSchema[U]


class _5(
    schemas.ListSchema[schemas.T]
):


    @dataclasses.dataclass(frozen=True)
    class Schema_(metaclass=schemas.SingletonMeta):
        types: typing.FrozenSet[typing.Type] = frozenset({tuple})
        max_items: int = 4
        min_items: int = 4
        items: typing.Type[Items] = dataclasses.field(default_factory=lambda: Items) # type: ignore

    def __new__(
        cls,
        arg: typing.Sequence[
            typing.Union[
                Items[
                    schemas.INPUT_BASE_TYPES
                ],
                dict,
                frozendict.frozendict,
                str,
                datetime.date,
                datetime.datetime,
                uuid.UUID,
                int,
                float,
                decimal.Decimal,
                bool,
                None,
                list,
                tuple,
                bytes,
                io.FileIO,
                io.BufferedReader
            ]
        ],
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None
    ) -> _5[tuple]:
        inst = super().__new__(
            cls,
            arg,
            configuration_=configuration_,
        )
        inst = typing.cast(
            _5[tuple],
            inst
        )
        return inst

    def __getitem__(self, name: int) -> Items[typing.Union[
        frozendict.frozendict,
        str,
        decimal.Decimal,
        schemas.BoolClass,
        schemas.NoneClass,
        tuple,
        bytes,
        schemas.FileIO
    ]]:
        return super().__getitem__(name)



class _6(
    schemas.DateTimeSchema[schemas.T]
):


    @dataclasses.dataclass(frozen=True)
    class Schema_(metaclass=schemas.SingletonMeta):
        types: typing.FrozenSet[typing.Type] = frozenset({
            str,
        })
        format: str = 'date-time'
        pattern: schemas.PatternInfo = schemas.PatternInfo(
            pattern=r'^2020.*'  # noqa: E501
        )
DictInput3 = typing.Mapping[str, schemas.INPUT_TYPES_ALL_INCL_SCHEMA]


class ComposedOneOfDifferentTypes(
    schemas.AnyTypeSchema[schemas.T],
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.

    this is a model that allows payloads of type object or number
    """


    @dataclasses.dataclass(frozen=True)
    class Schema_(metaclass=schemas.SingletonMeta):
        # any type
        one_of: OneOf = dataclasses.field(default_factory=lambda: schemas.tuple_to_instance(OneOf)) # type: ignore


    def __new__(
        cls,
        arg: typing.Union[
            DictInput3,
            schemas.INPUT_TYPES_ALL_INCL_SCHEMA
        ],
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None
    ) -> ComposedOneOfDifferentTypes[
        typing.Union[
            frozendict.frozendict,
            str,
            decimal.Decimal,
            schemas.BoolClass,
            schemas.NoneClass,
            tuple,
            bytes,
            schemas.FileIO
        ]
    ]:
        inst = super().__new__(
            cls,
            arg,
            configuration_=configuration_,
        )
        inst = typing.cast(
            ComposedOneOfDifferentTypes[
                typing.Union[
                    frozendict.frozendict,
                    str,
                    decimal.Decimal,
                    schemas.BoolClass,
                    schemas.NoneClass,
                    tuple,
                    bytes,
                    schemas.FileIO
                ]
            ],
            inst
        )
        return inst


from petstore_api.components.schema import animal
from petstore_api.components.schema import number_with_validations
OneOf = typing.Tuple[
    typing.Type[number_with_validations.NumberWithValidations],
    typing.Type[animal.Animal],
    typing.Type[_2[schemas.U]],
    typing.Type[_3[schemas.U]],
    typing.Type[_4[schemas.U]],
    typing.Type[_5[schemas.U]],
    typing.Type[_6[schemas.U]],
]
