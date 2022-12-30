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


class ScaleneTriangle(
    schemas.AnyTypeSchema,
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class Schema_:
        # any type
        
        class AllOf:
        
            @staticmethod
            def all_of0() -> typing.Type['triangle_interface.TriangleInterface']:
                return triangle_interface.TriangleInterface
            
            
            class AllOf1(
                schemas.DictSchema
            ):
            
            
                class Schema_:
                    
                    class Properties:
                        
                        
                        class TriangleType(
                            schemas.StrSchema
                        ):
                            
                            @schemas.classproperty
                            def SCALENE_TRIANGLE(cls):
                                return cls("ScaleneTriangle")
                        __annotations__ = {
                            "triangleType": TriangleType,
                        }
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["triangleType"]) -> Schema_.Properties.TriangleType: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(
                    self,
                    name: typing.Union[
                        typing_extensions.Literal["triangleType"],
                        str
                    ]
                ):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                @typing.overload
                def get_item_(self, name: typing_extensions.Literal["triangleType"]) -> typing.Union[Schema_.Properties.TriangleType, schemas.Unset]: ...
                
                @typing.overload
                def get_item_(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_(
                    self,
                    name: typing.Union[
                        typing_extensions.Literal["triangleType"],
                        str
                    ]
                ):
                    return super().get_item_(name)
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    triangleType: typing.Union[Schema_.Properties.TriangleType, str, schemas.Unset] = schemas.unset,
                    configuration_: typing.Optional[schemas.configuration_module.Configuration] = None,
                    **kwargs: typing.Union[dict, frozendict.frozendict, list, tuple, decimal.Decimal, float, int, str, datetime.date, datetime.datetime, uuid.UUID, bool, None, bytes, io.FileIO, io.BufferedReader, schemas.Schema],
                ) -> 'AllOf1':
                    return super().__new__(
                        cls,
                        *_args,
                        triangleType=triangleType,
                        configuration_=configuration_,
                        **kwargs,
                    )
            classes = [
                all_of0,
                AllOf1,
            ]


    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, str, datetime.date, datetime.datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        configuration_: typing.Optional[schemas.configuration_module.Configuration] = None,
        **kwargs: typing.Union[dict, frozendict.frozendict, list, tuple, decimal.Decimal, float, int, str, datetime.date, datetime.datetime, uuid.UUID, bool, None, bytes, io.FileIO, io.BufferedReader, schemas.Schema],
    ) -> 'ScaleneTriangle':
        return super().__new__(
            cls,
            *_args,
            configuration_=configuration_,
            **kwargs,
        )

from petstore_api.components.schema import triangle_interface
