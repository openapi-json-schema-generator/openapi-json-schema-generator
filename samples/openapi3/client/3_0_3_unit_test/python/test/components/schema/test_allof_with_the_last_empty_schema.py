# coding: utf-8

"""
    openapi 3.0.3 sample spec

    sample spec for testing openapi functionality, built from json schema tests for draft6  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://openapi-generator.tech
"""

import unittest

import unit_test_api
from unit_test_api.components.schema.allof_with_the_last_empty_schema import AllofWithTheLastEmptySchema
from unit_test_api import configuration


class TestAllofWithTheLastEmptySchema(unittest.TestCase):
    """AllofWithTheLastEmptySchema unit test stubs"""
    configuration_ = configuration.Configuration()

    def test_string_is_invalid_fails(self):
        # string is invalid
        with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
            AllofWithTheLastEmptySchema.from_openapi_data_(
                "foo",
                configuration_=self.configuration_
            )

    def test_number_is_valid_passes(self):
        # number is valid
        AllofWithTheLastEmptySchema.from_openapi_data_(
            1,
            configuration_=self.configuration_
        )


if __name__ == '__main__':
    unittest.main()
