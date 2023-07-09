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
    def TRUE(cls) -> str:
        return Schema.validate("true")

    @schemas.classproperty
    def FALSE(cls) -> str:
        return Schema.validate("false")


@dataclasses.dataclass(frozen=True)
class Schema(
    schemas.StrSchema
):
    types: typing.FrozenSet[typing.Type] = frozenset({
        str,
    })
    enum_value_to_name: typing.Mapping[typing.Union[int, float, str, bool, schemas.none_type_], str] = dataclasses.field(
        default_factory=lambda: {
            "true": "TRUE",
            "false": "FALSE",
        }
    )
    enums = SchemaEnums

    @classmethod
    def validate(
        cls,
        arg: typing.Union[str, datetime.date, datetime.datetime, uuid.UUID],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing.Literal[
        "true",
        "false",
    ]:
        return super().validate(
            arg,
            configuration=configuration,
        )
