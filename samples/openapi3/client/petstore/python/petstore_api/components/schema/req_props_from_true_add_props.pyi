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


class ReqPropsFromTrueAddProps(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "invalid-name",
            "validName",
        }
        AdditionalProperties = schemas.AnyTypeSchema
    
    validName: MetaOapg.AdditionalProperties
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["invalid-name"]) -> MetaOapg.AdditionalProperties: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["validName"]) -> MetaOapg.AdditionalProperties: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> MetaOapg.AdditionalProperties: ...
    
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal["invalid-name"],
            typing_extensions.Literal["validName"],
            str
        ]
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["invalid-name"]) -> MetaOapg.AdditionalProperties: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["validName"]) -> MetaOapg.AdditionalProperties: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[MetaOapg.AdditionalProperties, schemas.Unset]: ...
    
    def get_item_oapg(
        self,
        name: typing.Union[
            typing_extensions.Literal["invalid-name"],
            typing_extensions.Literal["validName"],
            str
        ]
    ):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        validName: typing.Union[MetaOapg.AdditionalProperties, dict, frozendict.frozendict, str, datetime.date, datetime.datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        _configuration: typing.Optional[schemas.configuration_module.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.AdditionalProperties, dict, frozendict.frozendict, str, datetime.date, datetime.datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
    ) -> 'ReqPropsFromTrueAddProps':
        return super().__new__(
            cls,
            *_args,
            validName=validName,
            _configuration=_configuration,
            **kwargs,
        )
