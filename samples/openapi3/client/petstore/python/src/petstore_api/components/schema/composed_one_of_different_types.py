# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *

_2: typing_extensions.TypeAlias = schemas.NoneSchema
_3: typing_extensions.TypeAlias = schemas.DateSchema


@dataclasses.dataclass(frozen=True)
class _4(
    schemas.DictSchema[immutabledict.immutabledict[str, schemas.OUTPUT_BASE_TYPES]]
):
    types: typing.FrozenSet[typing.Type] = frozenset({immutabledict.immutabledict})
    max_properties: int = 4
    min_properties: int = 4

    @classmethod
    def validate(
        cls,
        arg: typing.Mapping[str, schemas.INPUT_TYPES_ALL_INCL_SCHEMA],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> immutabledict.immutabledict[str, schemas.INPUT_TYPES_ALL_INCL_SCHEMA]:
        return super().validate(
            arg,
            configuration=configuration,
        )

Items: typing_extensions.TypeAlias = schemas.AnyTypeSchema


class _5Tuple(typing.Tuple[schemas.OUTPUT_BASE_TYPES]):
    def __getitem__(self, name: int) -> schemas.OUTPUT_BASE_TYPES:
        return super().__getitem__(name)
_5TupleInput = typing.Sequence[
    typing.Union[
        dict,
        immutabledict.immutabledict,
        str,
        datetime.date,
        datetime.datetime,
        uuid.UUID,
        int,
        float,
        bool,
        None,
        list,
        tuple,
        bytes,
        io.FileIO,
        io.BufferedReader
    ],
]


@dataclasses.dataclass(frozen=True)
class _5(
    schemas.ListSchema[_5Tuple]
):
    types: typing.FrozenSet[typing.Type] = frozenset({tuple})
    max_items: int = 4
    min_items: int = 4
    items: typing.Type[Items] = dataclasses.field(default_factory=lambda: Items) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            tuple: _5Tuple
        }
    )

    @classmethod
    def validate(
        cls,
        arg: typing.Union[
            _5TupleInput,
            _5Tuple,
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> _5Tuple:
        return super().validate(
            arg,
            configuration=configuration,
        )


@dataclasses.dataclass(frozen=True)
class _6(
    schemas.DateTimeSchema
):
    types: typing.FrozenSet[typing.Type] = frozenset({
        str,
    })
    format: str = 'date-time'
    pattern: schemas.PatternInfo = schemas.PatternInfo(
        pattern=r'^2020.*'  # noqa: E501
    )


@dataclasses.dataclass(frozen=True)
class ComposedOneOfDifferentTypes(
    schemas.AnyTypeSchema[immutabledict.immutabledict[str, schemas.OUTPUT_BASE_TYPES], typing.Tuple[schemas.OUTPUT_BASE_TYPES, ...]],
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.

    this is a model that allows payloads of type object or number
    """
    # any type
    one_of: OneOf = dataclasses.field(default_factory=lambda: schemas.tuple_to_instance(OneOf)) # type: ignore


from petstore_api.components.schema import animal
from petstore_api.components.schema import number_with_validations
OneOf = typing.Tuple[
    typing.Type[number_with_validations.NumberWithValidations],
    typing.Type[animal.Animal],
    typing.Type[_2],
    typing.Type[_3],
    typing.Type[_4],
    typing.Type[_5],
    typing.Type[_6],
]
