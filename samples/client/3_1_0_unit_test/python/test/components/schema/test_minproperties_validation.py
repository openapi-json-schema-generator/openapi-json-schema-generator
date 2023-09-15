# coding: utf-8

"""
    openapi 3.1.0 sample spec
    sample spec for testing openapi functionality, built from json schema tests for draft2020-12  # noqa: E501
    The version of the OpenAPI document: 0.0.1
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

import unittest

import unit_test_api
from unit_test_api.components.schema.minproperties_validation import MinpropertiesValidation
from unit_test_api.configurations import schema_configuration


class TestMinpropertiesValidation(unittest.TestCase):
    """MinpropertiesValidation unit test stubs"""
    configuration = schema_configuration.SchemaConfiguration()

    def test_ignores_arrays_passes(self):
        # ignores arrays
        MinpropertiesValidation.validate(
            [
            ],
            configuration=self.configuration
        )

    def test_ignores_other_non_objects_passes(self):
        # ignores other non-objects
        MinpropertiesValidation.validate(
            12,
            configuration=self.configuration
        )

    def test_too_short_is_invalid_fails(self):
        # too short is invalid
        with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
            MinpropertiesValidation.validate(
                {
                },
                configuration=self.configuration
            )

    def test_ignores_strings_passes(self):
        # ignores strings
        MinpropertiesValidation.validate(
            "",
            configuration=self.configuration
        )

    def test_longer_is_valid_passes(self):
        # longer is valid
        MinpropertiesValidation.validate(
            {
                "foo":
                    1,
                "bar":
                    2,
            },
            configuration=self.configuration
        )

    def test_exact_length_is_valid_passes(self):
        # exact length is valid
        MinpropertiesValidation.validate(
            {
                "foo":
                    1,
            },
            configuration=self.configuration
        )


if __name__ == '__main__':
    unittest.main()
