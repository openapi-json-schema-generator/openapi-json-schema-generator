# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

import datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from petstore_api import schemas  # noqa: F401


class FileSchemaTestClass(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """


    class Schema_:
        types = {frozendict.frozendict}
        
        class Properties:
        
            @staticmethod
            def file() -> typing.Type['file.File']:
                return file.File
            
            
            class Files(
                schemas.ListSchema
            ):
            
            
                class Schema_:
                    types = {tuple}
                    
                    @staticmethod
                    def items() -> typing.Type['file.File']:
                        return file.File
            
                def __new__(
                    cls,
                    arg_: typing.Union[
                        typing.Tuple[
                            typing.Union['file.File', dict, frozendict.frozendict], ...
                        ],
                        typing.List[
                            typing.Union['file.File', dict, frozendict.frozendict]
                        ],
                    ],
                    configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
                ) -> 'Files':
                    return super().__new__(
                        cls,
                        arg_,
                        configuration_=configuration_,
                    )
            
                def __getitem__(self, i: int) -> 'file.File':
                    return super().__getitem__(i)
            __annotations__ = {
                "file": file,
                "files": Files,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["file"]) -> 'file.File': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["files"]) -> Schema_.Properties.Files: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal["file"],
            typing_extensions.Literal["files"],
            str
        ]
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_(self, name: typing_extensions.Literal["file"]) -> typing.Union['file.File', schemas.Unset]: ...
    
    @typing.overload
    def get_item_(self, name: typing_extensions.Literal["files"]) -> typing.Union[Schema_.Properties.Files, schemas.Unset]: ...
    
    @typing.overload
    def get_item_(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_(
        self,
        name: typing.Union[
            typing_extensions.Literal["file"],
            typing_extensions.Literal["files"],
            str
        ]
    ):
        return super().get_item_(name)

    def __new__(
        cls,
        *args_: typing.Union[dict, frozendict.frozendict],
        file: typing.Union['file.File', dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        files: typing.Union[Schema_.Properties.Files, list, tuple, schemas.Unset] = schemas.unset,
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
        **kwargs: typing.Union[dict, frozendict.frozendict, list, tuple, decimal.Decimal, float, int, str, datetime.date, datetime.datetime, uuid.UUID, bool, None, bytes, io.FileIO, io.BufferedReader, schemas.Schema],
    ) -> 'FileSchemaTestClass':
        return super().__new__(
            cls,
            *args_,
            file=file,
            files=files,
            configuration_=configuration_,
            **kwargs,
        )

from petstore_api.components.schema import file
