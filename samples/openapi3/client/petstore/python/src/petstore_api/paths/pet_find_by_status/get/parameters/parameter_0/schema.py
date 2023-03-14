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


class Schema(
    schemas.ListSchema
):


    class Schema_:
        types = {tuple}
        
        
        class Items(
            schemas.StrSchema
        ):
        
        
            class Schema_:
                types = {
                    str,
                }
                default = "available"
                enum_value_to_name = {
                    "available": "AVAILABLE",
                    "pending": "PENDING",
                    "sold": "SOLD",
                }
            
            @schemas.classproperty
            def AVAILABLE(cls):
                return cls("available")
            
            @schemas.classproperty
            def PENDING(cls):
                return cls("pending")
            
            @schemas.classproperty
            def SOLD(cls):
                return cls("sold")

    def __new__(
        cls,
        arg_: typing.Union[
            typing.Tuple[
                typing.Union[Schema_.Items, str, ], ...
            ],
            typing.List[
                typing.Union[Schema_.Items, str, ]
            ],
        ],
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
    ) -> 'Schema':
        return super().__new__(
            cls,
            arg_,
            configuration_=configuration_,
        )

    def __getitem__(self, i: int) -> Schema_.Items:
        return super().__getitem__(i)
