# coding: utf-8

"""
    openapi 3.0.3 sample spec

    sample spec for testing openapi functionality, built from json schema tests for draft6  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://openapi-generator.tech
"""

import unittest

import unit_test_api
from unit_test_api.components.schema.nul_characters_in_strings import NulCharactersInStrings
from unit_test_api import configuration


class TestNulCharactersInStrings(unittest.TestCase):
    """NulCharactersInStrings unit test stubs"""
    configuration_ = configuration.Configuration()

    def test_match_string_with_nul_passes(self):
        # match string with nul
        NulCharactersInStrings.from_openapi_data_(
            "hello\x00there",
            configuration_=self.configuration_
        )

    def test_do_not_match_string_lacking_nul_fails(self):
        # do not match string lacking nul
        with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
            NulCharactersInStrings.from_openapi_data_(
                "hellothere",
                configuration_=self.configuration_
            )


if __name__ == '__main__':
    unittest.main()
