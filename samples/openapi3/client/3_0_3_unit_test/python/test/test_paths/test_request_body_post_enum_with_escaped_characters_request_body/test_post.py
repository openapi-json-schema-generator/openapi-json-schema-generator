# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import unit_test_api
from unit_test_api.paths.request_body_post_enum_with_escaped_characters_request_body import post  # noqa: E501
from unit_test_api import configuration, schemas, api_client

from .. import ApiTestMixin


class TestRequestBodyPostEnumWithEscapedCharactersRequestBody(ApiTestMixin, unittest.TestCase):
    """
    RequestBodyPostEnumWithEscapedCharactersRequestBody unit test stubs
    """
    configuration_ = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self.configuration_)
        self.api = post.ApiForpost(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200
    response_body = ''

    def test_member2_is_valid_passes(self):
        content_type = 'application/json'
        # member 2 is valid
        with patch.object(urllib3.PoolManager, 'request') as mock_request:
            payload = (
                "foo\rbar"
            )
            body = post.request_body.enum_with_escaped_characters.EnumWithEscapedCharacters.from_openapi_data_(
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
                self.configuration_.host + '/requestBody/postEnumWithEscapedCharactersRequestBody',
                method='post'.upper(),
                body=self.json_bytes(payload),
                content_type=content_type,
            )

            assert isinstance(api_response.response, urllib3.HTTPResponse)
            assert isinstance(api_response.body, schemas.Unset)

    def test_member1_is_valid_passes(self):
        content_type = 'application/json'
        # member 1 is valid
        with patch.object(urllib3.PoolManager, 'request') as mock_request:
            payload = (
                "foo\nbar"
            )
            body = post.request_body.enum_with_escaped_characters.EnumWithEscapedCharacters.from_openapi_data_(
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
                self.configuration_.host + '/requestBody/postEnumWithEscapedCharactersRequestBody',
                method='post'.upper(),
                body=self.json_bytes(payload),
                content_type=content_type,
            )

            assert isinstance(api_response.response, urllib3.HTTPResponse)
            assert isinstance(api_response.body, schemas.Unset)

    def test_another_string_is_invalid_fails(self):
        content_type = 'application/json'
        # another string is invalid
        with patch.object(urllib3.PoolManager, 'request') as mock_request:
            payload = (
                "abc"
            )
            with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
                body = post.request_body.enum_with_escaped_characters.EnumWithEscapedCharacters.from_openapi_data_(
                    payload,
                    configuration_=self.configuration_
                )
                self.api.post(body=body)

if __name__ == '__main__':
    unittest.main()
