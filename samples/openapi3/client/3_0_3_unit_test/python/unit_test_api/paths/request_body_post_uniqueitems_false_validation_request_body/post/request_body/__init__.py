# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

from unit_test_api import api_client, exceptions

from unit_test_api.components.schema import uniqueitems_false_validation

parameter_oapg = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=uniqueitems_false_validation.UniqueitemsFalseValidation,
        ),
    },
    required=True,
)
