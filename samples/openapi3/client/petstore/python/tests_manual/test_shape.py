# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import frozendict

import petstore_api
from petstore_api.schemas import Singleton
from petstore_api.components.schema.shape_oapg import Shape
from petstore_api.components.schema import complex_quadrilateral_oapg
from petstore_api.components.schema import simple_quadrilateral_oapg
from petstore_api.components.schema import triangle_oapg
from petstore_api.components.schema import triangle_interface_oapg
from petstore_api.components.schema import equilateral_triangle_oapg
from petstore_api.components.schema import isosceles_triangle_oapg
from petstore_api.components.schema import scalene_triangle_oapg


class TestShape(unittest.TestCase):
    """Shape unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_recursionlimit(self):
        """Test case for recursionlimit

        """
        assert sys.getrecursionlimit() == 1234

    def testShape(self):
        """Test Shape"""

        tri = Shape(
            shapeType="Triangle",
            triangleType="EquilateralTriangle"
        )
        assert isinstance(tri, equilateral_triangle_oapg.EquilateralTriangle)
        assert isinstance(tri, triangle_oapg.Triangle)
        assert isinstance(tri, triangle_interface_oapg.TriangleInterface)
        assert isinstance(tri, Shape)
        assert isinstance(tri, frozendict.frozendict)
        assert isinstance(tri.shapeType, str)
        assert isinstance(tri.shapeType, Singleton)

        tri = Shape(
            shapeType="Triangle",
            triangleType="IsoscelesTriangle"
        )
        assert isinstance(tri, isosceles_triangle_oapg.IsoscelesTriangle)

        tri = Shape(
            shapeType="Triangle",
            triangleType="ScaleneTriangle"
        )
        assert isinstance(tri, scalene_triangle_oapg.ScaleneTriangle)

        quad = Shape(
            shapeType="Quadrilateral",
            quadrilateralType="ComplexQuadrilateral"
        )
        assert isinstance(quad, complex_quadrilateral_oapg.ComplexQuadrilateral)

        quad = Shape(
            shapeType="Quadrilateral",
            quadrilateralType="SimpleQuadrilateral"
        )
        assert isinstance(quad, simple_quadrilateral_oapg.SimpleQuadrilateral)

        # data missing
        with self.assertRaisesRegex(
                petstore_api.exceptions.ApiValueError,
                r"Cannot deserialize input data due to missing discriminator. The discriminator "
                r"property 'shapeType' is missing at path: \('args\[0\]',\)"
        ):
            Shape({})

        # invalid shape_type (first discriminator). 'Circle' does not exist in the model.
        err_msg = (
            r"Invalid discriminator value was passed in to Shape.shapeType Only the values "
            r"\['Quadrilateral', 'Triangle'\] are allowed at \('args\[0\]', 'shapeType'\)"
        )
        with self.assertRaisesRegex(
                petstore_api.ApiValueError,
                err_msg
        ):
            Shape(shapeType="Circle")

        # invalid quadrilateral_type (second discriminator)
        err_msg = (
            r"Invalid discriminator value was passed in to Quadrilateral.quadrilateralType Only the values "
            r"\['ComplexQuadrilateral', 'SimpleQuadrilateral'\] are allowed at \('args\[0\]', 'quadrilateralType'\)"
        )
        with self.assertRaisesRegex(
                petstore_api.ApiValueError,
                err_msg
        ):
            Shape(
                shapeType="Quadrilateral",
                quadrilateralType="Triangle"
            )


if __name__ == '__main__':
    unittest.main()
