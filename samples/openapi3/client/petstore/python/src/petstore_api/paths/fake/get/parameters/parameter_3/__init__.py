# coding: utf-8

"""


    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from petstore_api import api_client

from . import schema


class Parameter3(api_client.QueryParameter):
    name = "enum_query_string"
    style = api_client.ParameterStyle.FORM
    schema = schema.Schema
    explode = True
