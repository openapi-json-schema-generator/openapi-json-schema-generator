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


class ArrayWithValidationsInItems(
    schemas.ListSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class Schema_:
        types = {tuple}
        max_items = 2
        
        
        class Items(
            schemas.Int64Schema
        ):
            pass

    def __new__(
        cls,
        _arg: typing.Union[typing.Tuple[typing.Union[Schema_.Items, decimal.Decimal, int, ]], typing.List[typing.Union[Schema_.Items, decimal.Decimal, int, ]]],
        _configuration: typing.Optional[schemas.configuration_module.Configuration] = None,
    ) -> 'ArrayWithValidationsInItems':
        return super().__new__(
            cls,
            _arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> Schema_.Items:
        return super().__getitem__(i)
