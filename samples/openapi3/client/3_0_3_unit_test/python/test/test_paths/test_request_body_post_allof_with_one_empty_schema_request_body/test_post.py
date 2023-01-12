# coding: utf-8

"""


    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

import unittest
from unittest.mock import patch

import urllib3

import unit_test_api
from unit_test_api.paths.request_body_post_allof_with_one_empty_schema_request_body import post  # noqa: E501
from unit_test_api import configuration, schemas, api_client

from .. import ApiTestMixin


class TestRequestBodyPostAllofWithOneEmptySchemaRequestBody(ApiTestMixin, unittest.TestCase):
    """
    RequestBodyPostAllofWithOneEmptySchemaRequestBody unit test stubs
    """
    configuration_ = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self.configuration_)
        self.api = post.ApiForpost(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200
    response_body = ''

    def test_any_data_is_valid_passes(self):
        content_type = 'org.openapitools.codegen.CodegenKey@63a70a10'
        # any data is valid
        with patch.object(urllib3.PoolManager, 'request') as mock_request:
            payload = (
                1
            )
            body = post.request_body.allof_with_one_empty_schema.AllofWithOneEmptySchema.from_openapi_data_(
                payload,
                configuration_=self.configuration_
            )
            mock_request.return_value = self.response(
                self.json_bytes(self.response_body),
                status=self.response_status
            )
            api_response = self.api.post(
                body=body,
                content_type=content_type
            )
            self.assert_pool_manager_request_called_with(
                mock_request,
                self.configuration_.host + '/requestBody/postAllofWithOneEmptySchemaRequestBody',
                method='post'.upper(),
                body=self.json_bytes(payload),
                content_type=content_type,
            )

            assert isinstance(api_response.response, urllib3.HTTPResponse)
            assert isinstance(api_response.body, schemas.Unset)

if __name__ == '__main__':
    unittest.main()
