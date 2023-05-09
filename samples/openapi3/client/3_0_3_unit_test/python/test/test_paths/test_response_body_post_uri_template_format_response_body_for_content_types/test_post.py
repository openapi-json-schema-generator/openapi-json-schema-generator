# coding: utf-8

"""
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

import unittest
from unittest.mock import patch

import urllib3

import unit_test_api
from unit_test_api.paths.response_body_post_uri_template_format_response_body_for_content_types.post import operation as post  # noqa: E501
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
    response_body_schema = post.response_200.ResponseFor200.content["application/json"].schema
    
    def test_all_string_formats_ignore_objects_passes(self):
        # all string formats ignore objects
        accept_content_type = 'application/json'
    
        with patch.object(urllib3.PoolManager, 'request') as mock_request:
            payload = (
                {
                }
            )
            mock_request.return_value = self.response(
                self.json_bytes(payload),
                status=self.response_status
            )
            api_response = self.api.post(
                accept_content_types=(accept_content_type,)
            )
            self.assert_pool_manager_request_called_with(
                mock_request,
                self.api_config.get_server_url('servers', None) + "/responseBody/postUriTemplateFormatResponseBodyForContentTypes",
                method='post'.upper(),
                accept_content_type=accept_content_type,
            )
    
            assert isinstance(api_response.response, urllib3.HTTPResponse)
            assert isinstance(api_response.body, self.response_body_schema)
            deserialized_response_body = self.response_body_schema.from_openapi_data_(
                payload,
                configuration_=self.schema_config
            )
            assert api_response.body == deserialized_response_body
    
    def test_all_string_formats_ignore_booleans_passes(self):
        # all string formats ignore booleans
        accept_content_type = 'application/json'
    
        with patch.object(urllib3.PoolManager, 'request') as mock_request:
            payload = (
                False
            )
            mock_request.return_value = self.response(
                self.json_bytes(payload),
                status=self.response_status
            )
            api_response = self.api.post(
                accept_content_types=(accept_content_type,)
            )
            self.assert_pool_manager_request_called_with(
                mock_request,
                self.api_config.get_server_url('servers', None) + "/responseBody/postUriTemplateFormatResponseBodyForContentTypes",
                method='post'.upper(),
                accept_content_type=accept_content_type,
            )
    
            assert isinstance(api_response.response, urllib3.HTTPResponse)
            assert isinstance(api_response.body, self.response_body_schema)
            deserialized_response_body = self.response_body_schema.from_openapi_data_(
                payload,
                configuration_=self.schema_config
            )
            assert api_response.body == deserialized_response_body
    
    def test_all_string_formats_ignore_integers_passes(self):
        # all string formats ignore integers
        accept_content_type = 'application/json'
    
        with patch.object(urllib3.PoolManager, 'request') as mock_request:
            payload = (
                12
            )
            mock_request.return_value = self.response(
                self.json_bytes(payload),
                status=self.response_status
            )
            api_response = self.api.post(
                accept_content_types=(accept_content_type,)
            )
            self.assert_pool_manager_request_called_with(
                mock_request,
                self.api_config.get_server_url('servers', None) + "/responseBody/postUriTemplateFormatResponseBodyForContentTypes",
                method='post'.upper(),
                accept_content_type=accept_content_type,
            )
    
            assert isinstance(api_response.response, urllib3.HTTPResponse)
            assert isinstance(api_response.body, self.response_body_schema)
            deserialized_response_body = self.response_body_schema.from_openapi_data_(
                payload,
                configuration_=self.schema_config
            )
            assert api_response.body == deserialized_response_body
    
    def test_all_string_formats_ignore_floats_passes(self):
        # all string formats ignore floats
        accept_content_type = 'application/json'
    
        with patch.object(urllib3.PoolManager, 'request') as mock_request:
            payload = (
                13.7
            )
            mock_request.return_value = self.response(
                self.json_bytes(payload),
                status=self.response_status
            )
            api_response = self.api.post(
                accept_content_types=(accept_content_type,)
            )
            self.assert_pool_manager_request_called_with(
                mock_request,
                self.api_config.get_server_url('servers', None) + "/responseBody/postUriTemplateFormatResponseBodyForContentTypes",
                method='post'.upper(),
                accept_content_type=accept_content_type,
            )
    
            assert isinstance(api_response.response, urllib3.HTTPResponse)
            assert isinstance(api_response.body, self.response_body_schema)
            deserialized_response_body = self.response_body_schema.from_openapi_data_(
                payload,
                configuration_=self.schema_config
            )
            assert api_response.body == deserialized_response_body
    
    def test_all_string_formats_ignore_arrays_passes(self):
        # all string formats ignore arrays
        accept_content_type = 'application/json'
    
        with patch.object(urllib3.PoolManager, 'request') as mock_request:
            payload = (
                [
                ]
            )
            mock_request.return_value = self.response(
                self.json_bytes(payload),
                status=self.response_status
            )
            api_response = self.api.post(
                accept_content_types=(accept_content_type,)
            )
            self.assert_pool_manager_request_called_with(
                mock_request,
                self.api_config.get_server_url('servers', None) + "/responseBody/postUriTemplateFormatResponseBodyForContentTypes",
                method='post'.upper(),
                accept_content_type=accept_content_type,
            )
    
            assert isinstance(api_response.response, urllib3.HTTPResponse)
            assert isinstance(api_response.body, self.response_body_schema)
            deserialized_response_body = self.response_body_schema.from_openapi_data_(
                payload,
                configuration_=self.schema_config
            )
            assert api_response.body == deserialized_response_body
    
    def test_all_string_formats_ignore_nulls_passes(self):
        # all string formats ignore nulls
        accept_content_type = 'application/json'
    
        with patch.object(urllib3.PoolManager, 'request') as mock_request:
            payload = (
                None
            )
            mock_request.return_value = self.response(
                self.json_bytes(payload),
                status=self.response_status
            )
            api_response = self.api.post(
                accept_content_types=(accept_content_type,)
            )
            self.assert_pool_manager_request_called_with(
                mock_request,
                self.api_config.get_server_url('servers', None) + "/responseBody/postUriTemplateFormatResponseBodyForContentTypes",
                method='post'.upper(),
                accept_content_type=accept_content_type,
            )
    
            assert isinstance(api_response.response, urllib3.HTTPResponse)
            assert isinstance(api_response.body, self.response_body_schema)
            deserialized_response_body = self.response_body_schema.from_openapi_data_(
                payload,
                configuration_=self.schema_config
            )
            assert api_response.body == deserialized_response_body

if __name__ == '__main__':
    unittest.main()
