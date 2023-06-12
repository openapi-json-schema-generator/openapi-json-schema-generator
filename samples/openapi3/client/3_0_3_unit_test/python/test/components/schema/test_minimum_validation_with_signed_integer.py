# coding: utf-8

"""
    openapi 3.0.3 sample spec
    sample spec for testing openapi functionality, built from json schema tests for draft6  # noqa: E501
    The version of the OpenAPI document: 0.0.1
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

import unittest

import unit_test_api
from unit_test_api.components.schema.minimum_validation_with_signed_integer import MinimumValidationWithSignedInteger
from unit_test_api.configurations import schema_configuration


class TestMinimumValidationWithSignedInteger(unittest.TestCase):
    """MinimumValidationWithSignedInteger unit test stubs"""
    configuration = schema_configuration.SchemaConfiguration()

    def test_boundary_point_is_valid_passes(self):
        # boundary point is valid
        MinimumValidationWithSignedInteger(
            -2,
            configuration=self.configuration
        )

    def test_positive_above_the_minimum_is_valid_passes(self):
        # positive above the minimum is valid
        MinimumValidationWithSignedInteger(
            0,
            configuration=self.configuration
        )

    def test_int_below_the_minimum_is_invalid_fails(self):
        # int below the minimum is invalid
        with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
            MinimumValidationWithSignedInteger(
                -3,
                configuration=self.configuration
            )

    def test_float_below_the_minimum_is_invalid_fails(self):
        # float below the minimum is invalid
        with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
            MinimumValidationWithSignedInteger(
                -2.0001,
                configuration=self.configuration
            )

    def test_boundary_point_with_float_is_valid_passes(self):
        # boundary point with float is valid
        MinimumValidationWithSignedInteger(
            -2.0,
            configuration=self.configuration
        )

    def test_negative_above_the_minimum_is_valid_passes(self):
        # negative above the minimum is valid
        MinimumValidationWithSignedInteger(
            -1,
            configuration=self.configuration
        )

    def test_ignores_non_numbers_passes(self):
        # ignores non-numbers
        MinimumValidationWithSignedInteger(
            "x",
            configuration=self.configuration
        )


if __name__ == '__main__':
    unittest.main()
