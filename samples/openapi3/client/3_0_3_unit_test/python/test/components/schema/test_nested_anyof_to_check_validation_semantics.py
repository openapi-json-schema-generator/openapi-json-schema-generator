# coding: utf-8

"""
    openapi 3.0.3 sample spec

    sample spec for testing openapi functionality, built from json schema tests for draft6  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://openapi-generator.tech
"""

import unittest

import unit_test_api
from unit_test_api.components.schema.nested_anyof_to_check_validation_semantics import NestedAnyofToCheckValidationSemantics
from unit_test_api import configuration


class TestNestedAnyofToCheckValidationSemantics(unittest.TestCase):
    """NestedAnyofToCheckValidationSemantics unit test stubs"""
    _configuration = configuration.Configuration()

    def test_anything_non_null_is_invalid_fails(self):
        # anything non-null is invalid
        with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
            NestedAnyofToCheckValidationSemantics.from_openapi_data_(
                123,
                _configuration=self._configuration
            )

    def test_null_is_valid_passes(self):
        # null is valid
        NestedAnyofToCheckValidationSemantics.from_openapi_data_(
            None,
            _configuration=self._configuration
        )


if __name__ == '__main__':
    unittest.main()
