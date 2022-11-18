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


class EnumsInProperties(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        types = {frozendict.frozendict}
        required = {
            "bar",
        }
        
        class properties:
            
            
            class bar(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    types = {
                        str,
                    }
                    enum_value_to_name = {
                        "bar": "BAR",
                    }
                
                @schemas.classproperty
                def BAR(cls):
                    return cls("bar")
            
            
            class foo(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    types = {
                        str,
                    }
                    enum_value_to_name = {
                        "foo": "FOO",
                    }
                
                @schemas.classproperty
                def FOO(cls):
                    return cls("foo")
            __annotations__ = {
                "bar": bar,
                "foo": foo,
            }
    
    bar: MetaOapg.properties.bar
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bar"]) -> MetaOapg.properties.bar: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["foo"]) -> MetaOapg.properties.foo: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["bar", "foo", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bar"]) -> MetaOapg.properties.bar: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["foo"]) -> typing.Union[MetaOapg.properties.foo, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["bar", "foo", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        bar: typing.Union[MetaOapg.properties.bar, str, ],
        foo: typing.Union[MetaOapg.properties.foo, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EnumsInProperties':
        return super().__new__(
            cls,
            *_args,
            bar=bar,
            foo=foo,
            _configuration=_configuration,
            **kwargs,
        )
