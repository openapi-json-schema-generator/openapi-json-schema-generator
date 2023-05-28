# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *


class JSONPatchRequest(
    schemas.ListSchema[schemas.T]
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """


    class Schema_:
        types = {tuple}
        
        
        class Items(
            schemas.AnyTypeSchema[schemas.T],
        ):
        
        
            class Schema_:
                # any type
                
                class OneOf:
                
                    @staticmethod
                    def _0() -> typing.Type[json_patch_request_add_replace_test.JSONPatchRequestAddReplaceTest]:
                        return json_patch_request_add_replace_test.JSONPatchRequestAddReplaceTest
                
                    @staticmethod
                    def _1() -> typing.Type[json_patch_request_remove.JSONPatchRequestRemove]:
                        return json_patch_request_remove.JSONPatchRequestRemove
                
                    @staticmethod
                    def _2() -> typing.Type[json_patch_request_move_copy.JSONPatchRequestMoveCopy]:
                        return json_patch_request_move_copy.JSONPatchRequestMoveCopy
                    classes = [
                        _0,
                        _1,
                        _2,
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
            ) -> JSONPatchRequest.Schema_.Items[
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
                    JSONPatchRequest.Schema_.Items[
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

    def __new__(
        cls,
        arg_: typing.Sequence[
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
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
    ) -> JSONPatchRequest[tuple]:
        inst = super().__new__(
            cls,
            arg_,
            configuration_=configuration_,
        )
        inst = typing.cast(
            JSONPatchRequest[tuple],
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

from petstore_api.components.schema import json_patch_request_add_replace_test
from petstore_api.components.schema import json_patch_request_move_copy
from petstore_api.components.schema import json_patch_request_remove
