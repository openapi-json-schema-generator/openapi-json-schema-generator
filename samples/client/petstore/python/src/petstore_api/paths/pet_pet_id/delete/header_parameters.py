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

from petstore_api.paths.pet_pet_id.delete.parameters.parameter_0 import schema
Properties = typing_extensions.TypedDict(
    'Properties',
    {
        "api_key": typing.Type[schema.Schema],
    }
)


class HeaderParametersDict(schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES]):

    __required_keys__: typing.FrozenSet[str] = frozenset({
    })
    __optional_keys__: typing.FrozenSet[str] = frozenset({
        "api_key",
    })
    
    def __new__(
        cls,
        *,
        api_key: typing.Union[
            str,
            schemas.Unset
        ] = schemas.unset,
        configuration_: typing.Optional[schema_configuration.SchemaConfiguration] = None,
    ):
        arg_: typing.Dict[str, typing.Any] = {}
        for key, val in (
            ("api_key", api_key),
        ):
            if isinstance(val, schemas.Unset):
                continue
            arg_[key] = val
        used_arg_ = typing.cast(HeaderParametersDictInput, arg_)
        return HeaderParameters.validate(used_arg_, configuration=configuration_)
    
    @staticmethod
    def from_dict_(
        arg: typing.Union[
            HeaderParametersDictInput,
            HeaderParametersDict
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> HeaderParametersDict:
        return HeaderParameters.validate(arg, configuration=configuration)
    
    @property
    def api_key(self) -> typing.Union[str, schemas.Unset]:
        val = self.get("api_key", schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return typing.cast(
            str,
            val
        )
HeaderParametersDictInput = typing_extensions.TypedDict(
    'HeaderParametersDictInput',
    {
        "api_key": str,
    },
    total=False
)


@dataclasses.dataclass(frozen=True)
class HeaderParameters(
    schemas.Schema[HeaderParametersDict, tuple]
):
    types: typing.FrozenSet[typing.Type] = frozenset({schemas.immutabledict})
    properties: Properties = dataclasses.field(default_factory=lambda: schemas.typed_dict_to_instance(Properties)) # type: ignore
    additional_properties: typing.Type[AdditionalProperties] = dataclasses.field(default_factory=lambda: AdditionalProperties) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            schemas.immutabledict: HeaderParametersDict
        }
    )

    @classmethod
    def validate(
        cls,
        arg: typing.Union[
            HeaderParametersDictInput,
            HeaderParametersDict,
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> HeaderParametersDict:
        return super().validate_base(
            arg,
            configuration=configuration,
        )

