# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
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

from petstore_api import schemas  # noqa: F401


class ObjectWithInvalidNamedRefedProperties(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """


    class Schema_:
        types = {frozendict.frozendict}
        required = {
            "!reference",
            "from",
        }
        
        class Properties:
        
            @staticmethod
            def _from() -> typing.Type['from_schema.FromSchema']:
                return from_schema.FromSchema
        
            @staticmethod
            def reference() -> typing.Type['array_with_validations_in_items.ArrayWithValidationsInItems']:
                return array_with_validations_in_items.ArrayWithValidationsInItems
            __annotations__ = {
                "from": _from,
                "!reference": reference,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["!reference"]) -> 'array_with_validations_in_items.ArrayWithValidationsInItems': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["from"]) -> 'from_schema.FromSchema': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal["!reference"],
            typing_extensions.Literal["from"],
            str
        ]
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    def __new__(
        cls,
        *args_: typing.Union[dict, frozendict.frozendict],
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
        **kwargs: typing.Union[dict, frozendict.frozendict, list, tuple, decimal.Decimal, float, int, str, datetime.date, datetime.datetime, uuid.UUID, bool, None, bytes, io.FileIO, io.BufferedReader, schemas.Schema],
    ) -> 'ObjectWithInvalidNamedRefedProperties':
        return super().__new__(
            cls,
            *args_,
            configuration_=configuration_,
            **kwargs,
        )

from petstore_api.components.schema import array_with_validations_in_items
from petstore_api.components.schema import from_schema
