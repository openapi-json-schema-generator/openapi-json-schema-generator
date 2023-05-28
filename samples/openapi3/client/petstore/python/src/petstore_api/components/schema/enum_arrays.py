# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *


class EnumArrays(
    schemas.DictSchema[schemas.T]
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """


    class Schema_:
        types = {frozendict.frozendict}
        
        class Properties:
            
            
            class JustSymbol(
                schemas.StrSchema[schemas.T]
            ):
            
            
                class Schema_:
                    types = {
                        str,
                    }
                    enum_value_to_name = {
                        ">=": "GREATER_THAN_SIGN_EQUALS_SIGN",
                        "$": "DOLLAR_SIGN",
                    }
                
                @schemas.classproperty
                def GREATER_THAN_SIGN_EQUALS_SIGN(cls):
                    return cls(">=") # type: ignore
                
                @schemas.classproperty
                def DOLLAR_SIGN(cls):
                    return cls("$") # type: ignore
            
            
            class ArrayEnum(
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
                            enum_value_to_name = {
                                "fish": "FISH",
                                "crab": "CRAB",
                            }
                        
                        @schemas.classproperty
                        def FISH(cls):
                            return cls("fish") # type: ignore
                        
                        @schemas.classproperty
                        def CRAB(cls):
                            return cls("crab") # type: ignore
            
                def __new__(
                    cls,
                    arg_: typing.Sequence[
                        typing.Union[
                            Schema_.Items[str],
                            str
                        ]
                    ],
                    configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
                ) -> EnumArrays.Schema_.Properties.ArrayEnum[tuple]:
                    inst = super().__new__(
                        cls,
                        arg_,
                        configuration_=configuration_,
                    )
                    inst = typing.cast(
                        EnumArrays.Schema_.Properties.ArrayEnum[tuple],
                        inst
                    )
                    return inst
            
                def __getitem__(self, name: int) -> Schema_.Items[str]:
                    return super().__getitem__(name)
            __annotations__ = {
                "just_symbol": JustSymbol,
                "array_enum": ArrayEnum,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["just_symbol"]) -> Schema_.Properties.JustSymbol[str]: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["array_enum"]) -> Schema_.Properties.ArrayEnum[tuple]: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.AnyTypeSchema[typing.Union[
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
            typing_extensions.Literal["just_symbol"],
            typing_extensions.Literal["array_enum"],
            str
        ]
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    def __new__(
        cls,
        *args_: typing.Union[dict, frozendict.frozendict],
        just_symbol: typing.Union[
            Schema_.Properties.JustSymbol[str],
            schemas.Unset,
            str
        ] = schemas.unset,
        array_enum: typing.Union[
            Schema_.Properties.ArrayEnum[tuple],
            schemas.Unset,
            list,
            tuple
        ] = schemas.unset,
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
        **kwargs: typing.Union[dict, frozendict.frozendict, list, tuple, decimal.Decimal, float, int, str, datetime.date, datetime.datetime, uuid.UUID, bool, None, bytes, io.FileIO, io.BufferedReader, schemas.Schema],
    ) -> EnumArrays[frozendict.frozendict]:
        inst = super().__new__(
            cls,
            *args_,
            just_symbol=just_symbol,
            array_enum=array_enum,
            configuration_=configuration_,
            **kwargs,
        )
        inst = typing.cast(
            EnumArrays[frozendict.frozendict],
            inst
        )
        return inst
