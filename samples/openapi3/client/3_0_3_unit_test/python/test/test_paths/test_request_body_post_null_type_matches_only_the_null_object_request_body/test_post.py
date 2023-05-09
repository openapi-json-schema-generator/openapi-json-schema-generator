# coding: utf-8

"""


    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

import unittest
from unittest.mock import patch

import urllib3

import unit_test_api
from unit_test_api.paths.request_body_post_null_type_matches_only_the_null_object_request_body.post import operation as post  # noqa: E501
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

    def test_a_float_is_not_null_fails(self):
        content_type = 'application/json'
        # a float is not null
        with patch.object(urllib3.PoolManager, 'request') as mock_request:
            payload = (
                1.1
            )
            with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
                body = post.request_body.RequestBody.content["application/json"].schema.from_openapi_data_(
                    payload,
                    configuration_=self.schema_config
                )
                self.api.post(body=body)

    def test_an_object_is_not_null_fails(self):
        content_type = 'application/json'
        # an object is not null
        with patch.object(urllib3.PoolManager, 'request') as mock_request:
            payload = (
                {
                }
            )
            with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
                body = post.request_body.RequestBody.content["application/json"].schema.from_openapi_data_(
                    payload,
                    configuration_=self.schema_config
                )
                self.api.post(body=body)

    def test_false_is_not_null_fails(self):
        content_type = 'application/json'
        # false is not null
        with patch.object(urllib3.PoolManager, 'request') as mock_request:
            payload = (
                False
            )
            with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
                body = post.request_body.RequestBody.content["application/json"].schema.from_openapi_data_(
                    payload,
                    configuration_=self.schema_config
                )
                self.api.post(body=body)

    def test_an_integer_is_not_null_fails(self):
        content_type = 'application/json'
        # an integer is not null
        with patch.object(urllib3.PoolManager, 'request') as mock_request:
            payload = (
                1
            )
            with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
                body = post.request_body.RequestBody.content["application/json"].schema.from_openapi_data_(
                    payload,
                    configuration_=self.schema_config
                )
                self.api.post(body=body)

    def test_true_is_not_null_fails(self):
        content_type = 'application/json'
        # true is not null
        with patch.object(urllib3.PoolManager, 'request') as mock_request:
            payload = (
                True
            )
            with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
                body = post.request_body.RequestBody.content["application/json"].schema.from_openapi_data_(
                    payload,
                    configuration_=self.schema_config
                )
                self.api.post(body=body)

    def test_zero_is_not_null_fails(self):
        content_type = 'application/json'
        # zero is not null
        with patch.object(urllib3.PoolManager, 'request') as mock_request:
            payload = (
                0
            )
            with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
                body = post.request_body.RequestBody.content["application/json"].schema.from_openapi_data_(
                    payload,
                    configuration_=self.schema_config
                )
                self.api.post(body=body)

    def test_an_empty_string_is_not_null_fails(self):
        content_type = 'application/json'
        # an empty string is not null
        with patch.object(urllib3.PoolManager, 'request') as mock_request:
            payload = (
                ""
            )
            with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
                body = post.request_body.RequestBody.content["application/json"].schema.from_openapi_data_(
                    payload,
                    configuration_=self.schema_config
                )
                self.api.post(body=body)

    def test_null_is_null_passes(self):
        content_type = 'application/json'
        # null is null
        with patch.object(urllib3.PoolManager, 'request') as mock_request:
            payload = (
                None
            )
            body = post.request_body.RequestBody.content["application/json"].schema.from_openapi_data_(
                payload,
                configuration_=self.schema_config
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
                self.api_config.get_server_url('servers', None) + "/requestBody/postNullTypeMatchesOnlyTheNullObjectRequestBody",
                method='post'.upper(),
                body=self.json_bytes(payload),
                content_type=content_type,
            )

            assert isinstance(api_response.response, urllib3.HTTPResponse)
            assert isinstance(api_response.body, schemas.Unset)

    def test_an_array_is_not_null_fails(self):
        content_type = 'application/json'
        # an array is not null
        with patch.object(urllib3.PoolManager, 'request') as mock_request:
            payload = (
                [
                ]
            )
            with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
                body = post.request_body.RequestBody.content["application/json"].schema.from_openapi_data_(
                    payload,
                    configuration_=self.schema_config
                )
                self.api.post(body=body)

    def test_a_string_is_not_null_fails(self):
        content_type = 'application/json'
        # a string is not null
        with patch.object(urllib3.PoolManager, 'request') as mock_request:
            payload = (
                "foo"
            )
            with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
                body = post.request_body.RequestBody.content["application/json"].schema.from_openapi_data_(
                    payload,
                    configuration_=self.schema_config
                )
                self.api.post(body=body)

if __name__ == '__main__':
    unittest.main()
