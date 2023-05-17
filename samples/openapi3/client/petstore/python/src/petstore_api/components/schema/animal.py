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


class Animal(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """


    class Schema_:
        types = {frozendict.frozendict}
        required = {
            "className",
        }
        
        @staticmethod
        def discriminator():
            return {
                'className': {
                    'Cat': cat.Cat,
                    'Dog': dog.Dog,
                }
            }
        
        class Properties:
            ClassName = schemas.StrSchema
            
            
            class Color(
                schemas.StrSchema
            ):
            
            
                class Schema_:
                    types = {
                        str,
                    }
                    default = "red"
            __annotations__ = {
                "className": ClassName,
                "color": Color,
            }
    
    def className(self) -> Schema_.Properties.ClassName:
        return self.__getitem__("className")
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["className"]) -> Schema_.Properties.ClassName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["color"]) -> Schema_.Properties.Color: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal["className"],
            typing_extensions.Literal["color"],
            str
        ]
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_(self, name: typing_extensions.Literal["className"]) -> Schema_.Properties.ClassName: ...
    
    @typing.overload
    def get_item_(self, name: typing_extensions.Literal["color"]) -> typing.Union[Schema_.Properties.Color, schemas.Unset]: ...
    
    @typing.overload
    def get_item_(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_(
        self,
        name: typing.Union[
            typing_extensions.Literal["className"],
            typing_extensions.Literal["color"],
            str
        ]
    ):
        return super().get_item_(name)

    def __new__(
        cls,
        *args_: typing.Union[dict, frozendict.frozendict],
        className: typing.Union[Schema_.Properties.ClassName, str],
        color: typing.Union[Schema_.Properties.Color, str, schemas.Unset] = schemas.unset,
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
        **kwargs: typing.Union[dict, frozendict.frozendict, list, tuple, decimal.Decimal, float, int, str, datetime.date, datetime.datetime, uuid.UUID, bool, None, bytes, io.FileIO, io.BufferedReader, schemas.Schema],
    ) -> 'Animal':
        return super().__new__(
            cls,
            *args_,
            className=className,
            color=color,
            configuration_=configuration_,
            **kwargs,
        )

from petstore_api.components.schema import cat
from petstore_api.components.schema import dog
