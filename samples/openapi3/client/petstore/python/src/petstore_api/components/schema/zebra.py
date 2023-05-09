# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

import datetime  # noqa: F401
import decimal  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from petstore_api import schemas  # noqa: F401


class Zebra(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """


    class Schema_:
        types = {frozendict.frozendict}
        required = {
            "className",
        }
        
        class Properties:
            
            
            class Type(
                schemas.StrSchema
            ):
            
            
                class Schema_:
                    types = {
                        str,
                    }
                    enum_value_to_name = {
                        "plains": "PLAINS",
                        "mountain": "MOUNTAIN",
                        "grevys": "GREVYS",
                    }
                
                @schemas.classproperty
                def PLAINS(cls):
                    return cls("plains")
                
                @schemas.classproperty
                def MOUNTAIN(cls):
                    return cls("mountain")
                
                @schemas.classproperty
                def GREVYS(cls):
                    return cls("grevys")
            
            
            class ClassName(
                schemas.StrSchema
            ):
            
            
                class Schema_:
                    types = {
                        str,
                    }
                    enum_value_to_name = {
                        "zebra": "ZEBRA",
                    }
                
                @schemas.classproperty
                def ZEBRA(cls):
                    return cls("zebra")
            __annotations__ = {
                "type": Type,
                "className": ClassName,
            }
        AdditionalProperties = schemas.AnyTypeSchema
    
    @property
    def className(self) -> Schema_.Properties.ClassName:
        return self.__getitem__("className")
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["className"]) -> Schema_.Properties.ClassName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> Schema_.Properties.Type: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> Schema_.AdditionalProperties: ...
    
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal["className"],
            typing_extensions.Literal["type"],
            str
        ]
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    def __new__(
        cls,
        *args_: typing.Union[dict, frozendict.frozendict],
        className: typing.Union[Schema_.Properties.ClassName, str],
        type: typing.Union[Schema_.Properties.Type, str, schemas.Unset] = schemas.unset,
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
        **kwargs: typing.Union[Schema_.AdditionalProperties, dict, frozendict.frozendict, str, datetime.date, datetime.datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader],
    ) -> 'Zebra':
        return super().__new__(
            cls,
            *args_,
            className=className,
            type=type,
            configuration_=configuration_,
            **kwargs,
        )
