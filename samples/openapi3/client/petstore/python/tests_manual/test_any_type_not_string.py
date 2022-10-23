# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""

import unittest

import petstore_api
from petstore_api.components.schema.any_type_not_string import AnyTypeNotString


class TestAnyTypeNotString(unittest.TestCase):
    """AnyTypeNotString unit test stubs"""

    def test_AnyTypeNotString(self):
        # valid values work
        valid_values = [
            True,
            None,
            0,
            3.14,
            [],
            {}
        ]
        for valid_value in valid_values:
            AnyTypeNotString(valid_value)

        # invalid value raises an exception
        with self.assertRaises(petstore_api.ApiValueError):
            AnyTypeNotString('')


if __name__ == '__main__':
    unittest.main()
