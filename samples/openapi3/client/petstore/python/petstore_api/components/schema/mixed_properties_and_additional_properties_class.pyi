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


class MixedPropertiesAndAdditionalPropertiesClass(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class Properties:
            Uuid = schemas.UUIDSchema
            DateTime = schemas.DateTimeSchema
            
            
            class Map(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def additional_properties() -> typing.Type['animal.Animal']:
                        return animal.Animal
                
                def __getitem__(self, name: str) -> 'animal.Animal':
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                def get_item_oapg(self, name: str) -> 'animal.Animal':
                    return super().get_item_oapg(name)
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: 'animal.Animal',
                ) -> 'Map':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "uuid": Uuid,
                "dateTime": DateTime,
                "map": Map,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["uuid"]) -> MetaOapg.Properties.Uuid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dateTime"]) -> MetaOapg.Properties.DateTime: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["map"]) -> MetaOapg.Properties.Map: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal["uuid"],
            typing_extensions.Literal["dateTime"],
            typing_extensions.Literal["map"],
            str
        ]
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["uuid"]) -> typing.Union[MetaOapg.Properties.Uuid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dateTime"]) -> typing.Union[MetaOapg.Properties.DateTime, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["map"]) -> typing.Union[MetaOapg.Properties.Map, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(
        self,
        name: typing.Union[
            typing_extensions.Literal["uuid"],
            typing_extensions.Literal["dateTime"],
            typing_extensions.Literal["map"],
            str
        ]
    ):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        uuid: typing.Union[MetaOapg.Properties.Uuid, str, uuid.UUID, schemas.Unset] = schemas.unset,
        dateTime: typing.Union[MetaOapg.Properties.DateTime, str, datetime, schemas.Unset] = schemas.unset,
        map: typing.Union[MetaOapg.Properties.Map, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'MixedPropertiesAndAdditionalPropertiesClass':
        return super().__new__(
            cls,
            *_args,
            uuid=uuid,
            dateTime=dateTime,
            map=map,
            _configuration=_configuration,
            **kwargs,
        )
