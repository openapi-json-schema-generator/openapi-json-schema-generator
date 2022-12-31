# coding: utf-8

"""


    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

import unittest
from unittest.mock import patch

import urllib3

import petstore_api
from petstore_api.paths.pet_find_by_tags import get  # noqa: E501
from petstore_api import configuration, schemas, api_client

from .. import ApiTestMixin


class TestPetFindByTags(ApiTestMixin, unittest.TestCase):
    """
    PetFindByTags unit test stubs
        Finds Pets by tags  # noqa: E501
    """
    configuration_ = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self.configuration_)
        self.api = get.ApiForget(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200
    response_body_schema = get.response_for_200.application_xml.ApplicationXml
    response_body_schema = get.response_for_200.application_json.ApplicationJson

if __name__ == '__main__':
    unittest.main()
