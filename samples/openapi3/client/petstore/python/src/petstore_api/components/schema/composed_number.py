# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *

_0: typing_extensions.TypeAlias = schemas.AnyTypeSchema[U]


class ComposedNumber(
    schemas.NumberSchema[schemas.T]
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """


    @dataclasses.dataclass(frozen=True)
    class Schema_(metaclass=schemas.SchemaBase):
        types: typing.FrozenSet[typing.Type] = frozenset({
            decimal.Decimal,
        })
        all_of: ComposedNumberAllOf = dataclasses.field(default_factory=lambda: schemas.tuple_to_instance(ComposedNumberAllOf)) # type: ignore


    def __new__(
        cls,
        arg_: typing.Union[decimal.Decimal, int, float],
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None,
    ) -> ComposedNumber[decimal.Decimal]:
        inst = super().__new__(
            cls,
            arg_,
            configuration_=configuration_,
        )
        inst = typing.cast(
            ComposedNumber[decimal.Decimal],
            inst
        )
        return inst

ComposedNumberAllOf = typing.Tuple[
    typing.Type[_0],
]
