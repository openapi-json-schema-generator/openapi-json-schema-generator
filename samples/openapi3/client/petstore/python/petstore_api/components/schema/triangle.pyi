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


class Triangle(
    schemas.ComposedSchema,
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        types = None
        
        @staticmethod
        def discriminator():
            return {
                'triangleType': {
                    'EquilateralTriangle': equilateral_triangle.EquilateralTriangle,
                    'IsoscelesTriangle': isosceles_triangle.IsoscelesTriangle,
                    'ScaleneTriangle': scalene_triangle.ScaleneTriangle,
                }
            }
        
        class one_of:
        
            @staticmethod
            def one_of_0() -> typing.Type['equilateral_triangle.EquilateralTriangle']:
                return equilateral_triangle.EquilateralTriangle
        
            @staticmethod
            def one_of_1() -> typing.Type['isosceles_triangle.IsoscelesTriangle']:
                return isosceles_triangle.IsoscelesTriangle
        
            @staticmethod
            def one_of_2() -> typing.Type['scalene_triangle.ScaleneTriangle']:
                return scalene_triangle.ScaleneTriangle
            classes = [
                one_of_0,
                one_of_1,
                one_of_2,
            ]


    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Triangle':
        return super().__new__(
            cls,
            *_args,
            _configuration=_configuration,
            **kwargs,
        )

from petstore_api.components.schema import equilateral_triangle
from petstore_api.components.schema import isosceles_triangle
from petstore_api.components.schema import scalene_triangle
