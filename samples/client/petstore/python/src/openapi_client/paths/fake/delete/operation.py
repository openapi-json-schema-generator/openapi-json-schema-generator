# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose.  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from openapi_client import api_client, security_schemes
from openapi_client.shared_imports.operation_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]

from .. import path
from .responses import response_200
from .parameters import (
    parameter_0,
    parameter_1,
    parameter_2,
    parameter_3,
    parameter_4,
    parameter_5,
)
from .security import security_requirement_object_0
from .query_parameters import QueryParameters, QueryParametersDictInput, QueryParametersDict
from .header_parameters import HeaderParameters, HeaderParametersDictInput, HeaderParametersDict
query_parameter_classes = (
    parameter_0.Parameter0,
    parameter_2.Parameter2,
    parameter_3.Parameter3,
    parameter_5.Parameter5,
)
header_parameter_classes = (
    parameter_1.Parameter1,
    parameter_4.Parameter4,
)

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
    def _group_parameters(
        self,
        query_params: typing.Union[
            QueryParametersDictInput,
            QueryParametersDict
        ],
        header_params: typing.Union[
            HeaderParametersDictInput,
            HeaderParametersDict
        ],
        *,
        skip_deserialization: typing.Literal[False] = False,
        security_index: typing.Optional[int] = None,
        server_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, float, typing.Tuple]] = None,
    ) -> response_200.ApiResponse: ...

    @typing.overload
    def _group_parameters(
        self,
        query_params: typing.Union[
            QueryParametersDictInput,
            QueryParametersDict
        ],
        header_params: typing.Union[
            HeaderParametersDictInput,
            HeaderParametersDict
        ],
        *,
        skip_deserialization: typing.Literal[True],
        security_index: typing.Optional[int] = None,
        server_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, float, typing.Tuple]] = None,
    ) -> api_response.ApiResponseWithoutDeserialization: ...

    def _group_parameters(
        self,
        query_params: typing.Union[
            QueryParametersDictInput,
            QueryParametersDict
        ],
        header_params: typing.Union[
            HeaderParametersDictInput,
            HeaderParametersDict
        ],
        *,
        skip_deserialization: bool = False,
        security_index: typing.Optional[int] = None,
        server_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, float, typing.Tuple]] = None,
    ):
        """
        Fake endpoint to test group parameters (optional)
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        query_params = QueryParameters.validate(
            query_params,
            configuration=self.api_client.schema_configuration
        )
        header_params = HeaderParameters.validate(
            header_params,
            configuration=self.api_client.schema_configuration
        )
        used_path, query_params_suffix = self._get_used_path(
            path,
            query_parameters=query_parameter_classes,
            query_params=query_params,
            skip_validation=True
        )
        headers = self._get_headers(
            header_parameters=header_parameter_classes,
            header_params=header_params,
            skip_validation=True
        )
        # TODO add cookie handling
        host = self.api_client.configuration.get_server_url(
            "servers", server_index
        )
        security_requirement_object = self.api_client.configuration.get_security_requirement_object(
            "paths//fake/delete/security",
            _security,
            security_index
        )

        raw_response = self.api_client.call_api(
            resource_path=used_path,
            query_params_suffix=query_params_suffix,
            method='delete',
            host=host,
            headers=headers,
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


class GroupParameters(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId.snakeCase fn names
    group_parameters = BaseApi._group_parameters


class ApiForDelete(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names
    delete = BaseApi._group_parameters
