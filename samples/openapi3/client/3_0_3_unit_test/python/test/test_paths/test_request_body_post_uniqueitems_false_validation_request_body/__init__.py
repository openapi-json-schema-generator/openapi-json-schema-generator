# coding: utf-8

"""


    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

import unittest
from unittest.mock import patch

import urllib3

import unit_test_api
from unit_test_api.paths.request_body_post_uniqueitems_false_validation_request_body.post import operation as post  # noqa: E501
from unit_test_api import schemas, api_client
from unit_test_api.configurations import api_configuration, schema_configuration

from .. import ApiTestMixin


class TestPost(ApiTestMixin, unittest.TestCase):
    """
    Post unit test stubs
    """
    configuration_ = api_configuration.ApiConfiguration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self.configuration_)
        self.api = post.ApiForPost(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200
    response_body = ''

    def test_non_unique_array_of_integers_is_valid_passes(self):
        content_type = 'application/json'
        # non-unique array of integers is valid
        with patch.object(urllib3.PoolManager, 'request') as mock_request:
            payload = (
                [
                    1,
                    1,
                ]
            )
            body = post.request_body.RequestBody.content["application/json"].schema.from_openapi_data_(
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
                self.configuration_.host + "/requestBody/postUniqueitemsFalseValidationRequestBody",
                method='post'.upper(),
                body=self.json_bytes(payload),
                content_type=content_type,
            )

            assert isinstance(api_response.response, urllib3.HTTPResponse)
            assert isinstance(api_response.body, schemas.Unset)

    def test_unique_array_of_objects_is_valid_passes(self):
        content_type = 'application/json'
        # unique array of objects is valid
        with patch.object(urllib3.PoolManager, 'request') as mock_request:
            payload = (
                [
                    {
                        "foo":
                            "bar",
                    },
                    {
                        "foo":
                            "baz",
                    },
                ]
            )
            body = post.request_body.RequestBody.content["application/json"].schema.from_openapi_data_(
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
                self.configuration_.host + "/requestBody/postUniqueitemsFalseValidationRequestBody",
                method='post'.upper(),
                body=self.json_bytes(payload),
                content_type=content_type,
            )

            assert isinstance(api_response.response, urllib3.HTTPResponse)
            assert isinstance(api_response.body, schemas.Unset)

    def test_non_unique_array_of_nested_objects_is_valid_passes(self):
        content_type = 'application/json'
        # non-unique array of nested objects is valid
        with patch.object(urllib3.PoolManager, 'request') as mock_request:
            payload = (
                [
                    {
                        "foo":
                            {
                                "bar":
                                    {
                                        "baz":
                                            True,
                                    },
                            },
                    },
                    {
                        "foo":
                            {
                                "bar":
                                    {
                                        "baz":
                                            True,
                                    },
                            },
                    },
                ]
            )
            body = post.request_body.RequestBody.content["application/json"].schema.from_openapi_data_(
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
                self.configuration_.host + "/requestBody/postUniqueitemsFalseValidationRequestBody",
                method='post'.upper(),
                body=self.json_bytes(payload),
                content_type=content_type,
            )

            assert isinstance(api_response.response, urllib3.HTTPResponse)
            assert isinstance(api_response.body, schemas.Unset)

    def test_non_unique_array_of_objects_is_valid_passes(self):
        content_type = 'application/json'
        # non-unique array of objects is valid
        with patch.object(urllib3.PoolManager, 'request') as mock_request:
            payload = (
                [
                    {
                        "foo":
                            "bar",
                    },
                    {
                        "foo":
                            "bar",
                    },
                ]
            )
            body = post.request_body.RequestBody.content["application/json"].schema.from_openapi_data_(
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
                self.configuration_.host + "/requestBody/postUniqueitemsFalseValidationRequestBody",
                method='post'.upper(),
                body=self.json_bytes(payload),
                content_type=content_type,
            )

            assert isinstance(api_response.response, urllib3.HTTPResponse)
            assert isinstance(api_response.body, schemas.Unset)

    def test_1_and_true_are_unique_passes(self):
        content_type = 'application/json'
        # 1 and true are unique
        with patch.object(urllib3.PoolManager, 'request') as mock_request:
            payload = (
                [
                    1,
                    True,
                ]
            )
            body = post.request_body.RequestBody.content["application/json"].schema.from_openapi_data_(
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
                self.configuration_.host + "/requestBody/postUniqueitemsFalseValidationRequestBody",
                method='post'.upper(),
                body=self.json_bytes(payload),
                content_type=content_type,
            )

            assert isinstance(api_response.response, urllib3.HTTPResponse)
            assert isinstance(api_response.body, schemas.Unset)

    def test_unique_array_of_integers_is_valid_passes(self):
        content_type = 'application/json'
        # unique array of integers is valid
        with patch.object(urllib3.PoolManager, 'request') as mock_request:
            payload = (
                [
                    1,
                    2,
                ]
            )
            body = post.request_body.RequestBody.content["application/json"].schema.from_openapi_data_(
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
                self.configuration_.host + "/requestBody/postUniqueitemsFalseValidationRequestBody",
                method='post'.upper(),
                body=self.json_bytes(payload),
                content_type=content_type,
            )

            assert isinstance(api_response.response, urllib3.HTTPResponse)
            assert isinstance(api_response.body, schemas.Unset)

    def test_non_unique_array_of_arrays_is_valid_passes(self):
        content_type = 'application/json'
        # non-unique array of arrays is valid
        with patch.object(urllib3.PoolManager, 'request') as mock_request:
            payload = (
                [
                    [
                        "foo",
                    ],
                    [
                        "foo",
                    ],
                ]
            )
            body = post.request_body.RequestBody.content["application/json"].schema.from_openapi_data_(
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
                self.configuration_.host + "/requestBody/postUniqueitemsFalseValidationRequestBody",
                method='post'.upper(),
                body=self.json_bytes(payload),
                content_type=content_type,
            )

            assert isinstance(api_response.response, urllib3.HTTPResponse)
            assert isinstance(api_response.body, schemas.Unset)

    def test_numbers_are_unique_if_mathematically_unequal_passes(self):
        content_type = 'application/json'
        # numbers are unique if mathematically unequal
        with patch.object(urllib3.PoolManager, 'request') as mock_request:
            payload = (
                [
                    1.0,
                    1.0,
                    1,
                ]
            )
            body = post.request_body.RequestBody.content["application/json"].schema.from_openapi_data_(
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
                self.configuration_.host + "/requestBody/postUniqueitemsFalseValidationRequestBody",
                method='post'.upper(),
                body=self.json_bytes(payload),
                content_type=content_type,
            )

            assert isinstance(api_response.response, urllib3.HTTPResponse)
            assert isinstance(api_response.body, schemas.Unset)

    def test_false_is_not_equal_to_zero_passes(self):
        content_type = 'application/json'
        # false is not equal to zero
        with patch.object(urllib3.PoolManager, 'request') as mock_request:
            payload = (
                [
                    0,
                    False,
                ]
            )
            body = post.request_body.RequestBody.content["application/json"].schema.from_openapi_data_(
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
                self.configuration_.host + "/requestBody/postUniqueitemsFalseValidationRequestBody",
                method='post'.upper(),
                body=self.json_bytes(payload),
                content_type=content_type,
            )

            assert isinstance(api_response.response, urllib3.HTTPResponse)
            assert isinstance(api_response.body, schemas.Unset)

    def test_unique_array_of_nested_objects_is_valid_passes(self):
        content_type = 'application/json'
        # unique array of nested objects is valid
        with patch.object(urllib3.PoolManager, 'request') as mock_request:
            payload = (
                [
                    {
                        "foo":
                            {
                                "bar":
                                    {
                                        "baz":
                                            True,
                                    },
                            },
                    },
                    {
                        "foo":
                            {
                                "bar":
                                    {
                                        "baz":
                                            False,
                                    },
                            },
                    },
                ]
            )
            body = post.request_body.RequestBody.content["application/json"].schema.from_openapi_data_(
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
                self.configuration_.host + "/requestBody/postUniqueitemsFalseValidationRequestBody",
                method='post'.upper(),
                body=self.json_bytes(payload),
                content_type=content_type,
            )

            assert isinstance(api_response.response, urllib3.HTTPResponse)
            assert isinstance(api_response.body, schemas.Unset)

    def test_0_and_false_are_unique_passes(self):
        content_type = 'application/json'
        # 0 and false are unique
        with patch.object(urllib3.PoolManager, 'request') as mock_request:
            payload = (
                [
                    0,
                    False,
                ]
            )
            body = post.request_body.RequestBody.content["application/json"].schema.from_openapi_data_(
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
                self.configuration_.host + "/requestBody/postUniqueitemsFalseValidationRequestBody",
                method='post'.upper(),
                body=self.json_bytes(payload),
                content_type=content_type,
            )

            assert isinstance(api_response.response, urllib3.HTTPResponse)
            assert isinstance(api_response.body, schemas.Unset)

    def test_unique_array_of_arrays_is_valid_passes(self):
        content_type = 'application/json'
        # unique array of arrays is valid
        with patch.object(urllib3.PoolManager, 'request') as mock_request:
            payload = (
                [
                    [
                        "foo",
                    ],
                    [
                        "bar",
                    ],
                ]
            )
            body = post.request_body.RequestBody.content["application/json"].schema.from_openapi_data_(
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
                self.configuration_.host + "/requestBody/postUniqueitemsFalseValidationRequestBody",
                method='post'.upper(),
                body=self.json_bytes(payload),
                content_type=content_type,
            )

            assert isinstance(api_response.response, urllib3.HTTPResponse)
            assert isinstance(api_response.body, schemas.Unset)

    def test_true_is_not_equal_to_one_passes(self):
        content_type = 'application/json'
        # true is not equal to one
        with patch.object(urllib3.PoolManager, 'request') as mock_request:
            payload = (
                [
                    1,
                    True,
                ]
            )
            body = post.request_body.RequestBody.content["application/json"].schema.from_openapi_data_(
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
                self.configuration_.host + "/requestBody/postUniqueitemsFalseValidationRequestBody",
                method='post'.upper(),
                body=self.json_bytes(payload),
                content_type=content_type,
            )

            assert isinstance(api_response.response, urllib3.HTTPResponse)
            assert isinstance(api_response.body, schemas.Unset)

    def test_non_unique_heterogeneous_types_are_valid_passes(self):
        content_type = 'application/json'
        # non-unique heterogeneous types are valid
        with patch.object(urllib3.PoolManager, 'request') as mock_request:
            payload = (
                [
                    {
                    },
                    [
                        1,
                    ],
                    True,
                    None,
                    {
                    },
                    1,
                ]
            )
            body = post.request_body.RequestBody.content["application/json"].schema.from_openapi_data_(
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
                self.configuration_.host + "/requestBody/postUniqueitemsFalseValidationRequestBody",
                method='post'.upper(),
                body=self.json_bytes(payload),
                content_type=content_type,
            )

            assert isinstance(api_response.response, urllib3.HTTPResponse)
            assert isinstance(api_response.body, schemas.Unset)

    def test_unique_heterogeneous_types_are_valid_passes(self):
        content_type = 'application/json'
        # unique heterogeneous types are valid
        with patch.object(urllib3.PoolManager, 'request') as mock_request:
            payload = (
                [
                    {
                    },
                    [
                        1,
                    ],
                    True,
                    None,
                    1,
                ]
            )
            body = post.request_body.RequestBody.content["application/json"].schema.from_openapi_data_(
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
                self.configuration_.host + "/requestBody/postUniqueitemsFalseValidationRequestBody",
                method='post'.upper(),
                body=self.json_bytes(payload),
                content_type=content_type,
            )

            assert isinstance(api_response.response, urllib3.HTTPResponse)
            assert isinstance(api_response.body, schemas.Unset)

if __name__ == '__main__':
    unittest.main()
