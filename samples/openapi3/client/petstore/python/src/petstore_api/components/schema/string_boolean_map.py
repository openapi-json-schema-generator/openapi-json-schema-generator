# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]

AdditionalProperties: typing_extensions.TypeAlias = schemas.BoolSchema


class StringBooleanMapDict(schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES]):
    __required_keys__ = frozenset({
    })
    __optional_keys__ = frozenset({
    })
    
    def get_additional_property(self, name: str) -> bool:
        return typing.cast(
            bool,
            self.__getitem__(name)
        )

    def __new__(cls, arg: StringBooleanMapDictInput, configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None):
        return StringBooleanMap.validate(arg, configuration=configuration)
StringBooleanMapDictInput = typing.Mapping[
    str,
    bool,
]


@dataclasses.dataclass(frozen=True)
class StringBooleanMap(
    schemas.Schema[StringBooleanMapDict, tuple]
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """
    types: typing.FrozenSet[typing.Type] = frozenset({schemas.immutabledict})
    additional_properties: typing.Type[AdditionalProperties] = dataclasses.field(default_factory=lambda: AdditionalProperties) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            schemas.immutabledict: StringBooleanMapDict
        }
    )

    @classmethod
    def validate(
        cls,
        arg: typing.Union[
            StringBooleanMapDictInput,
            StringBooleanMapDict,
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> StringBooleanMapDict:
        return super().validate_base(
            arg,
            configuration=configuration,
        )

