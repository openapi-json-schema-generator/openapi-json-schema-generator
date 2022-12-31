# coding: utf-8

"""
    openapi 3.0.3 sample spec

    sample spec for testing openapi functionality, built from json schema tests for draft6  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

import unittest

import unit_test_api
from unit_test_api.components.schema.not_more_complex_schema import NotMoreComplexSchema
from unit_test_api import configuration


class TestNotMoreComplexSchema(unittest.TestCase):
    """NotMoreComplexSchema unit test stubs"""
    configuration_ = configuration.Configuration()

    def test_other_match_passes(self):
        # other match
        NotMoreComplexSchema.from_openapi_data_(
            {
                "foo":
                    1,
            },
            configuration_=self.configuration_
        )

    def test_mismatch_fails(self):
        # mismatch
        with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
            NotMoreComplexSchema.from_openapi_data_(
                {
                    "foo":
                        "bar",
                },
                configuration_=self.configuration_
            )

    def test_match_passes(self):
        # match
        NotMoreComplexSchema.from_openapi_data_(
            1,
            configuration_=self.configuration_
        )


if __name__ == '__main__':
    unittest.main()
