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


class NoAdditionalProperties(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """


    class Schema_:
        types = {frozendict.frozendict}
        required = {
            "id",
        }
        
        class Properties:
            Id = schemas.Int64Schema
            PetId = schemas.Int64Schema
            __annotations__ = {
                "id": Id,
                "petId": PetId,
            }
        AdditionalProperties = schemas.NotAnyTypeSchema
    
    id: Schema_.Properties.Id
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> Schema_.Properties.Id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["petId"]) -> Schema_.Properties.PetId: ...
    
    def __getitem__(
        self,
        name: typing.Union[
            typing_extensions.Literal["id"],
            typing_extensions.Literal["petId"],
        ]
    ):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    def __new__(
        cls,
        *args_: typing.Union[dict, frozendict.frozendict],
        id: typing.Union[Schema_.Properties.Id, decimal.Decimal, int],
        petId: typing.Union[Schema_.Properties.PetId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
    ) -> 'NoAdditionalProperties':
        return super().__new__(
            cls,
            *args_,
            id=id,
            petId=petId,
            configuration_=configuration_,
        )
