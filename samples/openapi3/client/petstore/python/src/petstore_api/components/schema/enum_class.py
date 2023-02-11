# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
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


class EnumClass(
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """


    class Schema_:
        types = {
            str,
        }
        enum_value_to_name = {
            "_abc": "_ABC",
            "-efg": "HYPHEN_MINUS_EFG",
            "(xyz)": "LEFT_PARENTHESIS_XYZ",
            "COUNT_1M": "COUNT_1M",
            "COUNT_50M": "COUNT_50M",
        }
    
    @schemas.classproperty
    def _ABC(cls):
        return cls("_abc")
    
    @schemas.classproperty
    def HYPHEN_MINUS_EFG(cls):
        return cls("-efg")
    
    @schemas.classproperty
    def LEFT_PARENTHESIS_XYZ(cls):
        return cls("(xyz)")
    
    @schemas.classproperty
    def COUNT_1M(cls):
        return cls("COUNT_1M")
    
    @schemas.classproperty
    def COUNT_50M(cls):
        return cls("COUNT_50M")
