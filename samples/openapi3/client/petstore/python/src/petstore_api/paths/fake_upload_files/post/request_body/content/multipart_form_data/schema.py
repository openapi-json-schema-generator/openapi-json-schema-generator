# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *


class Schema(
    schemas.DictSchema[schemas.T]
):


    class Schema_:
        types = {frozendict.frozendict}
        
        class Properties:
            
            
            class Files(
                schemas.ListSchema[schemas.T]
            ):
            
            
                class Schema_:
                    types = {tuple}
                    Items: typing_extensions.TypeAlias = schemas.BinarySchema[U]
            
                def __new__(
                    cls,
                    arg_: typing.Union[
                        typing.Tuple[
                            typing.Union[
                                Schema_.Items[typing.Union[bytes, schemas.FileIO]],
                                bytes,
                                io.FileIO,
                                io.BufferedReader
                            ], ...
                        ],
                        typing.List[
                            typing.Union[
                                Schema_.Items[typing.Union[bytes, schemas.FileIO]],
                                bytes,
                                io.FileIO,
                                io.BufferedReader
                            ]
                        ],
                    ],
                    configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
                ) -> Schema.Schema_.Properties.Files[tuple]:
                    inst = super().__new__(
                        cls,
                        arg_,
                        configuration_=configuration_,
                    )
                    inst = typing.cast(
                        Schema.Schema_.Properties.Files[tuple],
                        inst
                    )
                    return inst
            
                def __getitem__(self, name: int) -> Schema_.Items[typing.Union[bytes, schemas.FileIO]]:
                    return super().__getitem__(name)
            __annotations__ = {
                "files": Files,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["files"]) -> Schema_.Properties.Files[tuple]: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.AnyTypeSchema[typing.Union[
        frozendict.frozendict,
        str,
        decimal.Decimal,
        schemas.BoolClass,
        schemas.NoneClass,
        tuple,
        bytes,
        schemas.FileIO
    ]]: ...
    
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal["files"],
            str
        ]
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    def __new__(
        cls,
        *args_: typing.Union[dict, frozendict.frozendict],
        files: typing.Union[
            Schema_.Properties.Files[tuple],
            schemas.Unset,
            list,
            tuple
        ] = schemas.unset,
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
        **kwargs: typing.Union[dict, frozendict.frozendict, list, tuple, decimal.Decimal, float, int, str, datetime.date, datetime.datetime, uuid.UUID, bool, None, bytes, io.FileIO, io.BufferedReader, schemas.Schema],
    ) -> Schema[frozendict.frozendict]:
        inst = super().__new__(
            cls,
            *args_,
            files=files,
            configuration_=configuration_,
            **kwargs,
        )
        inst = typing.cast(
            Schema[frozendict.frozendict],
            inst
        )
        return inst
