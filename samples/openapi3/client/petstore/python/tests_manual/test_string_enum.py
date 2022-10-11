# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import petstore_api
from petstore_api.components.schema.string_enum_oapg import StringEnum
from petstore_api.schemas import Singleton, NoneClass


class TestStringEnum(unittest.TestCase):
    """StringEnum unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testStringEnum(self):
        """Test StringEnum"""
        inst = StringEnum(None)
        assert isinstance(inst, StringEnum)
        assert isinstance(inst, NoneClass)
        assert repr(inst) == '<DynamicSchema: None>'

        inst = StringEnum('approved')
        assert isinstance(inst, StringEnum)
        assert isinstance(inst, Singleton)
        assert isinstance(inst, str)
        assert inst == 'approved'
        assert repr(inst) == "<DynamicSchema: 'approved'>"

        with self.assertRaises(petstore_api.ApiValueError):
            StringEnum('garbage')

        # make sure that we can access its allowed_values
        assert isinstance(StringEnum.NONE, NoneClass)
        assert StringEnum.PLACED == 'placed'
        assert StringEnum.APPROVED == 'approved'
        assert StringEnum.DELIVERED == 'delivered'
        assert StringEnum.DOUBLE_QUOTE_WITH_NEWLINE == "double quote \n with newline"
        assert StringEnum.MULTIPLE_LINES == "multiple\nlines"
        assert StringEnum.SINGLE_QUOTED == "single quoted"


if __name__ == '__main__':
    unittest.main()
