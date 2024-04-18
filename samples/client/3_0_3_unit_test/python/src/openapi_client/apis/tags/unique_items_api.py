# coding: utf-8

"""
    openapi 3.0.3 sample spec
    sample spec for testing openapi functionality, built from json schema tests for draft6  # noqa: E501
    The version of the OpenAPI document: 0.0.1
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from openapi_client.paths.request_body_post_uniqueitems_false_validation_request_body.post.operation import PostUniqueitemsFalseValidationRequestBody
from openapi_client.paths.request_body_post_uniqueitems_validation_request_body.post.operation import PostUniqueitemsValidationRequestBody
from openapi_client.paths.response_body_post_uniqueitems_validation_response_body_for_content_types.post.operation import PostUniqueitemsValidationResponseBodyForContentTypes
from openapi_client.paths.response_body_post_uniqueitems_false_validation_response_body_for_content_types.post.operation import PostUniqueitemsFalseValidationResponseBodyForContentTypes


class UniqueItemsApi(
    PostUniqueitemsFalseValidationRequestBody,
    PostUniqueitemsValidationRequestBody,
    PostUniqueitemsValidationResponseBodyForContentTypes,
    PostUniqueitemsFalseValidationResponseBodyForContentTypes,
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """
    pass
