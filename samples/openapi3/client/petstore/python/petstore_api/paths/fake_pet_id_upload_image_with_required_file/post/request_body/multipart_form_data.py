# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
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


class MultipartFormData(
    schemas.DictSchema
):


    class Schema_:
        types = {frozendict.frozendict}
        required = {
            "requiredFile",
        }
        
        class Properties:
            AdditionalMetadata = schemas.StrSchema
            RequiredFile = schemas.BinarySchema
            __annotations__ = {
                "additionalMetadata": AdditionalMetadata,
                "requiredFile": RequiredFile,
            }
    
    requiredFile: Schema_.Properties.RequiredFile
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["requiredFile"]) -> Schema_.Properties.RequiredFile: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["additionalMetadata"]) -> Schema_.Properties.AdditionalMetadata: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal["requiredFile"],
            typing_extensions.Literal["additionalMetadata"],
            str
        ]
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_(self, name: typing_extensions.Literal["requiredFile"]) -> Schema_.Properties.RequiredFile: ...
    
    @typing.overload
    def get_item_(self, name: typing_extensions.Literal["additionalMetadata"]) -> typing.Union[Schema_.Properties.AdditionalMetadata, schemas.Unset]: ...
    
    @typing.overload
    def get_item_(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_(
        self,
        name: typing.Union[
            typing_extensions.Literal["requiredFile"],
            typing_extensions.Literal["additionalMetadata"],
            str
        ]
    ):
        return super().get_item_(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        requiredFile: typing.Union[Schema_.Properties.RequiredFile, bytes, io.FileIO, io.BufferedReader, ],
        additionalMetadata: typing.Union[Schema_.Properties.AdditionalMetadata, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.configuration_module.Configuration] = None,
        **kwargs: typing.Union[dict, frozendict.frozendict, list, tuple, decimal.Decimal, float, int, str, datetime.date, datetime.datetime, uuid.UUID, bool, None, bytes, io.FileIO, io.BufferedReader, schemas.Schema],
    ) -> 'MultipartFormData':
        return super().__new__(
            cls,
            *_args,
            requiredFile=requiredFile,
            additionalMetadata=additionalMetadata,
            _configuration=_configuration,
            **kwargs,
        )
