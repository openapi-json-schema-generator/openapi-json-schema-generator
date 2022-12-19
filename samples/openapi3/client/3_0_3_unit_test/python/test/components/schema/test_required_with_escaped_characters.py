# coding: utf-8

"""
    openapi 3.0.3 sample spec

    sample spec for testing openapi functionality, built from json schema tests for draft6  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://openapi-generator.tech
"""

import unittest

import unit_test_api
from unit_test_api.components.schema.required_with_escaped_characters import RequiredWithEscapedCharacters
from unit_test_api import configuration


class TestRequiredWithEscapedCharacters(unittest.TestCase):
    """RequiredWithEscapedCharacters unit test stubs"""
    _configuration = configuration.Configuration()

    def test_object_with_some_properties_missing_is_invalid_fails(self):
        # object with some properties missing is invalid
        with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
            RequiredWithEscapedCharacters.from_openapi_data_oapg(
                {
                    "foo\nbar":
                        "1",
                    "foo\"bar":
                        "1",
                },
                _configuration=self._configuration
            )

    def test_object_with_all_properties_present_is_valid_passes(self):
        # object with all properties present is valid
        RequiredWithEscapedCharacters.from_openapi_data_oapg(
            {
                "foo\nbar":
                    1,
                "foo\"bar":
                    1,
                "foo\\bar":
                    1,
                "foo\rbar":
                    1,
                "foo\tbar":
                    1,
                "foo\fbar":
                    1,
            },
            _configuration=self._configuration
        )


if __name__ == '__main__':
    unittest.main()
