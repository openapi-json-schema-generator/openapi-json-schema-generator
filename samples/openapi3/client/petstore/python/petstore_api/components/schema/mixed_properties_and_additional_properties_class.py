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
        types = {frozendict.frozendict}
        
        class Properties:
            MixedPropertiesAndAdditionalPropertiesClass = schemas.UUIDSchema
            MixedPropertiesAndAdditionalPropertiesClass = schemas.DateTimeSchema
            
            
            class MixedPropertiesAndAdditionalPropertiesClass(
                schemas.DictSchema
            ):
                """NOTE: This class is auto generated by OpenAPI Generator.
                Ref: https://openapi-generator.tech
            
                Do not edit the class manually.
                """
            
            
                class MetaOapg:
                    types = {frozendict.frozendict}
                    
                    @staticmethod
                    def mixed_properties_and_additional_properties_class() -> typing.Type['animal.Animal']:
                        return animal.Animal
                
                def __getitem__(self, name: str) -> 'Animal':
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                def get_item_oapg(self, name: str) -> 'Animal':
                    return super().get_item_oapg(name)
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: 'Animal',
                ) -> 'MixedPropertiesAndAdditionalPropertiesClass':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "uuid": MixedPropertiesAndAdditionalPropertiesClass,
                "dateTime": MixedPropertiesAndAdditionalPropertiesClass,
                "map": MixedPropertiesAndAdditionalPropertiesClass,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["uuid"]) -> MetaOapg.Properties.MixedPropertiesAndAdditionalPropertiesClass: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dateTime"]) -> MetaOapg.Properties.MixedPropertiesAndAdditionalPropertiesClass: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["map"]) -> MetaOapg.Properties.MixedPropertiesAndAdditionalPropertiesClass: ...
    
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
    def get_item_oapg(self, name: typing_extensions.Literal["uuid"]) -> typing.Union[MetaOapg.Properties.MixedPropertiesAndAdditionalPropertiesClass, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dateTime"]) -> typing.Union[MetaOapg.Properties.MixedPropertiesAndAdditionalPropertiesClass, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["map"]) -> typing.Union[MetaOapg.Properties.MixedPropertiesAndAdditionalPropertiesClass, schemas.Unset]: ...
    
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
        uuid: typing.Union[MetaOapg.Properties.MixedPropertiesAndAdditionalPropertiesClass, str, uuid.UUID, schemas.Unset] = schemas.unset,
        dateTime: typing.Union[MetaOapg.Properties.MixedPropertiesAndAdditionalPropertiesClass, str, datetime, schemas.Unset] = schemas.unset,
        map: typing.Union[MetaOapg.Properties.MixedPropertiesAndAdditionalPropertiesClass, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
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
