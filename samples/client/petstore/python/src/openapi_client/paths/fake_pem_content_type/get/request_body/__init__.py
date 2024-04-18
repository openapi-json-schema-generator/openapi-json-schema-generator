# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose.  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from openapi_client.shared_imports.header_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]

from .content.application_x_pem_file import schema as application_x_pem_file_schema


class RequestBody(api_client.RequestBody):


    class ApplicationXPemFileMediaType(api_client.MediaType):
        schema: typing_extensions.TypeAlias = application_x_pem_file_schema.Schema
    content = {
        'application/x-pem-file': ApplicationXPemFileMediaType,
    }
