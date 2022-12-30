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


class Drawing(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class Schema_:
        
        class Properties:
        
            @staticmethod
            def main_shape() -> typing.Type['shape.Shape']:
                return shape.Shape
        
            @staticmethod
            def shape_or_null() -> typing.Type['shape_or_null.ShapeOrNull']:
                return shape_or_null.ShapeOrNull
        
            @staticmethod
            def nullable_shape() -> typing.Type['nullable_shape.NullableShape']:
                return nullable_shape.NullableShape
            
            
            class Shapes(
                schemas.ListSchema
            ):
            
            
                class Schema_:
                    types = {tuple}
                    
                    @staticmethod
                    def items() -> typing.Type['shape.Shape']:
                        return shape.Shape
            
                def __new__(
                    cls,
                    arg_: typing.Union[typing.Tuple['shape.Shape'], typing.List['shape.Shape']],
                    configuration_: typing.Optional[schemas.configuration_module.Configuration] = None,
                ) -> 'Shapes':
                    return super().__new__(
                        cls,
                        arg_,
                        configuration_=configuration_,
                    )
            
                def __getitem__(self, i: int) -> 'shape.Shape':
                    return super().__getitem__(i)
            __annotations__ = {
                "mainShape": main_shape,
                "shapeOrNull": shape_or_null,
                "nullableShape": nullable_shape,
                "shapes": Shapes,
            }
        
        @staticmethod
        def additional_properties() -> typing.Type['fruit.Fruit']:
            return fruit.Fruit
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mainShape"]) -> 'shape.Shape': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["shapeOrNull"]) -> 'shape_or_null.ShapeOrNull': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nullableShape"]) -> 'nullable_shape.NullableShape': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["shapes"]) -> Schema_.Properties.Shapes: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> 'fruit.Fruit': ...
    
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal["mainShape"],
            typing_extensions.Literal["shapeOrNull"],
            typing_extensions.Literal["nullableShape"],
            typing_extensions.Literal["shapes"],
            str
        ]
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_(self, name: typing_extensions.Literal["mainShape"]) -> typing.Union['shape.Shape', schemas.Unset]: ...
    
    @typing.overload
    def get_item_(self, name: typing_extensions.Literal["shapeOrNull"]) -> typing.Union['shape_or_null.ShapeOrNull', schemas.Unset]: ...
    
    @typing.overload
    def get_item_(self, name: typing_extensions.Literal["nullableShape"]) -> typing.Union['nullable_shape.NullableShape', schemas.Unset]: ...
    
    @typing.overload
    def get_item_(self, name: typing_extensions.Literal["shapes"]) -> typing.Union[Schema_.Properties.Shapes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_(self, name: str) -> typing.Union['fruit.Fruit', schemas.Unset]: ...
    
    def get_item_(
        self,
        name: typing.Union[
            typing_extensions.Literal["mainShape"],
            typing_extensions.Literal["shapeOrNull"],
            typing_extensions.Literal["nullableShape"],
            typing_extensions.Literal["shapes"],
            str
        ]
    ):
        return super().get_item_(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        mainShape: typing.Union['shape.Shape', schemas.Unset] = schemas.unset,
        shapeOrNull: typing.Union['shape_or_null.ShapeOrNull', schemas.Unset] = schemas.unset,
        nullableShape: typing.Union['nullable_shape.NullableShape', schemas.Unset] = schemas.unset,
        shapes: typing.Union[Schema_.Properties.Shapes, list, tuple, schemas.Unset] = schemas.unset,
        configuration_: typing.Optional[schemas.configuration_module.Configuration] = None,
        **kwargs: 'fruit.Fruit',
    ) -> 'Drawing':
        return super().__new__(
            cls,
            *_args,
            mainShape=mainShape,
            shapeOrNull=shapeOrNull,
            nullableShape=nullableShape,
            shapes=shapes,
            configuration_=configuration_,
            **kwargs,
        )

from petstore_api.components.schema import fruit
from petstore_api.components.schema import nullable_shape
from petstore_api.components.schema import shape
from petstore_api.components.schema import shape_or_null
