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


class ComplexQuadrilateral(
    schemas.AnyTypeSchema,
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """


    class Schema_:
        # any type
        
        class AllOf:
        
            @staticmethod
            def _0() -> typing.Type['quadrilateral_interface.QuadrilateralInterface']:
                return quadrilateral_interface.QuadrilateralInterface
            
            
            class _1(
                schemas.DictSchema
            ):
            
            
                class Schema_:
                    
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
                def __getitem__(self, name: typing_extensions.Literal["quadrilateralType"]) -> Schema_.Properties.QuadrilateralType: ...
                
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
                def get_item_(self, name: typing_extensions.Literal["quadrilateralType"]) -> typing.Union[Schema_.Properties.QuadrilateralType, schemas.Unset]: ...
                
                @typing.overload
                def get_item_(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_(
                    self,
                    name: typing.Union[
                        typing_extensions.Literal["quadrilateralType"],
                        str
                    ]
                ):
                    return super().get_item_(name)
            
                def __new__(
                    cls,
                    *args_: typing.Union[dict, frozendict.frozendict, ],
                    quadrilateralType: typing.Union[Schema_.Properties.QuadrilateralType, str, schemas.Unset] = schemas.unset,
                    configuration_: typing.Optional[schemas.configuration_module.Configuration] = None,
                    **kwargs: typing.Union[dict, frozendict.frozendict, list, tuple, decimal.Decimal, float, int, str, datetime.date, datetime.datetime, uuid.UUID, bool, None, bytes, io.FileIO, io.BufferedReader, schemas.Schema],
                ) -> '_1':
                    return super().__new__(
                        cls,
                        *args_,
                        quadrilateralType=quadrilateralType,
                        configuration_=configuration_,
                        **kwargs,
                    )
            classes = [
                _0,
                _1,
            ]


    def __new__(
        cls,
        *args_: typing.Union[dict, frozendict.frozendict, str, datetime.date, datetime.datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        configuration_: typing.Optional[schemas.configuration_module.Configuration] = None,
        **kwargs: typing.Union[dict, frozendict.frozendict, list, tuple, decimal.Decimal, float, int, str, datetime.date, datetime.datetime, uuid.UUID, bool, None, bytes, io.FileIO, io.BufferedReader, schemas.Schema],
    ) -> 'ComplexQuadrilateral':
        return super().__new__(
            cls,
            *args_,
            configuration_=configuration_,
            **kwargs,
        )

from petstore_api.components.schema import quadrilateral_interface
