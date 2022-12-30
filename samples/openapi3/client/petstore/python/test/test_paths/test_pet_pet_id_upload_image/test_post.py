# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import petstore_api
from petstore_api.paths.pet_pet_id_upload_image import post  # noqa: E501
from petstore_api import configuration, schemas, api_client

from .. import ApiTestMixin


class TestPetPetIdUploadImage(ApiTestMixin, unittest.TestCase):
    """
    PetPetIdUploadImage unit test stubs
        uploads an image  # noqa: E501
    """
    configuration_ = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self.configuration_)
        self.api = post.ApiForpost(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200
    response_body_schema = post.response_for_200.api_response.ApiResponse

if __name__ == '__main__':
    unittest.main()
