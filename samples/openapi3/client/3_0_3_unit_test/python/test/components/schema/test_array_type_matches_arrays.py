# coding: utf-8

"""
    openapi 3.0.3 sample spec

    sample spec for testing openapi functionality, built from json schema tests for draft6  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://openapi-generator.tech
"""

import unittest

import unit_test_api
from unit_test_api.components.schema. import ArrayTypeMatchesArrays
from unit_test_api import configuration


class TestArrayTypeMatchesArrays(unittest.TestCase):
    """ArrayTypeMatchesArrays unit test stubs"""
    _configuration = configuration.Configuration()

    def test_a_float_is_not_an_array_fails(self):
        # a float is not an array
        with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
            ArrayTypeMatchesArrays.from_openapi_data_oapg(
                1.1,
                _configuration=self._configuration
            )

    def test_a_boolean_is_not_an_array_fails(self):
        # a boolean is not an array
        with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
            ArrayTypeMatchesArrays.from_openapi_data_oapg(
                True,
                _configuration=self._configuration
            )

    def test_null_is_not_an_array_fails(self):
        # null is not an array
        with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
            ArrayTypeMatchesArrays.from_openapi_data_oapg(
                None,
                _configuration=self._configuration
            )

    def test_an_object_is_not_an_array_fails(self):
        # an object is not an array
        with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
            ArrayTypeMatchesArrays.from_openapi_data_oapg(
                {
                },
                _configuration=self._configuration
            )

    def test_a_string_is_not_an_array_fails(self):
        # a string is not an array
        with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
            ArrayTypeMatchesArrays.from_openapi_data_oapg(
                "foo",
                _configuration=self._configuration
            )

    def test_an_array_is_an_array_passes(self):
        # an array is an array
        ArrayTypeMatchesArrays.from_openapi_data_oapg(
            [
            ],
            _configuration=self._configuration
        )

    def test_an_integer_is_not_an_array_fails(self):
        # an integer is not an array
        with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
            ArrayTypeMatchesArrays.from_openapi_data_oapg(
                1,
                _configuration=self._configuration
            )


if __name__ == '__main__':
    unittest.main()
