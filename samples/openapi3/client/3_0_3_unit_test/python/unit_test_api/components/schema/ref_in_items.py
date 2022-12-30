# coding: utf-8

"""
    openapi 3.0.3 sample spec

    sample spec for testing openapi functionality, built from json schema tests for draft6  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://openapi-generator.tech
"""

import datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from unit_test_api import schemas  # noqa: F401


class RefInItems(
    schemas.ListSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class Schema_:
        types = {tuple}
        
        @staticmethod
        def items() -> typing.Type['property_named_ref_that_is_not_a_reference.PropertyNamedRefThatIsNotAReference']:
            return property_named_ref_that_is_not_a_reference.PropertyNamedRefThatIsNotAReference

    def __new__(
        cls,
        arg_: typing.Union[typing.Tuple['property_named_ref_that_is_not_a_reference.PropertyNamedRefThatIsNotAReference'], typing.List['property_named_ref_that_is_not_a_reference.PropertyNamedRefThatIsNotAReference']],
        configuration_: typing.Optional[schemas.configuration_module.Configuration] = None,
    ) -> 'RefInItems':
        return super().__new__(
            cls,
            arg_,
            configuration_=configuration_,
        )

    def __getitem__(self, i: int) -> 'property_named_ref_that_is_not_a_reference.PropertyNamedRefThatIsNotAReference':
        return super().__getitem__(i)

from unit_test_api.components.schema import property_named_ref_that_is_not_a_reference
