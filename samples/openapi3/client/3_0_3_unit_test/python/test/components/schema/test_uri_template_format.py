# coding: utf-8

"""
    openapi 3.0.3 sample spec

    sample spec for testing openapi functionality, built from json schema tests for draft6  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://openapi-generator.tech
"""

import unittest

import unit_test_api
from unit_test_api.components.schema.uri_template_format import UriTemplateFormat
from unit_test_api import configuration


class TestUriTemplateFormat(unittest.TestCase):
    """UriTemplateFormat unit test stubs"""
    configuration_ = configuration.Configuration()

    def test_all_string_formats_ignore_objects_passes(self):
        # all string formats ignore objects
        UriTemplateFormat.from_openapi_data_(
            {
            },
            configuration_=self.configuration_
        )

    def test_all_string_formats_ignore_booleans_passes(self):
        # all string formats ignore booleans
        UriTemplateFormat.from_openapi_data_(
            False,
            configuration_=self.configuration_
        )

    def test_all_string_formats_ignore_integers_passes(self):
        # all string formats ignore integers
        UriTemplateFormat.from_openapi_data_(
            12,
            configuration_=self.configuration_
        )

    def test_all_string_formats_ignore_floats_passes(self):
        # all string formats ignore floats
        UriTemplateFormat.from_openapi_data_(
            13.7,
            configuration_=self.configuration_
        )

    def test_all_string_formats_ignore_arrays_passes(self):
        # all string formats ignore arrays
        UriTemplateFormat.from_openapi_data_(
            [
            ],
            configuration_=self.configuration_
        )

    def test_all_string_formats_ignore_nulls_passes(self):
        # all string formats ignore nulls
        UriTemplateFormat.from_openapi_data_(
            None,
            configuration_=self.configuration_
        )


if __name__ == '__main__':
    unittest.main()
