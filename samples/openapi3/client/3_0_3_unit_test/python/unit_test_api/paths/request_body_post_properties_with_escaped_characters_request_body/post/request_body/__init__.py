# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

from unit_test_api import api_client, exceptions

from unit_test_api.components.schema import properties_with_escaped_characters

class RequestBody(api_client.RequestBody):
    content = {
        'application/json': api_client.MediaType(
            schema=properties_with_escaped_characters.PropertiesWithEscapedCharacters,
        ),
    }
    required = True
