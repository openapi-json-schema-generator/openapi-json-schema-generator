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


class NoAdditionalProperties(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "id",
        }
        
        class Properties:
            Id = schemas.Int64Schema
            PetId = schemas.Int64Schema
            __annotations__ = {
                "id": Id,
                "petId": PetId,
            }
        AdditionalProperties = schemas.NotAnyTypeSchema
    
    id: MetaOapg.Properties.Id
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.Properties.Id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["petId"]) -> MetaOapg.Properties.PetId: ...
    
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal["id"],
            typing_extensions.Literal["petId"],
        ]
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_(self, name: typing_extensions.Literal["id"]) -> MetaOapg.Properties.Id: ...
    
    @typing.overload
    def get_item_(self, name: typing_extensions.Literal["petId"]) -> typing.Union[MetaOapg.Properties.PetId, schemas.Unset]: ...
    
    def get_item_(
        self,
        name: typing.Union[
            typing_extensions.Literal["id"],
            typing_extensions.Literal["petId"],
        ]
    ):
        return super().get_item_(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.Properties.Id, decimal.Decimal, int, ],
        petId: typing.Union[MetaOapg.Properties.PetId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.configuration_module.Configuration] = None,
    ) -> 'NoAdditionalProperties':
        return super().__new__(
            cls,
            *_args,
            id=id,
            petId=petId,
            _configuration=_configuration,
        )
