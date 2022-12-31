# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

import unittest

from petstore_api.components.schema.additional_properties_validator import AdditionalPropertiesValidator
from petstore_api import schemas, exceptions


class TestAdditionalPropertiesValidator(unittest.TestCase):
    """AdditionalPropertiesValidator unit test stubs"""

    def test_additional_properties_validator(self):
        with self.assertRaises(exceptions.ApiValueError):
            AdditionalPropertiesValidator(tooShort='ab')

        with self.assertRaises(exceptions.ApiValueError):
            AdditionalPropertiesValidator(tooLong='abcdef')

        inst = AdditionalPropertiesValidator(addProp='abc')
        add_prop = inst['addProp']
        assert add_prop == 'abc'
        assert isinstance(add_prop, str)
        assert isinstance(add_prop, schemas.AnyTypeSchema)
        assert isinstance(add_prop, AdditionalPropertiesValidator.Schema_.AllOf.classes[1].Schema_.AdditionalProperties)
        assert isinstance(add_prop, AdditionalPropertiesValidator.Schema_.AllOf.classes[2].Schema_.AdditionalProperties)
        assert not isinstance(add_prop, schemas.UnsetAnyTypeSchema)


if __name__ == '__main__':
    unittest.main()
