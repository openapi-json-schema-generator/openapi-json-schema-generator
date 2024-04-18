# coding: utf-8

"""
    security-test
    No description provided (generated by Openapi JSON Schema Generator https://github.com/openapi-json-schema-tools/openapi-json-schema-generator)  # noqa: E501
    The version of the OpenAPI document: 1.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from openapi_client import api_client, security_schemes
from openapi_client.shared_imports.operation_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]

from .. import path
from .responses import response_200
from .security import security_requirement_object_0

_security: typing.List[security_schemes.SecurityRequirementObject] = [
    security_requirement_object_0.security_requirement_object,
]


__StatusCodeToResponse = typing.TypedDict(
    '__StatusCodeToResponse',
    {
        '200': typing.Type[response_200.ResponseFor200],
    }
)
_status_code_to_response: __StatusCodeToResponse = {
    '200': response_200.ResponseFor200,
}
_non_error_status_codes = frozenset({
    '200',
})


class BaseApi(api_client.Api):
    @typing.overload
    def _path_with_one_explicit_security(
        self,
        *,
        skip_deserialization: typing.Literal[False] = False,
        security_index: typing.Optional[int] = None,
        server_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, float, typing.Tuple]] = None,
    ) -> response_200.ApiResponse: ...

    @typing.overload
    def _path_with_one_explicit_security(
        self,
        *,
        skip_deserialization: typing.Literal[True],
        security_index: typing.Optional[int] = None,
        server_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, float, typing.Tuple]] = None,
    ) -> api_response.ApiResponseWithoutDeserialization: ...

    def _path_with_one_explicit_security(
        self,
        *,
        skip_deserialization: bool = False,
        security_index: typing.Optional[int] = None,
        server_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, float, typing.Tuple]] = None,
    ):
        """
        path with one explicit security
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path
        # TODO add cookie handling
        host = self.api_client.configuration.get_server_url(
            "servers", server_index
        )
        security_requirement_object = self.api_client.configuration.get_security_requirement_object(
            "paths//pathWithOneExplicitSecurity/get/security",
            _security,
            security_index
        )

        raw_response = self.api_client.call_api(
            resource_path=used_path,
            method='get',
            host=host,
            security_requirement_object=security_requirement_object,
            stream=stream,
            timeout=timeout,
        )

        if skip_deserialization:
            skip_deser_response = api_response.ApiResponseWithoutDeserialization(response=raw_response)
            self._verify_response_status(skip_deser_response)
            return skip_deser_response

        status = str(raw_response.status)
        if status in _non_error_status_codes:
            status_code = typing.cast(
                typing.Literal[
                    '200',
                ],
                status
            )
            return _status_code_to_response[status_code].deserialize(
                raw_response, self.api_client.schema_configuration)

        response = api_response.ApiResponseWithoutDeserialization(response=raw_response)
        self._verify_response_status(response)
        return response


class PathWithOneExplicitSecurity(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId.snakeCase fn names
    path_with_one_explicit_security = BaseApi._path_with_one_explicit_security


class ApiForGet(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names
    get = BaseApi._path_with_one_explicit_security
