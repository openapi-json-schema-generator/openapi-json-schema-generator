# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose.  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from openapi_client.shared_imports.header_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]

from . import schema


class Parameter5(api_client.HeaderParameter):
    name = "1"
    style = api_client.ParameterStyle.SIMPLE
    schema: typing_extensions.TypeAlias = schema.Schema
