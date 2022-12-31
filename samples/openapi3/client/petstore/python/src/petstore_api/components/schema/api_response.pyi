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


class ApiResponse(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """


    class Schema_:
        
        class Properties:
            Code = schemas.Int32Schema
            Type = schemas.StrSchema
            Message = schemas.StrSchema
            __annotations__ = {
                "code": Code,
                "type": Type,
                "message": Message,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["code"]) -> Schema_.Properties.Code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> Schema_.Properties.Type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["message"]) -> Schema_.Properties.Message: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal["code"],
            typing_extensions.Literal["type"],
            typing_extensions.Literal["message"],
            str
        ]
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_(self, name: typing_extensions.Literal["code"]) -> typing.Union[Schema_.Properties.Code, schemas.Unset]: ...
    
    @typing.overload
    def get_item_(self, name: typing_extensions.Literal["type"]) -> typing.Union[Schema_.Properties.Type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_(self, name: typing_extensions.Literal["message"]) -> typing.Union[Schema_.Properties.Message, schemas.Unset]: ...
    
    @typing.overload
    def get_item_(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_(
        self,
        name: typing.Union[
            typing_extensions.Literal["code"],
            typing_extensions.Literal["type"],
            typing_extensions.Literal["message"],
            str
        ]
    ):
        return super().get_item_(name)

    def __new__(
        cls,
        *args_: typing.Union[dict, frozendict.frozendict, ],
        code: typing.Union[Schema_.Properties.Code, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        type: typing.Union[Schema_.Properties.Type, str, schemas.Unset] = schemas.unset,
        message: typing.Union[Schema_.Properties.Message, str, schemas.Unset] = schemas.unset,
        configuration_: typing.Optional[schemas.configuration_module.Configuration] = None,
        **kwargs: typing.Union[dict, frozendict.frozendict, list, tuple, decimal.Decimal, float, int, str, datetime.date, datetime.datetime, uuid.UUID, bool, None, bytes, io.FileIO, io.BufferedReader, schemas.Schema],
    ) -> 'ApiResponse':
        return super().__new__(
            cls,
            *args_,
            code=code,
            type=type,
            message=message,
            configuration_=configuration_,
            **kwargs,
        )
