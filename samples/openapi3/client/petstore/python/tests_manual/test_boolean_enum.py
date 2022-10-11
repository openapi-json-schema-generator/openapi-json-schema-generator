# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import petstore_api
from petstore_api.components.schema.boolean_enum_oapg import BooleanEnum


class TestBooleanEnum(unittest.TestCase):
    """BooleanEnum unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_BooleanEnum(self):
        """Test BooleanEnum"""
        model = BooleanEnum(True)
        assert model is BooleanEnum.TRUE
        assert model.is_true_oapg()
        assert model.is_false_oapg() is False
        assert repr(model) == '<DynamicSchema: True>'
        with self.assertRaises(petstore_api.ApiValueError):
            BooleanEnum(False)


if __name__ == '__main__':
    unittest.main()
