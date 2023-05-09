# coding: utf-8

"""
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from petstore_api.shared_imports.response_imports import *


@dataclasses.dataclass
class ApiDefault(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: schemas.Unset = schemas.unset
    headers: schemas.Unset = schemas.unset


class Default(api_client.OpenApiResponse[ApiDefault]):
    response_cls = ApiDefault
