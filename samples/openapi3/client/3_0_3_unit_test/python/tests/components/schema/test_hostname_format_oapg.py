# coding: utf-8

"""
    openapi 3.0.3 sample spec

    sample spec for testing openapi functionality, built from json schema tests for draft6  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://openapi-generator.tech
"""

import unittest

import unit_test_api
from unit_test_api.components.schema.hostname_format_oapg import HostnameFormat
from unit_test_api import configuration


class TestHostnameFormat(unittest.TestCase):
    """HostnameFormat unit test stubs"""
    _configuration = configuration.Configuration()

    def test_all_string_formats_ignore_objects_passes(self):
        # all string formats ignore objects
        HostnameFormat.from_openapi_data_oapg(
            {
            },
            _configuration=self._configuration
        )

    def test_all_string_formats_ignore_booleans_passes(self):
        # all string formats ignore booleans
        HostnameFormat.from_openapi_data_oapg(
            False,
            _configuration=self._configuration
        )

    def test_all_string_formats_ignore_integers_passes(self):
        # all string formats ignore integers
        HostnameFormat.from_openapi_data_oapg(
            12,
            _configuration=self._configuration
        )

    def test_all_string_formats_ignore_floats_passes(self):
        # all string formats ignore floats
        HostnameFormat.from_openapi_data_oapg(
            13.7,
            _configuration=self._configuration
        )

    def test_all_string_formats_ignore_arrays_passes(self):
        # all string formats ignore arrays
        HostnameFormat.from_openapi_data_oapg(
            [
            ],
            _configuration=self._configuration
        )

    def test_all_string_formats_ignore_nulls_passes(self):
        # all string formats ignore nulls
        HostnameFormat.from_openapi_data_oapg(
            None,
            _configuration=self._configuration
        )


if __name__ == '__main__':
    unittest.main()
