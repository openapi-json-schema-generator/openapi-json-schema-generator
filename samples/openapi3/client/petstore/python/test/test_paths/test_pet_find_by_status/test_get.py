# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import petstore_api
from petstore_api.paths.pet_find_by_status import get  # noqa: E501
from petstore_api import configuration, schemas, api_client

from .. import ApiTestMixin


class TestPetFindByStatus(ApiTestMixin, unittest.TestCase):
    """
    PetFindByStatus unit test stubs
        Finds Pets by status  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = get.ApiForget(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 
    response_body_schema = get.response_for_.application_xml


    response_body_schema = get.response_for_.application_json




if __name__ == '__main__':
    unittest.main()
