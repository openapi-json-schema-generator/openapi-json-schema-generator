# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import unit_test_api
from unit_test_api.paths.request_body_post_minlength_validation_request_body import post  # noqa: E501
from unit_test_api import configuration, schemas, api_client

from .. import ApiTestMixin


class TestRequestBodyPostMinlengthValidationRequestBody(ApiTestMixin, unittest.TestCase):
    """
    RequestBodyPostMinlengthValidationRequestBody unit test stubs
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = post.ApiForpost(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200
    response_body = ''

    def test_too_short_is_invalid_fails(self):
        content_type = 'application/json'
        # too short is invalid
        with patch.object(urllib3.PoolManager, 'request') as mock_request:
            payload = (
                "f"
            )
            with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
                body = post.request_body.minlength_validation.MinlengthValidation.from_openapi_data_(
                    payload,
                    _configuration=self._configuration
                )
                self.api.post(body=body)

    def test_one_supplementary_unicode_code_point_is_not_long_enough_fails(self):
        content_type = 'application/json'
        # one supplementary Unicode code point is not long enough
        with patch.object(urllib3.PoolManager, 'request') as mock_request:
            payload = (
                "💩"
            )
            with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
                body = post.request_body.minlength_validation.MinlengthValidation.from_openapi_data_(
                    payload,
                    _configuration=self._configuration
                )
                self.api.post(body=body)

    def test_longer_is_valid_passes(self):
        content_type = 'application/json'
        # longer is valid
        with patch.object(urllib3.PoolManager, 'request') as mock_request:
            payload = (
                "foo"
            )
            body = post.request_body.minlength_validation.MinlengthValidation.from_openapi_data_(
                payload,
                _configuration=self._configuration
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
                self._configuration.host + '/requestBody/postMinlengthValidationRequestBody',
                method='post'.upper(),
                body=self.json_bytes(payload),
                content_type=content_type,
            )

            assert isinstance(api_response.response, urllib3.HTTPResponse)
            assert isinstance(api_response.body, schemas.Unset)

    def test_ignores_non_strings_passes(self):
        content_type = 'application/json'
        # ignores non-strings
        with patch.object(urllib3.PoolManager, 'request') as mock_request:
            payload = (
                1
            )
            body = post.request_body.minlength_validation.MinlengthValidation.from_openapi_data_(
                payload,
                _configuration=self._configuration
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
                self._configuration.host + '/requestBody/postMinlengthValidationRequestBody',
                method='post'.upper(),
                body=self.json_bytes(payload),
                content_type=content_type,
            )

            assert isinstance(api_response.response, urllib3.HTTPResponse)
            assert isinstance(api_response.body, schemas.Unset)

    def test_exact_length_is_valid_passes(self):
        content_type = 'application/json'
        # exact length is valid
        with patch.object(urllib3.PoolManager, 'request') as mock_request:
            payload = (
                "fo"
            )
            body = post.request_body.minlength_validation.MinlengthValidation.from_openapi_data_(
                payload,
                _configuration=self._configuration
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
                self._configuration.host + '/requestBody/postMinlengthValidationRequestBody',
                method='post'.upper(),
                body=self.json_bytes(payload),
                content_type=content_type,
            )

            assert isinstance(api_response.response, urllib3.HTTPResponse)
            assert isinstance(api_response.body, schemas.Unset)

if __name__ == '__main__':
    unittest.main()
