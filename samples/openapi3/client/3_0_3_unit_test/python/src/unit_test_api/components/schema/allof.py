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


class Allof(
    schemas.AnyTypeSchema,
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """


    class Schema_:
        # any type
        
        class AllOf:
            
            
            class _0(
                schemas.AnyTypeSchema,
            ):
            
            
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
            
            
            
            class _1(
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
            
            classes = [
                _0,
                _1,
            ]


