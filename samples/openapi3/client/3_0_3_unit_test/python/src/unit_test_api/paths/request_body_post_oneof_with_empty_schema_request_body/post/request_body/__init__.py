# coding: utf-8

"""


    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

import typing

from unit_test_api import api_client, exceptions

from unit_test_api.components.schema import oneof_with_empty_schema

class RequestBody(api_client.RequestBody):


    class __ApplicationJsonMediaType(api_client.MediaType):
        schema: typing.Type[oneof_with_empty_schema.OneofWithEmptySchema] = oneof_with_empty_schema.OneofWithEmptySchema
    __Content = typing.TypedDict(
        '__Content',
        {
            'application/json': __ApplicationJsonMediaType,
        }
    )
    content: __Content = {
        'application/json': __ApplicationJsonMediaType,
    }
    required = True
