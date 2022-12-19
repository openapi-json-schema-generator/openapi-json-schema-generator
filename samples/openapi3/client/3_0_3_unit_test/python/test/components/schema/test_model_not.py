# coding: utf-8

"""
    openapi 3.0.3 sample spec

    sample spec for testing openapi functionality, built from json schema tests for draft6  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://openapi-generator.tech
"""

import unittest

import unit_test_api
from unit_test_api.components.schema.model_not import ModelNot
from unit_test_api import configuration


class TestModelNot(unittest.TestCase):
    """ModelNot unit test stubs"""
    _configuration = configuration.Configuration()

    def test_allowed_passes(self):
        # allowed
        ModelNot.from_openapi_data_oapg(
            "foo",
            _configuration=self._configuration
        )

    def test_disallowed_fails(self):
        # disallowed
        with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
            ModelNot.from_openapi_data_oapg(
                1,
                _configuration=self._configuration
            )


if __name__ == '__main__':
    unittest.main()
