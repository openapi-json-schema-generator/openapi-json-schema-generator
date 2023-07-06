# coding: utf-8

"""
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

import unittest
from unittest.mock import patch

import urllib3
import typing_extensions

import unit_test_api
from unit_test_api.paths.response_body_post_integer_type_matches_integers_response_body_for_content_types.post import operation as post  # noqa: E501
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
    assert response_body_schema is not None
    
    def test_an_object_is_not_an_integer_fails(self):
        # an object is not an integer
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
            with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
                self.api.post(
                    accept_content_types=(accept_content_type,)
                )
            self.assert_pool_manager_request_called_with(
                mock_request,
                self.api_config.get_server_url('servers', None) + "/responseBody/postIntegerTypeMatchesIntegersResponseBodyForContentTypes",
                method='post'.upper(),
                content_type=None,
                accept_content_type=accept_content_type,
            )
    
    def test_a_string_is_not_an_integer_fails(self):
        # a string is not an integer
        accept_content_type = 'application/json'
    
        with patch.object(urllib3.PoolManager, 'request') as mock_request:
            payload = (
                "foo"
            )
            mock_request.return_value = self.response(
                self.json_bytes(payload),
                status=self.response_status
            )
            with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
                self.api.post(
                    accept_content_types=(accept_content_type,)
                )
            self.assert_pool_manager_request_called_with(
                mock_request,
                self.api_config.get_server_url('servers', None) + "/responseBody/postIntegerTypeMatchesIntegersResponseBodyForContentTypes",
                method='post'.upper(),
                content_type=None,
                accept_content_type=accept_content_type,
            )
    
    def test_null_is_not_an_integer_fails(self):
        # null is not an integer
        accept_content_type = 'application/json'
    
        with patch.object(urllib3.PoolManager, 'request') as mock_request:
            payload = (
                None
            )
            mock_request.return_value = self.response(
                self.json_bytes(payload),
                status=self.response_status
            )
            with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
                self.api.post(
                    accept_content_types=(accept_content_type,)
                )
            self.assert_pool_manager_request_called_with(
                mock_request,
                self.api_config.get_server_url('servers', None) + "/responseBody/postIntegerTypeMatchesIntegersResponseBodyForContentTypes",
                method='post'.upper(),
                content_type=None,
                accept_content_type=accept_content_type,
            )
    
    def test_a_float_with_zero_fractional_part_is_an_integer_passes(self):
        # a float with zero fractional part is an integer
        accept_content_type = 'application/json'
    
        with patch.object(urllib3.PoolManager, 'request') as mock_request:
            payload = (
                1.0
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
                self.api_config.get_server_url('servers', None) + "/responseBody/postIntegerTypeMatchesIntegersResponseBodyForContentTypes",
                method='post'.upper(),
                accept_content_type=accept_content_type,
            )
    
            assert isinstance(api_response.response, urllib3.HTTPResponse)
            deserialized_response_body = self.response_body_schema(
                payload,
                configuration=self.schema_config
            )
            assert api_response.body == deserialized_response_body
    
    def test_a_float_is_not_an_integer_fails(self):
        # a float is not an integer
        accept_content_type = 'application/json'
    
        with patch.object(urllib3.PoolManager, 'request') as mock_request:
            payload = (
                1.1
            )
            mock_request.return_value = self.response(
                self.json_bytes(payload),
                status=self.response_status
            )
            with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
                self.api.post(
                    accept_content_types=(accept_content_type,)
                )
            self.assert_pool_manager_request_called_with(
                mock_request,
                self.api_config.get_server_url('servers', None) + "/responseBody/postIntegerTypeMatchesIntegersResponseBodyForContentTypes",
                method='post'.upper(),
                content_type=None,
                accept_content_type=accept_content_type,
            )
    
    def test_a_boolean_is_not_an_integer_fails(self):
        # a boolean is not an integer
        accept_content_type = 'application/json'
    
        with patch.object(urllib3.PoolManager, 'request') as mock_request:
            payload = (
                True
            )
            mock_request.return_value = self.response(
                self.json_bytes(payload),
                status=self.response_status
            )
            with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
                self.api.post(
                    accept_content_types=(accept_content_type,)
                )
            self.assert_pool_manager_request_called_with(
                mock_request,
                self.api_config.get_server_url('servers', None) + "/responseBody/postIntegerTypeMatchesIntegersResponseBodyForContentTypes",
                method='post'.upper(),
                content_type=None,
                accept_content_type=accept_content_type,
            )
    
    def test_an_integer_is_an_integer_passes(self):
        # an integer is an integer
        accept_content_type = 'application/json'
    
        with patch.object(urllib3.PoolManager, 'request') as mock_request:
            payload = (
                1
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
                self.api_config.get_server_url('servers', None) + "/responseBody/postIntegerTypeMatchesIntegersResponseBodyForContentTypes",
                method='post'.upper(),
                accept_content_type=accept_content_type,
            )
    
            assert isinstance(api_response.response, urllib3.HTTPResponse)
            deserialized_response_body = self.response_body_schema(
                payload,
                configuration=self.schema_config
            )
            assert api_response.body == deserialized_response_body
    
    def test_a_string_is_still_not_an_integer_even_if_it_looks_like_one_fails(self):
        # a string is still not an integer, even if it looks like one
        accept_content_type = 'application/json'
    
        with patch.object(urllib3.PoolManager, 'request') as mock_request:
            payload = (
                "1"
            )
            mock_request.return_value = self.response(
                self.json_bytes(payload),
                status=self.response_status
            )
            with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
                self.api.post(
                    accept_content_types=(accept_content_type,)
                )
            self.assert_pool_manager_request_called_with(
                mock_request,
                self.api_config.get_server_url('servers', None) + "/responseBody/postIntegerTypeMatchesIntegersResponseBodyForContentTypes",
                method='post'.upper(),
                content_type=None,
                accept_content_type=accept_content_type,
            )
    
    def test_an_array_is_not_an_integer_fails(self):
        # an array is not an integer
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
            with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
                self.api.post(
                    accept_content_types=(accept_content_type,)
                )
            self.assert_pool_manager_request_called_with(
                mock_request,
                self.api_config.get_server_url('servers', None) + "/responseBody/postIntegerTypeMatchesIntegersResponseBodyForContentTypes",
                method='post'.upper(),
                content_type=None,
                accept_content_type=accept_content_type,
            )

if __name__ == '__main__':
    unittest.main()
