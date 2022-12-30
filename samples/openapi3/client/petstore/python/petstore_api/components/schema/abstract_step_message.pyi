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


class AbstractStepMessage(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Abstract Step
    """


    class Schema_:
        types = {
            frozendict.frozendict,
        }
        required = {
            "description",
            "discriminator",
            "sequenceNumber",
        }
        
        @staticmethod
        def discriminator():
            return {
                'discriminator': {
                    'AbstractStepMessage': AbstractStepMessage,
                }
            }
        
        class Properties:
            Discriminator = schemas.StrSchema
            __annotations__ = {
                "discriminator": Discriminator,
            }
        
        class AnyOf:
        
            @staticmethod
            def any_of0() -> typing.Type['AbstractStepMessage']:
                return AbstractStepMessage
            classes = [
                any_of0,
            ]

    
    description: schemas.AnyTypeSchema
    discriminator: Schema_.Properties.Discriminator
    sequenceNumber: schemas.AnyTypeSchema
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> schemas.AnyTypeSchema: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["discriminator"]) -> Schema_.Properties.Discriminator: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sequenceNumber"]) -> schemas.AnyTypeSchema: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal["description"],
            typing_extensions.Literal["discriminator"],
            typing_extensions.Literal["sequenceNumber"],
            str
        ]
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_(self, name: typing_extensions.Literal["description"]) -> schemas.AnyTypeSchema: ...
    
    @typing.overload
    def get_item_(self, name: typing_extensions.Literal["discriminator"]) -> Schema_.Properties.Discriminator: ...
    
    @typing.overload
    def get_item_(self, name: typing_extensions.Literal["sequenceNumber"]) -> schemas.AnyTypeSchema: ...
    
    @typing.overload
    def get_item_(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_(
        self,
        name: typing.Union[
            typing_extensions.Literal["description"],
            typing_extensions.Literal["discriminator"],
            typing_extensions.Literal["sequenceNumber"],
            str
        ]
    ):
        return super().get_item_(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        description: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, datetime.date, datetime.datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        discriminator: typing.Union[Schema_.Properties.Discriminator, str, ],
        sequenceNumber: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, datetime.date, datetime.datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        configuration_: typing.Optional[schemas.configuration_module.Configuration] = None,
        **kwargs: typing.Union[dict, frozendict.frozendict, list, tuple, decimal.Decimal, float, int, str, datetime.date, datetime.datetime, uuid.UUID, bool, None, bytes, io.FileIO, io.BufferedReader, schemas.Schema],
    ) -> 'AbstractStepMessage':
        return super().__new__(
            cls,
            *_args,
            description=description,
            discriminator=discriminator,
            sequenceNumber=sequenceNumber,
            configuration_=configuration_,
            **kwargs,
        )
