# coding: utf-8

"""


    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from petstore_api import api_client, exceptions

from petstore_api.components.schema import string_enum

class RequestBody(api_client.RequestBody):
    content = {
        'application/json': api_client.MediaType(
            schema=string_enum.StringEnum,
        ),
    }
