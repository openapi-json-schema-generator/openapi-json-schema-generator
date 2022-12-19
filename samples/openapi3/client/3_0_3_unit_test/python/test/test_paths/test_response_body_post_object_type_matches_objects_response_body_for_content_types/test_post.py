# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import unit_test_api
from unit_test_api.paths.response_body_post_object_type_matches_objects_response_body_for_content_types import post  # noqa: E501
from unit_test_api import configuration, schemas, api_client

from .. import ApiTestMixin


class TestResponseBodyPostObjectTypeMatchesObjectsResponseBodyForContentTypes(ApiTestMixin, unittest.TestCase):
    """
    ResponseBodyPostObjectTypeMatchesObjectsResponseBodyForContentTypes unit test stubs
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = post.ApiForpost(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200
    response_body_schema = post.response_for_200.ApplicationJson

    def test_a_float_is_not_an_object_fails(self):
        # a float is not an object
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
                self._configuration.host + '/responseBody/postObjectTypeMatchesObjectsResponseBodyForContentTypes',
                method='post'.upper(),
                content_type=None,
                accept_content_type=accept_content_type,
            )

    def test_null_is_not_an_object_fails(self):
        # null is not an object
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
                self._configuration.host + '/responseBody/postObjectTypeMatchesObjectsResponseBodyForContentTypes',
                method='post'.upper(),
                content_type=None,
                accept_content_type=accept_content_type,
            )

    def test_an_array_is_not_an_object_fails(self):
        # an array is not an object
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
                self._configuration.host + '/responseBody/postObjectTypeMatchesObjectsResponseBodyForContentTypes',
                method='post'.upper(),
                content_type=None,
                accept_content_type=accept_content_type,
            )

    def test_an_object_is_an_object_passes(self):
        # an object is an object
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
                self._configuration.host + '/responseBody/postObjectTypeMatchesObjectsResponseBodyForContentTypes',
                method='post'.upper(),
                accept_content_type=accept_content_type,
            )

            assert isinstance(api_response.response, urllib3.HTTPResponse)
            assert isinstance(api_response.body, self.response_body_schema)
            deserialized_response_body = self.response_body_schema.from_openapi_data_oapg(
                payload,
                _configuration=self._configuration
            )
            assert api_response.body == deserialized_response_body

    def test_a_string_is_not_an_object_fails(self):
        # a string is not an object
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
                self._configuration.host + '/responseBody/postObjectTypeMatchesObjectsResponseBodyForContentTypes',
                method='post'.upper(),
                content_type=None,
                accept_content_type=accept_content_type,
            )

    def test_an_integer_is_not_an_object_fails(self):
        # an integer is not an object
        accept_content_type = 'application/json'

        with patch.object(urllib3.PoolManager, 'request') as mock_request:
            payload = (
                1
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
                self._configuration.host + '/responseBody/postObjectTypeMatchesObjectsResponseBodyForContentTypes',
                method='post'.upper(),
                content_type=None,
                accept_content_type=accept_content_type,
            )

    def test_a_boolean_is_not_an_object_fails(self):
        # a boolean is not an object
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
                self._configuration.host + '/responseBody/postObjectTypeMatchesObjectsResponseBodyForContentTypes',
                method='post'.upper(),
                content_type=None,
                accept_content_type=accept_content_type,
            )

if __name__ == '__main__':
    unittest.main()
