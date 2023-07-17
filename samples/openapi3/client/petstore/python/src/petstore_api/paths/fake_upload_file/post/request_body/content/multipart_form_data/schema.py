# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]

AdditionalMetadata: typing_extensions.TypeAlias = schemas.StrSchema
File: typing_extensions.TypeAlias = schemas.BinarySchema
Properties = typing_extensions.TypedDict(
    'Properties',
    {
        "additionalMetadata": typing.Type[AdditionalMetadata],
        "file": typing.Type[File],
    }
)


class SchemaDict(schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES]):
    __required_keys__: typing.FrozenSet[str] = frozenset({
        "file",
    })
    __optional_keys__: typing.FrozenSet[str] = frozenset({
        "additionalMetadata",
    })
    
    @typing.overload
    def get_property(self, name: typing_extensions.Literal["file"]) -> typing.Union[bytes, schemas.FileIO]:
        ...
    
    @typing.overload
    def get_property(self, name: typing_extensions.Literal["additionalMetadata"]) -> str:
        ...
    
    def get_property(self, name):
        val = self.get(name, schemas.unset)
        if name == "file":
            return typing.cast(
                typing.Union[bytes, schemas.FileIO],
                val
            )
        elif name == "additionalMetadata":
            return val if val is schemas.unset else typing.cast(
                str,
                val
            )
        raise ValueError(schemas.key_unknown_error_msg(name))
    
    def get_additional_property_(self, name: str) -> schemas.OUTPUT_BASE_TYPES:
        schemas.raise_if_key_known(name, self.__required_keys__, self.__optional_keys__)
        return self.__getitem__(name)

    def __new__(cls, arg: SchemaDictInput, configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None):
        return Schema.validate(arg, configuration=configuration)
SchemaDictInput = typing.Mapping[str, schemas.INPUT_TYPES_ALL]


@dataclasses.dataclass(frozen=True)
class Schema(
    schemas.Schema[SchemaDict, tuple]
):
    types: typing.FrozenSet[typing.Type] = frozenset({schemas.immutabledict})
    required: typing.FrozenSet[str] = frozenset({
        "file",
    })
    properties: Properties = dataclasses.field(default_factory=lambda: schemas.typed_dict_to_instance(Properties)) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            schemas.immutabledict: SchemaDict
        }
    )

    @classmethod
    def validate(
        cls,
        arg: typing.Union[
            SchemaDictInput,
            SchemaDict,
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> SchemaDict:
        return super().validate_base(
            arg,
            configuration=configuration,
        )

