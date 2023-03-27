# coding: utf-8

"""


    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

import unittest
from unittest.mock import patch

import urllib3

import this_package
from this_package.paths.path_with_two_explicit_security.get import operation as get  # noqa: E501
from this_package import schemas, api_client
from this_package.configurations import api_configuration, schema_configuration
from this_package.components.security_schemes import security_scheme_api_key
from this_package.components.security_schemes import security_scheme_bearer_test

from .. import ApiTestMixin


class TestGet(ApiTestMixin, unittest.TestCase):
    """
    Get unit test stubs
        path with two explicit security  # noqa: E501
    """
    security_scheme_info: api_configuration.SecuritySchemeInfo = {
        # security_scheme_info for security_index 0
        "api_key": security_scheme_api_key.ApiKey(
            api_key='sampleApiKeyValue'
        ),
        # security_scheme_info for security_index 1
        "bearer_test": security_scheme_bearer_test.BearerTest(
            access_token='someAccessToken'
        ),
    }

    api_config = api_configuration.ApiConfiguration(
        security_scheme_info=security_scheme_info
    )
    schema_config = schema_configuration.SchemaConfiguration()
    used_api_client = api_client.ApiClient(configuration=api_config, schema_config=schema_config)
    api = get.ApiForGet(api_client=used_api_client)  # noqa: E501

    @patch.object(urllib3.PoolManager, 'request')
    def test_endpoint_call_contains_security_index0(self, mock_request):
        mock_request.return_value = self.response(b'')

        api = get.ApiForGet(api_client=self.used_api_client)
        api_response = api.get()
        self.assert_pool_manager_request_called_with(
            mock_request,
            f'http://localhost:3000/pathWithTwoExplicitSecurity',
            method='GET',
            additional_headers={'api_key': 'sampleApiKeyValue'}
        )

        assert isinstance(api_response.response, urllib3.HTTPResponse)
        assert isinstance(api_response.body, schemas.Unset)
        assert isinstance(api_response.headers, schemas.Unset)
        assert api_response.response.status == 200

    @patch.object(urllib3.PoolManager, 'request')
    def test_endpoint_call_contains_security_index1(self, mock_request):
        mock_request.return_value = self.response(b'')

        api = get.ApiForGet(api_client=self.used_api_client)
        api_response = api.get(security_index=1)
        self.assert_pool_manager_request_called_with(
            mock_request,
            f'http://localhost:3000/pathWithTwoExplicitSecurity',
            method='GET',
            additional_headers={'Authorization': 'Bearer someAccessToken'}
        )

        assert isinstance(api_response.response, urllib3.HTTPResponse)
        assert isinstance(api_response.body, schemas.Unset)
        assert isinstance(api_response.headers, schemas.Unset)
        assert api_response.response.status == 200

    @patch.object(urllib3.PoolManager, 'request')
    def test_endpoint_call_contains_security_index1_from_endpoint_config(self, mock_request):
        mock_request.return_value = self.response(b'')

        api_config = api_configuration.ApiConfiguration(
            security_scheme_info=self.security_scheme_info,
            security_index_info={'paths//pathWithTwoExplicitSecurity/get/security': 1}
        )
        used_api_client = api_client.ApiClient(configuration=api_config)
        api = get.ApiForGet(api_client=used_api_client)
        api_response = api.get()
        self.assert_pool_manager_request_called_with(
            mock_request,
            f'http://localhost:3000/pathWithTwoExplicitSecurity',
            method='GET',
            additional_headers={'Authorization': 'Bearer someAccessToken'}
        )

        assert isinstance(api_response.response, urllib3.HTTPResponse)
        assert isinstance(api_response.body, schemas.Unset)
        assert isinstance(api_response.headers, schemas.Unset)
        assert api_response.response.status == 200

if __name__ == '__main__':
    unittest.main()
