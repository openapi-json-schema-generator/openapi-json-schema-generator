# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

import datetime  # noqa: F401
import decimal  # noqa: F401
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
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.

    this is a model that allows payloads of type object or number
    """


    class Schema_:
        # any type
        
        class OneOf:
        
            @staticmethod
            def _0() -> typing.Type['number_with_validations.NumberWithValidations']:
                return number_with_validations.NumberWithValidations
        
            @staticmethod
            def _1() -> typing.Type['animal.Animal']:
                return animal.Animal
            _2 = schemas.NoneSchema
            _3 = schemas.DateSchema
            
            
            class _4(
                schemas.DictSchema
            ):
            
            
                class Schema_:
                    types = {frozendict.frozendict}
                    max_properties = 4
                    min_properties = 4
            
                def __new__(
                    cls,
                    *args_: typing.Union[dict, frozendict.frozendict],
                    configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
                    **kwargs: typing.Union[dict, frozendict.frozendict, list, tuple, decimal.Decimal, float, int, str, datetime.date, datetime.datetime, uuid.UUID, bool, None, bytes, io.FileIO, io.BufferedReader, schemas.Schema],
                ) -> 'ComposedOneOfDifferentTypes.Schema_.OneOf._4':
                    return super().__new__(
                        cls,
                        *args_,
                        configuration_=configuration_,
                        **kwargs,
                    )
            
            
            class _5(
                schemas.ListSchema
            ):
            
            
                class Schema_:
                    types = {tuple}
                    max_items = 4
                    min_items = 4
                    Items = schemas.AnyTypeSchema
            
                def __new__(
                    cls,
                    arg_: typing.Union[
                        typing.Tuple[
                            typing.Union[Schema_.Items, dict, frozendict.frozendict, str, datetime.date, datetime.datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader], ...
                        ],
                        typing.List[
                            typing.Union[Schema_.Items, dict, frozendict.frozendict, str, datetime.date, datetime.datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader]
                        ],
                    ],
                    configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
                ) -> 'ComposedOneOfDifferentTypes.Schema_.OneOf._5':
                    return super().__new__(
                        cls,
                        arg_,
                        configuration_=configuration_,
                    )
            
                def __getitem__(self, i: int) -> Schema_.Items:
                    return super().__getitem__(i)
            
            
            class _6(
                schemas.DateTimeSchema
            ):
            
            
                class Schema_:
                    types = {
                        str,
                    }
                    format = 'date-time'
                    regex={
                        'pattern': r'^2020.*',  # noqa: E501
                    }
            classes = [
                _0,
                _1,
                _2,
                _3,
                _4,
                _5,
                _6,
            ]



from petstore_api.components.schema import animal
from petstore_api.components.schema import number_with_validations
