# coding: utf-8

"""
    openapi 3.0.3 sample spec

    sample spec for testing openapi functionality, built from json schema tests for draft6  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

import unittest

import unit_test_api
from unit_test_api.components.schema.additionalproperties_are_allowed_by_default import AdditionalpropertiesAreAllowedByDefault
from unit_test_api import configuration


class TestAdditionalpropertiesAreAllowedByDefault(unittest.TestCase):
    """AdditionalpropertiesAreAllowedByDefault unit test stubs"""
    configuration_ = configuration.Configuration()

    def test_additional_properties_are_allowed_passes(self):
        # additional properties are allowed
        AdditionalpropertiesAreAllowedByDefault.from_openapi_data_(
            {
                "foo":
                    1,
                "bar":
                    2,
                "quux":
                    True,
            },
            configuration_=self.configuration_
        )


if __name__ == '__main__':
    unittest.main()
