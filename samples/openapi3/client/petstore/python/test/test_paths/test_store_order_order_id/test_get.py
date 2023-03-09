# coding: utf-8

"""


    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

import unittest
from unittest.mock import patch

import urllib3

import petstore_api
from petstore_api.paths. import   # noqa: E501
from petstore_api import configuration, schemas, api_client

from .. import ApiTestMixin


class Test(ApiTestMixin, unittest.TestCase):
    """
     unit test stubs
        Find purchase order by ID  # noqa: E501
    """
    configuration_ = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self.configuration_)
        self.api = .ApiFor(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200
    response_body_schema = .response_200.ResponseFor200.content["application/xml"].schema
    response_body_schema = .response_200.ResponseFor200.content["application/json"].schema

if __name__ == '__main__':
    unittest.main()
