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


class ObjectWithDecimalProperties(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class Properties:
        
            @staticmethod
            def length() -> typing.Type['decimal_payload.DecimalPayload']:
                return decimal_payload.DecimalPayload
            Width = schemas.DecimalSchema
        
            @staticmethod
            def cost() -> typing.Type['money.Money']:
                return money.Money
            __annotations__ = {
                "length": length,
                "width": Width,
                "cost": cost,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["length"]) -> 'decimal_payload.DecimalPayload': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["width"]) -> MetaOapg.Properties.Width: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cost"]) -> 'money.Money': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal["length"],
            typing_extensions.Literal["width"],
            typing_extensions.Literal["cost"],
            str
        ]
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_(self, name: typing_extensions.Literal["length"]) -> typing.Union['decimal_payload.DecimalPayload', schemas.Unset]: ...
    
    @typing.overload
    def get_item_(self, name: typing_extensions.Literal["width"]) -> typing.Union[MetaOapg.Properties.Width, schemas.Unset]: ...
    
    @typing.overload
    def get_item_(self, name: typing_extensions.Literal["cost"]) -> typing.Union['money.Money', schemas.Unset]: ...
    
    @typing.overload
    def get_item_(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_(
        self,
        name: typing.Union[
            typing_extensions.Literal["length"],
            typing_extensions.Literal["width"],
            typing_extensions.Literal["cost"],
            str
        ]
    ):
        return super().get_item_(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        length: typing.Union['decimal_payload.DecimalPayload', schemas.Unset] = schemas.unset,
        width: typing.Union[MetaOapg.Properties.Width, str, schemas.Unset] = schemas.unset,
        cost: typing.Union['money.Money', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.configuration_module.Configuration] = None,
        **kwargs: typing.Union[dict, frozendict.frozendict, list, tuple, decimal.Decimal, float, int, str, datetime.date, datetime.datetime, uuid.UUID, bool, None, bytes, io.FileIO, io.BufferedReader, schemas.Schema],
    ) -> 'ObjectWithDecimalProperties':
        return super().__new__(
            cls,
            *_args,
            length=length,
            width=width,
            cost=cost,
            _configuration=_configuration,
            **kwargs,
        )

from petstore_api.components.schema import decimal_payload
from petstore_api.components.schema import money
