# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

import unittest

from petstore_api import schemas, exceptions
from petstore_api.components.schema.uuid_string import UUIDString
import uuid


class TestUUIDString(unittest.TestCase):
    """UUIDString unit test stubs"""

    def test_UUIDString(self):
        """Test UUIDString"""
        uuid_value = '12345678-1234-5678-1234-567812345678'
        u = UUIDString.validate(uuid_value)
        self.assertEqual(u, uuid_value)
        self.assertTrue(isinstance(u, str))
        self.assertEqual(schemas.as_uuid(u), uuid.UUID(uuid_value))

        # passing in a uuid also works
        u = UUIDString.validate(uuid.UUID(uuid_value))
        self.assertEqual(u, uuid_value)
        self.assertTrue(isinstance(u, str))
        self.assertEqual(schemas.as_uuid(u), uuid.UUID(uuid_value))

        # an invalid value does not work
        with self.assertRaises(exceptions.ApiValueError):
            UUIDString.validate('1')


if __name__ == '__main__':
    unittest.main()
