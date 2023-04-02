# coding: utf-8

"""
    discriminator-test

    No description provided (generated by Openapi JSON Schema Generator https://github.com/openapi-json-schema-tools/openapi-json-schema-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0
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

from this_package import schemas  # noqa: F401


class SubtractionOperator(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """


    class Schema_:
        required = {
            "a",
            "b",
            "operator_id",
        }
        
        class Properties:
            A = schemas.Float64Schema
            B = schemas.Float64Schema
            
            
            class OperatorId(
                schemas.StrSchema
            ):
                pass
            __annotations__ = {
                "a": A,
                "b": B,
                "operator_id": OperatorId,
            }
        AdditionalProperties = schemas.NotAnyTypeSchema
    
    a: Schema_.Properties.A
    b: Schema_.Properties.B
    operator_id: Schema_.Properties.OperatorId
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["a"]) -> Schema_.Properties.A: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["b"]) -> Schema_.Properties.B: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["operator_id"]) -> Schema_.Properties.OperatorId: ...
    
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal["a"],
            typing_extensions.Literal["b"],
            typing_extensions.Literal["operator_id"],
        ]
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_(self, name: typing_extensions.Literal["a"]) -> Schema_.Properties.A: ...
    
    @typing.overload
    def get_item_(self, name: typing_extensions.Literal["b"]) -> Schema_.Properties.B: ...
    
    @typing.overload
    def get_item_(self, name: typing_extensions.Literal["operator_id"]) -> Schema_.Properties.OperatorId: ...
    
    def get_item_(
        self,
        name: typing.Union[
            typing_extensions.Literal["a"],
            typing_extensions.Literal["b"],
            typing_extensions.Literal["operator_id"],
        ]
    ):
        return super().get_item_(name)

    def __new__(
        cls,
        *args_: typing.Union[dict, frozendict.frozendict],
        a: typing.Union[Schema_.Properties.A, decimal.Decimal, int, float],
        b: typing.Union[Schema_.Properties.B, decimal.Decimal, int, float],
        operator_id: typing.Union[Schema_.Properties.OperatorId, str],
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
    ) -> 'SubtractionOperator':
        return super().__new__(
            cls,
            *args_,
            a=a,
            b=b,
            operator_id=operator_id,
            configuration_=configuration_,
        )
