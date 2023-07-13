# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from petstore_api.shared_imports.schema_imports import *

_0: typing_extensions.TypeAlias = schemas.DictSchema
_1: typing_extensions.TypeAlias = schemas.DateSchema
_2: typing_extensions.TypeAlias = schemas.DateTimeSchema
_3: typing_extensions.TypeAlias = schemas.BinarySchema
_4: typing_extensions.TypeAlias = schemas.StrSchema
_5: typing_extensions.TypeAlias = schemas.StrSchema
_6: typing_extensions.TypeAlias = schemas.DictSchema
_7: typing_extensions.TypeAlias = schemas.BoolSchema
_8: typing_extensions.TypeAlias = schemas.NoneSchema
Items: typing_extensions.TypeAlias = schemas.AnyTypeSchema


class _9Tuple(
    typing.Tuple[
        schemas.OUTPUT_BASE_TYPES,
        ...
    ]
):
    def __getitem__(self, name: int) -> schemas.OUTPUT_BASE_TYPES:
        return super().__getitem__(name)

    def __new__(cls, arg: _9TupleInput, configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None):
        return _9.validate(arg, configuration=configuration)
_9TupleInput = typing.Union[
    typing.List[
        typing.Union[
            dict,
            schemas.immutabledict,
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
    ],
    typing.Tuple[
        typing.Union[
            dict,
            schemas.immutabledict,
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
        ...
    ]
]


@dataclasses.dataclass(frozen=True)
class _9(
    schemas.Schema[schemas.immutabledict, _9Tuple]
):
    types: typing.FrozenSet[typing.Type] = frozenset({tuple})
    items: typing.Type[Items] = dataclasses.field(default_factory=lambda: Items) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            tuple: _9Tuple
        }
    )

    @classmethod
    def validate(
        cls,
        arg: typing.Union[
            _9TupleInput,
            _9Tuple,
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> _9Tuple:
        return super().validate_base(
            arg,
            configuration=configuration,
        )
_10: typing_extensions.TypeAlias = schemas.NumberSchema
_11: typing_extensions.TypeAlias = schemas.Float32Schema
_12: typing_extensions.TypeAlias = schemas.Float64Schema
_13: typing_extensions.TypeAlias = schemas.IntSchema
_14: typing_extensions.TypeAlias = schemas.Int32Schema
_15: typing_extensions.TypeAlias = schemas.Int64Schema
AnyOf = typing.Tuple[
    typing.Type[_0],
    typing.Type[_1],
    typing.Type[_2],
    typing.Type[_3],
    typing.Type[_4],
    typing.Type[_5],
    typing.Type[_6],
    typing.Type[_7],
    typing.Type[_8],
    typing.Type[_9],
    typing.Type[_10],
    typing.Type[_11],
    typing.Type[_12],
    typing.Type[_13],
    typing.Type[_14],
    typing.Type[_15],
]


@dataclasses.dataclass(frozen=True)
class ComposedAnyOfDifferentTypesNoValidations(
    schemas.AnyTypeSchema[schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES], typing.Tuple[schemas.OUTPUT_BASE_TYPES, ...]],
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """
    # any type
    any_of: AnyOf = dataclasses.field(default_factory=lambda: schemas.tuple_to_instance(AnyOf)) # type: ignore

