# coding: utf-8

"""
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from petstore_api.shared_imports.header_imports import *

from .content.application_json import schema as application_json_schema


class Parameter0(api_client.QueryParameter):
    name = "someParam"


    class ApplicationJsonMediaType(api_client.MediaType):
        schema: typing_extensions.TypeAlias = application_json_schema.Schema[typing.Union[
            frozendict.frozendict,
            str,
            decimal.Decimal,
            schemas.BoolClass,
            schemas.NoneClass,
            tuple,
            bytes,
            schemas.FileIO
        ]]
    content: typing.Tuple[str, typing.Type[ApplicationJsonMediaType]] = (
        'application/json',
        ApplicationJsonMediaType,
    )
    required = True
