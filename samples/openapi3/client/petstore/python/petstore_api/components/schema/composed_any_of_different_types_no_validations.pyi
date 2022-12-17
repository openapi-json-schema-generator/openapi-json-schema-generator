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


class ComposedAnyOfDifferentTypesNoValidations(
    schemas.AnyTypeSchema,
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        # any type
        
        class AnyOf:
            AnyOf0 = schemas.DictSchema
            AnyOf1 = schemas.DateSchema
            AnyOf2 = schemas.DateTimeSchema
            AnyOf3 = schemas.BinarySchema
            AnyOf4 = schemas.StrSchema
            AnyOf5 = schemas.StrSchema
            AnyOf6 = schemas.DictSchema
            AnyOf7 = schemas.BoolSchema
            AnyOf8 = schemas.NoneSchema
            
            
            class AnyOf9(
                schemas.ListSchema
            ):
                """NOTE: This class is auto generated by OpenAPI Generator.
                Ref: https://openapi-generator.tech
            
                Do not edit the class manually.
                """
            
            
                class MetaOapg:
                    types = {tuple}
                    Items = schemas.AnyTypeSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.Items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.Items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'AnyOf9':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.Items:
                    return super().__getitem__(i)
            AnyOf10 = schemas.NumberSchema
            AnyOf11 = schemas.Float32Schema
            AnyOf12 = schemas.Float64Schema
            AnyOf13 = schemas.IntSchema
            AnyOf14 = schemas.Int32Schema
            AnyOf15 = schemas.Int64Schema
            classes = [
                AnyOf0,
                AnyOf1,
                AnyOf2,
                AnyOf3,
                AnyOf4,
                AnyOf5,
                AnyOf6,
                AnyOf7,
                AnyOf8,
                AnyOf9,
                AnyOf10,
                AnyOf11,
                AnyOf12,
                AnyOf13,
                AnyOf14,
                AnyOf15,
            ]


    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ComposedAnyOfDifferentTypesNoValidations':
        return super().__new__(
            cls,
            *_args,
            _configuration=_configuration,
            **kwargs,
        )
