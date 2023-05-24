# coding: utf-8

"""
    openapi 3.0.3 sample spec
    sample spec for testing openapi functionality, built from json schema tests for draft6  # noqa: E501
    The version of the OpenAPI document: 0.0.1
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from unit_test_api.shared_imports.schema_imports import *


class SimpleEnumValidation(
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
        enum_value_to_name = {
            1: "POSITIVE_1",
            2: "POSITIVE_2",
            3: "POSITIVE_3",
        }
    
    @schemas.classproperty
    def POSITIVE_1(cls):
        return cls(1) # type: ignore
    
    @schemas.classproperty
    def POSITIVE_2(cls):
        return cls(2) # type: ignore
    
    @schemas.classproperty
    def POSITIVE_3(cls):
        return cls(3) # type: ignore
