# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]

Name2: typing_extensions.TypeAlias = schemas.Int32Schema
SnakeCase: typing_extensions.TypeAlias = schemas.Int32Schema
_Property: typing_extensions.TypeAlias = schemas.StrSchema
Properties = typing_extensions.TypedDict(
    'Properties',
    {
        "name": typing.Type[Name2],
        "snake_case": typing.Type[SnakeCase],
        "property": typing.Type[_Property],
    }
)


class NameDict(schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES]):
    __required_keys__: typing.FrozenSet[str] = frozenset({
        "name",
    })
    __optional_keys__: typing.FrozenSet[str] = frozenset({
        "snake_case",
        "property",
    })
    
    @property
    def get_name(self) -> int:
        return typing.cast(
            int,
            self.__getitem__("name")
        )
    
    @property
    def get_snake_case(self) -> int:
        val = self.get("snake_case", schemas.unset)
        if val is schemas.unset:
            return val
        return typing.cast(
            int,
            val
        )
    
    @property
    def get__property(self) -> str:
        val = self.get("property", schemas.unset)
        if val is schemas.unset:
            return val
        return typing.cast(
            str,
            val
        )
    
    def get_additional_property_(self, name: str) -> schemas.OUTPUT_BASE_TYPES:
        schemas.raise_if_key_known(name, self.__required_keys__, self.__optional_keys__)
        return self.__getitem__(name)

    def __new__(cls, arg: NameDictInput, configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None):
        return Name.validate(arg, configuration=configuration)
NameDictInput = typing.Mapping[str, schemas.INPUT_TYPES_ALL]


@dataclasses.dataclass(frozen=True)
class Name(
    schemas.AnyTypeSchema[NameDict, typing.Tuple[schemas.OUTPUT_BASE_TYPES, ...]],
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.

    Model for testing model name same as property name
    """
    # any type
    required: typing.FrozenSet[str] = frozenset({
        "name",
    })
    properties: Properties = dataclasses.field(default_factory=lambda: schemas.typed_dict_to_instance(Properties)) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            schemas.immutabledict: NameDict,
        }
    )

