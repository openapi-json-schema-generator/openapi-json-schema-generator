# coding: utf-8

"""
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from petstore_api.shared_imports.response_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]

from .content.application_json import schema as application_json_schema


@dataclasses.dataclass(frozen=True)
class ApiResponse(api_response.ApiResponse):
    body: application_json_schema.object_model_with_ref_props.ObjectModelWithRefPropsDict
    headers: schemas.Unset


class ResponseFor200(api_client.OpenApiResponse[ApiResponse]):
    @classmethod
    def get_response(cls, response, headers, body) -> ApiResponse:
        return ApiResponse(response=response, body=body, headers=headers)


    class ApplicationJsonMediaType(api_client.MediaType):
        schema: typing_extensions.TypeAlias = application_json_schema.Schema
    content = {
        'application/json': ApplicationJsonMediaType,
    }
