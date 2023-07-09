# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *



class EnumClassEnums:

    @schemas.classproperty
    def _ABC(cls) -> str:
        return EnumClass.validate("_abc")

    @schemas.classproperty
    def HYPHEN_MINUS_EFG(cls) -> str:
        return EnumClass.validate("-efg")

    @schemas.classproperty
    def LEFT_PARENTHESIS_XYZ_RIGHT_PARENTHESIS(cls) -> str:
        return EnumClass.validate("(xyz)")

    @schemas.classproperty
    def COUNT_1M(cls) -> str:
        return EnumClass.validate("COUNT_1M")

    @schemas.classproperty
    def COUNT_50M(cls) -> str:
        return EnumClass.validate("COUNT_50M")


@dataclasses.dataclass(frozen=True)
class EnumClass(
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """
    types: typing.FrozenSet[typing.Type] = frozenset({
        str,
    })
    default: str = "-efg"
    enum_value_to_name: typing.Mapping[typing.Union[int, float, str, bool, schemas.none_type_], str] = dataclasses.field(
        default_factory=lambda: {
            "_abc": "_ABC",
            "-efg": "HYPHEN_MINUS_EFG",
            "(xyz)": "LEFT_PARENTHESIS_XYZ_RIGHT_PARENTHESIS",
            "COUNT_1M": "COUNT_1M",
            "COUNT_50M": "COUNT_50M",
        }
    )
    enums = EnumClassEnums

    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: typing.Literal["_abc"],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing.Literal["_abc"]: ...
    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: typing.Literal["-efg"],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing.Literal["-efg"]: ...
    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: typing.Literal["(xyz)"],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing.Literal["(xyz)"]: ...
    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: typing.Literal["COUNT_1M"],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing.Literal["COUNT_1M"]: ...
    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: typing.Literal["COUNT_50M"],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing.Literal["COUNT_50M"]: ...
    @classmethod
    def validate(
        cls,
        arg: typing.Union[str, datetime.date, datetime.datetime, uuid.UUID],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing.Literal[
        "_abc",
        "-efg",
        "(xyz)",
        "COUNT_1M",
        "COUNT_50M",
    ]:
        return super().validate(
            arg,
            configuration=configuration,
        )
