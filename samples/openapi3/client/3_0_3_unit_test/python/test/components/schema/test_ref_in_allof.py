# coding: utf-8

"""
    openapi 3.0.3 sample spec
    sample spec for testing openapi functionality, built from json schema tests for draft6  # noqa: E501
    The version of the OpenAPI document: 0.0.1
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

import unittest

import unit_test_api
from unit_test_api.components.schema.ref_in_allof import RefInAllof
from unit_test_api.configurations import schema_configuration


class TestRefInAllof(unittest.TestCase):
    """RefInAllof unit test stubs"""
    configuration = schema_configuration.SchemaConfiguration()

    def test_property_named_ref_valid_passes(self):
        # property named $ref valid
        RefInAllof.validate(
            {
                "$ref":
                    "a",
            },
            configuration=self.configuration
        )

    def test_property_named_ref_invalid_fails(self):
        # property named $ref invalid
        with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
            RefInAllof.validate(
                {
                    "$ref":
                        2,
                },
                configuration=self.configuration
            )


if __name__ == '__main__':
    unittest.main()
