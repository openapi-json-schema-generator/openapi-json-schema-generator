# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

from unit_test_api import api_client, exceptions

from unit_test_api.components.schema import email_format

class RequestBody(api_client.RequestBody):
    content = {
        'application/json': api_client.MediaType(
            schema=email_format.EmailFormat,
        ),
    }
    required = True
