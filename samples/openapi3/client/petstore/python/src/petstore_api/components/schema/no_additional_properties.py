# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *

AdditionalProperties: typing_extensions.TypeAlias = schemas.NotAnyTypeSchema[U]
Id: typing_extensions.TypeAlias = schemas.Int64Schema[U]
PetId: typing_extensions.TypeAlias = schemas.Int64Schema[U]


class NoAdditionalProperties(
    schemas.DictSchema[schemas.T]
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """


    @dataclasses.dataclass(frozen=True)
    class Schema_:
        types: typing.FrozenSet[typing.Type] = frozenset({frozendict.frozendict})
        required: typing.FrozenSet[str] = frozenset({
            "id",
        })
        properties: NoAdditionalPropertiesProperties = dataclasses.field(default_factory=lambda: schemas.typed_dict_to_instance(NoAdditionalPropertiesProperties)) # type: ignore
        additional_properties: typing.Type[AdditionalProperties] = dataclasses.field(default_factory=lambda: AdditionalProperties) # type: ignore
    
    @property
    def id(self) -> Id[decimal.Decimal]:
        return self.__getitem__("id")
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> Id[decimal.Decimal]: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["petId"]) -> PetId[decimal.Decimal]: ...
    
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
        id: typing.Union[
            Id[decimal.Decimal],
            decimal.Decimal,
            int
        ],
        petId: typing.Union[
            PetId[decimal.Decimal],
            schemas.Unset,
            decimal.Decimal,
            int
        ] = schemas.unset,
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
    ) -> NoAdditionalProperties[frozendict.frozendict]:
        inst = super().__new__(
            cls,
            *args_,
            id=id,
            petId=petId,
            configuration_=configuration_,
        )
        inst = typing.cast(
            NoAdditionalProperties[frozendict.frozendict],
            inst
        )
        return inst

NoAdditionalPropertiesProperties = typing_extensions.TypedDict(
    'NoAdditionalPropertiesProperties',
    {
        "id": typing.Type[Id],
        "petId": typing.Type[PetId],
    }
)
