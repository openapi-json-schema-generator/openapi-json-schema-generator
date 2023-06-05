# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *



class StringEnumWithDefaultValue(
    schemas.StrSchema[schemas.T]
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """


    @dataclasses.dataclass(frozen=True)
    class Schema_(metaclass=schemas.SingletonMeta):
        types: typing.FrozenSet[typing.Type] = frozenset({
            str,
        })
        default: str = "placed"
        enum_value_to_name: typing.Mapping[typing.Union[int, float, str, schemas.BoolClass, schemas.NoneClass], str] = dataclasses.field(
            default_factory=lambda: {
                "placed": "PLACED",
                "approved": "APPROVED",
                "delivered": "DELIVERED",
            }
        )
    
    @schemas.classproperty
    def PLACED(cls) -> StringEnumWithDefaultValue[str]:
        return cls("placed") # type: ignore
    
    @schemas.classproperty
    def APPROVED(cls) -> StringEnumWithDefaultValue[str]:
        return cls("approved") # type: ignore
    
    @schemas.classproperty
    def DELIVERED(cls) -> StringEnumWithDefaultValue[str]:
        return cls("delivered") # type: ignore
