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


class Capitalization(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class Properties:
            Capitalization = schemas.StrSchema
            Capitalization = schemas.StrSchema
            Capitalization = schemas.StrSchema
            Capitalization = schemas.StrSchema
            Capitalization = schemas.StrSchema
            Capitalization = schemas.StrSchema
            __annotations__ = {
                "smallCamel": Capitalization,
                "CapitalCamel": Capitalization,
                "small_Snake": Capitalization,
                "Capital_Snake": Capitalization,
                "SCA_ETH_Flow_Points": Capitalization,
                "ATT_NAME": Capitalization,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["smallCamel"]) -> MetaOapg.Properties.Capitalization: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["CapitalCamel"]) -> MetaOapg.Properties.Capitalization: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["small_Snake"]) -> MetaOapg.Properties.Capitalization: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Capital_Snake"]) -> MetaOapg.Properties.Capitalization: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["SCA_ETH_Flow_Points"]) -> MetaOapg.Properties.Capitalization: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ATT_NAME"]) -> MetaOapg.Properties.Capitalization: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal["smallCamel"],
            typing_extensions.Literal["CapitalCamel"],
            typing_extensions.Literal["small_Snake"],
            typing_extensions.Literal["Capital_Snake"],
            typing_extensions.Literal["SCA_ETH_Flow_Points"],
            typing_extensions.Literal["ATT_NAME"],
            str
        ]
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["smallCamel"]) -> typing.Union[MetaOapg.Properties.Capitalization, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["CapitalCamel"]) -> typing.Union[MetaOapg.Properties.Capitalization, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["small_Snake"]) -> typing.Union[MetaOapg.Properties.Capitalization, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Capital_Snake"]) -> typing.Union[MetaOapg.Properties.Capitalization, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["SCA_ETH_Flow_Points"]) -> typing.Union[MetaOapg.Properties.Capitalization, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ATT_NAME"]) -> typing.Union[MetaOapg.Properties.Capitalization, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(
        self,
        name: typing.Union[
            typing_extensions.Literal["smallCamel"],
            typing_extensions.Literal["CapitalCamel"],
            typing_extensions.Literal["small_Snake"],
            typing_extensions.Literal["Capital_Snake"],
            typing_extensions.Literal["SCA_ETH_Flow_Points"],
            typing_extensions.Literal["ATT_NAME"],
            str
        ]
    ):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        smallCamel: typing.Union[MetaOapg.Properties.Capitalization, str, schemas.Unset] = schemas.unset,
        CapitalCamel: typing.Union[MetaOapg.Properties.Capitalization, str, schemas.Unset] = schemas.unset,
        small_Snake: typing.Union[MetaOapg.Properties.Capitalization, str, schemas.Unset] = schemas.unset,
        Capital_Snake: typing.Union[MetaOapg.Properties.Capitalization, str, schemas.Unset] = schemas.unset,
        SCA_ETH_Flow_Points: typing.Union[MetaOapg.Properties.Capitalization, str, schemas.Unset] = schemas.unset,
        ATT_NAME: typing.Union[MetaOapg.Properties.Capitalization, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Capitalization':
        return super().__new__(
            cls,
            *_args,
            smallCamel=smallCamel,
            CapitalCamel=CapitalCamel,
            small_Snake=small_Snake,
            Capital_Snake=Capital_Snake,
            SCA_ETH_Flow_Points=SCA_ETH_Flow_Points,
            ATT_NAME=ATT_NAME,
            _configuration=_configuration,
            **kwargs,
        )
