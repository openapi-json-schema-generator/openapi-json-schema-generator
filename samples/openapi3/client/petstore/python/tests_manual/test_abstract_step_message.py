# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""

import unittest

import petstore_api
from petstore_api.model.abstract_step_message import AbstractStepMessage


class TestAbstractStepMessage(unittest.TestCase):
    """AbstractStepMessage unit test stubs"""

    def test_model_instantiation(self):
        inst = AbstractStepMessage(
            discriminator='AbstractStepMessage',
            sequenceNumber=1,
            description='some description'
        )
        assert inst == {
            'discriminator': 'AbstractStepMessage',
            'sequenceNumber': 1,
            'description': 'some description'
        }

        # without the above required properties an exception is thrown
        invalid_kwargs = [
            {
                'sequenceNumber': 1,
                'description': 'some description'
            },
            {
                'discriminator': 'AbstractStepMessage',
                'description': 'some description'
            },
            {
                'discriminator': 'AbstractStepMessage',
                'sequenceNumber': 1,
            },
        ]
        for invalid_kwarg in invalid_kwargs:
            with self.assertRaises(petstore_api.exceptions.ApiTypeError):
                AbstractStepMessage(**invalid_kwarg)

if __name__ == '__main__':
    unittest.main()
