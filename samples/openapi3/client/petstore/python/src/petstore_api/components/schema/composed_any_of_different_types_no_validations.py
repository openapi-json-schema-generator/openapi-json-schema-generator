# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *

_0: typing_extensions.TypeAlias = schemas.DictSchema[U]
_1: typing_extensions.TypeAlias = schemas.DateSchema[U]
_2: typing_extensions.TypeAlias = schemas.DateTimeSchema[U]
_3: typing_extensions.TypeAlias = schemas.BinarySchema[U]
_4: typing_extensions.TypeAlias = schemas.StrSchema[U]
_5: typing_extensions.TypeAlias = schemas.StrSchema[U]
_6: typing_extensions.TypeAlias = schemas.DictSchema[U]
_7: typing_extensions.TypeAlias = schemas.BoolSchema[U]
_8: typing_extensions.TypeAlias = schemas.NoneSchema[U]
Items: typing_extensions.TypeAlias = schemas.AnyTypeSchema[U]


class _9(
    schemas.ListSchema[schemas.T]
):


    @dataclasses.dataclass(frozen=True)
    class Schema_(metaclass=schemas.SchemaBase):
        types: typing.FrozenSet[typing.Type] = frozenset({tuple})
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
    ) -> _9[tuple]:
        inst = super().__new__(
            cls,
            arg_,
            configuration_=configuration_,
        )
        inst = typing.cast(
            _9[tuple],
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

_10: typing_extensions.TypeAlias = schemas.NumberSchema[U]
_11: typing_extensions.TypeAlias = schemas.Float32Schema[U]
_12: typing_extensions.TypeAlias = schemas.Float64Schema[U]
_13: typing_extensions.TypeAlias = schemas.IntSchema[U]
_14: typing_extensions.TypeAlias = schemas.Int32Schema[U]
_15: typing_extensions.TypeAlias = schemas.Int64Schema[U]
AnyOf = typing.Tuple[
    typing.Type[_0],
    typing.Type[_1],
    typing.Type[_2],
    typing.Type[_3],
    typing.Type[_4],
    typing.Type[_5],
    typing.Type[_6],
    typing.Type[_7],
    typing.Type[_8],
    typing.Type[_9],
    typing.Type[_10],
    typing.Type[_11],
    typing.Type[_12],
    typing.Type[_13],
    typing.Type[_14],
    typing.Type[_15],
]

class ComposedAnyOfDifferentTypesNoValidations(
    schemas.AnyTypeSchema[schemas.T],
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """


    @dataclasses.dataclass(frozen=True)
    class Schema_(metaclass=schemas.SchemaBase):
        # any type
        any_of: AnyOf = dataclasses.field(default_factory=lambda: schemas.tuple_to_instance(AnyOf)) # type: ignore


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
    ) -> ComposedAnyOfDifferentTypesNoValidations[
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
            ComposedAnyOfDifferentTypesNoValidations[
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

