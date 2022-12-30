# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import petstore_api
from petstore_api.paths.fake_refs_object_model_with_ref_props import post  # noqa: E501
from petstore_api import configuration, schemas, api_client

from .. import ApiTestMixin


class TestFakeRefsObjectModelWithRefProps(ApiTestMixin, unittest.TestCase):
    """
    FakeRefsObjectModelWithRefProps unit test stubs
    """
    configuration_ = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self.configuration_)
        self.api = post.ApiForpost(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200
    response_body_schema = post.response_for_200.object_model_with_ref_props.ObjectModelWithRefProps

if __name__ == '__main__':
    unittest.main()
