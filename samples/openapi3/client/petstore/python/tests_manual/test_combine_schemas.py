# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import decimal
import unittest

import petstore_api
from petstore_api.components.schema.integer_enum_one_value_oapg import IntegerEnumOneValue
from petstore_api.components.schema.integer_enum_oapg import IntegerEnum
from petstore_api.components.schema.integer_max10_oapg import IntegerMax10
from petstore_api.schemas import Singleton


class TestCombineNonObjectSchemas(unittest.TestCase):

    def test_valid_enum_plus_prim(self):
        class EnumPlusPrim(IntegerMax10, IntegerEnumOneValue):
            pass

        # order of base classes does not matter
        class EnumPlusPrim(IntegerEnumOneValue, IntegerMax10):
            pass

        enum_value = EnumPlusPrim.POSITIVE_0
        assert isinstance(enum_value, EnumPlusPrim)
        assert isinstance(enum_value, Singleton)
        assert isinstance(enum_value, decimal.Decimal)
        # we can access this enum from our class
        assert EnumPlusPrim.POSITIVE_0 == 0

        # invalid value throws an exception
        with self.assertRaises(petstore_api.ApiValueError):
            EnumPlusPrim(9)

        # valid value succeeds
        val = EnumPlusPrim(0)
        assert val == 0
        assert isinstance(val, EnumPlusPrim)
        assert isinstance(val, Singleton)
        assert isinstance(val, decimal.Decimal)

    def test_valid_enum_plus_enum(self):
        class IntegerOneEnum(IntegerEnumOneValue, IntegerEnum):
            pass

        # order of base classes does not matter
        class IntegerOneEnum(IntegerEnum, IntegerEnumOneValue):
            pass

        enum_value = IntegerOneEnum.POSITIVE_0
        assert isinstance(enum_value, IntegerOneEnum)
        assert isinstance(enum_value, Singleton)
        assert isinstance(enum_value, decimal.Decimal)
        # we can access this enum from our class
        assert IntegerOneEnum.POSITIVE_0 == 0


if __name__ == '__main__':
    unittest.main()
