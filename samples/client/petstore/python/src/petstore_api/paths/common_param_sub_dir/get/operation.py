# coding: utf-8

"""
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from petstore_api import api_client
from petstore_api.shared_imports.operation_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]

from .. import path
from .responses import response_200
from .parameters import parameter_0
from ..parameters import parameter_0 as path_item_parameter_0
from .path_parameters import PathParameters, PathParametersDictInput, PathParametersDict
from .query_parameters import QueryParameters, QueryParametersDictInput, QueryParametersDict
query_parameter_classes = (
    parameter_0.Parameter0,
)
path_parameter_classes = (
    path_item_parameter_0.Parameter0,
)


__StatusCodeToResponse = typing.TypedDict(
    '__StatusCodeToResponse',
    {
        '200': typing.Type[response_200._200],
    }
)
_status_code_to_response: __StatusCodeToResponse = {
    '200': response_200._200,
}
_non_error_status_codes = frozenset({
    '200',
})


class BaseApi(api_client.Api):
    @typing.overload
    def _get_common_param(
        self,
        path_params: typing.Union[
            PathParametersDictInput,
            PathParametersDict
        ],
        query_params: typing.Union[
            QueryParametersDictInput,
            QueryParametersDict,
            None
        ] = None,
        *,
        skip_deserialization: typing.Literal[False] = False,
        server_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, float, typing.Tuple]] = None,
    ) -> response_200.ApiResponse: ...

    @typing.overload
    def _get_common_param(
        self,
        path_params: typing.Union[
            PathParametersDictInput,
            PathParametersDict
        ],
        query_params: typing.Union[
            QueryParametersDictInput,
            QueryParametersDict,
            None
        ] = None,
        *,
        skip_deserialization: typing.Literal[True],
        server_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, float, typing.Tuple]] = None,
    ) -> api_response.ApiResponseWithoutDeserialization: ...

    def _get_common_param(
        self,
        path_params: typing.Union[
            PathParametersDictInput,
            PathParametersDict
        ],
        query_params: typing.Union[
            QueryParametersDictInput,
            QueryParametersDict,
            None
        ] = None,
        *,
        skip_deserialization: bool = False,
        server_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, float, typing.Tuple]] = None,
    ):
        """
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        path_params = PathParameters.validate(
            path_params,
            configuration=self.api_client.schema_configuration
        )
        if query_params is not None:
            query_params = QueryParameters.validate(
                query_params,
                configuration=self.api_client.schema_configuration
            )
        used_path, query_params_suffix = self._get_used_path(
            path,
            path_parameters=path_parameter_classes,
            path_params=path_params,
            query_parameters=query_parameter_classes,
            query_params=query_params,
            skip_validation=True
        )
        # TODO add cookie handling
        host = self.api_client.configuration.get_server_url(
            "servers", server_index
        )

        raw_response = self.api_client.call_api(
            resource_path=used_path,
            query_params_suffix=query_params_suffix,
            method='get',
            host=host,
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


class GetCommonParam(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId.snakeCase fn names
    get_common_param = BaseApi._get_common_param


class ApiForGet(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names
    get = BaseApi._get_common_param
