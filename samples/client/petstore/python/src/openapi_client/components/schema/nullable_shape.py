# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose.  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from openapi_client.shared_imports.schema_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]

_2: typing_extensions.TypeAlias = schemas.NoneSchema
OneOf = typing.Tuple[
    typing.Type[triangle.Triangle],
    typing.Type[quadrilateral.Quadrilateral],
    typing.Type[_2],
]


@dataclasses.dataclass(frozen=True)
class NullableShape(
    schemas.AnyTypeSchema[schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES], typing.Tuple[schemas.OUTPUT_BASE_TYPES, ...]],
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.

    The value may be a shape or the 'null' value. For a composed schema to validate a null payload, one of its chosen oneOf schemas must be type null or nullable (introduced in OAS schema >= 3.0)
    """
    # any type
    one_of: OneOf = dataclasses.field(default_factory=lambda: schemas.tuple_to_instance(OneOf)) # type: ignore

