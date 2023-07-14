# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]

Return2: typing_extensions.TypeAlias = schemas.Int32Schema
Properties = typing_extensions.TypedDict(
    'Properties',
    {
        "return": typing.Type[Return2],
    }
)


class ReturnDict(schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES]):
    
    def get_property(self, name: typing_extensions.Literal["return"]) -> int:
        return typing.cast(
            int,
            self.__getitem__(name)
        )
    
    def get_additional_property(self, name: str) -> schemas.OUTPUT_BASE_TYPES:
        return self.__getitem__(name)

    def __new__(cls, arg: ReturnDictInput, configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None):
        return _Return.validate(arg, configuration=configuration)
ReturnDictInput = typing.Mapping[str, schemas.INPUT_TYPES_ALL]


@dataclasses.dataclass(frozen=True)
class _Return(
    schemas.AnyTypeSchema[ReturnDict, typing.Tuple[schemas.OUTPUT_BASE_TYPES, ...]],
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.

    Model for testing reserved words
    """
    # any type
    properties: Properties = dataclasses.field(default_factory=lambda: schemas.typed_dict_to_instance(Properties)) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            schemas.immutabledict: ReturnDict,
        }
    )

