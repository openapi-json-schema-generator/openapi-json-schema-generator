# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose.  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from openapi_client.shared_imports.schema_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]

AdditionalProperties: typing_extensions.TypeAlias = schemas.NotAnyTypeSchema

from openapi_client.paths.pet_pet_id.get.parameters.parameter_0 import schema
Properties = typing.TypedDict(
    'Properties',
    {
        "petId": typing.Type[schema.Schema],
    }
)


class PathParametersDict(schemas.immutabledict[str, int]):

    __required_keys__: typing.FrozenSet[str] = frozenset({
        "petId",
    })
    __optional_keys__: typing.FrozenSet[str] = frozenset({
    })
    
    def __new__(
        cls,
        *,
        petId: int,
        configuration_: typing.Optional[schema_configuration.SchemaConfiguration] = None,
    ):
        arg_: typing.Dict[str, typing.Any] = {
            "petId": petId,
        }
        used_arg_ = typing.cast(PathParametersDictInput, arg_)
        return PathParameters.validate(used_arg_, configuration=configuration_)
    
    @staticmethod
    def from_dict_(
        arg: typing.Union[
            PathParametersDictInput,
            PathParametersDict
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> PathParametersDict:
        return PathParameters.validate(arg, configuration=configuration)
    
    @property
    def petId(self) -> int:
        return self.__getitem__("petId")
PathParametersDictInput = typing.TypedDict(
    'PathParametersDictInput',
    {
        "petId": int,
    }
)


@dataclasses.dataclass(frozen=True)
class PathParameters(
    schemas.Schema[PathParametersDict, tuple]
):
    types: typing.FrozenSet[typing.Type] = frozenset({schemas.immutabledict})
    required: typing.FrozenSet[str] = frozenset({
        "petId",
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

