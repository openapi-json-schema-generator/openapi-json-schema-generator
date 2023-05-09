# coding: utf-8

"""
    openapi 3.0.3 sample spec
    sample spec for testing openapi functionality, built from json schema tests for draft6  # noqa: E501
    The version of the OpenAPI document: 0.0.1
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

import datetime  # noqa: F401
import decimal  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from unit_test_api import schemas  # noqa: F401


class OneofWithRequired(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """


    class Schema_:
        types = {
            frozendict.frozendict,
        }
        
        class OneOf:
            
            
            class _0(
                schemas.AnyTypeSchema,
            ):
            
            
                class Schema_:
                    # any type
                    required = {
                        "bar",
                        "foo",
                    }
            
                
                @property
                def bar(self) -> schemas.AnyTypeSchema:
                    return self.__getitem__("bar")
                
                @property
                def foo(self) -> schemas.AnyTypeSchema:
                    return self.__getitem__("foo")
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["bar"]) -> schemas.AnyTypeSchema: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["foo"]) -> schemas.AnyTypeSchema: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(
                    self,
                    name: typing.Union[
                        typing_extensions.Literal["bar"],
                        typing_extensions.Literal["foo"],
                        str
                    ]
                ):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
            
            
            
            class _1(
                schemas.AnyTypeSchema,
            ):
            
            
                class Schema_:
                    # any type
                    required = {
                        "baz",
                        "foo",
                    }
            
                
                @property
                def baz(self) -> schemas.AnyTypeSchema:
                    return self.__getitem__("baz")
                
                @property
                def foo(self) -> schemas.AnyTypeSchema:
                    return self.__getitem__("foo")
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["baz"]) -> schemas.AnyTypeSchema: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["foo"]) -> schemas.AnyTypeSchema: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(
                    self,
                    name: typing.Union[
                        typing_extensions.Literal["baz"],
                        typing_extensions.Literal["foo"],
                        str
                    ]
                ):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
            
            classes = [
                _0,
                _1,
            ]


