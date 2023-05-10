# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *


class Schema(
    schemas.DictSchema[schemas.T]
):


    class Schema_:
        types = {frozendict.frozendict}
        
        class Properties:
            
            
            class EnumFormStringArray(
                schemas.ListSchema[schemas.T]
            ):
            
            
                class Schema_:
                    types = {tuple}
                    
                    
                    class Items(
                        schemas.StrSchema[schemas.T]
                    ):
                    
                    
                        class Schema_:
                            types = {
                                str,
                            }
                            default = "$"
                            enum_value_to_name = {
                                ">": "GREATER_THAN_SIGN",
                                "$": "DOLLAR_SIGN",
                            }
                        
                        @schemas.classproperty
                        def GREATER_THAN_SIGN(cls):
                            return cls(">")
                        
                        @schemas.classproperty
                        def DOLLAR_SIGN(cls):
                            return cls("$")
            
                def __new__(
                    cls,
                    arg_: typing.Union[
                        typing.Tuple[
                            typing.Union[Schema_.Items, str], ...
                        ],
                        typing.List[
                            typing.Union[Schema_.Items, str]
                        ],
                    ],
                    configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
                ) -> Schema.Schema_.Properties.EnumFormStringArray[tuple]:
                    return super().__new__(
                        cls,
                        arg_,
                        configuration_=configuration_,
                    )
            
                def __getitem__(self, name: int) -> Schema_.Items[str]:
                    return super().__getitem__(name)
            
            
            class EnumFormString(
                schemas.StrSchema[schemas.T]
            ):
            
            
                class Schema_:
                    types = {
                        str,
                    }
                    default = "-efg"
                    enum_value_to_name = {
                        "_abc": "_ABC",
                        "-efg": "HYPHEN_MINUS_EFG",
                        "(xyz)": "LEFT_PARENTHESIS_XYZ_RIGHT_PARENTHESIS",
                    }
                
                @schemas.classproperty
                def _ABC(cls):
                    return cls("_abc")
                
                @schemas.classproperty
                def HYPHEN_MINUS_EFG(cls):
                    return cls("-efg")
                
                @schemas.classproperty
                def LEFT_PARENTHESIS_XYZ_RIGHT_PARENTHESIS(cls):
                    return cls("(xyz)")
            __annotations__ = {
                "enum_form_string_array": EnumFormStringArray,
                "enum_form_string": EnumFormString,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enum_form_string_array"]) -> Schema_.Properties.EnumFormStringArray[tuple]: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enum_form_string"]) -> Schema_.Properties.EnumFormString[str]: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema[typing.Union[
        frozendict.frozendict,
        str,
        decimal.Decimal,
        schemas.BoolClass,
        schemas.NoneClass,
        tuple,
        bytes,
        schemas.FileIO
    ]]: ...
    
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

    def __new__(
        cls,
        *args_: typing.Union[dict, frozendict.frozendict],
        enum_form_string_array: typing.Union[Schema_.Properties.EnumFormStringArray, list, tuple, schemas.Unset] = schemas.unset,
        enum_form_string: typing.Union[Schema_.Properties.EnumFormString, str, schemas.Unset] = schemas.unset,
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
        **kwargs: typing.Union[dict, frozendict.frozendict, list, tuple, decimal.Decimal, float, int, str, datetime.date, datetime.datetime, uuid.UUID, bool, None, bytes, io.FileIO, io.BufferedReader, schemas.Schema],
    ) -> Schema[frozendict.frozendict]:
        return super().__new__(
            cls,
            *args_,
            enum_form_string_array=enum_form_string_array,
            enum_form_string=enum_form_string,
            configuration_=configuration_,
            **kwargs,
        )
