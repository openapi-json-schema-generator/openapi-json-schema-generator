# coding: utf-8

"""
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from unit_test_api.shared_imports.response_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]

from .content.application_json import schema as application_json_schema


@dataclasses.dataclass(frozen=True)
class ApiResponse(api_response.ApiResponse):
    body: application_json_schema.items_does_not_look_in_applicators_valid_case.ItemsDoesNotLookInApplicatorsValidCaseTuple
    headers: schemas.Unset


class _200(api_client.OpenApiResponse[ApiResponse]):
    @classmethod
    def get_response(cls, response, headers, body) -> ApiResponse:
        return ApiResponse(response=response, body=body, headers=headers)


    class ApplicationJsonMediaType(api_client.MediaType):
        schema: typing_extensions.TypeAlias = application_json_schema.Schema2
    content = {
        'application/json': ApplicationJsonMediaType,
    }
