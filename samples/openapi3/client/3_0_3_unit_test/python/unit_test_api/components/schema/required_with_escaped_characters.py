# coding: utf-8

"""
    openapi 3.0.3 sample spec

    sample spec for testing openapi functionality, built from json schema tests for draft6  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from unit_test_api import schemas  # noqa: F401


class RequiredWithEscapedCharacters(
    schemas.AnyTypeSchema,
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        # any type
        required = {
            "foo\tbar",
            "foo\nbar",
            "foo\fbar",
            "foo\rbar",
            "foo\"bar",
            "foo\\bar",
        }

    
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["foo\tbar"]) -> schemas.AnyTypeSchema: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["foo\nbar"]) -> schemas.AnyTypeSchema: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["foo\fbar"]) -> schemas.AnyTypeSchema: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["foo\rbar"]) -> schemas.AnyTypeSchema: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["foo\"bar"]) -> schemas.AnyTypeSchema: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["foo\\bar"]) -> schemas.AnyTypeSchema: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal["foo\tbar"],
            typing_extensions.Literal["foo\nbar"],
            typing_extensions.Literal["foo\fbar"],
            typing_extensions.Literal["foo\rbar"],
            typing_extensions.Literal["foo\"bar"],
            typing_extensions.Literal["foo\\bar"],
            str
        ]
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["foo\tbar"]) -> schemas.AnyTypeSchema: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["foo\nbar"]) -> schemas.AnyTypeSchema: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["foo\fbar"]) -> schemas.AnyTypeSchema: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["foo\rbar"]) -> schemas.AnyTypeSchema: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["foo\"bar"]) -> schemas.AnyTypeSchema: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["foo\\bar"]) -> schemas.AnyTypeSchema: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(
        self,
        name: typing.Union[
            typing_extensions.Literal["foo\tbar"],
            typing_extensions.Literal["foo\nbar"],
            typing_extensions.Literal["foo\fbar"],
            typing_extensions.Literal["foo\rbar"],
            typing_extensions.Literal["foo\"bar"],
            typing_extensions.Literal["foo\\bar"],
            str
        ]
    ):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'RequiredWithEscapedCharacters':
        return super().__new__(
            cls,
            *_args,
            _configuration=_configuration,
            **kwargs,
        )
