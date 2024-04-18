# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose.  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from openapi_client.shared_imports.response_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]

from .content.application_json import schema as application_json_schema
from .headers import header_ref_schema_header
from .headers import header_int32
from .headers import header_ref_content_schema_header
from .headers import header_string_header
from .headers import header_number_header
from . import header_parameters
parameters: typing.Dict[str, typing.Type[api_client.HeaderParameterWithoutName]] = {
    'ref-schema-header': header_ref_schema_header.RefSchemaHeader,
    'int32': header_int32.Int32,
    'ref-content-schema-header': header_ref_content_schema_header.RefContentSchemaHeader,
    'stringHeader': header_string_header.StringHeader,
    'numberHeader': header_number_header.NumberHeader,
}


@dataclasses.dataclass(frozen=True)
class ApiResponse(api_response.ApiResponse):
    body: application_json_schema.api_response.ApiResponseDict
    headers: header_parameters.HeadersDict


class SuccessWithJsonApiResponse(api_client.OpenApiResponse[ApiResponse]):
    @classmethod
    def get_response(cls, response, headers, body) -> ApiResponse:
        return ApiResponse(response=response, body=body, headers=headers)


    class ApplicationJsonMediaType(api_client.MediaType):
        schema: typing_extensions.TypeAlias = application_json_schema.Schema
    content = {
        'application/json': ApplicationJsonMediaType,
    }
    headers=parameters
    headers_schema = header_parameters.Headers
