# coding: utf-8

"""
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

import unittest
from unittest.mock import patch

import urllib3

import petstore_api
from petstore_api.paths.another_fake_dummy.patch import operation as patch  # noqa: E501
from petstore_api import schemas, api_client
from petstore_api.configurations import api_configuration, schema_configuration

from .. import ApiTestMixin


class TestPatch(ApiTestMixin, unittest.TestCase):
    """
    Patch unit test stubs
        To test special tags  # noqa: E501
    """
    api_config = api_configuration.ApiConfiguration()
    schema_config = schema_configuration.SchemaConfiguration()
    used_api_client = api_client.ApiClient(configuration=api_config, schema_configuration=schema_config)
    api = patch.ApiForPatch(api_client=used_api_client)  # noqa: E501

    response_status = 200
    response_body_schema = patch.response_200.ResponseFor200.content["application/json"].schema

if __name__ == '__main__':
    unittest.main()
