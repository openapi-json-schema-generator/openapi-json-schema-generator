# coding: utf-8

"""
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from petstore_api.shared_imports.header_imports import *

from . import schema


class Parameter1(api_client.PathParameter):
    name = "petId"
    style = api_client.ParameterStyle.SIMPLE
    schema = schema.Schema
    required = True
