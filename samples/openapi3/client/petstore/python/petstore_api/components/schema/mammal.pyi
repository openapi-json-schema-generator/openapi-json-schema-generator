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


class Mammal(
    schemas.AnyTypeSchema,
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        # any type
        
        @staticmethod
        def discriminator():
            return {
                'className': {
                    'Pig': pig.Pig,
                    'whale': whale.Whale,
                    'zebra': zebra.Zebra,
                }
            }
        
        class one_of:
        
            @staticmethod
            def oneOf_0() -> typing.Type['whale.Whale']:
                return whale.Whale
        
            @staticmethod
            def oneOf_1() -> typing.Type['zebra.Zebra']:
                return zebra.Zebra
        
            @staticmethod
            def oneOf_2() -> typing.Type['pig.Pig']:
                return pig.Pig
            classes = [
                oneOf_0,
                oneOf_1,
                oneOf_2,
            ]


    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'mammal':
        return super().__new__(
            cls,
            *_args,
            _configuration=_configuration,
            **kwargs,
        )

from petstore_api.components.schema import pig
from petstore_api.components.schema import whale
from petstore_api.components.schema import zebra
