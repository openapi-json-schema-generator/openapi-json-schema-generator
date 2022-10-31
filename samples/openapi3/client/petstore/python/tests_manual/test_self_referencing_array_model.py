# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""

import unittest

import petstore_api
from petstore_api.components.schema.self_referencing_array_model import SelfReferencingArrayModel


class TestSelfReferencingArrayModel(unittest.TestCase):
    """SelfReferencingArrayModel unit test stubs"""
    def test_instantiation(self):
        inst = SelfReferencingArrayModel([
            SelfReferencingArrayModel([])
        ])
        assert inst == (
            (),
        )

        invalid_type_args = [
            1,
            [
                1,
            ],
            [
                [1]
            ]
        ]
        # error when wrong type passed in
        with self.assertRaises(petstore_api.ApiTypeError):
            for invalid_type_arg in invalid_type_args:
                SelfReferencingArrayModel(invalid_type_arg)

if __name__ == '__main__':
    unittest.main()
