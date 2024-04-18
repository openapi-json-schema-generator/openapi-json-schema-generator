# coding: utf-8

"""
    OpenAPI Petstore
    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose.  # noqa: E501
    The version of the OpenAPI document: 1.0.0
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from openapi_client import api_client, exceptions
from openapi_client.shared_imports.operation_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]

from .. import path
from .responses import (
    response_1xx,
    response_200,
    response_2xx,
    response_3xx,
    response_4xx,
    response_5xx,
)


__StatusCodeToResponse = typing.TypedDict(
    '__StatusCodeToResponse',
    {
        '200': typing.Type[response_200.ResponseFor200],
    }
)
_status_code_to_response: __StatusCodeToResponse = {
    '200': response_200.ResponseFor200,
}
__RangedStatusCodeToResponse = typing.TypedDict(
    '__RangedStatusCodeToResponse',
    {
        '1': typing.Type[response_1xx.ResponseFor1XX],
        '2': typing.Type[response_2xx.ResponseFor2XX],
        '3': typing.Type[response_3xx.ResponseFor3XX],
        '4': typing.Type[response_4xx.ResponseFor4XX],
        '5': typing.Type[response_5xx.ResponseFor5XX],
    }
)
_ranged_status_code_to_response: __RangedStatusCodeToResponse = {
    '1': response_1xx.ResponseFor1XX,
    '2': response_2xx.ResponseFor2XX,
    '3': response_3xx.ResponseFor3XX,
    '4': response_4xx.ResponseFor4XX,
    '5': response_5xx.ResponseFor5XX,
}
_non_error_status_codes = frozenset({
    '200',
})
_non_error_ranged_status_codes = frozenset({
    '1',
    '2',
    '3',
})
_error_ranged_status_codes = frozenset({
    '4',
    '5',
})

_all_accept_content_types = (
    "application/json",
)


class BaseApi(api_client.Api):
    @typing.overload
    def _wild_card_responses(
        self,
        *,
        skip_deserialization: typing.Literal[False] = False,
        accept_content_types: typing.Tuple[str, ...] = _all_accept_content_types,
        server_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, float, typing.Tuple]] = None,
    ) -> typing.Union[
        response_1xx.ApiResponse,
        response_2xx.ApiResponse,
        response_200.ApiResponse,
        response_3xx.ApiResponse,
    ]: ...

    @typing.overload
    def _wild_card_responses(
        self,
        *,
        skip_deserialization: typing.Literal[True],
        accept_content_types: typing.Tuple[str, ...] = _all_accept_content_types,
        server_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, float, typing.Tuple]] = None,
    ) -> api_response.ApiResponseWithoutDeserialization: ...

    def _wild_card_responses(
        self,
        *,
        skip_deserialization: bool = False,
        accept_content_types: typing.Tuple[str, ...] = _all_accept_content_types,
        server_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, float, typing.Tuple]] = None,
    ):
        """
        operation with wildcard responses
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path
        headers = self._get_headers(accept_content_types=accept_content_types)
        # TODO add cookie handling
        host = self.api_client.configuration.get_server_url(
            "servers", server_index
        )

        raw_response = self.api_client.call_api(
            resource_path=used_path,
            method='get',
            host=host,
            headers=headers,
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

        ranged_response_status_code = str(raw_response.status)[0]
        if ranged_response_status_code in _non_error_ranged_status_codes:
            ranged_status_code = typing.cast(
                typing.Literal[
                    '1',
                    '2',
                    '3',
                ],
                ranged_response_status_code
            )
            return _ranged_status_code_to_response[ranged_status_code].deserialize(
                raw_response, self.api_client.schema_configuration)
        elif ranged_response_status_code in _error_ranged_status_codes:
            error_ranged_status_code = typing.cast(
                typing.Literal[
                    '4',
                    '5',
                ],
                ranged_response_status_code
            )
            error_response = _ranged_status_code_to_response[error_ranged_status_code].deserialize(
                raw_response, self.api_client.schema_configuration)
            raise exceptions.ApiException(
                status=error_response.response.status,
                reason=error_response.response.reason,
                api_response=error_response
            )

        response = api_response.ApiResponseWithoutDeserialization(response=raw_response)
        self._verify_response_status(response)
        return response


class WildCardResponses(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId.snakeCase fn names
    wild_card_responses = BaseApi._wild_card_responses


class ApiForGet(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names
    get = BaseApi._wild_card_responses
