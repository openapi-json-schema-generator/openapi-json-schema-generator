# coding: utf-8

"""
    openapi 3.0.3 sample spec

    sample spec for testing openapi functionality, built from json schema tests for draft6  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://openapi-generator.tech
"""

import unittest

import unit_test_api
from unit_test_api.components.schema.oneof import Oneof
from unit_test_api import configuration


class TestOneof(unittest.TestCase):
    """Oneof unit test stubs"""
    _configuration = configuration.Configuration()

    def test_second_oneof_valid_passes(self):
        # second oneOf valid
        Oneof.from_openapi_data_oapg(
            2.5,
            _configuration=self._configuration
        )

    def test_both_oneof_valid_fails(self):
        # both oneOf valid
        with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
            Oneof.from_openapi_data_oapg(
                3,
                _configuration=self._configuration
            )

    def test_first_oneof_valid_passes(self):
        # first oneOf valid
        Oneof.from_openapi_data_oapg(
            1,
            _configuration=self._configuration
        )

    def test_neither_oneof_valid_fails(self):
        # neither oneOf valid
        with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
            Oneof.from_openapi_data_oapg(
                1.5,
                _configuration=self._configuration
            )


if __name__ == '__main__':
    unittest.main()
