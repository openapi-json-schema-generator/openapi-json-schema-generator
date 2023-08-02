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

from petstore_api.paths.fake_delete_coffee_id.delete.parameters.parameter_0 import schema
Properties = typing_extensions.TypedDict(
    'Properties',
    {
        "id": typing.Type[schema.Schema],
    }
)


class PathParametersDict(schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES]):

    __required_keys__: typing.FrozenSet[str] = frozenset({
        "id",
    })
    __optional_keys__: typing.FrozenSet[str] = frozenset({
    })
    
    @property
    def id(self) -> str:
        return typing.cast(
            str,
            self.__getitem__("id")
        )

    @staticmethod
    def from_dict_(
        arg: PathParametersDictInput,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> PathParametersDict:
        return PathParameters.validate(arg, configuration=configuration)
    
    def __new__(
        cls,
        id: str,
        configuration_: typing.Optional[schema_configuration.SchemaConfiguration] = None,
    ):
        arg_ = {
            "id": id,
        }
        arg_ = typing.cast(PathParametersDictInput, arg_)
        return PathParameters.validate(arg_, configuration=configuration_)
PathParametersDictInput = typing_extensions.TypedDict(
    'PathParametersDictInput',
    {
        "id": str,
    }
)


@dataclasses.dataclass(frozen=True)
class PathParameters(
    schemas.Schema[PathParametersDict, tuple]
):
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
            schemas.immutabledict: PathParametersDict
        }
    )

    @classmethod
    def validate(
        cls,
        arg: typing.Union[
            PathParametersDictInput,
            PathParametersDict,
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> PathParametersDict:
        return super().validate_base(
            arg,
            configuration=configuration,
        )

