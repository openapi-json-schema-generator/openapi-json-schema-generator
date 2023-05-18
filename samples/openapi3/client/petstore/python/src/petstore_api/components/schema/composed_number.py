# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *


class ComposedNumber(
    schemas.NumberSchema[schemas.T]
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """


    class Schema_:
        types = {
            decimal.Decimal,
        }
        
        class AllOf:
            _0: typing_extensions.TypeAlias = schemas.AnyTypeSchema[U]
            classes = [
                _0,
            ]


    def __new__(
        cls,
        arg_: typing.Union[decimal.Decimal, int, float],
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
    ) -> ComposedNumber[decimal.Decimal]:
        inst = super().__new__(
            cls,
            arg_,
            configuration_=configuration_,
        )
        inst = typing.cast(
            ComposedNumber[decimal.Decimal],
            inst
        )
        return inst

