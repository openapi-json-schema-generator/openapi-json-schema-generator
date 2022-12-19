# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
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
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "className",
        }
        
        class Properties:
            
            
            class Zebra(
                schemas.StrSchema
            ):
                """NOTE: This class is auto generated by OpenAPI Generator.
                Ref: https://openapi-generator.tech
            
                Do not edit the class manually.
                """
                
                @schemas.classproperty
                def PLAINS(cls):
                    return cls("plains")
                
                @schemas.classproperty
                def MOUNTAIN(cls):
                    return cls("mountain")
                
                @schemas.classproperty
                def GREVYS(cls):
                    return cls("grevys")
            
            
            class Zebra(
                schemas.StrSchema
            ):
                """NOTE: This class is auto generated by OpenAPI Generator.
                Ref: https://openapi-generator.tech
            
                Do not edit the class manually.
                """
                
                @schemas.classproperty
                def ZEBRA(cls):
                    return cls("zebra")
            __annotations__ = {
                "type": Zebra,
                "className": Zebra,
            }
        Zebra = schemas.AnyTypeSchema
    
    className: MetaOapg.Properties.Zebra
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["className"]) -> MetaOapg.Properties.Zebra: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.Properties.Zebra: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> MetaOapg.Zebra: ...
    
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
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["className"]) -> MetaOapg.Properties.Zebra: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.Properties.Zebra, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[MetaOapg.Zebra, schemas.Unset]: ...
    
    def get_item_oapg(
        self,
        name: typing.Union[
            typing_extensions.Literal["className"],
            typing_extensions.Literal["type"],
            str
        ]
    ):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        className: typing.Union[MetaOapg.Properties.Zebra, str, ],
        type: typing.Union[MetaOapg.Properties.Zebra, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[MetaOapg.Zebra, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
    ) -> 'Zebra':
        return super().__new__(
            cls,
            *_args,
            className=className,
            type=type,
            _configuration=_configuration,
            **kwargs,
        )
