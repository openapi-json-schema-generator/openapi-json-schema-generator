# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

from unit_test_api import api_client, exceptions

from unit_test_api.components.schema import null_type_matches_only_the_null_object

class RequestBody(api_client.RequestBody):
    content = {
        'application/json': api_client.MediaType(
            schema=null_type_matches_only_the_null_object.NullTypeMatchesOnlyTheNullObject,
        ),
    }
    required = True
