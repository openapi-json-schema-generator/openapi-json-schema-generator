# coding: utf-8

"""


    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from petstore_api import api_client, exceptions
from . import schema

class UserArray(api_client.RequestBody):
    content = {
        'application/json': api_client.MediaType(
            schema=schema.Schema,
        ),
    }
    required = True
