# coding: utf-8

"""
    openapi 3.0.3 sample spec

    sample spec for testing openapi functionality, built from json schema tests for draft6  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://openapi-generator.tech
"""

import unittest

import unit_test_api
from unit_test_api.components.schema.string_type_matches_strings_oapg import StringTypeMatchesStrings
from unit_test_api import configuration


class TestStringTypeMatchesStrings(unittest.TestCase):
    """StringTypeMatchesStrings unit test stubs"""
    _configuration = configuration.Configuration()

    def test_1_is_not_a_string_fails(self):
        # 1 is not a string
        with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
            StringTypeMatchesStrings.from_openapi_data_oapg(
                1,
                _configuration=self._configuration
            )

    def test_a_string_is_still_a_string_even_if_it_looks_like_a_number_passes(self):
        # a string is still a string, even if it looks like a number
        StringTypeMatchesStrings.from_openapi_data_oapg(
            "1",
            _configuration=self._configuration
        )

    def test_an_empty_string_is_still_a_string_passes(self):
        # an empty string is still a string
        StringTypeMatchesStrings.from_openapi_data_oapg(
            "",
            _configuration=self._configuration
        )

    def test_a_float_is_not_a_string_fails(self):
        # a float is not a string
        with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
            StringTypeMatchesStrings.from_openapi_data_oapg(
                1.1,
                _configuration=self._configuration
            )

    def test_an_object_is_not_a_string_fails(self):
        # an object is not a string
        with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
            StringTypeMatchesStrings.from_openapi_data_oapg(
                {
                },
                _configuration=self._configuration
            )

    def test_an_array_is_not_a_string_fails(self):
        # an array is not a string
        with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
            StringTypeMatchesStrings.from_openapi_data_oapg(
                [
                ],
                _configuration=self._configuration
            )

    def test_a_boolean_is_not_a_string_fails(self):
        # a boolean is not a string
        with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
            StringTypeMatchesStrings.from_openapi_data_oapg(
                True,
                _configuration=self._configuration
            )

    def test_null_is_not_a_string_fails(self):
        # null is not a string
        with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
            StringTypeMatchesStrings.from_openapi_data_oapg(
                None,
                _configuration=self._configuration
            )

    def test_a_string_is_a_string_passes(self):
        # a string is a string
        StringTypeMatchesStrings.from_openapi_data_oapg(
            "foo",
            _configuration=self._configuration
        )


if __name__ == '__main__':
    unittest.main()
