# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import frozendict

from petstore_api.components.schema.equilateral_triangle_oapg import EquilateralTriangle
from petstore_api.components.schema.isosceles_triangle_oapg import IsoscelesTriangle
from petstore_api.components.schema.scalene_triangle_oapg import ScaleneTriangle
from petstore_api.components.schema.triangle_oapg import Triangle
from petstore_api.components.schema.triangle_interface_oapg import TriangleInterface


class TestTriangle(unittest.TestCase):
    """Triangle unit test stubs"""

    def testTriangle(self):
        """Test Triangle"""
        tri_classes = [EquilateralTriangle, IsoscelesTriangle, ScaleneTriangle]
        for tri_class in tri_classes:
            tri = Triangle(shapeType="Triangle", triangleType=tri_class.__name__)
            assert isinstance(tri, tri_class)
            assert isinstance(tri, Triangle)
            assert isinstance(tri, TriangleInterface)
            assert isinstance(tri, frozendict.frozendict)


if __name__ == '__main__':
    unittest.main()
