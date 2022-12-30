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


class EnumTest(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class Schema_:
        types = {frozendict.frozendict}
        required = {
            "enum_string_required",
        }
        
        class Properties:
            
            
            class EnumString(
                schemas.StrSchema
            ):
            
            
                class Schema_:
                    types = {
                        str,
                    }
                    enum_value_to_name = {
                        "UPPER": "UPPER",
                        "lower": "LOWER",
                        "": "EMPTY",
                    }
                
                @schemas.classproperty
                def UPPER(cls):
                    return cls("UPPER")
                
                @schemas.classproperty
                def LOWER(cls):
                    return cls("lower")
                
                @schemas.classproperty
                def EMPTY(cls):
                    return cls("")
            
            
            class EnumStringRequired(
                schemas.StrSchema
            ):
            
            
                class Schema_:
                    types = {
                        str,
                    }
                    enum_value_to_name = {
                        "UPPER": "UPPER",
                        "lower": "LOWER",
                        "": "EMPTY",
                    }
                
                @schemas.classproperty
                def UPPER(cls):
                    return cls("UPPER")
                
                @schemas.classproperty
                def LOWER(cls):
                    return cls("lower")
                
                @schemas.classproperty
                def EMPTY(cls):
                    return cls("")
            
            
            class EnumInteger(
                schemas.Int32Schema
            ):
            
            
                class Schema_:
                    types = {
                        decimal.Decimal,
                    }
                    format = 'int32'
                    enum_value_to_name = {
                        1: "POSITIVE_1",
                        -1: "NEGATIVE_1",
                    }
                
                @schemas.classproperty
                def POSITIVE_1(cls):
                    return cls(1)
                
                @schemas.classproperty
                def NEGATIVE_1(cls):
                    return cls(-1)
            
            
            class EnumNumber(
                schemas.Float64Schema
            ):
            
            
                class Schema_:
                    types = {
                        decimal.Decimal,
                    }
                    format = 'double'
                    enum_value_to_name = {
                        1.1: "POSITIVE_1_PT_1",
                        -1.2: "NEGATIVE_1_PT_2",
                    }
                
                @schemas.classproperty
                def POSITIVE_1_PT_1(cls):
                    return cls(1.1)
                
                @schemas.classproperty
                def NEGATIVE_1_PT_2(cls):
                    return cls(-1.2)
        
            @staticmethod
            def string_enum() -> typing.Type['string_enum.StringEnum']:
                return string_enum.StringEnum
        
            @staticmethod
            def integer_enum() -> typing.Type['integer_enum.IntegerEnum']:
                return integer_enum.IntegerEnum
        
            @staticmethod
            def string_enum_with_default_value() -> typing.Type['string_enum_with_default_value.StringEnumWithDefaultValue']:
                return string_enum_with_default_value.StringEnumWithDefaultValue
        
            @staticmethod
            def integer_enum_with_default_value() -> typing.Type['integer_enum_with_default_value.IntegerEnumWithDefaultValue']:
                return integer_enum_with_default_value.IntegerEnumWithDefaultValue
        
            @staticmethod
            def integer_enum_one_value() -> typing.Type['integer_enum_one_value.IntegerEnumOneValue']:
                return integer_enum_one_value.IntegerEnumOneValue
            __annotations__ = {
                "enum_string": EnumString,
                "enum_string_required": EnumStringRequired,
                "enum_integer": EnumInteger,
                "enum_number": EnumNumber,
                "stringEnum": string_enum,
                "IntegerEnum": integer_enum,
                "StringEnumWithDefaultValue": string_enum_with_default_value,
                "IntegerEnumWithDefaultValue": integer_enum_with_default_value,
                "IntegerEnumOneValue": integer_enum_one_value,
            }
    
    enum_string_required: Schema_.Properties.EnumStringRequired
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enum_string_required"]) -> Schema_.Properties.EnumStringRequired: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enum_string"]) -> Schema_.Properties.EnumString: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enum_integer"]) -> Schema_.Properties.EnumInteger: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enum_number"]) -> Schema_.Properties.EnumNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["stringEnum"]) -> 'string_enum.StringEnum': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["IntegerEnum"]) -> 'integer_enum.IntegerEnum': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["StringEnumWithDefaultValue"]) -> 'string_enum_with_default_value.StringEnumWithDefaultValue': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["IntegerEnumWithDefaultValue"]) -> 'integer_enum_with_default_value.IntegerEnumWithDefaultValue': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["IntegerEnumOneValue"]) -> 'integer_enum_one_value.IntegerEnumOneValue': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal["enum_string_required"],
            typing_extensions.Literal["enum_string"],
            typing_extensions.Literal["enum_integer"],
            typing_extensions.Literal["enum_number"],
            typing_extensions.Literal["stringEnum"],
            typing_extensions.Literal["IntegerEnum"],
            typing_extensions.Literal["StringEnumWithDefaultValue"],
            typing_extensions.Literal["IntegerEnumWithDefaultValue"],
            typing_extensions.Literal["IntegerEnumOneValue"],
            str
        ]
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_(self, name: typing_extensions.Literal["enum_string_required"]) -> Schema_.Properties.EnumStringRequired: ...
    
    @typing.overload
    def get_item_(self, name: typing_extensions.Literal["enum_string"]) -> typing.Union[Schema_.Properties.EnumString, schemas.Unset]: ...
    
    @typing.overload
    def get_item_(self, name: typing_extensions.Literal["enum_integer"]) -> typing.Union[Schema_.Properties.EnumInteger, schemas.Unset]: ...
    
    @typing.overload
    def get_item_(self, name: typing_extensions.Literal["enum_number"]) -> typing.Union[Schema_.Properties.EnumNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_(self, name: typing_extensions.Literal["stringEnum"]) -> typing.Union['string_enum.StringEnum', schemas.Unset]: ...
    
    @typing.overload
    def get_item_(self, name: typing_extensions.Literal["IntegerEnum"]) -> typing.Union['integer_enum.IntegerEnum', schemas.Unset]: ...
    
    @typing.overload
    def get_item_(self, name: typing_extensions.Literal["StringEnumWithDefaultValue"]) -> typing.Union['string_enum_with_default_value.StringEnumWithDefaultValue', schemas.Unset]: ...
    
    @typing.overload
    def get_item_(self, name: typing_extensions.Literal["IntegerEnumWithDefaultValue"]) -> typing.Union['integer_enum_with_default_value.IntegerEnumWithDefaultValue', schemas.Unset]: ...
    
    @typing.overload
    def get_item_(self, name: typing_extensions.Literal["IntegerEnumOneValue"]) -> typing.Union['integer_enum_one_value.IntegerEnumOneValue', schemas.Unset]: ...
    
    @typing.overload
    def get_item_(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_(
        self,
        name: typing.Union[
            typing_extensions.Literal["enum_string_required"],
            typing_extensions.Literal["enum_string"],
            typing_extensions.Literal["enum_integer"],
            typing_extensions.Literal["enum_number"],
            typing_extensions.Literal["stringEnum"],
            typing_extensions.Literal["IntegerEnum"],
            typing_extensions.Literal["StringEnumWithDefaultValue"],
            typing_extensions.Literal["IntegerEnumWithDefaultValue"],
            typing_extensions.Literal["IntegerEnumOneValue"],
            str
        ]
    ):
        return super().get_item_(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        enum_string_required: typing.Union[Schema_.Properties.EnumStringRequired, str, ],
        enum_string: typing.Union[Schema_.Properties.EnumString, str, schemas.Unset] = schemas.unset,
        enum_integer: typing.Union[Schema_.Properties.EnumInteger, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        enum_number: typing.Union[Schema_.Properties.EnumNumber, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        stringEnum: typing.Union['string_enum.StringEnum', schemas.Unset] = schemas.unset,
        IntegerEnum: typing.Union['integer_enum.IntegerEnum', schemas.Unset] = schemas.unset,
        StringEnumWithDefaultValue: typing.Union['string_enum_with_default_value.StringEnumWithDefaultValue', schemas.Unset] = schemas.unset,
        IntegerEnumWithDefaultValue: typing.Union['integer_enum_with_default_value.IntegerEnumWithDefaultValue', schemas.Unset] = schemas.unset,
        IntegerEnumOneValue: typing.Union['integer_enum_one_value.IntegerEnumOneValue', schemas.Unset] = schemas.unset,
        configuration_: typing.Optional[schemas.configuration_module.Configuration] = None,
        **kwargs: typing.Union[dict, frozendict.frozendict, list, tuple, decimal.Decimal, float, int, str, datetime.date, datetime.datetime, uuid.UUID, bool, None, bytes, io.FileIO, io.BufferedReader, schemas.Schema],
    ) -> 'EnumTest':
        return super().__new__(
            cls,
            *_args,
            enum_string_required=enum_string_required,
            enum_string=enum_string,
            enum_integer=enum_integer,
            enum_number=enum_number,
            stringEnum=stringEnum,
            IntegerEnum=IntegerEnum,
            StringEnumWithDefaultValue=StringEnumWithDefaultValue,
            IntegerEnumWithDefaultValue=IntegerEnumWithDefaultValue,
            IntegerEnumOneValue=IntegerEnumOneValue,
            configuration_=configuration_,
            **kwargs,
        )

from petstore_api.components.schema import integer_enum
from petstore_api.components.schema import integer_enum_one_value
from petstore_api.components.schema import integer_enum_with_default_value
from petstore_api.components.schema import string_enum
from petstore_api.components.schema import string_enum_with_default_value
