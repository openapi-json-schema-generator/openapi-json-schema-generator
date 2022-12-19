# coding: utf-8

"""
    openapi 3.0.3 sample spec

    sample spec for testing openapi functionality, built from json schema tests for draft6  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://openapi-generator.tech
"""

import unittest

import unit_test_api
from unit_test_api.components.schema. import RequiredDefaultValidation
from unit_test_api import configuration


class TestRequiredDefaultValidation(unittest.TestCase):
    """RequiredDefaultValidation unit test stubs"""
    _configuration = configuration.Configuration()

    def test_not_required_by_default_passes(self):
        # not required by default
        RequiredDefaultValidation.from_openapi_data_oapg(
            {
            },
            _configuration=self._configuration
        )


if __name__ == '__main__':
    unittest.main()
