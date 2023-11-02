# coding: utf-8

"""
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

import unittest
from unittest.mock import patch

import urllib3
import typing_extensions

import unit_test_api
from unit_test_api.paths.request_body_post_dependent_schemas_dependencies_with_escaped_characters_request_body.post import operation as post  # noqa: E501
from unit_test_api import schemas, api_client
from unit_test_api.configurations import api_configuration, schema_configuration

from .. import ApiTestMixin


class TestPost(ApiTestMixin, unittest.TestCase):
    """
    Post unit test stubs
    """
    api_config = api_configuration.ApiConfiguration()
    schema_config = schema_configuration.SchemaConfiguration(
        disabled_json_schema_keywords={'format'}
    )
    used_api_client = api_client.ApiClient(configuration=api_config, schema_configuration=schema_config)
    api = post.ApiForPost(api_client=used_api_client)  # noqa: E501

    response_status = 200
    response_body = ''

    def test_quoted_tab_passes(self):
        content_type = 'application/json'
        # quoted tab
        with patch.object(urllib3.PoolManager, 'request') as mock_request:
            payload = (
                {
                    "foo\tbar":
                        1,
                    "a":
                        2,
                    "b":
                        3,
                    "c":
                        4,
                }
            )
            body = post.request_body.RequestBody.content["application/json"].schema.validate(
                payload,
                configuration=self.schema_config
            )
            mock_request.return_value = self.response(
                self.json_bytes(self.response_body),
                status=self.response_status
            )
            api_response = self.api.post(
                body=body,
            )
            self.assert_pool_manager_request_called_with(
                mock_request,
                self.api_config.get_server_url('servers', None) + "/requestBody/postDependentSchemasDependenciesWithEscapedCharactersRequestBody",
                method='post'.upper(),
                body=self.json_bytes(payload),
                content_type=content_type,
            )

            assert isinstance(api_response.response, urllib3.HTTPResponse)
            assert isinstance(api_response.body, schemas.Unset)

    def test_quoted_quote_invalid_under_dependent_schema_fails(self):
        content_type = 'application/json'
        # quoted quote invalid under dependent schema
        with patch.object(urllib3.PoolManager, 'request') as mock_request:
            payload = (
                {
                    "foo'bar":
                        1,
                }
            )
            with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
                body = post.request_body.RequestBody.content["application/json"].schema.validate(
                    payload,
                    configuration=self.schema_config
                )
                self.api.post(body=body)

    def test_quoted_quote_fails(self):
        content_type = 'application/json'
        # quoted quote
        with patch.object(urllib3.PoolManager, 'request') as mock_request:
            payload = (
                {
                    "foo'bar":
                        {
                            "foo\"bar":
                                1,
                        },
                }
            )
            with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
                body = post.request_body.RequestBody.content["application/json"].schema.validate(
                    payload,
                    configuration=self.schema_config
                )
                self.api.post(body=body)

    def test_quoted_tab_invalid_under_dependent_schema_fails(self):
        content_type = 'application/json'
        # quoted tab invalid under dependent schema
        with patch.object(urllib3.PoolManager, 'request') as mock_request:
            payload = (
                {
                    "foo\tbar":
                        1,
                    "a":
                        2,
                }
            )
            with self.assertRaises((unit_test_api.ApiValueError, unit_test_api.ApiTypeError)):
                body = post.request_body.RequestBody.content["application/json"].schema.validate(
                    payload,
                    configuration=self.schema_config
                )
                self.api.post(body=body)

if __name__ == '__main__':
    unittest.main()
