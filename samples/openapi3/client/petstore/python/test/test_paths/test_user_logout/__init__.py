# coding: utf-8

"""


    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

import unittest
from unittest.mock import patch

import urllib3

import petstore_api
from petstore_api.paths.user_logout.get import operation as get  # noqa: E501
from petstore_api import schemas, api_client
from petstore_api.configurations import api_configuration, schema_configuration

from .. import ApiTestMixin


class TestGet(ApiTestMixin, unittest.TestCase):
    """
    Get unit test stubs
        Logs out current logged in user session  # noqa: E501
    """
    configuration_ = api_configuration.ApiConfiguration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self.configuration_)
        self.api = get.ApiForGet(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 0
    response_body = ''

if __name__ == '__main__':
    unittest.main()
