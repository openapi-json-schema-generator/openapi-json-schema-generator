# coding: utf-8

"""
    openapi 3.0.3 sample spec

    sample spec for testing openapi functionality, built from json schema tests for draft6  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://openapi-generator.tech
"""

import unittest

import unit_test_api
from unit_test_api.components.schema.ref_in_property import RefInProperty
from unit_test_api import configuration


class TestRefInProperty(unittest.TestCase):
    """RefInProperty unit test stubs"""
    _configuration = configuration.Configuration()

    def test_property_named_ref_valid_passes(self):
        # property named $ref valid
        RefInProperty.from_openapi_data_oapg(
            {
                "a":
                    {
                        "$ref":
                            "a",
                    },
            },
            _configuration=self._configuration
        )

    def test_property_named_ref_invalid_fails(self):
        # property named $ref invalid
        with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
            RefInProperty.from_openapi_data_oapg(
                {
                    "a":
                        {
                            "$ref":
                                2,
                        },
                },
                _configuration=self._configuration
            )


if __name__ == '__main__':
    unittest.main()
