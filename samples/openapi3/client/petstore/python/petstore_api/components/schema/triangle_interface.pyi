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


class TriangleInterface(
    schemas.AnyTypeSchema,
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        # any type
        required = {
            "shapeType",
            "triangleType",
        }
        
        class Properties:
            
            
            class ShapeType(
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def TRIANGLE(cls):
                    return cls("Triangle")
            TriangleType = schemas.StrSchema
            __annotations__ = {
                "shapeType": ShapeType,
                "triangleType": TriangleType,
            }

    
    shapeType: MetaOapg.Properties.ShapeType
    triangleType: MetaOapg.Properties.TriangleType
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["shapeType"]) -> MetaOapg.Properties.ShapeType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["triangleType"]) -> MetaOapg.Properties.TriangleType: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal["shapeType"],
            typing_extensions.Literal["triangleType"],
            str
        ]
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["shapeType"]) -> MetaOapg.Properties.ShapeType: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["triangleType"]) -> MetaOapg.Properties.TriangleType: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(
        self,
        name: typing.Union[
            typing_extensions.Literal["shapeType"],
            typing_extensions.Literal["triangleType"],
            str
        ]
    ):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, str, datetime.date, datetime.datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        shapeType: typing.Union[MetaOapg.Properties.ShapeType, str, ],
        triangleType: typing.Union[MetaOapg.Properties.TriangleType, str, ],
        _configuration: typing.Optional[schemas.configuration_module.Configuration] = None,
        **kwargs: typing.Union[dict, frozendict.frozendict, list, tuple, decimal.Decimal, float, int, str, datetime.date, datetime.datetime, uuid.UUID, bool, None, bytes, io.FileIO, io.BufferedReader, schemas.Schema],
    ) -> 'TriangleInterface':
        return super().__new__(
            cls,
            *_args,
            shapeType=shapeType,
            triangleType=triangleType,
            _configuration=_configuration,
            **kwargs,
        )
