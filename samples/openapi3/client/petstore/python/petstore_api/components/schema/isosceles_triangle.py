# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from petstore_api import schemas  # noqa: F401


class IsoscelesTriangle(
    schemas.AnyTypeSchema,
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        # any type
        
        class AllOf:
        
            @staticmethod
            def all_of_0() -> typing.Type['triangle_interface.TriangleInterface']:
                return triangle_interface.TriangleInterface
            
            
            class AllOf1(
                schemas.DictSchema
            ):
                """NOTE: This class is auto generated by OpenAPI Generator.
                Ref: https://openapi-generator.tech
            
                Do not edit the class manually.
                """
            
            
                class MetaOapg:
                    types = {frozendict.frozendict}
                    
                    class Properties:
                        
                        
                        class TriangleType(
                            schemas.StrSchema
                        ):
                            """NOTE: This class is auto generated by OpenAPI Generator.
                            Ref: https://openapi-generator.tech
                        
                            Do not edit the class manually.
                            """
                        
                        
                            class MetaOapg:
                                types = {
                                    str,
                                }
                                enum_value_to_name = {
                                    "IsoscelesTriangle": "ISOSCELES_TRIANGLE",
                                }
                            
                            @schemas.classproperty
                            def ISOSCELES_TRIANGLE(cls):
                                return cls("IsoscelesTriangle")
                        __annotations__ = {
                            "triangleType": TriangleType,
                        }
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["triangleType"]) -> MetaOapg.Properties.TriangleType: ...
                
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
                def get_item_oapg(self, name: typing_extensions.Literal["triangleType"]) -> typing.Union[MetaOapg.Properties.TriangleType, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(
                    self,
                    name: typing.Union[
                        typing_extensions.Literal["triangleType"],
                        str
                    ]
                ):
                    return super().get_item_oapg(name)
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    triangleType: typing.Union[MetaOapg.Properties.TriangleType, str, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'AllOf1':
                    return super().__new__(
                        cls,
                        *_args,
                        triangleType=triangleType,
                        _configuration=_configuration,
                        **kwargs,
                    )
            classes = [
                all_of_0,
                AllOf1,
            ]


    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'IsoscelesTriangle':
        return super().__new__(
            cls,
            *_args,
            _configuration=_configuration,
            **kwargs,
        )

from petstore_api.components.schema import triangle_interface
