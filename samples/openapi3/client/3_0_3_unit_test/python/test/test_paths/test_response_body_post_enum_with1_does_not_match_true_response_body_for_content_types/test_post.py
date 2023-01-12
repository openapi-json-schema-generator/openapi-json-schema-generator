# coding: utf-8

"""


    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

import unittest
from unittest.mock import patch

import urllib3

import unit_test_api
from unit_test_api.paths.response_body_post_enum_with1_does_not_match_true_response_body_for_content_types import post  # noqa: E501
from unit_test_api import configuration, schemas, api_client

from .. import ApiTestMixin


class TestResponseBodyPostEnumWith1DoesNotMatchTrueResponseBodyForContentTypes(ApiTestMixin, unittest.TestCase):
    """
    ResponseBodyPostEnumWith1DoesNotMatchTrueResponseBodyForContentTypes unit test stubs
    """
    configuration_ = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self.configuration_)
        self.api = post.ApiForpost(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200
    response_body_schema = post.response_200.enum_with1_does_not_match_true.EnumWith1DoesNotMatchTrue
    
    def test_true_is_invalid_fails(self):
        # true is invalid
        accept_content_type = 'org.openapitools.codegen.CodegenKey@63a70a10'
    
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
                self.configuration_.host + '/responseBody/postEnumWith1DoesNotMatchTrueResponseBodyForContentTypes',
                method='post'.upper(),
                content_type=None,
                accept_content_type=accept_content_type,
            )
    
    def test_integer_one_is_valid_passes(self):
        # integer one is valid
        accept_content_type = 'org.openapitools.codegen.CodegenKey@63a70a10'
    
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
                self.configuration_.host + '/responseBody/postEnumWith1DoesNotMatchTrueResponseBodyForContentTypes',
                method='post'.upper(),
                accept_content_type=accept_content_type,
            )
    
            assert isinstance(api_response.response, urllib3.HTTPResponse)
            assert isinstance(api_response.body, self.response_body_schema)
            deserialized_response_body = self.response_body_schema.from_openapi_data_(
                payload,
                configuration_=self.configuration_
            )
            assert api_response.body == deserialized_response_body
    
    def test_float_one_is_valid_passes(self):
        # float one is valid
        accept_content_type = 'org.openapitools.codegen.CodegenKey@63a70a10'
    
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
                self.configuration_.host + '/responseBody/postEnumWith1DoesNotMatchTrueResponseBodyForContentTypes',
                method='post'.upper(),
                accept_content_type=accept_content_type,
            )
    
            assert isinstance(api_response.response, urllib3.HTTPResponse)
            assert isinstance(api_response.body, self.response_body_schema)
            deserialized_response_body = self.response_body_schema.from_openapi_data_(
                payload,
                configuration_=self.configuration_
            )
            assert api_response.body == deserialized_response_body

if __name__ == '__main__':
    unittest.main()
