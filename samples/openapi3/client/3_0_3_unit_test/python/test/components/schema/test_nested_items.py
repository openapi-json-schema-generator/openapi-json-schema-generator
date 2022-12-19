# coding: utf-8

"""
    openapi 3.0.3 sample spec

    sample spec for testing openapi functionality, built from json schema tests for draft6  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://openapi-generator.tech
"""

import unittest

import unit_test_api
from unit_test_api.components.schema.nested_items import NestedItems
from unit_test_api import configuration


class TestNestedItems(unittest.TestCase):
    """NestedItems unit test stubs"""
    _configuration = configuration.Configuration()

    def test_valid_nested_array_passes(self):
        # valid nested array
        NestedItems.from_openapi_data_oapg(
            [
                [
                    [
                        [
                            1,
                        ],
                    ],
                    [
                        [
                            2,
                        ],
                        [
                            3,
                        ],
                    ],
                ],
                [
                    [
                        [
                            4,
                        ],
                        [
                            5,
                        ],
                        [
                            6,
                        ],
                    ],
                ],
            ],
            _configuration=self._configuration
        )

    def test_nested_array_with_invalid_type_fails(self):
        # nested array with invalid type
        with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
            NestedItems.from_openapi_data_oapg(
                [
                    [
                        [
                            [
                                "1",
                            ],
                        ],
                        [
                            [
                                2,
                            ],
                            [
                                3,
                            ],
                        ],
                    ],
                    [
                        [
                            [
                                4,
                            ],
                            [
                                5,
                            ],
                            [
                                6,
                            ],
                        ],
                    ],
                ],
                _configuration=self._configuration
            )

    def test_not_deep_enough_fails(self):
        # not deep enough
        with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
            NestedItems.from_openapi_data_oapg(
                [
                    [
                        [
                            1,
                        ],
                        [
                            2,
                        ],
                        [
                            3,
                        ],
                    ],
                    [
                        [
                            4,
                        ],
                        [
                            5,
                        ],
                        [
                            6,
                        ],
                    ],
                ],
                _configuration=self._configuration
            )


if __name__ == '__main__':
    unittest.main()
