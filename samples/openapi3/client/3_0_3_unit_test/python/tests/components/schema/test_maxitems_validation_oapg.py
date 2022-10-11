# coding: utf-8

"""
    openapi 3.0.3 sample spec

    sample spec for testing openapi functionality, built from json schema tests for draft6  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://openapi-generator.tech
"""

import unittest

import unit_test_api
from unit_test_api.components.schema.maxitems_validation_oapg import MaxitemsValidation
from unit_test_api import configuration


class TestMaxitemsValidation(unittest.TestCase):
    """MaxitemsValidation unit test stubs"""
    _configuration = configuration.Configuration()

    def test_too_long_is_invalid_fails(self):
        # too long is invalid
        with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
            MaxitemsValidation.from_openapi_data_oapg(
                [
                    1,
                    2,
                    3,
                ],
                _configuration=self._configuration
            )

    def test_ignores_non_arrays_passes(self):
        # ignores non-arrays
        MaxitemsValidation.from_openapi_data_oapg(
            "foobar",
            _configuration=self._configuration
        )

    def test_shorter_is_valid_passes(self):
        # shorter is valid
        MaxitemsValidation.from_openapi_data_oapg(
            [
                1,
            ],
            _configuration=self._configuration
        )

    def test_exact_length_is_valid_passes(self):
        # exact length is valid
        MaxitemsValidation.from_openapi_data_oapg(
            [
                1,
                2,
            ],
            _configuration=self._configuration
        )


if __name__ == '__main__':
    unittest.main()
