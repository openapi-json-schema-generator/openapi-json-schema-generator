# coding: utf-8

"""
    openapi 3.0.3 sample spec
    sample spec for testing openapi functionality, built from json schema tests for draft6  # noqa: E501
    The version of the OpenAPI document: 0.0.1
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

import unittest

import unit_test_api
from unit_test_api.components.schema.enum_with1_does_not_match_true import EnumWith1DoesNotMatchTrue
from unit_test_api.configurations import schema_configuration


class TestEnumWith1DoesNotMatchTrue(unittest.TestCase):
    """EnumWith1DoesNotMatchTrue unit test stubs"""
    configuration = schema_configuration.SchemaConfiguration(
        disabled_json_schema_keywords={'format'}
    )

    def test_true_is_invalid_fails(self):
        # true is invalid
        with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
            EnumWith1DoesNotMatchTrue.validate(
                True,
                configuration=self.configuration
            )

    def test_integer_one_is_valid_passes(self):
        # integer one is valid
        EnumWith1DoesNotMatchTrue.validate(
            1,
            configuration=self.configuration
        )

    def test_float_one_is_valid_passes(self):
        # float one is valid
        EnumWith1DoesNotMatchTrue.validate(
            1.0,
            configuration=self.configuration
        )


if __name__ == '__main__':
    unittest.main()
