# coding: utf-8

"""
    openapi 3.1.0 sample spec
    sample spec for testing openapi functionality, built from json schema tests for draft2020-12  # noqa: E501
    The version of the OpenAPI document: 0.0.1
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from unit_test_api.paths.request_body_post_contains_with_null_instance_elements_request_body.post.operation import PostContainsWithNullInstanceElementsRequestBody
from unit_test_api.paths.response_body_post_contains_with_null_instance_elements_response_body_for_content_types.post.operation import PostContainsWithNullInstanceElementsResponseBodyForContentTypes
from unit_test_api.paths.request_body_post_items_contains_request_body.post.operation import PostItemsContainsRequestBody
from unit_test_api.paths.request_body_post_contains_keyword_validation_request_body.post.operation import PostContainsKeywordValidationRequestBody
from unit_test_api.paths.response_body_post_contains_keyword_validation_response_body_for_content_types.post.operation import PostContainsKeywordValidationResponseBodyForContentTypes
from unit_test_api.paths.response_body_post_items_contains_response_body_for_content_types.post.operation import PostItemsContainsResponseBodyForContentTypes


class ContainsApi(
    PostContainsWithNullInstanceElementsRequestBody,
    PostContainsWithNullInstanceElementsResponseBodyForContentTypes,
    PostItemsContainsRequestBody,
    PostContainsKeywordValidationRequestBody,
    PostContainsKeywordValidationResponseBodyForContentTypes,
    PostItemsContainsResponseBodyForContentTypes,
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """
    pass
