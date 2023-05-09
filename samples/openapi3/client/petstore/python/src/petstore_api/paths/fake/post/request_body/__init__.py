# coding: utf-8

"""
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from petstore_api.shared_imports.typing_imports import *

from .content.application_x_www_form_urlencoded import schema as application_x_www_form_urlencoded_schema

class RequestBody(api_client.RequestBody):


    class __ApplicationXWwwFormUrlencodedMediaType(api_client.MediaType):
        schema: typing.Type[application_x_www_form_urlencoded_schema.Schema] = application_x_www_form_urlencoded_schema.Schema
    __Content = typing_extensions.TypedDict(
        '__Content',
        {
            'application/x-www-form-urlencoded': typing.Type[__ApplicationXWwwFormUrlencodedMediaType],
        }
    )
    content: __Content = {
        'application/x-www-form-urlencoded': __ApplicationXWwwFormUrlencodedMediaType,
    }
