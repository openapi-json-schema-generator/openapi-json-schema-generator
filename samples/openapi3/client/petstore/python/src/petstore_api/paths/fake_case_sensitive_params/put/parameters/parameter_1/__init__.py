# coding: utf-8

"""


    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

import typing
import typing_extensions

from petstore_api import api_client

from . import schema


class Parameter1(api_client.QueryParameter):
    name = "SomeVar"
    style = api_client.ParameterStyle.FORM
    schema = schema.Schema
    required = True
    explode = True
