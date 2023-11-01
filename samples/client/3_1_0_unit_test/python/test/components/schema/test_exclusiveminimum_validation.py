# coding: utf-8

"""
    openapi 3.1.0 sample spec
    sample spec for testing openapi functionality, built from json schema tests for draft2020-12  # noqa: E501
    The version of the OpenAPI document: 0.0.1
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

import unittest

import unit_test_api
from unit_test_api.components.schema.exclusiveminimum_validation import ExclusiveminimumValidation
from unit_test_api.configurations import schema_configuration


class TestExclusiveminimumValidation(unittest.TestCase):
    """ExclusiveminimumValidation unit test stubs"""
    configuration = schema_configuration.SchemaConfiguration(
        disabled_json_schema_keywords={'format'}
    )

    def test_above_the_exclusiveminimum_is_valid_passes(self):
        # above the exclusiveMinimum is valid
        ExclusiveminimumValidation.validate(
            1.2,
            configuration=self.configuration
        )

    def test_below_the_exclusiveminimum_is_invalid_fails(self):
        # below the exclusiveMinimum is invalid
        with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
            ExclusiveminimumValidation.validate(
                0.6,
                configuration=self.configuration
            )

    def test_boundary_point_is_invalid_fails(self):
        # boundary point is invalid
        with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
            ExclusiveminimumValidation.validate(
                1.1,
                configuration=self.configuration
            )

    def test_ignores_non_numbers_passes(self):
        # ignores non-numbers
        ExclusiveminimumValidation.validate(
            "x",
            configuration=self.configuration
        )


if __name__ == '__main__':
    unittest.main()
