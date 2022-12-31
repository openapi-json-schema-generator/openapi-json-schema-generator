# coding: utf-8

"""
    openapi 3.0.3 sample spec

    sample spec for testing openapi functionality, built from json schema tests for draft6  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

import unittest

import unit_test_api
from unit_test_api.components.schema.forbidden_property import ForbiddenProperty
from unit_test_api import configuration


class TestForbiddenProperty(unittest.TestCase):
    """ForbiddenProperty unit test stubs"""
    configuration_ = configuration.Configuration()

    def test_property_present_fails(self):
        # property present
        with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
            ForbiddenProperty.from_openapi_data_(
                {
                    "foo":
                        1,
                    "bar":
                        2,
                },
                configuration_=self.configuration_
            )

    def test_property_absent_passes(self):
        # property absent
        ForbiddenProperty.from_openapi_data_(
            {
                "bar":
                    1,
                "baz":
                    2,
            },
            configuration_=self.configuration_
        )


if __name__ == '__main__':
    unittest.main()
