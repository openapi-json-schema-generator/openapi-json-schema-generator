# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *


class NoAdditionalProperties(
    schemas.DictSchema[schemas.T]
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
            Id: typing_extensions.TypeAlias = schemas.Int64Schema[U]
            PetId: typing_extensions.TypeAlias = schemas.Int64Schema[U]
            __annotations__ = {
                "id": Id,
                "petId": PetId,
            }
        AdditionalProperties: typing_extensions.TypeAlias = schemas.NotAnyTypeSchema[U]
    
    id: Schema_.Properties.Id[decimal.Decimal]
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> Schema_.Properties.Id[decimal.Decimal]: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["petId"]) -> Schema_.Properties.PetId[decimal.Decimal]: ...
    
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
    ) -> NoAdditionalProperties[frozendict.frozendict]:
        return super().__new__(
            cls,
            *args_,
            id=id,
            petId=petId,
            configuration_=configuration_,
        )
