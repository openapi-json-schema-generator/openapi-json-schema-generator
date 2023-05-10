# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *


class Quadrilateral(
    schemas.AnyTypeSchema[schemas.T],
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



from petstore_api.components.schema import complex_quadrilateral
from petstore_api.components.schema import simple_quadrilateral
