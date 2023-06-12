# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *

Items: typing_extensions.TypeAlias = schemas.StrSchema[U]


class Schema(
    schemas.ListSchema[schemas.T]
):


    @dataclasses.dataclass(frozen=True)
    class Schema_(metaclass=schemas.SingletonMeta):
        types: typing.FrozenSet[typing.Type] = frozenset({tuple})
        items: typing.Type[Items] = dataclasses.field(default_factory=lambda: Items) # type: ignore

    def __new__(
        cls,
        arg: typing.Sequence[
            typing.Union[
                Items[str],
                str
            ]
        ],
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None
    ) -> Schema[tuple]:
        inst = super().__new__(
            cls,
            arg,
            configuration_=configuration_,
        )
        inst = typing.cast(
            Schema[tuple],
            inst
        )
        return inst

    def __getitem__(self, name: int) -> Items[str]:
        return super().__getitem__(name)

