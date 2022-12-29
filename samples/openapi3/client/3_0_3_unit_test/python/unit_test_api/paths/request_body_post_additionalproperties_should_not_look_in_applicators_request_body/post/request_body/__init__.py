# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

from unit_test_api import api_client, exceptions

from unit_test_api.components.schema import additionalproperties_should_not_look_in_applicators

class RequestBody(api_client.RequestBody):
    content = {
        'application/json': api_client.MediaType(
            schema=additionalproperties_should_not_look_in_applicators.AdditionalpropertiesShouldNotLookInApplicators,
        ),
    }
    required = True
