# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
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

from petstore_api import schemas  # noqa: F401


class SelfReferencingObjectModel(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        types = {frozendict.frozendict}
        
        class properties:
        
            @staticmethod
            def selfRef() -> typing.Type['self_referencing_object_model.SelfReferencingObjectModel']:
                return self_referencing_object_model.SelfReferencingObjectModel
            __annotations__ = {
                "selfRef": selfRef,
            }
        
        @staticmethod
        def additionalProperties() -> typing.Type['self_referencing_object_model.SelfReferencingObjectModel']:
            return self_referencing_object_model.SelfReferencingObjectModel
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["selfRef"]) -> 'self_referencing_object_model.SelfReferencingObjectModel': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> 'self_referencing_object_model.SelfReferencingObjectModel': ...
    
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal["selfRef"],
            str
        ]
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["selfRef"]) -> typing.Union['self_referencing_object_model.SelfReferencingObjectModel', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union['self_referencing_object_model.SelfReferencingObjectModel', schemas.Unset]: ...
    
    def get_item_oapg(
        self,
        name: typing.Union[
            typing_extensions.Literal["selfRef"],
            str
        ]
    ):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        selfRef: typing.Union['self_referencing_object_model.SelfReferencingObjectModel', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: 'self_referencing_object_model.SelfReferencingObjectModel',
    ) -> 'SelfReferencingObjectModel':
        return super().__new__(
            cls,
            *_args,
            selfRef=selfRef,
            _configuration=_configuration,
            **kwargs,
        )

from petstore_api.components.schema import self_referencing_object_model
