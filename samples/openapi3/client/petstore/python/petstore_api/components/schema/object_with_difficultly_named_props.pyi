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


class ObjectWithDifficultlyNamedProps(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    model with properties that have invalid names for python
    """


    class Schema_:
        required = {
            "123-list",
        }
        
        class Properties:
            SpecialPropertyName = schemas.Int64Schema
            _123List = schemas.StrSchema
            _123Number = schemas.IntSchema
            __annotations__ = {
                "$special[property.name]": SpecialPropertyName,
                "123-list": _123List,
                "123Number": _123Number,
            }
    
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["123-list"]) -> Schema_.Properties._123List: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["$special[property.name]"]) -> Schema_.Properties.SpecialPropertyName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["123Number"]) -> Schema_.Properties._123Number: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal["123-list"],
            typing_extensions.Literal["$special[property.name]"],
            typing_extensions.Literal["123Number"],
            str
        ]
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_(self, name: typing_extensions.Literal["123-list"]) -> Schema_.Properties._123List: ...
    
    @typing.overload
    def get_item_(self, name: typing_extensions.Literal["$special[property.name]"]) -> typing.Union[Schema_.Properties.SpecialPropertyName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_(self, name: typing_extensions.Literal["123Number"]) -> typing.Union[Schema_.Properties._123Number, schemas.Unset]: ...
    
    @typing.overload
    def get_item_(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_(
        self,
        name: typing.Union[
            typing_extensions.Literal["123-list"],
            typing_extensions.Literal["$special[property.name]"],
            typing_extensions.Literal["123Number"],
            str
        ]
    ):
        return super().get_item_(name)

    def __new__(
        cls,
        *args_: typing.Union[dict, frozendict.frozendict, ],
        configuration_: typing.Optional[schemas.configuration_module.Configuration] = None,
        **kwargs: typing.Union[dict, frozendict.frozendict, list, tuple, decimal.Decimal, float, int, str, datetime.date, datetime.datetime, uuid.UUID, bool, None, bytes, io.FileIO, io.BufferedReader, schemas.Schema],
    ) -> 'ObjectWithDifficultlyNamedProps':
        return super().__new__(
            cls,
            *args_,
            configuration_=configuration_,
            **kwargs,
        )
