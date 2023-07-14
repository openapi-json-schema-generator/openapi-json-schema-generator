# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]

AdditionalProperties: typing_extensions.TypeAlias = schemas.NotAnyTypeSchema
Id: typing_extensions.TypeAlias = schemas.Int64Schema
PetId: typing_extensions.TypeAlias = schemas.Int64Schema
Properties = typing_extensions.TypedDict(
    'Properties',
    {
        "id": typing.Type[Id],
        "petId": typing.Type[PetId],
    }
)
NoAdditionalPropertiesRequiredDictInput = typing_extensions.TypedDict(
    'NoAdditionalPropertiesRequiredDictInput',
    {
        "id": int,
    }
)
NoAdditionalPropertiesOptionalDictInput = typing_extensions.TypedDict(
    'NoAdditionalPropertiesOptionalDictInput',
    {
        "petId": int,
    },
    total=False
)


class NoAdditionalPropertiesDict(schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES]):
    __required_keys__ = frozenset({
        "id",
    })
    __optional_keys__ = frozenset({
        "petId",
    })
    
    @typing.overload
    def get_property(self, name: typing_extensions.Literal["id"]) -> int:
        ...
    
    @typing.overload
    def get_property(self, name: typing_extensions.Literal["petId"]) -> int:
        ...
    
    def get_property(self, name):
        return self.__getitem__(name)

    def __new__(cls, arg: NoAdditionalPropertiesDictInput, configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None):
        return NoAdditionalProperties.validate(arg, configuration=configuration)


class NoAdditionalPropertiesDictInput(NoAdditionalPropertiesRequiredDictInput, NoAdditionalPropertiesOptionalDictInput):
    pass


@dataclasses.dataclass(frozen=True)
class NoAdditionalProperties(
    schemas.Schema[NoAdditionalPropertiesDict, tuple]
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """
    types: typing.FrozenSet[typing.Type] = frozenset({schemas.immutabledict})
    required: typing.FrozenSet[str] = frozenset({
        "id",
    })
    properties: Properties = dataclasses.field(default_factory=lambda: schemas.typed_dict_to_instance(Properties)) # type: ignore
    additional_properties: typing.Type[AdditionalProperties] = dataclasses.field(default_factory=lambda: AdditionalProperties) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            schemas.immutabledict: NoAdditionalPropertiesDict
        }
    )

    @classmethod
    def validate(
        cls,
        arg: typing.Union[
            NoAdditionalPropertiesDictInput,
            NoAdditionalPropertiesDict,
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> NoAdditionalPropertiesDict:
        return super().validate_base(
            arg,
            configuration=configuration,
        )

