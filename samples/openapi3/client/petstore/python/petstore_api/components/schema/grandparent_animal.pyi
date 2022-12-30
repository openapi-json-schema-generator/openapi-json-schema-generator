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


class GrandparentAnimal(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class Schema_:
        required = {
            "pet_type",
        }
        
        @staticmethod
        def discriminator():
            return {
                'pet_type': {
                    'ChildCat': child_cat.ChildCat,
                    'ParentPet': parent_pet.ParentPet,
                }
            }
        
        class Properties:
            PetType = schemas.StrSchema
            __annotations__ = {
                "pet_type": PetType,
            }
    
    pet_type: Schema_.Properties.PetType
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pet_type"]) -> Schema_.Properties.PetType: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal["pet_type"],
            str
        ]
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_(self, name: typing_extensions.Literal["pet_type"]) -> Schema_.Properties.PetType: ...
    
    @typing.overload
    def get_item_(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_(
        self,
        name: typing.Union[
            typing_extensions.Literal["pet_type"],
            str
        ]
    ):
        return super().get_item_(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        pet_type: typing.Union[Schema_.Properties.PetType, str, ],
        configuration_: typing.Optional[schemas.configuration_module.Configuration] = None,
        **kwargs: typing.Union[dict, frozendict.frozendict, list, tuple, decimal.Decimal, float, int, str, datetime.date, datetime.datetime, uuid.UUID, bool, None, bytes, io.FileIO, io.BufferedReader, schemas.Schema],
    ) -> 'GrandparentAnimal':
        return super().__new__(
            cls,
            *_args,
            pet_type=pet_type,
            configuration_=configuration_,
            **kwargs,
        )

from petstore_api.components.schema import child_cat
from petstore_api.components.schema import parent_pet
