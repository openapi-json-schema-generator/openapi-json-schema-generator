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


class ComplexQuadrilateral(
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
            def all_of0() -> typing.Type['quadrilateral_interface.QuadrilateralInterface']:
                return quadrilateral_interface.QuadrilateralInterface
            
            
            class AllOf1(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    class Properties:
                        
                        
                        class QuadrilateralType(
                            schemas.StrSchema
                        ):
                            
                            @schemas.classproperty
                            def COMPLEX_QUADRILATERAL(cls):
                                return cls("ComplexQuadrilateral")
                        __annotations__ = {
                            "quadrilateralType": QuadrilateralType,
                        }
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["quadrilateralType"]) -> MetaOapg.Properties.QuadrilateralType: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(
                    self,
                    name: typing.Union[
                        typing_extensions.Literal["quadrilateralType"],
                        str
                    ]
                ):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["quadrilateralType"]) -> typing.Union[MetaOapg.Properties.QuadrilateralType, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(
                    self,
                    name: typing.Union[
                        typing_extensions.Literal["quadrilateralType"],
                        str
                    ]
                ):
                    return super().get_item_oapg(name)
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    quadrilateralType: typing.Union[MetaOapg.Properties.QuadrilateralType, str, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.configuration_module.Configuration] = None,
                    **kwargs: typing.Union[dict, frozendict.frozendict, list, tuple, decimal.Decimal, float, int, str, datetime.date, datetime.datetime, uuid.UUID, bool, None, bytes, io.FileIO, io.BufferedReader, schemas.Schema],
                ) -> 'AllOf1':
                    return super().__new__(
                        cls,
                        *_args,
                        quadrilateralType=quadrilateralType,
                        _configuration=_configuration,
                        **kwargs,
                    )
            classes = [
                all_of0,
                AllOf1,
            ]


    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, str, datetime.date, datetime.datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        _configuration: typing.Optional[schemas.configuration_module.Configuration] = None,
        **kwargs: typing.Union[dict, frozendict.frozendict, list, tuple, decimal.Decimal, float, int, str, datetime.date, datetime.datetime, uuid.UUID, bool, None, bytes, io.FileIO, io.BufferedReader, schemas.Schema],
    ) -> 'ComplexQuadrilateral':
        return super().__new__(
            cls,
            *_args,
            _configuration=_configuration,
            **kwargs,
        )

from petstore_api.components.schema import quadrilateral_interface
