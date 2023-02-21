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


class ObjectWithCollidingProperties(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.

    component with properties that have name collisions
    """


    class Schema_:
        types = {frozendict.frozendict}
        
        class Properties:
            SomeProp = schemas.DictSchema
            Someprop = schemas.DictSchema
            __annotations__ = {
                "someProp": SomeProp,
                "someprop": Someprop,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["someProp"]) -> Schema_.Properties.SomeProp: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["someprop"]) -> Schema_.Properties.Someprop: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal["someProp"],
            typing_extensions.Literal["someprop"],
            str
        ]
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_(self, name: typing_extensions.Literal["someProp"]) -> typing.Union[Schema_.Properties.SomeProp, schemas.Unset]: ...
    
    @typing.overload
    def get_item_(self, name: typing_extensions.Literal["someprop"]) -> typing.Union[Schema_.Properties.Someprop, schemas.Unset]: ...
    
    @typing.overload
    def get_item_(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_(
        self,
        name: typing.Union[
            typing_extensions.Literal["someProp"],
            typing_extensions.Literal["someprop"],
            str
        ]
    ):
        return super().get_item_(name)

    def __new__(
        cls,
        *args_: typing.Union[dict, frozendict.frozendict, ],
        someProp: typing.Union[Schema_.Properties.SomeProp, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        someprop: typing.Union[Schema_.Properties.Someprop, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        configuration_: typing.Optional[schemas.configuration_module.Configuration] = None,
        **kwargs: typing.Union[dict, frozendict.frozendict, list, tuple, decimal.Decimal, float, int, str, datetime.date, datetime.datetime, uuid.UUID, bool, None, bytes, io.FileIO, io.BufferedReader, schemas.Schema],
    ) -> 'ObjectWithCollidingProperties':
        return super().__new__(
            cls,
            *args_,
            someProp=someProp,
            someprop=someprop,
            configuration_=configuration_,
            **kwargs,
        )
