# coding: utf-8

"""


    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

import unittest
from unittest.mock import patch

import urllib3

import unit_test_api
from unit_test_api.paths.request_body_post_oneof_with_required_request_body import post  # noqa: E501
from unit_test_api import configuration, schemas, api_client

from .. import ApiTestMixin


class TestRequestBodyPostOneofWithRequiredRequestBody(ApiTestMixin, unittest.TestCase):
    """
    RequestBodyPostOneofWithRequiredRequestBody unit test stubs
    """
    configuration_ = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self.configuration_)
        self.api = post.ApiForpost(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200
    response_body = ''

    def test_both_valid_invalid_fails(self):
        content_type = 'org.openapitools.codegen.CodegenKey@63a70a10'
        # both valid - invalid
        with patch.object(urllib3.PoolManager, 'request') as mock_request:
            payload = (
                {
                    "foo":
                        1,
                    "bar":
                        2,
                    "baz":
                        3,
                }
            )
            with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
                body = post.request_body.oneof_with_required.OneofWithRequired.from_openapi_data_(
                    payload,
                    configuration_=self.configuration_
                )
                self.api.post(body=body)

    def test_both_invalid_invalid_fails(self):
        content_type = 'org.openapitools.codegen.CodegenKey@63a70a10'
        # both invalid - invalid
        with patch.object(urllib3.PoolManager, 'request') as mock_request:
            payload = (
                {
                    "bar":
                        2,
                }
            )
            with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
                body = post.request_body.oneof_with_required.OneofWithRequired.from_openapi_data_(
                    payload,
                    configuration_=self.configuration_
                )
                self.api.post(body=body)

    def test_first_valid_valid_passes(self):
        content_type = 'org.openapitools.codegen.CodegenKey@63a70a10'
        # first valid - valid
        with patch.object(urllib3.PoolManager, 'request') as mock_request:
            payload = (
                {
                    "foo":
                        1,
                    "bar":
                        2,
                }
            )
            body = post.request_body.oneof_with_required.OneofWithRequired.from_openapi_data_(
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
                self.configuration_.host + '/requestBody/postOneofWithRequiredRequestBody',
                method='post'.upper(),
                body=self.json_bytes(payload),
                content_type=content_type,
            )

            assert isinstance(api_response.response, urllib3.HTTPResponse)
            assert isinstance(api_response.body, schemas.Unset)

    def test_second_valid_valid_passes(self):
        content_type = 'org.openapitools.codegen.CodegenKey@63a70a10'
        # second valid - valid
        with patch.object(urllib3.PoolManager, 'request') as mock_request:
            payload = (
                {
                    "foo":
                        1,
                    "baz":
                        3,
                }
            )
            body = post.request_body.oneof_with_required.OneofWithRequired.from_openapi_data_(
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
                self.configuration_.host + '/requestBody/postOneofWithRequiredRequestBody',
                method='post'.upper(),
                body=self.json_bytes(payload),
                content_type=content_type,
            )

            assert isinstance(api_response.response, urllib3.HTTPResponse)
            assert isinstance(api_response.body, schemas.Unset)

if __name__ == '__main__':
    unittest.main()
