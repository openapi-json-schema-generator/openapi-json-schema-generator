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
            ComposedAnyOfDifferentTypesNoValidations = schemas.DictSchema
            ComposedAnyOfDifferentTypesNoValidations = schemas.DateSchema
            ComposedAnyOfDifferentTypesNoValidations = schemas.DateTimeSchema
            ComposedAnyOfDifferentTypesNoValidations = schemas.BinarySchema
            ComposedAnyOfDifferentTypesNoValidations = schemas.StrSchema
            ComposedAnyOfDifferentTypesNoValidations = schemas.StrSchema
            ComposedAnyOfDifferentTypesNoValidations = schemas.DictSchema
            ComposedAnyOfDifferentTypesNoValidations = schemas.BoolSchema
            ComposedAnyOfDifferentTypesNoValidations = schemas.NoneSchema
            
            
            class ComposedAnyOfDifferentTypesNoValidations(
                schemas.ListSchema
            ):
                """NOTE: This class is auto generated by OpenAPI Generator.
                Ref: https://openapi-generator.tech
            
                Do not edit the class manually.
                """
            
            
                class MetaOapg:
                    types = {tuple}
                    ComposedAnyOfDifferentTypesNoValidations = schemas.AnyTypeSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.ComposedAnyOfDifferentTypesNoValidations, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.ComposedAnyOfDifferentTypesNoValidations, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'ComposedAnyOfDifferentTypesNoValidations':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.ComposedAnyOfDifferentTypesNoValidations:
                    return super().__getitem__(i)
            ComposedAnyOfDifferentTypesNoValidations = schemas.NumberSchema
            ComposedAnyOfDifferentTypesNoValidations = schemas.Float32Schema
            ComposedAnyOfDifferentTypesNoValidations = schemas.Float64Schema
            ComposedAnyOfDifferentTypesNoValidations = schemas.IntSchema
            ComposedAnyOfDifferentTypesNoValidations = schemas.Int32Schema
            ComposedAnyOfDifferentTypesNoValidations = schemas.Int64Schema
            classes = [
                ComposedAnyOfDifferentTypesNoValidations,
                ComposedAnyOfDifferentTypesNoValidations,
                ComposedAnyOfDifferentTypesNoValidations,
                ComposedAnyOfDifferentTypesNoValidations,
                ComposedAnyOfDifferentTypesNoValidations,
                ComposedAnyOfDifferentTypesNoValidations,
                ComposedAnyOfDifferentTypesNoValidations,
                ComposedAnyOfDifferentTypesNoValidations,
                ComposedAnyOfDifferentTypesNoValidations,
                ComposedAnyOfDifferentTypesNoValidations,
                ComposedAnyOfDifferentTypesNoValidations,
                ComposedAnyOfDifferentTypesNoValidations,
                ComposedAnyOfDifferentTypesNoValidations,
                ComposedAnyOfDifferentTypesNoValidations,
                ComposedAnyOfDifferentTypesNoValidations,
                ComposedAnyOfDifferentTypesNoValidations,
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
