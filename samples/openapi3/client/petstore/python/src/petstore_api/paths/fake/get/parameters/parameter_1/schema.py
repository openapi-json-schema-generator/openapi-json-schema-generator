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
    def _ABC(cls) -> str:
        return Schema.validate("_abc")

    @schemas.classproperty
    def HYPHEN_MINUS_EFG(cls) -> str:
        return Schema.validate("-efg")

    @schemas.classproperty
    def LEFT_PARENTHESIS_XYZ_RIGHT_PARENTHESIS(cls) -> str:
        return Schema.validate("(xyz)")


@dataclasses.dataclass(frozen=True)
class Schema(
    schemas.StrSchema
):
    types: typing.FrozenSet[typing.Type] = frozenset({
        str,
    })
    default: str = "-efg"
    enum_value_to_name: typing.Mapping[typing.Union[int, float, str, schemas.Bool, None], str] = dataclasses.field(
        default_factory=lambda: {
            "_abc": "_ABC",
            "-efg": "HYPHEN_MINUS_EFG",
            "(xyz)": "LEFT_PARENTHESIS_XYZ_RIGHT_PARENTHESIS",
        }
    )
    enums = SchemaEnums

    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: typing_extensions.Literal["_abc"],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing_extensions.Literal["_abc"]: ...
    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: typing_extensions.Literal["-efg"],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing_extensions.Literal["-efg"]: ...
    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: typing_extensions.Literal["(xyz)"],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing_extensions.Literal["(xyz)"]: ...
    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: str,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing_extensions.Literal["_abc","-efg","(xyz)",]: ...
    @classmethod
    def validate(
        cls,
        arg,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing_extensions.Literal[
        "_abc",
        "-efg",
        "(xyz)",
    ]:
        validated_arg = super().validate(
            arg,
            configuration=configuration,
        )
        return typing.cast(typing_extensions.Literal[
                "_abc",
                "-efg",
                "(xyz)",
            ],
            validated_arg
        )
