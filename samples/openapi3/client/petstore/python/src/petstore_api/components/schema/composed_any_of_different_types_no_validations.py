# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *


class ComposedAnyOfDifferentTypesNoValidations(
    schemas.AnyTypeSchema[schemas.T],
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """


    class Schema_:
        # any type
        
        class AnyOf:
            _0: typing_extensions.TypeAlias = schemas.DictSchema[U]
            _1: typing_extensions.TypeAlias = schemas.DateSchema[U]
            _2: typing_extensions.TypeAlias = schemas.DateTimeSchema[U]
            _3: typing_extensions.TypeAlias = schemas.BinarySchema[U]
            _4: typing_extensions.TypeAlias = schemas.StrSchema[U]
            _5: typing_extensions.TypeAlias = schemas.StrSchema[U]
            _6: typing_extensions.TypeAlias = schemas.DictSchema[U]
            _7: typing_extensions.TypeAlias = schemas.BoolSchema[U]
            _8: typing_extensions.TypeAlias = schemas.NoneSchema[U]
            
            
            class _9(
                schemas.ListSchema[schemas.T]
            ):
            
            
                class Schema_:
                    types = {tuple}
                    Items: typing_extensions.TypeAlias = schemas.AnyTypeSchema[U]
            
                def __new__(
                    cls,
                    arg_: typing.Union[
                        typing.Tuple[
                            typing.Union[
                                Schema_.Items[typing.Union[
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
                            ], ...
                        ],
                        typing.List[
                            typing.Union[
                                Schema_.Items[typing.Union[
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
                    ],
                    configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
                ) -> ComposedAnyOfDifferentTypesNoValidations.Schema_.AnyOf._9[tuple]:
                    inst = super().__new__(
                        cls,
                        arg_,
                        configuration_=configuration_,
                    )
                    inst = typing.cast(
                        ComposedAnyOfDifferentTypesNoValidations.Schema_.AnyOf._9[tuple],
                        inst
                    )
                    return inst
            
                def __getitem__(self, name: int) -> Schema_.Items[typing.Union[
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
            classes = [
                _0,
                _1,
                _2,
                _3,
                _4,
                _5,
                _6,
                _7,
                _8,
                _9,
                _10,
                _11,
                _12,
                _13,
                _14,
                _15,
            ]


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
        **kwargs: typing.Union[dict, frozendict.frozendict, list, tuple, decimal.Decimal, float, int, str, datetime.date, datetime.datetime, uuid.UUID, bool, None, bytes, io.FileIO, io.BufferedReader, schemas.Schema],
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
