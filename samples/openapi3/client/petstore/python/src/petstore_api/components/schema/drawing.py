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


class (
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """


    class Schema_:
        types = {frozendict.frozendict}
        
        class Properties:
        
            @staticmethod
            def () -> typing.Type['shape.Shape']:
                return shape.Shape
        
            @staticmethod
            def () -> typing.Type['shape_or_null.ShapeOrNull']:
                return shape_or_null.ShapeOrNull
        
            @staticmethod
            def () -> typing.Type['nullable_shape.NullableShape']:
                return nullable_shape.NullableShape
            
            
            class (
                schemas.ListSchema
            ):
            
            
                class Schema_:
                    types = {tuple}
                    
                    @staticmethod
                    def () -> typing.Type['shape.Shape']:
                        return shape.Shape
            
                def __new__(
                    cls,
                    arg_: typing.Union[typing.Tuple['shape.Shape'], typing.List['shape.Shape']],
                    configuration_: typing.Optional[schemas.configuration_module.Configuration] = None,
                ) -> '':
                    return super().__new__(
                        cls,
                        arg_,
                        configuration_=configuration_,
                    )
            
                def __getitem__(self, i: int) -> 'shape.Shape':
                    return super().__getitem__(i)
            __annotations__ = {
                "": ,
                "": ,
                "": ,
                "": ,
            }
        
        @staticmethod
        def () -> typing.Type['fruit.Fruit']:
            return fruit.Fruit
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal[""]) -> 'shape.Shape': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal[""]) -> 'shape_or_null.ShapeOrNull': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal[""]) -> 'nullable_shape.NullableShape': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal[""]) -> Schema_.Properties.: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> 'fruit.Fruit': ...
    
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal[""],
            typing_extensions.Literal[""],
            typing_extensions.Literal[""],
            typing_extensions.Literal[""],
            str
        ]
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_(self, name: typing_extensions.Literal[""]) -> typing.Union['shape.Shape', schemas.Unset]: ...
    
    @typing.overload
    def get_item_(self, name: typing_extensions.Literal[""]) -> typing.Union['shape_or_null.ShapeOrNull', schemas.Unset]: ...
    
    @typing.overload
    def get_item_(self, name: typing_extensions.Literal[""]) -> typing.Union['nullable_shape.NullableShape', schemas.Unset]: ...
    
    @typing.overload
    def get_item_(self, name: typing_extensions.Literal[""]) -> typing.Union[Schema_.Properties., schemas.Unset]: ...
    
    @typing.overload
    def get_item_(self, name: str) -> typing.Union['fruit.Fruit', schemas.Unset]: ...
    
    def get_item_(
        self,
        name: typing.Union[
            typing_extensions.Literal[""],
            typing_extensions.Literal[""],
            typing_extensions.Literal[""],
            typing_extensions.Literal[""],
            str
        ]
    ):
        return super().get_item_(name)

    def __new__(
        cls,
        *args_: typing.Union[dict, frozendict.frozendict, ],
        configuration_: typing.Optional[schemas.configuration_module.Configuration] = None,
        **kwargs: 'fruit.Fruit',
    ) -> '':
        return super().__new__(
            cls,
            *args_,
            configuration_=configuration_,
            **kwargs,
        )

from petstore_api.components.schema import fruit
from petstore_api.components.schema import nullable_shape
from petstore_api.components.schema import shape
from petstore_api.components.schema import shape_or_null
