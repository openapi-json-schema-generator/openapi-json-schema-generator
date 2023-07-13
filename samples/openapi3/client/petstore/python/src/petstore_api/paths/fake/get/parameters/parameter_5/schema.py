# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *



class SchemaEnums:

    @schemas.classproperty
    def POSITIVE_1_PT_1(cls) -> typing.Union[int, float]:
        return Schema.validate(1.1)

    @schemas.classproperty
    def NEGATIVE_1_PT_2(cls) -> typing.Union[int, float]:
        return Schema.validate(-1.2)


@dataclasses.dataclass(frozen=True)
class Schema(
    schemas.Schema
):
    types: typing.FrozenSet[typing.Type] = frozenset({
        float,
        int,
    })
    format: str = 'double'
    enum_value_to_name: typing.Mapping[typing.Union[int, float, str, schemas.Bool, None], str] = dataclasses.field(
        default_factory=lambda: {
            1.1: "POSITIVE_1_PT_1",
            -1.2: "NEGATIVE_1_PT_2",
        }
    )
    enums = SchemaEnums

    @classmethod
    def validate(
        cls,
        arg: typing.Union[int, float],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing.Union[int, float]:
        validated_arg = super().validate_base(
            arg,
            configuration=configuration,
        )
        return validated_arg
