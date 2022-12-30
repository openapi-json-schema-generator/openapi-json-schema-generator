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


class Schema(
    schemas.Float64Schema
):


    class MetaOapg:
        types = {
            decimal.Decimal,
        }
        format = 'double'
        enum_value_to_name = {
            1.1: "POSITIVE_1_PT_1",
            -1.2: "NEGATIVE_1_PT_2",
        }
    
    @schemas.classproperty
    def POSITIVE_1_PT_1(cls):
        return cls(1.1)
    
    @schemas.classproperty
    def NEGATIVE_1_PT_2(cls):
        return cls(-1.2)
