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


class EnumArrays(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """


    class Schema_:
        types = {frozendict.frozendict}
        
        class Properties:
            
            
            class JustSymbol(
                schemas.StrSchema
            ):
            
            
                class Schema_:
                    types = {
                        str,
                    }
                    enum_value_to_name = {
                        ">=": "GREATER_THAN_EQUALS",
                        "$": "DOLLAR",
                    }                
                @schemas.classproperty
                def GREATER_THAN_EQUALS(cls):
                    return cls(">=")
                
                @schemas.classproperty
                def DOLLAR(cls):
                    return cls("$")
            
            
            class ArrayEnum(
                schemas.ListSchema
            ):
            
            
                class Schema_:
                    types = {tuple}
                    
                    
                    class Items(
                        schemas.StrSchema
                    ):
                    
                    
                        class Schema_:
                            types = {
                                str,
                            }
                            enum_value_to_name = {
                                "fish": "FISH",
                                "crab": "CRAB",
                            }                        
                        @schemas.classproperty
                        def FISH(cls):
                            return cls("fish")
                        
                        @schemas.classproperty
                        def CRAB(cls):
                            return cls("crab")
            
                def __new__(
                    cls,
                    arg_: typing.Union[typing.Tuple[typing.Union[Schema_.Items, str, ]], typing.List[typing.Union[Schema_.Items, str, ]]],
                    configuration_: typing.Optional[schemas.configuration_module.Configuration] = None,
                ) -> 'ArrayEnum':
                    return super().__new__(
                        cls,
                        arg_,
                        configuration_=configuration_,
                    )
            
                def __getitem__(self, i: int) -> Schema_.Items:
                    return super().__getitem__(i)
            __annotations__ = {
                "just_symbol": JustSymbol,
                "array_enum": ArrayEnum,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["just_symbol"]) -> Schema_.Properties.JustSymbol: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["array_enum"]) -> Schema_.Properties.ArrayEnum: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal["just_symbol"],
            typing_extensions.Literal["array_enum"],
            str
        ]
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_(self, name: typing_extensions.Literal["just_symbol"]) -> typing.Union[Schema_.Properties.JustSymbol, schemas.Unset]: ...
    
    @typing.overload
    def get_item_(self, name: typing_extensions.Literal["array_enum"]) -> typing.Union[Schema_.Properties.ArrayEnum, schemas.Unset]: ...
    
    @typing.overload
    def get_item_(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_(
        self,
        name: typing.Union[
            typing_extensions.Literal["just_symbol"],
            typing_extensions.Literal["array_enum"],
            str
        ]
    ):
        return super().get_item_(name)

    def __new__(
        cls,
        *args_: typing.Union[dict, frozendict.frozendict, ],
        just_symbol: typing.Union[Schema_.Properties.JustSymbol, str, schemas.Unset] = schemas.unset,
        array_enum: typing.Union[Schema_.Properties.ArrayEnum, list, tuple, schemas.Unset] = schemas.unset,
        configuration_: typing.Optional[schemas.configuration_module.Configuration] = None,
        **kwargs: typing.Union[dict, frozendict.frozendict, list, tuple, decimal.Decimal, float, int, str, datetime.date, datetime.datetime, uuid.UUID, bool, None, bytes, io.FileIO, io.BufferedReader, schemas.Schema],
    ) -> 'EnumArrays':
        return super().__new__(
            cls,
            *args_,
            just_symbol=just_symbol,
            array_enum=array_enum,
            configuration_=configuration_,
            **kwargs,
        )
