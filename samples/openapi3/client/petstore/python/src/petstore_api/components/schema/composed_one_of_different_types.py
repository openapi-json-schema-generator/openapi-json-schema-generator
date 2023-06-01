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


class _4(
    schemas.DictSchema[schemas.T]
):


    @dataclasses.dataclass(frozen=True)
    class Schema_:
        types: typing.FrozenSet[typing.Type] = frozenset({frozendict.frozendict})
        max_properties: int = 4
        min_properties: int = 4

    def __new__(
        cls,
        *args_: typing.Union[dict, frozendict.frozendict],
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
        **kwargs: typing.Union[
            dict,
            frozendict.frozendict,
            list,
            tuple,
            decimal.Decimal,
            float,
            int,
            str,
            datetime.date,
            datetime.datetime,
            uuid.UUID,
            bool,
            None,
            bytes,
            io.FileIO,
            io.BufferedReader,
            schemas.Schema
        ],
    ) -> _4[frozendict.frozendict]:
        inst = super().__new__(
            cls,
            *args_,
            configuration_=configuration_,
            **kwargs,
        )
        inst = typing.cast(
            _4[frozendict.frozendict],
            inst
        )
        return inst

Items: typing_extensions.TypeAlias = schemas.AnyTypeSchema[U]


class _5(
    schemas.ListSchema[schemas.T]
):


    @dataclasses.dataclass(frozen=True)
    class Schema_:
        types: typing.FrozenSet[typing.Type] = frozenset({tuple})
        max_items: int = 4
        min_items: int = 4
        items: typing.Type[Items] = dataclasses.field(default_factory=lambda: Items) # type: ignore

    def __new__(
        cls,
        arg_: typing.Sequence[
            typing.Union[
                Items[typing.Union[
                    frozendict.frozendict,
                    str,
                    decimal.Decimal,
                    schemas.BoolClass,
                    schemas.NoneClass,
                    tuple,
                    bytes,
                    schemas.FileIO
                ]],
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
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
    ) -> _5[tuple]:
        inst = super().__new__(
            cls,
            arg_,
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
    class Schema_:
        types: typing.FrozenSet[typing.Type] = frozenset({
            str,
        })
        format = 'date-time'
        regex={
            'pattern': r'^2020.*',  # noqa: E501
        }


class ComposedOneOfDifferentTypes(
    schemas.AnyTypeSchema[schemas.T],
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.

    this is a model that allows payloads of type object or number
    """


    @dataclasses.dataclass(frozen=True)
    class Schema_:
        # any type
        
        one_of: typing.Tuple[
            typing.Type[number_with_validations.NumberWithValidations],
            typing.Type[animal.Animal],
            typing.Type[_2],
            typing.Type[_3],
            typing.Type[_4],
            typing.Type[_5],
            typing.Type[_6],
        ] = dataclasses.field(default_factory=lambda: (
            number_with_validations.NumberWithValidations,
            animal.Animal,
            _2,
            _3,
            _4,
            _5,
            _6,
        )) # type: ignore


    def __new__(
        cls,
        *args_: typing.Union[
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
        ],
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
        **kwargs: typing.Union[
            dict,
            frozendict.frozendict,
            list,
            tuple,
            decimal.Decimal,
            float,
            int,
            str,
            datetime.date,
            datetime.datetime,
            uuid.UUID,
            bool,
            None,
            bytes,
            io.FileIO,
            io.BufferedReader,
            schemas.Schema
        ],
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
            *args_,
            configuration_=configuration_,
            **kwargs,
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
