# coding: utf-8

"""


    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from urllib3._collections import HTTPHeaderDict

from petstore_api import api_client, exceptions
import datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from petstore_api import schemas  # noqa: F401

from .. import path
from .responses import (
    response_1xx,
    response_200,
    response_2xx,
    response_3xx,
    response_4xx,
    response_5xx,
)



__StatusCodeToResponse = typing_extensions.TypedDict(
    '__StatusCodeToResponse',
    {
        '200': typing.Type[response_200.ResponseFor200],
    }
)
_status_code_to_response: __StatusCodeToResponse = {
    '200': response_200.ResponseFor200,
}
__RangedStatusCodeToResponse = typing_extensions.TypedDict(
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

_all_accept_content_types = (
    "application/json",
)


class BaseApi(api_client.Api):
    @typing.overload
    def _wild_card_responses(
        self,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        server_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        response_200.ResponseFor200.response_cls,
        response_2xx.ResponseFor2XX.response_cls,
        response_3xx.ResponseFor3XX.response_cls,
    ]: ...

    @typing.overload
    def _wild_card_responses(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        server_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def _wild_card_responses(
        self,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        server_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        response_200.ResponseFor200.response_cls,
        response_2xx.ResponseFor2XX.response_cls,
        response_3xx.ResponseFor3XX.response_cls,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def _wild_card_responses(
        self,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        server_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        """
        operation with wildcard responses
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path

        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        host = self.api_client.configuration.get_server_url(
            'servers', server_index
        )

        response = self.api_client.call_api(
            resource_path=used_path,
            method='get',
            host=host,
            headers=_headers,
            stream=stream,
            timeout=timeout,
        )

        if skip_deserialization:
            api_response = api_client.ApiResponseWithoutDeserialization(response=response)
        else:
            status = str(response.status)
            ranged_response_status_code = status[0]
            if status in _status_code_to_response:
                status: typing_extensions.Literal[
                    '200',
                ]
                api_response = _status_code_to_response[status].deserialize(
                    response, self.api_client.schema_configuration)
            elif ranged_response_status_code in _ranged_status_code_to_response:
                ranged_response_status_code: typing_extensions.Literal[
                    '1',
                    '2',
                    '3',
                    '4',
                    '5',
                ]
                api_response = _ranged_status_code_to_response[ranged_response_status_code].deserialize(
                    response, self.api_client.schema_configuration)
            else:
                api_response = api_client.ApiResponseWithoutDeserialization(response=response)

        if not 200 <= response.status <= 399:
            raise exceptions.ApiException(
                status=response.status,
                reason=response.reason,
                api_response=api_response
            )

        return api_response


class WildCardResponses(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId.snakeCase fn names
    wild_card_responses = BaseApi._wild_card_responses


class ApiForGet(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names
    get = BaseApi._wild_card_responses
