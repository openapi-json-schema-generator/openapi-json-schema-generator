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

from petstore_api.paths.fake_parameter_collisions1_abab_self_ab.post.parameters.parameter_5 import schema
from petstore_api.paths.fake_parameter_collisions1_abab_self_ab.post.parameters.parameter_6 import schema as schema_2
from petstore_api.paths.fake_parameter_collisions1_abab_self_ab.post.parameters.parameter_7 import schema as schema_4
from petstore_api.paths.fake_parameter_collisions1_abab_self_ab.post.parameters.parameter_8 import schema as schema_3
Properties = typing_extensions.TypedDict(
    'Properties',
    {
        "1": typing.Type[schema.Schema],
        "aB": typing.Type[schema_2.Schema],
        "A-B": typing.Type[schema_3.Schema],
        "self": typing.Type[schema_4.Schema],
    }
)


class HeaderParametersDict(schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES]):
    __required_keys__: typing.FrozenSet[str] = frozenset({
    })
    __optional_keys__: typing.FrozenSet[str] = frozenset({
        "1",
        "aB",
        "A-B",
        "self",
    })
    
    @property
    def aB(self) -> typing.Union[str, schemas.Unset]:
        val = self.get("aB", schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return typing.cast(
            str,
            val
        )

    def __new__(cls, arg: HeaderParametersDictInput, configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None):
        return HeaderParameters.validate(arg, configuration=configuration)
HeaderParametersDictInput = typing_extensions.TypedDict(
    'HeaderParametersDictInput',
    {
        "1": str,
        "aB": str,
        "A-B": str,
        "self": str,
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

