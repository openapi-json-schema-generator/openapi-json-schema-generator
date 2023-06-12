# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *

DictInput = typing.Mapping[str, schemas.INPUT_TYPES_ALL_INCL_SCHEMA]
Items2: typing_extensions.TypeAlias = schemas.DictSchema[U]


class Items(
    schemas.ListSchema[schemas.T]
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.

    component's name collides with the inner schema name
    """


    @dataclasses.dataclass(frozen=True)
    class Schema_(metaclass=schemas.SingletonMeta):
        types: typing.FrozenSet[typing.Type] = frozenset({tuple})
        items: typing.Type[Items2] = dataclasses.field(default_factory=lambda: Items2) # type: ignore

    def __new__(
        cls,
        arg_: typing.Sequence[
            typing.Union[
                Items2[frozendict.frozendict],
                dict,
                frozendict.frozendict
            ]
        ],
        configuration_: typing.Optional[schemas.schema_configuration.SchemaConfiguration] = None
    ) -> Items[tuple]:
        inst = super().__new__(
            cls,
            arg_,
            configuration_=configuration_,
        )
        inst = typing.cast(
            Items[tuple],
            inst
        )
        return inst

    def __getitem__(self, name: int) -> Items2[frozendict.frozendict]:
        return super().__getitem__(name)

