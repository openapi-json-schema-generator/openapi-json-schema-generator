# coding: utf-8

"""
    openapi 3.0.3 sample spec

    sample spec for testing openapi functionality, built from json schema tests for draft6  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://openapi-generator.tech
"""

import unittest

import unit_test_api
from unit_test_api.components.schema.oneof_with_base_schema import OneofWithBaseSchema
from unit_test_api import configuration


class TestOneofWithBaseSchema(unittest.TestCase):
    """OneofWithBaseSchema unit test stubs"""
    _configuration = configuration.Configuration()

    def test_both_oneof_valid_fails(self):
        # both oneOf valid
        with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
            OneofWithBaseSchema.from_openapi_data_(
                "foo",
                _configuration=self._configuration
            )

    def test_mismatch_base_schema_fails(self):
        # mismatch base schema
        with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
            OneofWithBaseSchema.from_openapi_data_(
                3,
                _configuration=self._configuration
            )

    def test_one_oneof_valid_passes(self):
        # one oneOf valid
        OneofWithBaseSchema.from_openapi_data_(
            "foobar",
            _configuration=self._configuration
        )


if __name__ == '__main__':
    unittest.main()
