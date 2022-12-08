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


class ComposedNone(
    schemas.NoneSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        types = {
            schemas.NoneClass,
        }
        
        class all_of:
             = schemas.AnyTypeSchema
            classes = [
                ,
            ]

    
    
    def get_item_oapg(self, name: typing.Union[str]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[None, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'ComposedNone':
        return super().__new__(
            cls,
            *_args,
            _configuration=_configuration,
        )
