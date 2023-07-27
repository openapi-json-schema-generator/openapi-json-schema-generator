# coding: utf-8

"""
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

import unittest
from unittest.mock import patch

import urllib3
import typing_extensions

import unit_test_api
from unit_test_api.paths.request_body_post_by_number_request_body.post import operation as post  # noqa: E501
from unit_test_api import schemas, api_client
from unit_test_api.configurations import api_configuration, schema_configuration

from .. import ApiTestMixin


class TestPost(ApiTestMixin, unittest.TestCase):
    """
    Post unit test stubs
    """
    api_config = api_configuration.ApiConfiguration()
    schema_config = schema_configuration.SchemaConfiguration()
    used_api_client = api_client.ApiClient(configuration=api_config, schema_configuration=schema_config)
    api = post.ApiForPost(api_client=used_api_client)  # noqa: E501

    response_status = 200
    response_body = ''

    def test_45_is_multiple_of15_passes(self):
        content_type = 'application/json'
        # 4.5 is multiple of 1.5
        with patch.object(urllib3.PoolManager, 'request') as mock_request:
            payload = (
                4.5
            )
            body = post.request_body.RequestBody.content["application/json"].schema.validate(
                payload,
                configuration=self.schema_config
            )
            body_info = post.request_body.RequestBodyInfoForApplicationJson(body)
            mock_request.return_value = self.response(
                self.json_bytes(self.response_body),
                status=self.response_status
            )
            api_response = self.api.post(
                body_info=body_info,
            )
            self.assert_pool_manager_request_called_with(
                mock_request,
                self.api_config.get_server_url('servers', None) + "/requestBody/postByNumberRequestBody",
                method='post'.upper(),
                body=self.json_bytes(payload),
                content_type=content_type,
            )

            assert isinstance(api_response.response, urllib3.HTTPResponse)
            assert isinstance(api_response.body, schemas.Unset)

    def test_35_is_not_multiple_of15_fails(self):
        content_type = 'application/json'
        # 35 is not multiple of 1.5
        with patch.object(urllib3.PoolManager, 'request') as mock_request:
            payload = (
                35
            )
            with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
                body = post.request_body.RequestBody.content["application/json"].schema.validate(
                    payload,
                    configuration=self.schema_config
                )
                body_info = post.request_body.RequestBodyInfoForApplicationJson(body)
                self.api.post(body_info=body_info)

    def test_zero_is_multiple_of_anything_passes(self):
        content_type = 'application/json'
        # zero is multiple of anything
        with patch.object(urllib3.PoolManager, 'request') as mock_request:
            payload = (
                0
            )
            body = post.request_body.RequestBody.content["application/json"].schema.validate(
                payload,
                configuration=self.schema_config
            )
            body_info = post.request_body.RequestBodyInfoForApplicationJson(body)
            mock_request.return_value = self.response(
                self.json_bytes(self.response_body),
                status=self.response_status
            )
            api_response = self.api.post(
                body_info=body_info,
            )
            self.assert_pool_manager_request_called_with(
                mock_request,
                self.api_config.get_server_url('servers', None) + "/requestBody/postByNumberRequestBody",
                method='post'.upper(),
                body=self.json_bytes(payload),
                content_type=content_type,
            )

            assert isinstance(api_response.response, urllib3.HTTPResponse)
            assert isinstance(api_response.body, schemas.Unset)

if __name__ == '__main__':
    unittest.main()
