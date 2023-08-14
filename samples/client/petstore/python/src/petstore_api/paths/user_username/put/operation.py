# coding: utf-8

"""
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from petstore_api import api_client, exceptions
from petstore_api.shared_imports.operation_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]
from petstore_api.components.schema import user

from .. import path
from .responses import (
    response_400,
    response_404,
)
from . import request_body
from .parameters import parameter_0
from .path_parameters import PathParameters, PathParametersDictInput, PathParametersDict
path_parameter_classes = (
    parameter_0.Parameter0,
)


__StatusCodeToResponse = typing.TypedDict(
    '__StatusCodeToResponse',
    {
        '400': typing.Type[response_400.ResponseFor400],
        '404': typing.Type[response_404.ResponseFor404],
    }
)
_status_code_to_response: __StatusCodeToResponse = {
    '400': response_400.ResponseFor400,
    '404': response_404.ResponseFor404,
}
_error_status_codes = frozenset({
    '400',
    '404',
})


class BaseApi(api_client.Api):
    @typing.overload
    def _update_user(
        self,
        body: typing.Union[
            user.UserDictInput,
            user.UserDict,
        ],
        path_params: typing.Union[
            PathParametersDictInput,
            PathParametersDict
        ],
        *,
        skip_deserialization: typing.Literal[False] = False,
        content_type: typing.Literal["application/json"] = "application/json",
        server_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, float, typing.Tuple]] = None,
    ) -> api_response.ApiResponseWithoutDeserialization: ...
    @typing.overload
    def _update_user(
        self,
        body: typing.Union[
            user.UserDictInput,
            user.UserDict,
        ],
        path_params: typing.Union[
            PathParametersDictInput,
            PathParametersDict
        ],
        *,
        skip_deserialization: typing.Literal[True],
        content_type: typing.Literal["application/json"] = "application/json",
        server_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, float, typing.Tuple]] = None,
    ) -> api_response.ApiResponseWithoutDeserialization: ...

    def _update_user(
        self,
        body: typing.Union[
            user.UserDictInput,
            user.UserDict,
        ],
        path_params: typing.Union[
            PathParametersDictInput,
            PathParametersDict
        ],
        *,
        skip_deserialization: bool = False,
        content_type: typing.Literal["application/json"] = "application/json",
        server_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, float, typing.Tuple]] = None,
    ):
        """
        Updated user
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        path_params = PathParameters.validate(path_params)
        used_path, query_params_suffix = self._get_used_path(
            path,
            path_parameters=path_parameter_classes,
            path_params=path_params,
            skip_validation=True
        )
        headers = self._get_headers()
        # TODO add cookie handling

        fields, serialized_body = self._get_fields_and_body(
            request_body=request_body.RequestBody,
            body=body,
            content_type=content_type,
            headers=headers
        )
        host = self.api_client.configuration.get_server_url(
            "servers", server_index
        )

        raw_response = self.api_client.call_api(
            resource_path=used_path,
            method='put',
            host=host,
            headers=headers,
            fields=fields,
            body=serialized_body,
            stream=stream,
            timeout=timeout,
        )

        if skip_deserialization:
            skip_deser_response = api_response.ApiResponseWithoutDeserialization(response=raw_response)
            self._verify_response_status(skip_deser_response)
            return skip_deser_response

        status = str(raw_response.status)
        if status in _error_status_codes:
            error_status_code = typing.cast(
                typing.Literal[
                    '400',
                    '404',
                ],
                status
            )
            error_response = _status_code_to_response[error_status_code].deserialize(
                raw_response, self.api_client.schema_configuration)
            raise exceptions.ApiException(
                status=error_response.response.status,
                reason=error_response.response.reason,
                api_response=error_response
            )

        response = api_response.ApiResponseWithoutDeserialization(response=raw_response)
        self._verify_response_status(response)
        return response


class UpdateUser(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId.snakeCase fn names
    update_user = BaseApi._update_user


class ApiForPut(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names
    put = BaseApi._update_user
