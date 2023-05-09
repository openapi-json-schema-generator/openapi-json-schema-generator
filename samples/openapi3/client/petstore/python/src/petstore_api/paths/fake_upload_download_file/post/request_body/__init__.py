# coding: utf-8

"""
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from petstore_api.shared_imports.header_imports import *

from .content.application_octet_stream import schema as application_octet_stream_schema

class RequestBody(api_client.RequestBody):


    class __ApplicationOctetStreamMediaType(api_client.MediaType):
        schema: typing.Type[application_octet_stream_schema.Schema] = application_octet_stream_schema.Schema
    __Content = typing_extensions.TypedDict(
        '__Content',
        {
            'application/octet-stream': typing.Type[__ApplicationOctetStreamMediaType],
        }
    )
    content: __Content = {
        'application/octet-stream': __ApplicationOctetStreamMediaType,
    }
    required = True
