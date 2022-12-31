# coding: utf-8

"""


    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from unit_test_api import api_client, exceptions

from unit_test_api.components.schema import nested_allof_to_check_validation_semantics

class RequestBody(api_client.RequestBody):
    content = {
        'application/json': api_client.MediaType(
            schema=nested_allof_to_check_validation_semantics.NestedAllofToCheckValidationSemantics,
        ),
    }
    required = True
