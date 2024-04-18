# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose.  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from openapi_client.shared_imports.schema_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]



class IntegerEnumBigEnums:

    @schemas.classproperty
    def POSITIVE_10(cls) -> typing.Literal[10]:
        return IntegerEnumBig.validate(10)

    @schemas.classproperty
    def POSITIVE_11(cls) -> typing.Literal[11]:
        return IntegerEnumBig.validate(11)

    @schemas.classproperty
    def POSITIVE_12(cls) -> typing.Literal[12]:
        return IntegerEnumBig.validate(12)


@dataclasses.dataclass(frozen=True)
class IntegerEnumBig(
    schemas.Schema
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """
    types: typing.FrozenSet[typing.Type] = frozenset({
        int,
    })
    format: str = 'int'
    enum_value_to_name: typing.Mapping[typing.Union[int, float, str, schemas.Bool, None], str] = dataclasses.field(
        default_factory=lambda: {
            10: "POSITIVE_10",
            11: "POSITIVE_11",
            12: "POSITIVE_12",
        }
    )
    enums = IntegerEnumBigEnums

    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: typing.Literal[10],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing.Literal[10]: ...
    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: typing.Literal[11],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing.Literal[11]: ...
    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: typing.Literal[12],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing.Literal[12]: ...
    @typing.overload
    @classmethod
    def validate(
        cls,
        arg: int,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing.Literal[10,11,12,]: ...
    @classmethod
    def validate(
        cls,
        arg,
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> typing.Literal[
        10,
        11,
        12,
    ]:
        validated_arg = super().validate_base(
            arg,
            configuration=configuration,
        )
        return typing.cast(typing.Literal[
                10,
                11,
                12,
            ],
            validated_arg
        )
