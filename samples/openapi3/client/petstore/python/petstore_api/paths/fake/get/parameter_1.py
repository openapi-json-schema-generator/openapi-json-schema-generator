# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

from dataclasses import dataclass
import typing_extensions
import urllib3

from petstore_api import api_client, exceptions
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




class schema(
    schemas.EnumBase,
    schemas.StrSchema
):


    class MetaOapg(schemas.JsonSchemaValidator):
        types = {
            str,
        }
        enum_value_to_name = {
            "_abc": "_ABC",
            "-efg": "EFG",
            "(xyz)": "XYZ",
        }
    
    @schemas.classproperty
    def _ABC(cls):
        return cls("_abc")
    
    @schemas.classproperty
    def EFG(cls):
        return cls("-efg")
    
    @schemas.classproperty
    def XYZ(cls):
        return cls("(xyz)")


parameter_oapg = api_client.HeaderParameter(
    name="enum_header_string",
    style=api_client.ParameterStyle.SIMPLE,
    schema=schema,
)
