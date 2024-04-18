# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose.  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from openapi_client.shared_imports.response_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]

from .content.application_xml import schema as application_xml_schema
from .content.application_json import schema as application_json_schema


@dataclasses.dataclass(frozen=True)
class ApiResponse(api_response.ApiResponse):
    body: typing.Union[
        application_xml_schema.order.OrderDict,
        application_json_schema.order.OrderDict,
    ]
    headers: schemas.Unset


class ResponseFor200(api_client.OpenApiResponse[ApiResponse]):
    @classmethod
    def get_response(cls, response, headers, body) -> ApiResponse:
        return ApiResponse(response=response, body=body, headers=headers)


    class ApplicationXmlMediaType(api_client.MediaType):
        schema: typing_extensions.TypeAlias = application_xml_schema.Schema


    class ApplicationJsonMediaType(api_client.MediaType):
        schema: typing_extensions.TypeAlias = application_json_schema.Schema
    content = {
        'application/xml': ApplicationXmlMediaType,
        'application/json': ApplicationJsonMediaType,
    }
