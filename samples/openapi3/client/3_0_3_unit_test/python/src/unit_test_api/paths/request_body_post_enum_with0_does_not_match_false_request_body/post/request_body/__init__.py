# coding: utf-8

"""


    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

import typing
import typing_extensions

from unit_test_api import api_client, exceptions

from unit_test_api.components.schema import enum_with0_does_not_match_false

class RequestBody(api_client.RequestBody):


    class __ApplicationJsonMediaType(api_client.MediaType):
        schema: typing.Type[enum_with0_does_not_match_false.EnumWith0DoesNotMatchFalse] = enum_with0_does_not_match_false.EnumWith0DoesNotMatchFalse
    __Content = typing_extensions.TypedDict(
        '__Content',
        {
            'application/json': __ApplicationJsonMediaType,
        }
    )
    content: __Content = {
        'application/json': __ApplicationJsonMediaType,
    }
    required = True
