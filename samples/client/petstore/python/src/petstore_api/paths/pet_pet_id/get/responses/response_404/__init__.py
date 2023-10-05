# coding: utf-8

"""
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from petstore_api.shared_imports.response_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]


class ApiResponse(api_response.ApiResponse):
    def __init__(
        self,
        *,
        response: urllib3.HTTPResponse,
        body: schemas.Unset = schemas.unset,
        headers: schemas.Unset = schemas.unset
    ):
        self.response = response
        self.body = body
        self.headers = headers


class ResponseFor404(api_client.OpenApiResponse[ApiResponse]):
    @classmethod
    def get_response(cls, response, headers, body) -> ApiResponse:
        return ApiResponse(response=response, body=body, headers=headers)
