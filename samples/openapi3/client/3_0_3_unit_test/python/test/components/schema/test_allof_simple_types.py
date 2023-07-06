# coding: utf-8

"""
    openapi 3.0.3 sample spec
    sample spec for testing openapi functionality, built from json schema tests for draft6  # noqa: E501
    The version of the OpenAPI document: 0.0.1
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

import unittest

import unit_test_api
from unit_test_api.components.schema.allof_simple_types import AllofSimpleTypes
from unit_test_api.configurations import schema_configuration


class TestAllofSimpleTypes(unittest.TestCase):
    """AllofSimpleTypes unit test stubs"""
    configuration = schema_configuration.SchemaConfiguration()

    def test_valid_passes(self):
        # valid
        AllofSimpleTypes.validate(
            25,
            configuration=self.configuration
        )

    def test_mismatch_one_fails(self):
        # mismatch one
        with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
            AllofSimpleTypes.validate(
                35,
                configuration=self.configuration
            )


if __name__ == '__main__':
    unittest.main()
