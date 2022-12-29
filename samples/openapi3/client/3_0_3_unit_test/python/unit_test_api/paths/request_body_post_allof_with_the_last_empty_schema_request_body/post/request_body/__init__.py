# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

from unit_test_api import api_client, exceptions

from unit_test_api.components.schema import allof_with_the_last_empty_schema

class RequestBody(api_client.RequestBody):
    content = {
        'application/json': api_client.MediaType(
            schema=allof_with_the_last_empty_schema.AllofWithTheLastEmptySchema,
        ),
    }
    required = True
