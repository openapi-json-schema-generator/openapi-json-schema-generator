# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import petstore_api
from petstore_api.components.schema.composed_string import ComposedString


class TestComposedString(unittest.TestCase):
    """ComposedString unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_ComposedString(self):
        """Test ComposedString"""
        valid_values = ['']
        all_values = [None, True, False, 2, 3.14, '', {}, []]
        for value in all_values:
            if value not in valid_values:
                with self.assertRaises(petstore_api.ApiTypeError):
                    model = ComposedString(value)
                continue
            model = ComposedString(value)


if __name__ == '__main__':
    unittest.main()
