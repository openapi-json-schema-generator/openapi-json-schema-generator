# coding: utf-8

"""
    Example
    No description provided (generated by Openapi JSON Schema Generator https://github.com/openapi-json-schema-tools/openapi-json-schema-generator)  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from json_schema_api.shared_imports.schema_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]



@dataclasses.dataclass(frozen=True)
class AnyTypePatternProperties(
    schemas.AnyTypeSchema[schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES], typing.Tuple[schemas.OUTPUT_BASE_TYPES, ...]],
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """
    # any type
    pattern_properties: typing.Mapping[
        schemas.PatternInfo,
        typing.Type[schemas.Schema]
    ] = dataclasses.field(
        default_factory=lambda: {
            schemas.PatternInfo(
                pattern=r'^S_'  # noqa: E501
            ): S,
            schemas.PatternInfo(
                pattern=r'^I_'  # noqa: E501
            ): I,
        }
    )

