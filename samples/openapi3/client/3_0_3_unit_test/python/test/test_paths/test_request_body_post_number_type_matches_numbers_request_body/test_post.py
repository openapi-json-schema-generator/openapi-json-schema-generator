# coding: utf-8

"""


    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

import unittest
from unittest.mock import patch

import urllib3

import unit_test_api
from unit_test_api.paths.request_body_post_number_type_matches_numbers_request_body import post  # noqa: E501
from unit_test_api import configuration, schemas, api_client

from .. import ApiTestMixin


class TestRequestBodyPostNumberTypeMatchesNumbersRequestBody(ApiTestMixin, unittest.TestCase):
    """
    RequestBodyPostNumberTypeMatchesNumbersRequestBody unit test stubs
    """
    configuration_ = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self.configuration_)
        self.api = post.ApiForpost(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200
    response_body = ''

    def test_an_array_is_not_a_number_fails(self):
        content_type = 'org.openapitools.codegen.CodegenKey@63a70a10'
        # an array is not a number
        with patch.object(urllib3.PoolManager, 'request') as mock_request:
            payload = (
                [
                ]
            )
            with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
                body = post.request_body.number_type_matches_numbers.NumberTypeMatchesNumbers.from_openapi_data_(
                    payload,
                    configuration_=self.configuration_
                )
                self.api.post(body=body)

    def test_null_is_not_a_number_fails(self):
        content_type = 'org.openapitools.codegen.CodegenKey@63a70a10'
        # null is not a number
        with patch.object(urllib3.PoolManager, 'request') as mock_request:
            payload = (
                None
            )
            with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
                body = post.request_body.number_type_matches_numbers.NumberTypeMatchesNumbers.from_openapi_data_(
                    payload,
                    configuration_=self.configuration_
                )
                self.api.post(body=body)

    def test_an_object_is_not_a_number_fails(self):
        content_type = 'org.openapitools.codegen.CodegenKey@63a70a10'
        # an object is not a number
        with patch.object(urllib3.PoolManager, 'request') as mock_request:
            payload = (
                {
                }
            )
            with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
                body = post.request_body.number_type_matches_numbers.NumberTypeMatchesNumbers.from_openapi_data_(
                    payload,
                    configuration_=self.configuration_
                )
                self.api.post(body=body)

    def test_a_boolean_is_not_a_number_fails(self):
        content_type = 'org.openapitools.codegen.CodegenKey@63a70a10'
        # a boolean is not a number
        with patch.object(urllib3.PoolManager, 'request') as mock_request:
            payload = (
                True
            )
            with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
                body = post.request_body.number_type_matches_numbers.NumberTypeMatchesNumbers.from_openapi_data_(
                    payload,
                    configuration_=self.configuration_
                )
                self.api.post(body=body)

    def test_a_float_is_a_number_passes(self):
        content_type = 'org.openapitools.codegen.CodegenKey@63a70a10'
        # a float is a number
        with patch.object(urllib3.PoolManager, 'request') as mock_request:
            payload = (
                1.1
            )
            body = post.request_body.number_type_matches_numbers.NumberTypeMatchesNumbers.from_openapi_data_(
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
                self.configuration_.host + '/requestBody/postNumberTypeMatchesNumbersRequestBody',
                method='post'.upper(),
                body=self.json_bytes(payload),
                content_type=content_type,
            )

            assert isinstance(api_response.response, urllib3.HTTPResponse)
            assert isinstance(api_response.body, schemas.Unset)

    def test_a_string_is_still_not_a_number_even_if_it_looks_like_one_fails(self):
        content_type = 'org.openapitools.codegen.CodegenKey@63a70a10'
        # a string is still not a number, even if it looks like one
        with patch.object(urllib3.PoolManager, 'request') as mock_request:
            payload = (
                "1"
            )
            with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
                body = post.request_body.number_type_matches_numbers.NumberTypeMatchesNumbers.from_openapi_data_(
                    payload,
                    configuration_=self.configuration_
                )
                self.api.post(body=body)

    def test_a_string_is_not_a_number_fails(self):
        content_type = 'org.openapitools.codegen.CodegenKey@63a70a10'
        # a string is not a number
        with patch.object(urllib3.PoolManager, 'request') as mock_request:
            payload = (
                "foo"
            )
            with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
                body = post.request_body.number_type_matches_numbers.NumberTypeMatchesNumbers.from_openapi_data_(
                    payload,
                    configuration_=self.configuration_
                )
                self.api.post(body=body)

    def test_an_integer_is_a_number_passes(self):
        content_type = 'org.openapitools.codegen.CodegenKey@63a70a10'
        # an integer is a number
        with patch.object(urllib3.PoolManager, 'request') as mock_request:
            payload = (
                1
            )
            body = post.request_body.number_type_matches_numbers.NumberTypeMatchesNumbers.from_openapi_data_(
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
                self.configuration_.host + '/requestBody/postNumberTypeMatchesNumbersRequestBody',
                method='post'.upper(),
                body=self.json_bytes(payload),
                content_type=content_type,
            )

            assert isinstance(api_response.response, urllib3.HTTPResponse)
            assert isinstance(api_response.body, schemas.Unset)

    def test_a_float_with_zero_fractional_part_is_a_number_and_an_integer_passes(self):
        content_type = 'org.openapitools.codegen.CodegenKey@63a70a10'
        # a float with zero fractional part is a number (and an integer)
        with patch.object(urllib3.PoolManager, 'request') as mock_request:
            payload = (
                1.0
            )
            body = post.request_body.number_type_matches_numbers.NumberTypeMatchesNumbers.from_openapi_data_(
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
                self.configuration_.host + '/requestBody/postNumberTypeMatchesNumbersRequestBody',
                method='post'.upper(),
                body=self.json_bytes(payload),
                content_type=content_type,
            )

            assert isinstance(api_response.response, urllib3.HTTPResponse)
            assert isinstance(api_response.body, schemas.Unset)

if __name__ == '__main__':
    unittest.main()
