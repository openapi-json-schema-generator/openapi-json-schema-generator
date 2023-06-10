# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *

"""todo define mapping here"""


class IntegerEnumWithDefaultValue(
    schemas.IntSchema[schemas.T]
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """


    @dataclasses.dataclass(frozen=True)
    class Schema_(metaclass=schemas.SingletonMeta):
        types: typing.FrozenSet[typing.Type] = frozenset({
            decimal.Decimal,
        })
        format: str = 'int'
        default: int  = 0
        enum_value_to_name: typing.Mapping[typing.Union[int, float, str, schemas.BoolClass, schemas.NoneClass], str] = dataclasses.field(
            default_factory=lambda: {
                0: "POSITIVE_0",
                1: "POSITIVE_1",
                2: "POSITIVE_2",
            }
        )
    
    @schemas.classproperty
    def POSITIVE_0(cls) -> IntegerEnumWithDefaultValue[decimal.Decimal]:
        return cls(0) # type: ignore
    
    @schemas.classproperty
    def POSITIVE_1(cls) -> IntegerEnumWithDefaultValue[decimal.Decimal]:
        return cls(1) # type: ignore
    
    @schemas.classproperty
    def POSITIVE_2(cls) -> IntegerEnumWithDefaultValue[decimal.Decimal]:
        return cls(2) # type: ignore
