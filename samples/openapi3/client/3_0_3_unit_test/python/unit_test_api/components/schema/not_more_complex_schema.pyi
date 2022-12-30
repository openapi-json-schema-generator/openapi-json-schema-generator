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


class NotMoreComplexSchema(
    schemas.AnyTypeSchema,
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class Schema_:
        # any type
        
        
        class _Not(
            schemas.DictSchema
        ):
        
        
            class Schema_:
                
                class Properties:
                    Foo = schemas.StrSchema
                    __annotations__ = {
                        "foo": Foo,
                    }
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["foo"]) -> Schema_.Properties.Foo: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(
                self,
                name: typing.Union[
                    typing_extensions.Literal["foo"],
                    str
                ]
            ):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            @typing.overload
            def get_item_(self, name: typing_extensions.Literal["foo"]) -> typing.Union[Schema_.Properties.Foo, schemas.Unset]: ...
            
            @typing.overload
            def get_item_(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_(
                self,
                name: typing.Union[
                    typing_extensions.Literal["foo"],
                    str
                ]
            ):
                return super().get_item_(name)
        
            def __new__(
                cls,
                *_args: typing.Union[dict, frozendict.frozendict, ],
                foo: typing.Union[Schema_.Properties.Foo, str, schemas.Unset] = schemas.unset,
                configuration_: typing.Optional[schemas.configuration_module.Configuration] = None,
                **kwargs: typing.Union[dict, frozendict.frozendict, list, tuple, decimal.Decimal, float, int, str, datetime.date, datetime.datetime, uuid.UUID, bool, None, bytes, io.FileIO, io.BufferedReader, schemas.Schema],
            ) -> '_Not':
                return super().__new__(
                    cls,
                    *_args,
                    foo=foo,
                    configuration_=configuration_,
                    **kwargs,
                )


    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, str, datetime.date, datetime.datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        configuration_: typing.Optional[schemas.configuration_module.Configuration] = None,
        **kwargs: typing.Union[dict, frozendict.frozendict, list, tuple, decimal.Decimal, float, int, str, datetime.date, datetime.datetime, uuid.UUID, bool, None, bytes, io.FileIO, io.BufferedReader, schemas.Schema],
    ) -> 'NotMoreComplexSchema':
        return super().__new__(
            cls,
            *_args,
            configuration_=configuration_,
            **kwargs,
        )
