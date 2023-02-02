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


class Schema(
    schemas.DictSchema
):


    class Schema_:
        types = {frozendict.frozendict}
        
        class Properties:
            
            
            class EnumFormStringArray(
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
                                ">": "GREATER_THAN",
                                "$": "DOLLAR",
                            }
                        
                        @schemas.classproperty
                        def GREATER_THAN(cls):
                            return cls(">")
                        
                        @schemas.classproperty
                        def DOLLAR(cls):
                            return cls("$")
            
                def __new__(
                    cls,
                    arg_: typing.Union[typing.Tuple[typing.Union[Schema_.Items, str, ]], typing.List[typing.Union[Schema_.Items, str, ]]],
                    configuration_: typing.Optional[schemas.configuration_module.Configuration] = None,
                ) -> 'EnumFormStringArray':
                    return super().__new__(
                        cls,
                        arg_,
                        configuration_=configuration_,
                    )
            
                def __getitem__(self, i: int) -> Schema_.Items:
                    return super().__getitem__(i)
            
            
            class EnumFormString(
                schemas.StrSchema
            ):
            
            
                class Schema_:
                    types = {
                        str,
                    }
                    enum_value_to_name = {
                        "-efg": "EFG",
                        "(xyz)": "XYZ",
                        "_abc": "_ABC",
                    }
                
                @schemas.classproperty
                def EFG(cls):
                    return cls("-efg")
                
                @schemas.classproperty
                def XYZ(cls):
                    return cls("(xyz)")
                
                @schemas.classproperty
                def _ABC(cls):
                    return cls("_abc")
            __annotations__ = {
                "enum_form_string_array": EnumFormStringArray,
                "enum_form_string": EnumFormString,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enum_form_string_array"]) -> Schema_.Properties.EnumFormStringArray: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enum_form_string"]) -> Schema_.Properties.EnumFormString: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal["enum_form_string_array"],
            typing_extensions.Literal["enum_form_string"],
            str
        ]
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_(self, name: typing_extensions.Literal["enum_form_string_array"]) -> typing.Union[Schema_.Properties.EnumFormStringArray, schemas.Unset]: ...
    
    @typing.overload
    def get_item_(self, name: typing_extensions.Literal["enum_form_string"]) -> typing.Union[Schema_.Properties.EnumFormString, schemas.Unset]: ...
    
    @typing.overload
    def get_item_(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_(
        self,
        name: typing.Union[
            typing_extensions.Literal["enum_form_string_array"],
            typing_extensions.Literal["enum_form_string"],
            str
        ]
    ):
        return super().get_item_(name)

    def __new__(
        cls,
        *args_: typing.Union[dict, frozendict.frozendict, ],
        enum_form_string_array: typing.Union[Schema_.Properties.EnumFormStringArray, list, tuple, schemas.Unset] = schemas.unset,
        enum_form_string: typing.Union[Schema_.Properties.EnumFormString, str, schemas.Unset] = schemas.unset,
        configuration_: typing.Optional[schemas.configuration_module.Configuration] = None,
        **kwargs: typing.Union[dict, frozendict.frozendict, list, tuple, decimal.Decimal, float, int, str, datetime.date, datetime.datetime, uuid.UUID, bool, None, bytes, io.FileIO, io.BufferedReader, schemas.Schema],
    ) -> 'Schema':
        return super().__new__(
            cls,
            *args_,
            enum_form_string_array=enum_form_string_array,
            enum_form_string=enum_form_string,
            configuration_=configuration_,
            **kwargs,
        )
