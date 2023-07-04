# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *


from petstore_api.components.schema import ref_pet


class SchemaTuple(typing.Tuple[schemas.OUTPUT_BASE_TYPES]):
    def __getitem__(self, name: int) -> ref_pet.pet.PetDict:
        return super().__getitem__(name)
SchemaTupleInput = typing.Sequence[
    typing.Union[
        ref_pet.pet.PetDict,
        dict,
        immutabledict.immutabledict
    ],
]


@dataclasses.dataclass(frozen=True)
class Schema(
    schemas.ListSchema[SchemaTuple]
):
    types: typing.FrozenSet[typing.Type] = frozenset({tuple})
    items: typing.Type[ref_pet.RefPet] = dataclasses.field(default_factory=lambda: ref_pet.RefPet) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            tuple: SchemaTuple
        }
    )

    @classmethod
    def validate(
        cls,
        arg: typing.Union[
            SchemaTupleInput,
            SchemaTuple,
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> SchemaTuple:
        return super().validate(
            arg,
            configuration=configuration,
        )
