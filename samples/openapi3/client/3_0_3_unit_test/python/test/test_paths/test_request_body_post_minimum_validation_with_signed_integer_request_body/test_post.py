# coding: utf-8

"""


    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

import unittest
from unittest.mock import patch

import urllib3

import unit_test_api
from unit_test_api.paths.request_body_post_minimum_validation_with_signed_integer_request_body import post  # noqa: E501
from unit_test_api import configuration, schemas, api_client

from .. import ApiTestMixin


class TestRequestBodyPostMinimumValidationWithSignedIntegerRequestBody(ApiTestMixin, unittest.TestCase):
    """
    RequestBodyPostMinimumValidationWithSignedIntegerRequestBody unit test stubs
    """
    configuration_ = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self.configuration_)
        self.api = post.ApiForpost(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200
    response_body = ''

    def test_boundary_point_is_valid_passes(self):
        content_type = 'org.openapitools.codegen.CodegenKey@63a70a10'
        # boundary point is valid
        with patch.object(urllib3.PoolManager, 'request') as mock_request:
            payload = (
                -2
            )
            body = post.request_body.minimum_validation_with_signed_integer.MinimumValidationWithSignedInteger.from_openapi_data_(
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
                self.configuration_.host + '/requestBody/postMinimumValidationWithSignedIntegerRequestBody',
                method='post'.upper(),
                body=self.json_bytes(payload),
                content_type=content_type,
            )

            assert isinstance(api_response.response, urllib3.HTTPResponse)
            assert isinstance(api_response.body, schemas.Unset)

    def test_positive_above_the_minimum_is_valid_passes(self):
        content_type = 'org.openapitools.codegen.CodegenKey@63a70a10'
        # positive above the minimum is valid
        with patch.object(urllib3.PoolManager, 'request') as mock_request:
            payload = (
                0
            )
            body = post.request_body.minimum_validation_with_signed_integer.MinimumValidationWithSignedInteger.from_openapi_data_(
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
                self.configuration_.host + '/requestBody/postMinimumValidationWithSignedIntegerRequestBody',
                method='post'.upper(),
                body=self.json_bytes(payload),
                content_type=content_type,
            )

            assert isinstance(api_response.response, urllib3.HTTPResponse)
            assert isinstance(api_response.body, schemas.Unset)

    def test_int_below_the_minimum_is_invalid_fails(self):
        content_type = 'org.openapitools.codegen.CodegenKey@63a70a10'
        # int below the minimum is invalid
        with patch.object(urllib3.PoolManager, 'request') as mock_request:
            payload = (
                -3
            )
            with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
                body = post.request_body.minimum_validation_with_signed_integer.MinimumValidationWithSignedInteger.from_openapi_data_(
                    payload,
                    configuration_=self.configuration_
                )
                self.api.post(body=body)

    def test_float_below_the_minimum_is_invalid_fails(self):
        content_type = 'org.openapitools.codegen.CodegenKey@63a70a10'
        # float below the minimum is invalid
        with patch.object(urllib3.PoolManager, 'request') as mock_request:
            payload = (
                -2.0001
            )
            with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
                body = post.request_body.minimum_validation_with_signed_integer.MinimumValidationWithSignedInteger.from_openapi_data_(
                    payload,
                    configuration_=self.configuration_
                )
                self.api.post(body=body)

    def test_boundary_point_with_float_is_valid_passes(self):
        content_type = 'org.openapitools.codegen.CodegenKey@63a70a10'
        # boundary point with float is valid
        with patch.object(urllib3.PoolManager, 'request') as mock_request:
            payload = (
                -2.0
            )
            body = post.request_body.minimum_validation_with_signed_integer.MinimumValidationWithSignedInteger.from_openapi_data_(
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
                self.configuration_.host + '/requestBody/postMinimumValidationWithSignedIntegerRequestBody',
                method='post'.upper(),
                body=self.json_bytes(payload),
                content_type=content_type,
            )

            assert isinstance(api_response.response, urllib3.HTTPResponse)
            assert isinstance(api_response.body, schemas.Unset)

    def test_negative_above_the_minimum_is_valid_passes(self):
        content_type = 'org.openapitools.codegen.CodegenKey@63a70a10'
        # negative above the minimum is valid
        with patch.object(urllib3.PoolManager, 'request') as mock_request:
            payload = (
                -1
            )
            body = post.request_body.minimum_validation_with_signed_integer.MinimumValidationWithSignedInteger.from_openapi_data_(
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
                self.configuration_.host + '/requestBody/postMinimumValidationWithSignedIntegerRequestBody',
                method='post'.upper(),
                body=self.json_bytes(payload),
                content_type=content_type,
            )

            assert isinstance(api_response.response, urllib3.HTTPResponse)
            assert isinstance(api_response.body, schemas.Unset)

    def test_ignores_non_numbers_passes(self):
        content_type = 'org.openapitools.codegen.CodegenKey@63a70a10'
        # ignores non-numbers
        with patch.object(urllib3.PoolManager, 'request') as mock_request:
            payload = (
                "x"
            )
            body = post.request_body.minimum_validation_with_signed_integer.MinimumValidationWithSignedInteger.from_openapi_data_(
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
                self.configuration_.host + '/requestBody/postMinimumValidationWithSignedIntegerRequestBody',
                method='post'.upper(),
                body=self.json_bytes(payload),
                content_type=content_type,
            )

            assert isinstance(api_response.response, urllib3.HTTPResponse)
            assert isinstance(api_response.body, schemas.Unset)

if __name__ == '__main__':
    unittest.main()
