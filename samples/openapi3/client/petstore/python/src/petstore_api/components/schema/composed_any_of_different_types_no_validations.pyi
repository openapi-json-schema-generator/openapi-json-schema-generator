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


class (
    schemas.AnyTypeSchema,
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """


    class Schema_:
        # any type
        
        class AnyOf:
             = schemas.DictSchema
             = schemas.DateSchema
             = schemas.DateTimeSchema
             = schemas.BinarySchema
             = schemas.StrSchema
             = schemas.StrSchema
             = schemas.DictSchema
             = schemas.BoolSchema
             = schemas.NoneSchema
            
            
            class (
                schemas.ListSchema
            ):
            
            
                class Schema_:
                    types = {tuple}
                     = schemas.AnyTypeSchema
            
                def __new__(
                    cls,
                    arg_: typing.Union[typing.Tuple[typing.Union[Schema_., dict, frozendict.frozendict, str, datetime.date, datetime.datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[Schema_., dict, frozendict.frozendict, str, datetime.date, datetime.datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
                    configuration_: typing.Optional[schemas.configuration_module.Configuration] = None,
                ) -> '':
                    return super().__new__(
                        cls,
                        arg_,
                        configuration_=configuration_,
                    )
            
                def __getitem__(self, i: int) -> Schema_.:
                    return super().__getitem__(i)
             = schemas.NumberSchema
             = schemas.Float32Schema
             = schemas.Float64Schema
             = schemas.Schema
             = schemas.Schema
             = schemas.Schema
            classes = [
                ,
                ,
                ,
                ,
                ,
                ,
                ,
                ,
                ,
                ,
                ,
                ,
                ,
                ,
                ,
                ,
            ]


    def __new__(
        cls,
        *args_: typing.Union[dict, frozendict.frozendict, str, datetime.date, datetime.datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        configuration_: typing.Optional[schemas.configuration_module.Configuration] = None,
        **kwargs: typing.Union[dict, frozendict.frozendict, list, tuple, decimal.Decimal, float, int, str, datetime.date, datetime.datetime, uuid.UUID, bool, None, bytes, io.FileIO, io.BufferedReader, schemas.Schema],
    ) -> '':
        return super().__new__(
            cls,
            *args_,
            configuration_=configuration_,
            **kwargs,
        )
