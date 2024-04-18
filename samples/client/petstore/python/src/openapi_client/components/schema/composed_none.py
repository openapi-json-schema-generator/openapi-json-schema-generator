# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose.  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from openapi_client.shared_imports.schema_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]

_0: typing_extensions.TypeAlias = schemas.AnyTypeSchema
AllOf = typing.Tuple[
    typing.Type[_0],
]


@dataclasses.dataclass(frozen=True)
class ComposedNone(
    schemas.NoneSchema
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """
    types: typing.FrozenSet[typing.Type] = frozenset({
        type(None),
    })
    all_of: AllOf = dataclasses.field(default_factory=lambda: schemas.tuple_to_instance(AllOf)) # type: ignore

