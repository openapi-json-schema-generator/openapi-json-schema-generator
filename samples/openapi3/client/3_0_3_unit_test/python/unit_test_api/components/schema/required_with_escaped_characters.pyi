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


class RequiredWithEscapedCharacters(
    schemas.AnyTypeSchema,
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class Schema_:
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
    def get_item_(self, name: typing_extensions.Literal["foo\tbar"]) -> schemas.AnyTypeSchema: ...
    
    @typing.overload
    def get_item_(self, name: typing_extensions.Literal["foo\nbar"]) -> schemas.AnyTypeSchema: ...
    
    @typing.overload
    def get_item_(self, name: typing_extensions.Literal["foo\fbar"]) -> schemas.AnyTypeSchema: ...
    
    @typing.overload
    def get_item_(self, name: typing_extensions.Literal["foo\rbar"]) -> schemas.AnyTypeSchema: ...
    
    @typing.overload
    def get_item_(self, name: typing_extensions.Literal["foo\"bar"]) -> schemas.AnyTypeSchema: ...
    
    @typing.overload
    def get_item_(self, name: typing_extensions.Literal["foo\\bar"]) -> schemas.AnyTypeSchema: ...
    
    @typing.overload
    def get_item_(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_(
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
        return super().get_item_(name)

    def __new__(
        cls,
        *args_: typing.Union[dict, frozendict.frozendict, str, datetime.date, datetime.datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        configuration_: typing.Optional[schemas.configuration_module.Configuration] = None,
        **kwargs: typing.Union[dict, frozendict.frozendict, list, tuple, decimal.Decimal, float, int, str, datetime.date, datetime.datetime, uuid.UUID, bool, None, bytes, io.FileIO, io.BufferedReader, schemas.Schema],
    ) -> 'RequiredWithEscapedCharacters':
        return super().__new__(
            cls,
            *args_,
            configuration_=configuration_,
            **kwargs,
        )
