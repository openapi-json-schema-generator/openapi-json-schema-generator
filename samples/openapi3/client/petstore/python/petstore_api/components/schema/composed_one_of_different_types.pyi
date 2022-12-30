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


class ComposedOneOfDifferentTypes(
    schemas.AnyTypeSchema,
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    this is a model that allows payloads of type object or number
    """


    class Schema_:
        # any type
        
        class OneOf:
        
            @staticmethod
            def one_of0() -> typing.Type['number_with_validations.NumberWithValidations']:
                return number_with_validations.NumberWithValidations
        
            @staticmethod
            def one_of1() -> typing.Type['animal.Animal']:
                return animal.Animal
            OneOf2 = schemas.NoneSchema
            OneOf3 = schemas.DateSchema
            
            
            class OneOf4(
                schemas.DictSchema
            ):
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    _configuration: typing.Optional[schemas.configuration_module.Configuration] = None,
                    **kwargs: typing.Union[dict, frozendict.frozendict, list, tuple, decimal.Decimal, float, int, str, datetime.date, datetime.datetime, uuid.UUID, bool, None, bytes, io.FileIO, io.BufferedReader, schemas.Schema],
                ) -> 'OneOf4':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class OneOf5(
                schemas.ListSchema
            ):
            
            
                class Schema_:
                    types = {tuple}
                    max_items = 4
                    min_items = 4
                    Items = schemas.AnyTypeSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[Schema_.Items, dict, frozendict.frozendict, str, datetime.date, datetime.datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[Schema_.Items, dict, frozendict.frozendict, str, datetime.date, datetime.datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
                    _configuration: typing.Optional[schemas.configuration_module.Configuration] = None,
                ) -> 'OneOf5':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> Schema_.Items:
                    return super().__getitem__(i)
            
            
            class OneOf6(
                schemas.DateTimeSchema
            ):
                pass
            classes = [
                one_of0,
                one_of1,
                OneOf2,
                OneOf3,
                OneOf4,
                OneOf5,
                OneOf6,
            ]


    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, str, datetime.date, datetime.datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        _configuration: typing.Optional[schemas.configuration_module.Configuration] = None,
        **kwargs: typing.Union[dict, frozendict.frozendict, list, tuple, decimal.Decimal, float, int, str, datetime.date, datetime.datetime, uuid.UUID, bool, None, bytes, io.FileIO, io.BufferedReader, schemas.Schema],
    ) -> 'ComposedOneOfDifferentTypes':
        return super().__new__(
            cls,
            *_args,
            _configuration=_configuration,
            **kwargs,
        )

from petstore_api.components.schema import animal
from petstore_api.components.schema import number_with_validations
