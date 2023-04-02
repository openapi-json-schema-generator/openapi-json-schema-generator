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


class Quadrilateral(
    schemas.AnyTypeSchema,
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """


    class Schema_:
        # any type
        
        @staticmethod
        def discriminator():
            return {
                'quadrilateralType': {
                    'ComplexQuadrilateral': complex_quadrilateral.ComplexQuadrilateral,
                    'SimpleQuadrilateral': simple_quadrilateral.SimpleQuadrilateral,
                }
            }
        
        class OneOf:
        
            @staticmethod
            def _0() -> typing.Type['simple_quadrilateral.SimpleQuadrilateral']:
                return simple_quadrilateral.SimpleQuadrilateral
        
            @staticmethod
            def _1() -> typing.Type['complex_quadrilateral.ComplexQuadrilateral']:
                return complex_quadrilateral.ComplexQuadrilateral
            classes = [
                _0,
                _1,
            ]


    def __new__(
        cls,
        *args_: typing.Union[dict, frozendict.frozendict, str, datetime.date, datetime.datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader],
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
        **kwargs: typing.Union[dict, frozendict.frozendict, list, tuple, decimal.Decimal, float, int, str, datetime.date, datetime.datetime, uuid.UUID, bool, None, bytes, io.FileIO, io.BufferedReader, schemas.Schema],
    ) -> 'Quadrilateral':
        return super().__new__(
            cls,
            *args_,
            configuration_=configuration_,
            **kwargs,
        )

from petstore_api.components.schema import complex_quadrilateral
from petstore_api.components.schema import simple_quadrilateral
