# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose.  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from openapi_client.shared_imports.response_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]


@dataclasses.dataclass(frozen=True)
class ApiResponse(api_response.ApiResponse):
    body: schemas.Unset
    headers: schemas.Unset


class ResponseFor303(api_client.OpenApiResponse[ApiResponse]):
    @classmethod
    def get_response(cls, response, headers, body) -> ApiResponse:
        return ApiResponse(response=response, body=body, headers=headers)
