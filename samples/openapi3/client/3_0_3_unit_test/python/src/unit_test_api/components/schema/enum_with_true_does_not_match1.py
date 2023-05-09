# coding: utf-8

"""
    openapi 3.0.3 sample spec
    sample spec for testing openapi functionality, built from json schema tests for draft6  # noqa: E501
    The version of the OpenAPI document: 0.0.1
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from unit_test_api.shared_imports.schema_imports import *


class EnumWithTrueDoesNotMatch1(
    schemas.BoolSchema
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """


    class Schema_:
        types = {
            schemas.BoolClass,
        }
        enum_value_to_name = {
            schemas.BoolClass.TRUE: "TRUE",
        }
    
    @schemas.classproperty
    def TRUE(cls):
        return cls(True)
