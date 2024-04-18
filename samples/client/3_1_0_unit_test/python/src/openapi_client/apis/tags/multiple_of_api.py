# coding: utf-8

"""
    openapi 3.1.0 sample spec
    sample spec for testing openapi functionality, built from json schema tests for draft2020-12  # noqa: E501
    The version of the OpenAPI document: 0.0.1
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from openapi_client.paths.response_body_post_by_number_response_body_for_content_types.post.operation import PostByNumberResponseBodyForContentTypes
from openapi_client.paths.request_body_post_by_int_request_body.post.operation import PostByIntRequestBody
from openapi_client.paths.request_body_post_float_division_inf_request_body.post.operation import PostFloatDivisionInfRequestBody
from openapi_client.paths.response_body_post_by_small_number_response_body_for_content_types.post.operation import PostBySmallNumberResponseBodyForContentTypes
from openapi_client.paths.response_body_post_float_division_inf_response_body_for_content_types.post.operation import PostFloatDivisionInfResponseBodyForContentTypes
from openapi_client.paths.request_body_post_by_small_number_request_body.post.operation import PostBySmallNumberRequestBody
from openapi_client.paths.response_body_post_small_multiple_of_large_integer_response_body_for_content_types.post.operation import PostSmallMultipleOfLargeIntegerResponseBodyForContentTypes
from openapi_client.paths.request_body_post_by_number_request_body.post.operation import PostByNumberRequestBody
from openapi_client.paths.request_body_post_small_multiple_of_large_integer_request_body.post.operation import PostSmallMultipleOfLargeIntegerRequestBody
from openapi_client.paths.response_body_post_by_int_response_body_for_content_types.post.operation import PostByIntResponseBodyForContentTypes


class MultipleOfApi(
    PostByNumberResponseBodyForContentTypes,
    PostByIntRequestBody,
    PostFloatDivisionInfRequestBody,
    PostBySmallNumberResponseBodyForContentTypes,
    PostFloatDivisionInfResponseBodyForContentTypes,
    PostBySmallNumberRequestBody,
    PostSmallMultipleOfLargeIntegerResponseBodyForContentTypes,
    PostByNumberRequestBody,
    PostSmallMultipleOfLargeIntegerRequestBody,
    PostByIntResponseBodyForContentTypes,
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """
    pass
