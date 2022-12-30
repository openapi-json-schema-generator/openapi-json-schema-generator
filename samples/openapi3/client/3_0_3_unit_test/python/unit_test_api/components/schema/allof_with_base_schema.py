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


class AllofWithBaseSchema(
    schemas.AnyTypeSchema,
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class Schema_:
        # any type
        required = {
            "bar",
        }
        
        class Properties:
            Bar = schemas.IntSchema
            __annotations__ = {
                "bar": Bar,
            }
        
        class AllOf:
            
            
            class AllOf0(
                schemas.AnyTypeSchema,
            ):
            
            
                class Schema_:
                    # any type
                    required = {
                        "foo",
                    }
                    
                    class Properties:
                        Foo = schemas.StrSchema
                        __annotations__ = {
                            "foo": Foo,
                        }
            
                
                foo: Schema_.Properties.Foo
                
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
                def get_item_(self, name: typing_extensions.Literal["foo"]) -> Schema_.Properties.Foo: ...
                
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
                    *_args: typing.Union[dict, frozendict.frozendict, str, datetime.date, datetime.datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    foo: typing.Union[Schema_.Properties.Foo, str, ],
                    configuration_: typing.Optional[schemas.configuration_module.Configuration] = None,
                    **kwargs: typing.Union[dict, frozendict.frozendict, list, tuple, decimal.Decimal, float, int, str, datetime.date, datetime.datetime, uuid.UUID, bool, None, bytes, io.FileIO, io.BufferedReader, schemas.Schema],
                ) -> 'AllOf0':
                    return super().__new__(
                        cls,
                        *_args,
                        foo=foo,
                        configuration_=configuration_,
                        **kwargs,
                    )
            
            
            class AllOf1(
                schemas.AnyTypeSchema,
            ):
            
            
                class Schema_:
                    # any type
                    required = {
                        "baz",
                    }
                    
                    class Properties:
                        Baz = schemas.NoneSchema
                        __annotations__ = {
                            "baz": Baz,
                        }
            
                
                baz: Schema_.Properties.Baz
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["baz"]) -> Schema_.Properties.Baz: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(
                    self,
                    name: typing.Union[
                        typing_extensions.Literal["baz"],
                        str
                    ]
                ):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                @typing.overload
                def get_item_(self, name: typing_extensions.Literal["baz"]) -> Schema_.Properties.Baz: ...
                
                @typing.overload
                def get_item_(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_(
                    self,
                    name: typing.Union[
                        typing_extensions.Literal["baz"],
                        str
                    ]
                ):
                    return super().get_item_(name)
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, str, datetime.date, datetime.datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    baz: typing.Union[Schema_.Properties.Baz, None, ],
                    configuration_: typing.Optional[schemas.configuration_module.Configuration] = None,
                    **kwargs: typing.Union[dict, frozendict.frozendict, list, tuple, decimal.Decimal, float, int, str, datetime.date, datetime.datetime, uuid.UUID, bool, None, bytes, io.FileIO, io.BufferedReader, schemas.Schema],
                ) -> 'AllOf1':
                    return super().__new__(
                        cls,
                        *_args,
                        baz=baz,
                        configuration_=configuration_,
                        **kwargs,
                    )
            classes = [
                AllOf0,
                AllOf1,
            ]

    
    bar: Schema_.Properties.Bar
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bar"]) -> Schema_.Properties.Bar: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal["bar"],
            str
        ]
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_(self, name: typing_extensions.Literal["bar"]) -> Schema_.Properties.Bar: ...
    
    @typing.overload
    def get_item_(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_(
        self,
        name: typing.Union[
            typing_extensions.Literal["bar"],
            str
        ]
    ):
        return super().get_item_(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, str, datetime.date, datetime.datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        bar: typing.Union[Schema_.Properties.Bar, decimal.Decimal, int, ],
        configuration_: typing.Optional[schemas.configuration_module.Configuration] = None,
        **kwargs: typing.Union[dict, frozendict.frozendict, list, tuple, decimal.Decimal, float, int, str, datetime.date, datetime.datetime, uuid.UUID, bool, None, bytes, io.FileIO, io.BufferedReader, schemas.Schema],
    ) -> 'AllofWithBaseSchema':
        return super().__new__(
            cls,
            *_args,
            bar=bar,
            configuration_=configuration_,
            **kwargs,
        )
