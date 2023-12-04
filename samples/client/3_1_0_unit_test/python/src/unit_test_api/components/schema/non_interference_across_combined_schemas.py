# coding: utf-8

"""
    openapi 3.1.0 sample spec
    sample spec for testing openapi functionality, built from json schema tests for draft2020-12  # noqa: E501
    The version of the OpenAPI document: 0.0.1
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from unit_test_api.shared_imports.schema_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]

_If: typing_extensions.TypeAlias = schemas.AnyTypeSchema


@dataclasses.dataclass(frozen=True)
class _0(
    schemas.AnyTypeSchema[schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES], typing.Tuple[schemas.OUTPUT_BASE_TYPES, ...]],
):
    # any type
    if_: typing.Type[_If] = dataclasses.field(default_factory=lambda: _If) # type: ignore



@dataclasses.dataclass(frozen=True)
class Then(
    schemas.AnyTypeSchema[schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES], typing.Tuple[schemas.OUTPUT_BASE_TYPES, ...]],
):
    # any type
    inclusive_minimum: typing.Union[int, float] = -10



@dataclasses.dataclass(frozen=True)
class _1(
    schemas.AnyTypeSchema[schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES], typing.Tuple[schemas.OUTPUT_BASE_TYPES, ...]],
):
    # any type
    then: typing.Type[Then] = dataclasses.field(default_factory=lambda: Then) # type: ignore



@dataclasses.dataclass(frozen=True)
class _Else(
    schemas.AnyTypeSchema[schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES], typing.Tuple[schemas.OUTPUT_BASE_TYPES, ...]],
):
    # any type
    multiple_of: typing.Union[int, float] = 2



@dataclasses.dataclass(frozen=True)
class _2(
    schemas.AnyTypeSchema[schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES], typing.Tuple[schemas.OUTPUT_BASE_TYPES, ...]],
):
    # any type
    else_: typing.Type[_Else] = dataclasses.field(default_factory=lambda: _Else) # type: ignore

AllOf = typing.Tuple[
    typing.Type[_0],
    typing.Type[_1],
    typing.Type[_2],
]


@dataclasses.dataclass(frozen=True)
class NonInterferenceAcrossCombinedSchemas(
    schemas.AnyTypeSchema[schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES], typing.Tuple[schemas.OUTPUT_BASE_TYPES, ...]],
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """
    # any type
    all_of: AllOf = dataclasses.field(default_factory=lambda: schemas.tuple_to_instance(AllOf)) # type: ignore

