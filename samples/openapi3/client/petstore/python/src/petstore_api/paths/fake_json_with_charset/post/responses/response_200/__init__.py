# coding: utf-8

"""
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from petstore_api.shared_imports.response_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]

from .content.application_json_charsetutf8 import schema as application_json_charsetutf8_schema


@dataclasses.dataclass
class ApiResponse(api_response.ApiResponse):
    response: urllib3.HTTPResponse
    body: schemas.OUTPUT_BASE_TYPES
    headers: schemas.Unset = schemas.unset


class ResponseFor200(api_client.OpenApiResponse[ApiResponse]):
    @classmethod
    def get_response(cls, response, headers, body) -> ApiResponse:
        return ApiResponse(response=response, body=body, headers=headers)


    class ApplicationJsonCharsetutf8MediaType(api_client.MediaType):
        schema: typing_extensions.TypeAlias = application_json_charsetutf8_schema.Schema
    content = {
        'application/json; charset=utf-8': ApplicationJsonCharsetutf8MediaType,
    }
