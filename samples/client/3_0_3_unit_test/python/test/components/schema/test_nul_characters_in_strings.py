# coding: utf-8

"""
    openapi 3.0.3 sample spec
    sample spec for testing openapi functionality, built from json schema tests for draft6  # noqa: E501
    The version of the OpenAPI document: 0.0.1
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

import unittest

import unit_test_api
from unit_test_api.components.schema.nul_characters_in_strings import NulCharactersInStrings
from unit_test_api.configurations import schema_configuration


class TestNulCharactersInStrings(unittest.TestCase):
    """NulCharactersInStrings unit test stubs"""
    configuration = schema_configuration.SchemaConfiguration(
        disabled_json_schema_keywords={'format'}
    )

    def test_match_string_with_nul_passes(self):
        # match string with nul
        NulCharactersInStrings.validate(
            "hello\x00there",
            configuration=self.configuration
        )

    def test_do_not_match_string_lacking_nul_fails(self):
        # do not match string lacking nul
        with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
            NulCharactersInStrings.validate(
                "hellothere",
                configuration=self.configuration
            )


if __name__ == '__main__':
    unittest.main()
