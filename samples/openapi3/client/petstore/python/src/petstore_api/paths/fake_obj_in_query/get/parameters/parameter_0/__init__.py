# coding: utf-8

"""


    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from petstore_api import api_client

from . import schema


class Parameter0(api_client.QueryParameter):
    name = "mapBean"
    style=api_client.ParameterStyle.DEEP_OBJECT
    schema = schema.Schema
    explode = True
