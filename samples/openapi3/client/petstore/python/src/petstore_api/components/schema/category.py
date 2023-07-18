# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]

Id: typing_extensions.TypeAlias = schemas.Int64Schema


@dataclasses.dataclass(frozen=True)
class Name(
    schemas.StrSchema
):
    types: typing.FrozenSet[typing.Type] = frozenset({
        str,
    })
    default: str = "default-name"
Properties = typing_extensions.TypedDict(
    'Properties',
    {
        "id": typing.Type[Id],
        "name": typing.Type[Name],
    }
)


class CategoryDict(schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES]):
    __required_keys__: typing.FrozenSet[str] = frozenset({
        "name",
    })
    __optional_keys__: typing.FrozenSet[str] = frozenset({
        "id",
    })
    
    @property
    def get_name(self) -> str:
        return typing.cast(
            str,
            self.__getitem__("name")
        )
    
    @property
    def get_id(self) -> int:
        val = self.get("id", schemas.unset)
        if val is schemas.unset:
            return val
        return typing.cast(
            int,
            val
        )
    
    def get_additional_property_(self, name: str) -> schemas.OUTPUT_BASE_TYPES:
        schemas.raise_if_key_known(name, self.__required_keys__, self.__optional_keys__)
        return self.__getitem__(name)

    def __new__(cls, arg: CategoryDictInput, configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None):
        return Category.validate(arg, configuration=configuration)
CategoryDictInput = typing.Mapping[str, schemas.INPUT_TYPES_ALL]


@dataclasses.dataclass(frozen=True)
class Category(
    schemas.Schema[CategoryDict, tuple]
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """
    types: typing.FrozenSet[typing.Type] = frozenset({schemas.immutabledict})
    required: typing.FrozenSet[str] = frozenset({
        "name",
    })
    properties: Properties = dataclasses.field(default_factory=lambda: schemas.typed_dict_to_instance(Properties)) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            schemas.immutabledict: CategoryDict
        }
    )

    @classmethod
    def validate(
        cls,
        arg: typing.Union[
            CategoryDictInput,
            CategoryDict,
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> CategoryDict:
        return super().validate_base(
            arg,
            configuration=configuration,
        )

