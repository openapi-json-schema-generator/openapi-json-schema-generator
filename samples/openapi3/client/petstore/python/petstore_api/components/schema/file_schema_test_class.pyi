# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
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
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def file() -> typing.Type['file.File']:
                return file.File
            
            
            class files(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    types = {tuple}
                    
                    @staticmethod
                    def items() -> typing.Type['file.File']:
                        return file.File
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['file.File'], typing.List['file.File']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'files':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'file.File':
                    return super().__getitem__(i)
            __annotations__ = {
                "file": file,
                "files": files,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["file"]) -> 'file.File': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["files"]) -> MetaOapg.properties.files: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["file"], typing_extensions.Literal["files"], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["file"]) -> typing.Union['file.File', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["files"]) -> typing.Union[MetaOapg.properties.files, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["file"], typing_extensions.Literal["files"], str]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        file: typing.Union['file.File', schemas.Unset] = schemas.unset,
        files: typing.Union[MetaOapg.properties.files, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'FileSchemaTestClass':
        return super().__new__(
            cls,
            *_args,
            file=file,
            files=files,
            _configuration=_configuration,
            **kwargs,
        )

from petstore_api.components.schema import file
