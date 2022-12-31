# coding: utf-8

"""


    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from unit_test_api import api_client, exceptions

from unit_test_api.components.schema import invalid_instance_should_not_raise_error_when_float_division_inf

class RequestBody(api_client.RequestBody):
    content = {
        'application/json': api_client.MediaType(
            schema=invalid_instance_should_not_raise_error_when_float_division_inf.InvalidInstanceShouldNotRaiseErrorWhenFloatDivisionInf,
        ),
    }
    required = True
