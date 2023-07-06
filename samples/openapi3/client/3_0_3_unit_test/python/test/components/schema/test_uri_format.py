# coding: utf-8

"""
    openapi 3.0.3 sample spec
    sample spec for testing openapi functionality, built from json schema tests for draft6  # noqa: E501
    The version of the OpenAPI document: 0.0.1
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

import unittest

import unit_test_api
from unit_test_api.components.schema.uri_format import UriFormat
from unit_test_api.configurations import schema_configuration


class TestUriFormat(unittest.TestCase):
    """UriFormat unit test stubs"""
    configuration = schema_configuration.SchemaConfiguration()

    def test_all_string_formats_ignore_objects_passes(self):
        # all string formats ignore objects
        UriFormat.validate(
            {
            },
            configuration=self.configuration
        )

    def test_all_string_formats_ignore_booleans_passes(self):
        # all string formats ignore booleans
        UriFormat.validate(
            False,
            configuration=self.configuration
        )

    def test_all_string_formats_ignore_integers_passes(self):
        # all string formats ignore integers
        UriFormat.validate(
            12,
            configuration=self.configuration
        )

    def test_all_string_formats_ignore_floats_passes(self):
        # all string formats ignore floats
        UriFormat.validate(
            13.7,
            configuration=self.configuration
        )

    def test_all_string_formats_ignore_arrays_passes(self):
        # all string formats ignore arrays
        UriFormat.validate(
            [
            ],
            configuration=self.configuration
        )

    def test_all_string_formats_ignore_nulls_passes(self):
        # all string formats ignore nulls
        UriFormat.validate(
            None,
            configuration=self.configuration
        )


if __name__ == '__main__':
    unittest.main()
