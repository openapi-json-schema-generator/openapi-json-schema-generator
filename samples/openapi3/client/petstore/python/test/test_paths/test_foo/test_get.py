# coding: utf-8

"""


    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

import unittest
from unittest.mock import patch

import urllib3

import petstore_api
from petstore_api.paths.foo import get  # noqa: E501
from petstore_api import schemas, api_client
from petstore_api.configurations import api_configuration, schema_configuration

from .. import ApiTestMixin


class TestGet(ApiTestMixin, unittest.TestCase):
    """
    Get unit test stubs
    """
    configuration_ = api_configuration.ApiConfiguration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self.configuration_)
        self.api = get.ApiForGet(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 0
    response_body_schema = get.response_default.Default.content["application/json"].schema

if __name__ == '__main__':
    unittest.main()
