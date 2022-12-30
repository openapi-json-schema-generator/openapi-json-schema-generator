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


class QuadrilateralInterface(
    schemas.AnyTypeSchema,
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class Schema_:
        # any type
        required = {
            "quadrilateralType",
            "shapeType",
        }
        
        class Properties:
            
            
            class ShapeType(
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def QUADRILATERAL(cls):
                    return cls("Quadrilateral")
            QuadrilateralType = schemas.StrSchema
            __annotations__ = {
                "shapeType": ShapeType,
                "quadrilateralType": QuadrilateralType,
            }

    
    quadrilateralType: Schema_.Properties.QuadrilateralType
    shapeType: Schema_.Properties.ShapeType
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["quadrilateralType"]) -> Schema_.Properties.QuadrilateralType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["shapeType"]) -> Schema_.Properties.ShapeType: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal["quadrilateralType"],
            typing_extensions.Literal["shapeType"],
            str
        ]
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_(self, name: typing_extensions.Literal["quadrilateralType"]) -> Schema_.Properties.QuadrilateralType: ...
    
    @typing.overload
    def get_item_(self, name: typing_extensions.Literal["shapeType"]) -> Schema_.Properties.ShapeType: ...
    
    @typing.overload
    def get_item_(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_(
        self,
        name: typing.Union[
            typing_extensions.Literal["quadrilateralType"],
            typing_extensions.Literal["shapeType"],
            str
        ]
    ):
        return super().get_item_(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, str, datetime.date, datetime.datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        quadrilateralType: typing.Union[Schema_.Properties.QuadrilateralType, str, ],
        shapeType: typing.Union[Schema_.Properties.ShapeType, str, ],
        configuration_: typing.Optional[schemas.configuration_module.Configuration] = None,
        **kwargs: typing.Union[dict, frozendict.frozendict, list, tuple, decimal.Decimal, float, int, str, datetime.date, datetime.datetime, uuid.UUID, bool, None, bytes, io.FileIO, io.BufferedReader, schemas.Schema],
    ) -> 'QuadrilateralInterface':
        return super().__new__(
            cls,
            *_args,
            quadrilateralType=quadrilateralType,
            shapeType=shapeType,
            configuration_=configuration_,
            **kwargs,
        )
