# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
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

from petstore_api import schemas  # noqa: F401


class ApplicationJson(
    schemas.ListSchema
):


    class Schema_:
        types = {tuple}
        
        @staticmethod
        def items() -> typing.Type['user.User']:
            return user.User

    def __new__(
        cls,
        _arg: typing.Union[typing.Tuple['user.User'], typing.List['user.User']],
        _configuration: typing.Optional[schemas.configuration_module.Configuration] = None,
    ) -> 'ApplicationJson':
        return super().__new__(
            cls,
            _arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'user.User':
        return super().__getitem__(i)

from petstore_api.components.schema import user
