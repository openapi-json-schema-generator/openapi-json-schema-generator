# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

from unit_test_api import api_client, exceptions

from unit_test_api.components.schema import maximum_validation_with_unsigned_integer

class RequestBody(api_client.RequestBody):
    content = {
        'application/json': api_client.MediaType(
            schema=maximum_validation_with_unsigned_integer.MaximumValidationWithUnsignedInteger,
        ),
    }
    required = True
