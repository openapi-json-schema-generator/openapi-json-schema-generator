# coding: utf-8

"""


    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

import dataclasses
import datetime
import decimal
import io
import typing
import uuid

import frozendict
import typing_extensions
import urllib3

from petstore_api import api_client
from petstore_api import schemas
from .content.application_xml import schema as application_xml_schema
from .content.application_json import schema as application_json_schema
from .headers import header_ref_schema_header
from .headers import header_x_rate_limit
from .headers import header_int32
from .headers import header_x_expires_after
from .headers import header_ref_content_schema_header
from .headers import header_string_header
from .headers import header_number_header


class Header:
    RequiredParams = typing_extensions.TypedDict(
        'RequiredParams',
        {
            'ref-schema-header': typing.Union[header_ref_schema_header.RefSchemaHeader.schema, dict, frozendict.frozendict, str, datetime.date, datetime.datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader],
            'X-Rate-Limit': typing.Union[header_x_rate_limit.XRateLimit.content["application/json"].schema, decimal.Decimal, int],
            'int32': typing.Union[header_int32.Int32.content["application/json"].schema, decimal.Decimal, int],
            'ref-content-schema-header': typing.Union[header_ref_content_schema_header.RefContentSchemaHeader.content["application/json"].schema, dict, frozendict.frozendict, str, datetime.date, datetime.datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader],
            'stringHeader': typing.Union[header_string_header.StringHeader.schema, str],
        }
    )
    OptionalParams = typing_extensions.TypedDict(
        'OptionalParams',
        {
            'X-Expires-After': typing.Union[header_x_expires_after.XExpiresAfter.schema, str, datetime.datetime],
            'numberHeader': typing.Union[header_number_header.NumberHeader.schema, str],
        },
        total=False
    )


    class Params(RequiredParams, OptionalParams):
        pass


    parameters = [
        header_ref_schema_header.RefSchemaHeader,
        header_x_rate_limit.XRateLimit,
        header_int32.Int32,
        header_x_expires_after.XExpiresAfter,
        header_ref_content_schema_header.RefContentSchemaHeader,
        header_string_header.StringHeader,
        header_number_header.NumberHeader,
    ]

@dataclasses.dataclass
class ApiResponseFor200(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        application_xml_schema.Schema,
        application_json_schema.Schema,
    ]
    headers: Header.Params


class ResponseFor200(api_client.OpenApiResponse[ApiResponseFor200]):
    response_cls = ApiResponseFor200


    class __ApplicationXmlMediaType(api_client.MediaType):
        schema: typing.Type[application_xml_schema.Schema] = application_xml_schema.Schema


    class __ApplicationJsonMediaType(api_client.MediaType):
        schema: typing.Type[application_json_schema.Schema] = application_json_schema.Schema
    __Content = typing_extensions.TypedDict(
        '__Content',
        {
            'application/xml': typing.Type[__ApplicationXmlMediaType],
            'application/json': typing.Type[__ApplicationJsonMediaType],
        }
    )
    content: __Content = {
        'application/xml': __ApplicationXmlMediaType,
        'application/json': __ApplicationJsonMediaType,
    }
    headers=Header.parameters
