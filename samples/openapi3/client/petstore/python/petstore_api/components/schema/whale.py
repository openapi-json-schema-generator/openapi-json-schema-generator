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


class Whale(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class Schema_:
        types = {frozendict.frozendict}
        required = {
            "className",
        }
        
        class Properties:
            HasBaleen = schemas.BoolSchema
            HasTeeth = schemas.BoolSchema
            
            
            class ClassName(
                schemas.StrSchema
            ):
            
            
                class Schema_:
                    types = {
                        str,
                    }
                    enum_value_to_name = {
                        "whale": "WHALE",
                    }
                
                @schemas.classproperty
                def WHALE(cls):
                    return cls("whale")
            __annotations__ = {
                "hasBaleen": HasBaleen,
                "hasTeeth": HasTeeth,
                "className": ClassName,
            }
    
    className: Schema_.Properties.ClassName
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["className"]) -> Schema_.Properties.ClassName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hasBaleen"]) -> Schema_.Properties.HasBaleen: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hasTeeth"]) -> Schema_.Properties.HasTeeth: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal["className"],
            typing_extensions.Literal["hasBaleen"],
            typing_extensions.Literal["hasTeeth"],
            str
        ]
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_(self, name: typing_extensions.Literal["className"]) -> Schema_.Properties.ClassName: ...
    
    @typing.overload
    def get_item_(self, name: typing_extensions.Literal["hasBaleen"]) -> typing.Union[Schema_.Properties.HasBaleen, schemas.Unset]: ...
    
    @typing.overload
    def get_item_(self, name: typing_extensions.Literal["hasTeeth"]) -> typing.Union[Schema_.Properties.HasTeeth, schemas.Unset]: ...
    
    @typing.overload
    def get_item_(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_(
        self,
        name: typing.Union[
            typing_extensions.Literal["className"],
            typing_extensions.Literal["hasBaleen"],
            typing_extensions.Literal["hasTeeth"],
            str
        ]
    ):
        return super().get_item_(name)

    def __new__(
        cls,
        *args_: typing.Union[dict, frozendict.frozendict, ],
        className: typing.Union[Schema_.Properties.ClassName, str, ],
        hasBaleen: typing.Union[Schema_.Properties.HasBaleen, bool, schemas.Unset] = schemas.unset,
        hasTeeth: typing.Union[Schema_.Properties.HasTeeth, bool, schemas.Unset] = schemas.unset,
        configuration_: typing.Optional[schemas.configuration_module.Configuration] = None,
        **kwargs: typing.Union[dict, frozendict.frozendict, list, tuple, decimal.Decimal, float, int, str, datetime.date, datetime.datetime, uuid.UUID, bool, None, bytes, io.FileIO, io.BufferedReader, schemas.Schema],
    ) -> 'Whale':
        return super().__new__(
            cls,
            *args_,
            className=className,
            hasBaleen=hasBaleen,
            hasTeeth=hasTeeth,
            configuration_=configuration_,
            **kwargs,
        )
