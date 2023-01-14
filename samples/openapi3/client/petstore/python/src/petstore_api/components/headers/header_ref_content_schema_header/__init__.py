# coding: utf-8

"""


    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from dataclasses import dataclass
import typing_extensions
import urllib3

from petstore_api import api_client, exceptions


class RefContentSchemaHeader(api_client.HeaderParameterWithoutName):
    style = api_client.ParameterStyle.SIMPLE
    content = {
        "application/json": schema.Schema,
    }
    required = True
