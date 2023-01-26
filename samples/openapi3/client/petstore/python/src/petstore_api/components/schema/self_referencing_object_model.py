# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
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


class (
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """


    class Schema_:
        types = {frozendict.frozendict}
        
        class Properties:
        
            @staticmethod
            def () -> typing.Type['SelfReferencingObjectModel']:
                return SelfReferencingObjectModel
            __annotations__ = {
                "": ,
            }
        
        @staticmethod
        def () -> typing.Type['SelfReferencingObjectModel']:
            return SelfReferencingObjectModel
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal[""]) -> 'SelfReferencingObjectModel': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> 'SelfReferencingObjectModel': ...
    
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal[""],
            str
        ]
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_(self, name: typing_extensions.Literal[""]) -> typing.Union['SelfReferencingObjectModel', schemas.Unset]: ...
    
    @typing.overload
    def get_item_(self, name: str) -> typing.Union['SelfReferencingObjectModel', schemas.Unset]: ...
    
    def get_item_(
        self,
        name: typing.Union[
            typing_extensions.Literal[""],
            str
        ]
    ):
        return super().get_item_(name)

    def __new__(
        cls,
        *args_: typing.Union[dict, frozendict.frozendict, ],
        configuration_: typing.Optional[schemas.configuration_module.Configuration] = None,
        **kwargs: 'SelfReferencingObjectModel',
    ) -> '':
        return super().__new__(
            cls,
            *args_,
            configuration_=configuration_,
            **kwargs,
        )
