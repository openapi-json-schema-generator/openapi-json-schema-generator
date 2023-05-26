# coding: utf-8

"""
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from petstore_api.shared_imports.header_imports import *

from .content.application_json import schema as application_json_schema
from .content.application_xml import schema as application_xml_schema

class Pet(api_client.RequestBody):


    class ApplicationJsonMediaType(api_client.MediaType):
        schema: typing_extensions.TypeAlias = application_json_schema.Schema[frozendict.frozendict]


    class ApplicationXmlMediaType(api_client.MediaType):
        schema: typing_extensions.TypeAlias = application_xml_schema.Schema[frozendict.frozendict]
    Content = typing_extensions.TypedDict(
        'Content',
        {
            'application/json': typing.Type[ApplicationJsonMediaType],
            'application/xml': typing.Type[ApplicationXmlMediaType],
        }
    )
    content: Content = {
        'application/json': ApplicationJsonMediaType,
        'application/xml': ApplicationXmlMediaType,
    }
    required = True
