# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]

AdditionalProperties: typing_extensions.TypeAlias = schemas.AnyTypeSchema


class ReqPropsFromTrueAddPropsDict(schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES]):
    __required_keys__ = frozenset({
        "invalid-name",
        "validName",
    })
    __optional_keys__ = frozenset({
    })
    
    @typing.overload
    def get_property(self, name: typing_extensions.Literal["invalid-name"]) -> schemas.OUTPUT_BASE_TYPES:
        ...
    
    @typing.overload
    def get_property(self, name: typing_extensions.Literal["validName"]) -> schemas.OUTPUT_BASE_TYPES:
        ...
    
    def get_property(self, name):
        return self.__getitem__(name)
    
    def get_additional_property(self, name: str) -> schemas.OUTPUT_BASE_TYPES:
        return typing.cast(
            schemas.OUTPUT_BASE_TYPES,
            self.__getitem__(name)
        )

    def __new__(cls, arg: ReqPropsFromTrueAddPropsDictInput, configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None):
        return ReqPropsFromTrueAddProps.validate(arg, configuration=configuration)
ReqPropsFromTrueAddPropsDictInput = typing.Mapping[str, schemas.INPUT_TYPES_ALL]


@dataclasses.dataclass(frozen=True)
class ReqPropsFromTrueAddProps(
    schemas.Schema[ReqPropsFromTrueAddPropsDict, tuple]
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """
    types: typing.FrozenSet[typing.Type] = frozenset({schemas.immutabledict})
    required: typing.FrozenSet[str] = frozenset({
        "invalid-name",
        "validName",
    })
    additional_properties: typing.Type[AdditionalProperties] = dataclasses.field(default_factory=lambda: AdditionalProperties) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            schemas.immutabledict: ReqPropsFromTrueAddPropsDict
        }
    )

    @classmethod
    def validate(
        cls,
        arg: typing.Union[
            ReqPropsFromTrueAddPropsDictInput,
            ReqPropsFromTrueAddPropsDict,
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> ReqPropsFromTrueAddPropsDict:
        return super().validate_base(
            arg,
            configuration=configuration,
        )

