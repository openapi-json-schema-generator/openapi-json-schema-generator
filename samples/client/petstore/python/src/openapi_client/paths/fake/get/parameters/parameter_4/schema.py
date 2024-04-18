# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose.  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from openapi_client.shared_imports.schema_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]



class SchemaEnums:

    @schemas.classproperty
    def POSITIVE_1(cls) -> typing.Literal[1]:
        return Schema.validate(1)

    @schemas.classproperty
    def NEGATIVE_2(cls) -> typing.Literal[-2]:
        return Schema.validate(-2)


@dataclasses.dataclass(frozen=True)
class Schema(
    schemas.Schema
):
    types: typing.FrozenSet[typing.Type] = frozenset({
        int,
    })
    format: str = 'int32'
    enum_value_to_name: typing.Mapping[typing.Union[int, float, str, schemas.Bool, None], str] = dataclasses.field(
        default_factory=lambda: {
            1: "POSITIVE_1",
            -2: "NEGATIVE_2",
        }
    )
    enums = SchemaEnums

    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: typing.Literal[1],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing.Literal[1]: ...
    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: typing.Literal[-2],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing.Literal[-2]: ...
    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: int,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing.Literal[1,-2,]: ...
    @classmethod
    def validate(
        cls,
        arg,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing.Literal[
        1,
        -2,
    ]:
        validated_arg = super().validate_base(
            arg,
            configuration=configuration,
        )
        return typing.cast(typing.Literal[
                1,
                -2,
            ],
            validated_arg
        )
