# coding: utf-8

"""
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from petstore_api.shared_imports.header_imports import *

from . import schema


class RefSchemaStringWithValidation(api_client.PathParameter):
    name = "RSstringWithValidation"
    style = api_client.ParameterStyle.SIMPLE
    schema: typing_extensions.TypeAlias = schema.Schema[str]
    required = True
